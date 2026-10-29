# CC_WRITE_LICENSE_V0

## Machine

```yaml
fqdn: ai_governance::CC_WRITE_LICENSE_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: ai_licensing
core:
  summary: Write a new license in its first state
  inputs:
    license_id:
      type: string
      required: true
    submission:
      type: object
      required: true
  outputs:
    result_status:
      type: string
      required: true
  result_status_contract:
    allowed:
    - BACKEND_ERROR
    - VIOLATION
    - SUCCESS
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
  - step: assemble_license_record
    transform: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    inputs:
      fields:
        license_id: $.inputs.license_id
        last_used_at: $.results.read_now.timestamp
        employee_id: $.inputs.submission.employee_id
        tier: $.inputs.submission.tier
        state: ACTIVE
    outputs:
      license_record: $.capability_result.record
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: write_license_record
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: WRITE
    store: LICENSES
    inputs:
      key: $.inputs.license_id
      value: $.results.assemble_license_record.license_record
    outputs:
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

Write a new license in its first state
