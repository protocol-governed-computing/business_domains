# CT_PURE_FORM_RESPONSE_RULES_V0

## Machine

```yaml
fqdn: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0
authority: pgc.platform
concern: model_response
core:
  summary: Forms the response rules in force for one user prompt from the time in service and the customer's
    account numbers
  refusal: never
  inputs:
    response_rules:
      type: object
      required: true
    account_numbers:
      type: array
      required: true
    seed:
      type: integer
      required: true
  outputs:
    rules_in_force:
      type: object
      required: true
    positions:
      type: array
      required: true
machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: FORM_RESPONSE_RULES
  implementation:
    module: causal_language_model.implementation.capability_transforms.atoms.ct_pure_form_response_rules_v0
    callable: execute
```

---

## Intent

Forms the response rules in force for one user prompt from the time in service and the customer's account numbers
