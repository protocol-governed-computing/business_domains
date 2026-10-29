# EV_BOOK_REINSTATED_V0

## Machine

```yaml
fqdn: book_library_mgmt::EV_BOOK_REINSTATED_V0
artifact_kind: EVENT
version: v0
governed_by: event::CONSTITUTION_EVENT_V0
authority: pgc.platform
concern: catalog
core:
  summary: A book reinstated
  description: A book reinstated
  subdomain: catalog
  schema:
    identity_key:
      type: string
      required: true
    staff_id:
      type: string
      required: true
    timestamp:
      type: string
      format: date-time
      required: true
```

---

## Intent

A book reinstated
