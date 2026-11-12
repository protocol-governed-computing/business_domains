# CT_PURE_COMPARE_SENSITIVITY_V0

## Machine

```yaml
fqdn: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: capability_transforms::CONSTITUTION_DETERMINISTIC_ATOMS_V0
authority: pgc.platform
concern: model_response
core:
  summary: Decides whether a kind of information is no more sensitive than a ceiling, by the declared
    order
  refusal: raises
  inputs:
    kind:
      type: string
      required: true
    ceiling:
      type: string
      required: true
    kinds:
      type: array
      required: true
  outputs:
    within_ceiling:
      type: boolean
      required: true
machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: COMPARE_SENSITIVITY
  implementation:
    module: causal_language_model.implementation.capability_transforms.atoms.ct_pure_compare_sensitivity_v0
    callable: execute
```

---

## Intent

Decides whether a kind of information is no more sensitive than a ceiling, by the declared order
