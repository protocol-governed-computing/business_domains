# Stage 6 — Governance Intent: blockchain / identity

**Stage:** 6 — Governance Intent
**CR:** cr_02_identity
**Status:** DRAFT
**Feeds:** Stage 7 — Design Intent

Placement of everything this change offers. The acts being reached already exist and are owned where
they were owned; what is placed here is the door, and it is placed with the function whose acts it
admits. Two capabilities are satisfied by artifacts already in the composition, and one obligation
belongs to a subdomain that is not this one.

---

## 1. Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Offer registering an actor to a caller outside the business | identity | OWNED |  | S5 scope_boundary Offer registering an actor to a caller outside the business |
| Offer recording a verification decision to a caller outside the business | identity | OWNED |  | S5 scope_boundary Offer recording a verification decision to a caller outside the business |
| Hold what an act requires and a caller must not send | identity | OWNED |  | S5 scope_boundary Hold what an act requires and a caller must not send |
| Tell a caller how their registration ended | identity | OWNED |  | S5 scope_boundary Tell a caller how their registration ended |
| Tell a caller how their decision ended | identity | OWNED |  | S5 scope_boundary Tell a caller how their decision ended |
| Declare where the boundary declarations are found | identity | OWNED |  | S5 scope_boundary Declare where the boundary declarations are found |
| Show a person a form and its answer | identity | OWNED |  | S5 scope_boundary Show a person a form and its answer |
| Carry a detail from one page to the next | identity | OWNED |  | S5 scope_boundary Carry a detail from one page to the next |
| Show the functions the business has not built | identity | OWNED |  | S5 scope_boundary Show the functions the business has not built |
| Admit a person's registration | identity | SATISFIED | blockchain::WF_REGISTER_ACTOR_V0 | S4 capability_graph Admit a person's registration |
| Record an authority's decision | identity | SATISFIED | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | S4 capability_graph Record an authority's decision |
| Read a registration for absent or malformed details | identity | SATISFIED | blockchain::CC_VALIDATE_REGISTRATION_V0 | S4 capability_graph Read a registration for absent or malformed details |
| Offer both acts through one way in | identity | SATISFIED | fb.transport::CONSTITUTION_TRANSPORT_INGRESS_V0 | S4 capability_graph Offer both acts through one way in |
| Announce the moments an actor is registered, accepted and rejected | construction — how artifacts are rendered, not identity | DEFERRED |  | S5 scope_boundary Announce the moments an actor is registered, accepted and rejected |
| Hold what an act requires with the act that requires it | identity, in a later change | DEFERRED |  | S5 scope_boundary Hold what an act requires with the act that requires it |
| Establishing who a caller is, and what they are allowed to do | identity, in a later change | DEFERRED |  | S5 scope_boundary Establishing who a caller is, and what they are allowed to do |
| Looking up an actor from outside | identity, in a later change | DEFERRED |  | S5 scope_boundary Looking up an actor from outside |
| Telling a person anything after they leave the page | identity, in a later change | DEFERRED |  | S5 scope_boundary Telling a person anything after they leave the page |
| A way in for wallet, transaction, mempool, block, chain and consensus | the subdomain of each function, when it is built | DEFERRED |  | S5 scope_boundary A way in for wallet, transaction, mempool, block, chain and consensus |
| A kind of answer for an act that ran and refused | the platform's transport governance, not this domain | DEFERRED |  | S5 scope_boundary A kind of answer for an act that ran and refused |

---

## 2. Storage Governance

<!-- register:storage_governance business_language=storage_need,purpose -->
| Storage Need | Purpose | Subdomain | Source Finding |
|--------------|---------|-----------|----------------|
| NONE IDENTIFIED — this change stores nothing | A request is answered and not kept, and an answer is composed for one caller and not kept. The three stores identity owns are declared by the previous change and are neither extended nor read differently, because the acts that use them are unchanged | identity | S5 business_objects |

---

## 3. Cross-Subdomain Dependencies

<!-- register:cross_subdomain_deps optional -->
| Dependency | Direction | Existing Artifact | Status (SATISFIED, GAP) | Source Finding |
|------------|-----------|-------------------|-------------------------|----------------|
| The governed kind that admits a request from outside | identity -> platform | fb.transport::CONSTITUTION_TRANSPORT_INGRESS_V0 | SATISFIED | S4 dependency_graph fb.transport::CONSTITUTION_TRANSPORT_INGRESS_V0 |
| The governed kind that states what a caller is told | identity -> platform | fb.transport::CONSTITUTION_TRANSPORT_EGRESS_V0 | SATISFIED | S4 dependency_graph fb.transport::CONSTITUTION_TRANSPORT_EGRESS_V0 |
| Reading a record for absence and for form | identity -> platform | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | SATISFIED | S4 dependency_graph capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 |
| The worked precedent for naming an act and holding what a caller does not send | identity -> workload | workload::TI_COLLATZ_COMPUTE_V0 | SATISFIED | S4 dependency_graph workload::TI_COLLATZ_COMPUTE_V0 |
| The worked precedent for classifying an ending and exposing evidence by reference | identity -> workload | workload::TE_COLLATZ_COMPUTE_V0 | SATISFIED | S4 dependency_graph workload::TE_COLLATZ_COMPUTE_V0 |

