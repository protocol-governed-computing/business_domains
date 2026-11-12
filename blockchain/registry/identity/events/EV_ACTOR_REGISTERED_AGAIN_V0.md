# EV_ACTOR_REGISTERED_AGAIN_V0

## Machine

```yaml
fqdn: blockchain::EV_ACTOR_REGISTERED_AGAIN_V0
artifact_kind: EVENT
version: v0
governed_by: event::CONSTITUTION_EVENT_V0
authority: pgc.platform
concern: identity
core:
  summary: A actor registered again
  description: A actor registered again
  subdomain: identity
  schema:
    contact_address:
      type: string
      required: true
    name:
      type: string
      required: true
    currency_preference:
      type: string
      required: true
    language:
      type: string
      required: true
    occurred_at:
      type: string
      required: true
    timestamp:
      type: string
      format: date-time
      required: true
```

---

## Intent

A actor registered again
