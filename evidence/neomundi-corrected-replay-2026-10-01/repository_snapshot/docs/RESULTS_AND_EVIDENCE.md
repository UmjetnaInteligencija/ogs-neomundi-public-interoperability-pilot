# Results and Evidence

## Controlling public result

> Five synthetic NeoMundi-style observation payloads were processed through an explicit OGS admissibility mapping. Five corrected payload-bound receipts were generated, and an internal deterministic replay reproduced all five documented classifications under the same payloads and explicit rules. No external action was authorized. The result is synthetic, internally verified, and not independently reproduced or production-derived.

## Evidence determination

| Evidence object | Class | Verification | Publication status |
|---|---|---|---|
| Five supplied synthetic raw payloads | E3 | Hash verified | Eligible with synthetic qualification |
| Five case-level governance outcomes | E3 | Internally cross-checked | Eligible with synthetic qualification |
| Five corrected CAOM-lite receipts | E4 | Bound to supplied payload hashes | Eligible with synthetic qualification |
| Same-payload, same-explicit-rules replay | E5-internal | 5 passed, 0 failed | Eligible with internal-replay qualification |
| Independent reproduction | E6 | Not performed | Not claimable |
| Production evidence | E7 | Not performed | Prohibited |

## Quantitative summary

| Metric | Verified public statement |
|---|---:|
| Synthetic payloads | 5 |
| Case-level outcomes | 5 |
| Corrected payload-bound receipts | 5 |
| Internal deterministic replay | 5 passed / 0 failed |
| External action authorized | 0 |
| Independent reproductions | 0 |
| Production deployments evidenced | 0 |

## Evidence pack reference

```text
NEOMUNDI_OGS_PRIVATE_PILOT_v0_1_1_CORRECTED_EVIDENCE_PACK.zip
SHA-256: 6e5f5f24f29f9612ac53a48cac41dfbc48c435fcd21b34b6f5a938d4a482fdc6
```

The archive is referenced but not embedded in this public-release candidate. Its public attachment requires explicit joint approval and a disclosure review.

## Historical correction

The original v0.1 record contained an input-hash mismatch. The v0.1.1 correction binds receipts to the supplied payload hashes while preserving the original values in `legacy_recorded_input_hash`. The historical mismatch is not concealed or rewritten.

## Interpretation boundary

The result supports a claim about deterministic processing of a small synthetic case set under explicit rules. It does not establish live-model performance, production readiness, real-world safety, independent validation, regulatory compliance, or general superiority.
