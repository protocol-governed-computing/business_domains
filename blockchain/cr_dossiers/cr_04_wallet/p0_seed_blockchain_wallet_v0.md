# Change Seed — blockchain / wallet

## Machine

```yaml
document:
  phase: p0
  domain: blockchain
  subdomain: wallet
  cr: cr_04_wallet
  rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0
registers:
  subdomain_purpose: |2

    The Wallet subdomain governs where a person the business has accepted holds value. It holds one
    record for each wallet, the balance that wallet carries, the address others may pay to, and the
    state that says whether the wallet is in use. A wallet belongs to exactly one accepted person and
    follows from their acceptance rather than from a separate request. Wallet is the unit the rest of
    the project operates on: a transaction moves value between wallets, a block records transactions,
    and consensus finalises blocks. It does not govern whether a person is accepted, who may decide
    that, or how value moves once a wallet holds it.
  cr_type:
  - subdomain: wallet
    classification: EXTEND_SUBDOMAIN
    rationale: 'Wallet was built by a first pass of this change and is in the business''s hands. Two things it was asked for are missing: the act does not say it reads the records identity owns, and it gives a wallet to a person nobody accepted.'
  - subdomain: identity
    classification: MODIFY
    rationale: 'Identity is modified by this change: it declares an announcement of acceptance that it does not make, and wallet is the first function that needs to hear it. One unenforced rule of identity''s is corrected at the same time.'
  business_vocabulary:
  - term: Wallet
    definition: Where an accepted person holds value. Belongs to exactly one person.
  - term: Holder
    definition: The accepted person a wallet belongs to.
  - term: Balance
    definition: What a wallet currently carries. Never negative.
  - term: Denomination
    definition: The currency a wallet's balance is expressed in.
  - term: Classification
    definition: What kind of wallet this is — the business distinguishes a default wallet from a private, business, savings, investment, mint, burn or pool wallet.
  - term: Address
    definition: What others may pay to. Public; the business keeps no secret material behind it.
  - term: Acceptance
    definition: The moment an authority records that the business accepts a person.
  - term: Grounds
    definition: The reason an authority states when rejecting a person.
  - term: Trail
    definition: The business's record of moments that occurred, added to and never rewritten.
  - term: Reach
    definition: An act reading records another part of the business owns.
  - term: Binding
    definition: What connects an act, when it runs, to the descriptions of the records it works against.
  - term: Consulted
    definition: The records an act reads and never writes.
  requested_outcomes:
  - outcome: Each accepted person has a wallet, created once, when they are accepted.
  - outcome: The moments identity already declares are announced, so that acceptance can be acted on.
  - outcome: A rejection that states no grounds is refused.
  - outcome: The creation of a wallet is recorded as a moment on the business's trail.
  - outcome: The act that creates a wallet declares that it reads the records identity owns, and never writes them.
  - outcome: A wallet is refused to a person the business has not accepted.
  known_facts:
  - fact: A wallet belongs to exactly one person.
    certainty: HIGH
  - fact: A wallet cannot exist for a person the business does not hold.
    certainty: HIGH
  - fact: A wallet's balance is never negative.
    certainty: HIGH
  - fact: A wallet is denominated in a currency, with a default the business supplies.
    certainty: HIGH
  - fact: A wallet carries a classification, drawn from a set the business fixes.
    certainty: HIGH
  - fact: A wallet is active when created, may become inactive, and may be closed. Closed is the end.
    certainty: HIGH
  - fact: A wallet has an address others may pay to, and the business keeps no secret material behind it.
    certainty: HIGH
  - fact: Two wallets never share an identity.
    certainty: HIGH
  - fact: Asking again for a wallet that already exists changes nothing.
    certainty: HIGH
  - fact: A wallet follows acceptance; it is not something a person asks for separately.
    certainty: HIGH
  - fact: The business decided a rejection must state why.
    certainty: HIGH
  - fact: Nothing after wallet can be built without it — transaction, block and consensus all depend on it.
    certainty: HIGH
  - fact: Notifying a person that their wallet was created is dropped from this change.
    certainty: HIGH
  - fact: A new wallet holds a balance of zero.
    certainty: HIGH
  - fact: A wallet created by this change always carries the default classification.
    certainty: HIGH
  - fact: Every wallet is denominated in one currency, the business's own, the same for all.
    certainty: HIGH
  - fact: One person holds one wallet.
    certainty: HIGH
  - fact: The key material behind a wallet's address is supplied to the business, not generated by it.
    certainty: HIGH
  - fact: The business must be able to show that a wallet was created, for whom, when, and with what denomination and classification. Nothing further.
    certainty: HIGH
  - fact: Acceptance stands on its own. Failing to give an accepted person a wallet does not un-accept them.
    certainty: HIGH
  - fact: A wallet is never created for a person who was rejected, or one still unverified.
    certainty: HIGH
  - fact: Whether a person exists and has been accepted is a fact identity owns and alone should state.
    certainty: HIGH
  - fact: The wallet keeps no copy of who exists; a second copy of one truth can disagree with the thing it describes.
    certainty: HIGH
  - fact: An act may read records another part of the business owns, provided it declares what it consults and never writes them.
    certainty: HIGH
  - fact: A reach added to a built artifact by hand works, passes every check, and is a reach no reviewer saw.
    certainty: HIGH
  system_beliefs:
  - belief: 'Identity is built and reachable: a person registers and is admitted unverified, and an authority then accepts or rejects them.'
    why_it_matters: Wallet follows acceptance, so acceptance must already be a thing the business does.
    verification_goal: Confirm the two identity operations exist and that acceptance is one of the recorded outcomes.
  - belief: A person keeps the details they registered with when a decision is recorded about them.
    why_it_matters: A wallet belongs to a person; if the person's record is thinned by a decision, the wallet's holder is thin too.
    verification_goal: Confirm a decision leaves the registered details untouched.
  - belief: Identity declares that it announces an acceptance, and does not actually announce it.
    why_it_matters: Wallet is the first function that needs to hear it. If nothing is announced, nothing downstream can follow acceptance.
    verification_goal: Confirm the acceptance moment is declared, and establish whether it is ever announced.
  - belief: A rejection stating no grounds is currently accepted and recorded rather than refused.
    why_it_matters: The identity a wallet depends on should be one whose own stated rules hold.
    verification_goal: Confirm whether a rejection with no grounds is refused today.
  - belief: No wallet exists anywhere in the business today.
    why_it_matters: Determines whether this creates a function or extends one.
    verification_goal: Confirm no wallet record, balance or address is held anywhere.
  - belief: A wallet design was worked out in an earlier system, including which of a wallet's details are the business's own and which were implementation detail.
    why_it_matters: The business need not re-derive decisions it already made.
    verification_goal: Establish which of those decisions the current business still holds to.
  - belief: The act that creates a wallet reads records identity owns and declares nothing about them.
    why_it_matters: It is one of the two things missing from what was built.
    verification_goal: Establish what the act declares today about the records it reads.
  - belief: The business permits an act to declare the bindings it consults, and refuses a write through one.
    why_it_matters: Says the capability exists and this change uses it rather than inventing it.
    verification_goal: Confirm what is admitted, and what happens on a write through a consulted record.
  - belief: A person nobody accepted is given a wallet today.
    why_it_matters: The other missing thing, and the business's own rule going unenforced.
    verification_goal: Establish what the act does with the person's state after it reads it.
  assumptions:
  - assumption: The classifications the business named are still the ones it wants.
    basis: They were fixed in an earlier design and have not been revisited.
  - assumption: An accepted person expects a wallet without asking for one.
    basis: 'Stated by the author: acceptance was supposed to give them one.'
  - assumption: The one currency the business denominates in is the one the earlier design used.
    basis: The business stated one currency for all wallets and did not rename it.
  constraints:
  - constraint: No one is notified that a wallet was created. The moment is recorded; who is told is a later question.
    source: Business author
  - constraint: No value moves. A wallet is created holding what the business says a new wallet holds, and nothing moves it.
    source: Business author
  - constraint: The business does not go back for people already accepted.
    source: Business author — the record is added to, never rewritten.
  - constraint: The same request must produce the same wallet. The business will not accept a system whose output it can neither reproduce nor check.
    source: Business author
  - constraint: Only a default wallet is created. The other classifications remain named and unused until a second one is actually needed.
    source: Business author
  business_invariants:
  - invariant: A wallet has exactly one holder.
  - invariant: A wallet's balance is never negative.
  - invariant: No two wallets share an identity.
  - invariant: No wallet exists for a person the business does not hold.
  - invariant: A person holds at most one wallet.
  - invariant: No wallet exists for a person who is not accepted.
  - invariant: A recorded moment is never changed or removed.
  - invariant: The act that creates a wallet declares every binding it consults.
  - invariant: Identity is the only writer of what identity owns.
  - invariant: No wallet exists for a person the business has not accepted.
  lifecycle_states:
  - object: Wallet
    state: Active
    meaning: In use. The state a wallet is in when created.
  - object: Wallet
    state: Inactive
    meaning: Not in use, but not ended.
  - object: Wallet
    state: Closed
    meaning: Ended. Nothing follows.
  business_events:
  - event: A wallet was created
    when_it_occurs: When an accepted person is given their wallet
    significance: The business can show when a person came to hold value, and for whom.
  - event: A person was accepted
    when_it_occurs: When an authority records acceptance
    significance: Wallet follows from it; it is the moment wallet waits on.
  - event: A person was registered
    when_it_occurs: When a person supplies their details and is admitted unverified
    significance: Declared by identity today and not announced.
  - event: A person was rejected
    when_it_occurs: When an authority records a rejection
    significance: Declared by identity today and not announced.
  authority_boundaries:
  - business_object: Wallet
    authoritative_owner: Wallet
  - business_object: Balance
    authoritative_owner: Wallet
  - business_object: Address
    authoritative_owner: Wallet
  - business_object: Person, and whether the business accepts them
    authoritative_owner: Identity
  - business_object: Grounds stated for a rejection
    authoritative_owner: Identity
  out_of_scope:
  - item: Notifying anyone that a wallet was created
    reason: Dropped by the business. The moment is recorded; who is told, and how, is a later question.
  - item: Moving value — transactions, transfers, any change of balance
    reason: A wallet is created and nothing moves it yet.
  - item: Closing or deactivating a wallet
    reason: The lifecycle is declared; only creation is built.
  - item: Who may be an authority, or whether the one named is entitled to decide
    reason: Not this change.
  - item: People already accepted, who have no wallet
    reason: The business does not go back for them.
  - item: Recovering a wallet whose holder has lost access
    reason: A later change.
  - item: Transaction ordering
    reason: Carried in an earlier design and deliberately left dormant, having no consumer.
  - item: The other five functions
    reason: Not this change.
  governance_scope:
  - scope_item: Wallet
    relationship: CREATED
  - scope_item: Identity
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
  - criterion: A person who is accepted holds a wallet afterwards, and the business can show its identity, address, denomination and classification.
  - criterion: A person who is not accepted holds no wallet.
  - criterion: A wallet names exactly one holder, and that holder is a person the business holds.
  - criterion: Accepting the same person again does not produce a second wallet.
  - criterion: The business can show the moment a wallet was created, for whom, and when.
  - criterion: A rejection stating no grounds is refused, and no person is rejected by it.
  - criterion: The moments identity declares are announced when they occur.
  - criterion: No recorded moment is changed or removed by anything this change introduces.
  - criterion: The act declares the records it reads, and a reviewer reads that in the design rather than in the built act.
  - criterion: Identity's records are unchanged by every wallet act, including the refused ones.
  - criterion: A person the business has not accepted is refused a wallet, and none is recorded for them.
  identity_and_sameness:
  - business_object: Wallet
    identified_by: Its own wallet identity
    two_are_the_same_when: They carry the same wallet identity.
  - business_object: Holder
    identified_by: The person identity held by Identity
    two_are_the_same_when: They are the same person to Identity.
  lifecycle_transitions:
  - object: Wallet
    from_state: Does not exist
    to_state: Active
    triggered_by: A person being accepted
    cascade: A moment is recorded on the trail. Nothing else follows.
  - object: Wallet
    from_state: Active
    to_state: Inactive
    triggered_by: Out of scope for this change
    cascade: null
  - object: Wallet
    from_state: Active or Inactive
    to_state: Closed
    triggered_by: Out of scope for this change
    cascade: null
  operation_refusals:
  - operation: Creating a wallet
    refused_when: The person is not one the business holds
    business_reason: A wallet cannot exist for a person who does not exist.
  - operation: Creating a wallet
    refused_when: The person has not been accepted, or was rejected
    business_reason: A wallet follows acceptance and nothing else.
  - operation: Creating a wallet
    refused_when: The person already holds a wallet
    business_reason: One person holds one wallet; asking again changes nothing.
  - operation: Recording a rejection
    refused_when: No grounds are stated
    business_reason: The business decided a rejection must say why.
  authority_deferrals:
  - business_object: Transaction ordering
    deferred_to: Transaction
    until: Transaction exists and needs it.
  - business_object: Movement of value in and out of a wallet
    deferred_to: Transaction
    until: Transaction exists.
  - business_object: Notifying a person that their wallet was created
    deferred_to: A later change
    until: The business decides who is told and how.
  - business_object: Recovery of a wallet whose holder has lost access
    deferred_to: A later change
    until: The business decides what recovery means.
```

Reorganized faithfully from `p0_business_problem_statement.md`. Human input only — nothing here was
added, decided or designed by the pipeline. The clarifications its author has not yet answered are
carried forward as questions in §14, unanswered.

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
