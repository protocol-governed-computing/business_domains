# Stage 7 — Design Intent: blockchain / wallet
**Stage:** 7 — Design Intent
**CR:** cr_04_wallet
**Status:** DRAFT
**Feeds:** Stage 8 — Authoring Mandate

HOW it is realised. Binding identities are assigned here.

---

## 1. Design Decisions Resolution

<!-- register:design_resolution optional -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|
| Wallet is a subdomain of its own | A wallet is a thing the business holds in its own right | `wallet` subdomain, owning three stores and writing no store identity owns | S4 design_decisions #1 |
| Working out an address is pure computation | The same key material always yields the same address | `blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0`, a transform; the closed side-effect set is unchanged | S4 design_decisions #2 |
| Key material is supplied, never generated | The same request must produce the same wallet | The transform takes the material as a declared input and derives nothing at random | S4 design_decisions #3 |
| A wallet's identity is derived from its holder | One person holds one wallet | `CT_PURE_GENERATE_ID_V0` over the holder's identity alone | S4 design_decisions #4 |
| The declared moments are announced from where the operations record what they did | The moments already exist and are referred to by nothing | `emit:` on the terminal node of each identity workflow | S4 design_decisions #5 |
| Wallet creation is refused for a person not held, not accepted, or already holding a wallet | The business stated each refusal | Declared outcomes routing to a terminal node, never an unhandled path | S4 design_decisions #6 |
| Acceptance stands on its own | A wallet that cannot be created does not un-accept the person | Wallet creation is a separate workflow; identity's workflows terminate without it | S4 design_decisions #7 |
| The deciding workflow is split rather than amended | A rejection must state grounds, and each outcome must announce | Two workflows replace one, each with its own admission and its own terminal node to announce from | S6 pps_artifacts_requiring_action #1 |

---

## 2. Artifact Inventory — Existing Artifacts

<!-- register:existing_inventory -->
| FQDN | Action (REPLACE, REUSE, EXTEND, REVIEW) | Summary | Reason | Source Finding |
|------|------------------------------------------|---------|--------|----------------|
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | REPLACE | | Superseded by two workflows, one per outcome, each announcing its own moment and the rejection requiring grounds throughout. | S6 pps_artifacts_requiring_action #1 |
| blockchain::WF_REGISTER_ACTOR_V0 | EXTEND | The governed sequence that admits a person as an unverified actor, and announces that it did | Its terminal node announces nothing. Everything else about it is unchanged. | S6 pps_artifacts_requiring_action #3 |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | REUSE | | Records the decision unchanged. The grounds check is a separate contract ahead of it, so this one is not amended. | S6 pps_artifacts_requiring_action #2 |
| blockchain::CC_RESOLVE_ACTOR_V0 | REUSE | | Resolves a person and carries their state; wallet reads it and identity's workflows keep it. | S5 cross_subdomain_refs #1 |
| blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | REUSE | | Records a moment on a person's trail, unchanged. | S3 dependency_discoveries #8 |
| blockchain::IN_ACTOR_REGISTERED_V0 | REUSE | | Admits a registration, unchanged; the registration workflow is redeclared whole and runs it. | S6 pps_artifacts_requiring_action #3 |
| blockchain::CC_VALIDATE_REGISTRATION_V0 | REUSE | | Validates a registration, unchanged. | S6 pps_artifacts_requiring_action #3 |
| blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | REUSE | | Claims a contact address, unchanged. | S6 pps_artifacts_requiring_action #3 |
| blockchain::CC_REGISTER_ACTOR_V0 | REUSE | | Records the person, unchanged. | S6 pps_artifacts_requiring_action #3 |
| blockchain::EV_ACTOR_ACCEPTED_V0 | REUSE | | Declared already; this change refers to it for the first time. | S6 pps_artifacts_requiring_action #4 |
| blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0 | REUSE | | The same. | S6 pps_artifacts_requiring_action #5 |
| blockchain::EV_ACTOR_REJECTED_V0 | REUSE | | The same. | S6 pps_artifacts_requiring_action #6 |
| blockchain::AC_PARTICIPANT_V0 | REUSE | | The authority context both identity workflows already run under. | S6 ownership #10 |
| blockchain::RB_IDENTITY_BINDINGS_V0 | EXTEND | The bindings identity's workflows resolve their capabilities and stores through | Two new workflows must bind through it. | S6 pps_artifacts_requiring_action #1 |
| blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 | EXTEND | Declares what the blockchain domain compiles | It knows of one subdomain and must know of two. | S6 pps_artifacts_requiring_action #8 |
| capability_side_effects::CS_MUTABLE_JSON_V0 | REUSE | | Holds a wallet. | S6 ownership #6 |
| capability_side_effects::CS_APPENDONLY_JSONL_V0 | REUSE | | Holds a wallet's trail. | S6 ownership #7 |
| capability_side_effects::CS_REGISTRY_V0 | REUSE | | Claims a wallet's identity. | S6 ownership #9 |
| capability_side_effects::CS_CLOCK_V0 | REUSE | | Supplies the time a moment occurred. | S6 ownership #11 |
| capability_transforms::CT_PURE_GENERATE_ID_V0 | REUSE | | Derives a wallet's identity from its holder. | S6 ownership #8 |
| capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | REUSE | | Assembles a record from declared fields. | S7 cc_composition #5 |
| capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | REUSE | | Judges a parameter against declared rules. | S7 cc_composition #10 |

