# TEST_DATA_CT_PURE_FORM_WORK_IDENTITY_KEY_V0

## Machine

```yaml
fqdn: book_library_mgmt::TEST_DATA_CT_PURE_FORM_WORK_IDENTITY_KEY_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V2
authority: pgc.platform
concern: catalog
target: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
cases:
- case_id: forms_normalized_key
  expected_outcome: SUCCESS
  bindings:
    title: The Odyssey
    author: Homer
  expected:
    work_key: the odyssey|homer
```

## Intent

A work is keyed by title and author, normalized exactly as an edition is.
