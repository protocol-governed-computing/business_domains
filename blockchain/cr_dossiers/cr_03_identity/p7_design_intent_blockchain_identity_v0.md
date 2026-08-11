# Stage 7 — Design Intent: blockchain / identity

**Stage:** 7 — Design Intent

**CR:** cr_03_identity

**Status:** DRAFT

**Feeds:** Stage 8 — Authoring Mandate

One artifact, amended. No artifact is authored: this change corrects a step of a contract the
composition already holds, and the contract is rendered whole under its own code. Four of its five
steps are reproduced exactly as they are; the fifth changes the operation it calls and where its
value comes from.

---

## 1. Design Resolution

<!-- register:design_resolution -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|
| The writing step calls a keyed update rather than a keyed write. | A decision may change only the person's state, the authority who decided and the grounds stated, and must leave everything else the business holds about them as it was. | A whole-value write sets what is held at a key, so every field the caller did not supply ceases to be held. A keyed update sets the fields it is given and leaves the rest of the record alone. The step changes operation and nothing else about the contract changes. | S3 analysis_findings Q1 |
| What the update sets is the record the fourth step assembles. | The three things a decision is entitled to change, and the address that identifies whose record it is. | The assembling step already produces exactly those fields and no others, so it becomes the update's argument rather than a whole value to overwrite with. The set of fields it carries is where the business rule now lives: what is absent from it is what a decision cannot touch. | S3 analysis_findings Q4 |
| The assembling step keeps its consumer, and the gap that recorded its loss is closed. | Nothing in the business asked for a step whose output nothing reads. | An earlier reading of this correction passed the decided fields straight to the update, which would have left the fourth step producing a record no step consumed. Taking the update's argument from that step instead keeps it in the pipeline, doing what it always did. The deferral recorded for it is withdrawn rather than carried. | S4 gap_register GAP-03 |
| A decision that names a person the store does not hold is refused rather than creating one. | A decision records a decision; it does not admit anyone. | The keyed write would set a value at a key nothing held, inventing a person nobody registered. The keyed update reports a violation and changes nothing. The refusal is a property of the operation, and the contract already admits that status. | S3 analysis_findings Q6 |
| The step keeps the name it has. | Nothing in the business names a step. | Renaming it would report thirteen facts lost where one changed: the completeness check compares a render against what is held and cannot tell a renamed step from a deleted one. Keeping the name leaves exactly one narrowing — the whole-value input replaced by the fields to set — which is the change itself and should be the only thing a reviewer sees. | S3 analysis_findings Q1 |
| The contract's inputs, refusals and result statuses are reproduced unchanged. | A caller sends what they send now and is told what they are told now. | Its three validations, its assembling step, its declared inputs and its admitted result statuses are stated here exactly as the composition holds them. A correction that altered any of them would be observable above the contract, which the business asked it not to be. | S3 analysis_findings Q7 |

---

## 2. Existing Inventory

