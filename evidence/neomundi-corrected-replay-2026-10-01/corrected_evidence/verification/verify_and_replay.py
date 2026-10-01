#!/usr/bin/env python3
import json, hashlib, pathlib, sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
payload_dir=ROOT/"payloads"
results=json.loads((ROOT/"evidence"/"NEOMUNDI_OGS_PRIVATE_PILOT_RESULTS_v0_1_1_CORRECTED.json").read_text())
receipts=json.loads((ROOT/"evidence"/"NEOMUNDI_OGS_CAOM_LITE_RECEIPT_BUNDLE_v0_1_1_CORRECTED.json").read_text())
result_by_file={x["file"]:x for x in results["results"]}
receipt_by_file={x["source_file"]:x for x in receipts["receipts"]}
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def classify(obj):
    m=obj["measurement"]; fv=m["factual_validity_signal"]["status"]; sv=m["semantic_variability_signal"]["status"]; types=m["risk_signal"]["types"]
    if m["measurement_status"]=="partial":
        return ("observation_only_requires_more_measurement","allow_observation_require_more_measurement","limited_use")
    if fv=="contradiction_or_overclaim_signal":
        return ("not_admissible_as_claim","no_bind_refuse_claim_or_action","no_bind")
    if fv=="supported_with_limitations":
        return ("limited_hypothesis_or_claim_candidate","allow_limited_hypothesis_no_action","limited_use")
    if sv=="elevated" and "uncertainty" in types:
        return ("requires_review","hold_for_review","hold")
    if fv=="fragile":
        return ("observation_only","allow_as_internal_observation","limited_use")
    raise ValueError("unmapped payload")
fail=[]
records=[]
for p in sorted(payload_dir.glob("*.json")):
    obj=json.loads(p.read_text(encoding="utf-8-sig"))
    observed=classify(obj)
    rr=result_by_file[p.name]; rc=receipt_by_file[p.name]
    expected=(rr["petunia"]["petunia_status"],rr["judicator"]["judicator_status"],rr["judicator"]["receipt_type"])
    digest=sha(p)
    ok=(observed==expected and digest==rr["input_hash"]==rc["input_hash"] and
        rc["petunia_status"]==observed[0] and rc["judicator_status"]==observed[1] and rc["receipt_type"]==observed[2])
    records.append({"file":p.name,"sha256":digest,"observed":observed,"expected":expected,"passed":ok})
    if not ok: fail.append(p.name)
report={"run_id":results["run_id"],"method":"same_payload_same_explicit_rules","cases":records,
        "passed":len(records)-len(fail),"failed":len(fail),"verdict":"PASS" if not fail else "FAIL"}
(ROOT/"evidence"/"NEOMUNDI_OGS_REPLAY_EXECUTION_RESULT_v0_1_1.json").write_text(json.dumps(report,indent=2)+"\n")
print(json.dumps(report,indent=2))
sys.exit(1 if fail else 0)
