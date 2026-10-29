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
  summary: Claim a wallet's wallet id
  inputs:
    holder:
      type: string
      required: true
  outputs:
    wallet_id:
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
  - step: form_wallet_id
    transform: capability_transforms::CT_PURE_GENERATE_ID_V0
    inputs:
      data: $.inputs.holder
      prefix: wal
    outputs:
      wallet_id: $.capability_result.id
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: claim_id
    side_effect: capability_side_effects::CS_REGISTRY_V0
    op: REGISTER
    store: WALLET_IDENTITIES
    inputs:
      key: $.results.form_wallet_id.wallet_id
      target_cs: capability_side_effects::CS_MUTABLE_JSON_V0
      target_ref: WALLETS
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

Claim a wallet's wallet id
