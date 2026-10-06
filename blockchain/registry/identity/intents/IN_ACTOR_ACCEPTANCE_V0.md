# IN_ACTOR_ACCEPTANCE_V0

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
  summary: Admits a request to accept a person, with the grounds the authority chooses to state, and refuses
    one that names nobody
  workflow: WF_ACCEPT_ACTOR_V1
  inputs:
    contact_address:
      type: string
      required: true
    verifying_authority:
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

---

## Intent

Admits a request to accept a person, with the grounds the authority chooses to state, and refuses one that names nobody
