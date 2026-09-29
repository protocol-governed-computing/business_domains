# Stage 7 — Design Intent: blockchain / identity

**Stage:** 7 — Design Intent
**CR:** cr_05_identity
**Status:** DRAFT
**Feeds:** Stage 8 — Authoring Mandate

Every binding names a field the capability declares, read from the pinned baseline
`4d366ccab335cfbd9f94d49ec80b2c43cdcb5a0dd417e56e1895b076fbc10e02`.

Nothing new is authored. Ten artifacts identity already holds are redeclared whole: three contracts
take their rules as fixed values, three acts stop passing rules along and fix what they write, three
entrances stop supplying what identity now holds, and the acceptance gate declares the grounds an
acceptance may carry.

---

## 1. Design Decisions Resolution

<!-- register:design_resolution optional -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|
| Each rule is held by the step that applies it | A rule the caller supplies is a rule the caller can widen | The registration schema, the states admitting a decision, the admitted outcomes and the grounds rules are literal inputs of the step that applies each; the contracts no longer declare them as inputs | S4 design_decisions #1 |
| The registration check is followed by a rule refusing when it found anything | An incomplete registration is refused | `CC_VALIDATE_REGISTRATION_V0` gains `refuse_incomplete_registration`, a rule step over the check's violations requiring none | S4 design_decisions #2 |
| The self-decision rule is a comparison followed by a fixed rule | No authority decides about themselves | `compare_authority_to_person` compares the authority with the person; `refuse_self_decision` requires the comparison to be false | S4 design_decisions #3 |
| The decided record is built from the decision the step checked | The state recorded is the decision admitted | The decided record is assembled inside the contract from the checked decision, the authority and the grounds; no request hands it a record | S4 design_decisions #4 |
| Each act fixes its decision | An acceptance act accepts and a rejection act rejects | The acceptance act hands the contract ACCEPTED and the rejection act REJECTED, as literals | S4 design_decisions #4 |
| Registration writes the state unverified as its own | The lifecycle has one way in | The registration act builds the record it registers with the state UNVERIFIED as a literal | S4 design_decisions #5 |
| The entrances stop supplying what identity holds | Nothing a caller sends or is told changes | The three entrances drop the schema, the sets, the rules, the decision and the decided record from their payloads; their input contracts are unchanged | S4 design_decisions #6 |
| Records made before this change are left as they are | The record is added to and never rewritten | No migration, backfill or repair step is designed | S4 design_decisions #7 |

---

## 2. Artifact Inventory — Existing Artifacts

