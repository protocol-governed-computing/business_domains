# TEST_DATA_CT_IMPURE_OFFER_NEXT_WORDS_V0

## Machine

```yaml
fqdn: causal_language_model::TEST_DATA_CT_IMPURE_OFFER_NEXT_WORDS_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V2
authority: pgc.platform
concern: model_response
target: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
cases:
- case_id: offers_candidates
  expected_outcome: SUCCESS
  bindings:
    reading:
      system_prompt: Answer briefly.
      question: What is my balance?
      supporting_material: Account 12345678 balance 40.
    text: ''
    finished: false
    stopped_by: none
  assertions:
    candidates:
      mode: property
      type: non_zero
```

---

## Intent


