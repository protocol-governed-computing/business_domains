# Stage 7 — Design Intent: blockchain / identity and wallet

**Stage:** 7 — Design Intent
**CR:** cr_06_routing_closure
**Status:** DRAFT
**Feeds:** Stage 8 — Authoring Mandate

Every binding names a field the capability declares, read from the pinned baseline
`f8356d9c8938aea16ab7850d7bda964d8d16c42c64e5db9056d5fe58040ec1d0`.

Nothing new is authored. Eight artifacts identity and wallet already hold are redeclared whole. Four
contracts gain an answer for a failed record at the five steps whose stores declare one. Four acts
route a failed record to the rejected ending they already have, at thirteen nodes. Every other step,
route, binding and field is restated exactly as it stands.

---

## 1. Design Decisions Resolution

<!-- register:design_resolution optional -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|
| Each step whose store can fail ends its contract on a failed record | No act carries on past a record it could not read or write | The lookup and the read in blockchain::CC_RESOLVE_ACTOR_V0, the claim in blockchain::CC_CLAIM_WALLET_IDENTITY_V0, the write in blockchain::CC_CREATE_WALLET_RECORD_V0 and the append in blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 each route BACKEND_ERROR to exit | S4 design_decisions #1 |
| Each act routes a failed record to its rejected ending | Every act ends as succeeded or rejected | Every node of blockchain::WF_REGISTER_ACTOR_V0, blockchain::WF_ACCEPT_ACTOR_V0, blockchain::WF_REJECT_ACTOR_V0 and blockchain::WF_CREATE_WALLET_V0 whose contract can end with BACKEND_ERROR routes it to EXIT_REJECTED | S4 design_decisions #2 |
| A contract that can now end with a failed record says so | A contract states every outcome it can end with | The exit routes added above extend what blockchain::CC_RESOLVE_ACTOR_V0 and blockchain::CC_CLAIM_WALLET_IDENTITY_V0 can end with; the other two already end with it through their clock step | S4 design_decisions #3 |
| Records made before a failure are left as they are | The record is added to and never rewritten | No compensation, repair or backfill step is designed | S4 design_decisions #4 |

---

## 2. Artifact Inventory — Existing Artifacts