<!-- register:existing_inventory -->
| FQDN | Action (REPLACE, REUSE, EXTEND, REVIEW) | Summary | Reason | Source Finding |
|------|------------------------------------------|---------|--------|----------------|
| blockchain::CC_VALIDATE_REGISTRATION_V0 | EXTEND | Refuses a registration lacking the person's name or their address | It takes its schema from the request and refuses nothing it finds. | S6 pps_artifacts_requiring_action #1 |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | EXTEND | Refuses a decision about a person not unverified, a decision other than an acceptance or a rejection, or an authority deciding about themselves, and records the decision it checked | It takes its sets and its self-decision rule from the request, and records a state the request supplies. | S6 pps_artifacts_requiring_action #2 |
| blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 | EXTEND | Refuses a rejection stating no grounds, before anything is recorded | It takes its rules from the request. | S6 pps_artifacts_requiring_action #3 |
| blockchain::WF_REGISTER_ACTOR_V0 | EXTEND | The governed sequence that admits a person as an unverified actor, and announces that it did | It binds the schema from the request and writes the state it is handed. | S6 pps_artifacts_requiring_action #4 |
| blockchain::WF_ACCEPT_ACTOR_V0 | EXTEND | The governed sequence that records an acceptance and announces it | It binds the rules and the decision from the request. | S6 pps_artifacts_requiring_action #5 |
| blockchain::WF_REJECT_ACTOR_V0 | EXTEND | The governed sequence that records a rejection, with grounds required, and announces it | It binds the rules and the decision from the request. | S6 pps_artifacts_requiring_action #6 |
| blockchain::TI_REGISTER_ACTOR_V0 | EXTEND | Admits a request to register an actor, declaring the name and contact address a caller sends and holding the address path, stream, preferences and occurrence label the act requires | It supplies the schema and the state identity now holds. | S6 pps_artifacts_requiring_action #7 |
| blockchain::TI_ACCEPT_ACTOR_V0 | EXTEND | Admits a request to accept a registered actor, declaring the contact address, authority and optional grounds a caller sends and holding the stream and the acceptance occurrence label | It supplies the rules and the decided record identity now holds. | S6 pps_artifacts_requiring_action #8 |
| blockchain::TI_REJECT_ACTOR_V0 | EXTEND | Admits a request to reject a registered actor, declaring the contact address, authority and required grounds a caller sends and holding the stream and the rejection occurrence label | It supplies the rules and the decided record identity now holds. | S6 pps_artifacts_requiring_action #9 |
| blockchain::IN_ACTOR_ACCEPTANCE_V0 | EXTEND | Admits a request to accept a person, with the grounds the authority chooses to state, and refuses one that names nobody | It does not declare the grounds an acceptance may carry. | S6 pps_artifacts_requiring_action #10 |
| blockchain::CC_RESOLVE_ACTOR_V0 | REUSE | | Resolves a person and carries their state, unchanged. | S6 pps_artifacts_requiring_action #11 |
| blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | REUSE | | Claims a contact address, unchanged. | S6 pps_artifacts_requiring_action #12 |
| blockchain::CC_REGISTER_ACTOR_V0 | REUSE | | Records the person it is handed, unchanged; the act now hands it the state. | S6 pps_artifacts_requiring_action #13 |
| blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | REUSE | | Records a moment on a person's trail, unchanged. | S6 pps_artifacts_requiring_action #14 |
| blockchain::IN_ACTOR_REGISTERED_V0 | REUSE | | Admits a registration, unchanged. | S6 pps_artifacts_requiring_action #4 |
| blockchain::IN_ACTOR_REJECTION_V0 | REUSE | | Admits a rejection and its grounds, unchanged. | S6 pps_artifacts_requiring_action #6 |
| blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0 | REUSE | | Announced by the registration act, unchanged. | S6 pps_artifacts_requiring_action #4 |
| blockchain::EV_ACTOR_ACCEPTED_V0 | REUSE | | Announced by the acceptance act, unchanged. | S6 pps_artifacts_requiring_action #5 |
| blockchain::EV_ACTOR_REJECTED_V0 | REUSE | | Announced by the rejection act, unchanged. | S6 pps_artifacts_requiring_action #6 |
| blockchain::AC_PARTICIPANT_V0 | REUSE | | The authority context the three acts run under, unchanged. | S6 pps_artifacts_requiring_action #4 |
| blockchain::RB_IDENTITY_BINDINGS_V0 | REUSE | | The bindings the three acts resolve their capabilities and stores through, unchanged. | S6 pps_artifacts_requiring_action #4 |
| capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | REUSE | | Reports what a registration lacks. | S6 cross_subdomain_deps #1 |
| capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | REUSE | | Refuses on a fixed list of rules. | S6 cross_subdomain_deps #2 |
| capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 | REUSE | | Refuses a value outside a fixed set. | S6 cross_subdomain_deps #3 |
| capability_transforms::CT_PURE_COMPARE_EQUAL_V0 | REUSE | | Compares the authority with the person decided about. | S6 cross_subdomain_deps #4 |
| capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | REUSE | | Assembles the decided record from the checked decision. | S6 cross_subdomain_deps #5 |
| capability_side_effects::CS_MUTABLE_JSON_V0 | REUSE | | Holds the actor record the decision updates. | S6 storage_governance #1 |

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
| blockchain::RB_IDENTITY_BINDINGS_V0 | blockchain::WF_REGISTER_ACTOR_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_CLOCK_V0 | blockchain::STRUCTURE_IDENTITY_STORAGE_V0 | S6 pps_artifacts_requiring_action #4 |
| blockchain::RB_IDENTITY_BINDINGS_V0 | blockchain::WF_ACCEPT_ACTOR_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_CLOCK_V0 | blockchain::STRUCTURE_IDENTITY_STORAGE_V0 | S6 pps_artifacts_requiring_action #5 |
| blockchain::RB_IDENTITY_BINDINGS_V0 | blockchain::WF_REJECT_ACTOR_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_CLOCK_V0 | blockchain::STRUCTURE_IDENTITY_STORAGE_V0 | S6 pps_artifacts_requiring_action #6 |

---

## 5. Execution Topology

The routing of the three acts is unchanged. What changes is what each node is handed, in §7.

