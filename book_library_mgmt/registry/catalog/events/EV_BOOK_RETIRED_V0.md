# EV_BOOK_RETIRED_V0

## Header (Mandatory)

- **Artifact Code:** EV_BOOK_RETIRED_V0
- **Artifact Kind:** event
- **Governed By:** CONSTITUTION_EVENT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

A book record is no longer to be used

---

## Machine

```yaml
fqdn: book_library_mgmt::EV_BOOK_RETIRED_V0
artifact_kind: EVENT
version: v0
governed_by: fb.event::CONSTITUTION_EVENT_V0
core:
  summary: A book record is no longer to be used
  description: A book record is no longer to be used
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
