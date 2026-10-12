# Stage 5 — Business Intent: blockchain / identity and wallet

## Machine

```yaml
document:
  phase: p5
  domain: blockchain
  subdomain:
  - identity
  - wallet
  cr: cr_07_own_values
  rule_set: transformation.schemas.REGISTER_SCHEMA_P5_V0
registers:
  subdomain_purpose: |2

    The Identity subdomain governs who an actor is and whether the business trusts them. The Wallet
    subdomain governs the wallet an accepted person is given. Each act records a moment on a trail, and
    wallet writes the record of every wallet it creates. This change makes each act state the values only
    the business may decide: the moment it records, the trail it records it on, where a contact address
    sits, and every value of a new wallet's record. A request no longer supplies them.
  purpose_provenance:
  - source: CR seed §0 Subdomain Purpose
    disposition: INHERITED
    refinement: ''
  subdomain_purposes:
  - subdomain: identity
    purpose: Governs who an actor is and whether the business trusts them, and states the moment each of its acts records, the trail it goes on and where a contact address sits.
    source_finding: {phase: p4, register: actors, key: Identity}
  - subdomain: wallet
    purpose: Governs the wallet an accepted person is given, and states the record of every wallet it creates, its identity's prefix and its moment.
    source_finding: {phase: p4, register: actors, key: Wallet}
  scope_boundary:
  - capability: State the moment and the trail of each identity act
    status: IN_SCOPE
    notes: Registration, acceptance and rejection each state their moment, on ACTOR_OCCURRENCES.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-01}
  - capability: State where the contact address sits
    status: IN_SCOPE
    notes: Registration states contact_address, as a string.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-02}
  - capability: State a new wallet's record, prefix and moment
    status: IN_SCOPE
    notes: The holder is the person resolved; the balance, denomination, classification, state, prefix and moment are fixed.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-03}
  - capability: Stop the entrances sending what the acts state
    status: IN_SCOPE
    notes: Each identity entrance sends only what the caller supplies.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-04}
  - capability: Answer an acceptance without grounds through an entrance
    status: DEFERRED
    notes: Waits on the transport standard letting an entrance's answer leave a field out.
    source_finding: {phase: p4, register: authoring_scope, key: Answer an acceptance without grounds through an entrance}
  - capability: The four other stood-down blockchain artifacts
    status: DEFERRED
    notes: Untouched by this change.
    source_finding: {phase: p4, register: authoring_scope, key: The four other stood-down blockchain artifacts}
  business_objects:
  - store_name: Actor trail
    record_model: APPEND_ONLY_JOURNAL
    business_rationale: Unchanged, and named because each identity act now states the moment it appends and the trail it goes on.
    source_finding: {phase: p4, register: bm_entities, key: The Trail}
  - store_name: Contact address registry
    record_model: IDENTITY_REGISTRY
    business_rationale: Unchanged, and named because registration now states where the address it claims sits.
    source_finding: {phase: p4, register: bm_entities, key: The Claimed Address}
  - store_name: Wallet record
    record_model: MUTABLE_STATE
    business_rationale: Unchanged, and named because wallet now states every value of the record it writes.
    source_finding: {phase: p4, register: bm_entities, key: The Wallet}
  - store_name: Wallet trail
    record_model: APPEND_ONLY_JOURNAL
    business_rationale: Unchanged, and named because wallet now states the moment it appends.
    source_finding: {phase: p4, register: bm_entities, key: The Trail}
  identity_semantics:
  - store_name: Contact address registry
    identity_field: Contact address
    source: The contact_address field of the person's record, as the registration act states
    uniqueness_rule: Two actors never share a contact address; unchanged by this change.
    cross_subdomain_relationship: Named by wallet, which looks the person up
    source_finding: {phase: p4, register: bm_entities, key: The Claimed Address}
  - store_name: Wallet record
    identity_field: Wallet identity
    source: Determined when the wallet is created, from its holder and the prefix the act states
    uniqueness_rule: Two wallets never share an identity; unchanged by this change.
    cross_subdomain_relationship: Names the accepted person it belongs to, as identity resolved them
    source_finding: {phase: p4, register: bm_entities, key: The Wallet}
  invariants:
  - invariant: The moment an act records is the moment that happened.
    business_reason: The trail is the business's history, and a caller cannot write it.
    source_finding: {phase: p1, register: business_invariants, row: 1}
  - invariant: A wallet's holder is the person identity accepted.
    business_reason: A wallet belongs to the person it was created for.
    source_finding: {phase: p1, register: business_invariants, row: 2}
  - invariant: A new wallet holds nothing.
    business_reason: Value enters a wallet only through a later function, never at its creation.
    source_finding: {phase: p1, register: business_invariants, row: 3}
  - invariant: A value only the business may decide is never taken from a request.
    business_reason: What the business decides, its act states.
    source_finding: {phase: p1, register: business_invariants, row: 4}
  - invariant: A published identity means what it meant when it was published.
    business_reason: A citation of v5 relies on what v5 said.
    source_finding: {phase: p1, register: business_invariants, row: 5}
  actions:
  - action: State
    object: The moment and the trail of an identity act
    trigger: A registration, acceptance or rejection is recorded
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: State the moment and the trail of each identity act}
  - action: State
    object: Where a contact address sits
    trigger: A registration claims the person's address
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: State where the contact address sits}
  - action: State
    object: A new wallet's record, prefix and moment
    trigger: An accepted person is given a wallet
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: "State a new wallet's record, prefix and moment"}
  - action: Send
    object: Only what the caller supplies
    trigger: A caller starts an identity act through an entrance
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Stop the entrances sending what the acts state}
  provisional_codes:
  - subdomain: identity
    provisional_code: WF_REGISTER_ACTOR_V2
    family: WF
    summary: The governed sequence that admits a person as an unverified actor, records that moment as its own, and announces it.
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - subdomain: identity
    provisional_code: WF_ACCEPT_ACTOR_V2
    family: WF
    summary: The governed sequence that records an acceptance, records that moment as its own, and announces it.
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - subdomain: identity
    provisional_code: WF_REJECT_ACTOR_V2
    family: WF
    summary: The governed sequence that records a rejection, with grounds required, records that moment as its own, and announces it.
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - subdomain: wallet
    provisional_code: WF_CREATE_WALLET_V2
    family: WF
    summary: The governed sequence that gives an accepted person a wallet holding nothing, and records that it did.
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - subdomain: identity
    provisional_code: TI_REGISTER_ACTOR_V1
    family: TI
    summary: Admits a request to register an actor, and sends the act only what the caller supplies and the person's preferences.
    source_finding: {phase: p4, register: design_decisions, row: 4}
  - subdomain: identity
    provisional_code: TI_ACCEPT_ACTOR_V1
    family: TI
    summary: Admits a request to accept a registered actor, and sends the act only what the caller supplies.
    source_finding: {phase: p4, register: design_decisions, row: 4}
  - subdomain: identity
    provisional_code: TI_REJECT_ACTOR_V1
    family: TI
    summary: Admits a request to reject a registered actor, and sends the act only what the caller supplies.
    source_finding: {phase: p4, register: design_decisions, row: 4}
  - subdomain: wallet
    provisional_code: IN_WALLET_CREATION_V1
    family: IN
    summary: Admits a request naming the person a wallet is for and the key it is made from, and refuses one that names nobody.
    source_finding: {phase: p4, register: design_decisions, row: 3}
  cross_subdomain_refs:
  - cc_code: blockchain::CC_RESOLVE_ACTOR_V1
    defined_in: identity
    role: Wallet looks the person up through identity's lookup, and now reads the wallet's holder from what it resolves.
    source_finding: {phase: p4, register: design_decisions, row: 2}
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
