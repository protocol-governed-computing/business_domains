# IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0

## Header (Mandatory)

- **Artifact Code:** IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
- **Artifact Kind:** intent
- **Governed By:** CONSTITUTION_INTENT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

A request to replace the descriptive content of a registered work's record.

---

## Machine

```yaml
fqdn: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
artifact_kind: INTENT
version: v0
governed_by: fb.intent::CONSTITUTION_INTENT_V0

core:
  summary: Request an update to a registered work
  workflow: WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0

  inputs:
    staff_id:
      type: string
      required: true
      description: The staff member performing the operation
    work_id:
      type: string
      required: true
    bibliographic_information:
      type: object
      required: true

  outcomes:
    ACK:
      description: Request accepted for processing
    NACK:
      description: Request rejected
```
