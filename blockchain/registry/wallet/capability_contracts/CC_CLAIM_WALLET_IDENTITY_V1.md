# CC_CLAIM_WALLET_IDENTITY_V1

## Machine

```yaml
fqdn: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
artifact_kind: CAPABILITY_CONTRACT
version: v1
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: wallet
supersedes: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
core:
  summary: Claims the identity, and refuses when the person already holds a wallet
  inputs:
    wallet_id:
      type: string
      required: true
  outputs:
    result_status:
      type: string
      required: true
  result_status_contract:
    allowed:
    - SUCCESS
    - ALREADY_EXISTS
    - VIOLATION
    - BACKEND_ERROR
    on_input_failure: VIOLATION
  pipeline:
  - step: claim_wallet_identity
    side_effect: capability_side_effects::CS_REGISTRY_V0
    op: REGISTER
    store: WALLET_IDENTITIES
    inputs:
      key: $.inputs.wallet_id
    outputs:
      result_status: $.capability_result.result_status
    result_surface:
    - SUCCESS
    - ALREADY_EXISTS
    - VIOLATION
    - BACKEND_ERROR
    on_result:
      SUCCESS: continue
      ALREADY_EXISTS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
```

---

## Intent

Claims the identity, and refuses when the person already holds a wallet
