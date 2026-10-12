# Stage 5 — Business Intent: blockchain / identity and wallet

## Machine

```yaml
document:
  phase: p5
  domain: blockchain
  subdomain:
  - identity
  - wallet
  cr: cr_06_routing_closure
  rule_set: transformation.schemas.REGISTER_SCHEMA_P5_V0
registers:
  subdomain_purpose: |2

    The Identity subdomain governs who an actor is and whether the business trusts them. The Wallet
    subdomain governs the wallet an accepted person is given. Both keep records the business relies on:
    the person's record, the address they claimed, the trail of moments in their history, and their
    wallet. This change decides what every identity and wallet act does when one of those records cannot
    be read or written, and states each act it changes under a new identity.
  purpose_provenance:
  - source: CR seed §0 Subdomain Purpose
    disposition: INHERITED
    refinement: ''
  subdomain_purposes:
  - subdomain: identity
    purpose: Governs who an actor is and whether the business trusts them, and ends each of its acts as rejected when a record fails.
    source_finding: {phase: p4, register: actors, key: Identity}
  - subdomain: wallet
    purpose: Governs the wallet an accepted person is given, and ends its act as rejected when a record fails.
    source_finding: {phase: p4, register: actors, key: Wallet}
  scope_boundary:
  - capability: Stop a lookup at a failed record
    status: IN_SCOPE
    notes: The lookup and the read each end the contract on a failed record.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-01}
  - capability: Stop a wallet step at a failed record
    status: IN_SCOPE
    notes: The claim, the write and the append each end their contract on a failed record.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-02}
  - capability: End every act as rejected on a failed record
    status: IN_SCOPE
    notes: Each act routes a failed record to its rejected ending.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-03}
  - capability: Tell a refusal apart from a failure
    status: DEFERRED
    notes: The business keeps two endings.
    source_finding: {phase: p4, register: authoring_scope, key: Tell a refusal apart from a failure}
  - capability: The superseded act's unrouted nodes
    status: DEFERRED
    notes: Not dispatched; nothing reaches them.
    source_finding: {phase: p4, register: authoring_scope, key: The superseded act's unrouted nodes}
  business_objects:
  - store_name: Actor record
    record_model: MUTABLE_STATE
    business_rationale: Unchanged, and named because a failed read or write of it now ends the act.
    source_finding: {phase: p4, register: bm_entities, key: The Person's Record}
  - store_name: Contact address registry
    record_model: IDENTITY_REGISTRY
    business_rationale: Unchanged, and named because a failed lookup or claim in it now ends the act.
    source_finding: {phase: p4, register: bm_entities, key: The Claimed Address}
  - store_name: Wallet record
    record_model: MUTABLE_STATE
    business_rationale: Unchanged, and named because a failed write of it now ends the act.
    source_finding: {phase: p4, register: bm_entities, key: The Wallet}
  - store_name: Wallet trail
    record_model: APPEND_ONLY_JOURNAL
    business_rationale: Unchanged, and named because a failed append to it now ends the act.
    source_finding: {phase: p4, register: bm_entities, key: The Trail}
  identity_semantics:
  - store_name: Actor record
    identity_field: Contact address
    source: Supplied by the person registering themselves
    uniqueness_rule: Two actors never share a contact address; unchanged by this change.
    cross_subdomain_relationship: Named by wallet, which looks the person up
    source_finding: {phase: p4, register: bm_entities, key: The Person's Record}
  - store_name: Wallet record
    identity_field: Wallet identity
    source: Determined when the wallet is created
    uniqueness_rule: Two wallets never share an identity; unchanged by this change.
    cross_subdomain_relationship: Names the accepted person it belongs to
    source_finding: {phase: p4, register: bm_entities, key: The Wallet}
  invariants:
  - invariant: No act carries on past a record it could not read or write.
    business_reason: A step after a failed record would act on something the business does not hold.
    source_finding: {phase: p1, register: business_invariants, row: 1}
  - invariant: Every act ends as succeeded or rejected.
    business_reason: The business keeps two endings.
    source_finding: {phase: p1, register: business_invariants, row: 2}
  - invariant: A refusal changes no record.
    business_reason: A refused request leaves the business as it found it, and records made before a failure stay.
    source_finding: {phase: p1, register: business_invariants, row: 3}
  - invariant: A published identity means what it meant when it was published.
    business_reason: A citation of v5 relies on what v5 said.
    source_finding: {phase: p1, register: business_invariants, row: 4}
  actions:
  - action: Reject
    object: An act whose record failed
    trigger: A store reports a failed record
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: End every act as rejected on a failed record}
  - action: Stop
    object: A lookup whose record failed
    trigger: The address registry or the actor record fails
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Stop a lookup at a failed record}
  - action: Stop
    object: A wallet step whose record failed
    trigger: The wallet registry, record or trail fails
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Stop a wallet step at a failed record}
  - action: Distinguish
    object: A failure from a refusal
    trigger: An act ends on a failed record
    status: DEFERRED
    source_finding: {phase: p4, register: authoring_scope, key: Tell a refusal apart from a failure}
  provisional_codes:
  - subdomain: identity
    provisional_code: CC_RESOLVE_ACTOR_V1
    family: CC
    summary: Answers which actor a contact address denotes, and reports when none does.
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - subdomain: wallet
    provisional_code: CC_CLAIM_WALLET_IDENTITY_V1
    family: CC
    summary: Claims the identity, and refuses when the person already holds a wallet.
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - subdomain: wallet
    provisional_code: CC_CREATE_WALLET_RECORD_V1
    family: CC
    summary: Records the wallet with a balance of zero, its denomination and its classification.
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - subdomain: wallet
    provisional_code: CC_APPEND_WALLET_OCCURRENCE_V1
    family: CC
    summary: Records the moment on the wallet's trail.
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - subdomain: identity
    provisional_code: WF_REGISTER_ACTOR_V1
    family: WF
    summary: The governed sequence that admits a person as an unverified actor, and announces that it did.
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - subdomain: identity
    provisional_code: WF_ACCEPT_ACTOR_V1
    family: WF
    summary: The governed sequence that records an acceptance and announces it.
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - subdomain: identity
    provisional_code: WF_REJECT_ACTOR_V1
    family: WF
    summary: The governed sequence that records a rejection, with grounds required, and announces it.
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - subdomain: wallet
    provisional_code: WF_CREATE_WALLET_V1
    family: WF
    summary: The governed sequence that gives an accepted person a wallet and records that it did.
    source_finding: {phase: p4, register: design_decisions, row: 5}
  cross_subdomain_refs:
  - cc_code: blockchain::CC_RESOLVE_ACTOR_V0
    defined_in: identity
    role: Wallet looks the person up through identity's lookup, and runs its next version, which answers for a failed record.
    source_finding: {phase: p4, register: dependency_graph, key: 'blockchain::CC_RESOLVE_ACTOR_V0'}
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
