# NeoMundi × OGS Private Pilot v0.1.1 — Corrected Evidence Package

This package preserves the original v0.1 classifications while correcting the payload-to-receipt hash binding against the supplied raw payload files.

## Run

```bash
python3 verification/verify_and_replay.py
```

Expected result: five passed, zero failed.

## Evidence level

- Raw inputs present
- Case-level outcomes present
- Receipt-backed
- Internally executed deterministic replay
- Not independently reproduced
- Not live or production-derived

See `HASH_CORRECTION_AND_REPLAY_MEMO.md` for the claim boundary.
