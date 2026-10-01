# Corrected synthetic evidence handoff, 2026-10-01

## Current repository check

The inspected base is `cba5210cf873ca4a6e5801228c3b4c7f23d4464a`.
GitHub reported this repository as private and the current connection as able to
read and write it. No repository visibility change is part of this addition.

The committed `evidence/REPLAY_RESULT.json` equals the corrected handoff's
`fresh_verification/corrected_replay_result.json` as parsed JSON, including all
five cases, payload hashes, expected/observed classifications and verdicts.
The current `scripts/verify_public_pack.py` was separately executed and passed.
That script checks published sample-record consistency; it does not execute the
five-case classifier over the historical raw payloads.

## Added evidence

The [complete handoff](../evidence/neomundi-corrected-replay-2026-10-01/README.md)
contains 107 preserved files, including historical payloads/receipts, corrected
v0.1.1 evidence, the older v1.1.0-rc.1 snapshot, source ZIPs, fresh replay output,
execution metadata and an offline verifier. Existing root evidence and sample
objects are unchanged. The nested snapshot is historical material, not a
replacement for the current repository.

All five historical receipt hashes differ from the supplied raw payload hashes.
Corrected receipts bind to the exact raw files and retain the former hash values.
The payload bytes and documented classifications are unchanged. The historical
cause of the discrepancy remains unresolved; no fault is attributed to either
party. The original summary's replay-ready status must not be represented as an
original completed execution.

## Reproduce the corrected five-case package

From the repository root, using Python 3.9 or later:

```sh
python3 evidence/neomundi-corrected-replay-2026-10-01/verify_handoff.py
```

The unchanged verifier was executed locally before this addition:

```text
PASS: handoff manifest, five original/corrected payloads and receipt bindings; unchanged corrected replay: 5 passed, 0 failed.
Scope: synthetic package replayability and consistency. Not independent external validation or live integration.
```

The verifier checks the preserved inventory and hashes, original/corrected byte
identity, payload-to-receipt binding and an actual five-case replay in a temporary
copy. It leaves preserved artifacts untouched.

## Claims and release state

The reproduced classifier derives from the previously documented mapping.
These results establish replayability and internal consistency for this synthetic
package. They do not independently validate the original decisions, recover the
unknown historical execution, establish live NeoMundi integration, demonstrate
production performance, or confer external execution authority.

The handoff's publication-state documents describe its preparation-time status
and are deliberately preserved. This companion note records the now-verified
repository target and access. Inclusion on a private review branch does not
establish Sebastian's approval, a joint public release, or independent custody.
The note to Sebastian is a prepared draft; no message was sent through this work.
The broader contamination-trial provenance contract is a separate task and is
not included here.
