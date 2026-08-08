# Stage 7 — Design Intent: blockchain / identity

**Stage:** 7 — Design Intent
**CR:** cr_01_identity
**Status:** DRAFT
**Feeds:** Stage 8 — Authoring Mandate

The first phase that names artifacts. Every code the business intent proposed is bound to an
identity in the blockchain namespace, every store is given a type and a path, and every capability
contract is composed step by step. One step cannot be composed: the substrate offers no capability
that determines a time, and the design declares the field rather than inventing a value for it.

---

## 1. Design Decisions Resolution

<!-- register:design_resolution optional -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|
| The trail rests on the append-only capability | An occurrence that has happened cannot be un-happened | ACTOR_OCCURRENCES is typed CS_APPENDONLY_JSONL_V0, which offers no update and no delete | S4 design_decisions #1 |
| An actor's state is held as a value | The refusal that an actor is decided about once needs the state at the moment of deciding | ACTORS is typed CS_MUTABLE_JSON_V0 and read by blockchain::CC_RESOLVE_ACTOR_V0 before any decision is recorded | S4 design_decisions #2 |
| The contact address is the identifier | Two registrations carrying the same address are the same person | CONTACT_ADDRESS_REGISTRY is typed CS_REGISTRY_V0 and keyed on the address as supplied; no identifier is generated | S4 design_decisions #3 |
| Acceptance and rejection are two occurrences | A rejected actor must never be readable as accepted | blockchain::EV_ACTOR_ACCEPTED_V0 and blockchain::EV_ACTOR_REJECTED_V0 are separate artifacts; no artifact carries an outcome field | S4 design_decisions #4 |
| The time capability is a substrate gap | Every occurrence carries the time it actually happened, determined as it occurs | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 reads capability_side_effects::CS_CLOCK_V0 before it assembles the record, so occurred_at is determined where the occurrence is recorded and no caller may assert it | S4 design_decisions #5 |
| The authority is recorded and never resolved | An authority is identified outside this function | The decision carries verifying_authority as a value; no store holds authorities and no step resolves one | S4 design_decisions #6 |

---

## 2. Artifact Inventory — Existing Artifacts

<!-- register:existing_inventory -->
| FQDN | Action (REPLACE, REUSE, EXTEND, REVIEW) | Summary | Reason | Source Finding |
|------|------------------------------------------|---------|--------|----------------|
| capability_side_effects::CS_APPENDONLY_JSONL_V0 | REUSE | Appends a record to a named stream and reads the stream whole | Holds the occurrence trail; offers no update and no delete | S6 pps_artifacts_requiring_action capability_side_effects::CS_APPENDONLY_JSONL_V0 |
| capability_side_effects::CS_MUTABLE_JSON_V0 | REUSE | Keyed JSON state with read, write and select | Holds the actor record and its state | S6 pps_artifacts_requiring_action capability_side_effects::CS_MUTABLE_JSON_V0 |
| capability_side_effects::CS_REGISTRY_V0 | REUSE | Registers, resolves and reports a key | Claims the contact address and reports one already held | S6 pps_artifacts_requiring_action capability_side_effects::CS_REGISTRY_V0 |
| capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | REUSE | Reads a record for required fields and their form | Reads a registration for absence and malformation | S6 pps_artifacts_requiring_action capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 |
| capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 | REUSE | Reads a value against a declared admitted set | Reads the decision outcome and the state a decision is admitted from | S6 pps_artifacts_requiring_action capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 |
| capability_transforms::CT_PURE_COMPARE_EQUAL_V0 | REUSE | Compares two supplied values | Compares the authority named against the actor decided about | S6 pps_artifacts_requiring_action capability_transforms::CT_PURE_COMPARE_EQUAL_V0 |
| capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | REUSE | Assembles a record from supplied fields | Assembles the actor record and each occurrence record | S6 pps_artifacts_requiring_action capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 |
| capability_side_effects::CS_CLOCK_V0 | REUSE | Answers the current instant | Determines the time an occurrence happened, which no transform can | S4 dependency_graph the substrate capability supplying the current time |
| capability_transforms::CT_PURE_EXTRACT_V0 | REUSE | Extracts a named value from a supplied structure | Extracts the address and the decision fields | S6 pps_artifacts_requiring_action capability_transforms::CT_PURE_EXTRACT_V0 |

---

## 3. Artifact Family Mapping — New Artifacts

