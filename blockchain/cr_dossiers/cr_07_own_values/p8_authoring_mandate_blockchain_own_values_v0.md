# Stage 8 — Authoring Mandate: blockchain / identity and wallet

## Machine

```yaml
document:
  phase: p8
  domain: blockchain
  subdomain:
  - identity
  - wallet
  cr: cr_07_own_values
  rule_set: transformation.schemas.REGISTER_SCHEMA_P8_V0
registers:
  build_order:
  - wave: '1'
    step: '1'
    code: blockchain::IN_WALLET_CREATION_V1
    action: NEW
    subdomain: wallet
    depends_on: null
  - wave: '1'
    step: '2'
    code: blockchain::WF_REGISTER_ACTOR_V2
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '3'
    code: blockchain::WF_ACCEPT_ACTOR_V2
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '4'
    code: blockchain::WF_REJECT_ACTOR_V2
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '2'
    step: '5'
    code: blockchain::WF_CREATE_WALLET_V2
    action: NEW
    subdomain: wallet
    depends_on:
    - blockchain::IN_WALLET_CREATION_V1
  - wave: '2'
    step: '6'
    code: blockchain::TI_REGISTER_ACTOR_V1
    action: NEW
    subdomain: identity
    depends_on:
    - blockchain::WF_REGISTER_ACTOR_V2
  - wave: '2'
    step: '7'
    code: blockchain::TI_ACCEPT_ACTOR_V1
    action: NEW
    subdomain: identity
    depends_on:
    - blockchain::WF_ACCEPT_ACTOR_V2
  - wave: '2'
    step: '8'
    code: blockchain::TI_REJECT_ACTOR_V1
    action: NEW
    subdomain: identity
    depends_on:
    - blockchain::WF_REJECT_ACTOR_V2
  critical_path:
  - position: '1'
    code: blockchain::IN_WALLET_CREATION_V1
  - position: '2'
    code: blockchain::WF_CREATE_WALLET_V2
  mandate_artifact_summary:
  - action: NEW
    count: '8'
    description: The next versions of four acts that state their own values, of three entrances that send only what the caller supplies, and of the wallet entry point without the prefix.
  - action: REPLACE
    count: '8'
    description: The versions they stand in for, retired by record.
  field_declarations:
  - code: blockchain::IN_WALLET_CREATION_V1
    subdomain_field: wallet
  - code: blockchain::WF_REGISTER_ACTOR_V2
    subdomain_field: identity
  - code: blockchain::WF_ACCEPT_ACTOR_V2
    subdomain_field: identity
  - code: blockchain::WF_REJECT_ACTOR_V2
    subdomain_field: identity
  - code: blockchain::WF_CREATE_WALLET_V2
    subdomain_field: wallet
  - code: blockchain::TI_REGISTER_ACTOR_V1
    subdomain_field: identity
  - code: blockchain::TI_ACCEPT_ACTOR_V1
    subdomain_field: identity
  - code: blockchain::TI_REJECT_ACTOR_V1
    subdomain_field: identity
  new_capabilities: null
  new_intents:
  - code: blockchain::IN_WALLET_CREATION_V1
    purpose: Admits a request naming the person a wallet is for and the key it is made from, and refuses one that names nobody
    workflow: blockchain::WF_CREATE_WALLET_V2
    inputs: contact_address:string, key_material:string
  cross_subdomain_notes:
  - code: blockchain::WF_CREATE_WALLET_V2
    note: Reads the wallet's holder from identity's lookup, blockchain::CC_RESOLVE_ACTOR_V1, which wallet already runs; identity amends nothing.
```

IN WHAT ORDER. Mechanically derived from the design; it reconciles with Stage 7 exactly and adds
nothing. The wallet entry point comes first, because the wallet act starts at it. The three identity
acts depend on nothing this change authors, and each entrance waits for the act it starts. Each
predecessor is retired by record as its successor is built, and the identity entry points are
re-pointed with them.

---

## 1. Build Order

---

## 2. Critical Path

---

## 3. Artifact Summary

---

## 4. Field Declarations

---

## 5. New Capabilities

---

## 6. New Intents

---

## 7. Cross-Subdomain Notes
