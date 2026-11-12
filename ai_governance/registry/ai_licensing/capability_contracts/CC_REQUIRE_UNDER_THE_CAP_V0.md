# CC_REQUIRE_UNDER_THE_CAP_V0

## Machine

```yaml
fqdn: ai_governance::CC_REQUIRE_UNDER_THE_CAP_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: ai_licensing
core:
  summary: Refuse to provision license when the licenses held reach the cap
  inputs:
    cap:
      type: integer
      required: true
  outputs:
    valid:
      type: boolean
      required: true
  result_status_contract:
    allowed:
    - BACKEND_ERROR
    - SUCCESS
    - VIOLATION
    on_input_failure: VIOLATION
  pipeline:
  - step: count_licenses
    side_effect: capability_side_effects::CS_REGISTRY_V0
    op: COUNT
    store: LICENSE_IDENTITY_REGISTRY
    inputs: {}
    outputs:
      count: $.capability_result.count
      result_status: $.result_status
    result_surface:
    - SUCCESS
    - BACKEND_ERROR
    on_result:
      SUCCESS: continue
      BACKEND_ERROR: exit
  - step: require_below_cap
    transform: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    inputs:
      parameters:
        count: $.results.count_licenses.count
      rules:
      - field: count
        op: lt
        value: $.inputs.cap
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

Refuse to provision license when the licenses held reach the cap