<!-- register:new_artifacts business_language=capability -->
| Capability | Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE) | Code | Summary | Owner Subdomain | Status | Source Finding |
|------------|------------------------------------------------|------|---------|-----------------|--------|----------------|
| Declare the actors of this business | AC | blockchain::AC_PARTICIPANT_V0 | The ordinary participant who registers themselves and is decided about | identity | NEW | S5 provisional_codes AC_PARTICIPANT_V0 |
| Declare the stores identity owns | STRUCTURE | blockchain::STRUCTURE_IDENTITY_STORAGE_V0 | Declares the three stores identity owns and the paths they occupy | identity | NEW | S5 provisional_codes STRUCTURE_IDENTITY_STORAGE_V0 |
| Bind identity's workflows to the stores they use | RB | blockchain::RB_IDENTITY_BINDINGS_V0 | Binds identity's workflows to the side effects and storage they use | identity | NEW | S5 provisional_codes RB_IDENTITY_BINDINGS_V0 |
| Recognise the moments an actor is registered, accepted and rejected | EV | blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0 | The moment a person is admitted and trusted with nothing | identity | NEW | S5 provisional_codes EV_ACTOR_REGISTERED_UNVERIFIED_V0 |
| Recognise the moments an actor is registered, accepted and rejected | EV | blockchain::EV_ACTOR_ACCEPTED_V0 | The moment an authority records a decision to trust an actor | identity | NEW | S5 provisional_codes EV_ACTOR_ACCEPTED_V0 |
| Recognise the moments an actor is registered, accepted and rejected | EV | blockchain::EV_ACTOR_REJECTED_V0 | The moment an authority records a decision not to trust an actor | identity | NEW | S5 provisional_codes EV_ACTOR_REJECTED_V0 |
| Admit a request to register a person | IN | blockchain::IN_ACTOR_REGISTERED_V0 | A request to admit a person as an actor | identity | NEW | S5 provisional_codes IN_ACTOR_REGISTERED_V0 |
| Admit a request to record a verification decision | IN | blockchain::IN_ACTOR_VERIFIED_V0 | A request to record a decision, carrying the authority, the outcome and the grounds | identity | NEW | S5 provisional_codes IN_ACTOR_VERIFIED_V0 |
| Admit a person's registration and record them unverified | WF | blockchain::WF_REGISTER_ACTOR_V0 | The governed sequence that admits a person as an unverified actor | identity | NEW | S5 provisional_codes WF_REGISTER_ACTOR_V0 |
| Record an authority's decision against a registered actor | WF | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | The governed sequence that records a decision against a registered actor | identity | NEW | S5 provisional_codes WF_RECORD_VERIFICATION_DECISION_V0 |
| Admit a person's registration and record them unverified | CC | blockchain::CC_VALIDATE_REGISTRATION_V0 | Confirms a registration carries a name and an address of the form asked for | identity | NEW | S5 provisional_codes CC_VALIDATE_REGISTRATION_V0 |
| Admit a person's registration and record them unverified | CC | blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | Claims a contact address so that two registrations of one person do not produce two actors | identity | NEW | S5 provisional_codes CC_CLAIM_CONTACT_ADDRESS_V0 |
| Admit a person's registration and record them unverified | CC | blockchain::CC_REGISTER_ACTOR_V0 | Writes the actor unverified after its address is claimed | identity | NEW | S5 provisional_codes CC_REGISTER_ACTOR_V0 |
| Record an authority's decision against a registered actor | CC | blockchain::CC_RESOLVE_ACTOR_V0 | Answers which actor a contact address denotes, and reports when none does | identity | NEW | S5 provisional_codes CC_RESOLVE_ACTOR_V0 |
| Record an authority's decision against a registered actor | CC | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | Refuses every declared refusal and moves the actor to its decided state | identity | NEW | S5 provisional_codes CC_RECORD_VERIFICATION_DECISION_V0 |
| Record an acceptance and a rejection | CC | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | Appends one occurrence to the trail | identity | NEW | S5 provisional_codes CC_APPEND_ACTOR_OCCURRENCE_V0 |

---

## 4. Runtime Binding (RB) Declarations

