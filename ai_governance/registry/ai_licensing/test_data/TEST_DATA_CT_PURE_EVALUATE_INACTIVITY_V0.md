# TEST_DATA_CT_PURE_EVALUATE_INACTIVITY_V0

## Machine

```yaml
fqdn: ai_governance::TEST_DATA_CT_PURE_EVALUATE_INACTIVITY_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V2
authority: pgc.platform
concern: ai_licensing
target: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
cases:
- case_id: inactive_past_threshold
  expected_outcome: SUCCESS
  bindings:
    last_active_date: '2024-01-01T00:00:00Z'
    evaluation_date: '2024-02-15T00:00:00Z'
    threshold_days: 30
  expected:
    is_inactive: true
    days_inactive: 45
- case_id: inactive_at_threshold
  expected_outcome: SUCCESS
  bindings:
    last_active_date: '2024-01-16T00:00:00Z'
    evaluation_date: '2024-02-15T00:00:00Z'
    threshold_days: 30
  expected:
    is_inactive: true
    days_inactive: 30
- case_id: refuses_recently_used
  expected_outcome: VIOLATION
  bindings:
    last_active_date: '2024-02-10T00:00:00Z'
    evaluation_date: '2024-02-15T00:00:00Z'
    threshold_days: 30
```

---

## Intent


