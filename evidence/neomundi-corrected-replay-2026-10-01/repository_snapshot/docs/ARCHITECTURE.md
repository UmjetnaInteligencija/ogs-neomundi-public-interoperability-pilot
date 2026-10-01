# Architecture

## Public architecture

```text
Runtime System
      ↓
NeoMundi Observation Layer / ControlTower
      ↓
Versioned Observation / Risk / Drift Signal Package
      ↓
OGS Intake and Provenance Binding
      ↓
Petunia / DPA Epistemic Evaluation
      ↓
CAOM Cognition-to-Action Representation
      ↓
Judicator, only where an action is proposed
      ↓
Governance Receipt
      ↓
TAG-HAS Replay and Audit View
```

## Separation of responsibilities

| Layer | Primary responsibility | Explicit non-authority |
|---|---|---|
| NeoMundi | Runtime observation, risk/drift signals, provenance, measurement limitations | Does not determine final institutional authority or execution permission in this pilot |
| OGS intake / Injector | Intent, scope, context, provenance, and admissibility preconditions | Does not treat access to a signal as permission to act |
| Petunia / DPA | Claim standing, evidence burden, uncertainty, contradiction, and bounded reliance | Does not create execution authority |
| CAOM | Preserves the chain from observation and claim to proposed consequence | Does not grant permission |
| Judicator | Evaluates whether an exact proposed action may bind under current authority and constraints | Does not convert model reasoning into authority |
| TAG-HAS | Receipt, trajectory telemetry, reconstruction, and replay | Does not certify source truth or real-world safety |

## Invariants

1. A runtime signal is an observation object, not self-validating evidence.
2. Confidence is metadata about a measurement or assessment, not authority.
3. Epistemic admissibility may restrict reliance without authorizing action.
4. Action permission is evaluated against current authority, scope, context, consequence, and validity.
5. Every material decision should preserve its source references, constraints, prohibitions, policy/version context, and receipt.
6. Replay reconstructs the recorded decision path; it does not rewrite the historical outcome.

## No direct signal-to-execution path

A conforming pilot flow contains no edge from a NeoMundi signal directly to an external tool or operational effect. Any proposed action must pass through an explicit consequence and authority review.

## Deployment neutrality

The architecture describes logical control boundaries. It does not require every component to be deployed as a separate microservice. Conformance depends on preserved contracts, identities, versions, evidence custody, and non-collapse of authority—not on network topology.
