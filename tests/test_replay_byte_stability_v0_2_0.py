"""Stdlib regression controls. CRLF emulation is not a Windows execution."""
import ast
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]
HISTORY = Path("evidence/neomundi-corrected-replay-2026-10-01")
FIXTURE = HISTORY / "corrected_evidence"
OLD = FIXTURE / "verification/verify_and_replay.py"
NEW = Path("scripts/verify_and_replay_v0_2_0.py")
RESULT = FIXTURE / "evidence/NEOMUNDI_OGS_REPLAY_EXECUTION_RESULT_v0_1_1.json"
EXPECTED_SHA = "a94d4ce69d36baac79c243acc035ca16df6d253ce42859e5f0ba4158bc288bf8"
AUDIT = os.environ.get("REPLAY_AUDIT_DIR")

# Run the real script with stdlib text streams, overriding only unspecified
# writer newline defaults. This simulates Windows newline translation on any
# host; it does not simulate Windows paths, filesystem, or the Windows OS.
CRLF_RUNNER = '''import pathlib, runpy, sys
original_open = pathlib.Path.open
def simulated_open(self, mode="r", buffering=-1, encoding=None, errors=None, newline=None):
    if any(flag in mode for flag in "wax") and "b" not in mode and newline is None:
        newline = "\\r\\n"
    return original_open(self, mode, buffering, encoding, errors, newline)
pathlib.Path.open = simulated_open
sys.argv = sys.argv[1:]
runpy.run_path(sys.argv[0], run_name="__main__")
'''


def sha(data):
    return hashlib.sha256(data).hexdigest()


def inventory(root):
    return {p.relative_to(root).as_posix(): {"bytes": p.stat().st_size,
            "sha256": sha(p.read_bytes())}
            for p in sorted(root.rglob("*")) if p.is_file()}


