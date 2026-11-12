# CC_CLAIM_COPY_BARCODE_V1

## Machine

```yaml
fqdn: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V1
artifact_kind: CAPABILITY_CONTRACT
version: v1
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: catalog
supersedes: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
core:
  summary: Claim a physical copy's barcode
  inputs:
    barcode:
      type: string
      required: true
  outputs:
    barcode:
      type: string
      required: true
    address:
      type: string
      required: true
  result_status_contract:
    allowed:
    - SUCCESS
    - ALREADY_EXISTS
    - VIOLATION
    - BACKEND_ERROR
    on_input_failure: VIOLATION
  pipeline:
  - step: claim_barcode
    side_effect: capability_side_effects::CS_REGISTRY_V0
    op: REGISTER
    store: COPY_BARCODE_REGISTRY
    inputs:
      key: $.inputs.barcode
      target_cs: capability_side_effects::CS_MUTABLE_JSON_V0
      target_ref: PHYSICAL_COPIES
    outputs:
      address: $.capability_result.address
      result_status: $.result_status
    result_surface:
    - SUCCESS
    - ALREADY_EXISTS
    - VIOLATION
    - BACKEND_ERROR
    on_result:
      SUCCESS: exit
      ALREADY_EXISTS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
```

---

## Intent

Claim a physical copy's barcode
