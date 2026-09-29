# TEST_DATA_CT_PURE_CHECK_TRAINING_STATUS_V0

## Machine

```yaml
fqdn: ai_governance::TEST_DATA_CT_PURE_CHECK_TRAINING_STATUS_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V2
authority: pgc.platform
concern: ai_licensing
target: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
cases:
- case_id: eligible_once_trained
  expected_outcome: SUCCESS
  bindings:
    training_completed: true
  expected:
    training_eligible: true
- case_id: refuses_untrained
  expected_outcome: VIOLATION
  bindings:
    training_completed: false
```

---

## Intent


