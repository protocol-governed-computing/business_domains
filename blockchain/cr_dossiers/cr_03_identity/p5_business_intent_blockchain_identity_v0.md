# Stage 5 — Business Intent: blockchain / identity

## Machine

```yaml
document:
  phase: p5
  domain: blockchain
  subdomain: identity
  cr: cr_03_identity
  rule_set: transformation.schemas.REGISTER_SCHEMA_P5_V0
registers:
  subdomain_purpose: |2

    The Identity subdomain governs who an actor is and whether the business trusts them. It holds one
    record for each person known to the system, the state that says whether the business has accepted
    them, and the record of every moment in their history. A person supplies their own details and is
    admitted unverified; separately, an authority records a decision accepting or rejecting them. The
    details a person was admitted with are theirs and stay theirs: a decision records whether the
    business trusts someone, and it may change only three things about them — their state, the authority
    that decided, and the grounds stated. Identity also decides what of itself is offered to callers
    outside it. It does not govern what a trusted actor may then do, which persons may be an authority,
    or who a caller is.
  purpose_provenance:
  - source: CR seed §0 Subdomain Purpose
    disposition: REFINED
    refinement: 'The seed states that a person''s admitted details survive the decision made about them. This states the same rule as a bound rather than a promise: three things a decision may change, and everything else it may not. Nothing here contradicts the seed or either earlier change; what it adds is the enumeration, which is what makes the rule something a mechanism can hold rather than something a document asserts.'
  scope_boundary:
  - capability: Record a decision against a registered person
    status: IN_SCOPE
    notes: One step of the contract changes; its refusals, inputs and result statuses do not.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-01}
  - capability: State which of a person's details a decision may change
    status: IN_SCOPE
    notes: The three the business names become the fields the change sets.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-02}
  - capability: Assemble the record a decision writes
    status: DEFERRED
    notes: Retained unchanged, and left without a consumer by this change.
    source_finding: {phase: p4, register: authoring_scope, key: Assemble the record a decision writes}
  - capability: Say which artifacts consume a store
    status: DEFERRED
    notes: Owned by the components that build the composition's indexes, not by a business domain.
    source_finding: {phase: p4, register: authoring_scope, key: Say which artifacts consume a store}
  - capability: Restoring details lost from records already thinned
    status: DEFERRED
    notes: Declined by the business; the record is added to and never rewritten.
    source_finding: {phase: p4, register: authoring_scope, key: Restoring details lost from records already thinned}
  - capability: Correcting a person's own details
    status: DEFERRED
    notes: Deferred by the business and unchanged.
    source_finding: {phase: p4, register: authoring_scope, key: Correcting a person's own details}
  - capability: Enforcing that a rejection states grounds inside the business
    status: DEFERRED
    notes: Unchanged by this change and enforced at the boundary only.
    source_finding: {phase: p4, register: authoring_scope, key: Enforcing that a rejection states grounds inside the business}
  business_objects:
  - store_name: Actor record
    record_model: MUTABLE_STATE
    business_rationale: Unchanged by this change and named because what changes is how it is written. It holds one record per person, whose state changes when a decision is recorded and whose admitted details must survive that change.
    source_finding: {phase: p4, register: bm_entities, key: The Record}
  identity_semantics:
  - store_name: Actor record
    identity_field: Contact address
    source: Supplied by the person registering themselves
    uniqueness_rule: Two actors never share a contact address, unchanged and established by the change that created the function. This change addresses the record by that key and depends on no property beyond the key identifying one record.
    cross_subdomain_relationship: None — the actor is named by later subdomains and names none
    source_finding: {phase: p4, register: design_decisions, row: 3}
  invariants:
  - invariant: A person's admitted details survive every decision recorded about them.
    business_reason: The business decided at the outset that a person keeps what they were admitted with. Nothing an authority does should change who a person said they were.
    source_finding: {phase: p1, register: business_invariants, row: 1}
  - invariant: A decision changes the person's state, the authority named and the grounds, and nothing else about them.
    business_reason: Naming what a decision may change is what makes everything else safe from it. Stated as a bound rather than an intention, it is something a mechanism can hold.
    source_finding: {phase: p1, register: business_invariants, row: 2}
  - invariant: No decision alters a detail the person supplied themselves.
    business_reason: A decision records a decision. Changing a person's details is a different act, and one the business has deferred.
    source_finding: {phase: p1, register: business_invariants, row: 3}
  - invariant: A record already written is never rewritten, however thin it is.
    business_reason: The business would rather carry a thin old record than start editing history.
    source_finding: {phase: p1, register: business_invariants, row: 4}
  - invariant: What a caller sends and what they are told back is unchanged by how a decision is written.
    business_reason: The business is correcting how it does something, not what it offers, and a caller should not be able to tell.
    source_finding: {phase: p1, register: business_invariants, row: 5}
  actions:
  - action: Decide
    object: A registered person, accepted or rejected, keeping everything they were admitted with
    trigger: An authority records a decision against a registered person
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Record a decision against a registered person}
  - action: Bound
    object: What a decision may change about a person, to the state, the authority and the grounds
    trigger: The business states which details a decision is entitled to touch
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: State which of a person's details a decision may change}
  - action: Correct
    object: A person's own registered details
    trigger: A person's name or address changes after admission
    status: DEFERRED
    source_finding: {phase: p4, register: authoring_scope, key: Correcting a person's own details}
  - action: Restore
    object: Details lost from a record thinned before this change
    trigger: The business chooses to repair what it has already recorded
    status: DEFERRED
    source_finding: {phase: p4, register: authoring_scope, key: Restoring details lost from records already thinned}
  provisional_codes: null
  cross_subdomain_refs: []
```

---

## 1. Subdomain Purpose

---

## 2. Scope Boundary

---

## 3. Business Objects

---

## 4. Identity Semantics

---

## 5. Invariants

---

## 6. Actions

---

## 7. Provisional Codes

---

## 8. Cross-Subdomain References

---

## gov_projection — Governed Handoff to Stage 6

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 4 | actors · bm_entities · events · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
| **Emits** → Stage 6 | subdomain_purpose · purpose_provenance · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
