# CT_PURE_READ_HOSTED_STATE_V0

## Machine

```yaml
fqdn: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: capability_transforms::CONSTITUTION_DETERMINISTIC_ATOMS_V0
authority: pgc.platform
concern: model_response
core:
  summary: Reduces a hosted request's trail to the response as built, its position, whether it is complete,
    and its permitted length
  refusal: raises
  inputs:
    entries:
      type: array
      required: true
  outputs:
    state:
      type: object
      required: true
machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: READ_HOSTED_STATE
  implementation:
    module: causal_language_model.implementation.capability_transforms.atoms.ct_pure_read_hosted_state_v0
    callable: execute
```

---

## Intent

Reduces a hosted request's trail to the response as built, its position, whether it is complete, and its permitted length