<!-- register:execution_topology optional_columns=runs -->
| Workflow | Node | Runs | Node Type (IN, CC, EXIT, EXIT_SUCCESS) | Routing | Source Finding |
|----------|------|------|----------------------------------------|---------|----------------|
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::IN_ACTOR_REGISTERED_V0 |  | IN | ACK -> blockchain::CC_VALIDATE_REGISTRATION_V0; NACK -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #4 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_VALIDATE_REGISTRATION_V0 |  | CC | SUCCESS -> blockchain::CC_CLAIM_CONTACT_ADDRESS_V0; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #1 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 |  | CC | SUCCESS -> blockchain::CC_REGISTER_ACTOR_V0; ALREADY_EXISTS -> blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #12 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_REGISTER_ACTOR_V0 |  | CC | SUCCESS -> blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #13 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 |  | CC | SUCCESS -> EXIT_SUCCESS; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #14 |
| blockchain::WF_REGISTER_ACTOR_V0 | EXIT_SUCCESS |  | EXIT_SUCCESS | emit blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0 | S6 pps_artifacts_requiring_action #4 |
| blockchain::WF_REGISTER_ACTOR_V0 | EXIT_REJECTED |  | EXIT | — | S5 invariants #7 |
| blockchain::WF_ACCEPT_ACTOR_V0 | blockchain::IN_ACTOR_ACCEPTANCE_V0 |  | IN | ACK -> blockchain::CC_RESOLVE_ACTOR_V0; NACK -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #10 |
| blockchain::WF_ACCEPT_ACTOR_V0 | blockchain::CC_RESOLVE_ACTOR_V0 |  | CC | SUCCESS -> blockchain::CC_RECORD_VERIFICATION_DECISION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #11 |
| blockchain::WF_ACCEPT_ACTOR_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 |  | CC | SUCCESS -> blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #2 |
| blockchain::WF_ACCEPT_ACTOR_V0 | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 |  | CC | SUCCESS -> EXIT_SUCCESS; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #14 |
| blockchain::WF_ACCEPT_ACTOR_V0 | EXIT_SUCCESS |  | EXIT_SUCCESS | emit blockchain::EV_ACTOR_ACCEPTED_V0 | S6 pps_artifacts_requiring_action #5 |
| blockchain::WF_ACCEPT_ACTOR_V0 | EXIT_REJECTED |  | EXIT | — | S5 invariants #7 |
| blockchain::WF_REJECT_ACTOR_V0 | blockchain::IN_ACTOR_REJECTION_V0 |  | IN | ACK -> blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0; NACK -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #6 |
| blockchain::WF_REJECT_ACTOR_V0 | blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 |  | CC | SUCCESS -> blockchain::CC_RESOLVE_ACTOR_V0; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #3 |
| blockchain::WF_REJECT_ACTOR_V0 | blockchain::CC_RESOLVE_ACTOR_V0 |  | CC | SUCCESS -> blockchain::CC_RECORD_VERIFICATION_DECISION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #11 |
| blockchain::WF_REJECT_ACTOR_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 |  | CC | SUCCESS -> blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #2 |
| blockchain::WF_REJECT_ACTOR_V0 | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 |  | CC | SUCCESS -> EXIT_SUCCESS; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action #14 |
| blockchain::WF_REJECT_ACTOR_V0 | EXIT_SUCCESS |  | EXIT_SUCCESS | emit blockchain::EV_ACTOR_REJECTED_V0 | S6 pps_artifacts_requiring_action #6 |
| blockchain::WF_REJECT_ACTOR_V0 | EXIT_REJECTED |  | EXIT | — | S5 invariants #7 |

---

## 6. Capability Composition

