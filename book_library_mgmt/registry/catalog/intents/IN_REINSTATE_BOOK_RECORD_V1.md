# IN_REINSTATE_BOOK_RECORD_V1

## Machine

```yaml
fqdn: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V1
artifact_kind: INTENT
version: v1
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: catalog
supersedes: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
core:
  summary: A request to reinstate book record
  workflow: WF_REINSTATE_BOOK_RECORD_V2
  inputs:
    staff_credentials:
      type: object
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

---

## Intent

A request to reinstate book record