<!-- register:rb_declarations -->
| RB Code | Binds WF | CS Bindings | Storage Structure | Source Finding |
|---------|----------|-------------|-------------------|----------------|
| blockchain::RB_IDENTITY_BINDINGS_V0 | blockchain::WF_REGISTER_ACTOR_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_CLOCK_V0 | blockchain::STRUCTURE_IDENTITY_STORAGE_V0 | S6 storage_governance An atomic claim on each contact address |
| blockchain::RB_IDENTITY_BINDINGS_V0 | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_CLOCK_V0 | blockchain::STRUCTURE_IDENTITY_STORAGE_V0 | S6 storage_governance A durable record of every person the business knows, carrying whether it has accepted them |

---

## 5. Execution Topology

<!-- register:execution_topology -->
| Workflow | Node | Node Type (IN, CC, EXIT, EXIT_SUCCESS) | Routing | Source Finding |
|----------|------|----------------------------------------|---------|----------------|
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::IN_ACTOR_REGISTERED_V0 | IN | ACK -> blockchain::CC_VALIDATE_REGISTRATION_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_ACTOR_REGISTERED_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_VALIDATE_REGISTRATION_V0 | CC | SUCCESS -> blockchain::CC_CLAIM_CONTACT_ADDRESS_V0; VIOLATION -> EXIT_REJECTED | S7 new_artifacts CC_VALIDATE_REGISTRATION_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | CC | SUCCESS -> blockchain::CC_REGISTER_ACTOR_V0; ALREADY_EXISTS -> blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED | S7 new_artifacts CC_CLAIM_CONTACT_ADDRESS_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_REGISTER_ACTOR_V0 | CC | SUCCESS -> blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED | S7 new_artifacts CC_REGISTER_ACTOR_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | CC | SUCCESS -> EXIT_SUCCESS; VIOLATION -> EXIT_REJECTED | S7 new_artifacts CC_APPEND_ACTOR_OCCURRENCE_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | EXIT_REJECTED | EXIT | — | S7 new_artifacts WF_REGISTER_ACTOR_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | EXIT_SUCCESS | EXIT_SUCCESS | — | S7 new_artifacts WF_REGISTER_ACTOR_V0 |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | blockchain::IN_ACTOR_VERIFIED_V0 | IN | ACK -> blockchain::CC_RESOLVE_ACTOR_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_ACTOR_VERIFIED_V0 |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | blockchain::CC_RESOLVE_ACTOR_V0 | CC | SUCCESS -> blockchain::CC_RECORD_VERIFICATION_DECISION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED | S7 new_artifacts CC_RESOLVE_ACTOR_V0 |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | CC | SUCCESS -> blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED | S7 new_artifacts CC_RECORD_VERIFICATION_DECISION_V0 |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | CC | SUCCESS -> EXIT_SUCCESS; VIOLATION -> EXIT_REJECTED | S7 new_artifacts CC_APPEND_ACTOR_OCCURRENCE_V0 |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | EXIT_REJECTED | EXIT | — | S7 new_artifacts WF_RECORD_VERIFICATION_DECISION_V0 |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | EXIT_SUCCESS | EXIT_SUCCESS | — | S7 new_artifacts WF_RECORD_VERIFICATION_DECISION_V0 |

---

## 6. Capability Composition

