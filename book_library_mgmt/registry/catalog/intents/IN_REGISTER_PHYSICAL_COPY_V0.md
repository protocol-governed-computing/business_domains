# IN_REGISTER_PHYSICAL_COPY_V0

## Header (Mandatory)

- **Artifact Code:** IN_REGISTER_PHYSICAL_COPY_V0
- **Artifact Kind:** intent
- **Governed By:** CONSTITUTION_INTENT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

A request to register a further copy against a registered book

---

## Machine

```yaml
fqdn: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
artifact_kind: INTENT
version: v0
governed_by: fb.intent::CONSTITUTION_INTENT_V0
core:
  summary: A request to register a further copy against a registered book
  workflow: WF_REGISTER_PHYSICAL_COPY_V0
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
