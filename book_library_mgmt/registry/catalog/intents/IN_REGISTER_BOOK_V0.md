# IN_REGISTER_BOOK_V0

## 1. Intent

A request to register a book together with its first physical copy

---

## Machine

```yaml
fqdn: book_library_mgmt::IN_REGISTER_BOOK_V0
artifact_kind: INTENT
version: v0
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: catalog
core:
  summary: A request to register a book together with its first physical copy
  workflow: WF_REGISTER_BOOK_V0
  inputs:
    staff_credentials:
      type: object
      required: true
    authorization_rules:
      type: array
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
    book_fields:
      type: object
      required: true
    book_schema:
      type: object
      required: true
    barcode:
      type: string
      required: true
    copy_fields:
      type: object
      required: true
    staff_id:
      type: string
      required: true
  outcomes:
    ACK:
      description: Request accepted for processing
    NACK:
      description: Request rejected
```
