# Synthetic evidence integrity CI

This additive workflow extends the October 5, 2026 `neomundi-top-level-ci.patch`
candidate. It preserves the root manifest, all historical and corrected evidence,
source archives, nested workflow and existing verifier implementations.

Two independent jobs run on every push and pull request, and support manual
dispatch. There are no path filters, job dependencies or continue-on-error flags.
The workflow grants only `contents: read`, disables persisted checkout credentials,
pins both actions by commit and uses Python 3.12 on Ubuntu 24.04. Assertions remain
enabled because the preserved handoff verifier relies on them.

1. `root_sample_pack_consistency` checks the preserved manifest checksum, all 37
   entries' SHA-256 hashes and byte counts, then runs the unchanged public-pack
   verifier. The manifest pin prevents entry removal or coordinated edits from
   silently redefining this historical baseline. Additions are permitted outside
   its historical inventory; the original manifest must not be regenerated.
2. `preserved_corrected_handoff_replay` runs the unchanged handoff verifier. Its
   107-file package comprises 105 listed artifacts plus the manifest and checksum.
   The verifier checks inventory, hashes and sizes, five original/corrected payload
   pairs, payload-to-receipt bindings, and five-case replay in a temporary copy.
   The fresh replay must equal the preserved recorded result as parsed JSON.

Each job also runs its own negative tests. Root tests flip one byte in every one
of the 37 listed files without changing size, append bytes, remove a file and
remove a manifest entry. Handoff tests corrupt payload, receipts and an archive;
remove/add inventory entries; corrupt the manifest checksum; and repair outer
checksums in disposable copies to test rejection of an incorrect receipt binding
and incorrect recorded replay. Pristine controls must pass. All mutations occur
in temporary directories; the repository evidence is never rewritten.

## Local reproduction

From the repository root, with Python 3.12:

```sh
export PYTHONDONTWRITEBYTECODE=1 PYTHONOPTIMIZE=0
python3 scripts/verify_root_manifest.py
python3 scripts/verify_public_pack.py
python3 -m unittest discover -s tests -p test_root_manifest.py -v
python3 evidence/neomundi-corrected-replay-2026-10-01/verify_handoff.py
python3 -m unittest discover -s tests -p test_handoff_integrity.py -v
```

## Limits

These checks establish bounded synthetic internal consistency and deterministic
replay. They do not independently validate classification semantics, reconstruct
historical execution, establish production integration, confer institutional
Standing, or grant execution authorization. A consistent hash is not evidence of
truth or authority. Institutional Standing and Judicator execution authorization
remain separate.

This workflow does not make checks mandatory for merging. Repository maintainers
must separately configure required status checks or rulesets if desired. Both
jobs must be required to enforce both scopes. A future edit to the workflow or
verifier can change the gate and still requires review. Additional files outside
the two preserved inventories are not automatically admitted as evidence.

The handoff verifier's historical inventory exclusions and checksum behavior are
preserved, not strengthened here. This is regression coverage, not a security
proof against an actor able to change evidence, manifests and verification code.
