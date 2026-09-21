# Reproduction Notes

Run:

```bash
python3 scripts/verify_public_pack.py
```

The script verifies:

- all public JSON files parse;
- sample-object references align;
- source hashes match the published evidence record;
- receipt decisions match governance objects;
- replay objects reproduce expected classifications.

A successful run validates only the deterministic public sample pack. It does not constitute independent reproduction of either proprietary architecture or a production system.
