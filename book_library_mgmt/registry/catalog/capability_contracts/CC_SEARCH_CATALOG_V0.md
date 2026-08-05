# CC_SEARCH_CATALOG_V0

## Header (Mandatory)

- **Artifact Code:** CC_SEARCH_CATALOG_V0
- **Artifact Kind:** capability_contract
- **Governed By:** CONSTITUTION_CAPABILITY_CONTRACT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Select the registered books matching a subject or title, excluding retired ones

---

## Machine

```yaml
fqdn: book_library_mgmt::CC_SEARCH_CATALOG_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: fb.capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
core:
  summary: Select the registered books matching a subject or title, excluding retired ones
  inputs:
    search_criteria:
      type: object
      required: true
  outputs:
    matching_books:
      type: array
      required: true
  result_status_contract:
    allowed:
    - BACKEND_ERROR
    - SUCCESS
    - VIOLATION
    on_input_failure: VIOLATION
  pipeline:
  - step: select_book_records
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: SELECT
    store: BOOKS
    inputs: {}
    outputs:
      records: $.capability_result.records
      result_status: $.result_status
    result_surface:
    - SUCCESS
    - BACKEND_ERROR
    on_result:
      SUCCESS: continue
      BACKEND_ERROR: exit
  - step: select_matching_books
    transform: capability_transforms::CT_PURE_FILTER_RECORDS_V0
    inputs:
      source: $.results.select_book_records.records
      filter: $.inputs.search_criteria
    outputs:
      matching_books: $.capability_result.extracted
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: exit
      VIOLATION: exit
```
