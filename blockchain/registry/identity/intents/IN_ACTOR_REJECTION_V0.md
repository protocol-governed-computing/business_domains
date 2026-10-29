# IN_ACTOR_REJECTION_V0

## Machine

```yaml
fqdn: blockchain::IN_ACTOR_REJECTION_V0
artifact_kind: INTENT
version: v0
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: identity
core:
  summary: A request to reject actor
  workflow: WF_REJECT_ACTOR_V1
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

---

## Intent

A request to reject actor