<!-- register:cc_composition optional -->
| CC Code | Step | Step Name | Capability | Kind (CT, CS) | Operation | Store | Consumes | Produces | Routing | Interpreted By | Semantic Status | Interface |
|---------|------|-----------|------------|---------------|-----------|-------|----------|----------|---------|----------------|-----------------|-----------|
| blockchain::CC_VALIDATE_REGISTRATION_V0 | 1 | read_registration | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | CT | VALIDATE_RECORD_STRUCTURE | — | actor_record | violations | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: record=actor_record, schema=registration_schema; out: violations=violations |
| blockchain::CC_VALIDATE_REGISTRATION_V0 | 2 | refuse_incomplete_registration | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | CT | VALIDATE_PARAMETER_RULES | — | violations | valid | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: parameters=registration_findings, rules=completeness_rules; out: valid=valid |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | 1 | read_state_admits_decision | capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 | CT | VALIDATE_SET_MEMBERSHIP | — | current_state | is_member | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: value=current_state, allowed_set=states_admitting_a_decision; out: is_member=is_member |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | 2 | read_outcome_admitted | capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 | CT | VALIDATE_SET_MEMBERSHIP | — | decision | is_member | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: value=decision, allowed_set=admitted_outcomes; out: is_member=is_member |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | 3 | compare_authority_to_person | capability_transforms::CT_PURE_COMPARE_EQUAL_V0 | CT | COMPARE_EQUAL | — | verifying_authority, contact_address | is_self | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: left=verifying_authority, right=contact_address; out: is_equal=is_self |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | 4 | refuse_self_decision | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | CT | VALIDATE_PARAMETER_RULES | — | is_self | valid | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: parameters=self_findings, rules=self_rules; out: valid=valid |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | 5 | assemble_decided_actor | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | CT | ASSEMBLE_RECORD | — | contact_address, decision, verifying_authority, grounds | record | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: fields=decided_fields; out: record=record |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | 6 | write_decided_actor | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | UPDATE | ACTORS | key, updates | result_status | SUCCESS -> continue; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | in: key=contact_address, updates=record; out: result_status=result_status |
| blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 | 1 | require_grounds_stated | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | CT | VALIDATE_PARAMETER_RULES | — | grounds | valid | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: parameters=grounds_findings, rules=grounds_rules; out: valid=valid |

---

## 7. Step Bindings

<!-- register:step_bindings optional -->
| Owner | Step | Direction (INPUT, OUTPUT) | Field | Bound To | Source Finding |
|-------|------|---------------------------|-------|----------|----------------|
| blockchain::CC_VALIDATE_REGISTRATION_V0 | read_registration | INPUT | record | inputs.actor_record | S7 cc_composition read_registration |
| blockchain::CC_VALIDATE_REGISTRATION_V0 | read_registration | INPUT | schema | {'name': {'type': 'string', 'required': True}, 'contact_address': {'type': 'string', 'required': True}} | S7 cc_composition read_registration |
| blockchain::CC_VALIDATE_REGISTRATION_V0 | read_registration | OUTPUT | violations | capability_result.violations | S7 cc_composition read_registration |
| blockchain::CC_VALIDATE_REGISTRATION_V0 | refuse_incomplete_registration | INPUT | parameters | {'violations': '$.results.read_registration.violations'} | S7 cc_composition refuse_incomplete_registration |
| blockchain::CC_VALIDATE_REGISTRATION_V0 | refuse_incomplete_registration | INPUT | rules | [{'field': 'violations', 'op': 'eq', 'value': []}] | S7 cc_composition refuse_incomplete_registration |
| blockchain::CC_VALIDATE_REGISTRATION_V0 | refuse_incomplete_registration | OUTPUT | valid | capability_result.valid | S7 cc_composition refuse_incomplete_registration |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | read_state_admits_decision | INPUT | value | inputs.current_state | S7 cc_composition read_state_admits_decision |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | read_state_admits_decision | INPUT | allowed_set | ['UNVERIFIED'] | S7 cc_composition read_state_admits_decision |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | read_state_admits_decision | OUTPUT | is_member | capability_result.is_member | S7 cc_composition read_state_admits_decision |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | read_outcome_admitted | INPUT | value | inputs.decision | S7 cc_composition read_outcome_admitted |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | read_outcome_admitted | INPUT | allowed_set | ['ACCEPTED', 'REJECTED'] | S7 cc_composition read_outcome_admitted |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | read_outcome_admitted | OUTPUT | is_member | capability_result.is_member | S7 cc_composition read_outcome_admitted |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | compare_authority_to_person | INPUT | left | inputs.verifying_authority | S7 cc_composition compare_authority_to_person |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | compare_authority_to_person | INPUT | right | inputs.contact_address | S7 cc_composition compare_authority_to_person |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | compare_authority_to_person | OUTPUT | is_self | capability_result.is_equal | S7 cc_composition compare_authority_to_person |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | refuse_self_decision | INPUT | parameters | {'is_self': '$.results.compare_authority_to_person.is_self'} | S7 cc_composition refuse_self_decision |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | refuse_self_decision | INPUT | rules | [{'field': 'is_self', 'op': 'eq', 'value': False}] | S7 cc_composition refuse_self_decision |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | refuse_self_decision | OUTPUT | valid | capability_result.valid | S7 cc_composition refuse_self_decision |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | assemble_decided_actor | INPUT | fields | {'contact_address': '$.inputs.contact_address', 'state': '$.inputs.decision', 'verifying_authority': '$.inputs.verifying_authority', 'grounds': '$.inputs.grounds'} | S7 cc_composition assemble_decided_actor |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | assemble_decided_actor | OUTPUT | record | capability_result.record | S7 cc_composition assemble_decided_actor |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | write_decided_actor | INPUT | key | inputs.contact_address | S7 cc_composition write_decided_actor |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | write_decided_actor | INPUT | updates | results.assemble_decided_actor.record | S7 cc_composition write_decided_actor |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | write_decided_actor | OUTPUT | result_status | result_status | S7 cc_composition write_decided_actor |
| blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 | require_grounds_stated | INPUT | parameters | {'grounds': '$.inputs.grounds'} | S7 cc_composition require_grounds_stated |
| blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 | require_grounds_stated | INPUT | rules | [{'field': 'grounds', 'op': 'not_null'}, {'field': 'grounds', 'op': 'neq', 'value': ''}] | S7 cc_composition require_grounds_stated |
| blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 | require_grounds_stated | OUTPUT | valid | capability_result.valid | S7 cc_composition require_grounds_stated |
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

