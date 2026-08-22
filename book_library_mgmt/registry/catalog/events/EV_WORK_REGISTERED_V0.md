# EV_WORK_REGISTERED_V0

## Header (Mandatory)

- **Artifact Code:** EV_WORK_REGISTERED_V0
- **Artifact Kind:** event
- **Governed By:** CONSTITUTION_EVENT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

The moment a work enters the catalog, created by the edition that evidences it

---

## Machine

```yaml
fqdn: book_library_mgmt::EV_WORK_REGISTERED_V0
artifact_kind: EVENT
version: v0
governed_by: event::CONSTITUTION_EVENT_V0
authority: pgc.platform
concern: catalog
core:
  summary: The moment a work enters the catalog, created by the edition that evidences it
  description: The moment a work enters the catalog, created by the edition that evidences it
  subdomain: catalog
  schema:
    timestamp:
      type: string
      format: date-time
      required: true
      description: When the moment occurred
```
