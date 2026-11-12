# EV_ACTOR_ACCEPTED_V1

## Machine

```yaml
fqdn: blockchain::EV_ACTOR_ACCEPTED_V1
artifact_kind: EVENT
version: v1
governed_by: event::CONSTITUTION_EVENT_V0
authority: pgc.platform
concern: identity
supersedes: blockchain::EV_ACTOR_ACCEPTED_V0
core:
  summary: A actor accepted
  description: A actor accepted
  subdomain: identity
  schema:
    contact_address:
      type: string
      required: true
    verifying_authority:
      type: string
      required: true
    grounds:
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

A actor accepted
