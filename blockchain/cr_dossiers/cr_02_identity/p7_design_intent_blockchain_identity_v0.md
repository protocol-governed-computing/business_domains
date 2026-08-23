# Stage 7 — Design Intent: blockchain / identity

**Stage:** 7 — Design Intent
**CR:** cr_02_identity
**Status:** DRAFT
**Feeds:** Stage 8 — Authoring Mandate

Six artifacts, all of them boundary declarations. No workflow, contract, transform, event, actor or
store is authored: the acts being offered already exist and are reached unchanged. What is designed
here is what a caller may name, what they may send, what is held for them, and what they are told.

---

## 1. Design Resolution

<!-- register:design_resolution -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|
| The decision act is offered as two named acts, one for acceptance and one for rejection. | The business holds a rejection to be its own occurrence, distinct in kind from an acceptance, and refuses to record one decision distinguished by a field. | Each act records a fixed occurrence — accepted or rejected — and a boundary declaration substitutes whole values and passes constants; it derives nothing. One act carrying the decision as a field would require the occurrence to be computed from it, which no declaration can do. Two acts each hold a constant, and the split follows what the business already records. | S5 provisional_codes blockchain::TI_ACCEPT_ACTOR_V0 |
| A workflow input may be the caller's own data or a constant, never a derivation of the caller's data. | The business asks that a caller send only their own details, and that what judges them is held by the business. | The deciding act takes an occurrence name derived from the decision. Nothing in the act computes it, so whoever assembles the payload does — a person, silently, when the caller was inside the business. Reached from outside there is no such person. Where the derived value has one possible value per act it is held as a constant here; where it does not, the derivation belongs inside the act, which is the change GAP-11 records. | S3 analysis_findings Q3 |
| The two preferences are not offered to a caller and are recorded at their declared defaults. | The business records a preferred currency and a preferred language for every actor, each having a default, so that nothing downstream must decide what an absent preference means. | The boundary applies no default — an optional field a caller omits is omitted from what the act receives, and the act supplies nothing in its place. Rather than admit an actor carrying no preference, the declarations hold both defaults as constants. A caller states no preference because the page does not ask; every actor still carries an answer. | S1 known_facts #28 |
| Grounds are optional on an acceptance and required on a rejection. | The business requires grounds for a rejection, where they are the substance of the decision, and permits their omission on an acceptance, where the decision is the statement. | Each act declares its own requirement, which is possible only because they are two declarations. Verified against the pinned snapshot: an acceptance carrying no grounds is admitted and records grounds as absent rather than failing. | S1 known_facts #19 |
| What a caller sends is named in the business's own terms, not the prior implementation's. | The business names an actor by their name and their contact address, and a decision by its authority and its grounds. | The pages are lifted from the prior implementation and their fields are replaced: what it called a first name, a last name and an email registration is one name and one contact address; what it called a verifier and notes is the verifying authority and the grounds. The form and the way it gathers what is typed survive; none of its names does. | S4 design_decisions #7 |

---

## 2. Existing Inventory