<!-- register:cc_composition optional -->
| CC Code | Step | Step Name | Capability | Kind (CT, CS) | Operation | Store | Consumes | Produces | Routing | Interpreted By | Semantic Status | Interface |
|---------|------|-----------|------------|---------------|-----------|-------|----------|----------|---------|----------------|-----------------|-----------|
| blockchain::CC_VALIDATE_REGISTRATION_V0 | 1 | read_registration | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | CT | VALIDATE_RECORD_STRUCTURE | — | record, schema | violations | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: record=record, schema=schema; out: violations=violations |
| blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | 1 | extract_address | capability_transforms::CT_PURE_EXTRACT_V0 | CT | EXTRACT | — | from, path, type | result | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: from=from, path=path, type=type; out: result=result |
| blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | 2 | claim_address | capability_side_effects::CS_REGISTRY_V0 | CS | REGISTER | CONTACT_ADDRESS_REGISTRY | key, target_cs, target_ref | address | SUCCESS -> continue; ALREADY_EXISTS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | ALREADY_EXISTS | — |
| blockchain::CC_REGISTER_ACTOR_V0 | 1 | assemble_actor | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | CT | ASSEMBLE_RECORD | — | fields | record | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: fields=fields; out: record=record |
| blockchain::CC_REGISTER_ACTOR_V0 | 2 | write_actor | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | WRITE | ACTORS | key, value | result_status | SUCCESS -> continue; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | — |
| blockchain::CC_RESOLVE_ACTOR_V0 | 1 | resolve_address | capability_side_effects::CS_REGISTRY_V0 | CS | RESOLVE | CONTACT_ADDRESS_REGISTRY | key_or_address | target_ref | SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit | — | NOT_FOUND | — |
| blockchain::CC_RESOLVE_ACTOR_V0 | 2 | read_actor | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | READ | ACTORS | key | value | SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit | — | NOT_FOUND | — |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | 1 | read_state_admits_decision | capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 | CT | VALIDATE_SET_MEMBERSHIP | — | value, allowed_set | is_member | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: value=value, allowed_set=allowed_set; out: is_member=is_member |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | 2 | read_outcome_admitted | capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 | CT | VALIDATE_SET_MEMBERSHIP | — | value, allowed_set | is_member | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: value=value, allowed_set=allowed_set; out: is_member=is_member |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | 3 | refuse_self_verification | capability_transforms::CT_PURE_COMPARE_EQUAL_V0 | CT | COMPARE_EQUAL | — | left, right | is_equal | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: left=left, right=right; out: is_equal=is_equal |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | 4 | assemble_decided_actor | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | CT | ASSEMBLE_RECORD | — | fields | record | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: fields=fields; out: record=record |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | 5 | write_decided_actor | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | WRITE | ACTORS | key, value | result_status | SUCCESS -> continue; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | — |
| blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | 1 | read_now | capability_side_effects::CS_CLOCK_V0 | CS | NOW | — | — | timestamp | SUCCESS -> continue; BACKEND_ERROR -> exit | — | SUCCESS | — |
| blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | 2 | assemble_occurrence | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | CT | ASSEMBLE_RECORD | — | fields | record | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: fields=fields; out: record=record |
| blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | 3 | append_occurrence | capability_side_effects::CS_APPENDONLY_JSONL_V0 | CS | APPEND | ACTOR_OCCURRENCES | record, stream_id, actor_id | sequence_number | SUCCESS -> continue; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | — |

---

## 7. Step Bindings

