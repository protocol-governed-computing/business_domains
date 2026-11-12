# CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0

## Machine

```yaml
fqdn: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: model_response
core:
  summary: Confirm the requester may act for the customer the user prompt is for
  inputs:
    customer_id:
      type: string
      required: true
    permitted_customers:
      type: array
      required: true
  outputs:
    acts_for_customer:
      type: boolean
      required: true
  result_status_contract:
    allowed:
    - SUCCESS
    - VIOLATION
    on_input_failure: VIOLATION
  pipeline:
  - step: confirm_acts_for_customer
    transform: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    inputs:
      value: $.inputs.customer_id
      allowed_set: $.inputs.permitted_customers
    outputs:
      acts_for_customer: $.capability_result.is_member
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: exit
      VIOLATION: exit
```

---

## Intent

Confirm the requester may act for the customer the user prompt is for
