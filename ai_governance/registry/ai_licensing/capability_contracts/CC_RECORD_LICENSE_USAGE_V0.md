# CC_RECORD_LICENSE_USAGE_V0

## Machine

```yaml
fqdn: ai_governance::CC_RECORD_LICENSE_USAGE_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: ai_licensing
core:
  summary: Set what record license usage records on the license
  inputs:
    license_id:
      type: string
      required: true
  outputs:
    updated_count:
      type: integer
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
  - step: set_record
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: UPDATE_WHERE
    store: LICENSES
    inputs:
      filter:
        license_id: $.inputs.license_id
        state: ACTIVE
      updates:
        last_used_at: $.results.read_now.timestamp
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

Set what record license usage records on the license
