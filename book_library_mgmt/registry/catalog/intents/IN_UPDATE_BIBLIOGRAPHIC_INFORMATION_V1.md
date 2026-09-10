# IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1

## Machine

```yaml
fqdn: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
artifact_kind: INTENT
version: v0
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: catalog
supersedes: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
core:
  summary: A request to change a registered book's description
  workflow: WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
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
    identity_key:
      type: string
      required: true
    updated_fields:
      type: object
      required: true
  outcomes:
    ACK:
      description: Request accepted for processing
    NACK:
      description: Request rejected
```

---

## Intent

A request to change a registered book's description