---

## 3. Artifact Family Mapping — New Artifacts

<!-- register:new_artifacts optional business_language=capability -->
| Capability | Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE) | Code | Summary | Owner Subdomain | Status | Source Finding |
|------------|------------------------------------------------|------|---------|-----------------|--------|----------------|
| Admitting a request to give an accepted person a wallet | IN | blockchain::IN_WALLET_CREATION_V0 | Admits a request naming the person a wallet is for, and refuses one that names nobody | wallet | NEW | S5 provisional_codes #1 |
| Giving an accepted person a wallet | WF | blockchain::WF_CREATE_WALLET_V0 | The governed sequence that gives an accepted person a wallet and records that it did | wallet | NEW | S5 provisional_codes #2 |
| Determining a wallet's identity | CC | blockchain::CC_DETERMINE_WALLET_IDENTITY_V0 | Derives the wallet's identity from the person who holds it | wallet | NEW | S5 provisional_codes #3 |
| Claiming a wallet's identity | CC | blockchain::CC_CLAIM_WALLET_IDENTITY_V0 | Claims the identity, and refuses when the person already holds a wallet | wallet | NEW | S5 provisional_codes #4 |
| Establishing the address others may pay to | CC | blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0 | Establishes the address from key material supplied with the request | wallet | NEW | S5 provisional_codes #5 |
| Recording the wallet | CC | blockchain::CC_CREATE_WALLET_RECORD_V0 | Records the wallet with a balance of zero, its denomination and its classification | wallet | NEW | S5 provisional_codes #6 |
| Recording that the wallet was created | CC | blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | Records the moment on the wallet's trail | wallet | NEW | S5 provisional_codes #7 |
| Working out an address from supplied key material | CT | blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0 | Derives an address from supplied key material; the same material always yields the same address | wallet | NEW | S5 provisional_codes #8 |
| The moment a person came to hold value | EV | blockchain::EV_WALLET_CREATED_V0 | Announces that a wallet was created, for whom, and when | wallet | NEW | S5 provisional_codes #9 |
| Reaching a wallet's stores | RB | blockchain::RB_WALLET_BINDINGS_V0 | Binds the wallet workflow to the capabilities and stores it uses | wallet | NEW | S5 provisional_codes #10 |
| Declaring where a wallet is held | STRUCTURE | blockchain::STRUCTURE_WALLET_STORAGE_V0 | Declares the three stores wallet owns | wallet | NEW | S5 provisional_codes #11 |
| The classifications a wallet may carry | VOCAB | blockchain::VOCAB_WALLET_CLASSIFICATION_V0 | The fixed set of wallet classifications, of which only the default is used | wallet | NEW | S5 provisional_codes #12 |
| Admitting an acceptance | IN | blockchain::IN_ACTOR_ACCEPTANCE_V0 | Admits a request to accept a person, and refuses one that names nobody | identity | NEW | S5 provisional_codes #13 |
| Admitting a rejection | IN | blockchain::IN_ACTOR_REJECTION_V0 | Admits a request to reject a person, and refuses one that states no grounds | identity | NEW | S5 provisional_codes #14 |
| Recording and announcing an acceptance | WF | blockchain::WF_ACCEPT_ACTOR_V0 | The governed sequence that records an acceptance and announces it | identity | NEW | S5 provisional_codes #15 |
| Recording and announcing a rejection | WF | blockchain::WF_REJECT_ACTOR_V0 | The governed sequence that records a rejection, with grounds required, and announces it | identity | NEW | S5 provisional_codes #16 |
| Refusing a rejection that states no grounds | CC | blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 | Refuses a rejection stating no grounds, before anything is recorded | identity | NEW | S5 provisional_codes #17 |

---

## 4. Runtime Binding (RB) Declarations

