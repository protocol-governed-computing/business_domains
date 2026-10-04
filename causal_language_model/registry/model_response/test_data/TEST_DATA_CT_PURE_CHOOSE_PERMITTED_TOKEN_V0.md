# TEST_DATA_CT_PURE_CHOOSE_PERMITTED_TOKEN_V0

## Machine

```yaml
fqdn: causal_language_model::TEST_DATA_CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V2
authority: pgc.platform
concern: model_response
target: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
cases:
- case_id: stops_an_account_number_split_across_tokens
  expected_outcome: SUCCESS
  bindings:
    state:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
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
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
      position: 1
      text: Account 8765
      finished: false
      limit: 3
    candidates:
    - token: '4321'
      likelihood: 0.7
    - token: ' is'
      likelihood: 0.2
  expected:
    text: Account 8765 is
    finished: false
    stopped_by: none
    within_length: true
    step:
      position: 2
      candidates:
      - token: '4321'
        likelihood: 0.7
      - token: ' is'
        likelihood: 0.2
      chosen: ' is'
      stopped:
      - token: '4321'
        rule: another_customers_account_number
      stopped_by: none
      finished: false
      within_length: true
- case_id: writes_the_customers_own_account_across_tokens
  expected_outcome: SUCCESS
  bindings:
    state:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
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
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
      position: 1
      text: Account 1234
      finished: false
      limit: 3
    candidates:
    - token: '5678'
      likelihood: 0.8
  expected:
    text: Account 12345678
    stopped_by: none
    step:
      position: 2
      candidates:
      - token: '5678'
        likelihood: 0.8
      chosen: '5678'
      stopped: []
      stopped_by: none
      finished: false
      within_length: true
    finished: false
    within_length: true
- case_id: names_the_rule_when_no_permitted_token_remains
  expected_outcome: SUCCESS
  bindings:
    state:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
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
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
      position: 0
      text: ''
      finished: false
      limit: 3
    candidates:
    - token: '87654321'
      likelihood: 0.9
  expected:
    text: ''
    stopped_by: another_customers_account_number
    finished: false
    step:
      position: 1
      candidates:
      - token: '87654321'
        likelihood: 0.9
      chosen: null
      stopped:
      - token: '87654321'
        rule: another_customers_account_number
      stopped_by: another_customers_account_number
      finished: false
      within_length: true
    within_length: true
- case_id: passes_the_permitted_length_unfinished
  expected_outcome: SUCCESS
  bindings:
    state:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
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
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
      position: 3
      text: Your balance is
      finished: false
      limit: 3
    candidates:
    - token: ' today'
      likelihood: 0.9
  expected:
    text: Your balance is today
    within_length: false
    finished: false
    step:
      position: 4
      candidates:
      - token: ' today'
        likelihood: 0.9
      chosen: ' today'
      stopped: []
      stopped_by: none
      finished: false
      within_length: false
    stopped_by: none
- case_id: finishes_on_the_end_of_the_response
  expected_outcome: SUCCESS
  bindings:
    state:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
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
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
      position: 2
      text: Your balance
      finished: false
      limit: 3
    candidates:
    - token: <end>
      likelihood: 0.9
  expected:
    text: Your balance
    finished: true
    within_length: true
    step:
      position: 3
      candidates:
      - token: <end>
        likelihood: 0.9
      chosen: <end>
      stopped: []
      stopped_by: none
      finished: true
      within_length: true
    stopped_by: none
- case_id: judges_a_lookalike_digit_as_the_digit
  expected_outcome: SUCCESS
  bindings:
    state:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
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
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
      position: 2
      text: Spouse account 8765432
      finished: false
      limit: 3
    candidates:
    - token: ₁
      likelihood: 0.8
    - token: .
      likelihood: 0.1
  expected:
    text: Spouse account 8765432.
    stopped_by: none
    step:
      position: 3
      candidates:
      - token: ₁
        likelihood: 0.8
      - token: .
        likelihood: 0.1
      chosen: .
      stopped:
      - token: ₁
        rule: another_customers_account_number
      stopped_by: none
      finished: false
      within_length: true
    finished: false
    within_length: true
- case_id: does_not_begin_a_forbidden_number_the_model_read
  expected_outcome: SUCCESS
  bindings:
    state:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
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
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
      position: 2
      text: 'Spouse account '
      finished: false
      limit: 3
    candidates:
    - token: '8'
      likelihood: 0.8
    - token: withheld
      likelihood: 0.1
  expected:
    text: Spouse account withheld
    stopped_by: none
    step:
      position: 3
      candidates:
      - token: '8'
        likelihood: 0.8
      - token: withheld
        likelihood: 0.1
      chosen: withheld
      stopped:
      - token: '8'
        rule: another_customers_account_number
      stopped_by: none
      finished: false
      within_length: true
    finished: false
    within_length: true
- case_id: begins_a_number_the_model_read_that_is_permitted
  expected_outcome: SUCCESS
  bindings:
    state:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
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
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
      position: 2
      text: 'Balance '
      finished: false
      limit: 3
    candidates:
    - token: '4'
      likelihood: 0.8
  expected:
    text: Balance 4
    stopped_by: none
    step:
      position: 3
      candidates:
      - token: '4'
        likelihood: 0.8
      chosen: '4'
      stopped: []
      stopped_by: none
      finished: false
      within_length: true
    finished: false
    within_length: true
- case_id: grounded_writes_a_number_it_read
  expected_outcome: SUCCESS
  bindings:
    state:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
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
        ground_numbers: true
        maximum_response_length: 3
        longest_response: 5
      position: 2
      text: Balance 4
      finished: false
      limit: 3
    candidates:
    - token: '9'
      likelihood: 0.8
    - token: '0'
      likelihood: 0.1
  expected:
    text: Balance 40
    stopped_by: none
    step:
      position: 3
      candidates:
      - token: '9'
        likelihood: 0.8
      - token: '0'
        likelihood: 0.1
      chosen: '0'
      stopped:
      - token: '9'
        rule: numbers_from_the_reading
      stopped_by: none
      finished: false
      within_length: true
    finished: false
    within_length: true
- case_id: grounded_does_not_change_a_value_it_read
  expected_outcome: SUCCESS
  bindings:
    state:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
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
        ground_numbers: true
        maximum_response_length: 3
        longest_response: 5
      position: 2
      text: Balance 4
      finished: false
      limit: 3
    candidates:
    - token: ' dollars'
      likelihood: 0.8
    - token: <end>
      likelihood: 0.1
  expected:
    text: Balance 4
    stopped_by: numbers_from_the_reading
    step:
      position: 3
      candidates:
      - token: ' dollars'
        likelihood: 0.8
      - token: <end>
        likelihood: 0.1
      chosen: null
      stopped:
      - token: ' dollars'
        rule: numbers_from_the_reading
      - token: <end>
        rule: numbers_from_the_reading
      stopped_by: numbers_from_the_reading
      finished: false
      within_length: true
    finished: false
    within_length: true
- case_id: ungrounded_writes_a_number_it_did_not_read
  expected_outcome: SUCCESS
  bindings:
    state:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
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
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
      position: 2
      text: 'Balance '
      finished: false
      limit: 3
    candidates:
    - token: '9'
      likelihood: 0.8
  expected:
    text: Balance 9
    stopped_by: none
    step:
      position: 3
      candidates:
      - token: '9'
        likelihood: 0.8
      chosen: '9'
      stopped: []
      stopped_by: none
      finished: false
      within_length: true
    finished: false
    within_length: true
- case_id: refuses_an_offer_for_a_complete_response
  expected_outcome: VIOLATION
  bindings:
    state:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
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
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
      position: 2
      text: Your balance
      finished: true
      limit: 3
    candidates:
    - token: ' more'
      likelihood: 0.9
```

---

## Intent


