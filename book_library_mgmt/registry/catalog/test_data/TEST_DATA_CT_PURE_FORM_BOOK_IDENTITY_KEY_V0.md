# TEST_DATA_CT_PURE_FORM_BOOK_IDENTITY_KEY_V0

## Machine

```yaml
fqdn: book_library_mgmt::TEST_DATA_CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V0
authority: pgc.platform
concern: catalog
target: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
cases:
- case_id: forms_normalized_key
  expected_outcome: SUCCESS
  bindings:
    title: THE ODYSSEY
    author: Homer
    publication_year: 1614
  expected:
    identity_key: the odyssey|homer|1614
- case_id: refuses_blank_title
  expected_outcome: VIOLATION
  bindings:
    title: ' '
    author: Homer
    publication_year: 1614
```

## Intent

Case does not change which book is meant, and a blank title is refused.