<!-- register:existing_inventory -->
| FQDN | Action (REPLACE, REUSE, EXTEND, REVIEW) | Summary | Reason | Source Finding |
|------|------------------------------------------|---------|--------|----------------|
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | EXTEND | Refuses every declared refusal and moves the actor to its decided state | The one artifact this change touches. Its fifth step writes a whole record where it must change part of one. | S6 pps_artifacts_requiring_action blockchain::CC_RECORD_VERIFICATION_DECISION_V0 |
| capability_side_effects::CS_MUTABLE_JSON_V0 | REUSE | The keyed store, publishing a keyed write, a keyed update and a filtered update. | Reused unchanged. A different operation of the same capability is called, which is a choice the contract makes and not a change to the capability. | S6 cross_subdomain_deps Changing part of a held record without replacing it |
| blockchain::RB_IDENTITY_BINDINGS_V0 | REUSE | Binds identity's workflows to the side effects and storage they use. | Reused unchanged; it binds the capability, not the operation. | S6 pps_artifacts_requiring_action blockchain::RB_IDENTITY_BINDINGS_V0 |
| blockchain::STRUCTURE_IDENTITY_STORAGE_V0 | REUSE | Declares the stores identity owns, including the actor store. | Reused unchanged; the store, its path and its declaration are untouched. | S6 pps_artifacts_requiring_action blockchain::STRUCTURE_IDENTITY_STORAGE_V0 |
| blockchain::CC_RESOLVE_ACTOR_V0 | REVIEW | Resolves a contact address to an actor and reads the record whole. | Untouched, and the only reader of the store. What it reads will start carrying fields a decision had been stripping; it asserts nothing about the record's shape, so it is safe and still wants a look. | S6 pps_artifacts_requiring_action blockchain::CC_RESOLVE_ACTOR_V0 |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | REUSE | The governed sequence that records an authority's decision. | Composes the amended contract and routes on a result status this change preserves. Not itself amended. | S6 pps_artifacts_requiring_action blockchain::WF_RECORD_VERIFICATION_DECISION_V0 |
| blockchain::TI_ACCEPT_ACTOR_V0 | REUSE | Admits a request to accept a registered actor. | Names the workflow, not the contract. Unchanged. | S6 pps_artifacts_requiring_action blockchain::TI_ACCEPT_ACTOR_V0 |
| blockchain::TI_REJECT_ACTOR_V0 | REUSE | Admits a request to reject a registered actor. | The same. | S6 pps_artifacts_requiring_action blockchain::TI_REJECT_ACTOR_V0 |
| blockchain::IN_ACTOR_VERIFIED_V0 | REUSE | The request that starts the act of recording a decision. | Reached unchanged; named so the topology this change restates is complete rather than partial. | S3 analysis_findings Q7 |
| blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | REUSE | Appends one occurrence to the trail. | Reached unchanged; the trail is unchanged by constraint. | S3 analysis_findings Q1 |
| capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 | REUSE | Reads a supplied value against a declared admitted set. | Reached unchanged by two of the contract's steps. | S3 analysis_findings Q1 |
| capability_transforms::CT_PURE_COMPARE_EQUAL_V0 | REUSE | Compares two supplied values. | Reached unchanged by the contract's third step. | S3 analysis_findings Q1 |
| capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | REUSE | Assembles a record from supplied fields. | Reached unchanged by the contract's fourth step, whose output now feeds the update. | S3 analysis_findings Q5 |

---

## 3. New Artifacts

<!-- register:new_artifacts -->
| Capability | Family | Code | Summary | Owner Subdomain | Status | Source Finding |
|------------|--------|------|---------|-----------------|--------|----------------|

---

## 4. Runtime Binding Declarations

<!-- register:rb_declarations -->
| RB Code | Binds WF | CS Bindings | Storage Structure | Source Finding |
|---------|----------|-------------|-------------------|----------------|
| blockchain::RB_IDENTITY_BINDINGS_V0 | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | Unchanged by this change; the capability the corrected step calls is already bound | blockchain::STRUCTURE_IDENTITY_STORAGE_V0 | S6 pps_artifacts_requiring_action blockchain::RB_IDENTITY_BINDINGS_V0 |

---

## 5. Execution Topology

<!-- register:execution_topology -->
| Workflow | Node | Node Type | Routing | Source Finding |
|----------|------|-----------|---------|----------------|
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | blockchain::IN_ACTOR_VERIFIED_V0 | IN | ACK -> blockchain::CC_RESOLVE_ACTOR_V0; NACK -> EXIT_REJECTED | S6 pps_artifacts_requiring_action blockchain::WF_RECORD_VERIFICATION_DECISION_V0 |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | blockchain::CC_RESOLVE_ACTOR_V0 | CC | SUCCESS -> blockchain::CC_RECORD_VERIFICATION_DECISION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action blockchain::CC_RESOLVE_ACTOR_V0 |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | CC | SUCCESS -> blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0; VIOLATION -> EXIT_REJECTED | S6 pps_artifacts_requiring_action blockchain::WF_RECORD_VERIFICATION_DECISION_V0 |

---

## 6. Capability Contract Composition

<!-- register:cc_composition optional -->
| CC Code | Step | Step Name | Capability | Kind | Operation | Store | Consumes | Produces | Routing | Interpreted By | Semantic Status | Interface |
|---------|------|-----------|------------|------|-----------|-------|----------|----------|---------|----------------|-----------------|-----------|
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | 1 | read_state_admits_decision | capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 | CT | VALIDATE_SET_MEMBERSHIP | — | value, allowed_set | is_member | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: value=value, allowed_set=allowed_set; out: is_member=is_member |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | 2 | read_outcome_admitted | capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 | CT | VALIDATE_SET_MEMBERSHIP | — | value, allowed_set | is_member | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: value=value, allowed_set=allowed_set; out: is_member=is_member |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | 3 | refuse_self_verification | capability_transforms::CT_PURE_COMPARE_EQUAL_V0 | CT | COMPARE_EQUAL | — | left, right | is_equal | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: left=left, right=right; out: is_equal=is_equal |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | 4 | assemble_decided_actor | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | CT | ASSEMBLE_RECORD | — | fields | record | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: fields=fields; out: record=record |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | 5 | write_decided_actor | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | UPDATE | ACTORS | key, updates | result_status | SUCCESS -> continue; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | — |
---

