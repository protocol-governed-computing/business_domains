# TEST_DATA_CT_PURE_READ_HOSTED_STATE_V0

## Machine

```yaml
fqdn: causal_language_model::TEST_DATA_CT_PURE_READ_HOSTED_STATE_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V2
authority: pgc.platform
concern: model_response
target: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
cases:
- case_id: reduces_the_trail_to_the_response_as_built
  expected_outcome: SUCCESS
  bindings:
    entries:
    - sequence_number: 1
      record:
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
    - sequence_number: 2
      record:
        outcome: STEP
        chosen: Your
    - sequence_number: 3
      record:
        outcome: STEP
        chosen: ' balance'
  expected:
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
- case_id: refuses_a_request_never_admitted
  expected_outcome: VIOLATION
  bindings:
    entries:
    - sequence_number: 1
      record:
        outcome: REFUSED
        reason: model_not_registered
- case_id: refuses_a_closed_request
  expected_outcome: VIOLATION
  bindings:
    entries:
    - sequence_number: 1
      record:
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
    - sequence_number: 2
      record:
        outcome: RESPONDED
```

---

## Intent


