# TEST_DATA_CT_PURE_GROUP_RECORDS_V0

## Machine

```yaml
fqdn: book_library_mgmt::TEST_DATA_CT_PURE_GROUP_RECORDS_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V2
authority: pgc.platform
concern: catalog
target: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
cases:
- case_id: groups_by_attribute
  expected_outcome: SUCCESS
  bindings:
    source:
    - work: w1
      edition: 1
    - work: w2
      edition: 1
    - work: w1
      edition: 2
    attribute: work
  expected:
    grouped:
    - key: w1
      records:
      - work: w1
        edition: 1
      - work: w1
        edition: 2
    - key: w2
      records:
      - work: w2
        edition: 1
```

## Intent

Records are grouped by the attribute's value, one group per distinct value, in first-seen order.
