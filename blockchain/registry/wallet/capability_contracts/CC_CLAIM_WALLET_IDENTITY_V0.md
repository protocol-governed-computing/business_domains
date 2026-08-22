# CC_CLAIM_WALLET_IDENTITY_V0

## 1. Intent

Claims the identity, and refuses when the person already holds a wallet

---

## Machine

```yaml
fqdn: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: wallet
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
    on_result:
      SUCCESS: continue
      ALREADY_EXISTS: exit
      VIOLATION: exit
```