<!-- register:existing_inventory -->
| FQDN | Action (REPLACE, REUSE, EXTEND, REVIEW) | Summary | Reason | Source Finding |
|------|------------------------------------------|---------|--------|----------------|
| blockchain::CC_RESOLVE_ACTOR_V0 | EXTEND | Answers which actor a contact address denotes, and reports when none does | A step carries on past a failed record its store declares. | S6 pps_artifacts_requiring_action #1 |
| blockchain::CC_CLAIM_WALLET_IDENTITY_V0 | EXTEND | Claims the identity, and refuses when the person already holds a wallet | A step carries on past a failed record its store declares. | S6 pps_artifacts_requiring_action #2 |
| blockchain::CC_CREATE_WALLET_RECORD_V0 | EXTEND | Records the wallet with a balance of zero, its denomination and its classification | A step carries on past a failed record its store declares. | S6 pps_artifacts_requiring_action #3 |
| blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | EXTEND | Records the moment on the wallet's trail | A step carries on past a failed record its store declares. | S6 pps_artifacts_requiring_action #4 |
| blockchain::WF_REGISTER_ACTOR_V0 | EXTEND | The governed sequence that admits a person as an unverified actor, and announces that it did | It leaves a failed record unanswered. | S6 pps_artifacts_requiring_action #5 |
| blockchain::WF_ACCEPT_ACTOR_V0 | EXTEND | The governed sequence that records an acceptance and announces it | It leaves a failed record unanswered. | S6 pps_artifacts_requiring_action #6 |
| blockchain::WF_REJECT_ACTOR_V0 | EXTEND | The governed sequence that records a rejection, with grounds required, and announces it | It leaves a failed record unanswered. | S6 pps_artifacts_requiring_action #7 |
| blockchain::WF_CREATE_WALLET_V0 | EXTEND | The governed sequence that gives an accepted person a wallet and records that it did | It leaves a failed record unanswered. | S6 pps_artifacts_requiring_action #8 |
| capability_side_effects::CS_REGISTRY_V0 | REUSE |  | Named by an amended artifact, unchanged. | S6 cross_subdomain_deps #1 |
| capability_side_effects::CS_MUTABLE_JSON_V0 | REUSE |  | Named by an amended artifact, unchanged. | S6 cross_subdomain_deps #1 |
| capability_side_effects::CS_CLOCK_V0 | REUSE |  | Named by an amended artifact, unchanged. | S6 cross_subdomain_deps #1 |
| capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | REUSE |  | Named by an amended artifact, unchanged. | S6 cross_subdomain_deps #1 |
| capability_side_effects::CS_APPENDONLY_JSONL_V0 | REUSE |  | Named by an amended artifact, unchanged. | S6 cross_subdomain_deps #1 |
| blockchain::CC_VALIDATE_REGISTRATION_V0 | REUSE |  | Named by an amended artifact, unchanged. | S6 cross_subdomain_deps #1 |
| blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | REUSE |  | Named by an amended artifact, unchanged. | S6 pps_artifacts_requiring_action #9 |
| blockchain::CC_REGISTER_ACTOR_V0 | REUSE |  | Named by an amended artifact, unchanged. | S6 pps_artifacts_requiring_action #10 |
| blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | REUSE |  | Named by an amended artifact, unchanged. | S6 pps_artifacts_requiring_action #11 |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | REUSE |  | Named by an amended artifact, unchanged. | S6 pps_artifacts_requiring_action #12 |
| blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 | REUSE |  | Named by an amended artifact, unchanged. | S6 cross_subdomain_deps #1 |
| blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0 | REUSE |  | Named by an amended artifact, unchanged. | S6 cross_subdomain_deps #1 |
| blockchain::CC_DETERMINE_WALLET_IDENTITY_V0 | REUSE |  | Named by an amended artifact, unchanged. | S6 cross_subdomain_deps #1 |
| blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0 | REUSE |  | Named by an amended artifact, unchanged. | S6 cross_subdomain_deps #1 |
| blockchain::RB_IDENTITY_BINDINGS_V0 | REUSE |  | Named by an amended artifact, unchanged. | S6 cross_subdomain_deps #1 |
| blockchain::STRUCTURE_IDENTITY_STORAGE_V0 | REUSE |  | Named by an amended artifact, unchanged. | S6 cross_subdomain_deps #1 |
| blockchain::RB_WALLET_BINDINGS_V0 | REUSE |  | Named by an amended artifact, unchanged. | S6 cross_subdomain_deps #1 |
| blockchain::STRUCTURE_WALLET_STORAGE_V0 | REUSE |  | Named by an amended artifact, unchanged. | S6 cross_subdomain_deps #1 |
| blockchain::IN_ACTOR_REGISTERED_V0 | REUSE |  | Named by an amended artifact, unchanged. | S6 cross_subdomain_deps #1 |
| blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0 | REUSE |  | Named by an amended artifact, unchanged. | S6 cross_subdomain_deps #1 |
| blockchain::IN_ACTOR_ACCEPTANCE_V0 | REUSE |  | Named by an amended artifact, unchanged. | S6 cross_subdomain_deps #1 |
| blockchain::EV_ACTOR_ACCEPTED_V0 | REUSE |  | Named by an amended artifact, unchanged. | S6 cross_subdomain_deps #1 |
| blockchain::IN_ACTOR_REJECTION_V0 | REUSE |  | Named by an amended artifact, unchanged. | S6 cross_subdomain_deps #1 |
| blockchain::EV_ACTOR_REJECTED_V0 | REUSE |  | Named by an amended artifact, unchanged. | S6 cross_subdomain_deps #1 |
| blockchain::IN_WALLET_CREATION_V0 | REUSE |  | Named by an amended artifact, unchanged. | S6 cross_subdomain_deps #1 |
| blockchain::EV_WALLET_CREATED_V0 | REUSE |  | Named by an amended artifact, unchanged. | S6 cross_subdomain_deps #1 |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | REUSE |  | Named by an amended artifact, unchanged. | S6 cross_subdomain_deps #1 |
| blockchain::AC_PARTICIPANT_V0 | REUSE | | The authority context the four acts run under, unchanged. | S6 pps_artifacts_requiring_action #5 |

---

## 3. Artifact Family Mapping — New Artifacts

<!-- register:new_artifacts optional business_language=capability -->
| Capability | Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE) | Code | Summary | Owner Subdomain | Status | Source Finding |
|------------|------------------------------------------------|------|---------|-----------------|--------|----------------|

---

## 4. Runtime Binding (RB) Declarations

