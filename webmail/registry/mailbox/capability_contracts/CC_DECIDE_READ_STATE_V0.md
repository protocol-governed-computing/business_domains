# CC_DECIDE_READ_STATE_V0

## Machine

```yaml
fqdn: webmail::CC_DECIDE_READ_STATE_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: mailbox
core:
  summary: Decides whether a message becomes read, becomes unread or stays as it is
  inputs:
    seen:
      type: boolean
      required: true
    wanted_read:
      type: boolean
      required: true
  outputs:
    change:
      type: string
      required: true
    read_now:
      type: boolean
      required: true
  result_status_contract:
    allowed:
    - SUCCESS
    - VIOLATION
    on_input_failure: VIOLATION
  pipeline:
  - step: decide_read_state
    transform: webmail::CT_PURE_DECIDE_READ_STATE_V0
    inputs:
      seen: $.inputs.seen
      wanted_read: $.inputs.wanted_read
    outputs:
      change: $.capability_result.change
      read_now: $.capability_result.read_now
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: exit
      VIOLATION: exit
```

---

## Intent

Decides whether a message becomes read, becomes unread or stays as it is
