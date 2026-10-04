# TEST_DATA_CT_PURE_FORM_RESPONSE_RULES_V0

## Machine

```yaml
fqdn: causal_language_model::TEST_DATA_CT_PURE_FORM_RESPONSE_RULES_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V2
authority: pgc.platform
concern: model_response
target: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
cases:
- case_id: adds_the_account_rule_and_positions
  expected_outcome: SUCCESS
  bindings:
    response_rules:
      forbidden:
      - rule: no_guarantees
        pattern: \bguaranteed\b
      account_number_pattern: '[0-9](?:[ -]?[0-9]){7}'
      freedom: 0
      longest_response: 3
    account_numbers:
    - '12345678'
    seed: 7
  expected:
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
```

---

## Intent


