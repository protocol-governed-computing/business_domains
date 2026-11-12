# CC_CONFIRM_BOOK_IDENTITY_UNCHANGED_V0

## Machine

```yaml
fqdn: book_library_mgmt::CC_CONFIRM_BOOK_IDENTITY_UNCHANGED_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: catalog
core:
  summary: Confirm a corrected book keeps its identity
  inputs:
    identity_key:
      type: string
      required: true
    updated_identity_key:
      type: string
      required: true
  outputs:
    valid:
      type: boolean
      required: true
  result_status_contract:
    allowed:
    - VIOLATION
    - SUCCESS
    on_input_failure: VIOLATION
  pipeline:
  - step: compare_identity
    transform: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
    inputs:
      left: $.inputs.identity_key
      right: $.inputs.updated_identity_key
    outputs:
      identity_unchanged: $.capability_result.is_equal
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: require_identity_unchanged
    transform: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    inputs:
      parameters:
        identity_unchanged: $.results.compare_identity.identity_unchanged
      rules:
      - field: identity_unchanged
        op: eq
        value: true
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

Confirm a corrected book keeps its identity
