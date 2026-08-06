# EV_PHYSICAL_COPY_REGISTERED_V0

## Header (Mandatory)

- **Artifact Code:** EV_PHYSICAL_COPY_REGISTERED_V0
- **Artifact Kind:** event
- **Governed By:** CONSTITUTION_EVENT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

The library recorded another copy it owns

---

## Machine

```yaml
fqdn: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
artifact_kind: EVENT
version: v0
governed_by: fb.event::CONSTITUTION_EVENT_V0
core:
  summary: The library recorded another copy it owns
  description: The library recorded another copy it owns
  subdomain: catalog
  schema:
    identity_key:
      type: string
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
