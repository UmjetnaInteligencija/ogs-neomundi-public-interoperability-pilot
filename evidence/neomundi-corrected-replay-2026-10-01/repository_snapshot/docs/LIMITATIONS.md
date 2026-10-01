# Limitations

## Evidence limitations

- Five synthetic cases only.
- Internal verification only.
- No independent reproduction.
- No production evidence.
- No live customer data.
- No live NeoMundi-to-OGS API exchange demonstrated in this public package.
- No claim of statistical generalization.
- No comparison against a production baseline.

## Architecture and implementation limitations

- The public mapping is simplified and does not expose private OGS policy logic, thresholds, prompts, DPA internals, registry data, or execution-enforcement implementation.
- The repository contains illustrative objects, not the private historical payload set.
- The verifier checks local repository integrity and example consistency only.
- No autonomous remediation or external tool execution is enabled.
- No enterprise identity, IAM, delegation registry, or revocation service is integrated here.

## Receipt limitations

- SHA-256 hashes support local integrity checking but do not provide independent custody or non-repudiation.
- No digital signature, HSM/KMS protection, trusted timestamp, or external anchoring is claimed.
- A receipt preserves what the system evaluated and decided; it does not establish that the source observation was true, the policy was lawful, or an outcome was safe.

## Legal, regulatory, and commercial limitations

- No legal advice.
- No regulatory-compliance determination.
- No safety or conformity certification.
- No warranty of deployment fitness.
- No license to use either party's pre-existing intellectual property.
- Final brand treatment and commercial references require partner approval.

## Publication limitation

This release candidate should remain private until all blocking items in `PUBLICATION_GATE.md` are cleared.
