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

Select the current records matching the staff member's terms.

Retired records are withheld: they remain stored for audit but are not current, and offering one
as a result would defeat the reason it was retired.

---

## Machine

```yaml
fqdn: book_library_mgmt::CC_SEARCH_CATALOG_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: fb.capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0

core:
  summary: Search the catalog for current records

  inputs:
    search_terms:
      type: object
      required: true

  outputs:
    result_status:
      type: string
    matching_records:
      type: array

  result_status_contract:
    allowed: [SUCCESS, VIOLATION, BACKEND_ERROR]
    on_input_failure: VIOLATION

  pipeline:
    - step: select_current_records
      side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
      op: LIST
      store: BIBLIOGRAPHIC_WORKS
      inputs:
        filter: $.inputs.search_terms
      outputs:
        matching_records: $.capability_result.keys
        result_status: $.result_status
      result_surface: [SUCCESS, VIOLATION, BACKEND_ERROR]
      on_result:
        SUCCESS: exit
        VIOLATION: exit
        BACKEND_ERROR: exit

```
