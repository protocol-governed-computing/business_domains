# Change Seed — blockchain / identity and wallet

## Machine

```yaml
document:
  phase: p0
  domain: blockchain
  subdomain:
  - identity
  - wallet
  cr: cr_06_routing_closure
  rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0
registers:
  subdomain_purpose: |2

    The Identity subdomain governs who an actor is and whether the business trusts them. The Wallet
    subdomain governs the wallet an accepted person is given. Both keep records the business relies on:
    the person's record, the address they claimed, the trail of moments in their history, and their
    wallet. This change decides what every identity and wallet act does when one of those records cannot
    be read or written, and states each act it changes under a new identity.
  cr_type:
  - subdomain: identity
    classification: MODIFY
    rationale: Identity's acts do not say what happens when a record fails, and one carries on past a failed lookup. Nothing is added to what identity does.
  - subdomain: wallet
    classification: MODIFY
    rationale: Wallet's act does not say what happens when a record fails, and three of its steps carry on past a failure. Nothing is added to what wallet does.
  business_vocabulary:
  - term: Record
    definition: 'Something the business keeps: a person''s record, a claimed address, a trail of moments, or a wallet.'
  - term: Failed record
    definition: A record that could not be read or written, because the store was unreachable or answered with an error.
  - term: Act
    definition: 'One thing a caller asks identity or wallet to do: register, accept, reject, or create a wallet.'
  - term: Rejected
    definition: The ending of an act that did not succeed.
  - term: Published
    definition: Sealed into a composition that was released and cited.
  - term: Successor
    definition: The new identity that states what an act does after this change.
  - term: Stood down
    definition: Replaced by a declared successor, kept in the record and out of reach.
  requested_outcomes:
  - outcome: Every identity and wallet act ends as rejected when a record it needs fails.
  - outcome: An act stops at the step whose record failed, and nothing after it runs.
  - outcome: Everything else identity and wallet do is unchanged.
  - outcome: Each act whose meaning this changes has a successor, and its published identity is stood down unchanged.
  - outcome: Everything in force that names a stood-down act names its successor.
  known_facts:
  - fact: An act either succeeds or is rejected. There is no third ending.
    certainty: HIGH
  - fact: A rejection changes no record.
    certainty: HIGH
  - fact: The business adds to its record and does not rewrite it.
    certainty: HIGH
  - fact: A failed record ends the act. Nothing retries.
    certainty: HIGH
  - fact: A failed record ends as rejected, not as a separate failure.
    certainty: HIGH
  - fact: Every identity and wallet act reads or writes a record the business keeps.
    certainty: HIGH
  - fact: Identity is fixed at publication; a change of meaning is a new identity.
    certainty: HIGH
  - fact: A published identity stays in the record, stood down, when a successor replaces it.
    certainty: HIGH
  - fact: A re-point changes which act a referrer names, and nothing else about it.
    certainty: HIGH
  system_beliefs:
  - belief: Most identity and wallet acts stop without a declared ending when a record fails.
    why_it_matters: The caller cannot tell an intended refusal from an unplanned failure.
    verification_goal: Establish, for each act, what happens when each record it touches fails.
  - belief: When an acceptance's lookup of the person fails, identity carries on and records the acceptance.
    why_it_matters: This is the failure the business wants closed first.
    verification_goal: Establish what identity does when the lookup fails during an acceptance.
  - belief: Three of wallet's steps carry on past a failed record in the same way.
    why_it_matters: The same gap, in the same form, in the other subdomain.
    verification_goal: Establish which wallet steps carry on past a failed record.
  - belief: Each act already has a rejected ending.
    why_it_matters: The change can end a failed record there without adding an ending.
    verification_goal: Confirm every identity and wallet act has a rejected ending.
  - belief: Every identity and wallet act this change touches was published in v5.
    why_it_matters: Each one it changes needs a successor.
    verification_goal: Establish which touched acts the v5 composition holds.
  - belief: Entrances and intents name the workflows they start, and workflows name the contracts they run.
    why_it_matters: Each referrer of a replaced act must be re-pointed.
    verification_goal: Establish everything that names each replaced act, by full name and by short code.
  assumptions: []
  constraints:
  - constraint: Nothing changes for an act whose records are all read and written.
    source: Business author
  - constraint: Records made before a failure stay as they were made.
    source: Business author — the record is added to, never rewritten.
  - constraint: No ending is added.
    source: Business author — a failure ends as rejected.
  - constraint: No published identity changes what it says, except to be stood down.
    source: Business author — identity is fixed at publication.
  business_invariants:
  - invariant: No act carries on past a record it could not read or write.
  - invariant: Every act ends as succeeded or rejected.
  - invariant: A refusal changes no record.
  - invariant: A published identity means what it meant when it was published.
  lifecycle_states:
  - object: Person
    state: Unverified
    meaning: Registered, and not yet decided about. Unchanged by this change.
  - object: Person
    state: Accepted
    meaning: An authority recorded an acceptance. Unchanged by this change.
  - object: Person
    state: Rejected
    meaning: An authority recorded a rejection, with its grounds. Unchanged by this change.
  business_events:
  - event: A person was registered
    when_it_occurs: When a person supplies a complete registration and every record is written
    significance: Unchanged; it is not announced when a record fails.
  - event: A person was accepted
    when_it_occurs: When an authority records an acceptance and every record is written
    significance: Unchanged; it is not announced when a record fails.
  - event: A person was rejected
    when_it_occurs: When an authority records a rejection and every record is written
    significance: Unchanged; it is not announced when a record fails.
  - event: A wallet was created
    when_it_occurs: When an accepted person is given a wallet and every record is written
    significance: Unchanged; it is not announced when a record fails.
  authority_boundaries:
  - business_object: What an identity act does when a record fails
    authoritative_owner: Identity
  - business_object: What a wallet act does when a record fails
    authoritative_owner: Wallet
  out_of_scope:
  - item: Telling a refusal apart from a failure
    reason: A later decision; the business keeps two endings.
  - item: Trying a failed record again
    reason: The business decided a failed record ends the act.
  - item: Records made before a failure
    reason: The business adds to its record and does not rewrite it.
  - item: The other five functions
    reason: Not this change.
  governance_scope:
  - scope_item: Identity
    relationship: MODIFIED
  - scope_item: Wallet
    relationship: MODIFIED
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
  - criterion: An acceptance whose lookup of the person fails is rejected, and no acceptance is recorded.
  - criterion: Every identity and wallet act ends as rejected when a record it needs fails.
  - criterion: An act stops at the step whose record failed, and nothing after it runs.
  - criterion: Every act whose records are all read and written ends exactly as it did before this change.
  - criterion: Each act whose meaning this changes is stated under a new identity, and the published identity is unchanged except for its stand-down.
  - criterion: Nothing in force names a stood-down act.
  - criterion: Records made before a failure are unchanged by it.
  identity_and_sameness:
  - business_object: Act
    identified_by: Its identity
    two_are_the_same_when: Its declaration means what the published declaration meant
  lifecycle_transitions:
  - object: Published act
    from_state: In force
    to_state: Stood down
    triggered_by: This change adds its successor
    cascade: Whatever names it is re-pointed
  operation_refusals:
  - operation: Registering a person
    refused_when: A record the registration needs fails
    business_reason: A failed record ends the act.
  - operation: Accepting a person
    refused_when: A record the acceptance needs fails
    business_reason: A failed record ends the act.
  - operation: Rejecting a person
    refused_when: A record the rejection needs fails
    business_reason: A failed record ends the act.
  - operation: Creating a wallet
    refused_when: A record the wallet needs fails
    business_reason: A failed record ends the act.
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
