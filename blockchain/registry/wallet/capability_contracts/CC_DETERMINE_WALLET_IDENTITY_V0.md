# CC_DETERMINE_WALLET_IDENTITY_V0

## 1. Intent

Derives the wallet's identity from the person who holds it

---

## Machine

```yaml
fqdn: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: wallet
core:
  summary: Derives the wallet's identity from the person who holds it
  inputs:
    holder:
      type: string
      required: true
    wallet_id_prefix:
      type: string
      required: true
  outputs:
    id:
      type: string
      required: true
  result_status_contract:
    allowed:
    - SUCCESS
    - VIOLATION
    on_input_failure: VIOLATION
  pipeline:
  - step: derive_wallet_identity
    transform: capability_transforms::CT_PURE_GENERATE_ID_V0
    inputs:
      data: $.inputs.holder
      prefix: $.inputs.wallet_id_prefix
    outputs:
      id: $.capability_result.id
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
```
