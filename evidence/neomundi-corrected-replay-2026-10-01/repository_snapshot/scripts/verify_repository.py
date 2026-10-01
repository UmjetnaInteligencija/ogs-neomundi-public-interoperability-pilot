#!/usr/bin/env python3
"""Verify repository integrity and illustrative public trajectories.

This script validates local file hashes and public-example consistency only. It does
not reproduce the private pilot, validate NeoMundi measurements, or establish
production safety, independent verification, or regulatory compliance.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_EXAMPLE_STATUS = "illustrative_public_example_not_historical_pilot_artifact"


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def canonical_without_digest(obj: dict[str, Any]) -> bytes:
    clone = json.loads(json.dumps(obj))
    if isinstance(clone.get("integrity"), dict):
        clone["integrity"].pop("digest", None)
    return json.dumps(clone, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def verify_object_digest(path: Path, obj: dict[str, Any]) -> None:
    integrity = obj.get("integrity")
    if not isinstance(integrity, dict):
        fail(f"{path.relative_to(ROOT)} lacks integrity object")
    recorded = integrity.get("digest")
    expected = hashlib.sha256(canonical_without_digest(obj)).hexdigest()
    if recorded != expected:
        fail(f"integrity mismatch in {path.relative_to(ROOT)}: {recorded} != {expected}")


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"cannot parse {path.relative_to(ROOT)}: {exc}")
    if not isinstance(data, dict):
        fail(f"{path.relative_to(ROOT)} must contain a JSON object")
    return data


def require(obj: dict[str, Any], keys: list[str], path: Path) -> None:
    missing = [k for k in keys if k not in obj]
    if missing:
        fail(f"{path.relative_to(ROOT)} missing required keys: {missing}")


def verify_manifest() -> int:
    manifest_path = ROOT / "MANIFEST.json"
    manifest = load_json(manifest_path)
    files = manifest.get("files")
    if not isinstance(files, list):
        fail("MANIFEST.json files must be a list")
    for entry in files:
        rel = entry.get("path")
        expected_hash = entry.get("sha256")
        expected_bytes = entry.get("bytes")
        path = ROOT / rel
        if not path.is_file():
            fail(f"manifest file missing: {rel}")
        actual_hash = sha256_file(path)
        if actual_hash != expected_hash:
            fail(f"manifest hash mismatch for {rel}")
        if path.stat().st_size != expected_bytes:
            fail(f"manifest byte-count mismatch for {rel}")
    sha_path = ROOT / "MANIFEST.sha256"
    if sha_path.is_file():
        recorded = sha_path.read_text(encoding="utf-8").strip().split()[0]
        actual = sha256_file(manifest_path)
        if recorded != actual:
            fail("MANIFEST.sha256 does not match MANIFEST.json")
    return len(files)


def verify_trajectory(folder: Path) -> None:
    paths = {
        "signal": folder / "neomundi_signal.json",
        "governance": folder / "ogs_governance_object.json",
        "receipt": folder / "governance_receipt.json",
        "replay": folder / "replay_record.json",
    }
    objs = {name: load_json(path) for name, path in paths.items()}
    for name, obj in objs.items():
        if obj.get("example_status") != EXPECTED_EXAMPLE_STATUS:
            fail(f"{paths[name].relative_to(ROOT)} is not explicitly labeled illustrative")
        verify_object_digest(paths[name], obj)

    signal, gov, receipt, replay = objs["signal"], objs["governance"], objs["receipt"], objs["replay"]
    require(signal, ["signal_id", "measurement_limitations", "integrity"], paths["signal"])
    require(gov, ["object_id", "parent_signal_id", "parent_signal_digest", "trajectory_id", "execution_status", "external_action_authorized", "integrity"], paths["governance"])
    require(receipt, ["receipt_id", "source_signal_id", "source_signal_digest", "governance_object_id", "governance_object_digest", "decision", "external_action_authorized", "integrity"], paths["receipt"])
    require(replay, ["replay_id", "source_signal_id", "source_signal_digest", "governance_object_id", "governance_object_digest", "receipt_id", "receipt_digest", "replay_verdict", "historical_evidence", "external_action_authorized", "integrity"], paths["replay"])

    if gov["parent_signal_id"] != signal["signal_id"] or gov["parent_signal_digest"] != signal["integrity"]["digest"]:
        fail(f"governance object in {folder.name} does not bind the signal")
    if receipt["source_signal_id"] != signal["signal_id"] or receipt["source_signal_digest"] != signal["integrity"]["digest"]:
        fail(f"receipt in {folder.name} does not bind the signal")
    if receipt["governance_object_id"] != gov["object_id"] or receipt["governance_object_digest"] != gov["integrity"]["digest"]:
        fail(f"receipt in {folder.name} does not bind the governance object")
    if replay["source_signal_id"] != signal["signal_id"] or replay["source_signal_digest"] != signal["integrity"]["digest"]:
        fail(f"replay in {folder.name} does not bind the signal")
    if replay["governance_object_id"] != gov["object_id"] or replay["governance_object_digest"] != gov["integrity"]["digest"]:
        fail(f"replay in {folder.name} does not bind the governance object")
    if replay["receipt_id"] != receipt["receipt_id"] or replay["receipt_digest"] != receipt["integrity"]["digest"]:
        fail(f"replay in {folder.name} does not bind the receipt")
    if replay["original_decision"] != replay["replayed_decision"] or replay["replay_verdict"] != "REPRODUCED":
        fail(f"public example replay in {folder.name} did not reproduce")
    if replay.get("historical_evidence") is not False:
        fail(f"public example in {folder.name} is incorrectly labeled historical evidence")
    if any(obj.get("external_action_authorized") is not False for obj in [gov, receipt, replay]):
        fail(f"public example in {folder.name} authorizes an external action")


def main() -> None:
    manifest_count = verify_manifest()

    json_count = 0
    for path in ROOT.rglob("*.json"):
        load_json(path)
        json_count += 1

    folders = [
        ROOT / "sample_objects" / "trajectory_limited_use",
        ROOT / "sample_objects" / "trajectory_no_bind",
    ]
    for folder in folders:
        verify_trajectory(folder)

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    boundary = (ROOT / "docs" / "PUBLIC_CLAIM_BOUNDARY.md").read_text(encoding="utf-8")
    required_phrases = [
        "synthetic, internally verified",
        "not independently reproduced or production-derived",
        "No external action was authorized",
    ]
    for phrase in required_phrases:
        if phrase not in readme and phrase not in boundary:
            fail(f"required claim-boundary phrase missing: {phrase}")

    print(f"Manifest entries: {manifest_count} verified")
    print(f"JSON documents: {json_count} parsed")
    print(f"Illustrative trajectories: {len(folders)} verified")
    print("External execution authorizations in examples: 0")
    print("Claim boundary: present")
    print("Scope note: public repository integrity and illustrative examples only")
    print("Repository validation: PASS")


if __name__ == "__main__":
    main()
