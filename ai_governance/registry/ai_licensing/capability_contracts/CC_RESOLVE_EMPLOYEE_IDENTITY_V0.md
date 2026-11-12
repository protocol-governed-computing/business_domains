# CC_RESOLVE_EMPLOYEE_IDENTITY_V0

## Machine

```yaml
fqdn: ai_governance::CC_RESOLVE_EMPLOYEE_IDENTITY_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: ai_licensing
core:
  summary: Answer which employee its identity names, and refuse when none does
  inputs:
    employee_id:
      type: string
      required: true
  outputs:
    employee_record:
      type: object
      required: true
  result_status_contract:
    allowed:
    - NOT_FOUND
    - VIOLATION
    - BACKEND_ERROR
    - SUCCESS
    on_input_failure: VIOLATION
  pipeline:
  - step: resolve_identity
    side_effect: capability_side_effects::CS_REGISTRY_V0
    op: RESOLVE
    store: EMPLOYEE_EMPLOYEE_ID_REGISTRY
    inputs:
      key_or_address: $.inputs.employee_id
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
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
  - step: read_employee_record
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: READ
    store: EMPLOYEES
    inputs:
      key: $.inputs.employee_id
    outputs:
      employee_record: $.capability_result.value
      result_status: $.result_status
    result_surface:
    - SUCCESS
    - NOT_FOUND
    - VIOLATION
    - BACKEND_ERROR
    on_result:
      SUCCESS: exit
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
```

---

## Intent

Answer which employee its identity names, and refuse when none does
