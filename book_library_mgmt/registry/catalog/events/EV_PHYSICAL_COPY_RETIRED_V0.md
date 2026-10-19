# EV_PHYSICAL_COPY_RETIRED_V0

## 1. Intent

The library no longer holds that copy

---

## Machine

```yaml
fqdn: book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
artifact_kind: EVENT
version: v0
governed_by: event::CONSTITUTION_EVENT_V0
authority: pgc.platform
concern: catalog
core:
  summary: The library no longer holds that copy
  description: The library no longer holds that copy
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
      description: When the moment occurred
```
