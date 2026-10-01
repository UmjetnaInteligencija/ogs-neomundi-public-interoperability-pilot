# NeoMundi × OGS Private Pilot v0.1 — Evidence Note

**Project:** Petunia × Judicator / NeoMundi Private Pilot  
**Run ID:** NEOMUNDI_OGS_PRIVATE_PILOT_v0_1  
**Timestamp UTC:** 2026-06-28T09:02:58.310800+00:00  
**Status:** Controlled synthetic pilot completed  
**Input package:** `NeoMundi_OGS_Private_Pilot_v0.1_Synthetic_Payloads.zip`

---

## 1. Objective

Run the v0.1 private pilot over five NeoMundi-style synthetic payloads.

The pilot tests whether runtime measurement observations can become governed admissibility inputs without overstating what measurement alone proves.

Processing chain:

```text
NeoMundi observation payload
  ↓
Petunia / DPA epistemic admissibility classification
  ↓
Judicator consequence admissibility classification
  ↓
CAOM-lite receipt
  ↓
Replay summary
```

---

## 2. Payloads Processed

| Payload | Petunia Status | Judicator Status | Receipt Type |
|---|---|---|---|
| `01_stable_but_fragile.json` | observation_only | allow_as_internal_observation | limited_use |
| `02_variable_and_uncertain.json` | requires_review | hold_for_review | hold |
| `03_supported_but_limited.json` | limited_hypothesis_or_claim_candidate | allow_limited_hypothesis_no_action | limited_use |
| `04_contradiction_or_overclaim.json` | not_admissible_as_claim | no_bind_refuse_claim_or_action | no_bind |
| `05_partial_measurement.json` | observation_only_requires_more_measurement | allow_observation_require_more_measurement | limited_use |

---

## 3. Aggregate Results

| Metric | Result |
|---|---:|
| Payloads processed | 5 |
| External action allowed | 0 |
| Review required | 4 |
| No-bind receipts | 1 |
| Limited-use receipts | 3 |
| Hold receipts | 1 |

---

## 4. Interpretation

The pilot demonstrates that measurement signals can be converted into admissibility-relevant classifications.

The key distinction preserved:

> Measurement observes behavior. OGS determines what the observed behavior is allowed to become.

In this pilot:

- stable but fragile signals were not treated as claims;
- variable / uncertain signals were held for review;
- supported but limited signals were constrained to bounded internal use;
- contradiction / overclaim signals produced no-bind treatment;
- partial measurement signals remained observation-only and required more measurement.

No payload was allowed to become an external action or execution trigger.

---

## 5. What This Proves

At proof-of-method level, the pilot shows that OGS can:

- accept NeoMundi-style synthetic observation payloads;
- classify epistemic admissibility through a Petunia / DPA-style mapping;
- classify consequence admissibility through a Judicator-style mapping;
- generate lightweight receipts;
- preserve a replayable classification trail.

---

## 6. What This Does Not Prove

This does not prove production readiness.

Limitations:

- synthetic payloads only;
- no live NeoMundi endpoint;
- no production model evaluation;
- no raw proprietary prompts or customer data;
- simplified Petunia / Judicator mapping;
- no internal OGS schemas exposed;
- no external actions or tool calls permitted.

---

## 7. Controlled Claim

NeoMundi-style runtime measurement signals can serve as upstream observation inputs for an OGS admissibility chain, where Petunia / DPA classify epistemic standing, Judicator determines consequence admissibility, and CAOM-lite receipts preserve the decision trail.

---

## 8. Recommended Next Step

Run a v0.2 pilot with:

- a slightly richer observation payload;
- explicit measurement-limitations field;
- domain label;
- proposed downstream use;
- replay under changed downstream-use request;
- optional human-review flag.
