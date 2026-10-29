# CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0

## Machine

```yaml
fqdn: ai_governance::CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: agent_governance
core:
  summary: Record a moment on the agent_governance's own trail
  inputs:
    occurrence:
      type: string
      required: true
    tool_name:
      type: string
    requesting_user_id:
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
        decision: $.inputs.occurrence
        tool_name: $.inputs.tool_name
        requesting_user_id: $.inputs.requesting_user_id
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
    store: GOVERNANCE_AUDIT
    inputs:
      record: $.results.assemble_occurrence.record
      stream_id: GOVERNANCE_AUDIT
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

Record a moment on the agent_governance's own trail
