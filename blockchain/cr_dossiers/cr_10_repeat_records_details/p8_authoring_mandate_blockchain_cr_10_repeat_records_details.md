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
    code: blockchain::WF_REGISTER_ACTOR_V2
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
    - blockchain::CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
  - wave: '1'
    step: '2'
    code: blockchain::CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
    action: NEW
    subdomain: identity
    depends_on: null
  critical_path:
  - position: '1'
    code: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
  - position: '2'
    code: blockchain::RB_IDENTITY_BINDINGS_V0
  - position: '3'
    code: blockchain::WF_ACCEPT_ACTOR_V1
  - position: '4'
    code: blockchain::TI_ACCEPT_ACTOR_V0
  mandate_artifact_summary:
  - action: NEW
    count: '2'
    description: 1 CC, 1 WF
  field_declarations:
  - code: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    subdomain_field: identity
  - code: blockchain::STRUCTURE_WALLET_STORAGE_V1
    subdomain_field: wallet
  - code: blockchain::VOCAB_WALLET_CLASSIFICATION_V1
    subdomain_field: wallet
  - code: blockchain::AC_PARTICIPANT_V0
    subdomain_field: identity
  - code: blockchain::EV_ACTOR_ACCEPTED_V1
    subdomain_field: identity
  - code: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
    subdomain_field: identity
  - code: blockchain::EV_ACTOR_REJECTED_V0
    subdomain_field: identity
  - code: blockchain::EV_WALLET_CREATED_V0
    subdomain_field: wallet
  - code: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
    subdomain_field: wallet
  - code: blockchain::CC_CHECK_REGISTER_ACTOR_SUBMISSION_V0
    subdomain_field: identity
  - code: blockchain::CC_CLAIM_ACTOR_CONTACT_ADDRESS_V0
    subdomain_field: identity
  - code: blockchain::CC_LIST_ACTORS_V0
    subdomain_field: identity
  - code: blockchain::CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    subdomain_field: identity
  - code: blockchain::CC_RECORD_IDENTITY_MOMENT_V0
    subdomain_field: identity
  - code: blockchain::CC_REQUIRE_GROUNDS_TO_REJECT_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::CC_RESOLVE_ACTOR_IDENTITY_V0
    subdomain_field: identity
  - code: blockchain::CC_WRITE_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::CC_CLAIM_WALLET_ADDRESS_V0
    subdomain_field: wallet
  - code: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    subdomain_field: wallet
  - code: blockchain::CC_RECORD_WALLET_MOMENT_V0
    subdomain_field: wallet
  - code: blockchain::CC_REQUIRE_ACCEPTED_ACTOR_V0
    subdomain_field: wallet
  - code: blockchain::CC_REQUIRE_WALLET_ADDRESS_FREE_V0
    subdomain_field: wallet
  - code: blockchain::CC_WRITE_WALLET_V0
    subdomain_field: wallet
  - code: blockchain::IN_ACTOR_ACCEPTANCE_V0
    subdomain_field: identity
  - code: blockchain::IN_ACTOR_REGISTERED_V0
    subdomain_field: identity
  - code: blockchain::IN_ACTOR_REJECTION_V0
    subdomain_field: identity
  - code: blockchain::IN_LIST_ACTORS_V0
    subdomain_field: identity
  - code: blockchain::IN_WALLET_CREATION_V0
    subdomain_field: wallet
  - code: blockchain::TE_ACCEPT_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::TE_REGISTER_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::TE_REJECT_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::CC_DERIVE_WALLET_ADDRESS_V0
    subdomain_field: wallet
  - code: blockchain::RB_IDENTITY_BINDINGS_V0
    subdomain_field: identity
  - code: blockchain::RB_WALLET_BINDINGS_V1
    subdomain_field: wallet
  - code: blockchain::WF_ACCEPT_ACTOR_V1
    subdomain_field: identity
  - code: blockchain::WF_LIST_ACTORS_V0
    subdomain_field: identity
  - code: blockchain::WF_REJECT_ACTOR_V1
    subdomain_field: identity
  - code: blockchain::WF_CREATE_WALLET_V1
    subdomain_field: wallet
  - code: blockchain::TI_ACCEPT_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::TI_REGISTER_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::TI_REJECT_ACTOR_V0
    subdomain_field: identity
  - code: blockchain::CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
    subdomain_field: identity
  - code: blockchain::WF_REGISTER_ACTOR_V2
    subdomain_field: identity
  new_capabilities:
  - code: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
    purpose: Derives an address from supplied key material; the same material always yields the same address
    inputs: key_material:string
    outputs: address:string
  new_intents:
  - code: blockchain::IN_ACTOR_ACCEPTANCE_V0
    purpose: A request to accept actor
    workflow: WF_ACCEPT_ACTOR_V1
    inputs: contact_address:string, verifying_authority:string, grounds:string
  - code: blockchain::IN_ACTOR_REGISTERED_V0
    purpose: A request to register actor
    workflow: WF_REGISTER_ACTOR_V2
    inputs: actor_record:object
  - code: blockchain::IN_ACTOR_REJECTION_V0
    purpose: A request to reject actor
    workflow: WF_REJECT_ACTOR_V1
    inputs: contact_address:string, verifying_authority:string, grounds:string
  - code: blockchain::IN_LIST_ACTORS_V0
    purpose: A request to list actors
    workflow: WF_LIST_ACTORS_V0
    inputs: state:string
  - code: blockchain::IN_WALLET_CREATION_V0
    purpose: A request to create wallet
    workflow: WF_CREATE_WALLET_V1
    inputs: contact_address:string, key_material:string
  cross_subdomain_notes: []
```

The 42 artifacts of `blockchain`'s design of record, scheduled in dependency order. Written by
`python -m transformation.record` from the P7 beside it. The mandate orders the build; it decides
nothing.
