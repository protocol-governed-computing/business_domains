# CC_RECORD_IDENTITY_REPEATED_MOMENT_V0

## Machine

```yaml
fqdn: blockchain::CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: identity
core:
  summary: Record a moment on the identity's own trail
  inputs:
    occurrence:
      type: string
      required: true
    contact_address:
      type: string
    verifying_authority:
      type: string
    grounds:
      type: string
    name:
      type: string
    currency_preference:
      type: string
    language:
      type: string
  outputs:
    sequence_number:
      type: integer
      required: true
  result_status_contract:
    allowed:
    - BACKEND_ERROR
    - VIOLATION
    - SUCCESS
    on_input_failure: VIOLATION
  pipeline:
  - step: read_now
    side_effect: capability_side_effects::CS_CLOCK_V0
    op: NOW
    inputs: {}
    outputs:
      timestamp: $.capability_result.timestamp
    result_surface:
    - SUCCESS
    - BACKEND_ERROR
    on_result:
      SUCCESS: continue
      BACKEND_ERROR: exit
  - step: assemble_occurrence
    transform: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    inputs:
      fields:
        occurrence: $.inputs.occurrence
        contact_address: $.inputs.contact_address
        verifying_authority: $.inputs.verifying_authority
        grounds: $.inputs.grounds
        name: $.inputs.name
        currency_preference: $.inputs.currency_preference
        language: $.inputs.language
        occurred_at: $.results.read_now.timestamp
    outputs:
      record: $.capability_result.record
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: append_occurrence
    side_effect: capability_side_effects::CS_APPENDONLY_JSONL_V0
    op: APPEND
    store: ACTOR_OCCURRENCES
    inputs:
      record: $.results.assemble_occurrence.record
      stream_id: ACTOR_OCCURRENCES
    outputs:
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

Record a moment on the identity's own trail
