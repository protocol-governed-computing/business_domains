# EV_BOOK_REGISTERED_V0

## Header (Mandatory)

- **Artifact Code:** EV_BOOK_REGISTERED_V0
- **Artifact Kind:** event
- **Governed By:** CONSTITUTION_EVENT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

A book entered the catalog and acquired its authoritative record

---

## Machine

```yaml
fqdn: book_library_mgmt::EV_BOOK_REGISTERED_V0
artifact_kind: EVENT
version: v0
governed_by: event::CONSTITUTION_EVENT_V0
authority: pgc.platform
concern: catalog
core:
  summary: A book entered the catalog and acquired its authoritative record
  description: A book entered the catalog and acquired its authoritative record
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
