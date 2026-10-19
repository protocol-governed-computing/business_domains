# CC_ESTABLISH_WALLET_ADDRESS_V0

## 1. Intent

Establishes the address from key material supplied with the request

---

## Machine

```yaml
fqdn: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: wallet
core:
  summary: Establishes the address from key material supplied with the request
  inputs:
    key_material:
      type: string
      required: true
  outputs:
    address:
      type: string
      required: true
  result_status_contract:
    allowed:
    - SUCCESS
    - VIOLATION
    on_input_failure: VIOLATION
  pipeline:
  - step: derive_wallet_address
    transform: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
    inputs:
      key_material: $.inputs.key_material
    outputs:
      address: $.capability_result.address
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
```
