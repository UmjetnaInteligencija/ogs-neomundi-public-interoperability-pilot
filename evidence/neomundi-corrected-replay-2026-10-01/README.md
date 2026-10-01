# NeoMundi × Judicator™ OGS: corrected evidence handoff v1.0

**Public release candidate, prepared for Sebastian Fauve (Neo Mundi) and Mark Mocnaj.**

This handoff preserves the original synthetic evidence, the corrected v0.1.1 package, and the v1.1.0-rc.1 repository snapshot. It adds a fresh assistant-run replay and a comparison of the original and corrected receipt bindings.

## Verified result

Five original receipt hashes do not match the supplied raw payload files. The corrected receipts bind to SHA-256 of those exact files and preserve the old values as `legacy_recorded_input_hash`. All five original payloads are byte-identical to the corrected payloads. Original receipt classifications are unchanged. The original replay summary says `deterministic_replay_ready`; it is not a completed replay execution record.

The fresh execution reproduced all five corrected classifications: **5 passed, 0 failed**. Its case report equals the corrected package's recorded replay result. Twelve corrected-package manifest entries were checked. The repository snapshot verifier also passed: 65 manifest entries, 13 JSON documents and two illustrative trajectories.

## What this establishes

The preserved corrected package can execute a deterministic replay over five supplied synthetic inputs, reproduce the documented mapping outputs, and verify the payload-to-receipt hash links.

## What it does not establish

The replay classifier was derived from previously documented classifications. This is a consistency reproduction, not an independent validation of those classifications, recovery of the unknown original execution, live NeoMundi integration, production evidence, unseen-case generalization or independently controlled external reproduction. Local hashes are not authenticated issuance, non-repudiation or trusted time evidence. No external execution authority is conferred by this evidence.

The historical cause of the incorrect hashes remains unresolved. Common JSON reserialization checks did not reproduce them; that does not prove how they arose or attribute fault to Mark, NeoMundi or another person.

## Contents

- `corrected_evidence/`: unchanged extracted corrected v0.1.1 package, including five payloads, receipts, outcomes and original replay script.
- `historical/`: supplied original payloads, receipt bundle, replay-ready summary and evidence note, retained as historical records.
- `repository_snapshot/`: unchanged v1.1.0-rc.1 repository snapshot. Its illustrative objects are not historical pilot evidence.
- `source_archives/`: original source ZIPs with their byte identity preserved.
- `fresh_verification/`: fresh replay result, command output, execution metadata and hash comparison.
- `verify_handoff.py`: offline package verifier and replay wrapper. It runs the unchanged historical script in a temporary copy and does not overwrite evidence.
- `GITHUB_HANDOFF.md`, `PUBLIC_RELEASE_REVIEW.md`, `NOTE_TO_SEBASTIAN.txt`: upload, review and communication instructions.

## Reproduce

With Python 3.9 or later, run from this folder:

```bash
python3 verify_handoff.py
```

No provider accounts, API keys, network access or third-party Python packages are needed. A successful run verifies the handoff manifest, five-case input/receipt bindings and the unchanged corrected replay.

## Publication state

Mark requested preparation for public release on 2026-10-01. No repository has been changed or made public by this handoff. NeoMundi approval of wording, name/brand use, attribution and the evidence archive remains unrecorded. Existing publication-gate text is preserved as historical snapshot content, not silently rewritten as approved. See `PUBLIC_RELEASE_REVIEW.md` for current review status.
