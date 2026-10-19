# TEST_DATA_CT_PURE_SELECT_RECORDS_V0

## Machine

```yaml
fqdn: book_library_mgmt::TEST_DATA_CT_PURE_SELECT_RECORDS_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V0
authority: pgc.platform
concern: catalog
target: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
cases:
- case_id: selects_matching_records
  expected_outcome: SUCCESS
  bindings:
    source:
    - author: Homer
      title: Iliad
    - author: Virgil
      title: Aeneid
    filter:
      author: Homer
  expected:
    extracted:
    - author: Homer
      title: Iliad
```

## Intent

The records matching every criterion are selected.
