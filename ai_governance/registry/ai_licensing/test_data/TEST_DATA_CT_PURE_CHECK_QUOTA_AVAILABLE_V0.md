# TEST_DATA_CT_PURE_CHECK_QUOTA_AVAILABLE_V0

## Machine

```yaml
fqdn: ai_governance::TEST_DATA_CT_PURE_CHECK_QUOTA_AVAILABLE_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V2
authority: pgc.platform
concern: ai_licensing
target: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
cases:
- case_id: available_under_cap
  expected_outcome: SUCCESS
  bindings:
    assigned_count: 5
    quota: 10
  expected:
    quota_available: true
    remaining: 5
- case_id: refuses_at_cap
  expected_outcome: VIOLATION
  bindings:
    assigned_count: 10
    quota: 10
```

---

## Intent


