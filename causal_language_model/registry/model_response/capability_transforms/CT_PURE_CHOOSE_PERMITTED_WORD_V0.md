# CT_PURE_CHOOSE_PERMITTED_WORD_V0

## Machine

```yaml
fqdn: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: capability_transforms::CONSTITUTION_DETERMINISTIC_ATOMS_V0
authority: pgc.platform
concern: model_response
core:
  summary: Stops forbidden words among those offered and chooses one permitted word under the freedom
    of word choice and a stated seed
  refusal: returns
  inputs:
    candidates:
      type: array
      required: true
    rules_in_force:
      type: object
      required: true
    position:
      type: integer
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
    stopped:
      type: array
      required: true
  outputs:
    text:
      type: string
      required: true
    finished:
      type: boolean
      required: true
    stopped_by:
      type: string
      required: true
    stopped:
      type: array
      required: true
machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: CHOOSE_PERMITTED_WORD
  implementation:
    module: causal_language_model.implementation.capability_transforms.atoms.ct_pure_choose_permitted_word_v0
    callable: execute
```

---

## Intent

Stops forbidden words among those offered and chooses one permitted word under the freedom of word choice and a stated seed