## 7. Step Bindings

<!-- register:step_bindings optional -->
| Owner | Step | Direction | Field | Bound To | Source Finding |
|-------|------|-----------|-------|----------|----------------|
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
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | write_decided_actor | INPUT | updates | results.assemble_decided_actor.record | S7 cc_composition write_decided_actor |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | write_decided_actor | OUTPUT | result_status | result_status | S7 cc_composition write_decided_actor |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | current_state | results.CC_RESOLVE_ACTOR_V0.value.state | S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0 |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | states_admitting_a_decision | payload.states_admitting_a_decision | S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0 |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | decision | payload.decision | S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0 |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | admitted_outcomes | payload.admitted_outcomes | S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0 |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | verifying_authority | payload.verifying_authority | S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0 |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | contact_address | payload.contact_address | S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0 |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | decided_actor_fields | payload.decided_actor_fields | S7 execution_topology blockchain::CC_RECORD_VERIFICATION_DECISION_V0 |
---

## 8. Interface Fields

<!-- register:interface_fields optional -->
| Artifact | Direction | Field | Type | Required | Default | Meaning |
|----------|-----------|-------|------|----------|---------|---------|
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | current_state | string | YES |  | The state the person is in when the decision is recorded. |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | states_admitting_a_decision | array | YES |  | The states from which a decision may be recorded. |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | decision | string | YES |  | The outcome the authority states. |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | admitted_outcomes | array | YES |  | The outcomes a decision may carry. |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | verifying_authority | string | YES |  | The authority recording the decision. |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | contact_address | string | YES |  | Whose record the decision is recorded against, and the key that identifies it. |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | INPUT | decided_actor_fields | object | YES |  | The fields a decision sets. What is absent from it is what a decision may not change. |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | OUTPUT | result_status | string | YES |  | Whether the decision was recorded, refused, or failed in the store. |

---

## 9. Implementation Bindings

<!-- register:implementation_bindings optional -->
| CT Code | Module | Callable | Operation | Kind (atom, molecule) | Purity (ct_pure, ct_impure) | Source Finding |
|---------|--------|----------|-----------|------------------------|-----------------------------|----------------|

---

## 10. Vocabulary Extensions

<!-- register:vocabulary_extensions optional -->
| Vocabulary Code | Extends | Value | Meaning | Source Finding |
|-----------------|---------|-------|---------|----------------|

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
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | summary | Refuses every declared refusal and moves the actor to its decided state — carried unchanged, because an amendment states what the artifact is and not what the change did to it | S3 analysis_findings Q1 |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | result_status_contract.allowed | VIOLATION, SUCCESS, BACKEND_ERROR | S3 analysis_findings Q7 |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | result_status_contract.on_input_failure | VIOLATION | S3 analysis_findings Q7 |

---

## 13. Structure Stores

<!-- register:structure_stores optional -->
| Store Name | Storage Type | Proposed Path | Used By | Source Finding |
|------------|--------------|---------------|---------|----------------|

---

## 14. Transport Bindings

<!-- register:transport_bindings optional -->
| Artifact | Direction | Operation | Handler Kind | Handler Target | Field | Bound To | Source Finding |
|----------|-----------|-----------|--------------|----------------|-------|----------|----------------|

---

## 15. Artifact Summary

<!-- register:artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Subdomain | Count | Artifacts |
|-------------------------------|-----------|-------|-----------|
| EXTEND | identity | 1 | 1 CC |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | Purpose, scope, invariants, actions | COMPLETE |
| Stage 6 — Governance Intent | Ownership, dependencies, boundary rules | COMPLETE |
| Stage 7 — Design Intent | This document | COMPLETE |

---

## gov_projection — Governed Handoff to Stage 8

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 6 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
| **Emits** → Stage 8 | design_resolution · existing_inventory · new_artifacts · cc_composition · step_bindings · interface_fields · artifact_properties · artifact_summary |