<!-- register:rb_declarations -->
| RB Code | Binds WF | CS Bindings | Storage Structure | Source Finding |
|---------|----------|-------------|-------------------|----------------|
| blockchain::RB_WALLET_BINDINGS_V0 | blockchain::WF_CREATE_WALLET_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_CLOCK_V0 | blockchain::STRUCTURE_WALLET_STORAGE_V0 | S5 provisional_codes #10 |
| blockchain::RB_IDENTITY_BINDINGS_V0 | blockchain::WF_ACCEPT_ACTOR_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_CLOCK_V0 | blockchain::STRUCTURE_IDENTITY_STORAGE_V0 | S6 pps_artifacts_requiring_action #1 |
| blockchain::RB_IDENTITY_BINDINGS_V0 | blockchain::WF_REJECT_ACTOR_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_CLOCK_V0 | blockchain::STRUCTURE_IDENTITY_STORAGE_V0 | S6 pps_artifacts_requiring_action #1 |
| blockchain::RB_IDENTITY_BINDINGS_V0 | blockchain::WF_REGISTER_ACTOR_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_CLOCK_V0 | blockchain::STRUCTURE_IDENTITY_STORAGE_V0 | S6 pps_artifacts_requiring_action #3 |

---

## 5. Execution Topology

<!-- register:execution_topology -->
| Workflow | Node | Node Type (IN, CC, EXIT, EXIT_SUCCESS) | Routing | Source Finding |
|----------|------|----------------------------------------|---------|----------------|
| blockchain::WF_CREATE_WALLET_V0 | blockchain::IN_WALLET_CREATION_V0 | IN | ACK -> blockchain::CC_RESOLVE_ACTOR_V0; NACK -> EXIT_REJECTED | S5 actions #1 |
| blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_RESOLVE_ACTOR_V0 | CC | SUCCESS -> blockchain::CC_DETERMINE_WALLET_IDENTITY_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED | S6 cross_subdomain_deps #1 |
| blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_DETERMINE_WALLET_IDENTITY_V0 | CC | SUCCESS -> blockchain::CC_CLAIM_WALLET_IDENTITY_V0; VIOLATION -> EXIT_REJECTED | S5 provisional_codes #3 |
| blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_CLAIM_WALLET_IDENTITY_V0 | CC | SUCCESS -> blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED | S5 provisional_codes #4 |
| blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0 | CC | SUCCESS -> blockchain::CC_CREATE_WALLET_RECORD_V0; VIOLATION -> EXIT_REJECTED | S5 provisional_codes #5 |
| blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_CREATE_WALLET_RECORD_V0 | CC | SUCCESS -> blockchain::CC_APPEND_WALLET_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED | S5 provisional_codes #6 |
| blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | CC | SUCCESS -> EXIT_SUCCESS; VIOLATION -> EXIT_REJECTED | S5 provisional_codes #7 |
| blockchain::WF_CREATE_WALLET_V0 | EXIT_SUCCESS | EXIT | emit blockchain::EV_WALLET_CREATED_V0 | S5 provisional_codes #9 |
| blockchain::WF_CREATE_WALLET_V0 | EXIT_REJECTED | EXIT | — | S5 invariants #4 |
| blockchain::WF_ACCEPT_ACTOR_V0 | blockchain::IN_ACTOR_ACCEPTANCE_V0 | IN | ACK -> blockchain::CC_RESOLVE_ACTOR_V0; NACK -> EXIT_REJECTED | S5 provisional_codes #13 |
| blockchain::WF_ACCEPT_ACTOR_V0 | blockchain::CC_RESOLVE_ACTOR_V0 | CC | SUCCESS -> blockchain::CC_RECORD_VERIFICATION_DECISION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #4 |
| blockchain::WF_ACCEPT_ACTOR_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | CC | SUCCESS -> blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #2 |
| blockchain::WF_ACCEPT_ACTOR_V0 | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | CC | SUCCESS -> EXIT_SUCCESS; VIOLATION -> EXIT_REJECTED | S3 dependency_discoveries #8 |
| blockchain::WF_ACCEPT_ACTOR_V0 | EXIT_SUCCESS | EXIT | emit blockchain::EV_ACTOR_ACCEPTED_V0 | S4 gap_register GAP-4 |
| blockchain::WF_ACCEPT_ACTOR_V0 | EXIT_REJECTED | EXIT | — | S5 invariants #4 |
| blockchain::WF_REJECT_ACTOR_V0 | blockchain::IN_ACTOR_REJECTION_V0 | IN | ACK -> blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0; NACK -> EXIT_REJECTED | S5 provisional_codes #14 |
| blockchain::WF_REJECT_ACTOR_V0 | blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 | CC | SUCCESS -> blockchain::CC_RESOLVE_ACTOR_V0; VIOLATION -> EXIT_REJECTED | S4 gap_register GAP-5 |
| blockchain::WF_REJECT_ACTOR_V0 | blockchain::CC_RESOLVE_ACTOR_V0 | CC | SUCCESS -> blockchain::CC_RECORD_VERIFICATION_DECISION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #4 |
| blockchain::WF_REJECT_ACTOR_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | CC | SUCCESS -> blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #2 |
| blockchain::WF_REJECT_ACTOR_V0 | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | CC | SUCCESS -> EXIT_SUCCESS; VIOLATION -> EXIT_REJECTED | S3 dependency_discoveries #8 |
| blockchain::WF_REJECT_ACTOR_V0 | EXIT_SUCCESS | EXIT | emit blockchain::EV_ACTOR_REJECTED_V0 | S4 gap_register GAP-4 |
| blockchain::WF_REJECT_ACTOR_V0 | EXIT_REJECTED | EXIT | — | S5 invariants #4 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::IN_ACTOR_REGISTERED_V0 | IN | ACK -> blockchain::CC_VALIDATE_REGISTRATION_V0; NACK -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #3 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_VALIDATE_REGISTRATION_V0 | CC | SUCCESS -> blockchain::CC_CLAIM_CONTACT_ADDRESS_V0; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #3 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | CC | SUCCESS -> blockchain::CC_REGISTER_ACTOR_V0; ALREADY_EXISTS -> blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #3 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_REGISTER_ACTOR_V0 | CC | SUCCESS -> blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #3 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | CC | SUCCESS -> EXIT_SUCCESS; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #3 |
| blockchain::WF_REGISTER_ACTOR_V0 | EXIT_SUCCESS | EXIT | emit blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0 | S4 gap_register GAP-4 |
| blockchain::WF_REGISTER_ACTOR_V0 | EXIT_REJECTED | EXIT | — | S6 pps_artifacts_requiring_action #3 |

