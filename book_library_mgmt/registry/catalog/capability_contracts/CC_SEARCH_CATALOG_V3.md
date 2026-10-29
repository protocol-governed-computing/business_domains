# CC_SEARCH_CATALOG_V3

## Machine

```yaml
fqdn: book_library_mgmt::CC_SEARCH_CATALOG_V3
artifact_kind: CAPABILITY_CONTRACT
version: v3
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: catalog
supersedes: book_library_mgmt::CC_SEARCH_CATALOG_V2
core:
  summary: Answer the books matching the criteria named
  inputs:
    search_criteria:
      type: object
      required: true
  outputs:
    matching_works:
      type: array
      required: true
    matching_books:
      type: array
      required: true
  result_status_contract:
    allowed:
    - BACKEND_ERROR
    - VIOLATION
    - SUCCESS
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
  - step: select_registered_books
    transform: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
    inputs:
      source: $.results.select_book_records.records
      filter:
        state: REGISTERED
    outputs:
      registered_books: $.capability_result.extracted
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: select_matching_books
    transform: capability_transforms::CT_PURE_SELECT_RECORDS_V0
    inputs:
      source: $.results.select_registered_books.registered_books
      filter: $.inputs.search_criteria
    outputs:
      matching_books: $.capability_result.extracted
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: group_books_by_work
    transform: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
    inputs:
      source: $.results.select_matching_books.matching_books
      attribute: work_key
    outputs:
      matching_works: $.capability_result.grouped
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: exit
      VIOLATION: exit
```

---

## Intent

Answer the books matching the criteria named