<!-- register:rb_declarations -->
| RB Code | Binds WF | CS Bindings | Storage Structure | Source Finding |
|---------|----------|-------------|-------------------|----------------|
| blockchain::RB_IDENTITY_BINDINGS_V0 | blockchain::WF_REGISTER_ACTOR_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_CLOCK_V0 | blockchain::STRUCTURE_IDENTITY_STORAGE_V0 | S6 pps_artifacts_requiring_action #5 |
| blockchain::RB_IDENTITY_BINDINGS_V0 | blockchain::WF_ACCEPT_ACTOR_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_CLOCK_V0 | blockchain::STRUCTURE_IDENTITY_STORAGE_V0 | S6 pps_artifacts_requiring_action #6 |
| blockchain::RB_IDENTITY_BINDINGS_V0 | blockchain::WF_REJECT_ACTOR_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_CLOCK_V0 | blockchain::STRUCTURE_IDENTITY_STORAGE_V0 | S6 pps_artifacts_requiring_action #7 |
| blockchain::RB_WALLET_BINDINGS_V0 | blockchain::WF_CREATE_WALLET_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_CLOCK_V0 | blockchain::STRUCTURE_WALLET_STORAGE_V0 | S6 pps_artifacts_requiring_action #8 |

---

## 5. Execution Topology

<!-- register:execution_topology optional_columns=runs -->
| Workflow | Node | Runs | Node Type (IN, CC, EXIT, EXIT_SUCCESS) | Routing | Source Finding |
|----------|------|------|----------------------------------------|---------|----------------|
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::IN_ACTOR_REGISTERED_V0 |  | IN | ACK -> blockchain::CC_VALIDATE_REGISTRATION_V0; NACK -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #5 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_VALIDATE_REGISTRATION_V0 |  | CC | SUCCESS -> blockchain::CC_CLAIM_CONTACT_ADDRESS_V0; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #5 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 |  | CC | SUCCESS -> blockchain::CC_REGISTER_ACTOR_V0; ALREADY_EXISTS -> blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #5 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_REGISTER_ACTOR_V0 |  | CC | SUCCESS -> blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #5 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 |  | CC | SUCCESS -> EXIT_SUCCESS; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #5 |
| blockchain::WF_REGISTER_ACTOR_V0 | EXIT_SUCCESS |  | EXIT_SUCCESS | emit blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0 | S6 pps_artifacts_requiring_action #5 |
| blockchain::WF_REGISTER_ACTOR_V0 | EXIT_REJECTED |  | EXIT | — | S6 pps_artifacts_requiring_action #5 |
| blockchain::WF_ACCEPT_ACTOR_V0 | blockchain::IN_ACTOR_ACCEPTANCE_V0 |  | IN | ACK -> blockchain::CC_RESOLVE_ACTOR_V0; NACK -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #6 |
| blockchain::WF_ACCEPT_ACTOR_V0 | blockchain::CC_RESOLVE_ACTOR_V0 |  | CC | SUCCESS -> blockchain::CC_RECORD_VERIFICATION_DECISION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #6 |
| blockchain::WF_ACCEPT_ACTOR_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 |  | CC | SUCCESS -> blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #6 |
| blockchain::WF_ACCEPT_ACTOR_V0 | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 |  | CC | SUCCESS -> EXIT_SUCCESS; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #6 |
| blockchain::WF_ACCEPT_ACTOR_V0 | EXIT_SUCCESS |  | EXIT_SUCCESS | emit blockchain::EV_ACTOR_ACCEPTED_V0 | S6 pps_artifacts_requiring_action #6 |
| blockchain::WF_ACCEPT_ACTOR_V0 | EXIT_REJECTED |  | EXIT | — | S6 pps_artifacts_requiring_action #6 |
| blockchain::WF_REJECT_ACTOR_V0 | blockchain::IN_ACTOR_REJECTION_V0 |  | IN | ACK -> blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0; NACK -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #7 |
| blockchain::WF_REJECT_ACTOR_V0 | blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 |  | CC | SUCCESS -> blockchain::CC_RESOLVE_ACTOR_V0; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #7 |
| blockchain::WF_REJECT_ACTOR_V0 | blockchain::CC_RESOLVE_ACTOR_V0 |  | CC | SUCCESS -> blockchain::CC_RECORD_VERIFICATION_DECISION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #7 |
| blockchain::WF_REJECT_ACTOR_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 |  | CC | SUCCESS -> blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #7 |
| blockchain::WF_REJECT_ACTOR_V0 | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 |  | CC | SUCCESS -> EXIT_SUCCESS; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #7 |
| blockchain::WF_REJECT_ACTOR_V0 | EXIT_SUCCESS |  | EXIT_SUCCESS | emit blockchain::EV_ACTOR_REJECTED_V0 | S6 pps_artifacts_requiring_action #7 |
| blockchain::WF_REJECT_ACTOR_V0 | EXIT_REJECTED |  | EXIT | — | S6 pps_artifacts_requiring_action #7 |
| blockchain::WF_CREATE_WALLET_V0 | blockchain::IN_WALLET_CREATION_V0 |  | IN | ACK -> blockchain::CC_RESOLVE_ACTOR_V0; NACK -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #8 |
| blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_RESOLVE_ACTOR_V0 |  | CC | SUCCESS -> blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #8 |
| blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0 |  | CC | SUCCESS -> blockchain::CC_DETERMINE_WALLET_IDENTITY_V0; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #8 |
| blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_DETERMINE_WALLET_IDENTITY_V0 |  | CC | SUCCESS -> blockchain::CC_CLAIM_WALLET_IDENTITY_V0; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #8 |
| blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_CLAIM_WALLET_IDENTITY_V0 |  | CC | SUCCESS -> blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #8 |
| blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0 |  | CC | SUCCESS -> blockchain::CC_CREATE_WALLET_RECORD_V0; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #8 |
| blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_CREATE_WALLET_RECORD_V0 |  | CC | SUCCESS -> blockchain::CC_APPEND_WALLET_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #8 |
| blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 |  | CC | SUCCESS -> EXIT_SUCCESS; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #8 |
| blockchain::WF_CREATE_WALLET_V0 | EXIT_SUCCESS |  | EXIT_SUCCESS | emit blockchain::EV_WALLET_CREATED_V0 | S6 pps_artifacts_requiring_action #8 |
| blockchain::WF_CREATE_WALLET_V0 | EXIT_REJECTED |  | EXIT | — | S6 pps_artifacts_requiring_action #8 |

