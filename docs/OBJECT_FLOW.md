# Object Flow

## Public namespace

```text
NM-OBS-001
→ OGS-GOV-001
→ OGS-RCPT-001
→ OGS-RPL-001
```

The NeoMundi object remains the source observation. OGS creates separate governance, receipt, and replay objects. This preserves source provenance and prevents the upstream signal from being confused with the downstream judgment.

## Required links

Every downstream object carries:

- source signal ID;
- trajectory ID;
- policy version;
- source payload hash;
- issuer;
- synthetic-evidence classification.