---

## 8. Interface Fields

<!-- register:interface_fields optional -->
| Artifact | Direction (INPUT, OUTPUT, ATTRIBUTE) | Field | Type | Required (YES, NO) | Default | Meaning |
|----------|--------------------------------------|-------|------|--------------------|---------|---------|
| blockchain::CC_VALIDATE_REGISTRATION_V0 | INPUT | actor_record | object | YES |  | The registration as the person supplied it. |
| blockchain::CC_VALIDATE_REGISTRATION_V0 | OUTPUT | violations | array | YES |  | What the registration lacks; a registration lacking anything is refused. |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | current_state | string | YES |  | The state the person is in when the decision is made. |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | decision | string | YES |  | The decision the act records. |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | verifying_authority | string | YES |  | Who is making the decision. |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | contact_address | string | YES |  | The person the decision is about. |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | grounds | string | NO |  | Why, where the authority states it. |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | OUTPUT | result_status | string | YES |  | Whether the decision was recorded. |
| blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 | INPUT | grounds | string | NO |  | Why the person is refused. A rejection stating none is refused by the rule, not by admission. |
| blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 | OUTPUT | valid | boolean | YES |  | Whether grounds were stated. |
| blockchain::IN_ACTOR_ACCEPTANCE_V0 | INPUT | contact_address | string | YES |  | The person being accepted. |
| blockchain::IN_ACTOR_ACCEPTANCE_V0 | INPUT | verifying_authority | string | YES |  | The authority recording the acceptance. |
| blockchain::IN_ACTOR_ACCEPTANCE_V0 | INPUT | grounds | string | NO |  | Why, where the authority chooses to say. |
| blockchain::TI_REGISTER_ACTOR_V0 | INPUT | name | string | YES |  | The person's name. |
| blockchain::TI_REGISTER_ACTOR_V0 | INPUT | contact_address | string | YES |  | The address the person is reached at. |
| blockchain::TI_ACCEPT_ACTOR_V0 | INPUT | contact_address | string | YES |  | The person the decision is about. |
| blockchain::TI_ACCEPT_ACTOR_V0 | INPUT | verifying_authority | string | YES |  | Who is making the decision. |
| blockchain::TI_ACCEPT_ACTOR_V0 | INPUT | grounds | string | NO |  | Why, where the decider chooses to say. |
| blockchain::TI_REJECT_ACTOR_V0 | INPUT | contact_address | string | YES |  | The person the decision is about. |
| blockchain::TI_REJECT_ACTOR_V0 | INPUT | verifying_authority | string | YES |  | Who is making the decision. |
| blockchain::TI_REJECT_ACTOR_V0 | INPUT | grounds | string | YES |  | Why the person is refused. A rejection stating none is refused. |

---

## 9. Implementation Bindings

<!-- register:implementation_bindings optional -->
| CT Code | Module | Callable | Operation | Kind (atom, molecule) | Purity (ct_pure, ct_impure) | Refusal (raises, returns, never) | Source Finding |
|---------|--------|----------|-----------|-----------------------|-----------------------------|----------------------------------|----------------|

---

## 10. Vocabulary Extensions

<!-- register:vocabulary_extensions optional -->
| Vocabulary Code | Extends | Group | Casing | Value | Meaning | Source Finding |
|-----------------|---------|-------|--------|-------|---------|----------------|

---

## 11. Runtime Policies

<!-- register:runtime_policies optional -->
| RB Code | Capability | Key | Value | Source Finding |
|---------|------------|-----|-------|----------------|

