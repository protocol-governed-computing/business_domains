# IN_REINSTATE_PHYSICAL_COPY_V0

## 1. Intent

A request to return a retired copy to the registered state

---

## Machine

```yaml
fqdn: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
artifact_kind: INTENT
version: v0
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: catalog
core:
  summary: A request to return a retired copy to the registered state
  workflow: WF_REINSTATE_PHYSICAL_COPY_V0
  inputs:
    staff_credentials:
      type: object
      required: true
    authorization_rules:
      type: array
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
