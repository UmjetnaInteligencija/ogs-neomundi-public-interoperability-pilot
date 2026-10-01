# Reproducibility and Verification

## Public repository verification

Run:

```bash
python3 scripts/verify_repository.py
```

The script uses only the Python standard library. It verifies:

- every file listed in `MANIFEST.json`;
- the manifest digest;
- JSON parsing;
- required fields in public examples;
- integrity digests of signals, governance objects, receipts, and replay records;
- cross-references between objects;
- zero execution authorization in the illustrative trajectories;
- presence of the controlled claim and public claim boundary.

## What the script does not verify

- the private corrected evidence archive;
- NeoMundi measurement accuracy;
- production runtime behavior;
- independent reproduction;
- legal or regulatory compliance;
- safety certification;
- cryptographic non-repudiation;
- private OGS policy or execution-enforcement logic.

## Corrected private-pilot evidence reference

```text
Archive: NEOMUNDI_OGS_PRIVATE_PILOT_v0_1_1_CORRECTED_EVIDENCE_PACK.zip
SHA-256: 6e5f5f24f29f9612ac53a48cac41dfbc48c435fcd21b34b6f5a938d4a482fdc6
Evidence: E3 payloads/outcomes; E4 corrected receipts; E5-internal replay
Replay result: 5 passed, 0 failed
```

## Independent reproduction requirements

A later independent reproduction should preserve:

1. exact archive hash;
2. clean execution environment;
3. operating-system and Python versions;
4. exact commands and exit codes;
5. source payload hashes;
6. policy/rule version;
7. generated governance objects and receipts;
8. replay output;
9. full stdout/stderr transcript;
10. reviewer identity, date, and attestation;
11. a new independent evidence classification without rewriting the historical internal result.
