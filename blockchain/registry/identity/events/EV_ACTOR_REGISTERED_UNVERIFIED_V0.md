# EV_ACTOR_REGISTERED_UNVERIFIED_V0

## 1. Intent

The moment a person is admitted and trusted with nothing

---

## Machine

```yaml
fqdn: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
artifact_kind: EVENT
version: v0
governed_by: event::CONSTITUTION_EVENT_V0
authority: pgc.platform
concern: identity
core:
  summary: The moment a person is admitted and trusted with nothing
  description: The moment a person is admitted and trusted with nothing
  subdomain: identity
  schema:
    timestamp:
      type: string
      format: date-time
      required: true
      description: When the moment occurred
```