---

## 6. Capability Composition

<!-- register:cc_composition optional -->
| CC Code | Step | Step Name | Capability | Kind (CT, CS) | Operation | Store | Consumes | Produces | Routing | Interpreted By | Semantic Status | Interface |
|---------|------|-----------|------------|---------------|-----------|-------|----------|----------|---------|----------------|-----------------|-----------|
| blockchain::CC_RESOLVE_ACTOR_V0 | 1 | resolve_address | capability_side_effects::CS_REGISTRY_V0 | CS | RESOLVE | CONTACT_ADDRESS_REGISTRY | key_or_address | target_ref | SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | NOT_FOUND | — |
| blockchain::CC_RESOLVE_ACTOR_V0 | 2 | read_actor | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | READ | ACTORS | key | value | SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | NOT_FOUND | — |
| blockchain::CC_CLAIM_WALLET_IDENTITY_V0 | 1 | claim_wallet_identity | capability_side_effects::CS_REGISTRY_V0 | CS | REGISTER | WALLET_IDENTITIES | key | result_status | SUCCESS -> continue; ALREADY_EXISTS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | in: key=key; out: result_status=result_status |
| blockchain::CC_CREATE_WALLET_RECORD_V0 | 1 | read_created_at | capability_side_effects::CS_CLOCK_V0 | CS | NOW | — |  | timestamp | SUCCESS -> continue; BACKEND_ERROR -> exit | — | SUCCESS |  |
| blockchain::CC_CREATE_WALLET_RECORD_V0 | 2 | assemble_wallet | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | CT | ASSEMBLE_RECORD | — | fields | record | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: fields=fields; out: record=record |
| blockchain::CC_CREATE_WALLET_RECORD_V0 | 3 | write_wallet | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | WRITE | WALLETS | key, value | result_status | SUCCESS -> continue; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | in: key=key, value=value; out: result_status=result_status |
| blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | 1 | read_occurred_at | capability_side_effects::CS_CLOCK_V0 | CS | NOW | — |  | timestamp | SUCCESS -> continue; BACKEND_ERROR -> exit | — | SUCCESS |  |
| blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | 2 | assemble_occurrence | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | CT | ASSEMBLE_RECORD | — | fields | record | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: fields=fields; out: record=record |
| blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | 3 | append_occurrence | capability_side_effects::CS_APPENDONLY_JSONL_V0 | CS | APPEND | WALLET_OCCURRENCES | stream_id, record | result_status | SUCCESS -> continue; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | in: stream_id=stream_id, record=record; out: result_status=result_status |

---

## 7. Step Bindings

