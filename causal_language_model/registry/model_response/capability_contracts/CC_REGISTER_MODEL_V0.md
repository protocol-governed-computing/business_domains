# CC_REGISTER_MODEL_V0

## Machine

```yaml
fqdn: causal_language_model::CC_REGISTER_MODEL_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: model_response
core:
  summary: Record a model's description and fingerprint as its record, registered
  inputs:
    identity_key:
      type: string
      required: true
    description:
      type: object
      required: true
    fingerprint:
      type: string
      required: true
  outputs:
    model_record:
      type: object
      required: true
  result_status_contract:
    allowed:
    - VIOLATION
    - SUCCESS
    - BACKEND_ERROR
    on_input_failure: VIOLATION
  pipeline:
  - step: assemble_model_record
    transform: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    inputs:
      fields:
        identity_key: $.inputs.identity_key
        description: $.inputs.description
        fingerprint: $.inputs.fingerprint
        state: REGISTERED
        time_in_service_id: ''
    outputs:
      model_record: $.capability_result.record
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: write_model_record
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: WRITE
    store: MODELS
    inputs:
      key: $.inputs.identity_key
      value: $.results.assemble_model_record.model_record
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

Record a model's description and fingerprint as its record, registered
