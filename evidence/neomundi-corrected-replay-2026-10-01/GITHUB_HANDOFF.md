# GitHub handoff for both repositories

This package is repository-neutral. No remote URL, current commit or permission is assumed.

1. Confirm the exact destination repository on each side. Use a review branch such as `evidence/neomundi-corrected-replay-2026-10-01`.
2. Add this folder under `evidence/neomundi-corrected-replay-2026-10-01/`, preserving its filenames and historical files. Do not replace existing evidence or existing repository metadata with the snapshot.
3. Run `python3 evidence/neomundi-corrected-replay-2026-10-01/verify_handoff.py` from the repository root. Preserve the output separately.
4. Review the public-disclosure checklist, then review the exact files to be published. Keep the repository private during review if it is currently private.
5. After each owner approves the exact content and publication, commit the same reviewed folder to both repositories. Use a release-candidate designation until the joint release record is complete.
6. Record each repository URL, destination path and commit SHA in a separate cross-repository release record. The file hashes in this package should match on both sides. Do not rewrite the handoff to insert the hosting commit inside its own hashed content.
7. Attach the complete outer ZIP and its separate SHA-256 checksum sidecar to an approved release if desired. Changing repository visibility requires a separate explicit action.

Suggested PR title: Add corrected NeoMundi synthetic pilot evidence and replay record

Suggested PR description: Preserves historical hash-mismatch evidence alongside corrected payload-bound receipts and an assistant-run five-case replay (5 passed, 0 failed). Adds an offline verification wrapper and explicit evidence qualifications. No live endpoint, production result, independent external validation, mapping change or external execution is claimed.

A GitHub integrity workflow pass alone is not a pilot reproduction. Run the handoff verifier for the corrected five-case replay. No GitHub update or external message has been performed by this package.
