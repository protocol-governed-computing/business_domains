# IN_ACTOR_REJECTION_V0

## Header (Mandatory)

- **Artifact Code:** IN_ACTOR_REJECTION_V0
- **Artifact Kind:** intent
- **Governed By:** CONSTITUTION_INTENT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** IN_ACTOR_VERIFIED_V0

---

## 1. Intent

Admits a request to reject a person, and refuses one that states no grounds

---

## Machine

```yaml
fqdn: blockchain::IN_ACTOR_REJECTION_V0
artifact_kind: INTENT
version: v0
governed_by: fb.intent::CONSTITUTION_INTENT_V0
core:
  summary: Admits a request to reject a person, and refuses one that states no grounds
  workflow: WF_REJECT_ACTOR_V0
  inputs:
    contact_address:
      type: string
      required: true
    verifying_authority:
      type: string
      required: true
    grounds:
      type: string
      required: true
  outcomes:
    ACK:
      description: Request accepted for processing
    NACK:
      description: Request rejected
```
