# IN_RETIRE_CATALOG_RECORD_V0

## Header (Mandatory)

- **Artifact Code:** IN_RETIRE_CATALOG_RECORD_V0
- **Artifact Kind:** intent
- **Governed By:** CONSTITUTION_INTENT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

A request to retire an obsolete record. Retirement withholds; it never deletes.

---

## Machine

```yaml
fqdn: book_library_mgmt::IN_RETIRE_CATALOG_RECORD_V0
artifact_kind: INTENT
version: v0
governed_by: fb.intent::CONSTITUTION_INTENT_V0

core:
  summary: Request retirement of an obsolete record
  workflow: WF_RETIRE_CATALOG_RECORD_V0

  inputs:
    staff_id:
      type: string
      required: true
      description: The staff member performing the operation
    work_id:
      type: string
      required: true

  outcomes:
    ACK:
      description: Request accepted for processing
    NACK:
      description: Request rejected
```
