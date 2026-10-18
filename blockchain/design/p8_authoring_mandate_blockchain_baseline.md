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
    code: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '2'
    code: blockchain::STRUCTURE_WALLET_STORAGE_V0
    action: NEW
    subdomain: wallet
    depends_on: null
  - wave: '1'
    step: '3'
    code: blockchain::VOCAB_WALLET_CLASSIFICATION_V0
    action: NEW
    subdomain: wallet
    depends_on: null
  - wave: '1'
    step: '4'
    code: blockchain::AC_PARTICIPANT_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '5'
    code: blockchain::EV_ACTOR_ACCEPTED_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '6'
    code: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '7'
    code: blockchain::EV_ACTOR_REJECTED_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '8'
    code: blockchain::EV_WALLET_CREATED_V0
    action: NEW
    subdomain: wallet
    depends_on: null
  - wave: '1'
    step: '9'
    code: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
    action: NEW
    subdomain: wallet
    depends_on: null
  - wave: '1'
    step: '10'
    code: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '11'
    code: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '12'
    code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '13'
    code: blockchain::CC_REGISTER_ACTOR_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '14'
    code: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '15'
    code: blockchain::CC_RESOLVE_ACTOR_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '16'
    code: blockchain::CC_RESOLVE_ACTOR_V1
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '17'
    code: blockchain::CC_VALIDATE_REGISTRATION_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '18'
    code: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    action: NEW
    subdomain: wallet
    depends_on: null
  - wave: '1'
    step: '19'
    code: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
    action: NEW
    subdomain: wallet
    depends_on: null
  - wave: '1'
    step: '20'
    code: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    action: NEW
    subdomain: wallet
    depends_on: null
  - wave: '1'
    step: '21'
    code: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    action: NEW
    subdomain: wallet
    depends_on: null
  - wave: '1'
    step: '22'
    code: blockchain::CC_CREATE_WALLET_RECORD_V0
    action: NEW
    subdomain: wallet
    depends_on: null
  - wave: '1'
    step: '23'
    code: blockchain::CC_CREATE_WALLET_RECORD_V1
    action: NEW
    subdomain: wallet
    depends_on: null
  - wave: '1'
    step: '24'
    code: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    action: NEW
    subdomain: wallet
    depends_on: null
  - wave: '1'
    step: '25'
    code: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    action: NEW
    subdomain: wallet
    depends_on: null
  - wave: '1'
    step: '26'
    code: blockchain::IN_ACTOR_ACCEPTANCE_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '27'
    code: blockchain::IN_ACTOR_REGISTERED_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '28'
    code: blockchain::IN_ACTOR_REJECTION_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '29'
    code: blockchain::IN_WALLET_CREATION_V1
    action: NEW
    subdomain: wallet
    depends_on: null
  - wave: '1'
    step: '30'
    code: blockchain::TE_ACCEPT_ACTOR_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '31'
    code: blockchain::TE_REGISTER_ACTOR_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '1'
    step: '32'
    code: blockchain::TE_REJECT_ACTOR_V0
    action: NEW
    subdomain: identity
    depends_on: null
  - wave: '2'
    step: '33'
    code: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
    action: NEW
    subdomain: wallet
    depends_on:
    - blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
  - wave: '2'
    step: '34'
    code: blockchain::RB_IDENTITY_BINDINGS_V0
    action: NEW
    subdomain: identity
    depends_on:
    - blockchain::STRUCTURE_IDENTITY_STORAGE_V0
  - wave: '2'
    step: '35'
    code: blockchain::RB_WALLET_BINDINGS_V0
    action: NEW
    subdomain: wallet
    depends_on:
    - blockchain::STRUCTURE_WALLET_STORAGE_V0
  - wave: '3'
    step: '36'
    code: blockchain::WF_ACCEPT_ACTOR_V2
    action: NEW
    subdomain: identity
    depends_on:
    - blockchain::RB_IDENTITY_BINDINGS_V0
    - blockchain::AC_PARTICIPANT_V0
    - blockchain::EV_ACTOR_ACCEPTED_V0
    - blockchain::IN_ACTOR_ACCEPTANCE_V0
    - blockchain::CC_RESOLVE_ACTOR_V0
    - blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    - blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
  - wave: '3'
    step: '37'
    code: blockchain::WF_REGISTER_ACTOR_V2
    action: NEW
    subdomain: identity
    depends_on:
    - blockchain::RB_IDENTITY_BINDINGS_V0
    - blockchain::AC_PARTICIPANT_V0
    - blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
    - blockchain::IN_ACTOR_REGISTERED_V0
    - blockchain::CC_VALIDATE_REGISTRATION_V0
    - blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    - blockchain::CC_REGISTER_ACTOR_V0
    - blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
  - wave: '3'
    step: '38'
    code: blockchain::WF_REJECT_ACTOR_V2
    action: NEW
    subdomain: identity
    depends_on:
    - blockchain::RB_IDENTITY_BINDINGS_V0
    - blockchain::AC_PARTICIPANT_V0
    - blockchain::EV_ACTOR_REJECTED_V0
    - blockchain::IN_ACTOR_REJECTION_V0
    - blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    - blockchain::CC_RESOLVE_ACTOR_V0
    - blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    - blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
  - wave: '3'
    step: '39'
    code: blockchain::WF_CREATE_WALLET_V2
    action: NEW
    subdomain: wallet
    depends_on:
    - blockchain::RB_WALLET_BINDINGS_V0
    - blockchain::RB_IDENTITY_BINDINGS_V0
    - blockchain::AC_PARTICIPANT_V0
    - blockchain::EV_WALLET_CREATED_V0
    - blockchain::IN_WALLET_CREATION_V1
    - blockchain::CC_RESOLVE_ACTOR_V0
    - blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    - blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    - blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    - blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
    - blockchain::CC_CREATE_WALLET_RECORD_V0
    - blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
  - wave: '4'
    step: '40'
    code: blockchain::TI_ACCEPT_ACTOR_V1
    action: NEW
    subdomain: identity
    depends_on:
    - blockchain::WF_ACCEPT_ACTOR_V2
  - wave: '4'
    step: '41'
    code: blockchain::TI_REGISTER_ACTOR_V1
    action: NEW
    subdomain: identity
    depends_on:
    - blockchain::WF_REGISTER_ACTOR_V2
  - wave: '4'
    step: '42'
    code: blockchain::TI_REJECT_ACTOR_V1
    action: NEW
    subdomain: identity
    depends_on:
    - blockchain::WF_REJECT_ACTOR_V2
  critical_path:
  - position: '1'
    code: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
  - position: '2'
    code: blockchain::RB_IDENTITY_BINDINGS_V0
  - position: '3'
    code: blockchain::WF_ACCEPT_ACTOR_V2
  - position: '4'
    code: blockchain::TI_ACCEPT_ACTOR_V1
  mandate_artifact_summary:
  - action: NEW
    count: '42'
    description: 2 STRUCTURE, 1 VOCAB, 1 AC, 4 EV, 1 CT, 17 CC, 4 IN, 4 WF, 2 RB, 3 TI, 3 TE
  field_declarations:
  - code: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    subdomain_field: identity
  - code: blockchain::STRUCTURE_WALLET_STORAGE_V0
    subdomain_field: wallet
  - code: blockchain::VOCAB_WALLET_CLASSIFICATION_V0
    subdomain_field: wallet
  - code: blockchain::AC_PARTICIPANT_V0
    subdomain_field: identity
  - code: blockchain::EV_ACTOR_ACCEPTED_V0
    subdomain_field: identity
  - code: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
    subdomain_field: identity
  - code: blockchain::EV_ACTOR_REJECTED_V0
    subdomain_field: identity
  - code: blockchain::EV_WALLET_CREATED_V0
    subdomain_field: wallet
  - code: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
    subdomain_field: wallet
  - code: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    subdomain_field: identity
  - code: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    subdomain_field: identity
  - code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    subdomain_field: identity
  - code: blockchain::CC_REGISTER_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    subdomain_field: identity
  - code: blockchain::CC_RESOLVE_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::CC_RESOLVE_ACTOR_V1
    subdomain_field: identity
  - code: blockchain::CC_VALIDATE_REGISTRATION_V0
    subdomain_field: identity
  - code: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    subdomain_field: wallet
  - code: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
    subdomain_field: wallet
  - code: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    subdomain_field: wallet
  - code: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    subdomain_field: wallet
  - code: blockchain::CC_CREATE_WALLET_RECORD_V0
    subdomain_field: wallet
  - code: blockchain::CC_CREATE_WALLET_RECORD_V1
    subdomain_field: wallet
  - code: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    subdomain_field: wallet
  - code: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    subdomain_field: wallet
  - code: blockchain::IN_ACTOR_ACCEPTANCE_V0
    subdomain_field: identity
  - code: blockchain::IN_ACTOR_REGISTERED_V0
    subdomain_field: identity
  - code: blockchain::IN_ACTOR_REJECTION_V0
    subdomain_field: identity
  - code: blockchain::IN_WALLET_CREATION_V1
    subdomain_field: wallet
  - code: blockchain::TE_ACCEPT_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::TE_REGISTER_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::TE_REJECT_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
    subdomain_field: wallet
  - code: blockchain::RB_IDENTITY_BINDINGS_V0
    subdomain_field: identity
  - code: blockchain::RB_WALLET_BINDINGS_V0
    subdomain_field: wallet
  - code: blockchain::WF_ACCEPT_ACTOR_V2
    subdomain_field: identity
  - code: blockchain::WF_REGISTER_ACTOR_V2
    subdomain_field: identity
  - code: blockchain::WF_REJECT_ACTOR_V2
    subdomain_field: identity
  - code: blockchain::WF_CREATE_WALLET_V2
    subdomain_field: wallet
  - code: blockchain::TI_ACCEPT_ACTOR_V1
    subdomain_field: identity
  - code: blockchain::TI_REGISTER_ACTOR_V1
    subdomain_field: identity
  - code: blockchain::TI_REJECT_ACTOR_V1
    subdomain_field: identity
  new_capabilities:
  - code: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
    purpose: Derives an address from supplied key material; the same material always yields the same address
    inputs: key_material:string
    outputs: address:string
  new_intents:
  - code: blockchain::IN_ACTOR_ACCEPTANCE_V0
    purpose: Admits a request to accept a person, with the grounds the authority chooses to state, and
      refuses one that names nobody
    workflow: WF_ACCEPT_ACTOR_V2
    inputs: contact_address:string, verifying_authority:string, grounds:string
  - code: blockchain::IN_ACTOR_REGISTERED_V0
    purpose: A request to admit a person as an actor
    workflow: WF_REGISTER_ACTOR_V2
    inputs: actor_record:object
  - code: blockchain::IN_ACTOR_REJECTION_V0
    purpose: Admits a request to reject a person, and refuses one that states no grounds
    workflow: WF_REJECT_ACTOR_V2
    inputs: contact_address:string, verifying_authority:string, grounds:string
  - code: blockchain::IN_WALLET_CREATION_V1
    purpose: Admits a request naming the person a wallet is for and the key it is made from, and refuses
      one that names nobody
    workflow: WF_CREATE_WALLET_V2
    inputs: contact_address:string, key_material:string
  cross_subdomain_notes: []
```

The 42 artifacts of `blockchain`'s design of record, scheduled in dependency order. Written by
`python -m transformation.record` from the P7 beside it. The mandate orders the build; it decides
nothing.
