# CC_CLAIM_ACTION_IDENTITY_V0

## Machine

```yaml
fqdn: ai_governance::CC_CLAIM_ACTION_IDENTITY_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: agent_governance
core:
  summary: Claim a action's action id
  inputs:
    tool_name:
      type: string
      required: true
    requesting_user_id:
      type: string
      required: true
    domain_context:
      type: string
      required: true
    action_fields:
      type: object
      required: true
  outputs:
    action_id:
      type: string
      required: true
  result_status_contract:
    allowed:
    - VIOLATION
    - ALREADY_EXISTS
    - BACKEND_ERROR
    - SUCCESS
    on_input_failure: VIOLATION
  pipeline:
  - step: form_action_id
    transform: capability_transforms::CT_PURE_GENERATE_ID_V0
    inputs:
      data:
        tool_name: $.inputs.tool_name
        requesting_user_id: $.inputs.requesting_user_id
        domain_context: $.inputs.domain_context
      prefix: AGOV
    outputs:
      action_id: $.capability_result.id
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: claim_id
    side_effect: capability_side_effects::CS_REGISTRY_V0
    op: REGISTER
    store: ACTION_IDENTITY_REGISTRY
    inputs:
      key: $.results.form_action_id.action_id
      target_cs: capability_side_effects::CS_MUTABLE_JSON_V0
      target_ref: ACTIONS
    outputs:
      address: $.capability_result.address
      result_status: $.result_status
    result_surface:
    - SUCCESS
    - ALREADY_EXISTS
    - VIOLATION
    - BACKEND_ERROR
    on_result:
      SUCCESS: continue
      ALREADY_EXISTS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
  - step: assemble_action_record
    transform: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    inputs:
      fields: $.inputs.action_fields
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
      key: $.results.form_action_id.action_id
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

Claim a action's action id
