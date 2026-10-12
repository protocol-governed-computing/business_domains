# Stage 1 — Change Request: Clarification & Fact Capture: blockchain / identity

## Machine

```yaml
document:
  phase: p1
  domain: blockchain
  subdomain: identity
  cr: cr_05_identity
  rule_set: transformation.schemas.REGISTER_SCHEMA_P1_V0
registers:
  cr_type:
  - subdomain: identity
    classification: MODIFY
    rationale: Identity is built and reachable. It applies its rules as each request states them rather than holding them itself, and it registers a person whose registration it has found incomplete. Nothing is added to what identity does; its own rules are made to hold however it is reached.
    source_finding: {phase: p0, register: cr_type, row: 1}
  business_vocabulary:
  - term: Registration
    definition: 'What a person supplies to become known to the business: their name and the address they are reached at.'
    source_finding: {phase: p0, register: business_vocabulary, row: 1}
  - term: Decision
    definition: 'What an authority records about a person: an acceptance or a rejection. There is no third.'
    source_finding: {phase: p0, register: business_vocabulary, row: 2}
  - term: Authority
    definition: The person who records a decision about someone else.
    source_finding: {phase: p0, register: business_vocabulary, row: 3}
  - term: Grounds
    definition: The reason an authority states when rejecting a person.
    source_finding: {phase: p0, register: business_vocabulary, row: 4}
  - term: Public entrance
    definition: The way a caller outside the business reaches identity.
    source_finding: {phase: p0, register: business_vocabulary, row: 5}
  - term: Business rule
    definition: 'Something the business decided about identity: what a registration must contain, who may be decided about, which decisions may be recorded.'
    source_finding: {phase: p0, register: business_vocabulary, row: 6}
  requested_outcomes:
  - outcome: Identity holds what a registration must contain, and refuses a registration that does not meet it.
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - outcome: Identity holds which people an authority may decide about, and refuses a decision about anyone else, whatever the request says.
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - outcome: Identity holds which decisions may be recorded, and refuses any other, whatever the request says.
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  - outcome: Everything a caller sees through the public entrance is unchanged.
    source_finding: {phase: p0, register: requested_outcomes, row: 4}
  - outcome: Identity holds that an authority does not decide about themselves, and refuses such a decision, whatever the request says.
    source_finding: {phase: p0, register: requested_outcomes, row: 5}
  - outcome: Identity holds that a rejection states its grounds, and refuses one that does not, whatever the request says.
    source_finding: {phase: p0, register: requested_outcomes, row: 6}
  known_facts:
  - fact: A registration names the person and the address they are reached at. Both are required.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 1}
  - fact: A person is decided about once. Only an unverified person may be accepted or rejected.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 2}
  - fact: A decision is an acceptance or a rejection. There is no third.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 3}
  - fact: A rejection states its grounds. An acceptance may.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 4}
  - fact: An authority does not decide about themselves.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 5}
  - fact: A business rule the caller supplies is a business rule the caller can widen.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 6}
  - fact: The wallet function met this and closed it for itself.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 7}
  - fact: A registration missing its name or address is refused.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 8}
  - fact: What a request says about the business's rules is ignored, not refused; it is not part of the request.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 9}
  - fact: A decision refused because the person was already decided about changes no record.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 10}
  - fact: The business adds to its record and does not rewrite it.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 11}
  - fact: 'Every business rule of identity''s is held by identity: what a registration must contain, who may be decided about, which decisions may be recorded, that an authority does not decide about themselves, and that a rejection states its grounds.'
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 12}
  system_beliefs:
  - belief: 'The public entrance supplies the business''s rules to identity with each request: what a registration must contain, who may be decided about, and which decisions may be recorded.'
    why_it_matters: If the entrance supplies them, a caller through it is held to them, and what changes is invisible there.
    verification_goal: Confirm what the public entrance supplies to identity on each request.
    source_finding: {phase: p0, register: system_beliefs, row: 1}
  - belief: Identity takes each of those rules from the request rather than holding them itself.
    why_it_matters: 'This is the hole: anything reaching identity another way states its own rules and is judged by them.'
    verification_goal: Establish where identity reads each rule from.
    source_finding: {phase: p0, register: system_beliefs, row: 2}
  - belief: 'A request that states a wider rule is judged by it: a second decision about an accepted person, or a decision the business never allowed, is recorded.'
    why_it_matters: The consequence the business wants closed.
    verification_goal: Establish what identity does with a decision request stating a wider rule than the business's.
    source_finding: {phase: p0, register: system_beliefs, row: 3}
  - belief: Identity checks a registration against what it must contain, finds what is missing, and registers the person anyway.
    why_it_matters: The second consequence the business wants closed.
    verification_goal: Establish what identity does with what its registration check finds.
    source_finding: {phase: p0, register: system_beliefs, row: 4}
  - belief: Through the public entrance an incomplete registration is refused before identity checks it.
    why_it_matters: Explains why nothing has shown the second fault from outside.
    verification_goal: Confirm what the public entrance refuses before identity is reached.
    source_finding: {phase: p0, register: system_beliefs, row: 5}
  - belief: The wallet function holds its own rule about who may have a wallet, rather than taking it from the request.
    why_it_matters: The business has already closed this hole once, and the change follows that precedent.
    verification_goal: Confirm where wallet's rule is held.
    source_finding: {phase: p0, register: system_beliefs, row: 6}
  assumptions: []
  constraints:
  - constraint: 'Nothing a caller sees through the public entrance changes: the same requests are admitted and refused, with the same answers.'
    source: Business author
    source_finding: {phase: p0, register: constraints, row: 1}
  - constraint: Records made under a request's own rules stay as they were made.
    source: Business author — the record is added to, never rewritten.
    source_finding: {phase: p0, register: constraints, row: 2}
  business_invariants:
  - invariant: No person is registered without a name and an address they are reached at.
    source_finding: {phase: p0, register: business_invariants, row: 1}
  - invariant: No person is decided about more than once.
    source_finding: {phase: p0, register: business_invariants, row: 2}
  - invariant: No decision other than an acceptance or a rejection is recorded.
    source_finding: {phase: p0, register: business_invariants, row: 3}
  - invariant: No rejection is recorded without its grounds.
    source_finding: {phase: p0, register: business_invariants, row: 4}
  - invariant: No authority decides about themselves.
    source_finding: {phase: p0, register: business_invariants, row: 5}
  - invariant: A business rule of identity's is held by identity, and no request changes it.
    source_finding: {phase: p0, register: business_invariants, row: 6}
  - invariant: A refusal changes no record.
    source_finding: {phase: p0, register: business_invariants, row: 7}
  lifecycle_states:
  - object: Person
    state: Unverified
    meaning: Registered, and not yet decided about. The only state a decision may be recorded from.
    source_finding: {phase: p0, register: lifecycle_states, row: 1}
  - object: Person
    state: Accepted
    meaning: An authority recorded an acceptance.
    source_finding: {phase: p0, register: lifecycle_states, row: 2}
  - object: Person
    state: Rejected
    meaning: An authority recorded a rejection, with its grounds.
    source_finding: {phase: p0, register: lifecycle_states, row: 3}
  business_events:
  - event: A person was registered
    when_it_occurs: When a person supplies a complete registration
    significance: Unchanged by this change.
    source_finding: {phase: p0, register: business_events, row: 1}
  - event: A person was accepted
    when_it_occurs: When an authority records an acceptance about an unverified person
    significance: Unchanged by this change.
    source_finding: {phase: p0, register: business_events, row: 2}
  - event: A person was rejected
    when_it_occurs: When an authority records a rejection, with grounds, about an unverified person
    significance: Unchanged by this change.
    source_finding: {phase: p0, register: business_events, row: 3}
  authority_boundaries:
  - business_object: What a registration must contain
    authoritative_owner: Identity
    source_finding: {phase: p0, register: authority_boundaries, row: 1}
  - business_object: Which people may be decided about
    authoritative_owner: Identity
    source_finding: {phase: p0, register: authority_boundaries, row: 2}
  - business_object: Which decisions may be recorded
    authoritative_owner: Identity
    source_finding: {phase: p0, register: authority_boundaries, row: 3}
  - business_object: Person, and whether the business accepts them
    authoritative_owner: Identity
    source_finding: {phase: p0, register: authority_boundaries, row: 4}
  out_of_scope:
  - item: Who may be an authority, or whether the one named is entitled to decide
    reason: Not this change.
    source_finding: {phase: p0, register: out_of_scope, row: 1}
  - item: What a registration may contain beyond its two required parts
    reason: Not this change.
    source_finding: {phase: p0, register: out_of_scope, row: 2}
  - item: The wallet function
    reason: It already holds its own rules.
    source_finding: {phase: p0, register: out_of_scope, row: 3}
  - item: People already registered or decided about
    reason: The business adds to its record and does not rewrite it.
    source_finding: {phase: p0, register: out_of_scope, row: 4}
  - item: The other five functions
    reason: Not this change.
    source_finding: {phase: p0, register: out_of_scope, row: 5}
  governance_scope:
  - scope_item: Identity
    relationship: MODIFIED
    source_finding: {phase: p0, register: governance_scope, row: 1}
  - scope_item: Wallet
    relationship: ADJACENT
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
  - criterion: A registration missing its name or its address is refused, however identity is reached, and no person is registered by it.
    source_finding: {phase: p0, register: acceptance_criteria, row: 1}
  - criterion: A decision about a person already accepted or rejected is refused, whatever the request says about who may be decided about, and no record changes.
    source_finding: {phase: p0, register: acceptance_criteria, row: 2}
  - criterion: A decision other than an acceptance or a rejection is refused, whatever the request says about which decisions are allowed.
    source_finding: {phase: p0, register: acceptance_criteria, row: 3}
  - criterion: An authority deciding about themselves is refused, whatever the request says.
    source_finding: {phase: p0, register: acceptance_criteria, row: 4}
  - criterion: A rejection stating no grounds is refused, whatever the request says.
    source_finding: {phase: p0, register: acceptance_criteria, row: 5}
  - criterion: A request stating rules of its own is judged by the business's rules, and is not refused for stating them.
    source_finding: {phase: p0, register: acceptance_criteria, row: 6}
  - criterion: Every request admitted through the public entrance before this change is admitted after it, with the same answer; every request refused there is refused, with the same answer.
    source_finding: {phase: p0, register: acceptance_criteria, row: 7}
  - criterion: Records made before this change are unchanged by it.
    source_finding: {phase: p0, register: acceptance_criteria, row: 8}
  identity_and_sameness: []
  lifecycle_transitions:
  - object: Person
    from_state: Does not exist
    to_state: Unverified
    triggered_by: A complete registration
    cascade: Unchanged by this change.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 1}
  - object: Person
    from_state: Unverified
    to_state: Accepted
    triggered_by: An authority recording an acceptance
    cascade: Unchanged by this change.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 2}
  - object: Person
    from_state: Unverified
    to_state: Rejected
    triggered_by: An authority recording a rejection with grounds
    cascade: Unchanged by this change.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 3}
  operation_refusals:
  - operation: Registering a person
    refused_when: The registration lacks the person's name or their address
    business_reason: The business said both are required.
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: Recording a decision
    refused_when: The person is not unverified
    business_reason: A person is decided about once.
    source_finding: {phase: p0, register: operation_refusals, row: 2}
  - operation: Recording a decision
    refused_when: The decision is neither an acceptance nor a rejection
    business_reason: There is no third decision.
    source_finding: {phase: p0, register: operation_refusals, row: 3}
  - operation: Recording a rejection
    refused_when: No grounds are stated
    business_reason: The business decided a rejection must say why.
    source_finding: {phase: p0, register: operation_refusals, row: 4}
  - operation: Recording a decision
    refused_when: The authority is the person decided about
    business_reason: An authority does not decide about themselves.
    source_finding: {phase: p0, register: operation_refusals, row: 5}
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
