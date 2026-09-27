# TEST_DATA_CT_WRITE_RESPONSE_V0

## Machine

```yaml
fqdn: causal_language_model::TEST_DATA_CT_WRITE_RESPONSE_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V2
authority: pgc.platform
concern: model_response
target: causal_language_model::CT_WRITE_RESPONSE_V0
cases:
- case_id: writes_a_finished_response_and_offers_nothing_after
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
    positions:
    - 1
    - 2
    - 3
    - 4
  expected:
    result:
      text: Your balance
      finished: true
      stopped_by: none
      stopped:
      - position: 1
        word: '87654321'
        rule: another_customers_account_number
  recorded:
    written[0]/offered:
      candidates:
      - word: '87654321'
        likelihood: 0.6
      - word: Your
        likelihood: 0.3
    written[1]/offered:
      candidates:
      - word: balance
        likelihood: 0.9
    written[2]/offered:
      candidates:
      - word: <end>
        likelihood: 0.9
    written[3]/offered:
      candidates: []
- case_id: stops_unfinished_at_the_longest_response
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
    positions:
    - 1
  expected:
    result:
      text: Your
      finished: false
      stopped_by: none
      stopped: []
  recorded:
    written[0]/offered:
      candidates:
      - word: Your
        likelihood: 0.9
```

---

## Intent


