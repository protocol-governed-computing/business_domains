# CC_LIST_ACTORS_V0

## Machine

```yaml
fqdn: blockchain::CC_LIST_ACTORS_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: identity
core:
  summary: Answer the actors matching the criteria named
  inputs:
    state:
      type: string
      required: true
  outputs:
    matching_actors:
      type: array
      required: true
  result_status_contract:
    allowed:
    - BACKEND_ERROR
    - SUCCESS
    - VIOLATION
    on_input_failure: VIOLATION
  pipeline:
  - step: select_actor_records
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: SELECT
    store: ACTORS
    inputs: {}
    outputs:
      records: $.capability_result.records
      result_status: $.result_status
    result_surface:
    - SUCCESS
    - BACKEND_ERROR
    on_result:
      SUCCESS: continue
      BACKEND_ERROR: exit
  - step: select_matching_actors
    transform: capability_transforms::CT_PURE_SELECT_RECORDS_V0
    inputs:
      source: $.results.select_actor_records.records
      filter:
        state: $.inputs.state
    outputs:
      matching_actors: $.capability_result.extracted
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: exit
      VIOLATION: exit
```

---

## Intent

Answer the actors matching the criteria named