<!-- register:step_bindings optional -->
| Owner | Step | Direction (INPUT, OUTPUT) | Field | Bound To | Source Finding |
|-------|------|--------------------------|-------|----------|----------------|
| blockchain::CC_RESOLVE_ACTOR_V0 | resolve_address | INPUT | key_or_address | inputs.contact_address | S7 cc_composition resolve_address |
| blockchain::CC_RESOLVE_ACTOR_V0 | resolve_address | OUTPUT | target_ref | capability_result.target_ref | S7 cc_composition resolve_address |
| blockchain::CC_RESOLVE_ACTOR_V0 | read_actor | INPUT | key | inputs.contact_address | S7 cc_composition read_actor |
| blockchain::CC_RESOLVE_ACTOR_V0 | read_actor | OUTPUT | value | capability_result.value | S7 cc_composition read_actor |
| blockchain::CC_CLAIM_WALLET_IDENTITY_V0 | claim_wallet_identity | INPUT | key | inputs.wallet_id | S7 cc_composition claim_wallet_identity |
| blockchain::CC_CLAIM_WALLET_IDENTITY_V0 | claim_wallet_identity | OUTPUT | result_status | capability_result.result_status | S7 cc_composition claim_wallet_identity |
| blockchain::CC_CREATE_WALLET_RECORD_V0 | read_created_at | OUTPUT | timestamp | capability_result.timestamp | S7 cc_composition read_created_at |
| blockchain::CC_CREATE_WALLET_RECORD_V0 | assemble_wallet | INPUT | fields | inputs.wallet_fields | S7 cc_composition assemble_wallet |
| blockchain::CC_CREATE_WALLET_RECORD_V0 | assemble_wallet | OUTPUT | record | capability_result.record | S7 cc_composition assemble_wallet |
| blockchain::CC_CREATE_WALLET_RECORD_V0 | write_wallet | INPUT | key | inputs.wallet_id | S7 cc_composition write_wallet |
| blockchain::CC_CREATE_WALLET_RECORD_V0 | write_wallet | INPUT | value | results.assemble_wallet.record | S7 cc_composition write_wallet |
| blockchain::CC_CREATE_WALLET_RECORD_V0 | write_wallet | OUTPUT | result_status | capability_result.result_status | S7 cc_composition write_wallet |
| blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | read_occurred_at | OUTPUT | timestamp | capability_result.timestamp | S7 cc_composition read_occurred_at |
| blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | assemble_occurrence | INPUT | fields | inputs.occurrence_fields | S7 cc_composition assemble_occurrence |
| blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | assemble_occurrence | OUTPUT | record | capability_result.record | S7 cc_composition assemble_occurrence |
| blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | append_occurrence | INPUT | stream_id | inputs.stream_id | S7 cc_composition append_occurrence |
| blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | append_occurrence | INPUT | record | results.assemble_occurrence.record | S7 cc_composition append_occurrence |
| blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | append_occurrence | OUTPUT | result_status | capability_result.result_status | S7 cc_composition append_occurrence |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_VALIDATE_REGISTRATION_V0 | INPUT | actor_record | payload.actor_record | S7 execution_topology blockchain::CC_VALIDATE_REGISTRATION_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | INPUT | actor_record | payload.actor_record | S7 execution_topology blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | INPUT | address_path | payload.address_path | S7 execution_topology blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | INPUT | address_type | payload.address_type | S7 execution_topology blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_REGISTER_ACTOR_V0 | INPUT | actor_fields | {'name': '$.payload.actor_record.name', 'contact_address': '$.payload.actor_record.contact_address', 'state': 'UNVERIFIED', 'currency_preference': '$.payload.actor_record.currency_preference', 'language': '$.payload.actor_record.language'} | S7 execution_topology blockchain::CC_REGISTER_ACTOR_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_REGISTER_ACTOR_V0 | INPUT | contact_address | results.CC_CLAIM_CONTACT_ADDRESS_V0.result | S7 execution_topology blockchain::CC_REGISTER_ACTOR_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | INPUT | occurrence_fields | payload.occurrence_fields | S7 execution_topology blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | INPUT | stream_id | payload.stream_id | S7 execution_topology blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | INPUT | contact_address | results.CC_CLAIM_CONTACT_ADDRESS_V0.result | S7 execution_topology blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 |
| blockchain::WF_ACCEPT_ACTOR_V0 | blockchain::CC_RESOLVE_ACTOR_V0 | INPUT | contact_address | payload.contact_address | S7 execution_topology blockchain::CC_RESOLVE_ACTOR_V0 |
| blockchain::WF_ACCEPT_ACTOR_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | current_state | results.CC_RESOLVE_ACTOR_V0.value.state | S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0 |
| blockchain::WF_ACCEPT_ACTOR_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | decision | ACCEPTED | S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0 |
| blockchain::WF_ACCEPT_ACTOR_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | verifying_authority | payload.verifying_authority | S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0 |
| blockchain::WF_ACCEPT_ACTOR_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | contact_address | payload.contact_address | S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0 |
| blockchain::WF_ACCEPT_ACTOR_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | grounds | payload.grounds | S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0 |
| blockchain::WF_ACCEPT_ACTOR_V0 | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | INPUT | occurrence_fields | payload.occurrence_fields | S7 execution_topology blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 |
| blockchain::WF_ACCEPT_ACTOR_V0 | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | INPUT | stream_id | payload.stream_id | S7 execution_topology blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 |
| blockchain::WF_ACCEPT_ACTOR_V0 | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | INPUT | contact_address | payload.contact_address | S7 execution_topology blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 |
| blockchain::WF_REJECT_ACTOR_V0 | blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 | INPUT | grounds | payload.grounds | S7 execution_topology blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 |
| blockchain::WF_REJECT_ACTOR_V0 | blockchain::CC_RESOLVE_ACTOR_V0 | INPUT | contact_address | payload.contact_address | S7 execution_topology blockchain::CC_RESOLVE_ACTOR_V0 |
| blockchain::WF_REJECT_ACTOR_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | current_state | results.CC_RESOLVE_ACTOR_V0.value.state | S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0 |
| blockchain::WF_REJECT_ACTOR_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | decision | REJECTED | S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0 |
| blockchain::WF_REJECT_ACTOR_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | verifying_authority | payload.verifying_authority | S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0 |
| blockchain::WF_REJECT_ACTOR_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | contact_address | payload.contact_address | S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0 |
| blockchain::WF_REJECT_ACTOR_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | grounds | payload.grounds | S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0 |
| blockchain::WF_REJECT_ACTOR_V0 | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | INPUT | occurrence_fields | payload.occurrence_fields | S7 execution_topology blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 |
| blockchain::WF_REJECT_ACTOR_V0 | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | INPUT | stream_id | payload.stream_id | S7 execution_topology blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 |
| blockchain::WF_REJECT_ACTOR_V0 | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | INPUT | contact_address | payload.contact_address | S7 execution_topology blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 |
| blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0 | INPUT | holder_state | results.CC_RESOLVE_ACTOR_V0.value.state | S7 execution_topology blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0 |
| blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0 | INPUT | states_admitting_a_wallet | ['ACCEPTED'] | S7 execution_topology blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0 |
| blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_DETERMINE_WALLET_IDENTITY_V0 | INPUT | holder | results.CC_RESOLVE_ACTOR_V0.value.contact_address | S7 execution_topology blockchain::CC_DETERMINE_WALLET_IDENTITY_V0 |
| blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_DETERMINE_WALLET_IDENTITY_V0 | INPUT | wallet_id_prefix | payload.wallet_id_prefix | S7 execution_topology blockchain::CC_DETERMINE_WALLET_IDENTITY_V0 |
| blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_CLAIM_WALLET_IDENTITY_V0 | INPUT | wallet_id | results.CC_DETERMINE_WALLET_IDENTITY_V0.id | S7 execution_topology blockchain::CC_CLAIM_WALLET_IDENTITY_V0 |
| blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0 | INPUT | key_material | payload.key_material | S7 execution_topology blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0 |
| blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_CREATE_WALLET_RECORD_V0 | INPUT | wallet_id | results.CC_DETERMINE_WALLET_IDENTITY_V0.id | S7 execution_topology blockchain::CC_CREATE_WALLET_RECORD_V0 |
| blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_CREATE_WALLET_RECORD_V0 | INPUT | wallet_fields | payload.wallet_fields | S7 execution_topology blockchain::CC_CREATE_WALLET_RECORD_V0 |
| blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | INPUT | stream_id | results.CC_DETERMINE_WALLET_IDENTITY_V0.id | S7 execution_topology blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 |
| blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | INPUT | occurrence_fields | payload.occurrence_fields | S7 execution_topology blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 |
| blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_RESOLVE_ACTOR_V0 | INPUT | contact_address | payload.contact_address | S6 pps_artifacts_requiring_action #8 |

