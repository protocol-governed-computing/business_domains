# TEST_DATA_CT_PURE_DECIDE_READ_STATE_V0

## Machine

```yaml
fqdn: webmail::TEST_DATA_CT_PURE_DECIDE_READ_STATE_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V0
authority: pgc.platform
concern: mailbox
target: webmail::CT_PURE_DECIDE_READ_STATE_V0
cases:
- case_id: unread_asked_read_becomes_read
  expected_outcome: SUCCESS
  bindings:
    seen: false
    wanted_read: true
  expected:
    change: SET_READ
    read_now: true
- case_id: read_asked_unread_becomes_unread
  expected_outcome: SUCCESS
  bindings:
    seen: true
    wanted_read: false
  expected:
    change: SET_UNREAD
    read_now: false
- case_id: read_asked_read_changes_nothing
  expected_outcome: SUCCESS
  bindings:
    seen: true
    wanted_read: true
  expected:
    change: NONE
    read_now: true
- case_id: unread_asked_unread_changes_nothing
  expected_outcome: SUCCESS
  bindings:
    seen: false
    wanted_read: false
  expected:
    change: NONE
    read_now: false
- case_id: a_state_that_is_not_true_or_false_is_refused
  expected_outcome: VIOLATION
  bindings:
    seen: 'yes'
    wanted_read: true
```

---

## Intent