class ReplayByteStability(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="ogs-writer-test-")
        self.addCleanup(self.tmp.cleanup)
        self.work = Path(self.tmp.name)
        self.repo = self.work / "repo"
        (self.repo / "scripts").mkdir(parents=True)
        shutil.copytree(REPO / HISTORY, self.repo / HISTORY)
        shutil.copyfile(REPO / NEW, self.repo / NEW)
        self.output = self.work / "replay_v0_2_0.json"
        self.preserved = (REPO / RESULT).read_bytes()
        self.before = inventory(self.repo / HISTORY)

    def run_writer(self, *, old=False, crlf=False, extra=None, output=None, env=None):
        target = self.repo / (OLD if old else NEW)
        destination = self.repo / RESULT if old else (output or self.output)
        command = [sys.executable]
        if crlf:
            command += ["-c", CRLF_RUNNER]
        command += [str(target)]
        command += ([] if old else ["--output", str(destination)]) if extra is None else extra
        proc = subprocess.run(command, cwd=self.work, capture_output=True,
                              env={**os.environ, **(env or {})})
        if AUDIT:
            folder = Path(AUDIT) / self.id().split(".")[-1]
            folder.mkdir(parents=True, exist_ok=True)
            index = len(list(folder.glob("*.command.json")))
            prefix = folder / f"{index:02d}"
            prefix.with_suffix(".stdout.bin").write_bytes(proc.stdout)
            prefix.with_suffix(".stderr.bin").write_bytes(proc.stderr)
            entry = {"argv": command, "cwd": str(self.work), "exit_code": proc.returncode,
                     "newline_mode": "SIMULATED_CRLF_DEFAULT" if crlf else "NATIVE",
                     "environment_overrides": env or {}}
            if destination.is_file():
                data = destination.read_bytes()
                prefix.with_suffix(".artifact.bin").write_bytes(data)
                entry["artifact"] = {"path": str(destination), "bytes": len(data),
                                     "sha256": sha(data), "lf_count": data.count(b"\n"),
                                     "cr_count": data.count(b"\r")}
            prefix.with_suffix(".command.json").write_bytes(
                (json.dumps(entry, indent=2) + "\n").encode("utf-8"))
        return proc, destination

    def read_json(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def write_json(self, path, value):
        path.write_bytes((json.dumps(value, indent=2) + "\n").encode("utf-8"))

    def test_01_preserved_reference(self):
        self.assertEqual(len(self.preserved), 2298)
        self.assertEqual(sha(self.preserved), EXPECTED_SHA)
        self.assertEqual(self.preserved.count(b"\n"), 84)
        self.assertNotIn(b"\r", self.preserved)

    def test_02_native_original_and_successor(self):
        original, old_output = self.run_writer(old=True)
        successor, output = self.run_writer()
        self.assertEqual((original.returncode, successor.returncode), (0, 0))
        self.assertEqual(output.read_bytes(), self.preserved)
        # Original native output can be CRLF on Windows; compare semantics.
        self.assertEqual(self.read_json(old_output), self.read_json(output))
        report = self.read_json(output)
        self.assertEqual((len(report["cases"]), report["passed"], report["failed"]), (5, 5, 0))
        self.assertEqual(report["verdict"], "PASS")

    def test_03_simulated_crlf_original_negative(self):
        proc, output = self.run_writer(old=True, crlf=True)
        data = output.read_bytes()
        self.assertEqual(proc.returncode, 0)
        self.assertEqual(len(data), 2382)
        self.assertEqual(data.count(b"\r\n"), 84)
        self.assertNotEqual(sha(data), EXPECTED_SHA)
        self.assertEqual(data.replace(b"\r\n", b"\n"), self.preserved)
        self.assertEqual(json.loads(data), json.loads(self.preserved))

    def test_04_simulated_crlf_successor_positive(self):
        proc, output = self.run_writer(crlf=True)
        self.assertEqual(proc.returncode, 0)
        self.assertEqual(output.read_bytes(), self.preserved)
        self.assertNotIn(b"\r", output.read_bytes())

    def test_05_posthoc_crlf_transformation_negative(self):
        transformed = self.preserved.replace(b"\n", b"\r\n")
        self.assertEqual(len(transformed), 2382)
        self.assertNotEqual(sha(transformed), EXPECTED_SHA)
        self.assertEqual(json.loads(transformed), json.loads(self.preserved))

    def test_06_repeat_and_locale_stability(self):
        for index, env in enumerate(({}, {"PYTHONUTF8": "0", "LC_ALL": "C"},
                                      {"PYTHONUTF8": "1"})):
            with self.subTest(environment=env):
                proc, output = self.run_writer(output=self.work / f"repeat-{index}.json", env=env)
                self.assertEqual(proc.returncode, 0)
                self.assertEqual(output.read_bytes(), self.preserved)

    def test_07_each_classification_mismatch_is_rejected(self):
        path = self.repo / FIXTURE / "evidence/NEOMUNDI_OGS_PRIVATE_PILOT_RESULTS_v0_1_1_CORRECTED.json"
        original = self.read_json(path)
        for index in range(5):
            with self.subTest(case=index + 1):
                value = json.loads(json.dumps(original))
                value["results"][index]["petunia"]["petunia_status"] = "deliberate_negative_control"
                self.write_json(path, value)
                proc, output = self.run_writer(output=self.work / f"mismatch-{index}.json")
                self.assertEqual(proc.returncode, 1)
                report = self.read_json(output)
                self.assertEqual((report["passed"], report["failed"], report["verdict"]), (4, 1, "FAIL"))
                original_proc, original_output = self.run_writer(old=True)
                self.assertEqual(original_proc.returncode, 1)
                self.assertEqual(self.read_json(original_output), report)

    def test_08_payload_byte_tamper_is_rejected(self):
        path = next((self.repo / FIXTURE / "payloads").glob("*.json"))
        path.write_bytes(path.read_bytes() + b" ")
        proc, output = self.run_writer()
        self.assertEqual(proc.returncode, 1)
        self.assertEqual(self.read_json(output)["failed"], 1)
        original_proc, original_output = self.run_writer(old=True)
        self.assertEqual(original_proc.returncode, 1)
        self.assertEqual(self.read_json(original_output), self.read_json(output))

    def test_09_receipt_hash_tamper_is_rejected(self):
        path = self.repo / FIXTURE / "evidence/NEOMUNDI_OGS_CAOM_LITE_RECEIPT_BUNDLE_v0_1_1_CORRECTED.json"
        value = self.read_json(path)
        value["receipts"][0]["input_hash"] = "0" * 64
        self.write_json(path, value)
        proc, output = self.run_writer()
        self.assertEqual(proc.returncode, 1)
        self.assertEqual(self.read_json(output)["failed"], 1)
        original_proc, original_output = self.run_writer(old=True)
        self.assertEqual(original_proc.returncode, 1)
        self.assertEqual(self.read_json(original_output), self.read_json(output))

    def test_10_historical_destination_is_rejected(self):
        for relative in (RESULT, HISTORY / "new-result.json"):
            with self.subTest(path=str(relative)):
                proc, _ = self.run_writer(output=self.repo / relative)
                self.assertEqual(proc.returncode, 2)
        self.assertEqual(inventory(self.repo / HISTORY), self.before)

    def test_11_existing_output_is_not_replaced(self):
        self.output.write_bytes(b"preserve me\r\n")
        proc, output = self.run_writer()
        self.assertEqual(proc.returncode, 2)
        self.assertEqual(output.read_bytes(), b"preserve me\r\n")

    def test_12_output_required_and_version(self):
        proc, _ = self.run_writer(extra=[])
        self.assertEqual(proc.returncode, 2)
        proc, _ = self.run_writer(extra=["--version"])
        self.assertEqual(proc.returncode, 0)
        self.assertEqual(proc.stdout.strip(), b"0.2.0")
        self.assertFalse(self.output.exists())

    def test_13_history_is_unchanged_by_successor(self):
        proc, _ = self.run_writer()
        self.assertEqual(proc.returncode, 0)
        self.assertEqual(inventory(self.repo / HISTORY), self.before)

    def test_14_rule_function_is_identical(self):
        def classification(path):
            tree = ast.parse(path.read_text(encoding="utf-8"))
            return ast.dump(next(n for n in tree.body if isinstance(n, ast.FunctionDef)
                                 and n.name == "classify"), include_attributes=False)
        self.assertEqual(classification(REPO / OLD), classification(REPO / NEW))

    def test_15_utf8_input_under_ascii_locale(self):
        path = self.repo / FIXTURE / "evidence/NEOMUNDI_OGS_PRIVATE_PILOT_RESULTS_v0_1_1_CORRECTED.json"
        value = self.read_json(path)
        value["run_id"] = "UTF8-é-č-Ω-漢字"
        path.write_bytes((json.dumps(value, ensure_ascii=False) + "\n").encode("utf-8"))
        proc, output = self.run_writer(env={"PYTHONUTF8": "0", "LC_ALL": "C"})
        self.assertEqual(proc.returncode, 0)
        self.assertEqual(self.read_json(output)["run_id"], value["run_id"])
        self.assertNotIn(b"\r", output.read_bytes())
        output.read_bytes().decode("utf-8", errors="strict")


if __name__ == "__main__":
    unittest.main(verbosity=2)
