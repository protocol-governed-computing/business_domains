# CC_CLAIM_LICENSE_IDENTITY_V0

## Machine

```yaml
fqdn: ai_governance::CC_CLAIM_LICENSE_IDENTITY_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: ai_licensing
core:
  summary: Claim a license's license id
  inputs:
    employee_id:
      type: string
      required: true
  outputs:
    license_id:
      type: string
      required: true
  result_status_contract:
    allowed:
    - VIOLATION
    - SUCCESS
    - ALREADY_EXISTS
    - BACKEND_ERROR
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
  - step: claim_id
    side_effect: capability_side_effects::CS_REGISTRY_V0
    op: REGISTER
    store: LICENSE_IDENTITY_REGISTRY
    inputs:
      key: $.results.form_license_id.license_id
      target_cs: capability_side_effects::CS_MUTABLE_JSON_V0
      target_ref: LICENSES
    outputs:
      address: $.capability_result.address
      result_status: $.result_status
    result_surface:
    - SUCCESS
    - ALREADY_EXISTS
    - VIOLATION
    - BACKEND_ERROR
    on_result:
      SUCCESS: exit
      ALREADY_EXISTS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
```

---

## Intent

Claim a license's license id
