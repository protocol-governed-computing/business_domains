# EV_WALLET_CREATED_V0

## Machine

```yaml
fqdn: blockchain::EV_WALLET_CREATED_V0
artifact_kind: EVENT
version: v0
governed_by: event::CONSTITUTION_EVENT_V0
authority: pgc.platform
concern: wallet
core:
  summary: A wallet created
  description: A wallet created
  subdomain: wallet
  schema:
    wallet_id:
      type: string
      required: true
    holder:
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

A wallet created
