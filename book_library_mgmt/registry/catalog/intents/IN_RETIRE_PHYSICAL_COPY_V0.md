# IN_RETIRE_PHYSICAL_COPY_V0

## Machine

```yaml
fqdn: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
artifact_kind: INTENT
version: v0
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: catalog
core:
  summary: A request to retire a lost or damaged copy
  workflow: WF_RETIRE_PHYSICAL_COPY_V0
  inputs:
    staff_credentials:
      type: object
      required: true
    barcode:
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

A request to retire a lost or damaged copy