---

---

## 6. Capability Composition

<!-- register:cc_composition optional -->
| CC Code | Step | Step Name | Capability | Kind (CT, CS) | Operation | Store | Consumes | Produces | Routing | Interpreted By | Semantic Status | Interface |
|---------|------|-----------|------------|---------------|-----------|-------|----------|----------|---------|----------------|-----------------|-----------|
| blockchain::CC_DETERMINE_WALLET_IDENTITY_V0 | 1 | derive_wallet_identity | capability_transforms::CT_PURE_GENERATE_ID_V0 | CT | GENERATE_ID | — | data, prefix | id | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: data=data, prefix=prefix; out: id=id |
| blockchain::CC_CLAIM_WALLET_IDENTITY_V0 | 1 | claim_wallet_identity | capability_side_effects::CS_REGISTRY_V0 | CS | REGISTER | WALLET_IDENTITIES | key | result_status | SUCCESS -> continue; ALREADY_EXISTS -> exit; VIOLATION -> exit | — | SUCCESS | in: key=key; out: result_status=result_status |
| blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0 | 1 | derive_wallet_address | blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0 | CT | DERIVE_WALLET_ADDRESS | — | key_material | address | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: key_material=key_material; out: address=address |
| blockchain::CC_CREATE_WALLET_RECORD_V0 | 1 | read_created_at | capability_side_effects::CS_CLOCK_V0 | CS | READ | — | | now | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | out: now=now |
| blockchain::CC_CREATE_WALLET_RECORD_V0 | 2 | assemble_wallet | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | CT | ASSEMBLE_RECORD | — | fields | record | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: fields=fields; out: record=record |
| blockchain::CC_CREATE_WALLET_RECORD_V0 | 3 | write_wallet | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | WRITE | WALLETS | key, value | result_status | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: key=key, value=value; out: result_status=result_status |
| blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | 1 | read_occurred_at | capability_side_effects::CS_CLOCK_V0 | CS | READ | — | | now | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | out: now=now |
| blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | 2 | assemble_occurrence | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | CT | ASSEMBLE_RECORD | — | fields | record | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: fields=fields; out: record=record |
| blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | 3 | append_occurrence | capability_side_effects::CS_APPENDONLY_JSONL_V0 | CS | APPEND | WALLET_OCCURRENCES | stream_id, record | result_status | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: stream_id=stream_id, record=record; out: result_status=result_status |
| blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 | 1 | require_grounds_stated | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | CT | VALIDATE_PARAMETER_RULES | — | parameters, rules | valid | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: parameters=parameters, rules=rules; out: valid=valid |

---

## 7. Step Bindings

