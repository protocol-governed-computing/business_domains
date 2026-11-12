# EV_PHYSICAL_COPY_REGISTERED_V1

## Machine

```yaml
fqdn: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V1
artifact_kind: EVENT
version: v1
governed_by: event::CONSTITUTION_EVENT_V0
authority: pgc.platform
concern: catalog
supersedes: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
core:
  summary: A physical copy registered
  description: A physical copy registered
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

A physical copy registered