<!-- register:step_bindings optional -->
| Owner | Step | Direction (INPUT, OUTPUT) | Field | Bound To | Source Finding |
|-------|------|--------------------------|-------|----------|----------------|
| blockchain::CC_VALIDATE_REGISTRATION_V0 | read_registration | INPUT | record | inputs.actor_record | S7 cc_composition read_registration |
| blockchain::CC_VALIDATE_REGISTRATION_V0 | read_registration | INPUT | schema | inputs.registration_schema | S7 cc_composition read_registration |
| blockchain::CC_VALIDATE_REGISTRATION_V0 | read_registration | OUTPUT | violations | capability_result.violations | S7 cc_composition read_registration |
| blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | extract_address | INPUT | from | inputs.actor_record | S7 cc_composition extract_address |
| blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | extract_address | INPUT | path | inputs.address_path | S7 cc_composition extract_address |
| blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | extract_address | INPUT | type | inputs.address_type | S7 cc_composition extract_address |
| blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | extract_address | OUTPUT | result | capability_result.result | S7 cc_composition extract_address |
| blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | claim_address | INPUT | key | results.extract_address.result | S7 cc_composition claim_address |
| blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | claim_address | INPUT | target_cs | CS_MUTABLE_JSON_V0 | S7 cc_composition claim_address |
| blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | claim_address | INPUT | target_ref | ACTORS | S7 cc_composition claim_address |
| blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | claim_address | OUTPUT | address | capability_result.address | S7 cc_composition claim_address |
| blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | claim_address | OUTPUT | result_status | result_status | S7 cc_composition claim_address |
| blockchain::CC_REGISTER_ACTOR_V0 | assemble_actor | INPUT | fields | inputs.actor_fields | S7 cc_composition assemble_actor |
| blockchain::CC_REGISTER_ACTOR_V0 | assemble_actor | OUTPUT | record | capability_result.record | S7 cc_composition assemble_actor |
| blockchain::CC_REGISTER_ACTOR_V0 | write_actor | INPUT | key | inputs.contact_address | S7 cc_composition write_actor |
| blockchain::CC_REGISTER_ACTOR_V0 | write_actor | INPUT | value | results.assemble_actor.record | S7 cc_composition write_actor |
| blockchain::CC_REGISTER_ACTOR_V0 | write_actor | OUTPUT | result_status | result_status | S7 cc_composition write_actor |
| blockchain::CC_RESOLVE_ACTOR_V0 | resolve_address | INPUT | key_or_address | inputs.contact_address | S7 cc_composition resolve_address |
| blockchain::CC_RESOLVE_ACTOR_V0 | resolve_address | OUTPUT | target_ref | capability_result.target_ref | S7 cc_composition resolve_address |
| blockchain::CC_RESOLVE_ACTOR_V0 | read_actor | INPUT | key | inputs.contact_address | S7 cc_composition read_actor |
| blockchain::CC_RESOLVE_ACTOR_V0 | read_actor | OUTPUT | value | capability_result.value | S7 cc_composition read_actor |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | read_state_admits_decision | INPUT | value | inputs.current_state | S7 cc_composition read_state_admits_decision |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | read_state_admits_decision | INPUT | allowed_set | inputs.states_admitting_a_decision | S7 cc_composition read_state_admits_decision |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | read_state_admits_decision | OUTPUT | is_member | capability_result.is_member | S7 cc_composition read_state_admits_decision |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | read_outcome_admitted | INPUT | value | inputs.decision | S7 cc_composition read_outcome_admitted |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | read_outcome_admitted | INPUT | allowed_set | inputs.admitted_outcomes | S7 cc_composition read_outcome_admitted |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | read_outcome_admitted | OUTPUT | is_member | capability_result.is_member | S7 cc_composition read_outcome_admitted |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | refuse_self_verification | INPUT | left | inputs.verifying_authority | S7 cc_composition refuse_self_verification |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | refuse_self_verification | INPUT | right | inputs.contact_address | S7 cc_composition refuse_self_verification |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | refuse_self_verification | OUTPUT | is_equal | capability_result.is_equal | S7 cc_composition refuse_self_verification |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | assemble_decided_actor | INPUT | fields | inputs.decided_actor_fields | S7 cc_composition assemble_decided_actor |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | assemble_decided_actor | OUTPUT | record | capability_result.record | S7 cc_composition assemble_decided_actor |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | write_decided_actor | INPUT | key | inputs.contact_address | S7 cc_composition write_decided_actor |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | write_decided_actor | INPUT | value | results.assemble_decided_actor.record | S7 cc_composition write_decided_actor |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | write_decided_actor | OUTPUT | result_status | result_status | S7 cc_composition write_decided_actor |
| blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | read_now | OUTPUT | timestamp | capability_result.timestamp | S7 cc_composition read_now |
| blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | assemble_occurrence | INPUT | fields | {'occurrence': '$.inputs.occurrence_fields.occurrence', 'contact_address': '$.inputs.contact_address', 'verifying_authority': '$.inputs.occurrence_fields.verifying_authority', 'grounds': '$.inputs.occurrence_fields.grounds', 'occurred_at': '$.results.read_now.timestamp'} | S7 cc_composition assemble_occurrence |
| blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | assemble_occurrence | OUTPUT | record | capability_result.record | S7 cc_composition assemble_occurrence |
| blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | append_occurrence | INPUT | record | results.assemble_occurrence.record | S7 cc_composition append_occurrence |
| blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | append_occurrence | INPUT | stream_id | inputs.stream_id | S7 cc_composition append_occurrence |
| blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | append_occurrence | INPUT | actor_id | inputs.contact_address | S7 cc_composition append_occurrence |
| blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | append_occurrence | OUTPUT | sequence_number | capability_result.sequence_number | S7 cc_composition append_occurrence |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_VALIDATE_REGISTRATION_V0 | INPUT | actor_record | payload.actor_record | S7 execution_topology CC_VALIDATE_REGISTRATION_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_VALIDATE_REGISTRATION_V0 | INPUT | registration_schema | payload.registration_schema | S7 execution_topology CC_VALIDATE_REGISTRATION_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | INPUT | actor_record | payload.actor_record | S7 execution_topology CC_CLAIM_CONTACT_ADDRESS_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | INPUT | address_path | payload.address_path | S7 execution_topology CC_CLAIM_CONTACT_ADDRESS_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | INPUT | address_type | payload.address_type | S7 execution_topology CC_CLAIM_CONTACT_ADDRESS_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_REGISTER_ACTOR_V0 | INPUT | actor_fields | payload.actor_record | S7 execution_topology CC_REGISTER_ACTOR_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_REGISTER_ACTOR_V0 | INPUT | contact_address | results.CC_CLAIM_CONTACT_ADDRESS_V0.result | S7 execution_topology CC_REGISTER_ACTOR_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | INPUT | occurrence_fields | payload.occurrence_fields | S7 execution_topology CC_APPEND_ACTOR_OCCURRENCE_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | INPUT | stream_id | payload.stream_id | S7 execution_topology CC_APPEND_ACTOR_OCCURRENCE_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | INPUT | contact_address | results.CC_CLAIM_CONTACT_ADDRESS_V0.result | S7 execution_topology CC_APPEND_ACTOR_OCCURRENCE_V0 |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | blockchain::CC_RESOLVE_ACTOR_V0 | INPUT | contact_address | payload.contact_address | S7 execution_topology CC_RESOLVE_ACTOR_V0 |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | current_state | results.CC_RESOLVE_ACTOR_V0.value.state | S7 execution_topology CC_RECORD_VERIFICATION_DECISION_V0 |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | states_admitting_a_decision | payload.states_admitting_a_decision | S7 execution_topology CC_RECORD_VERIFICATION_DECISION_V0 |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | decision | payload.decision | S7 execution_topology CC_RECORD_VERIFICATION_DECISION_V0 |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | admitted_outcomes | payload.admitted_outcomes | S7 execution_topology CC_RECORD_VERIFICATION_DECISION_V0 |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | verifying_authority | payload.verifying_authority | S7 execution_topology CC_RECORD_VERIFICATION_DECISION_V0 |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | contact_address | payload.contact_address | S7 execution_topology CC_RECORD_VERIFICATION_DECISION_V0 |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | decided_actor_fields | payload.decided_actor_fields | S7 execution_topology CC_RECORD_VERIFICATION_DECISION_V0 |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | INPUT | occurrence_fields | payload.occurrence_fields | S7 execution_topology CC_APPEND_ACTOR_OCCURRENCE_V0 |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | INPUT | stream_id | payload.stream_id | S7 execution_topology CC_APPEND_ACTOR_OCCURRENCE_V0 |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | INPUT | contact_address | payload.contact_address | S7 execution_topology CC_APPEND_ACTOR_OCCURRENCE_V0 |