<!-- register:step_bindings optional -->
| Owner | Step | Direction (INPUT, OUTPUT) | Field | Bound To | Source Finding |
|-------|------|---------------------------|-------|----------|----------------|
| blockchain::CC_DETERMINE_WALLET_IDENTITY_V0 | derive_wallet_identity | INPUT | data | inputs.holder | S7 cc_composition derive_wallet_identity |
| blockchain::CC_DETERMINE_WALLET_IDENTITY_V0 | derive_wallet_identity | INPUT | prefix | inputs.wallet_id_prefix | S7 cc_composition derive_wallet_identity |
| blockchain::CC_DETERMINE_WALLET_IDENTITY_V0 | derive_wallet_identity | OUTPUT | id | capability_result.id | S7 cc_composition derive_wallet_identity |
| blockchain::CC_CLAIM_WALLET_IDENTITY_V0 | claim_wallet_identity | INPUT | key | inputs.wallet_id | S7 cc_composition claim_wallet_identity |
| blockchain::CC_CLAIM_WALLET_IDENTITY_V0 | claim_wallet_identity | OUTPUT | result_status | capability_result.result_status | S7 cc_composition claim_wallet_identity |
| blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0 | derive_wallet_address | INPUT | key_material | inputs.key_material | S7 cc_composition derive_wallet_address |
| blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0 | derive_wallet_address | OUTPUT | address | capability_result.address | S7 cc_composition derive_wallet_address |
| blockchain::CC_CREATE_WALLET_RECORD_V0 | read_created_at | OUTPUT | now | capability_result.now | S7 cc_composition read_created_at |
| blockchain::CC_CREATE_WALLET_RECORD_V0 | assemble_wallet | INPUT | fields | inputs.wallet_fields | S7 cc_composition assemble_wallet |
| blockchain::CC_CREATE_WALLET_RECORD_V0 | assemble_wallet | OUTPUT | record | capability_result.record | S7 cc_composition assemble_wallet |
| blockchain::CC_CREATE_WALLET_RECORD_V0 | write_wallet | INPUT | key | inputs.wallet_id | S7 cc_composition write_wallet |
| blockchain::CC_CREATE_WALLET_RECORD_V0 | write_wallet | INPUT | value | results.assemble_wallet.record | S7 cc_composition write_wallet |
| blockchain::CC_CREATE_WALLET_RECORD_V0 | write_wallet | OUTPUT | result_status | capability_result.result_status | S7 cc_composition write_wallet |
| blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | read_occurred_at | OUTPUT | now | capability_result.now | S7 cc_composition read_occurred_at |
| blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | assemble_occurrence | INPUT | fields | inputs.occurrence_fields | S7 cc_composition assemble_occurrence |
| blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | assemble_occurrence | OUTPUT | record | capability_result.record | S7 cc_composition assemble_occurrence |
| blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | append_occurrence | INPUT | stream_id | inputs.stream_id | S7 cc_composition append_occurrence |
| blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | append_occurrence | INPUT | record | results.assemble_occurrence.record | S7 cc_composition append_occurrence |
| blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | append_occurrence | OUTPUT | result_status | capability_result.result_status | S7 cc_composition append_occurrence |
| blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 | require_grounds_stated | INPUT | parameters | inputs.grounds | S7 cc_composition require_grounds_stated |
| blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 | require_grounds_stated | INPUT | rules | inputs.grounds_rules | S7 cc_composition require_grounds_stated |
| blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 | require_grounds_stated | OUTPUT | valid | capability_result.valid | S7 cc_composition require_grounds_stated |
| blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_DETERMINE_WALLET_IDENTITY_V0 | INPUT | holder | results.CC_RESOLVE_ACTOR_V0.value.contact_address | S7 execution_topology blockchain::CC_DETERMINE_WALLET_IDENTITY_V0 |
| blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_DETERMINE_WALLET_IDENTITY_V0 | INPUT | wallet_id_prefix | payload.wallet_id_prefix | S7 execution_topology blockchain::CC_DETERMINE_WALLET_IDENTITY_V0 |
| blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_CLAIM_WALLET_IDENTITY_V0 | INPUT | wallet_id | results.CC_DETERMINE_WALLET_IDENTITY_V0.id | S7 execution_topology blockchain::CC_CLAIM_WALLET_IDENTITY_V0 |
| blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0 | INPUT | key_material | payload.key_material | S7 execution_topology blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0 |
| blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_CREATE_WALLET_RECORD_V0 | INPUT | wallet_id | results.CC_DETERMINE_WALLET_IDENTITY_V0.id | S7 execution_topology blockchain::CC_CREATE_WALLET_RECORD_V0 |
| blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_CREATE_WALLET_RECORD_V0 | INPUT | wallet_fields | payload.wallet_fields | S7 execution_topology blockchain::CC_CREATE_WALLET_RECORD_V0 |
| blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | INPUT | stream_id | results.CC_DETERMINE_WALLET_IDENTITY_V0.id | S7 execution_topology blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 |
| blockchain::WF_CREATE_WALLET_V0 | blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | INPUT | occurrence_fields | payload.occurrence_fields | S7 execution_topology blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 |
| blockchain::WF_REJECT_ACTOR_V0 | blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 | INPUT | grounds | payload.grounds | S7 execution_topology blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 |
| blockchain::WF_REJECT_ACTOR_V0 | blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 | INPUT | grounds_rules | payload.grounds_rules | S7 execution_topology blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_VALIDATE_REGISTRATION_V0 | INPUT | actor_record | payload.actor_record | S7 existing_inventory WF_REGISTER_ACTOR_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_VALIDATE_REGISTRATION_V0 | INPUT | registration_schema | payload.registration_schema | S7 existing_inventory WF_REGISTER_ACTOR_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | INPUT | actor_record | payload.actor_record | S7 existing_inventory WF_REGISTER_ACTOR_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | INPUT | address_path | payload.address_path | S7 existing_inventory WF_REGISTER_ACTOR_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | INPUT | address_type | payload.address_type | S7 existing_inventory WF_REGISTER_ACTOR_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_REGISTER_ACTOR_V0 | INPUT | actor_fields | payload.actor_record | S7 existing_inventory WF_REGISTER_ACTOR_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_REGISTER_ACTOR_V0 | INPUT | contact_address | results.CC_CLAIM_CONTACT_ADDRESS_V0.result | S7 existing_inventory WF_REGISTER_ACTOR_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | INPUT | occurrence_fields | payload.occurrence_fields | S7 existing_inventory WF_REGISTER_ACTOR_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | INPUT | stream_id | payload.stream_id | S7 existing_inventory WF_REGISTER_ACTOR_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | INPUT | contact_address | results.CC_CLAIM_CONTACT_ADDRESS_V0.result | S7 existing_inventory WF_REGISTER_ACTOR_V0 |

