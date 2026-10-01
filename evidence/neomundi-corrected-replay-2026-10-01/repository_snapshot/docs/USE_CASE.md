# Use Case

## Public problem statement

Organizations increasingly collect telemetry, anomaly scores, model-output signals, risk indicators, and drift measurements. A recurring governance failure occurs when those observations are allowed to become deployment changes, public assurances, compliance conclusions, procurement decisions, or automated actions without a separate admissibility and authority evaluation.

## Pilot question

> When an AI runtime signal changes, what should it be allowed to trigger?

## Scenario

A model service shows acceptable aggregate performance but increasing instability in a high-consequence workflow. The observation indicates rising variance, greater sensitivity to contextual phrasing, and material uncertainty about causal attribution. There is insufficient evidence for a public reliability claim and no confirmed basis for automatic operational intervention.

## NeoMundi role

NeoMundi detects and structures the runtime signal, preserving:

- source and observation window;
- measured variation or risk;
- confidence and uncertainty;
- supporting measurements;
- measurement limitations;
- provenance and version.

## OGS role

OGS evaluates what the signal may support and whether a proposed downstream consequence is admissible. Possible results include:

- internal observation only;
- limited decision-support input;
- manual review required;
- revalidation required;
- hold;
- refusal;
- no-bind;
- a separate Judicator review when execution is proposed.

## Value demonstrated

The pilot preserves visibility without allowing visibility to become authority. It gives operators, auditors, and reviewers a traceable record of the signal, the allowed reliance, the prohibited uses, and the reason the result did or did not advance.
