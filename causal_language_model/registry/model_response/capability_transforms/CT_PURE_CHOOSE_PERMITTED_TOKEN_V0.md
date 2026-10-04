# CT_PURE_CHOOSE_PERMITTED_TOKEN_V0

## Machine

```yaml
fqdn: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: capability_transforms::CONSTITUTION_DETERMINISTIC_ATOMS_V0
authority: pgc.platform
concern: model_response
core:
  summary: Stops forbidden tokens among those offered and chooses one permitted token, joined as it is,
    within the permitted length
  refusal: raises
  inputs:
    state:
      type: object
      required: true
    candidates:
      type: array
      required: true
  outputs:
    step:
      type: object
      required: true
    text:
      type: string
      required: true
    finished:
      type: boolean
      required: true
    stopped_by:
      type: string
      required: true
    within_length:
      type: boolean
      required: true
machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: CHOOSE_PERMITTED_TOKEN
  implementation:
    module: causal_language_model.implementation.capability_transforms.atoms.ct_pure_choose_permitted_token_v0
    callable: execute
```

---

## Intent

Stops forbidden tokens among those offered and chooses one permitted token, joined as it is, within the permitted length
