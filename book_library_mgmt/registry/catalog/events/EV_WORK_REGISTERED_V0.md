# EV_WORK_REGISTERED_V0

## Machine

```yaml
fqdn: book_library_mgmt::EV_WORK_REGISTERED_V0
artifact_kind: EVENT
version: v0
governed_by: event::CONSTITUTION_EVENT_V0
authority: pgc.platform
concern: catalog
core:
  summary: A work registered
  description: A work registered
  subdomain: catalog
  schema:
    work_key:
      type: string
      required: true
    title:
      type: string
      required: true
    author:
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

A work registered
