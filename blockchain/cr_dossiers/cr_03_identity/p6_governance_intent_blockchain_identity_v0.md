# Stage 6 — Governance Intent: blockchain / identity

## Machine

```yaml
document:
  phase: p6
  domain: blockchain
  subdomain: identity
  cr: cr_03_identity
  rule_set: transformation.schemas.REGISTER_SCHEMA_P6_V0
registers:
  ownership:
  - capability: Record a decision against a registered person
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Record a decision against a registered person}
  - capability: State which of a person's details a decision may change
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: State which of a person's details a decision may change}
  - capability: Change part of a held record without replacing it
    owner_subdomain: identity
    disposition: SATISFIED
    existing_artifact: capability_side_effects::CS_MUTABLE_JSON_V0
    source_finding: {phase: p4, register: capability_graph, key: Change part of a held record without replacing it}
  - capability: Resolve the actor before a decision is recorded
    owner_subdomain: identity
    disposition: SATISFIED
    existing_artifact: blockchain::CC_RESOLVE_ACTOR_V0
    source_finding: {phase: p4, register: capability_graph, key: Resolve the actor before a decision is recorded}
  - capability: Reach the decision from outside
    owner_subdomain: identity
    disposition: SATISFIED
    existing_artifact: blockchain::TI_ACCEPT_ACTOR_V0
    source_finding: {phase: p4, register: capability_graph, key: Reach the decision from outside}
  - capability: Restore details already lost
    owner_subdomain: identity
    disposition: SATISFIED
    existing_artifact: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    source_finding: {phase: p4, register: capability_graph, key: Restore details already lost}
  - capability: Assemble the record a decision writes
    owner_subdomain: identity, in a later change
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Assemble the record a decision writes}
  - capability: Say which artifacts consume a store
    owner_subdomain: the components that build the composition's indexes, not a business domain
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Say which artifacts consume a store}
  - capability: Restoring details lost from records already thinned
    owner_subdomain: nowhere; the business declines it
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Restoring details lost from records already thinned}
  - capability: Correcting a person's own details
    owner_subdomain: identity, in a later change
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Correcting a person's own details}
  - capability: Enforcing that a rejection states grounds inside the business
    owner_subdomain: identity, in a later change
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Enforcing that a rejection states grounds inside the business}
  storage_governance:
  - storage_need: A durable record of every person the business knows, carrying both what they were admitted with and what was decided about them
    purpose: Unchanged by this change, and named because what changes is how it is written. The business requires one authoritative record per person; a decision changes three fields of it and must leave the rest as they are
    subdomain: identity
    source_finding: {phase: p5, register: business_objects, key: Actor record}
  cross_subdomain_deps:
  - dependency: Changing part of a held record without replacing it
    direction: identity -> platform
    existing_artifact: capability_side_effects::CS_MUTABLE_JSON_V0
    status: SATISFIED
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_side_effects::CS_MUTABLE_JSON_V0'}
  pps_artifacts_requiring_action:
  - fqdn: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    current_status: Present and reached by both decision workflows; its fifth step writes a whole record where it must change part of one
    action: EXTEND
    source_finding: {phase: p4, register: dependency_graph, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - fqdn: capability_side_effects::CS_MUTABLE_JSON_V0
    current_status: Present and reused unchanged; a different operation of the same capability is called
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_side_effects::CS_MUTABLE_JSON_V0'}
  - fqdn: blockchain::RB_IDENTITY_BINDINGS_V0
    current_status: Present and reused unchanged; it binds the capability, not the operation
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'blockchain::RB_IDENTITY_BINDINGS_V0'}
  - fqdn: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    current_status: Present and reused unchanged; the store, its path and its declaration are untouched
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'blockchain::STRUCTURE_IDENTITY_STORAGE_V0'}
  - fqdn: blockchain::CC_RESOLVE_ACTOR_V0
    current_status: Present and reused unchanged; the only reader of the store, unaffected by fields being restored
    action: REVIEW
    source_finding: {phase: p4, register: dependency_graph, key: 'blockchain::CC_RESOLVE_ACTOR_V0'}
  - fqdn: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    current_status: Present and unchanged; it composes the amended contract and routes on a result status this change preserves
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'blockchain::WF_RECORD_VERIFICATION_DECISION_V0'}
  - fqdn: blockchain::TI_ACCEPT_ACTOR_V0
    current_status: Present and unchanged; it names the workflow, not the contract
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'blockchain::TI_ACCEPT_ACTOR_V0'}
  - fqdn: blockchain::TI_REJECT_ACTOR_V0
    current_status: Present and unchanged; the same
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'blockchain::TI_REJECT_ACTOR_V0'}
  boundary_rules:
  - rule_name: A_DECISION_CHANGES_THREE_THINGS
    statement: A decision sets the person's state, the authority that decided and the grounds stated. Every other field of the record is absent from what it writes, and absence is how the rule is enforced rather than asserted.
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - rule_name: ADMITTED_DETAILS_ARE_NOT_THE_BUSINESS_TO_CHANGE
    statement: No act of this subdomain that records a decision may write a detail the person supplied. Changing those is a different act, and one this subdomain has deferred.
    source_finding: {phase: p5, register: invariants, key: No decision alters a detail the person supplied themselves.}
  - rule_name: WRITE_WHAT_DOES_NOT_EXIST_UPDATE_WHAT_DOES
    statement: A whole-value write is correct where a record is being created and wrong where one is being changed. Admitting a person writes; deciding about them updates. A step that writes a record it did not create is the defect this change corrects, and the store offers both so that neither needs the other's shape.
    source_finding: {phase: p4, register: design_decisions, row: 1}
  - rule_name: A_DECISION_CREATES_NOBODY
    statement: No act of this subdomain may bring a person into existence by deciding about them. A decision reaches a person the store already holds, or it refuses.
    source_finding: {phase: p4, register: design_decisions, row: 4}
  - rule_name: THE_RECORD_IS_ADDED_TO_NEVER_REWRITTEN
    statement: A record already written is left as it is, including one this defect has already thinned. No act of this change repairs history.
    source_finding: {phase: p4, register: design_decisions, row: 6}
  - rule_name: A_CORRECTION_IS_INVISIBLE_ABOVE_THE_CONTRACT
    statement: What a caller sends and is told is declared by the boundary, which names a workflow; the workflow routes on a result status. A change within a contract that preserves its statuses is observable to neither.
    source_finding: {phase: p3, register: analysis_findings, key: Q7}
  governance_outcome:
  - capability: Record a decision against a registered person
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: Record a decision against a registered person}
  - capability: State which of a person's details a decision may change
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: State which of a person's details a decision may change}
```

Placement of a correction. Nothing moves and nothing is added: the step being corrected already
belongs to the function that owns the record it writes. What is placed here is the rule the
correction realises — which of a person's details a decision may change — and it is placed with the
subdomain that holds them.

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
