# TEST_DATA_CT_PURE_CHOOSE_MESSAGE_TEXT_V0

## Machine

```yaml
fqdn: webmail::TEST_DATA_CT_PURE_CHOOSE_MESSAGE_TEXT_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V0
authority: pgc.platform
concern: mailbox
target: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
cases:
- case_id: plain_text_part_is_chosen
  expected_outcome: SUCCESS
  bindings:
    parts:
    - part: '1'
      kind: text/plain
    - part: '2'
      kind: text/html
  expected:
    text_part: '1'
    text_displayable: true
    shown_headers:
    - from
    - to
    - cc
    - subject
    - date
- case_id: first_plain_text_part_wins
  expected_outcome: SUCCESS
  bindings:
    parts:
    - part: '1.1'
      kind: text/plain
    - part: '2'
      kind: text/plain
  expected:
    text_part: '1.1'
    text_displayable: true
    shown_headers:
    - from
    - to
    - cc
    - subject
    - date
- case_id: kind_is_read_without_regard_to_case
  expected_outcome: SUCCESS
  bindings:
    parts:
    - part: '1'
      kind: TEXT/PLAIN
  expected:
    text_part: '1'
    text_displayable: true
    shown_headers:
    - from
    - to
    - cc
    - subject
    - date
- case_id: html_only_cannot_be_displayed_yet
  expected_outcome: SUCCESS
  bindings:
    parts:
    - part: '1'
      kind: text/html
  expected:
    text_part: ''
    text_displayable: false
    shown_headers:
    - from
    - to
    - cc
    - subject
    - date
- case_id: a_part_without_a_kind_is_refused
  expected_outcome: VIOLATION
  bindings:
    parts:
    - part: '1'
```

---

## Intent


