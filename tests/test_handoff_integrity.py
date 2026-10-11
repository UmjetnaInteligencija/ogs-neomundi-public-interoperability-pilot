"""Challenge the unchanged handoff verifier in isolated temporary copies."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
HANDOFF = ROOT / "evidence/neomundi-corrected-replay-2026-10-01"
PAYLOAD = "corrected_evidence/payloads/01_stable_but_fragile.json"
RECEIPTS = "corrected_evidence/evidence/NEOMUNDI_OGS_CAOM_LITE_RECEIPT_BUNDLE_v0_1_1_CORRECTED.json"
ARCHIVE = "source_archives/NeoMundi_OGS_Private_Pilot_v0.1_Synthetic_Payloads.zip"


class HandoffIntegrity(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="handoff-integrity-test-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / "handoff"
        shutil.copytree(HANDOFF, self.root)

    def run_verifier(self):
        env = dict(os.environ, PYTHONOPTIMIZE="0", PYTHONDONTWRITEBYTECODE="1")
        return subprocess.run(
            [sys.executable, str(self.root / "verify_handoff.py")],
            capture_output=True, text=True, timeout=30, env=env,
        )

    def assert_rejected(self, expected):
        result = self.run_verifier()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(expected, result.stderr)

    def rehash_test_copy(self, rel):
        # Deliberately repair outer checksums in THIS TEMP COPY to reach deeper
        # binding/replay checks. Never changes a repository evidence artifact.
        p = self.root / "HANDOFF_MANIFEST.json"
        manifest = json.loads(p.read_text())
        data = (self.root / rel).read_bytes()
        entry = next(e for e in manifest["files"] if e["path"] == rel)
        entry.update(bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
        p.write_text(json.dumps(manifest))
        (self.root / "HANDOFF_MANIFEST.sha256").write_text(
            hashlib.sha256(p.read_bytes()).hexdigest() + "  HANDOFF_MANIFEST.json\n"
        )

    def test_pristine_handoff_passes(self):
        result = self.run_verifier()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("5 passed, 0 failed", result.stdout)

    def test_corrupted_payload_receipts_and_archive_fail(self):
        for rel in [PAYLOAD, RECEIPTS, ARCHIVE]:
            with self.subTest(path=rel):
                p = self.root / rel
                original = p.read_bytes()
                try:
                    p.write_bytes(bytes([original[0] ^ 1]) + original[1:])
                    self.assert_rejected(rel)
                finally:
                    p.write_bytes(original)

    def test_missing_artifact_fails_inventory(self):
        (self.root / ARCHIVE).unlink()
        self.assert_rejected("File inventory changed")

    def test_extra_artifact_fails_inventory(self):
        (self.root / "unexpected.txt").write_text("unexpected")
        self.assert_rejected("File inventory changed")

    def test_manifest_checksum_corruption_fails(self):
        (self.root / "HANDOFF_MANIFEST.sha256").write_text("0" * 64)
        self.assert_rejected("Manifest checksum")

    def test_rehashed_wrong_receipt_binding_still_fails(self):
        p = self.root / RECEIPTS
        obj = json.loads(p.read_text())
        receipt = next(r for r in obj["receipts"] if r["source_file"] == Path(PAYLOAD).name)
        receipt["input_hash"] = "0" * 64
        p.write_text(json.dumps(obj))
        self.rehash_test_copy(RECEIPTS)
        self.assert_rejected(Path(PAYLOAD).name)

    def test_rehashed_wrong_replay_record_still_fails(self):
        rel = "fresh_verification/corrected_replay_result.json"
        p = self.root / rel
        obj = json.loads(p.read_text())
        obj["passed"] = 4
        p.write_text(json.dumps(obj))
        self.rehash_test_copy(rel)
        self.assert_rejected("Replay differs from recorded result")


if __name__ == "__main__":
    unittest.main()
