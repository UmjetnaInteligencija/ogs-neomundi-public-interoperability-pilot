# Public pilot filename cleanup

Public filenames now use **Synthetic Pilot** to describe the evidence without implying restricted access. These files were already present in the public repository; this change does not publish a new implementation or change repository visibility.

The four renamed files retain exactly the same bytes. ZIP members are unchanged. Historical run IDs, earlier source-package names, preserved execution transcripts, and frozen repository snapshots keep their original wording. Those historical references can be reconciled with the mapping below.

Only active verifier path references and current packaging manifests are updated. Classification logic and recorded outcomes are unchanged. Earlier manifest bytes remain recoverable at the predecessor commit, and the source ZIP archives remain byte-identical.

| Previous filename | Current filename |
| --- | --- |
| `NEOMUNDI_OGS_PRIVATE_PILOT_RESULTS_v0_1_1_CORRECTED.json` | `NEOMUNDI_OGS_SYNTHETIC_PILOT_RESULTS_v0_1_1_CORRECTED.json` |
| `NEOMUNDI_OGS_PRIVATE_PILOT_EVIDENCE_NOTE_v0_1(5).md` | `NEOMUNDI_OGS_SYNTHETIC_PILOT_EVIDENCE_NOTE_v0_1(5).md` |
| `NEOMUNDI_OGS_PRIVATE_PILOT_v0_1_1_CORRECTED_EVIDENCE_PACK.zip` | `NEOMUNDI_OGS_SYNTHETIC_PILOT_v0_1_1_CORRECTED_EVIDENCE_PACK.zip` |
| `NeoMundi_OGS_Private_Pilot_v0.1_Synthetic_Payloads.zip` | `NeoMundi_OGS_Synthetic_Pilot_v0.1_Payloads.zip` |

[Machine-readable paths, sizes and preserved SHA-256 hashes](PUBLIC_FILENAME_RENAMES_2026-11-13.json).

Verification from the repository root:

```bash
python3 -B scripts/verify_public_pack.py
python3 -B evidence/neomundi-corrected-replay-2026-10-01/verify_handoff.py
```

The handoff command verifies its complete current manifest and replays the five synthetic cases in a temporary copy. It does not establish independent validation, live integration or production readiness.
