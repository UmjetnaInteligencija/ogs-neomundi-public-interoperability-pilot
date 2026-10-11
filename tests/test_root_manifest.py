"""Exercise the real root-manifest CLI using disposable copies only."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RootManifestIntegrity(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="root-integrity-test-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.entries = json.loads((ROOT / "MANIFEST.json").read_text())["files"]
        for rel in ["MANIFEST.json", "scripts/verify_root_manifest.py"] + [e["path"] for e in self.entries]:
            target = self.root / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / rel, target)

    def run_verifier(self):
        return subprocess.run(
            [sys.executable, str(self.root / "scripts/verify_root_manifest.py")],
            capture_output=True, text=True, timeout=30,
        )

    def test_pristine_pack_passes(self):
        result = self.run_verifier()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_same_size_corruption_of_every_listed_file_fails(self):
        for entry in self.entries:
            with self.subTest(path=entry["path"]):
                p = self.root / entry["path"]
                original = p.read_bytes()
                try:
                    p.write_bytes(bytes([original[0] ^ 1]) + original[1:])
                    result = self.run_verifier()
                    self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                    self.assertIn(entry["path"] + ": SHA-256 mismatch", result.stderr)
                    self.assertNotIn("byte count mismatch", result.stderr)
                finally:
                    p.write_bytes(original)

    def test_appended_bytes_fail_hash_and_size(self):
        p = self.root / "README.md"
        p.write_bytes(p.read_bytes() + b"corrupt")
        result = self.run_verifier()
        self.assertEqual(result.returncode, 1)
        self.assertIn("README.md: byte count mismatch", result.stderr)
        self.assertIn("README.md: SHA-256 mismatch", result.stderr)

    def test_missing_file_fails(self):
        (self.root / "README.md").unlink()
        result = self.run_verifier()
        self.assertEqual(result.returncode, 1)
        self.assertIn("README.md: missing", result.stderr)

    def test_removing_manifest_entry_fails(self):
        p = self.root / "MANIFEST.json"
        manifest = json.loads(p.read_text())
        manifest["files"].pop()
        manifest["artifact_count"] -= 1
        p.write_text(json.dumps(manifest))
        result = self.run_verifier()
        self.assertEqual(result.returncode, 1)
        self.assertIn("manifest checksum mismatch", result.stderr)


if __name__ == "__main__":
    unittest.main()