---

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE, EXTEND) | Source Finding |
|------|----------------|----------------------------------|----------------|
| blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 | Present; admits both boundary kinds among its artifact types while declaring no source layer they could be found in | EXTEND | S4 dependency_graph blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | Present and reached unchanged; named by a new boundary declaration and impacted by nothing | REUSE | S4 dependency_graph blockchain::WF_REGISTER_ACTOR_V0 |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | Present and reached unchanged; named by a new boundary declaration and impacted by nothing | REUSE | S4 dependency_graph blockchain::WF_RECORD_VERIFICATION_DECISION_V0 |
| blockchain::CC_VALIDATE_REGISTRATION_V0 | Present and reached unchanged through the act; the declaration it validates against is now held at the boundary rather than supplied by whoever calls | REVIEW | S4 dependency_graph blockchain::CC_VALIDATE_REGISTRATION_V0 |
| blockchain::AC_PARTICIPANT_V0 | Present and reused unchanged; a caller from outside is not established to be this or any actor | REUSE | S4 dependency_graph blockchain::AC_PARTICIPANT_V0 |
| capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | Present and reused unchanged; impacted by 31 artifacts | REUSE | S4 dependency_graph capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| THE_DOOR_IS_OWNED_BY_THE_FUNCTION | The declaration that offers an act belongs to the subdomain that owns the act. No subdomain offers another's acts, and no separate surface owns the names of acts it does not perform. | S3 placement_decision EXTEND |
| A_NAME_IS_NOT_AN_ACT | The public name of an act is declared apart from the act it reaches, and no caller may name an act by the thing that performs it. Re-pointing an act may not change what a caller sends or what they are told. | S4 design_decisions #2 |
| ONE_WAY_IN_MANY_NAMES | Both acts are reached through one way in, and the request names the act. Adding a function later adds a name and never a place. | S4 design_decisions #1 |
| ONLY_READABILITY_IS_JUDGED_AT_THE_DOOR | The door judges whether the business can read what was sent, and nothing else. Anything further is the act's own decision, made where it was always made. | S5 invariants A request whose details can be read is passed to the act, and nothing further is judged beforehand. |
| ONE_TEST_STATED_TWICE | What the door states a caller may send and what the act validates against name the same fields, and neither may be changed without the other. | S4 design_decisions #5 |
| THE_CALLER_SENDS_ONLY_THEIR_OWN | Nothing the business judges by may reach it from a caller. What an act requires and a caller must not send is held in the declaration that admits the request, sealed with it. | S4 design_decisions #3 |
| THE_PAGE_HOLDS_NO_RULE | No page validates, judges, or keeps a copy of what the business holds. What a page may hold is what the person has just typed, and no act of the business depends on it. | S5 invariants No business rule is held by the web page. |
| THE_ANSWER_KINDS_ARE_NOT_OURS | The kinds of answer a caller may be told are governed by the platform and closed. This subdomain declares which kind each ending takes and never invents a kind, and where a kind is rendered for one manner of access is settled outside this domain entirely. | S4 constraint_register #10 |
| NOTHING_DEPENDS_ON_AN_ANNOUNCEMENT | No artifact of this change is reached by the announcement of a moment. The three declared moments remain correct and unannounceable, and that is not a prerequisite of this change. | S4 design_decisions #8 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Offer registering an actor to a caller outside the business | identity | S6 ownership Offer registering an actor to a caller outside the business |
| Offer recording a verification decision to a caller outside the business | identity | S6 ownership Offer recording a verification decision to a caller outside the business |
| Hold what an act requires and a caller must not send | identity | S6 ownership Hold what an act requires and a caller must not send |
| Tell a caller how their registration ended | identity | S6 ownership Tell a caller how their registration ended |
| Tell a caller how their decision ended | identity | S6 ownership Tell a caller how their decision ended |
| Declare where the boundary declarations are found | identity | S6 ownership Declare where the boundary declarations are found |
| Show a person a form and its answer | identity | S6 ownership Show a person a form and its answer |
| Carry a detail from one page to the next | identity | S6 ownership Carry a detail from one page to the next |
| Show the functions the business has not built | identity | S6 ownership Show the functions the business has not built |

---

## gov_projection — Governed Handoff to Stage 7

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | subdomain_purpose · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
| **Emits** → Stage 7 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
