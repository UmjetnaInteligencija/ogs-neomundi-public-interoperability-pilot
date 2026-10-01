# Evidence Register

## Status

This register incorporates the v1.1 correction update and supersedes the earlier v1.0 evidence determination wherever the two conflict.

## Evidence classes

| Code | Meaning |
|---|---|
| E0 | Assertion only |
| E1 | Reported summary |
| E2 | Source artifact located; chain incomplete |
| E3 | Case-level trace with input and outcome |
| E4 | Receipt-backed case-level result |
| E5 | Replay-verified result |
| E6 | Independently reproduced |
| E7 | Production evidence |

## Current register

| Register ID | Claim | Evidence class | Status | Public wording |
|---|---|---|---|---|
| NM-EV-001 | Five supplied synthetic payloads exist and are hash-identified | E3 | Internally verified | Synthetic qualification required |
| NM-EV-002 | Five governance outcomes were cross-checked | E3 | Internally verified | Synthetic qualification required |
| NM-EV-003 | Five corrected receipts bind to supplied payload hashes | E4 | Internally verified | Synthetic qualification required |
| NM-EV-004 | Same-payload, same-explicit-rules replay reproduced five outcomes | E5-internal | 5/5 passed | Must say internal deterministic replay |
| NM-EV-005 | No external action was authorized | E3/E4 | Internally verified | Limited to tested synthetic cases |
| NM-EV-006 | Independent reproduction | E6 | Not performed | Not claimable |
| NM-EV-007 | Production evidence | E7 | Not performed | Prohibited |

## Public repository examples

The JSON objects under `sample_objects/` are newly generated public examples. They are evidence of repository-interface consistency only and are not included in the five historical pilot cases.

## Publication rule

No statement may be upgraded from internal replay to independent reproduction, from synthetic proof of method to production evidence, or from no authorized action in five cases to a general safety guarantee.
