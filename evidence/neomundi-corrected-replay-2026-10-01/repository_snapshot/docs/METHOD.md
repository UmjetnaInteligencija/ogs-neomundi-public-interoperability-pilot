# Public Method

## 1. Signal intake

Receive a versioned NeoMundi-style observation object. Reject or quarantine a material object that lacks source, observation window, runtime context, uncertainty, limitations, timestamp, version, or provenance.

## 2. Intended-use declaration

Record the proposed downstream use separately from the signal itself. Examples include:

- internal observation;
- technical review;
- bounded decision support;
- public reliability statement;
- deployment change;
- execution trigger.

The same measurement may be admissible for one purpose and inadmissible for another.

## 3. Petunia / DPA evaluation

Evaluate public-safe dimensions:

- what the signal actually measures;
- what it does not establish;
- evidence burden;
- uncertainty and contradiction;
- scope and domain limits;
- claim class and allowed reliance;
- review or revalidation requirement.

## 4. CAOM representation

Preserve the trajectory:

```text
observation intent
→ signal
→ measurement limitations
→ claim or reliance request
→ reasoning/evaluation
→ proposed consequence
→ admissibility result
→ execution status
→ receipt
```

## 5. Judicator review

When an action is proposed, separately evaluate:

- authority;
- scope;
- current context;
- effect class and consequence;
- temporal validity;
- delegation or revocation state;
- required human review;
- receipt and replay requirements.

## 6. Receipt

Emit a receipt recording the exact source signal, governance object, decision, allowed and prohibited uses, review/revalidation status, policy/version context, and integrity digest.

## 7. Replay

Reconstruct the same public example from the same inputs and rules. Record exact reproduction or explicit divergence. The verified private-pilot claim is limited to same-payload, same-explicit-rules internal deterministic replay.

## 8. Release discipline

High coherence, high confidence, or cross-system agreement is not a release criterion. It is a signal requiring evidence review, falsifiers, replay, and—where appropriate—human or independent review.
