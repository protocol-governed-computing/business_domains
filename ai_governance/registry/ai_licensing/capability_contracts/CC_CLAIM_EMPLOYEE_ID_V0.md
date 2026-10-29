# CC_CLAIM_EMPLOYEE_ID_V0

## Machine

```yaml
fqdn: ai_governance::CC_CLAIM_EMPLOYEE_ID_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: ai_licensing
core:
  summary: Claim a employee's employee id
  inputs:
    employee_id:
      type: string
      required: true
  outputs:
    employee_id:
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
  - step: claim_id
    side_effect: capability_side_effects::CS_REGISTRY_V0
    op: REGISTER
    store: EMPLOYEE_EMPLOYEE_ID_REGISTRY
    inputs:
      key: $.inputs.employee_id
      target_cs: capability_side_effects::CS_MUTABLE_JSON_V0
      target_ref: EMPLOYEES
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

Claim a employee's employee id
