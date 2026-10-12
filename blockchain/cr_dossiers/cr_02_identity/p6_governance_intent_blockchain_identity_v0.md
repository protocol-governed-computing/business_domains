# Stage 6 — Governance Intent: blockchain / identity

## Machine

```yaml
document:
  phase: p6
  domain: blockchain
  subdomain: identity
  cr: cr_02_identity
  rule_set: transformation.schemas.REGISTER_SCHEMA_P6_V0
registers:
  ownership:
  - capability: Offer registering an actor to a caller outside the business
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Offer registering an actor to a caller outside the business}
  - capability: Offer recording a verification decision to a caller outside the business
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Offer recording a verification decision to a caller outside the business}
  - capability: Hold what an act requires and a caller must not send
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Hold what an act requires and a caller must not send}
  - capability: Tell a caller how their registration ended
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Tell a caller how their registration ended}
  - capability: Tell a caller how their decision ended
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Tell a caller how their decision ended}
  - capability: Declare where the boundary declarations are found
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Declare where the boundary declarations are found}
  - capability: Show a person a form and its answer
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Show a person a form and its answer}
  - capability: Carry a detail from one page to the next
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Carry a detail from one page to the next}
  - capability: Show the functions the business has not built
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Show the functions the business has not built}
  - capability: Admit a person's registration
    owner_subdomain: identity
    disposition: SATISFIED
    existing_artifact: blockchain::WF_REGISTER_ACTOR_V0
    source_finding: {phase: p4, register: capability_graph, key: Admit a person's registration}
  - capability: Record an authority's decision
    owner_subdomain: identity
    disposition: SATISFIED
    existing_artifact: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    source_finding: {phase: p4, register: capability_graph, key: Record an authority's decision}
  - capability: Read a registration for absent or malformed details
    owner_subdomain: identity
    disposition: SATISFIED
    existing_artifact: blockchain::CC_VALIDATE_REGISTRATION_V0
    source_finding: {phase: p4, register: capability_graph, key: Read a registration for absent or malformed details}
  - capability: Offer both acts through one way in
    owner_subdomain: identity
    disposition: SATISFIED
    existing_artifact: transport::CONSTITUTION_TRANSPORT_INGRESS_V0
    source_finding: {phase: p4, register: capability_graph, key: Offer both acts through one way in}
  - capability: Announce the moments an actor is registered, accepted and rejected
    owner_subdomain: construction — how artifacts are rendered, not identity
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: 'Announce the moments an actor is registered, accepted and rejected'}
  - capability: Hold what an act requires with the act that requires it
    owner_subdomain: identity, in a later change
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Hold what an act requires with the act that requires it}
  - capability: Establishing who a caller is, and what they are allowed to do
    owner_subdomain: identity, in a later change
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: 'Establishing who a caller is, and what they are allowed to do'}
  - capability: Looking up an actor from outside
    owner_subdomain: identity, in a later change
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Looking up an actor from outside}
  - capability: Telling a person anything after they leave the page
    owner_subdomain: identity, in a later change
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Telling a person anything after they leave the page}
  - capability: A way in for wallet, transaction, mempool, block, chain and consensus
    owner_subdomain: the subdomain of each function, when it is built
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: 'A way in for wallet, transaction, mempool, block, chain and consensus'}
  - capability: A kind of answer for an act that ran and refused
    owner_subdomain: the platform's transport governance, not this domain
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: A kind of answer for an act that ran and refused}
  storage_governance:
  - storage_need: NONE IDENTIFIED — this change stores nothing
    purpose: A request is answered and not kept, and an answer is composed for one caller and not kept. The three stores identity owns are declared by the previous change and are neither extended nor read differently, because the acts that use them are unchanged
    subdomain: identity
    source_finding: {phase: p5, register: business_objects}
  cross_subdomain_deps:
  - dependency: The governed kind that admits a request from outside
    direction: identity -> platform
    existing_artifact: transport::CONSTITUTION_TRANSPORT_INGRESS_V0
    status: SATISFIED
    source_finding: {phase: p4, register: dependency_graph, key: 'transport::CONSTITUTION_TRANSPORT_INGRESS_V0'}
  - dependency: The governed kind that states what a caller is told
    direction: identity -> platform
    existing_artifact: transport::CONSTITUTION_TRANSPORT_EGRESS_V0
    status: SATISFIED
    source_finding: {phase: p4, register: dependency_graph, key: 'transport::CONSTITUTION_TRANSPORT_EGRESS_V0'}
  - dependency: Reading a record for absence and for form
    direction: identity -> platform
    existing_artifact: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    status: SATISFIED
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0'}
  - dependency: The worked precedent for naming an act and holding what a caller does not send
    direction: identity -> workload
    existing_artifact: workload::TI_COLLATZ_COMPUTE_V0
    status: SATISFIED
    source_finding: {phase: p4, register: dependency_graph, key: 'workload::TI_COLLATZ_COMPUTE_V0'}
  - dependency: The worked precedent for classifying an ending and exposing evidence by reference
    direction: identity -> workload
    existing_artifact: workload::TE_COLLATZ_COMPUTE_V0
    status: SATISFIED
    source_finding: {phase: p4, register: dependency_graph, key: 'workload::TE_COLLATZ_COMPUTE_V0'}
  pps_artifacts_requiring_action:
  - fqdn: blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0
    current_status: Present; admits both boundary kinds among its artifact types while declaring no source layer they could be found in
    action: EXTEND
    source_finding: {phase: p4, register: dependency_graph, key: 'blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0'}
  - fqdn: blockchain::WF_REGISTER_ACTOR_V0
    current_status: Present and reached unchanged; named by a new boundary declaration and impacted by nothing
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'blockchain::WF_REGISTER_ACTOR_V0'}
  - fqdn: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    current_status: Present and reached unchanged; named by a new boundary declaration and impacted by nothing
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'blockchain::WF_RECORD_VERIFICATION_DECISION_V0'}
  - fqdn: blockchain::CC_VALIDATE_REGISTRATION_V0
    current_status: Present and reached unchanged through the act; the declaration it validates against is now held at the boundary rather than supplied by whoever calls
    action: REVIEW
    source_finding: {phase: p4, register: dependency_graph, key: 'blockchain::CC_VALIDATE_REGISTRATION_V0'}
  - fqdn: blockchain::AC_PARTICIPANT_V0
    current_status: Present and reused unchanged; a caller from outside is not established to be this or any actor
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'blockchain::AC_PARTICIPANT_V0'}
  - fqdn: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    current_status: Present and reused unchanged; impacted by 31 artifacts
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0'}
  boundary_rules:
  - rule_name: THE_DOOR_IS_OWNED_BY_THE_FUNCTION
    statement: The declaration that offers an act belongs to the subdomain that owns the act. No subdomain offers another's acts, and no separate surface owns the names of acts it does not perform.
    source_finding: {phase: p3, register: placement_decision, key: EXTEND}
  - rule_name: A_NAME_IS_NOT_AN_ACT
    statement: The public name of an act is declared apart from the act it reaches, and no caller may name an act by the thing that performs it. Re-pointing an act may not change what a caller sends or what they are told.
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - rule_name: ONE_WAY_IN_MANY_NAMES
    statement: Both acts are reached through one way in, and the request names the act. Adding a function later adds a name and never a place.
    source_finding: {phase: p4, register: design_decisions, row: 1}
  - rule_name: ONLY_READABILITY_IS_JUDGED_AT_THE_DOOR
    statement: The door judges whether the business can read what was sent, and nothing else. Anything further is the act's own decision, made where it was always made.
    source_finding: {phase: p5, register: invariants, key: 'A request whose details can be read is passed to the act, and nothing further is judged beforehand.'}
  - rule_name: ONE_TEST_STATED_TWICE
    statement: What the door states a caller may send and what the act validates against name the same fields, and neither may be changed without the other.
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - rule_name: THE_CALLER_SENDS_ONLY_THEIR_OWN
    statement: Nothing the business judges by may reach it from a caller. What an act requires and a caller must not send is held in the declaration that admits the request, sealed with it.
    source_finding: {phase: p4, register: design_decisions, row: 3}
  - rule_name: THE_PAGE_HOLDS_NO_RULE
    statement: No page validates, judges, or keeps a copy of what the business holds. What a page may hold is what the person has just typed, and no act of the business depends on it.
    source_finding: {phase: p5, register: invariants, key: No business rule is held by the web page.}
  - rule_name: THE_ANSWER_KINDS_ARE_NOT_OURS
    statement: The kinds of answer a caller may be told are governed by the platform and closed. This subdomain declares which kind each ending takes and never invents a kind, and where a kind is rendered for one manner of access is settled outside this domain entirely.
    source_finding: {phase: p4, register: constraint_register, row: 10}
  - rule_name: NOTHING_DEPENDS_ON_AN_ANNOUNCEMENT
    statement: No artifact of this change is reached by the announcement of a moment. The three declared moments remain correct and unannounceable, and that is not a prerequisite of this change.
    source_finding: {phase: p4, register: design_decisions, row: 8}
  governance_outcome:
  - capability: Offer registering an actor to a caller outside the business
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: Offer registering an actor to a caller outside the business}
  - capability: Offer recording a verification decision to a caller outside the business
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: Offer recording a verification decision to a caller outside the business}
  - capability: Hold what an act requires and a caller must not send
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: Hold what an act requires and a caller must not send}
  - capability: Tell a caller how their registration ended
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: Tell a caller how their registration ended}
  - capability: Tell a caller how their decision ended
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: Tell a caller how their decision ended}
  - capability: Declare where the boundary declarations are found
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: Declare where the boundary declarations are found}
  - capability: Show a person a form and its answer
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: Show a person a form and its answer}
  - capability: Carry a detail from one page to the next
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: Carry a detail from one page to the next}
  - capability: Show the functions the business has not built
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: Show the functions the business has not built}
```

Placement of everything this change offers. The acts being reached already exist and are owned where
they were owned; what is placed here is the door, and it is placed with the function whose acts it
admits. Two capabilities are satisfied by artifacts already in the composition, and one obligation
belongs to a subdomain that is not this one.

---

## 1. Ownership

---

## 2. Storage Governance

---

## 3. Cross-Subdomain Dependencies

---

## 4. PPS Artifacts Requiring Action

---

## 5. Governance Boundary Rules

---

## 6. Governance Outcome

---

## gov_projection — Governed Handoff to Stage 7

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | subdomain_purpose · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
| **Emits** → Stage 7 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
