# CC_RECORD_TRAINING_COMPLETED_V0

## Machine

```yaml
fqdn: ai_governance::CC_RECORD_TRAINING_COMPLETED_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: ai_licensing
core:
  summary: Set what record training completed records on the employee
  inputs:
    employee_id:
      type: string
      required: true
  outputs:
    updated_count:
      type: integer
      required: true
  result_status_contract:
    allowed:
    - SUCCESS
    - VIOLATION
    - BACKEND_ERROR
    on_input_failure: VIOLATION
  pipeline:
  - step: set_record
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: UPDATE_WHERE
    store: EMPLOYEES
    inputs:
      filter:
        employee_id: $.inputs.employee_id
      updates:
        training_completed: true
    outputs:
      matched_keys: $.capability_result.matched_keys
      updated_count: $.capability_result.updated_count
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

Set what record training completed records on the employee