---

## 8. Interface Fields

<!-- register:interface_fields optional -->
| Artifact | Direction (INPUT, OUTPUT, ATTRIBUTE) | Field | Type | Required (YES, NO) | Default | Meaning |
|----------|--------------------------------------|-------|------|--------------------|---------|---------|
| blockchain::CC_RESOLVE_ACTOR_V0 | INPUT | contact_address | string | YES |  | The address naming the actor to resolve |
| blockchain::CC_RESOLVE_ACTOR_V0 | OUTPUT | value | object | YES |  | The actor and its current state, or absent when none is held |
| blockchain::CC_CLAIM_WALLET_IDENTITY_V0 | INPUT | wallet_id | string | YES |  | The identity being claimed. |
| blockchain::CC_CLAIM_WALLET_IDENTITY_V0 | OUTPUT | result_status | string | YES |  | Whether the claim succeeded, or the identity was already held. |
| blockchain::CC_CREATE_WALLET_RECORD_V0 | INPUT | wallet_id | string | YES |  | The wallet being recorded. |
| blockchain::CC_CREATE_WALLET_RECORD_V0 | INPUT | wallet_fields | object | YES |  | What the business holds about the wallet. |
| blockchain::CC_CREATE_WALLET_RECORD_V0 | OUTPUT | result_status | string | YES |  | Whether the wallet was recorded. |
| blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | INPUT | stream_id | string | YES |  | The trail the moment is added to. |
| blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | INPUT | occurrence_fields | object | YES |  | What the moment records. |
| blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | OUTPUT | result_status | string | YES |  | Whether the moment was recorded. |