<!-- register:existing_inventory -->
| FQDN | Action (REPLACE, REUSE, EXTEND, REVIEW) | Summary | Reason | Source Finding |
|------|------------------------------------------|---------|--------|----------------|
| blockchain::WF_REGISTER_ACTOR_V0 | REUSE | The governed sequence that admits a person as an unverified actor. | Reached unchanged by a new boundary declaration. Nothing about the act is amended, and it is impacted by nothing in the composition. | S6 ownership Admit a person's registration |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | REUSE | The governed sequence that records an authority's decision against a registered actor. | Reached unchanged by two new boundary declarations, one for each outcome the business records. | S6 ownership Record an authority's decision |
| blockchain::CC_VALIDATE_REGISTRATION_V0 | REVIEW | Confirms a registration carries a name and an address of the form asked for. | Untouched, but the declaration it validates against is now supplied by a sealed boundary artifact rather than by whoever calls. Same contract, different provenance for its input. | S6 pps_artifacts_requiring_action blockchain::CC_VALIDATE_REGISTRATION_V0 |
| blockchain::AC_PARTICIPANT_V0 | REUSE | Declares the kind of party that performs identity's acts. | Reused unchanged. A caller from outside is not established to be this or any actor. | S6 pps_artifacts_requiring_action blockchain::AC_PARTICIPANT_V0 |
| blockchain::RB_IDENTITY_BINDINGS_V0 | REUSE | Binds identity's workflows to the stores they use. | Reused unchanged; the acts reached bind exactly as they did. | S6 ownership Admit a person's registration |
| blockchain::IN_ACTOR_REGISTERED_V0 | REUSE | The request that starts the act of admitting a person. | Reached unchanged; what a caller sends becomes this act's payload. | S6 ownership Admit a person's registration |
| blockchain::IN_ACTOR_VERIFIED_V0 | REUSE | The request that starts the act of recording a decision. | Reached unchanged by both decision declarations. | S6 ownership Record an authority's decision |
| capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | REUSE | Reads a supplied record for fields the declaration requires and for the form they must take. | Reused unchanged, reached through the act. Impacted by 31 artifacts. | S6 cross_subdomain_deps Reading a record for absence and for form |
| transport::CONSTITUTION_TRANSPORT_INGRESS_V0 | REUSE | Governs the kind that admits a request from outside. | Governs the three new ingress declarations; not amended. | S6 cross_subdomain_deps The governed kind that admits a request from outside |
| transport::CONSTITUTION_TRANSPORT_EGRESS_V0 | REUSE | Governs the kind that states what a caller is told, over a closed set of answer kinds. | Governs the three new egress declarations; not amended, and its closed set is not extended. | S6 cross_subdomain_deps The governed kind that states what a caller is told |
| workload::TI_COLLATZ_COMPUTE_V0 | REUSE | The worked precedent for a public name, a declared caller input and a template holding what a caller does not send. | Read, not changed. | S6 cross_subdomain_deps The worked precedent for naming an act and holding what a caller does not send |
| workload::TE_COLLATZ_COMPUTE_V0 | REUSE | The worked precedent for classifying an ending and exposing evidence by reference. | Read, not changed. | S6 cross_subdomain_deps The worked precedent for classifying an ending and exposing evidence by reference |

---

## 3. New Artifacts

<!-- register:new_artifacts -->
| Capability | Family | Code | Summary | Owner Subdomain | Status | Source Finding |
|------------|--------|------|---------|-----------------|--------|----------------|
| Offer registering an actor to a caller outside the business | TI | blockchain::TI_REGISTER_ACTOR_V0 | Admits a request to register an actor, declaring the name and contact address a caller sends and holding the schema, address path, stream, preferences and occurrence label the act requires. | identity | NEW | S5 provisional_codes blockchain::TI_REGISTER_ACTOR_V0 |
| Tell a caller how their registration ended | TE | blockchain::TE_REGISTER_ACTOR_V0 | Classifies the endings of registering an actor and projects the contact address, the occurrence, its time and its position. | identity | NEW | S5 provisional_codes blockchain::TE_REGISTER_ACTOR_V0 |
| Offer recording a verification decision to a caller outside the business | TI | blockchain::TI_ACCEPT_ACTOR_V0 | Admits a request to accept a registered actor, declaring the contact address, authority and optional grounds a caller sends and holding the decision, admitted states and outcomes, and the acceptance occurrence label. | identity | NEW | S5 provisional_codes blockchain::TI_ACCEPT_ACTOR_V0 |
| Tell a caller how their decision ended | TE | blockchain::TE_ACCEPT_ACTOR_V0 | Classifies the endings of accepting an actor, including the actor that does not exist, and projects what was recorded. | identity | NEW | S5 provisional_codes blockchain::TE_ACCEPT_ACTOR_V0 |
| Offer recording a verification decision to a caller outside the business | TI | blockchain::TI_REJECT_ACTOR_V0 | Admits a request to reject a registered actor, declaring the contact address, authority and required grounds a caller sends and holding the decision, admitted states and outcomes, and the rejection occurrence label. | identity | NEW | S5 provisional_codes blockchain::TI_REJECT_ACTOR_V0 |
| Tell a caller how their decision ended | TE | blockchain::TE_REJECT_ACTOR_V0 | Classifies the endings of rejecting an actor, including the actor that does not exist, and projects what was recorded. | identity | NEW | S5 provisional_codes blockchain::TE_REJECT_ACTOR_V0 |

---

## 4. Runtime Binding Declarations

<!-- register:rb_declarations -->
| RB Code | Binds WF | CS Bindings | Storage Structure | Source Finding |
|---------|----------|-------------|-------------------|----------------|
| blockchain::RB_IDENTITY_BINDINGS_V0 | blockchain::WF_REGISTER_ACTOR_V0 | Unchanged by this change | Unchanged by this change | S6 ownership Admit a person's registration |
| blockchain::RB_IDENTITY_BINDINGS_V0 | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | Unchanged by this change | Unchanged by this change | S6 ownership Record an authority's decision |

