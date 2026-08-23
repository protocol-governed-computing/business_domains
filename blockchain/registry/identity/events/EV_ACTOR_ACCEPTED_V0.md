# EV_ACTOR_ACCEPTED_V0

## 1. Intent

The moment an authority records a decision to trust an actor

---

## Machine

```yaml
fqdn: blockchain::EV_ACTOR_ACCEPTED_V0
artifact_kind: EVENT
version: v0
governed_by: event::CONSTITUTION_EVENT_V0
authority: pgc.platform
concern: identity
core:
  summary: The moment an authority records a decision to trust an actor
  description: The moment an authority records a decision to trust an actor
  subdomain: identity
  schema:
    timestamp:
      type: string
      format: date-time
      required: true
      description: When the moment occurred
```
