# EV_PHYSICAL_COPY_REINSTATED_V0

## Machine

```yaml
fqdn: book_library_mgmt::EV_PHYSICAL_COPY_REINSTATED_V0
artifact_kind: EVENT
version: v0
governed_by: event::CONSTITUTION_EVENT_V0
authority: pgc.platform
concern: catalog
core:
  summary: A physical copy reinstated
  description: A physical copy reinstated
  subdomain: catalog
  schema:
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
```

---

## Intent

A physical copy reinstated
