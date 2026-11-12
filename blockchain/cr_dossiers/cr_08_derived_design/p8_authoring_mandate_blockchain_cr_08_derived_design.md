# Authoring Mandate — blockchain, baseline

## Machine

```yaml
document:
  phase: p8
  domain: blockchain
  subdomain:
  - identity
  - wallet
  cr: baseline
  rule_set: transformation.schemas.REGISTER_SCHEMA_P8_V0
registers:
  build_order:
  - wave: '1'
    step: '1'
    code: blockchain::VOCAB_WALLET_CLASSIFICATION_V1
    action: NEW
    subdomain: wallet
    depends_on: null
  - wave: '1'
    step: '2'
    code: blockchain::EV_ACTOR_ACCEPTED_V1
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '3'
    code: blockchain::WF_CREATE_WALLET_V1
    action: NEW
    subdomain: wallet
    depends_on:
    - blockchain::RB_WALLET_BINDINGS_V1
    - blockchain::AC_PARTICIPANT_V0
    - blockchain::EV_WALLET_CREATED_V0
    - blockchain::IN_WALLET_CREATION_V0
    - blockchain::CC_RESOLVE_ACTOR_IDENTITY_V0
    - blockchain::CC_REQUIRE_ACCEPTED_ACTOR_V0
    - blockchain::CC_DERIVE_WALLET_ADDRESS_V0
    - blockchain::CC_REQUIRE_WALLET_ADDRESS_FREE_V0
    - blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    - blockchain::CC_CLAIM_WALLET_ADDRESS_V0
    - blockchain::CC_WRITE_WALLET_V0
    - blockchain::CC_RECORD_WALLET_MOMENT_V0
  - wave: '1'
    step: '4'
    code: blockchain::WF_REJECT_ACTOR_V1
    action: NEW
    subdomain: identity
    depends_on:
    - blockchain::RB_IDENTITY_BINDINGS_V0
    - blockchain::AC_PARTICIPANT_V0
    - blockchain::EV_ACTOR_REJECTED_V0
    - blockchain::IN_ACTOR_REJECTION_V0
    - blockchain::CC_REQUIRE_GROUNDS_TO_REJECT_ACTOR_V0
    - blockchain::CC_RESOLVE_ACTOR_IDENTITY_V0
    - blockchain::CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    - blockchain::CC_RECORD_IDENTITY_MOMENT_V0
  - wave: '1'
    step: '5'
    code: blockchain::WF_ACCEPT_ACTOR_V1
    action: NEW
    subdomain: identity
    depends_on:
    - blockchain::RB_IDENTITY_BINDINGS_V0
    - blockchain::AC_PARTICIPANT_V0
    - blockchain::EV_ACTOR_ACCEPTED_V1
    - blockchain::IN_ACTOR_ACCEPTANCE_V0
    - blockchain::CC_RESOLVE_ACTOR_IDENTITY_V0
    - blockchain::CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    - blockchain::CC_RECORD_IDENTITY_MOMENT_V0
  - wave: '1'
    step: '6'
    code: blockchain::WF_REGISTER_ACTOR_V1
    action: NEW
    subdomain: identity
    depends_on:
    - blockchain::RB_IDENTITY_BINDINGS_V0
    - blockchain::AC_PARTICIPANT_V0
    - blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
    - blockchain::IN_ACTOR_REGISTERED_V0
    - blockchain::CC_CHECK_REGISTER_ACTOR_SUBMISSION_V0
    - blockchain::CC_CLAIM_ACTOR_CONTACT_ADDRESS_V0
    - blockchain::CC_WRITE_ACTOR_V0
    - blockchain::CC_RECORD_IDENTITY_MOMENT_V0
  - wave: '1'
    step: '7'
    code: blockchain::CC_RECORD_WALLET_MOMENT_V0
    action: NEW
    subdomain: wallet
    depends_on: null
  - wave: '1'
    step: '8'
    code: blockchain::CC_WRITE_WALLET_V0
    action: NEW
    subdomain: wallet
    depends_on: null
  - wave: '1'
    step: '9'
    code: blockchain::CC_CLAIM_WALLET_ADDRESS_V0
    action: NEW
    subdomain: wallet
    depends_on: null
  - wave: '1'
    step: '10'
    code: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    action: NEW
    subdomain: wallet
    depends_on: null
  - wave: '1'
    step: '11'
    code: blockchain::CC_REQUIRE_WALLET_ADDRESS_FREE_V0
    action: NEW
    subdomain: wallet
    depends_on: null
  - wave: '1'
    step: '12'
    code: blockchain::CC_DERIVE_WALLET_ADDRESS_V0
    action: NEW
    subdomain: wallet
    depends_on: null
  - wave: '1'
    step: '13'
    code: blockchain::CC_REQUIRE_ACCEPTED_ACTOR_V0
    action: NEW
    subdomain: wallet
    depends_on: null
  - wave: '1'
    step: '14'
    code: blockchain::CC_REQUIRE_GROUNDS_TO_REJECT_ACTOR_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '15'
    code: blockchain::CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '16'
    code: blockchain::CC_RESOLVE_ACTOR_IDENTITY_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '17'
    code: blockchain::CC_RECORD_IDENTITY_MOMENT_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '18'
    code: blockchain::CC_WRITE_ACTOR_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '19'
    code: blockchain::CC_CLAIM_ACTOR_CONTACT_ADDRESS_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '20'
    code: blockchain::CC_CHECK_REGISTER_ACTOR_SUBMISSION_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '21'
    code: blockchain::RB_WALLET_BINDINGS_V1
    action: NEW
    subdomain: wallet
    depends_on: null
  - wave: '1'
    step: '22'
    code: blockchain::STRUCTURE_WALLET_STORAGE_V1
    action: NEW
    subdomain: wallet
    depends_on: null
  critical_path:
  - position: '1'
    code: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
  - position: '2'
    code: blockchain::RB_IDENTITY_BINDINGS_V0
  - position: '3'
    code: blockchain::TI_ACCEPT_ACTOR_V0
  mandate_artifact_summary:
  - action: NEW
    count: '22'
    description: 1 STRUCTURE, 1 RB, 14 CC, 4 WF, 1 EV, 1 VOCAB
  field_declarations:
  - code: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    subdomain_field: identity
  - code: blockchain::AC_PARTICIPANT_V0
    subdomain_field: identity
  - code: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
    subdomain_field: identity
  - code: blockchain::EV_ACTOR_REJECTED_V0
    subdomain_field: identity
  - code: blockchain::EV_WALLET_CREATED_V0
    subdomain_field: wallet
  - code: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
    subdomain_field: wallet
  - code: blockchain::IN_ACTOR_ACCEPTANCE_V0
    subdomain_field: identity
  - code: blockchain::IN_ACTOR_REGISTERED_V0
    subdomain_field: identity
  - code: blockchain::IN_ACTOR_REJECTION_V0
    subdomain_field: identity
  - code: blockchain::IN_WALLET_CREATION_V0
    subdomain_field: wallet
  - code: blockchain::TE_ACCEPT_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::TE_REGISTER_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::TE_REJECT_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::RB_IDENTITY_BINDINGS_V0
    subdomain_field: identity
  - code: blockchain::TI_ACCEPT_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::TI_REGISTER_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::TI_REJECT_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::STRUCTURE_WALLET_STORAGE_V1
    subdomain_field: wallet
  - code: blockchain::RB_WALLET_BINDINGS_V1
    subdomain_field: wallet
  - code: blockchain::CC_CHECK_REGISTER_ACTOR_SUBMISSION_V0
    subdomain_field: identity
  - code: blockchain::CC_CLAIM_ACTOR_CONTACT_ADDRESS_V0
    subdomain_field: identity
  - code: blockchain::CC_WRITE_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::CC_RECORD_IDENTITY_MOMENT_V0
    subdomain_field: identity
  - code: blockchain::CC_RESOLVE_ACTOR_IDENTITY_V0
    subdomain_field: identity
  - code: blockchain::CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    subdomain_field: identity
  - code: blockchain::CC_REQUIRE_GROUNDS_TO_REJECT_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::CC_REQUIRE_ACCEPTED_ACTOR_V0
    subdomain_field: wallet
  - code: blockchain::CC_DERIVE_WALLET_ADDRESS_V0
    subdomain_field: wallet
  - code: blockchain::CC_REQUIRE_WALLET_ADDRESS_FREE_V0
    subdomain_field: wallet
  - code: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    subdomain_field: wallet
  - code: blockchain::CC_CLAIM_WALLET_ADDRESS_V0
    subdomain_field: wallet
  - code: blockchain::CC_WRITE_WALLET_V0
    subdomain_field: wallet
  - code: blockchain::CC_RECORD_WALLET_MOMENT_V0
    subdomain_field: wallet
  - code: blockchain::WF_REGISTER_ACTOR_V1
    subdomain_field: identity
  - code: blockchain::WF_ACCEPT_ACTOR_V1
    subdomain_field: identity
  - code: blockchain::WF_REJECT_ACTOR_V1
    subdomain_field: identity
  - code: blockchain::WF_CREATE_WALLET_V1
    subdomain_field: wallet
  - code: blockchain::EV_ACTOR_ACCEPTED_V1
    subdomain_field: identity
  - code: blockchain::VOCAB_WALLET_CLASSIFICATION_V1
    subdomain_field: wallet
  new_capabilities:
  - code: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
    purpose: Derives an address from supplied key material; the same material always yields the same address
    inputs: key_material:string
    outputs: address:string
  new_intents:
  - code: blockchain::IN_ACTOR_ACCEPTANCE_V0
    purpose: Admits a request to accept a person, with the grounds the authority chooses to state, and
      refuses one that names nobody
    workflow: WF_ACCEPT_ACTOR_V1
    inputs: contact_address:string, verifying_authority:string, grounds:string
  - code: blockchain::IN_ACTOR_REGISTERED_V0
    purpose: A request to admit a person as an actor
    workflow: WF_REGISTER_ACTOR_V1
    inputs: actor_record:object
  - code: blockchain::IN_ACTOR_REJECTION_V0
    purpose: Admits a request to reject a person, and refuses one that states no grounds
    workflow: WF_REJECT_ACTOR_V1
    inputs: contact_address:string, verifying_authority:string, grounds:string
  - code: blockchain::IN_WALLET_CREATION_V0
    purpose: Admits a request naming the person a wallet is for and the key it is made from, and refuses
      one that names nobody
    workflow: WF_CREATE_WALLET_V1
    inputs: contact_address:string, key_material:string
  cross_subdomain_notes: []
```

The 38 artifacts of `blockchain`'s design of record, scheduled in dependency order. Written by
`python -m transformation.record` from the P7 beside it. The mandate orders the build; it decides
nothing.
