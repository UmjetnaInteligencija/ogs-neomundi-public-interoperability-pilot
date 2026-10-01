# Historical v0.1 Disclosure

## Original record

The original v0.1 evidence record preserved five classifications and receipt-style objects but contained an input-hash mismatch between recorded values and the supplied payload files.

## Correction

The v0.1.1 correction:

- recalculated the supplied payload hashes;
- bound the corrected receipts to those hashes;
- executed same-payload, same-explicit-rules replay;
- preserved the original values as `legacy_recorded_input_hash`;
- recorded five replay passes and zero failures;
- did not claim independent reproduction or production evidence.

## Governance significance

The correction is part of the evidence, not an embarrassment to be removed. A receipt created from an incorrect source binding cannot be made trustworthy by presentation alone. The corrected pack preserves the mismatch, repair, and resulting evidence class.

## Supersession rule

Where the v0.1 summary and v0.1.1 correction differ on source binding or replay status, the v0.1.1 correction controls. The historical v0.1 record remains preserved for provenance.
