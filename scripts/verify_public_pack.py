#!/usr/bin/env python3
from pathlib import Path
import json, hashlib, sys

ROOT = Path(__file__).resolve().parents[1]

def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))

def fail(msg):
    print(f"FAIL: {msg}")
    raise SystemExit(1)

cases = ["001", "004"]
for n in cases:
    signal = load(f"sample_objects/NM-OBS-{n}.json")
    gov = load(f"sample_objects/OGS-GOV-{n}.json")
    rec = load(f"sample_objects/OGS-RCPT-{n}.json")
    rpl = load(f"sample_objects/OGS-RPL-{n}.json")
    if gov["parent_signal_id"] != signal["signal_id"]:
        fail(f"governance parent mismatch for {n}")
    if rec["source_signal_id"] != signal["signal_id"]:
        fail(f"receipt signal mismatch for {n}")
    if rec["governance_object_id"] != gov["object_id"]:
        fail(f"receipt governance mismatch for {n}")
    if rpl["source_signal_id"] != signal["signal_id"]:
        fail(f"replay signal mismatch for {n}")
    if rpl["governance_object_id"] != gov["object_id"]:
        fail(f"replay governance mismatch for {n}")
    if rpl["receipt_id"] != rec["receipt_id"]:
        fail(f"replay receipt mismatch for {n}")
    if signal["provenance"]["input_sha256"] != gov["source_input_sha256"]:
        fail(f"source hash mismatch for {n}")
    if gov["source_input_sha256"] != rec["source_input_sha256"]:
        fail(f"receipt source hash mismatch for {n}")
    if rec["external_action_allowed"] is not False or gov["external_action_allowed"] is not False:
        fail(f"external action allowed for {n}")
    if rpl["expected_classification"] != rpl["observed_classification"] or not rpl["passed"]:
        fail(f"replay mismatch for {n}")

agg = load("evidence/AGGREGATE_RESULTS.json")
if agg["processed_payloads"] != 5:
    fail("aggregate payload count")
if agg["external_action_allowed_count"] != 0:
    fail("aggregate external action count")
if agg["internal_replay"]["passed"] != 5 or agg["internal_replay"]["failed"] != 0:
    fail("aggregate replay count")

print("PASS: public object links, hashes, outcomes, and replay records are internally consistent.")
print("Evidence boundary: synthetic, internally verified, not independently reproduced, not production-derived.")