---

## 8. Interface Fields

<!-- register:interface_fields optional -->
| Artifact | Direction (INPUT, OUTPUT, ATTRIBUTE) | Field | Type | Required (YES, NO) | Default | Meaning |
|----------|--------------------------------------|-------|------|--------------------|---------|---------|
| blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0 | INPUT | key_material | string | YES | | The public key material supplied with the request. Never generated here. |
| blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0 | OUTPUT | address | string | YES | | The address others may pay to. The same material always yields the same address. |
| blockchain::IN_WALLET_CREATION_V0 | INPUT | contact_address | string | YES | | The person the wallet is for. |
| blockchain::IN_WALLET_CREATION_V0 | INPUT | key_material | string | YES | | The key material the address is worked out from. |
| blockchain::IN_WALLET_CREATION_V0 | INPUT | wallet_id_prefix | string | YES | | The prefix a wallet identity carries, so the identity is recognisable as a wallet. |
| blockchain::IN_ACTOR_ACCEPTANCE_V0 | INPUT | contact_address | string | YES | | The person being accepted. |
| blockchain::IN_ACTOR_ACCEPTANCE_V0 | INPUT | verifying_authority | string | YES | | The authority recording the acceptance. |
| blockchain::IN_ACTOR_REJECTION_V0 | INPUT | contact_address | string | YES | | The person being rejected. |
| blockchain::IN_ACTOR_REJECTION_V0 | INPUT | verifying_authority | string | YES | | The authority recording the rejection. |
| blockchain::IN_ACTOR_REJECTION_V0 | INPUT | grounds | string | YES | | Why the person is refused. A rejection stating none is refused. |
| blockchain::EV_WALLET_CREATED_V0 | ATTRIBUTE | wallet_id | string | YES | | The wallet created. |
| blockchain::EV_WALLET_CREATED_V0 | ATTRIBUTE | holder | string | YES | | The person it belongs to. |
| blockchain::EV_WALLET_CREATED_V0 | ATTRIBUTE | occurred_at | string | YES | | When it was created. |
| blockchain::CC_DETERMINE_WALLET_IDENTITY_V0 | INPUT | holder | string | YES |  | The person the wallet belongs to. |
| blockchain::CC_DETERMINE_WALLET_IDENTITY_V0 | INPUT | wallet_id_prefix | string | YES |  | The prefix a wallet identity carries. |
| blockchain::CC_DETERMINE_WALLET_IDENTITY_V0 | OUTPUT | id | string | YES |  | The identity derived for the wallet. |
| blockchain::CC_CLAIM_WALLET_IDENTITY_V0 | INPUT | wallet_id | string | YES |  | The identity being claimed. |
| blockchain::CC_CLAIM_WALLET_IDENTITY_V0 | OUTPUT | result_status | string | YES |  | Whether the claim succeeded, or the identity was already held. |
| blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0 | INPUT | key_material | string | YES |  | The key material supplied with the request. |
| blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0 | OUTPUT | address | string | YES |  | The address others may pay to. |
| blockchain::CC_CREATE_WALLET_RECORD_V0 | INPUT | wallet_id | string | YES |  | The wallet being recorded. |
| blockchain::CC_CREATE_WALLET_RECORD_V0 | INPUT | wallet_fields | object | YES |  | What the business holds about the wallet. |
| blockchain::CC_CREATE_WALLET_RECORD_V0 | OUTPUT | result_status | string | YES |  | Whether the wallet was recorded. |
| blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | INPUT | stream_id | string | YES |  | The trail the moment is added to. |
| blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | INPUT | occurrence_fields | object | YES |  | What the moment records. |
| blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | OUTPUT | result_status | string | YES |  | Whether the moment was recorded. |
| blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 | INPUT | grounds | string | YES |  | Why the person is refused. |
| blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 | INPUT | grounds_rules | object | YES |  | The rule the grounds must satisfy. |
| blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 | OUTPUT | valid | boolean | YES |  | Whether grounds were stated. |