---

## 9. Artifact Properties

<!-- register:artifact_properties optional -->
| Artifact | Property | Value | Source Finding |
|----------|----------|-------|----------------|
| blockchain::WF_REGISTER_ACTOR_V0 | emit.EXIT_SUCCESS | blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0 | S6 pps_artifacts_requiring_action #5 |
| blockchain::WF_ACCEPT_ACTOR_V0 | emit.EXIT_SUCCESS | blockchain::EV_ACTOR_ACCEPTED_V0 | S6 pps_artifacts_requiring_action #6 |
| blockchain::WF_ACCEPT_ACTOR_V0 | supersedes | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | S6 pps_artifacts_requiring_action #6 |
| blockchain::WF_REJECT_ACTOR_V0 | emit.EXIT_SUCCESS | blockchain::EV_ACTOR_REJECTED_V0 | S6 pps_artifacts_requiring_action #7 |
| blockchain::WF_REJECT_ACTOR_V0 | supersedes | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | S6 pps_artifacts_requiring_action #7 |
| blockchain::WF_CREATE_WALLET_V0 | emit.EXIT_SUCCESS | blockchain::EV_WALLET_CREATED_V0 | S6 pps_artifacts_requiring_action #8 |

---

## 10. Structure Stores

<!-- register:structure_stores optional -->
| Store Name | Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0) | Proposed Path | Used By | Source Finding |
|------------|------|------|------|----------------|
| WALLET_IDENTITIES | CS_REGISTRY_V0 | blockchain/wallet/wallet_identity_registry.jsonl | blockchain::CC_CLAIM_WALLET_IDENTITY_V0 | S6 pps_artifacts_requiring_action #2 |
| WALLETS | CS_MUTABLE_JSON_V0 | blockchain/wallet/wallets.json | blockchain::CC_CREATE_WALLET_RECORD_V0 | S6 pps_artifacts_requiring_action #3 |
| WALLET_OCCURRENCES | CS_APPENDONLY_JSONL_V0 | blockchain/wallet/wallet_occurrences.jsonl | blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | S6 pps_artifacts_requiring_action #4 |

---

## 11. Artifact Summary

<!-- register:artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Subdomain | Count | Artifacts |
|-------------------------------|-----------|-------|-----------|
| EXTEND | identity | 4 | blockchain::CC_RESOLVE_ACTOR_V0, blockchain::WF_REGISTER_ACTOR_V0, blockchain::WF_ACCEPT_ACTOR_V0, blockchain::WF_REJECT_ACTOR_V0 |
| EXTEND | wallet | 4 | blockchain::CC_CLAIM_WALLET_IDENTITY_V0, blockchain::CC_CREATE_WALLET_RECORD_V0, blockchain::CC_APPEND_WALLET_OCCURRENCE_V0, blockchain::WF_CREATE_WALLET_V0 |

---

## 12. Declared Reach

<!-- register:declared_reach optional -->
| Act | Consults | Source Finding |
|-----|----------|----------------|
| blockchain::WF_CREATE_WALLET_V0 | blockchain::RB_IDENTITY_BINDINGS_V0 | S6 pps_artifacts_requiring_action #8 |

---

## 13. Unchanged Registers

No transform, vocabulary, policy, entrance or generator is touched.

<!-- register:implementation_bindings optional -->
| CT Code | Module | Callable | Operation | Kind (atom, molecule) | Purity (ct_pure, ct_impure) | Refusal (raises, returns, never) | Source Finding |
|---|---|---|---|---|---|---|---|

