# CC_WRITE_PHYSICAL_COPY_V0

## Machine

```yaml
fqdn: book_library_mgmt::CC_WRITE_PHYSICAL_COPY_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: catalog
core:
  summary: Write a new physical copy in its first state
  inputs:
    barcode:
      type: string
      required: true
    identity_key:
      type: string
      required: true
  outputs:
    result_status:
      type: string
      required: true
  result_status_contract:
    allowed:
    - VIOLATION
    - SUCCESS
    - BACKEND_ERROR
    on_input_failure: VIOLATION
  pipeline:
  - step: assemble_copy_record
    transform: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    inputs:
      fields:
        barcode: $.inputs.barcode
        identity_key: $.inputs.identity_key
        state: REGISTERED
    outputs:
      copy_record: $.capability_result.record
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: write_copy_record
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: WRITE
    store: PHYSICAL_COPIES
    inputs:
      key: $.inputs.barcode
      value: $.results.assemble_copy_record.copy_record
    outputs:
      result_status: $.result_status
    result_surface:
    - SUCCESS
    - VIOLATION
    - BACKEND_ERROR
    on_result:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
```

---

## Intent

Write a new physical copy in its first state
