# EV_ACTOR_REGISTERED_UNVERIFIED_V0

## Machine

```yaml
fqdn: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
artifact_kind: EVENT
version: v0
governed_by: event::CONSTITUTION_EVENT_V0
authority: pgc.platform
concern: identity
core:
  summary: A actor registered unverified
  description: A actor registered unverified
  subdomain: identity
  schema:
    contact_address:
      type: string
      required: true
    occurred_at:
      type: string
      required: true
    timestamp:
      type: string
      format: date-time
      required: true
      description: When the moment occurred
```

---

## Intent

A actor registered unverified