---

## 12. Artifact Properties

<!-- register:artifact_properties optional -->
| Artifact | Property | Value | Source Finding |
|----------|----------|-------|----------------|
| blockchain::WF_REGISTER_ACTOR_V0 | emit.EXIT_SUCCESS | blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0 | S6 pps_artifacts_requiring_action #4 |
| blockchain::WF_ACCEPT_ACTOR_V0 | emit.EXIT_SUCCESS | blockchain::EV_ACTOR_ACCEPTED_V0 | S6 pps_artifacts_requiring_action #5 |
| blockchain::WF_REJECT_ACTOR_V0 | emit.EXIT_SUCCESS | blockchain::EV_ACTOR_REJECTED_V0 | S6 pps_artifacts_requiring_action #6 |
| blockchain::WF_ACCEPT_ACTOR_V0 | supersedes | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | S6 pps_artifacts_requiring_action #5 |
| blockchain::WF_REJECT_ACTOR_V0 | supersedes | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | S6 pps_artifacts_requiring_action #6 |
| blockchain::IN_ACTOR_ACCEPTANCE_V0 | supersedes | blockchain::IN_ACTOR_VERIFIED_V0 | S6 pps_artifacts_requiring_action #10 |

---

## 13. STRUCTURE Stores

<!-- register:structure_stores optional -->
| Store Name | Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0) | Proposed Path | Used By | Source Finding |
|------------|------|------|------|----------------|

---

## 14. Transport Bindings

