# Stage 8 — Authoring Mandate: blockchain / wallet
**Stage:** 8 — Authoring Mandate
**CR:** cr_04_wallet
**Status:** DRAFT
**Feeds:** Construction

IN WHAT ORDER. Mechanically derived from the design; it reconciles with Stage 7 exactly and adds
nothing.

---

## 1. Build Order

<!-- register:build_order optional -->
| Wave | Step | Code | Action (REPLACE, EXTEND, NEW) | Subdomain | Depends On |
|------|------|------|-------------------------------|-----------|------------|
| 1 | 1 | blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0 | NEW | wallet | — |


---

## 2. Critical Path

<!-- register:critical_path optional -->
| Position | Code |
|----------|------|
| 1 | blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0 |


---

## 3. Artifact Summary

<!-- register:mandate_artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Count | Description |
|-------------------------------|-------|-------------|
| NEW | 1 | The step that refuses a wallet to a person the business has not accepted. |
| EXTEND | 22 | The wallet function and the identity acts it depends on, redeclared whole so that the design and the artifacts agree — carrying the reach the act declares and the refusal it was always meant to make. |


---

## 4. Field Declarations

<!-- register:field_declarations -->
| Code | Subdomain Field |
|------|-----------------|
| blockchain::IN_WALLET_CREATION_V0 | wallet |
| blockchain::WF_CREATE_WALLET_V0 | wallet |
| blockchain::CC_DETERMINE_WALLET_IDENTITY_V0 | wallet |
| blockchain::CC_CLAIM_WALLET_IDENTITY_V0 | wallet |
| blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0 | wallet |
| blockchain::CC_CREATE_WALLET_RECORD_V0 | wallet |
| blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | wallet |
| blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0 | wallet |
| blockchain::EV_WALLET_CREATED_V0 | wallet |
| blockchain::RB_WALLET_BINDINGS_V0 | wallet |
| blockchain::STRUCTURE_WALLET_STORAGE_V0 | wallet |
| blockchain::VOCAB_WALLET_CLASSIFICATION_V0 | wallet |
| blockchain::IN_ACTOR_ACCEPTANCE_V0 | identity |
| blockchain::IN_ACTOR_REJECTION_V0 | identity |
| blockchain::WF_ACCEPT_ACTOR_V0 | identity |
| blockchain::WF_REJECT_ACTOR_V0 | identity |
| blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 | identity |
| blockchain::WF_REGISTER_ACTOR_V0 | identity |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | identity |
| blockchain::RB_IDENTITY_BINDINGS_V0 | identity |
| blockchain::TI_ACCEPT_ACTOR_V0 | identity |
| blockchain::TI_REJECT_ACTOR_V0 | identity |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | identity |
| blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0 | wallet |

---

## 5. New Capabilities

<!-- register:new_capabilities optional -->
| Code | Purpose | Inputs | Outputs |
|------|---------|--------|---------|
| blockchain::CC_DETERMINE_WALLET_IDENTITY_V0 | Derives the wallet's identity from the person who holds it | holder, wallet_id_prefix | wallet_id |
| blockchain::CC_CLAIM_WALLET_IDENTITY_V0 | Claims the identity, refusing when the person already holds a wallet | wallet_id | result_status |
| blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0 | Establishes the address others may pay to, from supplied key material | key_material | address |
| blockchain::CC_CREATE_WALLET_RECORD_V0 | Records the wallet with a balance of zero, its denomination and its classification | wallet_id, wallet_fields | result_status |
| blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | Records that the wallet was created, for whom, and when | stream_id, occurrence_fields | result_status |
| blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 | Refuses a rejection that states no grounds, before anything is recorded | grounds, grounds_rules | valid |
| blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0 | Works out an address from supplied key material; the same material always yields the same address | key_material | address |
| blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0 | Refuses a wallet for a person the business has not accepted, before anything is claimed or recorded. | holder_state:string, states_admitting_a_wallet:array | is_accepted:boolean |

---

## 6. New Intents

<!-- register:new_intents optional -->
| Code | Purpose | Workflow | Inputs |
|------|---------|----------|--------|
| blockchain::IN_WALLET_CREATION_V0 | Admits a request to give an accepted person a wallet | blockchain::WF_CREATE_WALLET_V0 | contact_address, key_material, wallet_id_prefix |
| blockchain::IN_ACTOR_ACCEPTANCE_V0 | Admits a request to accept a person | blockchain::WF_ACCEPT_ACTOR_V0 | contact_address, verifying_authority |
| blockchain::IN_ACTOR_REJECTION_V0 | Admits a request to reject a person, refusing one that states no grounds | blockchain::WF_REJECT_ACTOR_V0 | contact_address, verifying_authority, grounds |

---

## 7. Cross-Subdomain Notes

<!-- register:cross_subdomain_notes optional -->
| Code | Note |
|------|------|
| blockchain::CC_RESOLVE_ACTOR_V0 | Owned by identity, read by wallet's workflow. Wallet reads a person and never writes one. |
| blockchain::EV_ACTOR_ACCEPTED_V0 | Declared and announced by identity. Wallet consumes the moment and declares none of the three. |
| blockchain::WF_REGISTER_ACTOR_V0 | Extended by this change although wallet does not use it, because the three declared moments are announced together or the gap simply moves. |
| blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 | Built last: it declares the second subdomain, and declaring a subdomain whose artifacts do not yet exist would compile to nothing. |
