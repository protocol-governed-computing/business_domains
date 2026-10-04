# TEST_DATA_CT_PURE_COMPARE_SENSITIVITY_V0

## Machine

```yaml
fqdn: causal_language_model::TEST_DATA_CT_PURE_COMPARE_SENSITIVITY_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V2
authority: pgc.platform
concern: model_response
target: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
cases:
- case_id: admits_kind_within_ceiling
  expected_outcome: SUCCESS
  bindings:
    kind: internal
    ceiling: confidential
    kinds:
    - public
    - internal
    - confidential
    - restricted
  expected:
    within_ceiling: true
- case_id: refuses_kind_above_ceiling
  expected_outcome: VIOLATION
  bindings:
    kind: restricted
    ceiling: internal
    kinds:
    - public
    - internal
    - confidential
    - restricted
```

---

## Intent


