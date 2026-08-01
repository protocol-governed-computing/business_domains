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

A request to register a copy the library owns against the work it belongs to.

---

## Machine

```yaml
fqdn: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
artifact_kind: INTENT
version: v0
governed_by: fb.intent::CONSTITUTION_INTENT_V0

core:
  summary: Request registration of a physical copy
  workflow: WF_REGISTER_PHYSICAL_COPY_V0

  inputs:
    staff_id:
      type: string
      required: true
      description: The staff member performing the operation
    copy_id:
      type: string
      required: true
    work_id:
      type: string
      required: true

  outcomes:
    ACK:
      description: Request accepted for processing
    NACK:
      description: Request rejected
```
