# CT_IMPURE_OFFER_NEXT_WORDS_V0

## Machine

```yaml
fqdn: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: capability_transforms::CONSTITUTION_NONDETERMINISTIC_ATOMS_V0
authority: pgc.platform
concern: model_response
core:
  summary: 'The model''s step: offers its next words given the response so far; the one step whose result
    is not determined by its inputs'
  refusal: never
  inputs:
    reading:
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
  outputs:
    candidates:
      type: array
      required: true
machine:
  ct_kind: atom
  ct_purity: ct_impure
  operation: OFFER_NEXT_WORDS
  implementation:
    module: causal_language_model.implementation.capability_transforms.atoms.ct_impure_offer_next_words_v0
    callable: execute
```

---

## Intent

The model's step: offers its next words given the response so far; the one step whose result is not determined by its inputs
