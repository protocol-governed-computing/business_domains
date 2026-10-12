# Stage 1 — Change Request: Clarification & Fact Capture: blockchain / identity and wallet

## Machine

```yaml
document:
  phase: p1
  domain: blockchain
  subdomain:
  - identity
  - wallet
  cr: cr_06_routing_closure
  rule_set: transformation.schemas.REGISTER_SCHEMA_P1_V0
registers:
  cr_type:
  - subdomain: identity
    classification: MODIFY
    rationale: Identity's acts do not say what happens when a record fails, and one carries on past a failed lookup. Nothing is added to what identity does.
    source_finding: {phase: p0, register: cr_type, row: 1}
  - subdomain: wallet
    classification: MODIFY
    rationale: Wallet's act does not say what happens when a record fails, and three of its steps carry on past a failure. Nothing is added to what wallet does.
    source_finding: {phase: p0, register: cr_type, row: 2}
  business_vocabulary:
  - term: Record
    definition: 'Something the business keeps: a person''s record, a claimed address, a trail of moments, or a wallet.'
    source_finding: {phase: p0, register: business_vocabulary, row: 1}
  - term: Failed record
    definition: A record that could not be read or written, because the store was unreachable or answered with an error.
    source_finding: {phase: p0, register: business_vocabulary, row: 2}
  - term: Act
    definition: 'One thing a caller asks identity or wallet to do: register, accept, reject, or create a wallet.'
    source_finding: {phase: p0, register: business_vocabulary, row: 3}
  - term: Rejected
    definition: The ending of an act that did not succeed.
    source_finding: {phase: p0, register: business_vocabulary, row: 4}
  - term: Published
    definition: Sealed into a composition that was released and cited.
    source_finding: {phase: p0, register: business_vocabulary, row: 5}
  - term: Successor
    definition: The new identity that states what an act does after this change.
    source_finding: {phase: p0, register: business_vocabulary, row: 6}
  - term: Stood down
    definition: Replaced by a declared successor, kept in the record and out of reach.
    source_finding: {phase: p0, register: business_vocabulary, row: 7}
  requested_outcomes:
  - outcome: Every identity and wallet act ends as rejected when a record it needs fails.
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - outcome: An act stops at the step whose record failed, and nothing after it runs.
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - outcome: Everything else identity and wallet do is unchanged.
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  - outcome: Each act whose meaning this changes has a successor, and its published identity is stood down unchanged.
    source_finding: {phase: p0, register: requested_outcomes, row: 4}
  - outcome: Everything in force that names a stood-down act names its successor.
    source_finding: {phase: p0, register: requested_outcomes, row: 5}
  known_facts:
  - fact: An act either succeeds or is rejected. There is no third ending.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 1}
  - fact: A rejection changes no record.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 2}
  - fact: The business adds to its record and does not rewrite it.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 3}
  - fact: A failed record ends the act. Nothing retries.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 4}
  - fact: A failed record ends as rejected, not as a separate failure.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 5}
  - fact: Every identity and wallet act reads or writes a record the business keeps.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 6}
  - fact: Identity is fixed at publication; a change of meaning is a new identity.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 7}
  - fact: A published identity stays in the record, stood down, when a successor replaces it.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 8}
  - fact: A re-point changes which act a referrer names, and nothing else about it.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 9}
  system_beliefs:
  - belief: Most identity and wallet acts stop without a declared ending when a record fails.
    why_it_matters: The caller cannot tell an intended refusal from an unplanned failure.
    verification_goal: Establish, for each act, what happens when each record it touches fails.
    source_finding: {phase: p0, register: system_beliefs, row: 1}
  - belief: When an acceptance's lookup of the person fails, identity carries on and records the acceptance.
    why_it_matters: This is the failure the business wants closed first.
    verification_goal: Establish what identity does when the lookup fails during an acceptance.
    source_finding: {phase: p0, register: system_beliefs, row: 2}
  - belief: Three of wallet's steps carry on past a failed record in the same way.
    why_it_matters: The same gap, in the same form, in the other subdomain.
    verification_goal: Establish which wallet steps carry on past a failed record.
    source_finding: {phase: p0, register: system_beliefs, row: 3}
  - belief: Each act already has a rejected ending.
    why_it_matters: The change can end a failed record there without adding an ending.
    verification_goal: Confirm every identity and wallet act has a rejected ending.
    source_finding: {phase: p0, register: system_beliefs, row: 4}
  - belief: Every identity and wallet act this change touches was published in v5.
    why_it_matters: Each one it changes needs a successor.
    verification_goal: Establish which touched acts the v5 composition holds.
    source_finding: {phase: p0, register: system_beliefs, row: 5}
  - belief: Entrances and intents name the workflows they start, and workflows name the contracts they run.
    why_it_matters: Each referrer of a replaced act must be re-pointed.
    verification_goal: Establish everything that names each replaced act, by full name and by short code.
    source_finding: {phase: p0, register: system_beliefs, row: 6}
  assumptions: []
  constraints:
  - constraint: Nothing changes for an act whose records are all read and written.
    source: Business author
    source_finding: {phase: p0, register: constraints, row: 1}
  - constraint: Records made before a failure stay as they were made.
    source: Business author — the record is added to, never rewritten.
    source_finding: {phase: p0, register: constraints, row: 2}
  - constraint: No ending is added.
    source: Business author — a failure ends as rejected.
    source_finding: {phase: p0, register: constraints, row: 3}
  - constraint: No published identity changes what it says, except to be stood down.
    source: Business author — identity is fixed at publication.
    source_finding: {phase: p0, register: constraints, row: 4}
  business_invariants:
  - invariant: No act carries on past a record it could not read or write.
    source_finding: {phase: p0, register: business_invariants, row: 1}
  - invariant: Every act ends as succeeded or rejected.
    source_finding: {phase: p0, register: business_invariants, row: 2}
  - invariant: A refusal changes no record.
    source_finding: {phase: p0, register: business_invariants, row: 3}
  - invariant: A published identity means what it meant when it was published.
    source_finding: {phase: p0, register: business_invariants, row: 4}
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
  business_events:
  - event: A person was registered
    when_it_occurs: When a person supplies a complete registration and every record is written
    significance: Unchanged; it is not announced when a record fails.
    source_finding: {phase: p0, register: business_events, row: 1}
  - event: A person was accepted
    when_it_occurs: When an authority records an acceptance and every record is written
    significance: Unchanged; it is not announced when a record fails.
    source_finding: {phase: p0, register: business_events, row: 2}
  - event: A person was rejected
    when_it_occurs: When an authority records a rejection and every record is written
    significance: Unchanged; it is not announced when a record fails.
    source_finding: {phase: p0, register: business_events, row: 3}
  - event: A wallet was created
    when_it_occurs: When an accepted person is given a wallet and every record is written
    significance: Unchanged; it is not announced when a record fails.
    source_finding: {phase: p0, register: business_events, row: 4}
  authority_boundaries:
  - business_object: What an identity act does when a record fails
    authoritative_owner: Identity
    source_finding: {phase: p0, register: authority_boundaries, row: 1}
  - business_object: What a wallet act does when a record fails
    authoritative_owner: Wallet
    source_finding: {phase: p0, register: authority_boundaries, row: 2}
  out_of_scope:
  - item: Telling a refusal apart from a failure
    reason: A later decision; the business keeps two endings.
    source_finding: {phase: p0, register: out_of_scope, row: 1}
  - item: Trying a failed record again
    reason: The business decided a failed record ends the act.
    source_finding: {phase: p0, register: out_of_scope, row: 2}
  - item: Records made before a failure
    reason: The business adds to its record and does not rewrite it.
    source_finding: {phase: p0, register: out_of_scope, row: 3}
  - item: The other five functions
    reason: Not this change.
    source_finding: {phase: p0, register: out_of_scope, row: 4}
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
  - criterion: An acceptance whose lookup of the person fails is rejected, and no acceptance is recorded.
    source_finding: {phase: p0, register: acceptance_criteria, row: 1}
  - criterion: Every identity and wallet act ends as rejected when a record it needs fails.
    source_finding: {phase: p0, register: acceptance_criteria, row: 2}
  - criterion: An act stops at the step whose record failed, and nothing after it runs.
    source_finding: {phase: p0, register: acceptance_criteria, row: 3}
  - criterion: Every act whose records are all read and written ends exactly as it did before this change.
    source_finding: {phase: p0, register: acceptance_criteria, row: 4}
  - criterion: Each act whose meaning this changes is stated under a new identity, and the published identity is unchanged except for its stand-down.
    source_finding: {phase: p0, register: acceptance_criteria, row: 5}
  - criterion: Nothing in force names a stood-down act.
    source_finding: {phase: p0, register: acceptance_criteria, row: 6}
  - criterion: Records made before a failure are unchanged by it.
    source_finding: {phase: p0, register: acceptance_criteria, row: 7}
  identity_and_sameness:
  - business_object: Act
    identified_by: Its identity
    two_are_the_same_when: Its declaration means what the published declaration meant
    source_finding: {phase: p0, register: identity_and_sameness, row: 1}
  lifecycle_transitions:
  - object: Published act
    from_state: In force
    to_state: Stood down
    triggered_by: This change adds its successor
    cascade: Whatever names it is re-pointed
    source_finding: {phase: p0, register: lifecycle_transitions, row: 1}
  operation_refusals:
  - operation: Registering a person
    refused_when: A record the registration needs fails
    business_reason: A failed record ends the act.
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: Accepting a person
    refused_when: A record the acceptance needs fails
    business_reason: A failed record ends the act.
    source_finding: {phase: p0, register: operation_refusals, row: 2}
  - operation: Rejecting a person
    refused_when: A record the rejection needs fails
    business_reason: A failed record ends the act.
    source_finding: {phase: p0, register: operation_refusals, row: 3}
  - operation: Creating a wallet
    refused_when: A record the wallet needs fails
    business_reason: A failed record ends the act.
    source_finding: {phase: p0, register: operation_refusals, row: 4}
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
