# CC_REQUIRE_CAP_SET_V0

## Machine

```yaml
fqdn: ai_governance::CC_REQUIRE_CAP_SET_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: ai_licensing
core:
  summary: Refuse to provision license before the license cap is set
  inputs:
    cap_key:
      type: string
      required: true
  outputs:
    cap_record:
      type: object
      required: true
  result_status_contract:
    allowed:
    - SUCCESS
    - NOT_FOUND
    - VIOLATION
    - BACKEND_ERROR
    on_input_failure: VIOLATION
  pipeline:
  - step: read_cap_record
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: READ
    store: LICENSE_CAPS
    inputs:
      key: $.inputs.cap_key
    outputs:
      cap_record: $.capability_result.value
      result_status: $.result_status
    result_surface:
    - SUCCESS
    - NOT_FOUND
    - VIOLATION
    - BACKEND_ERROR
    on_result:
      SUCCESS: exit
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
```

---

## Intent

Refuse to provision license before the license cap is set
