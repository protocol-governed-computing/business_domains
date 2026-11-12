# CT_WRITE_RESPONSE_V0

## Machine

```yaml
fqdn: causal_language_model::CT_WRITE_RESPONSE_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: capability_transforms::CONSTITUTION_MOLECULES_V0
authority: pgc.platform
concern: model_response
core:
  summary: Writes a response by repeating one pass per word, up to the longest response, carrying the
    response so far and the words stopped
  refusal: returns
  inputs:
    reading:
      type: object
      required: true
    rules_in_force:
      type: object
      required: true
    positions:
      type: array
      required: true
  outputs:
    result:
      type: object
      required: true
machine:
  ct_kind: molecule
  ct_purity: ct_impure
  operation: WRITE_RESPONSE
  atom_stream:
  - kind: loop
    molecule: causal_language_model::CT_WRITE_NEXT_WORD_V0
    as: written
    over: $.inputs.positions
    iterator: position
    accumulator:
      text: ''
      finished: false
      stopped_by: none
      stopped: []
    inputs:
      position: $.iterator
      reading: $.inputs.reading
      rules_in_force: $.inputs.rules_in_force
      text: $.accumulator.text
      finished: $.accumulator.finished
      stopped_by: $.accumulator.stopped_by
      stopped: $.accumulator.stopped
    update_accumulator:
      text: $.results.text
      finished: $.results.finished
      stopped_by: $.results.stopped_by
      stopped: $.results.stopped
  emit:
    result: written
```

---

## Intent

Writes a response by repeating one pass per word, up to the longest response, carrying the response so far and the words stopped
