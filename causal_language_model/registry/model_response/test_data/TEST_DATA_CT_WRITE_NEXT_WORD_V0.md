# TEST_DATA_CT_WRITE_NEXT_WORD_V0

## Machine

```yaml
fqdn: causal_language_model::TEST_DATA_CT_WRITE_NEXT_WORD_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V2
authority: pgc.platform
concern: model_response
target: causal_language_model::CT_WRITE_NEXT_WORD_V0
cases:
- case_id: writes_one_permitted_word_from_a_recorded_offer
  expected_outcome: SUCCESS
  bindings:
    reading:
      system_prompt: Answer briefly.
      question: What is my balance?
      supporting_material: Account 12345678 balance 40.
    rules_in_force:
      forbidden:
      - rule: no_guarantees
        pattern: \bguaranteed\b
      - rule: another_customers_account_number
        pattern: '[0-9](?:[ -]?[0-9]){7}'
        except:
        - '12345678'
      freedom: 0
      seed: 7
    position: 1
    text: ''
    finished: false
    stopped_by: none
    stopped: []
  expected:
    result:
      text: Your
      finished: false
      stopped_by: none
      stopped:
      - position: 1
        word: '87654321'
        rule: another_customers_account_number
  recorded:
    offered:
      candidates:
      - word: '87654321'
        likelihood: 0.6
      - word: Your
        likelihood: 0.3
```

---

## Intent


