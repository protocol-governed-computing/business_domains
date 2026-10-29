# CC_REQUIRE_COPY_BARCODE_FREE_V0

## Machine

```yaml
fqdn: book_library_mgmt::CC_REQUIRE_COPY_BARCODE_FREE_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: catalog
core:
  summary: Refuse when a copy's barcode is already held, before any is claimed
  inputs:
    barcode:
      type: string
      required: true
  outputs:
    valid:
      type: boolean
      required: true
  result_status_contract:
    allowed:
    - VIOLATION
    - BACKEND_ERROR
    - SUCCESS
    on_input_failure: VIOLATION
  pipeline:
  - step: resolve_identity
    side_effect: capability_side_effects::CS_REGISTRY_V0
    op: RESOLVE
    store: COPY_BARCODE_REGISTRY
    inputs:
      key_or_address: $.inputs.barcode
    outputs:
      target_ref: $.capability_result.target_ref
      result_status: $.result_status
    result_surface:
    - SUCCESS
    - NOT_FOUND
    - VIOLATION
    - BACKEND_ERROR
    on_result:
      SUCCESS: continue
      NOT_FOUND: continue
      VIOLATION: exit
      BACKEND_ERROR: exit
  - step: require_unheld
    transform: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    inputs:
      parameters:
        held: $.results.resolve_identity.result_status
      rules:
      - field: held
        op: eq
        value: NOT_FOUND
    outputs:
      valid: $.capability_result.valid
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: exit
      VIOLATION: exit
```

---

## Intent

Refuse when a copy's barcode is already held, before any is claimed
