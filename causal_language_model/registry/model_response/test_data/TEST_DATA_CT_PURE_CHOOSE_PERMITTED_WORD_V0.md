# TEST_DATA_CT_PURE_CHOOSE_PERMITTED_WORD_V0

## Machine

```yaml
fqdn: causal_language_model::TEST_DATA_CT_PURE_CHOOSE_PERMITTED_WORD_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V2
authority: pgc.platform
concern: model_response
target: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
cases:
- case_id: stops_another_customers_account_and_continues
  expected_outcome: SUCCESS
  bindings:
    candidates:
    - word: '87654321'
      likelihood: 0.6
    - word: Your
      likelihood: 0.3
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
    text: Your
    finished: false
    stopped_by: none
    stopped:
    - position: 1
      word: '87654321'
      rule: another_customers_account_number
- case_id: stops_an_account_number_written_across_two_words
  expected_outcome: SUCCESS
  bindings:
    candidates:
    - word: '4321'
      likelihood: 0.7
    - word: is
      likelihood: 0.2
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
    position: 3
    text: Account 8765
    finished: false
    stopped_by: none
    stopped: []
  expected:
    text: Account 8765 is
    finished: false
    stopped_by: none
    stopped:
    - position: 3
      word: '4321'
      rule: another_customers_account_number
- case_id: writes_the_customers_own_account_across_two_words
  expected_outcome: SUCCESS
  bindings:
    candidates:
    - word: '5678'
      likelihood: 0.8
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
    position: 3
    text: Account 1234
    finished: false
    stopped_by: none
    stopped: []
  expected:
    text: Account 1234 5678
    finished: false
    stopped_by: none
    stopped: []
- case_id: names_the_rule_when_no_permitted_word_remains
  expected_outcome: SUCCESS
  bindings:
    candidates:
    - word: '87654321'
      likelihood: 0.9
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
    text: ''
    finished: false
    stopped_by: another_customers_account_number
    stopped:
    - position: 1
      word: '87654321'
      rule: another_customers_account_number
- case_id: draws_an_adventurous_word_from_the_seed
  expected_outcome: SUCCESS
  bindings:
    candidates:
    - word: balance
      likelihood: 0.6
    - word: savings
      likelihood: 0.3
    - word: loan
      likelihood: 0.1
    rules_in_force:
      forbidden:
      - rule: no_guarantees
        pattern: \bguaranteed\b
      - rule: another_customers_account_number
        pattern: '[0-9](?:[ -]?[0-9]){7}'
        except:
        - '12345678'
      freedom: 1
      seed: 7
    position: 2
    text: Your
    finished: false
    stopped_by: none
    stopped: []
  expected:
    text: Your savings
    finished: false
    stopped_by: none
    stopped: []
- case_id: finishes_on_the_end_of_the_response
  expected_outcome: SUCCESS
  bindings:
    candidates:
    - word: <end>
      likelihood: 0.9
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
    position: 3
    text: Your balance
    finished: false
    stopped_by: none
    stopped: []
  expected:
    text: Your balance
    finished: true
    stopped_by: none
    stopped: []
```

---

## Intent


