# Deterministic replay writer v0.2.0

This additive successor fixes platform-dependent result serialization. It
does not replace or edit the historical writer, result, manifests, archives,
or submission. The source baseline is OGS commit
`1f03469de56b9b3c902da78ed8d9fda4eaf5ea36`.

## Run a future replay

From the repository root, using CPython 3.11, 3.12, or 3.13:

```sh
python evidence/neomundi-corrected-replay-2026-10-01/verify_handoff.py
python scripts/verify_and_replay_v0_2_0.py --output replay_result_v0_2_0.json
python tests/test_replay_byte_stability_v0_2_0.py
```

Use a new output filename on every run. `--output` is mandatory. Destinations
within the preserved historical handoff are rejected. Existing output paths
are rejected, and the result is opened in exclusive creation mode. The output
parent directory must already exist. Ordinary I/O failures propagate as
nonzero exits. The protection assumes a trusted local workspace; it is not
an adversarial filesystem sandbox or a crash-atomic publication protocol.

The integrity preflight checks the complete preserved five-case handoff.
The successor keeps the original verifier's input traversal and comparison
logic. It does not introduce a general admission validator or independently
establish input completeness without that preflight.

## Exact behavior changes

- Add a separately versioned entry point and explicit output destination.
- Read the result and receipt reference JSON as UTF-8 with optional BOM,
  matching the existing payload reader and avoiding default locale decoding.
- Open the new result with `encoding="utf-8"` and `newline="\n"`.
- Keep `json.dumps(report, indent=2) + "\n"`, field insertion order, case
  ordering, default ASCII escaping, hash comparisons, and all five
  classification rules unchanged.

The report's historical `run_id` identifies the unchanged synthetic case
set; it does not identify this writer version. Writer version is available
through `--version` and the separately versioned script path. Console output
is diagnostic and is not the byte-stable evidence artifact.

## Regression controls

The stdlib test suite checks the preserved byte reference, native original
versus successor output, simulated Windows CRLF defaults, an independent
post-generation CRLF transformation, repeatability and locale modes, all five
classification mismatches, payload and receipt hash tampering, destination
protection, version reporting, historical byte preservation, identical rule
ASTs, and UTF-8 input under an ASCII locale.

The simulation runs both actual scripts with `pathlib.Path.open` patched to
map an unspecified writer newline to CRLF. Explicit newline arguments are
left intact. It uses real Python text-stream translation on the host OS.
It is not a native Windows execution. No simulated result may be reported
as a native platform result. Temporary mutations affect test copies only.

For raw per-command logs and output bytes, set `REPLAY_AUDIT_DIR` to an
existing or new audit directory before running the tests. The suite creates
it and records arguments, working directory, exit code, environment overrides,
artifact size, SHA-256, LF/CR counts, and raw stdout/stderr and artifact bytes.

## Result and compatibility boundary

For identical preserved inputs the intended result is exactly 2,298 bytes,
84 LF characters, no CR characters, and SHA-256:

```text
a94d4ce69d36baac79c243acc035ca16df6d253ce42859e5f0ba4158bc288bf8
```

The five cases must retain `passed: 5`, `failed: 0`, `verdict: PASS`, with
the same observed and expected classification triples. An original-writer
CRLF result instead has 2,382 bytes despite identical parsed JSON.

The intended compatibility target is CPython 3.11-3.13 on Linux, Windows,
and macOS. Native confirmation remains required on each platform/version
before claiming a fully executed matrix. The initial controlled run covers
Linux / CPython 3.12.14 plus labeled CRLF and locale simulations.

Explicit encoding and LF remove the identified output-serialization
dependency. This is not a general JSON canonicalization specification: it
assumes the same input bytes, data structures, and Python JSON behavior.
Changing payload line endings changes their raw input hashes and is
correctly rejected. No input or preserved output normalization is performed.

This synthetic replay does not establish formal NeoMundi acceptance,
institutional Standing, Judicator execution authorization, production
integration, upstream model provenance, or independent reproduction of this
successor. Existing claim and authorization boundaries remain unchanged.
