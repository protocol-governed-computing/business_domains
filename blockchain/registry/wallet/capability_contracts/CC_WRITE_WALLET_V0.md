# CC_WRITE_WALLET_V0

## Machine

```yaml
fqdn: blockchain::CC_WRITE_WALLET_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: wallet
core:
  summary: Write a new wallet in its first state
  inputs:
    wallet_id:
      type: string
      required: true
    holder:
      type: string
      required: true
  outputs:
    result_status:
      type: string
      required: true
  result_status_contract:
    allowed:
    - VIOLATION
    - SUCCESS
    - BACKEND_ERROR
    on_input_failure: VIOLATION
  pipeline:
  - step: assemble_wallet_record
    transform: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    inputs:
      fields:
        holder: $.inputs.holder
        balance: 0
        denomination: BACHI
        classification: DEFAULT
        state: ACTIVE
    outputs:
      wallet_record: $.capability_result.record
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: write_wallet_record
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: WRITE
    store: WALLETS
    inputs:
      key: $.inputs.wallet_id
      value: $.results.assemble_wallet_record.wallet_record
    outputs:
      result_status: $.result_status
    result_surface:
    - SUCCESS
    - VIOLATION
    - BACKEND_ERROR
    on_result:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
```

---

## Intent

Write a new wallet in its first state
