# EV_WALLET_CREATED_V0

## Header (Mandatory)

- **Artifact Code:** EV_WALLET_CREATED_V0
- **Artifact Kind:** event
- **Governed By:** CONSTITUTION_EVENT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Announces that a wallet was created, for whom, and when

---

## Machine

```yaml
fqdn: blockchain::EV_WALLET_CREATED_V0
artifact_kind: EVENT
version: v0
governed_by: event::CONSTITUTION_EVENT_V0
authority: pgc.platform
concern: wallet
core:
  summary: Announces that a wallet was created, for whom, and when
  description: Announces that a wallet was created, for whom, and when
  subdomain: wallet
  schema:
    timestamp:
      type: string
      format: date-time
      required: true
      description: When the moment occurred
```
