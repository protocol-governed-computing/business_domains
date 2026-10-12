# Change Seed — blockchain / identity and wallet

## Machine

```yaml
document:
  phase: p0
  domain: blockchain
  subdomain:
  - identity
  - wallet
  cr: cr_07_own_values
  rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0
registers:
  subdomain_purpose: |2

    The Identity subdomain governs who an actor is and whether the business trusts them. The Wallet
    subdomain governs the wallet an accepted person is given. Each act records a moment on a trail, and
    wallet writes the record of every wallet it creates. This change makes each act state the values only
    the business may decide: the moment it records, the trail it records it on, where a contact address
    sits, and every value of a new wallet's record. A request no longer supplies them.
  cr_type:
  - subdomain: identity
    classification: MODIFY
    rationale: Identity's acts take the moment, the trail and the contact address's place from the request. Nothing is added to what identity does.
  - subdomain: wallet
    classification: MODIFY
    rationale: Wallet's act takes the wallet's record, its identity's prefix and its moment from the request. Nothing is added to what wallet does.
  business_vocabulary:
  - term: Moment
    definition: 'One occurrence in a person''s or a wallet''s history: registered, accepted, rejected, or wallet created.'
  - term: Trail
    definition: The ordered record of moments the business keeps and never rewrites.
  - term: Contact address
    definition: The address that makes one person one actor.
  - term: Wallet record
    definition: 'What the business holds about a wallet: its holder, balance, denomination, classification and state.'
  - term: Entrance
    definition: The way a caller outside the composition starts an act.
  - term: Entry point
    definition: The declaration of what a request to start an act must carry.
  - term: Act
    definition: 'One thing a caller asks identity or wallet to do: register, accept, reject, or create a wallet.'
  - term: Successor
    definition: The new identity that states what an act, entrance or entry point does after this change.
  - term: Retired by record
    definition: Replaced by a declared successor, removed from the registry, and recorded as retired.
  requested_outcomes:
  - outcome: Every identity and wallet act states the moment it records and the trail it records it on.
  - outcome: Registration states where the contact address sits and what kind of value it is.
  - outcome: Wallet states every value of the record it creates.
  - outcome: Wallet states the prefix of a wallet's identity.
  - outcome: No entrance sends a value its act states.
  - outcome: Everything else identity and wallet do is unchanged.
  - outcome: Each act, entrance and entry point whose meaning this changes has a successor, and its predecessor is retired by record.
  known_facts:
  - fact: An act either succeeds or is rejected. There is no third ending.
    certainty: HIGH
  - fact: The business adds to its record and does not rewrite it.
    certainty: HIGH
  - fact: Identity is fixed at publication; a change of meaning is a new identity.
    certainty: HIGH
  - fact: A predecessor is retired by record when its successor replaces it.
    certainty: HIGH
  - fact: An acceptance may state its grounds or not. A rejection must state them.
    certainty: HIGH
  - fact: A new wallet's holder is the accepted person identity holds.
    certainty: HIGH
  - fact: A new wallet's balance is zero, its denomination BACHI, its classification DEFAULT and its state ACTIVE.
    certainty: HIGH
  - fact: Callers send the same inputs through each entrance after this change as before it.
    certainty: HIGH
  system_beliefs:
  - belief: Each identity act takes the moment it records and the trail it records it on from the request.
    why_it_matters: A direct caller can name a moment that did not happen.
    verification_goal: Establish, for each identity act, where the moment and the trail come from.
  - belief: Registration takes where the contact address sits, and what kind of value it is, from the request.
    why_it_matters: A caller can point the claim at another field.
    verification_goal: Establish where registration's claim reads the address's place and kind.
  - belief: Wallet's record is whatever the request supplies.
    why_it_matters: A caller can create a wallet for another holder, with any balance.
    verification_goal: Establish where each value of a new wallet's record comes from.
  - belief: The wallet entry point declares the prefix of the wallet's identity as a request value.
    why_it_matters: A caller chooses part of the wallet's identity.
    verification_goal: Establish what the wallet entry point declares.
  - belief: The three identity entrances send the moment, the trail and the address's place on every request.
    why_it_matters: Each entrance changes, and so needs a successor.
    verification_goal: Establish what each entrance hands its act.
  - belief: The business's check of its entry points reports ten undeclared request values on identity and wallet acts.
    why_it_matters: It is the measure this change closes.
    verification_goal: Establish the findings the entry-point check reports for blockchain.
  - belief: Entrances, entry points and runtime bindings name the acts they start or bind.
    why_it_matters: Each referrer of a replaced act must be re-pointed.
    verification_goal: Establish everything that names each replaced act, entrance and entry point.
  assumptions: []
  constraints:
  - constraint: Nothing changes for a request that supplies the values the acts now state.
    source: Business author
  - constraint: Records made before this change stay as they were made.
    source: Business author — the record is added to, never rewritten.
  - constraint: No ending is added.
    source: Business author — an act succeeds or is rejected.
  - constraint: Callers through an entrance send the same inputs as before.
    source: Business author
  business_invariants:
  - invariant: The moment an act records is the moment that happened.
  - invariant: A wallet's holder is the person identity accepted.
  - invariant: A new wallet holds nothing.
  - invariant: A value only the business may decide is never taken from a request.
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
  - object: Wallet
    state: Active
    meaning: Given to an accepted person, holding nothing. Every new wallet starts here.
  business_events:
  - event: A person was registered
    when_it_occurs: When a person supplies a complete registration
    significance: Unchanged; its moment is now the act's own.
  - event: A person was accepted
    when_it_occurs: When an authority records an acceptance
    significance: Unchanged; its moment is now the act's own.
  - event: A person was rejected
    when_it_occurs: When an authority records a rejection with its grounds
    significance: Unchanged; its moment is now the act's own.
  - event: A wallet was created
    when_it_occurs: When an accepted person is given a wallet
    significance: Unchanged; the wallet's record and moment are now the act's own.
  authority_boundaries:
  - business_object: The moments identity records and the trail they go on
    authoritative_owner: Identity
  - business_object: Where a contact address sits in a person's record
    authoritative_owner: Identity
  - business_object: A new wallet's record, its identity's prefix and its moment
    authoritative_owner: Wallet
  out_of_scope:
  - item: An acceptance an entrance cannot answer without grounds
    reason: Waits on the transport standard letting an entrance's answer leave a field out.
  - item: Records made before this change
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
  - criterion: A registration records the person as registered, whatever moment or trail the request names.
  - criterion: An acceptance records the person as accepted, whatever moment or trail the request names.
  - criterion: A rejection records the person as rejected, whatever moment or trail the request names.
  - criterion: A registration claims the person's contact address, whatever place the request names for it.
  - criterion: A new wallet is held by the accepted person, with a balance of zero, BACHI, DEFAULT and ACTIVE, whatever the request states.
  - criterion: A new wallet's identity carries the business's prefix, whatever the request states.
  - criterion: A new wallet's trail records that the wallet was created, whatever moment the request names.
  - criterion: Every request admitted through an entrance before this change is admitted after it, and every request refused there is refused.
  - criterion: The entry-point check reports no undeclared request value on any identity or wallet act.
  - criterion: Each act, entrance and entry point whose meaning this changes is stated under a new identity, and its predecessor is retired by record.
  - criterion: Nothing in force names a retired identity.
  identity_and_sameness:
  - business_object: Act, entrance or entry point
    identified_by: Its identity
    two_are_the_same_when: Its declaration means what the published declaration meant
  lifecycle_transitions:
  - object: Act, entrance or entry point
    from_state: In force
    to_state: Retired by record
    triggered_by: This change adds its successor
    cascade: Whatever names it is re-pointed
  operation_refusals: []
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