---

## 9. Implementation Bindings

<!-- register:implementation_bindings optional -->
| CT Code | Module | Callable | Operation | Kind (atom, molecule) | Purity (ct_pure, ct_impure) | Source Finding |
|---------|--------|----------|-----------|------------------------|------------------------------|----------------|
| blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0 | blockchain.implementation.capability_transforms.derive_wallet_address | derive_wallet_address_v0 | DERIVE_WALLET_ADDRESS | atom | ct_pure | S4 design_decisions #3 |

---

## 10. Vocabulary Extensions

<!-- register:vocabulary_extensions optional -->
| Vocabulary Code | Extends | Value | Meaning | Source Finding |
|-----------------|---------|-------|---------|----------------|
| blockchain::VOCAB_WALLET_CLASSIFICATION_V0 | | DEFAULT | The only classification this change creates. | S5 known_facts #15 |
| blockchain::VOCAB_WALLET_CLASSIFICATION_V0 | | PRIVATE | Named and unused until a business need arises. | S5 known_facts #15 |
| blockchain::VOCAB_WALLET_CLASSIFICATION_V0 | | BUSINESS | Named and unused. | S5 known_facts #15 |
| blockchain::VOCAB_WALLET_CLASSIFICATION_V0 | | SAVINGS | Named and unused. | S5 known_facts #15 |
| blockchain::VOCAB_WALLET_CLASSIFICATION_V0 | | INVESTMENT | Named and unused. | S5 known_facts #15 |
| blockchain::VOCAB_WALLET_CLASSIFICATION_V0 | | MINT | Named and unused. | S5 known_facts #15 |
| blockchain::VOCAB_WALLET_CLASSIFICATION_V0 | | BURN | Named and unused. | S5 known_facts #15 |
| blockchain::VOCAB_WALLET_CLASSIFICATION_V0 | | POOL | Named and unused. | S5 known_facts #15 |

---

## 11. Runtime Policies

<!-- register:runtime_policies optional -->
| RB Code | Capability | Key | Value | Source Finding |
|---------|------------|-----|-------|----------------|
| blockchain::RB_WALLET_BINDINGS_V0 | capability_side_effects::CS_MUTABLE_JSON_V0 | store | WALLETS | S7 structure_stores #1 |
| blockchain::RB_WALLET_BINDINGS_V0 | capability_side_effects::CS_APPENDONLY_JSONL_V0 | store | WALLET_OCCURRENCES | S7 structure_stores #2 |
| blockchain::RB_WALLET_BINDINGS_V0 | capability_side_effects::CS_REGISTRY_V0 | store | WALLET_IDENTITIES | S7 structure_stores #3 |
| blockchain::RB_WALLET_BINDINGS_V0 | capability_side_effects::CS_CLOCK_V0 | policy | utc | S7 rb_declarations #1 |
| blockchain::RB_IDENTITY_BINDINGS_V0 | capability_side_effects::CS_MUTABLE_JSON_V0 | structure | blockchain::STRUCTURE_IDENTITY_STORAGE_V0 | S7 existing_inventory RB_IDENTITY_BINDINGS_V0 |
| blockchain::RB_IDENTITY_BINDINGS_V0 | capability_side_effects::CS_REGISTRY_V0 | structure | blockchain::STRUCTURE_IDENTITY_STORAGE_V0 | S7 existing_inventory RB_IDENTITY_BINDINGS_V0 |
| blockchain::RB_IDENTITY_BINDINGS_V0 | capability_side_effects::CS_APPENDONLY_JSONL_V0 | structure | blockchain::STRUCTURE_IDENTITY_STORAGE_V0 | S7 existing_inventory RB_IDENTITY_BINDINGS_V0 |
| blockchain::RB_IDENTITY_BINDINGS_V0 | capability_side_effects::CS_CLOCK_V0 | precision | seconds | S7 existing_inventory RB_IDENTITY_BINDINGS_V0 |

---

## 12. Artifact Properties

