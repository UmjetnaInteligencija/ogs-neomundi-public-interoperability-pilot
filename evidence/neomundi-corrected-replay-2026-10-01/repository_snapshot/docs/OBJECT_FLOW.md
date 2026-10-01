# Object Flow

## Canonical public sequence

```text
NeoMundiSignal
  ↓ references runtime source and measurement window
OGSGovernanceObject
  ↓ records permitted reliance, restrictions, and no-bind/review status
GovernanceReceipt
  ↓ binds signal and governance object
ReplayRecord
  ↓ records whether reconstruction reproduced the public example
```

## Object classes

### NeoMundi signal

Carries measurement context and limitations. It does not contain or imply execution authority.

### OGS governance object

Records what the signal may support, the evidence burden, uncertainty, permitted use, prohibited use, review requirement, revalidation requirement, and execution status.

### Governance receipt

Binds the source signal and governance object to an explicit decision and integrity digest. The receipt preserves what the system evaluated and decided; it does not certify that the source measurement was true or that an outcome was safe.

### Replay record

Records the replay method, policy/rule version, original object digests, reconstructed object digests, verdict, and any divergence.

## Public examples

Two illustrative trajectories are provided:

- `sample_objects/trajectory_limited_use/` — a material drift signal allowed only for bounded internal use, with review/revalidation and no-bind.
- `sample_objects/trajectory_no_bind/` — a contradiction/overclaim signal refused as a claim or action basis.

Every example is labeled:

```text
illustrative_public_example_not_historical_pilot_artifact
```

They demonstrate interface and integrity mechanics only.
