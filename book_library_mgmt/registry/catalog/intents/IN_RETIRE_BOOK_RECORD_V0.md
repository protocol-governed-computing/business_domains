# IN_RETIRE_BOOK_RECORD_V0

## 1. Intent

A request to retire a book record judged obsolete

---

## Machine

```yaml
fqdn: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
artifact_kind: INTENT
version: v0
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: catalog
core:
  summary: A request to retire a book record judged obsolete
  workflow: WF_RETIRE_BOOK_RECORD_V0
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
    staff_id:
      type: string
      required: true
  outcomes:
    ACK:
      description: Request accepted for processing
    NACK:
      description: Request rejected
```
