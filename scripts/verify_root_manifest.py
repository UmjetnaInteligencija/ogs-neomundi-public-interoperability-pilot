#!/usr/bin/env python3
"""Check the preserved 37-file public pack without rewriting its manifest."""
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
# Pin the historical manifest itself so deleting entries cannot weaken this gate.
MANIFEST_SHA256 = "8062aa978d004494db374e6a00b341fd948019f0a347e0b65fe6bcf343fa908f"


def verify(root):
    raw = (root / "MANIFEST.json").read_bytes()
    if hashlib.sha256(raw).hexdigest() != MANIFEST_SHA256:
        raise ValueError("Preserved root manifest checksum mismatch")
    manifest = json.loads(raw)
    entries = manifest["files"]
    if manifest["artifact_count"] != 37 or len(entries) != 37:
        raise ValueError("Expected exactly 37 root manifest entries")
    errors = []
    for entry in entries:
        path = root / entry["path"]
        try:
            if path.is_symlink() or not path.is_file():
                raise ValueError("missing or non-regular file")
            if not path.resolve().is_relative_to(root.resolve()):
                raise ValueError("path escapes repository")
            data = path.read_bytes()
            if len(data) != entry["bytes"]:
                errors.append(f"{entry['path']}: byte count mismatch")
            if hashlib.sha256(data).hexdigest() != entry["sha256"]:
                errors.append(f"{entry['path']}: SHA-256 mismatch")
        except (OSError, ValueError) as exc:
            errors.append(f"{entry['path']}: {exc}")
    if errors:
        raise ValueError("\n".join(errors))
    print("PASS: preserved root manifest checksum and all 37 file hashes and byte counts.")
    print("Scope: listed historical artifacts; additive files are not added to this manifest.")


if __name__ == "__main__":
    try:
        verify(ROOT)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
