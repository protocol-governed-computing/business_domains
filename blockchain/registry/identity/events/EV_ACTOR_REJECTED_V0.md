# EV_ACTOR_REJECTED_V0

## Header (Mandatory)

- **Artifact Code:** EV_ACTOR_REJECTED_V0
- **Artifact Kind:** event
- **Governed By:** CONSTITUTION_EVENT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

The moment an authority records a decision not to trust an actor

---

## Machine

```yaml
fqdn: blockchain::EV_ACTOR_REJECTED_V0
artifact_kind: EVENT
version: v0
governed_by: event::CONSTITUTION_EVENT_V0
authority: pgc.platform
concern: identity
core:
  summary: The moment an authority records a decision not to trust an actor
  description: The moment an authority records a decision not to trust an actor
  subdomain: identity
  schema:
    timestamp:
      type: string
      format: date-time
      required: true
      description: When the moment occurred
```
