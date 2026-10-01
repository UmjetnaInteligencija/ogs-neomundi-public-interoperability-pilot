# NeoMundi × OGS Public Interoperability Pilot — Consolidated Specification

**Version:** 1.1.0-rc.1  
**Status:** Release candidate; pending final joint sign-off  
**Classification:** Public-safe synthetic proof of method  
**Audience:** Enterprise operators, auditors, regulators, technology partners, researchers, and prospective pilot participants

## 1. Purpose

This specification defines the scope, architecture, public evidence model, disclosure boundary, ownership structure, and release criteria for an interoperability demonstration between NeoMundi and Operational Governance Systems / Project Petunia × Judicator.

The pilot shows how runtime observations can be transformed into bounded governance objects, admissibility outcomes, receipts, and replayable evidence without treating measurement as self-authorizing.

It is not a production deployment, safety certification, regulatory approval, independent validation, or universal applicability claim.

## 2. Core use case

A runtime system initially appears stable but begins to exhibit increasing fragility, inconsistency, factual-risk signals, or semantic drift across observation windows.

NeoMundi structures the runtime observation. OGS evaluates:

- what the signal may legitimately support;
- which reliance class is admissible;
- whether review or revalidation is required;
- whether public or operational use must be restricted;
- whether the signal must remain non-binding;
- whether a proposed consequence must be refused.

```text
runtime behavior
→ NeoMundi observation
→ structured signal package
→ OGS admissibility evaluation
→ bounded reliance classification
→ review / revalidation / refusal / no-bind
→ governance receipt
→ replay
```

## 3. System boundaries

### NeoMundi boundary

NeoMundi provides runtime observation, signal generation, drift/risk indicators, variation tracking, source metadata, timestamps, provenance, and observation-window definition.

NeoMundi does not, within this pilot, independently determine institutional authority, final epistemic admissibility, execution permission, or governance consequence.

### OGS boundary

OGS evaluates evidence burden, uncertainty, contradiction, permitted reliance, review and revalidation requirements, refusal/no-bind outcomes, governance-object construction, receipt generation, and replay traceability.

Where an action is proposed, Judicator evaluates whether the exact action may bind into the world under current authority, scope, context, consequence, and validity conditions.

### Shared boundary

The interoperability boundary is the explicit, versioned, contextualized, and traceable signal package passed from NeoMundi to OGS. The two systems remain distinct control layers; the pilot does not imply a merged platform.

## 4. Non-collapse rules

```text
observation ≠ evidence
risk score ≠ truth
drift signal ≠ authority
measurement ≠ admissibility
admissibility ≠ execution permission
receipt ≠ certification
```

## 5. Minimum signal package

A material public interface object should identify:

- signal ID;
- source system and component;
- observation window;
- runtime context;
- signal type and value;
- risk or drift class;
- confidence and uncertainty;
- supporting measurements;
- measurement limitations;
- provenance;
- timestamp;
- signal version;
- issuer.

## 6. Evidence result

The controlling public evidence determination is recorded in `evidence/OGS_NEOMUNDI_PILOT_EVIDENCE_REGISTER_v1_1_CORRECTION_UPDATE.md`.

## 7. Excluded scope

- direct production API integration;
- live customer data;
- autonomous remediation;
- enterprise IAM or identity proofing;
- legal or regulatory certification;
- HSM/KMS-backed receipt custody;
- external receipt anchoring;
- continuous production deployment;
- safety-critical physical execution;
- independent reproduction.

## 8. Completion standard

A final public release requires:

1. fixed use-case wording;
2. explicit system boundaries;
3. at least one complete public signal-to-receipt flow;
4. internally consistent sample objects;
5. evidence and replay qualification;
6. visible synthetic status;
7. visible limitations;
8. joint approval of final wording and attribution;
9. documented IP and brand boundaries;
10. a versioned, integrity-checked public repository.
