# IN_ACTOR_VERIFIED_V0

## 1. Intent

A request to record a decision, carrying the authority, the outcome and the grounds

---

## Machine

```yaml
fqdn: blockchain::IN_ACTOR_VERIFIED_V0
superseded_by:
- blockchain::IN_ACTOR_ACCEPTANCE_V0
- blockchain::IN_ACTOR_REJECTION_V0
artifact_kind: INTENT
version: v0
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: identity
core:
  summary: A request to record a decision, carrying the authority, the outcome and the grounds
  workflow: WF_RECORD_VERIFICATION_DECISION_V0
  inputs:
    contact_address:
      type: string
      required: true
    verifying_authority:
      type: string
      required: true
    decision:
      type: string
      required: true
    grounds:
      type: string
  outcomes:
    ACK:
      description: Request accepted for processing
    NACK:
      description: Request rejected
```