<!-- register:transport_bindings optional -->
| Artifact | Direction (INGRESS, EGRESS) | Operation | Handler Kind (WF_INVOCATION, SNAPSHOT_READ) | Handler Target | Field | Bound To | Source Finding |
|----------|------------------------------|-----------|----------------------------------------------|----------------|-------|----------|----------------|
| blockchain::TI_REGISTER_ACTOR_V0 | INGRESS | blockchain.register_actor | WF_INVOCATION | blockchain::WF_REGISTER_ACTOR_V0 | actor_record.name | ${input.name} | S6 pps_artifacts_requiring_action #7 |
| blockchain::TI_REGISTER_ACTOR_V0 | INGRESS | blockchain.register_actor | WF_INVOCATION | blockchain::WF_REGISTER_ACTOR_V0 | actor_record.contact_address | ${input.contact_address} | S6 pps_artifacts_requiring_action #7 |
| blockchain::TI_REGISTER_ACTOR_V0 | INGRESS | blockchain.register_actor | WF_INVOCATION | blockchain::WF_REGISTER_ACTOR_V0 | actor_record.currency_preference | BACHI | S6 pps_artifacts_requiring_action #7 |
| blockchain::TI_REGISTER_ACTOR_V0 | INGRESS | blockchain.register_actor | WF_INVOCATION | blockchain::WF_REGISTER_ACTOR_V0 | actor_record.language | en | S6 pps_artifacts_requiring_action #7 |
| blockchain::TI_REGISTER_ACTOR_V0 | INGRESS | blockchain.register_actor | WF_INVOCATION | blockchain::WF_REGISTER_ACTOR_V0 | address_path | contact_address | S6 pps_artifacts_requiring_action #7 |
| blockchain::TI_REGISTER_ACTOR_V0 | INGRESS | blockchain.register_actor | WF_INVOCATION | blockchain::WF_REGISTER_ACTOR_V0 | address_type | string | S6 pps_artifacts_requiring_action #7 |
| blockchain::TI_REGISTER_ACTOR_V0 | INGRESS | blockchain.register_actor | WF_INVOCATION | blockchain::WF_REGISTER_ACTOR_V0 | stream_id | ACTOR_OCCURRENCES | S6 pps_artifacts_requiring_action #7 |
| blockchain::TI_REGISTER_ACTOR_V0 | INGRESS | blockchain.register_actor | WF_INVOCATION | blockchain::WF_REGISTER_ACTOR_V0 | occurrence_fields.occurrence | ACTOR_REGISTERED_UNVERIFIED | S6 pps_artifacts_requiring_action #7 |
| blockchain::TI_REGISTER_ACTOR_V0 | INGRESS | blockchain.register_actor | WF_INVOCATION | blockchain::WF_REGISTER_ACTOR_V0 | occurrence_fields.contact_address | ${input.contact_address} | S6 pps_artifacts_requiring_action #7 |
| blockchain::TI_ACCEPT_ACTOR_V0 | INGRESS | blockchain.accept_actor | WF_INVOCATION | blockchain::WF_ACCEPT_ACTOR_V0 | contact_address | ${input.contact_address} | S6 pps_artifacts_requiring_action #8 |
| blockchain::TI_ACCEPT_ACTOR_V0 | INGRESS | blockchain.accept_actor | WF_INVOCATION | blockchain::WF_ACCEPT_ACTOR_V0 | verifying_authority | ${input.verifying_authority} | S6 pps_artifacts_requiring_action #8 |
| blockchain::TI_ACCEPT_ACTOR_V0 | INGRESS | blockchain.accept_actor | WF_INVOCATION | blockchain::WF_ACCEPT_ACTOR_V0 | grounds | ${input.grounds} | S6 pps_artifacts_requiring_action #8 |
| blockchain::TI_ACCEPT_ACTOR_V0 | INGRESS | blockchain.accept_actor | WF_INVOCATION | blockchain::WF_ACCEPT_ACTOR_V0 | stream_id | ACTOR_OCCURRENCES | S6 pps_artifacts_requiring_action #8 |
| blockchain::TI_ACCEPT_ACTOR_V0 | INGRESS | blockchain.accept_actor | WF_INVOCATION | blockchain::WF_ACCEPT_ACTOR_V0 | occurrence_fields.occurrence | ACTOR_ACCEPTED | S6 pps_artifacts_requiring_action #8 |
| blockchain::TI_ACCEPT_ACTOR_V0 | INGRESS | blockchain.accept_actor | WF_INVOCATION | blockchain::WF_ACCEPT_ACTOR_V0 | occurrence_fields.contact_address | ${input.contact_address} | S6 pps_artifacts_requiring_action #8 |
| blockchain::TI_ACCEPT_ACTOR_V0 | INGRESS | blockchain.accept_actor | WF_INVOCATION | blockchain::WF_ACCEPT_ACTOR_V0 | occurrence_fields.verifying_authority | ${input.verifying_authority} | S6 pps_artifacts_requiring_action #8 |
| blockchain::TI_ACCEPT_ACTOR_V0 | INGRESS | blockchain.accept_actor | WF_INVOCATION | blockchain::WF_ACCEPT_ACTOR_V0 | occurrence_fields.grounds | ${input.grounds} | S6 pps_artifacts_requiring_action #8 |
| blockchain::TI_REJECT_ACTOR_V0 | INGRESS | blockchain.reject_actor | WF_INVOCATION | blockchain::WF_REJECT_ACTOR_V0 | contact_address | ${input.contact_address} | S6 pps_artifacts_requiring_action #9 |
| blockchain::TI_REJECT_ACTOR_V0 | INGRESS | blockchain.reject_actor | WF_INVOCATION | blockchain::WF_REJECT_ACTOR_V0 | verifying_authority | ${input.verifying_authority} | S6 pps_artifacts_requiring_action #9 |
| blockchain::TI_REJECT_ACTOR_V0 | INGRESS | blockchain.reject_actor | WF_INVOCATION | blockchain::WF_REJECT_ACTOR_V0 | grounds | ${input.grounds} | S6 pps_artifacts_requiring_action #9 |
| blockchain::TI_REJECT_ACTOR_V0 | INGRESS | blockchain.reject_actor | WF_INVOCATION | blockchain::WF_REJECT_ACTOR_V0 | stream_id | ACTOR_OCCURRENCES | S6 pps_artifacts_requiring_action #9 |
| blockchain::TI_REJECT_ACTOR_V0 | INGRESS | blockchain.reject_actor | WF_INVOCATION | blockchain::WF_REJECT_ACTOR_V0 | occurrence_fields.occurrence | ACTOR_REJECTED | S6 pps_artifacts_requiring_action #9 |
| blockchain::TI_REJECT_ACTOR_V0 | INGRESS | blockchain.reject_actor | WF_INVOCATION | blockchain::WF_REJECT_ACTOR_V0 | occurrence_fields.contact_address | ${input.contact_address} | S6 pps_artifacts_requiring_action #9 |
| blockchain::TI_REJECT_ACTOR_V0 | INGRESS | blockchain.reject_actor | WF_INVOCATION | blockchain::WF_REJECT_ACTOR_V0 | occurrence_fields.verifying_authority | ${input.verifying_authority} | S6 pps_artifacts_requiring_action #9 |
| blockchain::TI_REJECT_ACTOR_V0 | INGRESS | blockchain.reject_actor | WF_INVOCATION | blockchain::WF_REJECT_ACTOR_V0 | occurrence_fields.grounds | ${input.grounds} | S6 pps_artifacts_requiring_action #9 |

