# CC_CONFIRM_OFFER_FOR_MODEL_V0

## Machine

```yaml
fqdn: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: model_response
core:
  summary: Refuse an offer naming another model's fingerprint
  inputs:
    offered_fingerprint:
      type: string
      required: true
    admitted_fingerprint:
      type: string
      required: true
  outputs:
    offer_for_model:
      type: boolean
      required: true
  result_status_contract:
    allowed:
    - SUCCESS
    - VIOLATION
    on_input_failure: VIOLATION
  pipeline:
  - step: confirm_same_model
    transform: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    inputs:
      value: $.inputs.offered_fingerprint
      allowed_set:
      - $.inputs.admitted_fingerprint
    outputs:
      offer_for_model: $.capability_result.is_member
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: exit
      VIOLATION: exit
```

---

## Intent

Refuse an offer naming another model's fingerprint