---

## 8. Interface Fields

<!-- register:interface_fields optional -->
| Artifact | Direction (INPUT, OUTPUT, ATTRIBUTE) | Field | Type | Required (YES, NO) | Default | Meaning |
|----------|--------------------------------------|-------|------|--------------------|---------|---------|
| blockchain::IN_ACTOR_REGISTERED_V0 | INPUT | actor_record | object | YES |  | The details the person supplies about themselves |
| blockchain::IN_ACTOR_REGISTERED_V0 | INPUT | registration_schema | object | YES |  | The schema the supplied details are read against for absence and form |
| blockchain::IN_ACTOR_VERIFIED_V0 | INPUT | contact_address | string | YES |  | The address naming the actor the decision is about |
| blockchain::IN_ACTOR_VERIFIED_V0 | INPUT | verifying_authority | string | YES |  | The authority making the decision, recorded and never resolved |
| blockchain::IN_ACTOR_VERIFIED_V0 | INPUT | decision | string | YES |  | The outcome, which must be one of the two admitted values |
| blockchain::IN_ACTOR_VERIFIED_V0 | INPUT | grounds | string | NO |  | The reason stated for the decision; required for a rejection |
| blockchain::AC_PARTICIPANT_V0 | ATTRIBUTE | contact_address | string | YES |  | The address identifying the participant |
| blockchain::AC_PARTICIPANT_V0 | ATTRIBUTE | name | string | YES |  | What the person is called, as they supplied it |
| blockchain::AC_PARTICIPANT_V0 | ATTRIBUTE | currency_preference | string | NO | BACHI | The currency the person prefers to be quoted in |
| blockchain::AC_PARTICIPANT_V0 | ATTRIBUTE | language | string | NO | en | The language the person prefers to be addressed in |
| blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0 | ATTRIBUTE | contact_address | string | YES |  | The actor admitted |
| blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0 | ATTRIBUTE | occurred_at | string | YES |  | The time the admission happened, determined at the moment it occurred |
| blockchain::EV_ACTOR_ACCEPTED_V0 | ATTRIBUTE | contact_address | string | YES |  | The actor accepted |
| blockchain::EV_ACTOR_ACCEPTED_V0 | ATTRIBUTE | verifying_authority | string | YES |  | The authority that accepted them |
| blockchain::EV_ACTOR_ACCEPTED_V0 | ATTRIBUTE | grounds | string | NO |  | The reason stated, which an acceptance may omit |
| blockchain::EV_ACTOR_ACCEPTED_V0 | ATTRIBUTE | occurred_at | string | YES |  | The time the acceptance happened, determined at the moment it occurred |
| blockchain::EV_ACTOR_REJECTED_V0 | ATTRIBUTE | contact_address | string | YES |  | The actor rejected |
| blockchain::EV_ACTOR_REJECTED_V0 | ATTRIBUTE | verifying_authority | string | YES |  | The authority that rejected them |
| blockchain::EV_ACTOR_REJECTED_V0 | ATTRIBUTE | grounds | string | YES |  | The reason stated, which a rejection must carry |
| blockchain::EV_ACTOR_REJECTED_V0 | ATTRIBUTE | occurred_at | string | YES |  | The time the rejection happened, determined at the moment it occurred |
| blockchain::CC_VALIDATE_REGISTRATION_V0 | INPUT | actor_record | object | YES |  | The details the person supplied, as the operation receives them |
| blockchain::CC_VALIDATE_REGISTRATION_V0 | INPUT | registration_schema | object | YES |  | The schema the details are read against for absence and form |
| blockchain::CC_VALIDATE_REGISTRATION_V0 | OUTPUT | violations | array | YES |  | The fields the registration failed to supply readably |
| blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | INPUT | actor_record | object | YES |  | The registration carrying the address to claim |
| blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | INPUT | address_path | string | YES |  | Where in the registration the contact address is found |
| blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | INPUT | address_type | string | YES |  | The type the contact address must be |
| blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | OUTPUT | result | string | YES |  | The contact address as extracted from the registration |
| blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | OUTPUT | address | string | YES |  | The store address the claim was registered at |
| blockchain::CC_REGISTER_ACTOR_V0 | INPUT | actor_fields | object | YES |  | The fields the actor record is assembled from |
| blockchain::CC_REGISTER_ACTOR_V0 | INPUT | contact_address | string | YES |  | The claimed address the actor is written under |
| blockchain::CC_REGISTER_ACTOR_V0 | OUTPUT | result_status | string | YES |  | Whether the actor was written |
| blockchain::CC_RESOLVE_ACTOR_V0 | INPUT | contact_address | string | YES |  | The address naming the actor to resolve |
| blockchain::CC_RESOLVE_ACTOR_V0 | OUTPUT | value | object | YES |  | The actor and its current state, or absent when none is held |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | current_state | string | YES |  | The actor's state as read before the decision |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | states_admitting_a_decision | array | YES |  | The states from which a decision may be made |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | decision | string | YES |  | The outcome the authority states |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | admitted_outcomes | array | YES |  | The two outcomes a decision may carry |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | verifying_authority | string | YES |  | The authority making the decision, recorded and never resolved |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | contact_address | string | YES |  | The actor decided about |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | decided_actor_fields | object | YES |  | The fields the decided actor record is assembled from |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | OUTPUT | result_status | string | YES |  | Whether the decision was recorded |
| blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | INPUT | occurrence_fields | object | YES |  | The fields the occurrence record is assembled from, including occurred_at |
| blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | INPUT | stream_id | string | YES |  | The trail the occurrence is appended to |
| blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | INPUT | contact_address | string | YES |  | The actor the occurrence is recorded against |
| blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | OUTPUT | sequence_number | integer | YES |  | The position the occurrence was written at, which the store assigns |