---

## 15. Artifact Summary

<!-- register:artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Subdomain | Count | Artifacts |
|-------------------------------|-----------|-------|-----------|
| EXTEND | identity | 10 | blockchain::CC_VALIDATE_REGISTRATION_V0, blockchain::CC_RECORD_VERIFICATION_DECISION_V0, blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0, blockchain::WF_REGISTER_ACTOR_V0, blockchain::WF_ACCEPT_ACTOR_V0, blockchain::WF_REJECT_ACTOR_V0, blockchain::TI_REGISTER_ACTOR_V0, blockchain::TI_ACCEPT_ACTOR_V0, blockchain::TI_REJECT_ACTOR_V0, blockchain::IN_ACTOR_ACCEPTANCE_V0 |

---

## 16. Generation Provenance

<!-- register:generation_provenance optional -->
| Artifact | Generator | Generator Sources | Source Finding |
|----------|-----------|-------------------|----------------|

---

## 17. Declared Reach

<!-- register:declared_reach optional -->
| Act | Consults | Source Finding |
|-----|----------|----------------|

---

## 18. Refusal Discharge

<!-- register:refusal_discharge optional -->
| Operation | Refused When | Act | Step | Outcome | Source Finding |
|-----------|--------------|-----|------|---------|----------------|
| Registering a person | The registration lacks the person's name or their address | blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_VALIDATE_REGISTRATION_V0 | VIOLATION | S0 operation_refusals #1 |
| Recording a decision | The person is not unverified | blockchain::WF_ACCEPT_ACTOR_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | VIOLATION | S0 operation_refusals #2 |
| Recording a decision | The person is not unverified | blockchain::WF_REJECT_ACTOR_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | VIOLATION | S0 operation_refusals #2 |
| Recording a decision | The decision is neither an acceptance nor a rejection | blockchain::WF_ACCEPT_ACTOR_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | VIOLATION | S0 operation_refusals #3 |
| Recording a decision | The decision is neither an acceptance nor a rejection | blockchain::WF_REJECT_ACTOR_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | VIOLATION | S0 operation_refusals #3 |
| Recording a rejection | No grounds are stated | blockchain::WF_REJECT_ACTOR_V0 | blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 | VIOLATION | S0 operation_refusals #4 |
| Recording a decision | The authority is the person decided about | blockchain::WF_ACCEPT_ACTOR_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | VIOLATION | S0 operation_refusals #5 |
| Recording a decision | The authority is the person decided about | blockchain::WF_REJECT_ACTOR_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | VIOLATION | S0 operation_refusals #5 |

---

## 19. Refusal Deferrals

<!-- register:refusal_deferrals optional -->
| Operation | Refused When | Deferred To | Until | Source Finding |
|-----------|--------------|-------------|-------|----------------|

---

## 20. Refusal — Governance-Surface Discharge

<!-- register:refusal_governance_discharge optional -->
| Operation | Refused When | Phase | Governing Rule | Source Finding |
|-----------|--------------|-------|----------------|----------------|

---

## 21. Molecule Steps

<!-- register:molecule_steps optional -->
| CT Code | Step | Kind (atom, molecule, loop) | Target | Over | Iterator | Emits | Source Finding |
|---------|------|-----------------------------|--------|------|----------|-------|----------------|

---

## 22. Molecule Step Bindings

<!-- register:molecule_step_bindings optional -->
| CT Code | Step | Role (INPUT, CARRY, UPDATE) | Field | Bound To | Source Finding |
|---------|------|-----------------------------|-------|----------|----------------|

---

## 23. Test Cases

<!-- register:test_cases optional -->
| CT Code | Case | Expected Outcome (SUCCESS, VIOLATION) | Source Finding |
|---------|------|---------------------------------------|----------------|

---

## 24. Test Case Values

<!-- register:test_case_values optional -->
| CT Code | Case | Role (INPUT, EXPECTED, ASSERT, RECORDED) | Field | Value | Source Finding |
|---------|------|------------------------------------------|-------|-------|----------------|

---

## gov_projection — Governed Handoff to Stage 8

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 6 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
| **Emits** → Stage 8 | design_resolution · existing_inventory · new_artifacts · rb_declarations · execution_topology · cc_composition · step_bindings · interface_fields · implementation_bindings · vocabulary_extensions · runtime_policies · artifact_properties · structure_stores · artifact_summary · generation_provenance |
