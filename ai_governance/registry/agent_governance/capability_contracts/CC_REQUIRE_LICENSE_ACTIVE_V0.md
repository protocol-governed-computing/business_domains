# CC_REQUIRE_LICENSE_ACTIVE_V0

## Machine

```yaml
fqdn: ai_governance::CC_REQUIRE_LICENSE_ACTIVE_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: agent_governance
core:
  summary: Refuse to govern agent action unless the license holds what the business requires
  inputs:
    state:
      type: string
      required: true
  outputs:
    valid:
      type: boolean
      required: true
  result_status_contract:
    allowed:
    - SUCCESS
    - VIOLATION
    on_input_failure: VIOLATION
  pipeline:
  - step: require_license_active
    transform: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    inputs:
      parameters:
        state: $.inputs.state
      rules:
      - field: state
        op: eq
        value: ACTIVE
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

Refuse to govern agent action unless the license holds what the business requires