---

## 9. Implementation Bindings

<!-- register:implementation_bindings optional -->
| CT Code | Module | Callable | Operation | Kind (atom, molecule) | Purity (ct_pure, ct_impure) | Source Finding |
|---------|--------|----------|-----------|-----------------------|------------------------------|----------------|
| NONE IDENTIFIED |

---

## 10. Vocabulary Extensions

<!-- register:vocabulary_extensions optional -->
| Vocabulary Code | Extends | Value | Meaning | Source Finding |
|-----------------|---------|-------|---------|----------------|
| NONE IDENTIFIED |

---

## 11. Runtime Policies

<!-- register:runtime_policies optional -->
| RB Code | Capability | Key | Value | Source Finding |
|---------|-----------|-----|-------|----------------|
| blockchain::RB_IDENTITY_BINDINGS_V0 | capability_side_effects::CS_MUTABLE_JSON_V0 | structure | blockchain::STRUCTURE_IDENTITY_STORAGE_V0 | S6 storage_governance A durable record of every person the business knows, carrying whether it has accepted them |
| blockchain::RB_IDENTITY_BINDINGS_V0 | capability_side_effects::CS_REGISTRY_V0 | structure | blockchain::STRUCTURE_IDENTITY_STORAGE_V0 | S6 storage_governance An atomic claim on each contact address |
| blockchain::RB_IDENTITY_BINDINGS_V0 | capability_side_effects::CS_APPENDONLY_JSONL_V0 | structure | blockchain::STRUCTURE_IDENTITY_STORAGE_V0 | S6 storage_governance An unamendable trail of every occurrence recorded against an actor |
| blockchain::RB_IDENTITY_BINDINGS_V0 | capability_side_effects::CS_CLOCK_V0 | precision | seconds | S4 design_decisions #5 | S6 storage_governance An unamendable trail of every occurrence recorded against an actor |

