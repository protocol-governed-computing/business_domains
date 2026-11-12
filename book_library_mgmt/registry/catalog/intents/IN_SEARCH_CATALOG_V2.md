# IN_SEARCH_CATALOG_V2

## Machine

```yaml
fqdn: book_library_mgmt::IN_SEARCH_CATALOG_V2
artifact_kind: INTENT
version: v2
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: catalog
supersedes: book_library_mgmt::IN_SEARCH_CATALOG_V1
core:
  summary: A request to search catalog
  workflow: WF_SEARCH_CATALOG_V3
  inputs:
    staff_credentials:
      type: object
      required: true
    search_criteria:
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

---

## Intent

A request to search catalog
