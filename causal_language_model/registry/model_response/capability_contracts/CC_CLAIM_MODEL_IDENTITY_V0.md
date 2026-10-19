# CC_CLAIM_MODEL_IDENTITY_V0

## Machine

```yaml
fqdn: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: model_response
core:
  summary: Claim a model's identity so a second registration of the same model is refused
  inputs:
    description:
      type: object
      required: true
    description_schema:
      type: object
      required: true
    fingerprint:
      type: string
      required: true
  outputs:
    identity_key:
      type: string
      required: true
    address:
      type: string
      required: true
  result_status_contract:
    allowed:
    - VIOLATION
    - SUCCESS
    - ALREADY_EXISTS
    - BACKEND_ERROR
    on_input_failure: VIOLATION
  pipeline:
  - step: validate_description
    transform: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    inputs:
      record: $.inputs.description
      schema: $.inputs.description_schema
    outputs:
      violations: $.capability_result.violations
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: require_description_complete
    transform: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    inputs:
      parameters:
        violations: $.results.validate_description.violations
      rules:
      - field: violations
        op: eq
        value: []
    outputs:
      valid: $.capability_result.valid
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: form_identity_key
    transform: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    inputs:
      description: $.inputs.description
      fingerprint: $.inputs.fingerprint
    outputs:
      identity_key: $.capability_result.identity_key
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: claim_identity
    side_effect: capability_side_effects::CS_REGISTRY_V0
    op: REGISTER
    store: MODEL_IDENTITY_REGISTRY
    inputs:
      key: $.results.form_identity_key.identity_key
      target_cs: CS_MUTABLE_JSON_V0
      target_ref: MODELS
    outputs:
      address: $.capability_result.address
      result_status: $.result_status
    result_surface:
    - SUCCESS
    - ALREADY_EXISTS
    - VIOLATION
    - BACKEND_ERROR
    on_result:
      SUCCESS: exit
      ALREADY_EXISTS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
```

---

## Intent

Claim a model's identity so a second registration of the same model is refused
