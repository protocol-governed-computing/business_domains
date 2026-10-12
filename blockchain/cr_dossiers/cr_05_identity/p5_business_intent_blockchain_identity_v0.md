# Stage 5 — Business Intent: blockchain / identity

## Machine

```yaml
document:
  phase: p5
  domain: blockchain
  subdomain: identity
  cr: cr_05_identity
  rule_set: transformation.schemas.REGISTER_SCHEMA_P5_V0
registers:
  subdomain_purpose: |2

    The Identity subdomain governs who an actor is and whether the business trusts them. It holds one
    record for each person known to the system, the state that says whether the business has accepted
    them, and the record of every moment in their history. A person supplies their own details and is
    admitted unverified; separately, an authority records a decision accepting or rejecting them. The
    details a person was admitted with are theirs and stay theirs: a decision records whether the
    business trusts someone, and it is not an occasion to alter who they said they were. Identity also
    decides what of itself is offered to callers outside it. It does not govern what a trusted actor may
    then do, which persons may be an authority, or who a caller is.
  purpose_provenance:
  - source: CR seed §0 Subdomain Purpose
    disposition: INHERITED
    refinement: ''
  subdomain_purposes:
  - subdomain: identity
    purpose: Governs who an actor is and whether the business trusts them, and now holds every rule it applies to that question.
    source_finding: {phase: p4, register: bm_entities, key: The Business's Rules}
  scope_boundary:
  - capability: Check a registration and refuse an incomplete one
    status: IN_SCOPE
    notes: The check holds what a registration must contain and refuses on what it finds.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-01}
  - capability: Record a decision only about an unverified person, and only an acceptance or a rejection
    status: IN_SCOPE
    notes: The deciding step holds both sets and builds the record from the decision it checked.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-02}
  - capability: Refuse an authority deciding about themselves
    status: IN_SCOPE
    notes: A comparison and a fixed rule on its result.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-03}
  - capability: Refuse a rejection stating no grounds
    status: IN_SCOPE
    notes: The grounds step holds its own rules.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-04}
  - capability: Fix the decision each act records
    status: IN_SCOPE
    notes: Each act records its own decision.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-05}
  - capability: Register a person unverified
    status: IN_SCOPE
    notes: The registration act writes the state unverified as its own.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-06}
  - capability: Reach identity from outside
    status: IN_SCOPE
    notes: The entrances stop supplying what identity holds; nothing a caller sends or is told changes.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-07}
  - capability: Admit an acceptance with its grounds
    status: IN_SCOPE
    notes: The acceptance gate declares the optional grounds the act reads.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-08}
  - capability: Admit a registration without the schema identity holds
    status: IN_SCOPE
    notes: The registration gate stops requiring what identity now holds.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-10}
  - capability: Record the moment of each act as the act's own
    status: DEFERRED
    notes: The moment and its stream stay the request's to name.
    source_finding: {phase: p4, register: authoring_scope, key: Record the moment of each act as the act's own}
  - capability: Records made under a request's own rules
    status: DEFERRED
    notes: Declined by the business; the record is added to and never rewritten.
    source_finding: {phase: p4, register: authoring_scope, key: Records made under a request's own rules}
  business_objects:
  - store_name: Actor record
    record_model: MUTABLE_STATE
    business_rationale: 'Unchanged by this change, and named because what changes is what may be written into it: a registration only as unverified, a decision only as the one checked.'
    source_finding: {phase: p4, register: bm_entities, key: The Record}
  identity_semantics:
  - store_name: Actor record
    identity_field: Contact address
    source: Supplied by the person registering themselves
    uniqueness_rule: Two actors never share a contact address; unchanged by this change.
    cross_subdomain_relationship: None — the actor is named by later subdomains and names none
    source_finding: {phase: p4, register: bm_entities, key: The Record}
  invariants:
  - invariant: No person is registered without a name and an address they are reached at.
    business_reason: The business said both are required.
    source_finding: {phase: p1, register: business_invariants, row: 1}
  - invariant: No person is decided about more than once.
    business_reason: Only an unverified person may be accepted or rejected.
    source_finding: {phase: p1, register: business_invariants, row: 2}
  - invariant: No decision other than an acceptance or a rejection is recorded.
    business_reason: There is no third decision.
    source_finding: {phase: p1, register: business_invariants, row: 3}
  - invariant: No rejection is recorded without its grounds.
    business_reason: The business decided a rejection must say why.
    source_finding: {phase: p1, register: business_invariants, row: 4}
  - invariant: No authority decides about themselves.
    business_reason: A decision about oneself is not a decision by the business.
    source_finding: {phase: p1, register: business_invariants, row: 5}
  - invariant: A business rule of identity's is held by identity, and no request changes it.
    business_reason: A business rule the caller supplies is a business rule the caller can widen.
    source_finding: {phase: p1, register: business_invariants, row: 6}
  - invariant: A refusal changes no record.
    business_reason: A refused request leaves the business as it found it.
    source_finding: {phase: p1, register: business_invariants, row: 7}
  actions:
  - action: Register
    object: A person, held unverified, whose registration is complete
    trigger: A person supplies a registration
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Register a person unverified}
  - action: Refuse
    object: A registration missing its name or address
    trigger: A person supplies an incomplete registration
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Check a registration and refuse an incomplete one}
  - action: Accept
    object: An unverified person, decided about by someone other than themselves
    trigger: An authority records an acceptance
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: 'Record a decision only about an unverified person, and only an acceptance or a rejection'}
  - action: Reject
    object: An unverified person, with grounds, decided about by someone other than themselves
    trigger: An authority records a rejection
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Refuse a rejection stating no grounds}
  - action: Name the moment
    object: The moment each act records
    trigger: An act completes
    status: DEFERRED
    source_finding: {phase: p4, register: authoring_scope, key: Record the moment of each act as the act's own}
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
