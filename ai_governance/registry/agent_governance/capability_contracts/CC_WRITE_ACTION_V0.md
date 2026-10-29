# CC_WRITE_ACTION_V0

## Machine

```yaml
fqdn: ai_governance::CC_WRITE_ACTION_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: agent_governance
core:
  summary: Write a new action in its first state
  inputs:
    action_id:
      type: string
      required: true
    submission:
      type: object
      required: true
    request_identity:
      type: string
      required: true
  outputs:
    result_status:
      type: string
      required: true
  result_status_contract:
    allowed:
    - VIOLATION
    - SUCCESS
    - BACKEND_ERROR
    on_input_failure: VIOLATION
  pipeline:
  - step: assemble_action_record
    transform: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    inputs:
      fields:
        action_id: $.inputs.action_id
        tool_name: $.inputs.submission.tool_name
        requesting_user_id: $.inputs.submission.requesting_user_id
        request_identity: $.inputs.request_identity
    outputs:
      action_record: $.capability_result.record
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: write_action_record
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: WRITE
    store: ACTIONS
    inputs:
      key: $.inputs.action_id
      value: $.results.assemble_action_record.action_record
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

Write a new action in its first state