---

## 12. Artifact Properties

<!-- register:artifact_properties optional -->
| Artifact | Property | Value | Source Finding |
|----------|----------|-------|----------------|
| blockchain::AC_PARTICIPANT_V0 | type | ENDUSER | S5 provisional_codes AC_PARTICIPANT_V0 |
| blockchain::EV_ACTOR_REJECTED_V0 | grounds_required | YES | S6 boundary_rules ACCEPTANCE_AND_REJECTION_ARE_DISTINCT |
| blockchain::EV_ACTOR_ACCEPTED_V0 | grounds_required | NO | S6 boundary_rules ACCEPTANCE_AND_REJECTION_ARE_DISTINCT |
| blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | occurred_at_source | capability_side_effects::CS_CLOCK_V0 | S6 boundary_rules NO_TIME_IS_INVENTED |

---

## 13. STRUCTURE Stores

<!-- register:structure_stores optional -->
| Store Name | Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0) | Proposed Path | Used By | Source Finding |
|------------|-----------------------------------------------------------|---------------|---------|----------------|
| ACTORS | CS_MUTABLE_JSON_V0 | blockchain/identity/actors.json | blockchain::CC_REGISTER_ACTOR_V0 | S6 storage_governance A durable record of every person the business knows, carrying whether it has accepted them |
| CONTACT_ADDRESS_REGISTRY | CS_REGISTRY_V0 | blockchain/identity/contact_address_registry.jsonl | blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | S6 storage_governance An atomic claim on each contact address |
| ACTOR_OCCURRENCES | CS_APPENDONLY_JSONL_V0 | blockchain/identity/actor_occurrences.jsonl | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | S6 storage_governance An unamendable trail of every occurrence recorded against an actor |

---

## 14. Transport Bindings

<!-- register:transport_bindings optional -->
| Artifact | Direction (INGRESS, EGRESS) | Operation | Handler Kind (WF_INVOCATION, SNAPSHOT_READ) | Handler Target | Field | Bound To | Source Finding |
|----------|----------------------------|-----------|---------------------------------------------|----------------|-------|----------|----------------|
| NONE IDENTIFIED |

## 15. Artifact Summary

<!-- register:artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Subdomain | Count | Artifacts |
|-------------------------------|-----------|-------|-----------|
| NEW | identity | 16 | 1 AC, 1 STRUCTURE, 1 RB, 3 EV, 2 IN, 2 WF, 6 CC |

---

## Gate 1 — Design Approval

The dossier is reviewed as a body. One thing is known and unresolved: no capability in the
composition determines a time, so `occurred_at` is declared on every occurrence and supplied by no
step of this design. Construction will report it undetermined, which is the correct outcome —
the design states what must be true and refuses to invent the value that would make it appear true.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | p5_business_intent_blockchain_identity_v0.md | COMPLETE |
| Stage 6 — Governance Intent | p6_governance_intent_blockchain_identity_v0.md | COMPLETE |
| Stage 7 — Design Intent | This document | COMPLETE |

---

## gov_projection — Governed Handoff to Stage 8

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | provisional_codes · business_objects · identity_semantics · invariants · actions |
| **Consumes** ← Stage 6 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules |
| **Emits** → Stage 8 | design_resolution · existing_inventory · new_artifacts · rb_declarations · execution_topology · cc_composition · step_bindings · interface_fields · implementation_bindings · vocabulary_extensions · runtime_policies · artifact_properties · structure_stores · artifact_summary |
