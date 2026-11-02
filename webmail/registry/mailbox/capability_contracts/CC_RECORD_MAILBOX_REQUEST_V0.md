# CC_RECORD_MAILBOX_REQUEST_V0

## Machine

```yaml
fqdn: webmail::CC_RECORD_MAILBOX_REQUEST_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: mailbox
core:
  summary: Adds an entry to the mailbox record
  inputs:
    entry:
      type: object
      required: true
    host_id:
      type: string
      required: true
  outputs:
    entry:
      type: object
      required: true
    record_id:
      type: string
      required: true
    sequence_number:
      type: integer
      required: true
  result_status_contract:
    allowed:
    - SUCCESS
    - VIOLATION
    - BACKEND_ERROR
    on_input_failure: VIOLATION
  pipeline:
  - step: assemble_entry
    transform: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    inputs:
      fields: $.inputs.entry
    outputs:
      entry: $.capability_result.record
    result_surface:
    - SUCCESS
    on_result:
      SUCCESS: continue
  - step: append_entry
    side_effect: capability_side_effects::CS_APPENDONLY_JSONL_V0
    op: APPEND
    store: MAILBOX_RECORDS
    inputs:
      record: $.results.assemble_entry.entry
      stream_id: MAILBOX_RECORDS
      actor_id: $.inputs.host_id
    outputs:
      record_id: $.capability_result.record_id
      sequence_number: $.capability_result.sequence_number
    result_surface:
    - SUCCESS
    - VIOLATION
    - BACKEND_ERROR
    on_result:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
```

---

## Intent

Adds an entry to the mailbox record
