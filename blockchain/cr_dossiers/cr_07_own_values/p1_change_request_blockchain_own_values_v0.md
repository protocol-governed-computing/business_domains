# Stage 1 — Change Request: Clarification & Fact Capture: blockchain / identity and wallet

## Machine

```yaml
document:
  phase: p1
  domain: blockchain
  subdomain:
  - identity
  - wallet
  cr: cr_07_own_values
  rule_set: transformation.schemas.REGISTER_SCHEMA_P1_V0
registers:
  cr_type:
  - subdomain: identity
    classification: MODIFY
    rationale: Identity's acts take the moment, the trail and the contact address's place from the request. Nothing is added to what identity does.
    source_finding: {phase: p0, register: cr_type, row: 1}
  - subdomain: wallet
    classification: MODIFY
    rationale: Wallet's act takes the wallet's record, its identity's prefix and its moment from the request. Nothing is added to what wallet does.
    source_finding: {phase: p0, register: cr_type, row: 2}
  business_vocabulary:
  - term: Moment
    definition: 'One occurrence in a person''s or a wallet''s history: registered, accepted, rejected, or wallet created.'
    source_finding: {phase: p0, register: business_vocabulary, row: 1}
  - term: Trail
    definition: The ordered record of moments the business keeps and never rewrites.
    source_finding: {phase: p0, register: business_vocabulary, row: 2}
  - term: Contact address
    definition: The address that makes one person one actor.
    source_finding: {phase: p0, register: business_vocabulary, row: 3}
  - term: Wallet record
    definition: 'What the business holds about a wallet: its holder, balance, denomination, classification and state.'
    source_finding: {phase: p0, register: business_vocabulary, row: 4}
  - term: Entrance
    definition: The way a caller outside the composition starts an act.
    source_finding: {phase: p0, register: business_vocabulary, row: 5}
  - term: Entry point
    definition: The declaration of what a request to start an act must carry.
    source_finding: {phase: p0, register: business_vocabulary, row: 6}
  - term: Act
    definition: 'One thing a caller asks identity or wallet to do: register, accept, reject, or create a wallet.'
    source_finding: {phase: p0, register: business_vocabulary, row: 7}
  - term: Successor
    definition: The new identity that states what an act, entrance or entry point does after this change.
    source_finding: {phase: p0, register: business_vocabulary, row: 8}
  - term: Retired by record
    definition: Replaced by a declared successor, removed from the registry, and recorded as retired.
    source_finding: {phase: p0, register: business_vocabulary, row: 9}
  requested_outcomes:
  - outcome: Every identity and wallet act states the moment it records and the trail it records it on.
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - outcome: Registration states where the contact address sits and what kind of value it is.
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - outcome: Wallet states every value of the record it creates.
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  - outcome: Wallet states the prefix of a wallet's identity.
    source_finding: {phase: p0, register: requested_outcomes, row: 4}
  - outcome: No entrance sends a value its act states.
    source_finding: {phase: p0, register: requested_outcomes, row: 5}
  - outcome: Everything else identity and wallet do is unchanged.
    source_finding: {phase: p0, register: requested_outcomes, row: 6}
  - outcome: Each act, entrance and entry point whose meaning this changes has a successor, and its predecessor is retired by record.
    source_finding: {phase: p0, register: requested_outcomes, row: 7}
  known_facts:
  - fact: An act either succeeds or is rejected. There is no third ending.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 1}
  - fact: The business adds to its record and does not rewrite it.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 2}
  - fact: Identity is fixed at publication; a change of meaning is a new identity.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 3}
  - fact: A predecessor is retired by record when its successor replaces it.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 4}
  - fact: An acceptance may state its grounds or not. A rejection must state them.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 5}
  - fact: A new wallet's holder is the accepted person identity holds.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 6}
  - fact: A new wallet's balance is zero, its denomination BACHI, its classification DEFAULT and its state ACTIVE.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 7}
  - fact: Callers send the same inputs through each entrance after this change as before it.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 8}
  system_beliefs:
  - belief: Each identity act takes the moment it records and the trail it records it on from the request.
    why_it_matters: A direct caller can name a moment that did not happen.
    verification_goal: Establish, for each identity act, where the moment and the trail come from.
    source_finding: {phase: p0, register: system_beliefs, row: 1}
  - belief: Registration takes where the contact address sits, and what kind of value it is, from the request.
    why_it_matters: A caller can point the claim at another field.
    verification_goal: Establish where registration's claim reads the address's place and kind.
    source_finding: {phase: p0, register: system_beliefs, row: 2}
  - belief: Wallet's record is whatever the request supplies.
    why_it_matters: A caller can create a wallet for another holder, with any balance.
    verification_goal: Establish where each value of a new wallet's record comes from.
    source_finding: {phase: p0, register: system_beliefs, row: 3}
  - belief: The wallet entry point declares the prefix of the wallet's identity as a request value.
    why_it_matters: A caller chooses part of the wallet's identity.
    verification_goal: Establish what the wallet entry point declares.
    source_finding: {phase: p0, register: system_beliefs, row: 4}
  - belief: The three identity entrances send the moment, the trail and the address's place on every request.
    why_it_matters: Each entrance changes, and so needs a successor.
    verification_goal: Establish what each entrance hands its act.
    source_finding: {phase: p0, register: system_beliefs, row: 5}
  - belief: The business's check of its entry points reports ten undeclared request values on identity and wallet acts.
    why_it_matters: It is the measure this change closes.
    verification_goal: Establish the findings the entry-point check reports for blockchain.
    source_finding: {phase: p0, register: system_beliefs, row: 6}
  - belief: Entrances, entry points and runtime bindings name the acts they start or bind.
    why_it_matters: Each referrer of a replaced act must be re-pointed.
    verification_goal: Establish everything that names each replaced act, entrance and entry point.
    source_finding: {phase: p0, register: system_beliefs, row: 7}
  assumptions: []
  constraints:
  - constraint: Nothing changes for a request that supplies the values the acts now state.
    source: Business author
    source_finding: {phase: p0, register: constraints, row: 1}
  - constraint: Records made before this change stay as they were made.
    source: Business author — the record is added to, never rewritten.
    source_finding: {phase: p0, register: constraints, row: 2}
  - constraint: No ending is added.
    source: Business author — an act succeeds or is rejected.
    source_finding: {phase: p0, register: constraints, row: 3}
  - constraint: Callers through an entrance send the same inputs as before.
    source: Business author
    source_finding: {phase: p0, register: constraints, row: 4}
  business_invariants:
  - invariant: The moment an act records is the moment that happened.
    source_finding: {phase: p0, register: business_invariants, row: 1}
  - invariant: A wallet's holder is the person identity accepted.
    source_finding: {phase: p0, register: business_invariants, row: 2}
  - invariant: A new wallet holds nothing.
    source_finding: {phase: p0, register: business_invariants, row: 3}
  - invariant: A value only the business may decide is never taken from a request.
    source_finding: {phase: p0, register: business_invariants, row: 4}
  - invariant: A published identity means what it meant when it was published.
    source_finding: {phase: p0, register: business_invariants, row: 5}
  lifecycle_states:
  - object: Person
    state: Unverified
    meaning: Registered, and not yet decided about. Unchanged by this change.
    source_finding: {phase: p0, register: lifecycle_states, row: 1}
  - object: Person
    state: Accepted
    meaning: An authority recorded an acceptance. Unchanged by this change.
    source_finding: {phase: p0, register: lifecycle_states, row: 2}
  - object: Person
    state: Rejected
    meaning: An authority recorded a rejection, with its grounds. Unchanged by this change.
    source_finding: {phase: p0, register: lifecycle_states, row: 3}
  - object: Wallet
    state: Active
    meaning: Given to an accepted person, holding nothing. Every new wallet starts here.
    source_finding: {phase: p0, register: lifecycle_states, row: 4}
  business_events:
  - event: A person was registered
    when_it_occurs: When a person supplies a complete registration
    significance: Unchanged; its moment is now the act's own.
    source_finding: {phase: p0, register: business_events, row: 1}
  - event: A person was accepted
    when_it_occurs: When an authority records an acceptance
    significance: Unchanged; its moment is now the act's own.
    source_finding: {phase: p0, register: business_events, row: 2}
  - event: A person was rejected
    when_it_occurs: When an authority records a rejection with its grounds
    significance: Unchanged; its moment is now the act's own.
    source_finding: {phase: p0, register: business_events, row: 3}
  - event: A wallet was created
    when_it_occurs: When an accepted person is given a wallet
    significance: Unchanged; the wallet's record and moment are now the act's own.
    source_finding: {phase: p0, register: business_events, row: 4}
  authority_boundaries:
  - business_object: The moments identity records and the trail they go on
    authoritative_owner: Identity
    source_finding: {phase: p0, register: authority_boundaries, row: 1}
  - business_object: Where a contact address sits in a person's record
    authoritative_owner: Identity
    source_finding: {phase: p0, register: authority_boundaries, row: 2}
  - business_object: A new wallet's record, its identity's prefix and its moment
    authoritative_owner: Wallet
    source_finding: {phase: p0, register: authority_boundaries, row: 3}
  out_of_scope:
  - item: An acceptance an entrance cannot answer without grounds
    reason: Waits on the transport standard letting an entrance's answer leave a field out.
    source_finding: {phase: p0, register: out_of_scope, row: 1}
  - item: Records made before this change
    reason: The business adds to its record and does not rewrite it.
    source_finding: {phase: p0, register: out_of_scope, row: 2}
  - item: The other five functions
    reason: Not this change.
    source_finding: {phase: p0, register: out_of_scope, row: 3}
  governance_scope:
  - scope_item: Identity
    relationship: MODIFIED
    source_finding: {phase: p0, register: governance_scope, row: 1}
  - scope_item: Wallet
    relationship: MODIFIED
    source_finding: {phase: p0, register: governance_scope, row: 2}
  - scope_item: Transaction
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 3}
  - scope_item: Mempool
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 4}
  - scope_item: Block
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 5}
  - scope_item: Chain
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 6}
  - scope_item: Consensus
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 7}
  clarification_requests: []
  acceptance_criteria:
  - criterion: A registration records the person as registered, whatever moment or trail the request names.
    source_finding: {phase: p0, register: acceptance_criteria, row: 1}
  - criterion: An acceptance records the person as accepted, whatever moment or trail the request names.
    source_finding: {phase: p0, register: acceptance_criteria, row: 2}
  - criterion: A rejection records the person as rejected, whatever moment or trail the request names.
    source_finding: {phase: p0, register: acceptance_criteria, row: 3}
  - criterion: A registration claims the person's contact address, whatever place the request names for it.
    source_finding: {phase: p0, register: acceptance_criteria, row: 4}
  - criterion: A new wallet is held by the accepted person, with a balance of zero, BACHI, DEFAULT and ACTIVE, whatever the request states.
    source_finding: {phase: p0, register: acceptance_criteria, row: 5}
  - criterion: A new wallet's identity carries the business's prefix, whatever the request states.
    source_finding: {phase: p0, register: acceptance_criteria, row: 6}
  - criterion: A new wallet's trail records that the wallet was created, whatever moment the request names.
    source_finding: {phase: p0, register: acceptance_criteria, row: 7}
  - criterion: Every request admitted through an entrance before this change is admitted after it, and every request refused there is refused.
    source_finding: {phase: p0, register: acceptance_criteria, row: 8}
  - criterion: The entry-point check reports no undeclared request value on any identity or wallet act.
    source_finding: {phase: p0, register: acceptance_criteria, row: 9}
  - criterion: Each act, entrance and entry point whose meaning this changes is stated under a new identity, and its predecessor is retired by record.
    source_finding: {phase: p0, register: acceptance_criteria, row: 10}
  - criterion: Nothing in force names a retired identity.
    source_finding: {phase: p0, register: acceptance_criteria, row: 11}
  identity_and_sameness:
  - business_object: Act, entrance or entry point
    identified_by: Its identity
    two_are_the_same_when: Its declaration means what the published declaration meant
    source_finding: {phase: p0, register: identity_and_sameness, row: 1}
  lifecycle_transitions:
  - object: Act, entrance or entry point
    from_state: In force
    to_state: Retired by record
    triggered_by: This change adds its successor
    cascade: Whatever names it is re-pointed
    source_finding: {phase: p0, register: lifecycle_transitions, row: 1}
  operation_refusals: []
  authority_deferrals: []
```

Projected from the change seed. Every row is the seed's own, cited to the section it was
said in. S1 interrogates and does not author: a question raised by restating the seed
amends the seed and is projected again, so no row here states business content the seed
does not.

---

## 1. CR Type

---

## 2. Business Vocabulary

---

## 3. Requested Outcomes

---

## 4. Known Facts — Business Truths

---

## 5. Existing-System Beliefs — Requiring Verification

---

## 6. Assumptions

---

## 7. Constraints

---

## 8. Business Invariants

---

## 9. Lifecycle States

---

## 10. Business Events

---

## 11. Authority Boundaries

---

## 12. Out of Scope

---

## 13. Governance Scope

---

## 14. Clarification Requests

---

## 15. Acceptance Criteria

---

## 16. Identity and Sameness

---

## 17. Lifecycle Transitions

---

## 18. Operation Refusals

---

## 19. Authority Deferrals

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