<!-- register:artifact_properties optional -->
| Artifact | Property | Value | Source Finding |
|----------|----------|-------|----------------|
| blockchain::WF_CREATE_WALLET_V0 | emit.EXIT_SUCCESS | blockchain::EV_WALLET_CREATED_V0 | S7 execution_topology #8 |
| blockchain::WF_ACCEPT_ACTOR_V0 | emit.EXIT_SUCCESS | blockchain::EV_ACTOR_ACCEPTED_V0 | S4 gap_register GAP-4 |
| blockchain::WF_REJECT_ACTOR_V0 | emit.EXIT_SUCCESS | blockchain::EV_ACTOR_REJECTED_V0 | S4 gap_register GAP-4 |
| blockchain::WF_REGISTER_ACTOR_V0 | emit.EXIT_SUCCESS | blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0 | S4 gap_register GAP-4 |
| blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 | core.subdomain | wallet | S6 pps_artifacts_requiring_action #8 |
| blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 | artifact_discovery.search_layers[0] | BLOCKCHAIN | S7 existing_inventory STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 |
| blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 | artifact_discovery.import_surface.domain | platform | S7 existing_inventory STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 |
| blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 | artifact_discovery.artifact_types[0] | AC | S7 existing_inventory STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 |
| blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 | artifact_discovery.artifact_types[1] | IN | S7 existing_inventory STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 |
| blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 | artifact_discovery.artifact_types[2] | WF | S7 existing_inventory STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 |
| blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 | artifact_discovery.artifact_types[3] | CC | S7 existing_inventory STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 |
| blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 | artifact_discovery.artifact_types[4] | CT | S7 existing_inventory STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 |
| blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 | artifact_discovery.artifact_types[5] | RB | S7 existing_inventory STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 |
| blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 | artifact_discovery.artifact_types[6] | EV | S7 existing_inventory STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 |
| blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 | artifact_discovery.artifact_types[7] | VOCAB | S7 existing_inventory STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 |
| blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 | artifact_discovery.artifact_types[8] | STRUCTURE | S7 existing_inventory STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 |
| blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 | artifact_discovery.artifact_types[9] | TI | S7 existing_inventory STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 |
| blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 | artifact_discovery.artifact_types[10] | TE | S7 existing_inventory STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 |

---

## 14. Transport Bindings

<!-- register:transport_bindings optional -->
| Artifact | Direction (INGRESS, EGRESS) | Operation | Handler Kind (WF_INVOCATION, SNAPSHOT_READ) | Handler Target | Field | Bound To | Source Finding |
|----------|------------------------------|-----------|----------------------------------------------|----------------|-------|----------|----------------|
| NONE IDENTIFIED |

## 13. STRUCTURE Stores

<!-- register:structure_stores optional -->
| Store Name | Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0) | Proposed Path | Used By | Source Finding |
|------------|------|------|------|----------------|
| WALLETS | CS_MUTABLE_JSON_V0 | blockchain/wallet/wallets.json | blockchain::CC_CREATE_WALLET_RECORD_V0 | S5 business_objects #1 |
| WALLET_OCCURRENCES | CS_APPENDONLY_JSONL_V0 | blockchain/wallet/wallet_occurrences.jsonl | blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | S5 business_objects #2 |
| WALLET_IDENTITIES | CS_REGISTRY_V0 | blockchain/wallet/wallet_identity_registry.jsonl | blockchain::CC_CLAIM_WALLET_IDENTITY_V0 | S5 business_objects #3 |

---

## 15. Artifact Summary

<!-- register:artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Subdomain | Count | Artifacts |
|-------------------------------|-----------|-------|-----------|
| NEW | wallet | 12 | blockchain::IN_WALLET_CREATION_V0, blockchain::WF_CREATE_WALLET_V0, blockchain::CC_DETERMINE_WALLET_IDENTITY_V0, blockchain::CC_CLAIM_WALLET_IDENTITY_V0, blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0, blockchain::CC_CREATE_WALLET_RECORD_V0, blockchain::CC_APPEND_WALLET_OCCURRENCE_V0, blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0, blockchain::EV_WALLET_CREATED_V0, blockchain::RB_WALLET_BINDINGS_V0, blockchain::STRUCTURE_WALLET_STORAGE_V0, blockchain::VOCAB_WALLET_CLASSIFICATION_V0 |
| NEW | identity | 5 | blockchain::IN_ACTOR_ACCEPTANCE_V0, blockchain::IN_ACTOR_REJECTION_V0, blockchain::WF_ACCEPT_ACTOR_V0, blockchain::WF_REJECT_ACTOR_V0, blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 |
| EXTEND | identity | 3 | blockchain::WF_REGISTER_ACTOR_V0, blockchain::RB_IDENTITY_BINDINGS_V0, blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 |
| REPLACE | identity | 1 | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 |

---

## 16. Generation Provenance

*Every artifact this design schedules is authored, including the three it amends: construction
renders each from the registers above and it is its own source of truth. Nothing here is reached
by invoking a generator.*

<!-- register:generation_provenance optional -->
| Artifact | Generator | Generator Sources | Source Finding |
|----------|-----------|-------------------|----------------|
| NONE IDENTIFIED |
