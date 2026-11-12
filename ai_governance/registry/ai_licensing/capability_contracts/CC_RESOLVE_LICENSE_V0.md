# CC_RESOLVE_LICENSE_V0

## Machine

```yaml
fqdn: ai_governance::CC_RESOLVE_LICENSE_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: ai_licensing
core:
  summary: Answer which license its identity names, and refuse when none does
  inputs:
    employee_id:
      type: string
      required: true
  outputs:
    license_record:
      type: object
      required: true
  result_status_contract:
    allowed:
    - VIOLATION
    - NOT_FOUND
    - BACKEND_ERROR
    - SUCCESS
    on_input_failure: VIOLATION
  pipeline:
  - step: form_license_id
    transform: capability_transforms::CT_PURE_GENERATE_ID_V0
    inputs:
      data: $.inputs.employee_id
      prefix: lic
    outputs:
      license_id: $.capability_result.id
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: resolve_identity
    side_effect: capability_side_effects::CS_REGISTRY_V0
    op: RESOLVE
    store: LICENSE_IDENTITY_REGISTRY
    inputs:
      key_or_address: $.results.form_license_id.license_id
    outputs:
      target_ref: $.capability_result.target_ref
      result_status: $.result_status
    result_surface:
    - SUCCESS
    - NOT_FOUND
    - VIOLATION
    - BACKEND_ERROR
    on_result:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
  - step: read_license_record
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: READ
    store: LICENSES
    inputs:
      key: $.results.form_license_id.license_id
    outputs:
      license_record: $.capability_result.value
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

Answer which license its identity names, and refuse when none does
