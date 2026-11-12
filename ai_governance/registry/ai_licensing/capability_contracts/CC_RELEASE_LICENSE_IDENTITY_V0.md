# CC_RELEASE_LICENSE_IDENTITY_V0

## Machine

```yaml
fqdn: ai_governance::CC_RELEASE_LICENSE_IDENTITY_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: ai_licensing
core:
  summary: Release a license's identity
  inputs:
    license_id:
      type: string
      required: true
  outputs:
    result_status:
      type: string
      required: true
  result_status_contract:
    allowed:
    - SUCCESS
    - NOT_FOUND
    - VIOLATION
    - BACKEND_ERROR
    on_input_failure: VIOLATION
  pipeline:
  - step: release_identity
    side_effect: capability_side_effects::CS_REGISTRY_V0
    op: DEREGISTER
    store: LICENSE_IDENTITY_REGISTRY
    inputs:
      key_or_address: $.inputs.license_id
    outputs:
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

Release a license's identity
