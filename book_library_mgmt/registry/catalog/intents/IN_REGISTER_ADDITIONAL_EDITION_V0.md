# IN_REGISTER_ADDITIONAL_EDITION_V0

## 1. Intent

A request to register a further edition of a work the catalog already holds

---

## Machine

```yaml
fqdn: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
artifact_kind: INTENT
version: v0
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: catalog
core:
  summary: A request to register a further edition of a work the catalog already holds
  workflow: WF_REGISTER_ADDITIONAL_EDITION_V0
  inputs:
    staff_credentials:
      type: object
      required: true
    authorization_rules:
      type: array
      required: true
    staff_id:
      type: string
      required: true
    title:
      type: string
      required: true
    author:
      type: string
      required: true
    publication_year:
      type: string
      required: true
    subject:
      type: array
      required: true
    edition_fields:
      type: object
      required: true
    edition_schema:
      type: object
      required: true
    work_fields:
      type: object
      required: true
    work_schema:
      type: object
      required: true
  outcomes:
    ACK:
      description: Request accepted for processing
    NACK:
      description: Request rejected
```
