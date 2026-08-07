# IN_ACTOR_REGISTERED_V0

## Header (Mandatory)

- **Artifact Code:** IN_ACTOR_REGISTERED_V0
- **Artifact Kind:** intent
- **Governed By:** CONSTITUTION_INTENT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

A request to admit a person as an actor

---

## Machine

```yaml
fqdn: blockchain::IN_ACTOR_REGISTERED_V0
artifact_kind: INTENT
version: v0
governed_by: fb.intent::CONSTITUTION_INTENT_V0
core:
  summary: A request to admit a person as an actor
  workflow: WF_REGISTER_ACTOR_V0
  inputs:
    actor_record:
      type: object
      required: true
    registration_schema:
      type: object
      required: true
  outcomes:
    ACK:
      description: Request accepted for processing
    NACK:
      description: Request rejected
```
