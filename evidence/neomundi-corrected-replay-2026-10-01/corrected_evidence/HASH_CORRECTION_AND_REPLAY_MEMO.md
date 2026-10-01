# NeoMundi × OGS v0.1.1 Hash-Correction and Replay Memo

**Corrected run:** `NEOMUNDI_OGS_PRIVATE_PILOT_v0_1_1_CORRECTED`  
**Superseded evidence run:** `NEOMUNDI_OGS_PRIVATE_PILOT_v0_1`

## Correction

The original v0.1 results and receipts contained input hashes that did not match the subsequently supplied raw payload files. The historical values are preserved in `legacy_recorded_input_hash`. The active `input_hash` fields in v0.1.1 are SHA-256 digests of the exact raw file bytes supplied in `payloads/`.

No historical evidence was overwritten.

## Replay

`verification/verify_and_replay.py`:

1. recomputes each raw payload SHA-256;
2. applies an explicit deterministic mapping derived from the documented v0.1 classifications;
3. compares the reproduced Petunia status, Judicator status, and receipt type with the corrected results and receipts;
4. writes a case-level replay result.

## Claim boundary

This is an internally executed deterministic reproduction of the documented synthetic mapping. It is not a live NeoMundi endpoint test, independent external reproduction, production evidence, or validation of the underlying runtime measurements.
