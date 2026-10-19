# CT_WRITE_NEXT_WORD_V0

## Machine

```yaml
fqdn: causal_language_model::CT_WRITE_NEXT_WORD_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: capability_transforms::CONSTITUTION_MOLECULES_V0
authority: pgc.platform
concern: model_response
core:
  summary: One pass of writing, composed of the model's offer and the rules' choice
  refusal: returns
  inputs:
    reading:
      type: object
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
    result:
      type: object
      required: true
machine:
  ct_kind: molecule
  ct_purity: ct_impure
  operation: WRITE_NEXT_WORD
  atom_stream:
  - kind: atom
    atom: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    as: offered
    with:
      reading: $.inputs.reading
      text: $.inputs.text
      finished: $.inputs.finished
      stopped_by: $.inputs.stopped_by
  - kind: atom
    atom: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    as: chosen
    with:
      candidates: $.results.offered.candidates
      rules_in_force: $.inputs.rules_in_force
      position: $.inputs.position
      text: $.inputs.text
      finished: $.inputs.finished
      stopped_by: $.inputs.stopped_by
      stopped: $.inputs.stopped
  emit:
    result: chosen
```

---

## Intent

One pass of writing, composed of the model's offer and the rules' choice