---

## 5. Execution Topology

<!-- register:execution_topology -->
| Workflow | Node | Node Type | Routing | Source Finding |
|----------|------|-----------|---------|----------------|
| blockchain::WF_REGISTER_ACTOR_V0 | blockchain::IN_ACTOR_REGISTERED_V0 | IN | Unchanged by this change; what a caller sends becomes this act's payload and the act routes as it already does | S6 ownership Admit a person's registration |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | blockchain::IN_ACTOR_VERIFIED_V0 | IN | Unchanged by this change; both decision declarations reach this same entry, differing only in what they hold | S6 ownership Record an authority's decision |

---

## 6. Capability Contract Composition

<!-- register:cc_composition optional -->
| CC Code | Step | Step Name | Capability | Kind | Operation | Store | Consumes | Produces | Routing | Interpreted By | Semantic Status | Interface |
|---------|------|-----------|------------|------|-----------|-------|----------|----------|---------|----------------|-----------------|-----------|

---

## 7. Step Bindings

<!-- register:step_bindings optional -->
| Owner | Step | Direction | Field | Bound To | Source Finding |
|-------|------|-----------|-------|----------|----------------|

---

## 8. Interface Fields

<!-- register:interface_fields optional -->
| Artifact | Direction | Field | Type | Required | Default | Meaning |
|----------|-----------|-------|------|----------|---------|---------|
| blockchain::TI_REGISTER_ACTOR_V0 | INPUT | name | string | YES |  | What the person is called, supplied by them. |
| blockchain::TI_REGISTER_ACTOR_V0 | INPUT | contact_address | string | YES |  | The address the person registers with, which is what identifies them as an actor. |
| blockchain::TE_REGISTER_ACTOR_V0 | OUTPUT | contact_address | string | YES |  | The address the actor was admitted under. |
| blockchain::TE_REGISTER_ACTOR_V0 | OUTPUT | occurrence | string | YES |  | Which moment was recorded. |
| blockchain::TE_REGISTER_ACTOR_V0 | OUTPUT | occurred_at | string | YES |  | The time the occurrence happened, determined as it occurred. |
| blockchain::TE_REGISTER_ACTOR_V0 | OUTPUT | sequence_number | integer | YES |  | The position at which the occurrence was written to the trail. |
| blockchain::TI_ACCEPT_ACTOR_V0 | INPUT | contact_address | string | YES |  | The actor being accepted. |
| blockchain::TI_ACCEPT_ACTOR_V0 | INPUT | verifying_authority | string | YES |  | The authority recording the acceptance. Recorded as named and never resolved. |
| blockchain::TI_ACCEPT_ACTOR_V0 | INPUT | grounds | string | NO |  | The reason stated. Optional on an acceptance, where the decision is itself the statement. |
| blockchain::TE_ACCEPT_ACTOR_V0 | OUTPUT | contact_address | string | YES |  | The actor the decision was recorded against. |
| blockchain::TE_ACCEPT_ACTOR_V0 | OUTPUT | occurrence | string | YES |  | Which moment was recorded. |
| blockchain::TE_ACCEPT_ACTOR_V0 | OUTPUT | verifying_authority | string | YES |  | The authority the record names. |
| blockchain::TE_ACCEPT_ACTOR_V0 | OUTPUT | grounds | string | NO |  | The grounds recorded, absent when none were stated. |
| blockchain::TE_ACCEPT_ACTOR_V0 | OUTPUT | occurred_at | string | YES |  | The time the decision was recorded. |
| blockchain::TE_ACCEPT_ACTOR_V0 | OUTPUT | sequence_number | integer | YES |  | The position at which the occurrence was written to the trail. |
| blockchain::TI_REJECT_ACTOR_V0 | INPUT | contact_address | string | YES |  | The actor being rejected. |
| blockchain::TI_REJECT_ACTOR_V0 | INPUT | verifying_authority | string | YES |  | The authority recording the rejection. Recorded as named and never resolved. |
| blockchain::TI_REJECT_ACTOR_V0 | INPUT | grounds | string | YES |  | The reason stated. Required on a rejection, where the grounds are the substance of the decision. |
| blockchain::TE_REJECT_ACTOR_V0 | OUTPUT | contact_address | string | YES |  | The actor the decision was recorded against. |
| blockchain::TE_REJECT_ACTOR_V0 | OUTPUT | occurrence | string | YES |  | Which moment was recorded. |
| blockchain::TE_REJECT_ACTOR_V0 | OUTPUT | verifying_authority | string | YES |  | The authority the record names. |
| blockchain::TE_REJECT_ACTOR_V0 | OUTPUT | grounds | string | YES |  | The grounds stated for the rejection. |
| blockchain::TE_REJECT_ACTOR_V0 | OUTPUT | occurred_at | string | YES |  | The time the decision was recorded. |
| blockchain::TE_REJECT_ACTOR_V0 | OUTPUT | sequence_number | integer | YES |  | The position at which the occurrence was written to the trail. |

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
| blockchain::TI_REGISTER_ACTOR_V0 | governed_by | transport::CONSTITUTION_TRANSPORT_INGRESS_V0 | S6 cross_subdomain_deps The governed kind that admits a request from outside |
| blockchain::TI_ACCEPT_ACTOR_V0 | governed_by | transport::CONSTITUTION_TRANSPORT_INGRESS_V0 | S6 cross_subdomain_deps The governed kind that admits a request from outside |
| blockchain::TI_REJECT_ACTOR_V0 | governed_by | transport::CONSTITUTION_TRANSPORT_INGRESS_V0 | S6 cross_subdomain_deps The governed kind that admits a request from outside |
| blockchain::TI_REGISTER_ACTOR_V0 | context_requirements | none — the boundary requires no context of a caller, and this change establishes nothing about who they are | S6 ownership Establishing who a caller is, and what they are allowed to do |
| blockchain::TI_ACCEPT_ACTOR_V0 | context_requirements | none — the boundary requires no context of a caller, and this change establishes nothing about who they are | S6 ownership Establishing who a caller is, and what they are allowed to do |
| blockchain::TI_REJECT_ACTOR_V0 | context_requirements | none — the boundary requires no context of a caller, and this change establishes nothing about who they are | S6 ownership Establishing who a caller is, and what they are allowed to do |
| blockchain::TE_REGISTER_ACTOR_V0 | governed_by | transport::CONSTITUTION_TRANSPORT_EGRESS_V0 | S6 cross_subdomain_deps The governed kind that states what a caller is told |
| blockchain::TE_ACCEPT_ACTOR_V0 | governed_by | transport::CONSTITUTION_TRANSPORT_EGRESS_V0 | S6 cross_subdomain_deps The governed kind that states what a caller is told |
| blockchain::TE_REJECT_ACTOR_V0 | governed_by | transport::CONSTITUTION_TRANSPORT_EGRESS_V0 | S6 cross_subdomain_deps The governed kind that states what a caller is told |
| blockchain::TE_REGISTER_ACTOR_V0 | result_class.SUCCESS | SUCCESS | S6 boundary_rules THE_ANSWER_KINDS_ARE_NOT_OURS |
| blockchain::TE_REGISTER_ACTOR_V0 | result_class.VIOLATION | VIOLATION | S6 boundary_rules THE_ANSWER_KINDS_ARE_NOT_OURS |
| blockchain::TE_REGISTER_ACTOR_V0 | result_class.NOT_FOUND | NOT_FOUND | S6 boundary_rules THE_ANSWER_KINDS_ARE_NOT_OURS |
| blockchain::TE_ACCEPT_ACTOR_V0 | result_class.SUCCESS | SUCCESS | S6 boundary_rules THE_ANSWER_KINDS_ARE_NOT_OURS |
| blockchain::TE_ACCEPT_ACTOR_V0 | result_class.VIOLATION | VIOLATION | S6 boundary_rules THE_ANSWER_KINDS_ARE_NOT_OURS |
| blockchain::TE_ACCEPT_ACTOR_V0 | result_class.NOT_FOUND | NOT_FOUND | S6 boundary_rules THE_ANSWER_KINDS_ARE_NOT_OURS |
| blockchain::TE_REJECT_ACTOR_V0 | result_class.SUCCESS | SUCCESS | S6 boundary_rules THE_ANSWER_KINDS_ARE_NOT_OURS |
| blockchain::TE_REJECT_ACTOR_V0 | result_class.VIOLATION | VIOLATION | S6 boundary_rules THE_ANSWER_KINDS_ARE_NOT_OURS |
| blockchain::TE_REJECT_ACTOR_V0 | result_class.NOT_FOUND | NOT_FOUND | S6 boundary_rules THE_ANSWER_KINDS_ARE_NOT_OURS |
| blockchain::TE_REGISTER_ACTOR_V0 | default_result_class | EXECUTION_FAILURE | S6 boundary_rules THE_ANSWER_KINDS_ARE_NOT_OURS |
| blockchain::TE_ACCEPT_ACTOR_V0 | default_result_class | EXECUTION_FAILURE | S6 boundary_rules THE_ANSWER_KINDS_ARE_NOT_OURS |
| blockchain::TE_REJECT_ACTOR_V0 | default_result_class | EXECUTION_FAILURE | S6 boundary_rules THE_ANSWER_KINDS_ARE_NOT_OURS |
| blockchain::TE_REGISTER_ACTOR_V0 | evidence_policy | reference_only | S4 design_decisions #6 |
| blockchain::TE_ACCEPT_ACTOR_V0 | evidence_policy | reference_only | S4 design_decisions #6 |
| blockchain::TE_REJECT_ACTOR_V0 | evidence_policy | reference_only | S4 design_decisions #6 |

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
| blockchain::TI_REGISTER_ACTOR_V0 | INGRESS | blockchain.register_actor | WF_INVOCATION | blockchain::WF_REGISTER_ACTOR_V0 | actor_record.name | ${input.name} | S7 interface_fields blockchain::TI_REGISTER_ACTOR_V0 name |
| blockchain::TI_REGISTER_ACTOR_V0 | INGRESS | blockchain.register_actor | WF_INVOCATION | blockchain::WF_REGISTER_ACTOR_V0 | actor_record.contact_address | ${input.contact_address} | S7 interface_fields blockchain::TI_REGISTER_ACTOR_V0 contact_address |
| blockchain::TI_REGISTER_ACTOR_V0 | INGRESS | blockchain.register_actor | WF_INVOCATION | blockchain::WF_REGISTER_ACTOR_V0 | actor_record.state | UNVERIFIED | S7 design_resolution The two preferences are not offered to a caller and are recorded at their declared defaults. |
| blockchain::TI_REGISTER_ACTOR_V0 | INGRESS | blockchain.register_actor | WF_INVOCATION | blockchain::WF_REGISTER_ACTOR_V0 | actor_record.currency_preference | BACHI | S7 design_resolution The two preferences are not offered to a caller and are recorded at their declared defaults. |
| blockchain::TI_REGISTER_ACTOR_V0 | INGRESS | blockchain.register_actor | WF_INVOCATION | blockchain::WF_REGISTER_ACTOR_V0 | actor_record.language | en | S7 design_resolution The two preferences are not offered to a caller and are recorded at their declared defaults. |
| blockchain::TI_REGISTER_ACTOR_V0 | INGRESS | blockchain.register_actor | WF_INVOCATION | blockchain::WF_REGISTER_ACTOR_V0 | registration_schema.name.required | true | S6 boundary_rules ONE_TEST_STATED_TWICE |
| blockchain::TI_REGISTER_ACTOR_V0 | INGRESS | blockchain.register_actor | WF_INVOCATION | blockchain::WF_REGISTER_ACTOR_V0 | registration_schema.name.type | string | S6 boundary_rules ONE_TEST_STATED_TWICE |
| blockchain::TI_REGISTER_ACTOR_V0 | INGRESS | blockchain.register_actor | WF_INVOCATION | blockchain::WF_REGISTER_ACTOR_V0 | registration_schema.contact_address.required | true | S6 boundary_rules ONE_TEST_STATED_TWICE |
| blockchain::TI_REGISTER_ACTOR_V0 | INGRESS | blockchain.register_actor | WF_INVOCATION | blockchain::WF_REGISTER_ACTOR_V0 | registration_schema.contact_address.type | string | S6 boundary_rules ONE_TEST_STATED_TWICE |
| blockchain::TI_REGISTER_ACTOR_V0 | INGRESS | blockchain.register_actor | WF_INVOCATION | blockchain::WF_REGISTER_ACTOR_V0 | address_path | contact_address | S6 boundary_rules THE_CALLER_SENDS_ONLY_THEIR_OWN |
| blockchain::TI_REGISTER_ACTOR_V0 | INGRESS | blockchain.register_actor | WF_INVOCATION | blockchain::WF_REGISTER_ACTOR_V0 | address_type | string | S6 boundary_rules THE_CALLER_SENDS_ONLY_THEIR_OWN |
| blockchain::TI_REGISTER_ACTOR_V0 | INGRESS | blockchain.register_actor | WF_INVOCATION | blockchain::WF_REGISTER_ACTOR_V0 | stream_id | ACTOR_OCCURRENCES | S6 boundary_rules THE_CALLER_SENDS_ONLY_THEIR_OWN |
| blockchain::TI_REGISTER_ACTOR_V0 | INGRESS | blockchain.register_actor | WF_INVOCATION | blockchain::WF_REGISTER_ACTOR_V0 | occurrence_fields.occurrence | ACTOR_REGISTERED_UNVERIFIED | S6 boundary_rules THE_CALLER_SENDS_ONLY_THEIR_OWN |
| blockchain::TI_REGISTER_ACTOR_V0 | INGRESS | blockchain.register_actor | WF_INVOCATION | blockchain::WF_REGISTER_ACTOR_V0 | occurrence_fields.contact_address | ${input.contact_address} | S7 interface_fields blockchain::TI_REGISTER_ACTOR_V0 contact_address |
| blockchain::TE_REGISTER_ACTOR_V0 | EGRESS | blockchain.register_actor | WF_INVOCATION | blockchain::WF_REGISTER_ACTOR_V0 | contact_address | surface.contact_address | S7 interface_fields blockchain::TE_REGISTER_ACTOR_V0 contact_address |
| blockchain::TE_REGISTER_ACTOR_V0 | EGRESS | blockchain.register_actor | WF_INVOCATION | blockchain::WF_REGISTER_ACTOR_V0 | occurrence | surface.record.occurrence | S7 interface_fields blockchain::TE_REGISTER_ACTOR_V0 occurrence |
| blockchain::TE_REGISTER_ACTOR_V0 | EGRESS | blockchain.register_actor | WF_INVOCATION | blockchain::WF_REGISTER_ACTOR_V0 | occurred_at | surface.record.occurred_at | S7 interface_fields blockchain::TE_REGISTER_ACTOR_V0 occurred_at |
| blockchain::TE_REGISTER_ACTOR_V0 | EGRESS | blockchain.register_actor | WF_INVOCATION | blockchain::WF_REGISTER_ACTOR_V0 | sequence_number | surface.sequence_number | S7 interface_fields blockchain::TE_REGISTER_ACTOR_V0 sequence_number |
| blockchain::TI_ACCEPT_ACTOR_V0 | INGRESS | blockchain.accept_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | contact_address | ${input.contact_address} | S7 interface_fields blockchain::TI_ACCEPT_ACTOR_V0 contact_address |
| blockchain::TI_ACCEPT_ACTOR_V0 | INGRESS | blockchain.accept_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | verifying_authority | ${input.verifying_authority} | S7 interface_fields blockchain::TI_ACCEPT_ACTOR_V0 verifying_authority |
| blockchain::TI_ACCEPT_ACTOR_V0 | INGRESS | blockchain.accept_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | decision | ACCEPTED | S7 design_resolution The decision act is offered as two named acts, one for acceptance and one for rejection. |
| blockchain::TI_ACCEPT_ACTOR_V0 | INGRESS | blockchain.accept_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | grounds | ${input.grounds} | S7 interface_fields blockchain::TI_ACCEPT_ACTOR_V0 grounds |
| blockchain::TI_ACCEPT_ACTOR_V0 | INGRESS | blockchain.accept_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | states_admitting_a_decision | [UNVERIFIED] | S6 boundary_rules THE_CALLER_SENDS_ONLY_THEIR_OWN |
| blockchain::TI_ACCEPT_ACTOR_V0 | INGRESS | blockchain.accept_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | admitted_outcomes | [ACCEPTED, REJECTED] | S6 boundary_rules THE_CALLER_SENDS_ONLY_THEIR_OWN |
| blockchain::TI_ACCEPT_ACTOR_V0 | INGRESS | blockchain.accept_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | decided_actor_fields.contact_address | ${input.contact_address} | S7 interface_fields blockchain::TI_ACCEPT_ACTOR_V0 contact_address |
| blockchain::TI_ACCEPT_ACTOR_V0 | INGRESS | blockchain.accept_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | decided_actor_fields.state | ACCEPTED | S7 design_resolution The decision act is offered as two named acts, one for acceptance and one for rejection. |
| blockchain::TI_ACCEPT_ACTOR_V0 | INGRESS | blockchain.accept_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | decided_actor_fields.verifying_authority | ${input.verifying_authority} | S7 interface_fields blockchain::TI_ACCEPT_ACTOR_V0 verifying_authority |
| blockchain::TI_ACCEPT_ACTOR_V0 | INGRESS | blockchain.accept_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | decided_actor_fields.grounds | ${input.grounds} | S7 interface_fields blockchain::TI_ACCEPT_ACTOR_V0 grounds |
| blockchain::TI_ACCEPT_ACTOR_V0 | INGRESS | blockchain.accept_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | stream_id | ACTOR_OCCURRENCES | S6 boundary_rules THE_CALLER_SENDS_ONLY_THEIR_OWN |
| blockchain::TI_ACCEPT_ACTOR_V0 | INGRESS | blockchain.accept_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | occurrence_fields.occurrence | ACTOR_ACCEPTED | S7 design_resolution The decision act is offered as two named acts, one for acceptance and one for rejection. |
| blockchain::TI_ACCEPT_ACTOR_V0 | INGRESS | blockchain.accept_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | occurrence_fields.contact_address | ${input.contact_address} | S7 interface_fields blockchain::TI_ACCEPT_ACTOR_V0 contact_address |
| blockchain::TI_ACCEPT_ACTOR_V0 | INGRESS | blockchain.accept_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | occurrence_fields.verifying_authority | ${input.verifying_authority} | S7 interface_fields blockchain::TI_ACCEPT_ACTOR_V0 verifying_authority |
| blockchain::TI_ACCEPT_ACTOR_V0 | INGRESS | blockchain.accept_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | occurrence_fields.grounds | ${input.grounds} | S7 interface_fields blockchain::TI_ACCEPT_ACTOR_V0 grounds |
| blockchain::TE_ACCEPT_ACTOR_V0 | EGRESS | blockchain.accept_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | contact_address | surface.contact_address | S7 interface_fields blockchain::TE_ACCEPT_ACTOR_V0 contact_address |
| blockchain::TE_ACCEPT_ACTOR_V0 | EGRESS | blockchain.accept_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | occurrence | surface.record.occurrence | S7 interface_fields blockchain::TE_ACCEPT_ACTOR_V0 occurrence |
| blockchain::TE_ACCEPT_ACTOR_V0 | EGRESS | blockchain.accept_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | verifying_authority | surface.record.verifying_authority | S7 interface_fields blockchain::TE_ACCEPT_ACTOR_V0 verifying_authority |
| blockchain::TE_ACCEPT_ACTOR_V0 | EGRESS | blockchain.accept_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | grounds | surface.record.grounds | S7 interface_fields blockchain::TE_ACCEPT_ACTOR_V0 grounds |
| blockchain::TE_ACCEPT_ACTOR_V0 | EGRESS | blockchain.accept_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | occurred_at | surface.record.occurred_at | S7 interface_fields blockchain::TE_ACCEPT_ACTOR_V0 occurred_at |
| blockchain::TE_ACCEPT_ACTOR_V0 | EGRESS | blockchain.accept_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | sequence_number | surface.sequence_number | S7 interface_fields blockchain::TE_ACCEPT_ACTOR_V0 sequence_number |
| blockchain::TI_REJECT_ACTOR_V0 | INGRESS | blockchain.reject_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | contact_address | ${input.contact_address} | S7 interface_fields blockchain::TI_REJECT_ACTOR_V0 contact_address |
| blockchain::TI_REJECT_ACTOR_V0 | INGRESS | blockchain.reject_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | verifying_authority | ${input.verifying_authority} | S7 interface_fields blockchain::TI_REJECT_ACTOR_V0 verifying_authority |
| blockchain::TI_REJECT_ACTOR_V0 | INGRESS | blockchain.reject_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | decision | REJECTED | S7 design_resolution The decision act is offered as two named acts, one for acceptance and one for rejection. |
| blockchain::TI_REJECT_ACTOR_V0 | INGRESS | blockchain.reject_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | grounds | ${input.grounds} | S7 interface_fields blockchain::TI_REJECT_ACTOR_V0 grounds |
| blockchain::TI_REJECT_ACTOR_V0 | INGRESS | blockchain.reject_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | states_admitting_a_decision | [UNVERIFIED] | S6 boundary_rules THE_CALLER_SENDS_ONLY_THEIR_OWN |
| blockchain::TI_REJECT_ACTOR_V0 | INGRESS | blockchain.reject_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | admitted_outcomes | [ACCEPTED, REJECTED] | S6 boundary_rules THE_CALLER_SENDS_ONLY_THEIR_OWN |
| blockchain::TI_REJECT_ACTOR_V0 | INGRESS | blockchain.reject_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | decided_actor_fields.contact_address | ${input.contact_address} | S7 interface_fields blockchain::TI_REJECT_ACTOR_V0 contact_address |
| blockchain::TI_REJECT_ACTOR_V0 | INGRESS | blockchain.reject_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | decided_actor_fields.state | REJECTED | S7 design_resolution The decision act is offered as two named acts, one for acceptance and one for rejection. |
| blockchain::TI_REJECT_ACTOR_V0 | INGRESS | blockchain.reject_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | decided_actor_fields.verifying_authority | ${input.verifying_authority} | S7 interface_fields blockchain::TI_REJECT_ACTOR_V0 verifying_authority |
| blockchain::TI_REJECT_ACTOR_V0 | INGRESS | blockchain.reject_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | decided_actor_fields.grounds | ${input.grounds} | S7 interface_fields blockchain::TI_REJECT_ACTOR_V0 grounds |
| blockchain::TI_REJECT_ACTOR_V0 | INGRESS | blockchain.reject_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | stream_id | ACTOR_OCCURRENCES | S6 boundary_rules THE_CALLER_SENDS_ONLY_THEIR_OWN |
| blockchain::TI_REJECT_ACTOR_V0 | INGRESS | blockchain.reject_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | occurrence_fields.occurrence | ACTOR_REJECTED | S7 design_resolution The decision act is offered as two named acts, one for acceptance and one for rejection. |
| blockchain::TI_REJECT_ACTOR_V0 | INGRESS | blockchain.reject_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | occurrence_fields.contact_address | ${input.contact_address} | S7 interface_fields blockchain::TI_REJECT_ACTOR_V0 contact_address |
| blockchain::TI_REJECT_ACTOR_V0 | INGRESS | blockchain.reject_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | occurrence_fields.verifying_authority | ${input.verifying_authority} | S7 interface_fields blockchain::TI_REJECT_ACTOR_V0 verifying_authority |
| blockchain::TI_REJECT_ACTOR_V0 | INGRESS | blockchain.reject_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | occurrence_fields.grounds | ${input.grounds} | S7 interface_fields blockchain::TI_REJECT_ACTOR_V0 grounds |
| blockchain::TE_REJECT_ACTOR_V0 | EGRESS | blockchain.reject_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | contact_address | surface.contact_address | S7 interface_fields blockchain::TE_REJECT_ACTOR_V0 contact_address |
| blockchain::TE_REJECT_ACTOR_V0 | EGRESS | blockchain.reject_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | occurrence | surface.record.occurrence | S7 interface_fields blockchain::TE_REJECT_ACTOR_V0 occurrence |
| blockchain::TE_REJECT_ACTOR_V0 | EGRESS | blockchain.reject_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | verifying_authority | surface.record.verifying_authority | S7 interface_fields blockchain::TE_REJECT_ACTOR_V0 verifying_authority |
| blockchain::TE_REJECT_ACTOR_V0 | EGRESS | blockchain.reject_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | grounds | surface.record.grounds | S7 interface_fields blockchain::TE_REJECT_ACTOR_V0 grounds |
| blockchain::TE_REJECT_ACTOR_V0 | EGRESS | blockchain.reject_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | occurred_at | surface.record.occurred_at | S7 interface_fields blockchain::TE_REJECT_ACTOR_V0 occurred_at |
| blockchain::TE_REJECT_ACTOR_V0 | EGRESS | blockchain.reject_actor | WF_INVOCATION | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | sequence_number | surface.sequence_number | S7 interface_fields blockchain::TE_REJECT_ACTOR_V0 sequence_number |

---

## 15. Artifact Summary

<!-- register:artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Subdomain | Count | Artifacts |
|-------------------------------|-----------|-------|-----------|
| NEW | identity | 6 | 3 TI, 3 TE |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | Purpose, scope, invariants, actions, provisional codes | COMPLETE |
| Stage 6 — Governance Intent | Ownership, dependencies, boundary rules | COMPLETE |
| Stage 7 — Design Intent | This document | COMPLETE |

---

## gov_projection — Governed Handoff to Stage 8

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 6 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
| **Emits** → Stage 8 | design_resolution · existing_inventory · new_artifacts · interface_fields · artifact_properties · transport_bindings · artifact_summary |
