# CC_REQUIRE_LICENSE_UNUSED_FOR_DAYS_V0

## Machine

```yaml
fqdn: ai_governance::CC_REQUIRE_LICENSE_UNUSED_FOR_DAYS_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: ai_licensing
core:
  summary: Refuse to reclaim license until the condition holds
  inputs:
    last_used_at:
      type: string
      required: true
  outputs:
    is_inactive:
      type: boolean
      required: true
  result_status_contract:
    allowed:
    - BACKEND_ERROR
    - SUCCESS
    - VIOLATION
    on_input_failure: VIOLATION
  pipeline:
  - step: read_now
    side_effect: capability_side_effects::CS_CLOCK_V0
    op: NOW
    inputs: {}
    outputs:
      timestamp: $.capability_result.timestamp
    result_surface:
    - SUCCESS
    - BACKEND_ERROR
    on_result:
      SUCCESS: continue
      BACKEND_ERROR: exit
  - step: evaluate_unused_for_days
    transform: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    inputs:
      last_active_date: $.inputs.last_used_at
      evaluation_date: $.results.read_now.timestamp
      threshold_days: 30
    outputs:
      is_inactive: $.capability_result.is_inactive
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: exit
      VIOLATION: exit
```

---

## Intent

Refuse to reclaim license until the condition holds
