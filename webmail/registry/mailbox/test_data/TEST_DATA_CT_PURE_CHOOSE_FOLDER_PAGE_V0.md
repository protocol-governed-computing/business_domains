# TEST_DATA_CT_PURE_CHOOSE_FOLDER_PAGE_V0

## Machine

```yaml
fqdn: webmail::TEST_DATA_CT_PURE_CHOOSE_FOLDER_PAGE_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V0
authority: pgc.platform
concern: mailbox
target: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
cases:
- case_id: first_page_is_newest_received_first
  expected_outcome: SUCCESS
  bindings:
    message_ids:
    - 3
    - 7
    - 9
    - 12
    page: 1
    page_size: 2
  expected:
    page_ids:
    - 12
    - 9
    more_exist: true
    folder_empty: false
    message_count: 4
- case_id: last_page_says_no_more_exist
  expected_outcome: SUCCESS
  bindings:
    message_ids:
    - 3
    - 7
    - 9
    - 12
    page: 2
    page_size: 2
  expected:
    page_ids:
    - 7
    - 3
    more_exist: false
    folder_empty: false
    message_count: 4
- case_id: received_order_decides_not_the_identifier
  expected_outcome: SUCCESS
  bindings:
    message_ids:
    - 40
    - 5
    - 22
    page: 1
    page_size: 50
  expected:
    page_ids:
    - 22
    - 5
    - 40
    more_exist: false
    folder_empty: false
    message_count: 3
- case_id: empty_folder_answers_empty
  expected_outcome: SUCCESS
  bindings:
    message_ids: []
    page: 1
    page_size: 50
  expected:
    page_ids: []
    more_exist: false
    folder_empty: true
    message_count: 0
- case_id: a_page_before_the_first_is_refused
  expected_outcome: VIOLATION
  bindings:
    message_ids:
    - 1
    - 2
    page: 0
    page_size: 50
- case_id: an_identifier_that_is_not_a_number_is_refused
  expected_outcome: VIOLATION
  bindings:
    message_ids:
    - 1
    - two
    page: 1
    page_size: 50
```

---

## Intent


