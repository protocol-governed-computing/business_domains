# EV_BOOK_REGISTERED_V0

## Machine

```yaml
fqdn: book_library_mgmt::EV_BOOK_REGISTERED_V0
artifact_kind: EVENT
version: v0
governed_by: event::CONSTITUTION_EVENT_V0
authority: pgc.platform
concern: catalog
core:
  summary: A book registered
  description: A book registered
  subdomain: catalog
  schema:
    identity_key:
      type: string
      required: true
    title:
      type: string
      required: true
    author:
      type: string
      required: true
    publication_year:
      type: integer
      required: true
    barcode:
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

A book registered
