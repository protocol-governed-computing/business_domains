# Change Seed — blockchain / identity

## Machine

```yaml
document:
  phase: p0
  domain: blockchain
  subdomain: identity
  cr: cr_05_identity
  rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0
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
  cr_type:
  - subdomain: identity
    classification: MODIFY
    rationale: Identity is built and reachable. It applies its rules as each request states them rather than holding them itself, and it registers a person whose registration it has found incomplete. Nothing is added to what identity does; its own rules are made to hold however it is reached.
  business_vocabulary:
  - term: Registration
    definition: 'What a person supplies to become known to the business: their name and the address they are reached at.'
  - term: Decision
    definition: 'What an authority records about a person: an acceptance or a rejection. There is no third.'
  - term: Authority
    definition: The person who records a decision about someone else.
  - term: Grounds
    definition: The reason an authority states when rejecting a person.
  - term: Public entrance
    definition: The way a caller outside the business reaches identity.
  - term: Business rule
    definition: 'Something the business decided about identity: what a registration must contain, who may be decided about, which decisions may be recorded.'
  requested_outcomes:
  - outcome: Identity holds what a registration must contain, and refuses a registration that does not meet it.
  - outcome: Identity holds which people an authority may decide about, and refuses a decision about anyone else, whatever the request says.
  - outcome: Identity holds which decisions may be recorded, and refuses any other, whatever the request says.
  - outcome: Everything a caller sees through the public entrance is unchanged.
  - outcome: Identity holds that an authority does not decide about themselves, and refuses such a decision, whatever the request says.
  - outcome: Identity holds that a rejection states its grounds, and refuses one that does not, whatever the request says.
  known_facts:
  - fact: A registration names the person and the address they are reached at. Both are required.
    certainty: HIGH
  - fact: A person is decided about once. Only an unverified person may be accepted or rejected.
    certainty: HIGH
  - fact: A decision is an acceptance or a rejection. There is no third.
    certainty: HIGH
  - fact: A rejection states its grounds. An acceptance may.
    certainty: HIGH
  - fact: An authority does not decide about themselves.
    certainty: HIGH
  - fact: A business rule the caller supplies is a business rule the caller can widen.
    certainty: HIGH
  - fact: The wallet function met this and closed it for itself.
    certainty: HIGH
  - fact: A registration missing its name or address is refused.
    certainty: HIGH
  - fact: What a request says about the business's rules is ignored, not refused; it is not part of the request.
    certainty: HIGH
  - fact: A decision refused because the person was already decided about changes no record.
    certainty: HIGH
  - fact: The business adds to its record and does not rewrite it.
    certainty: HIGH
  - fact: 'Every business rule of identity''s is held by identity: what a registration must contain, who may be decided about, which decisions may be recorded, that an authority does not decide about themselves, and that a rejection states its grounds.'
    certainty: HIGH
  system_beliefs:
  - belief: 'The public entrance supplies the business''s rules to identity with each request: what a registration must contain, who may be decided about, and which decisions may be recorded.'
    why_it_matters: If the entrance supplies them, a caller through it is held to them, and what changes is invisible there.
    verification_goal: Confirm what the public entrance supplies to identity on each request.
  - belief: Identity takes each of those rules from the request rather than holding them itself.
    why_it_matters: 'This is the hole: anything reaching identity another way states its own rules and is judged by them.'
    verification_goal: Establish where identity reads each rule from.
  - belief: 'A request that states a wider rule is judged by it: a second decision about an accepted person, or a decision the business never allowed, is recorded.'
    why_it_matters: The consequence the business wants closed.
    verification_goal: Establish what identity does with a decision request stating a wider rule than the business's.
  - belief: Identity checks a registration against what it must contain, finds what is missing, and registers the person anyway.
    why_it_matters: The second consequence the business wants closed.
    verification_goal: Establish what identity does with what its registration check finds.
  - belief: Through the public entrance an incomplete registration is refused before identity checks it.
    why_it_matters: Explains why nothing has shown the second fault from outside.
    verification_goal: Confirm what the public entrance refuses before identity is reached.
  - belief: The wallet function holds its own rule about who may have a wallet, rather than taking it from the request.
    why_it_matters: The business has already closed this hole once, and the change follows that precedent.
    verification_goal: Confirm where wallet's rule is held.
  assumptions: []
  constraints:
  - constraint: 'Nothing a caller sees through the public entrance changes: the same requests are admitted and refused, with the same answers.'
    source: Business author
  - constraint: Records made under a request's own rules stay as they were made.
    source: Business author — the record is added to, never rewritten.
  business_invariants:
  - invariant: No person is registered without a name and an address they are reached at.
  - invariant: No person is decided about more than once.
  - invariant: No decision other than an acceptance or a rejection is recorded.
  - invariant: No rejection is recorded without its grounds.
  - invariant: No authority decides about themselves.
  - invariant: A business rule of identity's is held by identity, and no request changes it.
  - invariant: A refusal changes no record.
  lifecycle_states:
  - object: Person
    state: Unverified
    meaning: Registered, and not yet decided about. The only state a decision may be recorded from.
  - object: Person
    state: Accepted
    meaning: An authority recorded an acceptance.
  - object: Person
    state: Rejected
    meaning: An authority recorded a rejection, with its grounds.
  business_events:
  - event: A person was registered
    when_it_occurs: When a person supplies a complete registration
    significance: Unchanged by this change.
  - event: A person was accepted
    when_it_occurs: When an authority records an acceptance about an unverified person
    significance: Unchanged by this change.
  - event: A person was rejected
    when_it_occurs: When an authority records a rejection, with grounds, about an unverified person
    significance: Unchanged by this change.
  authority_boundaries:
  - business_object: What a registration must contain
    authoritative_owner: Identity
  - business_object: Which people may be decided about
    authoritative_owner: Identity
  - business_object: Which decisions may be recorded
    authoritative_owner: Identity
  - business_object: Person, and whether the business accepts them
    authoritative_owner: Identity
  out_of_scope:
  - item: Who may be an authority, or whether the one named is entitled to decide
    reason: Not this change.
  - item: What a registration may contain beyond its two required parts
    reason: Not this change.
  - item: The wallet function
    reason: It already holds its own rules.
  - item: People already registered or decided about
    reason: The business adds to its record and does not rewrite it.
  - item: The other five functions
    reason: Not this change.
  governance_scope:
  - scope_item: Identity
    relationship: MODIFIED
  - scope_item: Wallet
    relationship: ADJACENT
  - scope_item: Transaction
    relationship: ADJACENT
  - scope_item: Mempool
    relationship: ADJACENT
  - scope_item: Block
    relationship: ADJACENT
  - scope_item: Chain
    relationship: ADJACENT
  - scope_item: Consensus
    relationship: ADJACENT
  clarification_requests: []
  acceptance_criteria:
  - criterion: A registration missing its name or its address is refused, however identity is reached, and no person is registered by it.
  - criterion: A decision about a person already accepted or rejected is refused, whatever the request says about who may be decided about, and no record changes.
  - criterion: A decision other than an acceptance or a rejection is refused, whatever the request says about which decisions are allowed.
  - criterion: An authority deciding about themselves is refused, whatever the request says.
  - criterion: A rejection stating no grounds is refused, whatever the request says.
  - criterion: A request stating rules of its own is judged by the business's rules, and is not refused for stating them.
  - criterion: Every request admitted through the public entrance before this change is admitted after it, with the same answer; every request refused there is refused, with the same answer.
  - criterion: Records made before this change are unchanged by it.
  identity_and_sameness: []
  lifecycle_transitions:
  - object: Person
    from_state: Does not exist
    to_state: Unverified
    triggered_by: A complete registration
    cascade: Unchanged by this change.
  - object: Person
    from_state: Unverified
    to_state: Accepted
    triggered_by: An authority recording an acceptance
    cascade: Unchanged by this change.
  - object: Person
    from_state: Unverified
    to_state: Rejected
    triggered_by: An authority recording a rejection with grounds
    cascade: Unchanged by this change.
  operation_refusals:
  - operation: Registering a person
    refused_when: The registration lacks the person's name or their address
    business_reason: The business said both are required.
  - operation: Recording a decision
    refused_when: The person is not unverified
    business_reason: A person is decided about once.
  - operation: Recording a decision
    refused_when: The decision is neither an acceptance nor a rejection
    business_reason: There is no third decision.
  - operation: Recording a rejection
    refused_when: No grounds are stated
    business_reason: The business decided a rejection must say why.
  - operation: Recording a decision
    refused_when: The authority is the person decided about
    business_reason: An authority does not decide about themselves.
  authority_deferrals: []
```

Reorganized faithfully from `p0_business_problem_statement.md`, including the clarifications its
author answered. Human input only — nothing here was added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

## 1. CR Type

## 2. Business Vocabulary

## 3. Requested Outcomes

## 4. Known Facts — Business Truths

## 5. Existing-System Beliefs — Requiring Verification

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

## 6. Assumptions

## 7. Constraints

## 8. Business Invariants

## 9. Lifecycle States

## 10. Business Events

## 11. Authority Boundaries

## 12. Out of Scope

## 13. Governance Scope

## 14. Clarification Requests

## 15. Acceptance Criteria

## 16. Identity and Sameness

## 17. Lifecycle Transitions

## 18. Operation Refusals

## 19. Authority Deferrals
