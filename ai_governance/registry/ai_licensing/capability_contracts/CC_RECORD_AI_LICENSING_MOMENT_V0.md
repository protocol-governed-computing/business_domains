# CC_RECORD_AI_LICENSING_MOMENT_V0

## Machine

```yaml
fqdn: ai_governance::CC_RECORD_AI_LICENSING_MOMENT_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: ai_licensing
core:
  summary: Record a moment on the ai_licensing's own trail
  inputs:
    occurrence:
      type: string
      required: true
    employee_id:
      type: string
    license_id:
      type: string
    tier:
      type: string
    reason:
      type: string
  outputs:
    sequence_number:
      type: integer
      required: true
  result_status_contract:
    allowed:
    - VIOLATION
    - SUCCESS
    - BACKEND_ERROR
    on_input_failure: VIOLATION
  pipeline:
  - step: assemble_occurrence
    transform: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    inputs:
      fields:
        occurrence: $.inputs.occurrence
        employee_id: $.inputs.employee_id
        license_id: $.inputs.license_id
        tier: $.inputs.tier
        reason: $.inputs.reason
    outputs:
      record: $.capability_result.record
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: append_occurrence
    side_effect: capability_side_effects::CS_APPENDONLY_JSONL_V0
    op: APPEND
    store: LICENSE_AUDIT
    inputs:
      record: $.results.assemble_occurrence.record
      stream_id: LICENSE_AUDIT
    outputs:
      sequence_number: $.capability_result.sequence_number
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

Record a moment on the ai_licensing's own trail
