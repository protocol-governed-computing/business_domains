# EV_BOOK_RETIRED_V0

## Machine

```yaml
fqdn: book_library_mgmt::EV_BOOK_RETIRED_V0
artifact_kind: EVENT
version: v0
governed_by: event::CONSTITUTION_EVENT_V0
authority: pgc.platform
concern: catalog
core:
  summary: A book retired
  description: A book retired
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
      description: When the moment occurred
```

---

## Intent

A book retired
