# IN_ACTOR_ACCEPTANCE_V0

## Header (Mandatory)

- **Artifact Code:** IN_ACTOR_ACCEPTANCE_V0
- **Artifact Kind:** intent
- **Governed By:** CONSTITUTION_INTENT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** blockchain::IN_ACTOR_VERIFIED_V0

---

## 1. Intent

Admits a request to accept a person, and refuses one that names nobody

---

## Machine

```yaml
fqdn: blockchain::IN_ACTOR_ACCEPTANCE_V0
artifact_kind: INTENT
version: v0
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: identity
supersedes: blockchain::IN_ACTOR_VERIFIED_V0
core:
  summary: Admits a request to accept a person, and refuses one that names nobody
  workflow: WF_ACCEPT_ACTOR_V0
  inputs:
    contact_address:
      type: string
      required: true
    verifying_authority:
      type: string
      required: true
  outcomes:
    ACK:
      description: Request accepted for processing
    NACK:
      description: Request rejected
```
