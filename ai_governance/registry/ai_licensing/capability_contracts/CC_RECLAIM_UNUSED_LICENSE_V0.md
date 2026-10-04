# CC_RECLAIM_UNUSED_LICENSE_V0

## Machine

```yaml
fqdn: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: ai_licensing
core:
  summary: Reclaim license from inactive user
  inputs:
    license_id:
      type: string
      required: true
    employee_id:
      type: string
      required: true
    last_active_date:
      type: string
      format: date-time
      required: true
    evaluation_date:
      type: string
      format: date-time
      required: true
    threshold_days:
      type: integer
      required: true
      default: 30
  outputs:
    result_status:
      type: string
    is_inactive:
      type: boolean
    days_inactive:
      type: integer
  result_status_contract:
    allowed:
    - VIOLATION
    - SUCCESS
    - NOT_FOUND
    - BACKEND_ERROR
    on_input_failure: VIOLATION
  pipeline:
  - step: evaluate_inactivity
    transform: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    inputs:
      last_active_date: $.inputs.last_active_date
      evaluation_date: $.inputs.evaluation_date
      threshold_days: $.inputs.threshold_days
    outputs:
      is_inactive: $.capability_result.is_inactive
      days_inactive: $.capability_result.days_inactive
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: deregister_license
    side_effect: capability_side_effects::CS_REGISTRY_V0
    op: DEREGISTER
    store: LICENSE_REGISTRY
    inputs:
      key_or_address: $.inputs.employee_id
    outputs:
      result_status: $.result_status
    result_surface:
    - SUCCESS
    - NOT_FOUND
    - BACKEND_ERROR
    - VIOLATION
    on_result:
      SUCCESS: exit
      NOT_FOUND: exit
      BACKEND_ERROR: exit
      VIOLATION: exit
extensions:
  description: Evaluates inactivity and reclaims license if threshold exceeded
```

---

## Intent

Reclaim license from inactive user