<!-- register:vocabulary_extensions optional -->
| Vocabulary Code | Extends | Group | Casing | Value | Meaning | Source Finding |
|---|---|---|---|---|---|---|

<!-- register:runtime_policies optional -->
| RB Code | Capability | Key | Value | Source Finding |
|---|---|---|---|---|

<!-- register:transport_bindings optional -->
| Artifact | Direction (INGRESS, EGRESS) | Operation | Handler Kind (WF_INVOCATION, SNAPSHOT_READ) | Handler Target | Field | Bound To | Source Finding |
|---|---|---|---|---|---|---|---|

<!-- register:generation_provenance optional -->
| Artifact | Generator | Generator Sources | Source Finding |
|---|---|---|---|

---

## 14. Refusal Discharge

Each refusal the business named is discharged where a failed record reaches the rejected ending.

<!-- register:refusal_discharge optional -->
| Operation | Refused When | Act | Step | Outcome | Source Finding |
|-----------|--------------|-----|------|---------|----------------|
| Registering a person | A record the registration needs fails | blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | BACKEND_ERROR | S0 operation_refusals #1 |
| Registering a person | A record the registration needs fails | blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_REGISTER_ACTOR_V0 | BACKEND_ERROR | S0 operation_refusals #1 |
| Registering a person | A record the registration needs fails | blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | BACKEND_ERROR | S0 operation_refusals #1 |
| Accepting a person | A record the acceptance needs fails | blockchain::WF_ACCEPT_ACTOR_V0 | blockchain::CC_RESOLVE_ACTOR_V0 | BACKEND_ERROR | S0 operation_refusals #2 |
| Accepting a person | A record the acceptance needs fails | blockchain::WF_ACCEPT_ACTOR_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | BACKEND_ERROR | S0 operation_refusals #2 |
| Accepting a person | A record the acceptance needs fails | blockchain::WF_ACCEPT_ACTOR_V0 | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | BACKEND_ERROR | S0 operation_refusals #2 |
| Rejecting a person | A record the rejection needs fails | blockchain::WF_REJECT_ACTOR_V0 | blockchain::CC_RESOLVE_ACTOR_V0 | BACKEND_ERROR | S0 operation_refusals #3 |
| Rejecting a person | A record the rejection needs fails | blockchain::WF_REJECT_ACTOR_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | BACKEND_ERROR | S0 operation_refusals #3 |
| Rejecting a person | A record the rejection needs fails | blockchain::WF_REJECT_ACTOR_V0 | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | BACKEND_ERROR | S0 operation_refusals #3 |
| Creating a wallet | A record the wallet needs fails | blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_RESOLVE_ACTOR_V0 | BACKEND_ERROR | S0 operation_refusals #4 |
| Creating a wallet | A record the wallet needs fails | blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_CLAIM_WALLET_IDENTITY_V0 | BACKEND_ERROR | S0 operation_refusals #4 |
| Creating a wallet | A record the wallet needs fails | blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_CREATE_WALLET_RECORD_V0 | BACKEND_ERROR | S0 operation_refusals #4 |
| Creating a wallet | A record the wallet needs fails | blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | BACKEND_ERROR | S0 operation_refusals #4 |

<!-- register:refusal_deferrals optional -->
| Operation | Refused When | Deferred To | Until | Source Finding |
|---|---|---|---|---|

<!-- register:refusal_governance_discharge optional -->
| Operation | Refused When | Phase | Governing Rule | Source Finding |
|---|---|---|---|---|

---

## 15. Molecules, Tests and Withdrawals

No molecule or test is touched, and nothing is withdrawn: every amended artifact keeps every fact it has and gains one answer.

<!-- register:molecule_steps optional -->
| CT Code | Step | Kind (atom, molecule, loop) | Target | Over | Iterator | Emits | Source Finding |
|---|---|---|---|---|---|---|---|

<!-- register:molecule_step_bindings optional -->
| CT Code | Step | Role (INPUT, CARRY, UPDATE) | Field | Bound To | Source Finding |
|---|---|---|---|---|---|

<!-- register:test_cases optional -->
| CT Code | Case | Expected Outcome (SUCCESS, VIOLATION) | Source Finding |
|---|---|---|---|

<!-- register:test_case_values optional -->
| CT Code | Case | Role (INPUT, EXPECTED, ASSERT, RECORDED) | Field | Value | Source Finding |
|---|---|---|---|---|---|

<!-- register:withdrawn_facts optional -->
| Artifact | Fact | Reason | Source Finding |
|---|---|---|---|

