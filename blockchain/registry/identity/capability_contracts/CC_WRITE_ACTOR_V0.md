# CC_WRITE_ACTOR_V0

## Machine

```yaml
fqdn: blockchain::CC_WRITE_ACTOR_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: identity
core:
  summary: Write a new actor in its first state
  inputs:
    contact_address:
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
    - VIOLATION
    - SUCCESS
    - BACKEND_ERROR
    on_input_failure: VIOLATION
  pipeline:
  - step: assemble_actor_record
    transform: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    inputs:
      fields:
        contact_address: $.inputs.submission.contact_address
        name: $.inputs.submission.name
        currency_preference: $.inputs.submission.currency_preference
        language: $.inputs.submission.language
        state: UNVERIFIED
    outputs:
      actor_record: $.capability_result.record
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: write_actor_record
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: WRITE
    store: ACTORS
    inputs:
      key: $.inputs.contact_address
      value: $.results.assemble_actor_record.actor_record
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

Write a new actor in its first state
