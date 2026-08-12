# CC_CREATE_WALLET_RECORD_V0

## Header (Mandatory)

- **Artifact Code:** CC_CREATE_WALLET_RECORD_V0
- **Artifact Kind:** capability_contract
- **Governed By:** CONSTITUTION_CAPABILITY_CONTRACT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Records the wallet with a balance of zero, its denomination and its classification

---

## Machine

```yaml
fqdn: blockchain::CC_CREATE_WALLET_RECORD_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: fb.capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
core:
  summary: Records the wallet with a balance of zero, its denomination and its classification
  inputs:
    wallet_id:
      type: string
      required: true
    wallet_fields:
      type: object
      required: true
  outputs:
    result_status:
      type: string
      required: true
  result_status_contract:
    allowed:
    - VIOLATION
    - SUCCESS
    on_input_failure: VIOLATION
  pipeline:
  - step: read_created_at
    side_effect: capability_side_effects::CS_CLOCK_V0
    op: NOW
    inputs: {}
    outputs:
      timestamp: $.capability_result.timestamp
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: assemble_wallet
    transform: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    inputs:
      fields: $.inputs.wallet_fields
    outputs:
      record: $.capability_result.record
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: write_wallet
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: WRITE
    store: WALLETS
    inputs:
      key: $.inputs.wallet_id
      value: $.results.assemble_wallet.record
    outputs:
      result_status: $.capability_result.result_status
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
```
