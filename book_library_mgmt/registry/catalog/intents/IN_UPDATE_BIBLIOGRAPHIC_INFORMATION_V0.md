# IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0

## 1. Intent

A request to change a registered book's description

---

## Machine

```yaml
fqdn: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
superseded_by:
- book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
artifact_kind: INTENT
version: v0
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: catalog
core:
  summary: A request to change a registered book's description
  workflow: WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
  inputs:
    staff_credentials:
      type: object
      required: true
    authorization_rules:
      type: array
      required: true
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
    updated_fields:
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
