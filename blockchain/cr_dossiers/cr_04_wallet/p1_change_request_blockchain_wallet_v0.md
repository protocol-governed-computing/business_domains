# Stage 1 — Change Request: Clarification & Fact Capture: blockchain / wallet

## Machine

```yaml
document:
  phase: p1
  domain: blockchain
  subdomain: wallet
  cr: cr_04_wallet
  rule_set: transformation.schemas.REGISTER_SCHEMA_P1_V0
registers:
  cr_type:
  - subdomain: wallet
    classification: EXTEND_SUBDOMAIN
    rationale: 'Wallet was built by a first pass of this change and is in the business''s hands. Two things it was asked for are missing: the act does not say it reads the records identity owns, and it gives a wallet to a person nobody accepted.'
    source_finding: {phase: p0, register: cr_type, row: 1}
  - subdomain: identity
    classification: MODIFY
    rationale: 'Identity is modified by this change: it declares an announcement of acceptance that it does not make, and wallet is the first function that needs to hear it. One unenforced rule of identity''s is corrected at the same time.'
    source_finding: {phase: p0, register: cr_type, row: 2}
  business_vocabulary:
  - term: Wallet
    definition: Where an accepted person holds value. Belongs to exactly one person.
    source_finding: {phase: p0, register: business_vocabulary, row: 1}
  - term: Holder
    definition: The accepted person a wallet belongs to.
    source_finding: {phase: p0, register: business_vocabulary, row: 2}
  - term: Balance
    definition: What a wallet currently carries. Never negative.
    source_finding: {phase: p0, register: business_vocabulary, row: 3}
  - term: Denomination
    definition: The currency a wallet's balance is expressed in.
    source_finding: {phase: p0, register: business_vocabulary, row: 4}
  - term: Classification
    definition: What kind of wallet this is — the business distinguishes a default wallet from a private, business, savings, investment, mint, burn or pool wallet.
    source_finding: {phase: p0, register: business_vocabulary, row: 5}
  - term: Address
    definition: What others may pay to. Public; the business keeps no secret material behind it.
    source_finding: {phase: p0, register: business_vocabulary, row: 6}
  - term: Acceptance
    definition: The moment an authority records that the business accepts a person.
    source_finding: {phase: p0, register: business_vocabulary, row: 7}
  - term: Grounds
    definition: The reason an authority states when rejecting a person.
    source_finding: {phase: p0, register: business_vocabulary, row: 8}
  - term: Trail
    definition: The business's record of moments that occurred, added to and never rewritten.
    source_finding: {phase: p0, register: business_vocabulary, row: 9}
  - term: Reach
    definition: An act reading records another part of the business owns.
    source_finding: {phase: p0, register: business_vocabulary, row: 10}
  - term: Binding
    definition: What connects an act, when it runs, to the descriptions of the records it works against.
    source_finding: {phase: p0, register: business_vocabulary, row: 11}
  - term: Consulted
    definition: The records an act reads and never writes.
    source_finding: {phase: p0, register: business_vocabulary, row: 12}
  requested_outcomes:
  - outcome: Each accepted person has a wallet, created once, when they are accepted.
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - outcome: The moments identity already declares are announced, so that acceptance can be acted on.
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - outcome: A rejection that states no grounds is refused.
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  - outcome: The creation of a wallet is recorded as a moment on the business's trail.
    source_finding: {phase: p0, register: requested_outcomes, row: 4}
  - outcome: The act that creates a wallet declares that it reads the records identity owns, and never writes them.
    source_finding: {phase: p0, register: requested_outcomes, row: 5}
  - outcome: A wallet is refused to a person the business has not accepted.
    source_finding: {phase: p0, register: requested_outcomes, row: 6}
  known_facts:
  - fact: A wallet belongs to exactly one person.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 1}
  - fact: A wallet cannot exist for a person the business does not hold.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 2}
  - fact: A wallet's balance is never negative.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 3}
  - fact: A wallet is denominated in a currency, with a default the business supplies.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 4}
  - fact: A wallet carries a classification, drawn from a set the business fixes.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 5}
  - fact: A wallet is active when created, may become inactive, and may be closed. Closed is the end.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 6}
  - fact: A wallet has an address others may pay to, and the business keeps no secret material behind it.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 7}
  - fact: Two wallets never share an identity.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 8}
  - fact: Asking again for a wallet that already exists changes nothing.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 9}
  - fact: A wallet follows acceptance; it is not something a person asks for separately.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 10}
  - fact: The business decided a rejection must state why.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 11}
  - fact: Nothing after wallet can be built without it — transaction, block and consensus all depend on it.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 12}
  - fact: Notifying a person that their wallet was created is dropped from this change.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 13}
  - fact: A new wallet holds a balance of zero.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 14}
  - fact: A wallet created by this change always carries the default classification.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 15}
  - fact: Every wallet is denominated in one currency, the business's own, the same for all.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 16}
  - fact: One person holds one wallet.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 17}
  - fact: The key material behind a wallet's address is supplied to the business, not generated by it.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 18}
  - fact: The business must be able to show that a wallet was created, for whom, when, and with what denomination and classification. Nothing further.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 19}
  - fact: Acceptance stands on its own. Failing to give an accepted person a wallet does not un-accept them.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 20}
  - fact: A wallet is never created for a person who was rejected, or one still unverified.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 21}
  - fact: Whether a person exists and has been accepted is a fact identity owns and alone should state.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 22}
  - fact: The wallet keeps no copy of who exists; a second copy of one truth can disagree with the thing it describes.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 23}
  - fact: An act may read records another part of the business owns, provided it declares what it consults and never writes them.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 24}
  - fact: A reach added to a built artifact by hand works, passes every check, and is a reach no reviewer saw.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 25}
  system_beliefs:
  - belief: 'Identity is built and reachable: a person registers and is admitted unverified, and an authority then accepts or rejects them.'
    why_it_matters: Wallet follows acceptance, so acceptance must already be a thing the business does.
    verification_goal: Confirm the two identity operations exist and that acceptance is one of the recorded outcomes.
    source_finding: {phase: p0, register: system_beliefs, row: 1}
  - belief: A person keeps the details they registered with when a decision is recorded about them.
    why_it_matters: A wallet belongs to a person; if the person's record is thinned by a decision, the wallet's holder is thin too.
    verification_goal: Confirm a decision leaves the registered details untouched.
    source_finding: {phase: p0, register: system_beliefs, row: 2}
  - belief: Identity declares that it announces an acceptance, and does not actually announce it.
    why_it_matters: Wallet is the first function that needs to hear it. If nothing is announced, nothing downstream can follow acceptance.
    verification_goal: Confirm the acceptance moment is declared, and establish whether it is ever announced.
    source_finding: {phase: p0, register: system_beliefs, row: 3}
  - belief: A rejection stating no grounds is currently accepted and recorded rather than refused.
    why_it_matters: The identity a wallet depends on should be one whose own stated rules hold.
    verification_goal: Confirm whether a rejection with no grounds is refused today.
    source_finding: {phase: p0, register: system_beliefs, row: 4}
  - belief: No wallet exists anywhere in the business today.
    why_it_matters: Determines whether this creates a function or extends one.
    verification_goal: Confirm no wallet record, balance or address is held anywhere.
    source_finding: {phase: p0, register: system_beliefs, row: 5}
  - belief: A wallet design was worked out in an earlier system, including which of a wallet's details are the business's own and which were implementation detail.
    why_it_matters: The business need not re-derive decisions it already made.
    verification_goal: Establish which of those decisions the current business still holds to.
    source_finding: {phase: p0, register: system_beliefs, row: 6}
  - belief: The act that creates a wallet reads records identity owns and declares nothing about them.
    why_it_matters: It is one of the two things missing from what was built.
    verification_goal: Establish what the act declares today about the records it reads.
    source_finding: {phase: p0, register: system_beliefs, row: 7}
  - belief: The business permits an act to declare the bindings it consults, and refuses a write through one.
    why_it_matters: Says the capability exists and this change uses it rather than inventing it.
    verification_goal: Confirm what is admitted, and what happens on a write through a consulted record.
    source_finding: {phase: p0, register: system_beliefs, row: 8}
  - belief: A person nobody accepted is given a wallet today.
    why_it_matters: The other missing thing, and the business's own rule going unenforced.
    verification_goal: Establish what the act does with the person's state after it reads it.
    source_finding: {phase: p0, register: system_beliefs, row: 9}
  assumptions:
  - assumption: The classifications the business named are still the ones it wants.
    basis: They were fixed in an earlier design and have not been revisited.
    source_finding: {phase: p0, register: assumptions, row: 1}
  - assumption: An accepted person expects a wallet without asking for one.
    basis: 'Stated by the author: acceptance was supposed to give them one.'
    source_finding: {phase: p0, register: assumptions, row: 2}
  - assumption: The one currency the business denominates in is the one the earlier design used.
    basis: The business stated one currency for all wallets and did not rename it.
    source_finding: {phase: p0, register: assumptions, row: 3}
  constraints:
  - constraint: No one is notified that a wallet was created. The moment is recorded; who is told is a later question.
    source: Business author
    source_finding: {phase: p0, register: constraints, row: 1}
  - constraint: No value moves. A wallet is created holding what the business says a new wallet holds, and nothing moves it.
    source: Business author
    source_finding: {phase: p0, register: constraints, row: 2}
  - constraint: The business does not go back for people already accepted.
    source: Business author — the record is added to, never rewritten.
    source_finding: {phase: p0, register: constraints, row: 3}
  - constraint: The same request must produce the same wallet. The business will not accept a system whose output it can neither reproduce nor check.
    source: Business author
    source_finding: {phase: p0, register: constraints, row: 4}
  - constraint: Only a default wallet is created. The other classifications remain named and unused until a second one is actually needed.
    source: Business author
    source_finding: {phase: p0, register: constraints, row: 5}
  business_invariants:
  - invariant: A wallet has exactly one holder.
    source_finding: {phase: p0, register: business_invariants, row: 1}
  - invariant: A wallet's balance is never negative.
    source_finding: {phase: p0, register: business_invariants, row: 2}
  - invariant: No two wallets share an identity.
    source_finding: {phase: p0, register: business_invariants, row: 3}
  - invariant: No wallet exists for a person the business does not hold.
    source_finding: {phase: p0, register: business_invariants, row: 4}
  - invariant: A person holds at most one wallet.
    source_finding: {phase: p0, register: business_invariants, row: 5}
  - invariant: No wallet exists for a person who is not accepted.
    source_finding: {phase: p0, register: business_invariants, row: 6}
  - invariant: A recorded moment is never changed or removed.
    source_finding: {phase: p0, register: business_invariants, row: 7}
  - invariant: The act that creates a wallet declares every binding it consults.
    source_finding: {phase: p0, register: business_invariants, row: 8}
  - invariant: Identity is the only writer of what identity owns.
    source_finding: {phase: p0, register: business_invariants, row: 9}
  - invariant: No wallet exists for a person the business has not accepted.
    source_finding: {phase: p0, register: business_invariants, row: 10}
  lifecycle_states:
  - object: Wallet
    state: Active
    meaning: In use. The state a wallet is in when created.
    source_finding: {phase: p0, register: lifecycle_states, row: 1}
  - object: Wallet
    state: Inactive
    meaning: Not in use, but not ended.
    source_finding: {phase: p0, register: lifecycle_states, row: 2}
  - object: Wallet
    state: Closed
    meaning: Ended. Nothing follows.
    source_finding: {phase: p0, register: lifecycle_states, row: 3}
  business_events:
  - event: A wallet was created
    when_it_occurs: When an accepted person is given their wallet
    significance: The business can show when a person came to hold value, and for whom.
    source_finding: {phase: p0, register: business_events, row: 1}
  - event: A person was accepted
    when_it_occurs: When an authority records acceptance
    significance: Wallet follows from it; it is the moment wallet waits on.
    source_finding: {phase: p0, register: business_events, row: 2}
  - event: A person was registered
    when_it_occurs: When a person supplies their details and is admitted unverified
    significance: Declared by identity today and not announced.
    source_finding: {phase: p0, register: business_events, row: 3}
  - event: A person was rejected
    when_it_occurs: When an authority records a rejection
    significance: Declared by identity today and not announced.
    source_finding: {phase: p0, register: business_events, row: 4}
  authority_boundaries:
  - business_object: Wallet
    authoritative_owner: Wallet
    source_finding: {phase: p0, register: authority_boundaries, row: 1}
  - business_object: Balance
    authoritative_owner: Wallet
    source_finding: {phase: p0, register: authority_boundaries, row: 2}
  - business_object: Address
    authoritative_owner: Wallet
    source_finding: {phase: p0, register: authority_boundaries, row: 3}
  - business_object: Person, and whether the business accepts them
    authoritative_owner: Identity
    source_finding: {phase: p0, register: authority_boundaries, row: 4}
  - business_object: Grounds stated for a rejection
    authoritative_owner: Identity
    source_finding: {phase: p0, register: authority_boundaries, row: 5}
  out_of_scope:
  - item: Notifying anyone that a wallet was created
    reason: Dropped by the business. The moment is recorded; who is told, and how, is a later question.
    source_finding: {phase: p0, register: out_of_scope, row: 1}
  - item: Moving value — transactions, transfers, any change of balance
    reason: A wallet is created and nothing moves it yet.
    source_finding: {phase: p0, register: out_of_scope, row: 2}
  - item: Closing or deactivating a wallet
    reason: The lifecycle is declared; only creation is built.
    source_finding: {phase: p0, register: out_of_scope, row: 3}
  - item: Who may be an authority, or whether the one named is entitled to decide
    reason: Not this change.
    source_finding: {phase: p0, register: out_of_scope, row: 4}
  - item: People already accepted, who have no wallet
    reason: The business does not go back for them.
    source_finding: {phase: p0, register: out_of_scope, row: 5}
  - item: Recovering a wallet whose holder has lost access
    reason: A later change.
    source_finding: {phase: p0, register: out_of_scope, row: 6}
  - item: Transaction ordering
    reason: Carried in an earlier design and deliberately left dormant, having no consumer.
    source_finding: {phase: p0, register: out_of_scope, row: 7}
  - item: The other five functions
    reason: Not this change.
    source_finding: {phase: p0, register: out_of_scope, row: 8}
  governance_scope:
  - scope_item: Wallet
    relationship: CREATED
    source_finding: {phase: p0, register: governance_scope, row: 1}
  - scope_item: Identity
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
  - criterion: A person who is accepted holds a wallet afterwards, and the business can show its identity, address, denomination and classification.
    source_finding: {phase: p0, register: acceptance_criteria, row: 1}
  - criterion: A person who is not accepted holds no wallet.
    source_finding: {phase: p0, register: acceptance_criteria, row: 2}
  - criterion: A wallet names exactly one holder, and that holder is a person the business holds.
    source_finding: {phase: p0, register: acceptance_criteria, row: 3}
  - criterion: Accepting the same person again does not produce a second wallet.
    source_finding: {phase: p0, register: acceptance_criteria, row: 4}
  - criterion: The business can show the moment a wallet was created, for whom, and when.
    source_finding: {phase: p0, register: acceptance_criteria, row: 5}
  - criterion: A rejection stating no grounds is refused, and no person is rejected by it.
    source_finding: {phase: p0, register: acceptance_criteria, row: 6}
  - criterion: The moments identity declares are announced when they occur.
    source_finding: {phase: p0, register: acceptance_criteria, row: 7}
  - criterion: No recorded moment is changed or removed by anything this change introduces.
    source_finding: {phase: p0, register: acceptance_criteria, row: 8}
  - criterion: The act declares the records it reads, and a reviewer reads that in the design rather than in the built act.
    source_finding: {phase: p0, register: acceptance_criteria, row: 9}
  - criterion: Identity's records are unchanged by every wallet act, including the refused ones.
    source_finding: {phase: p0, register: acceptance_criteria, row: 10}
  - criterion: A person the business has not accepted is refused a wallet, and none is recorded for them.
    source_finding: {phase: p0, register: acceptance_criteria, row: 11}
  identity_and_sameness:
  - business_object: Wallet
    identified_by: Its own wallet identity
    two_are_the_same_when: They carry the same wallet identity.
    source_finding: {phase: p0, register: identity_and_sameness, row: 1}
  - business_object: Holder
    identified_by: The person identity held by Identity
    two_are_the_same_when: They are the same person to Identity.
    source_finding: {phase: p0, register: identity_and_sameness, row: 2}
  lifecycle_transitions:
  - object: Wallet
    from_state: Does not exist
    to_state: Active
    triggered_by: A person being accepted
    cascade: A moment is recorded on the trail. Nothing else follows.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 1}
  - object: Wallet
    from_state: Active
    to_state: Inactive
    triggered_by: Out of scope for this change
    cascade: null
    source_finding: {phase: p0, register: lifecycle_transitions, row: 2}
  - object: Wallet
    from_state: Active or Inactive
    to_state: Closed
    triggered_by: Out of scope for this change
    cascade: null
    source_finding: {phase: p0, register: lifecycle_transitions, row: 3}
  operation_refusals:
  - operation: Creating a wallet
    refused_when: The person is not one the business holds
    business_reason: A wallet cannot exist for a person who does not exist.
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: Creating a wallet
    refused_when: The person has not been accepted, or was rejected
    business_reason: A wallet follows acceptance and nothing else.
    source_finding: {phase: p0, register: operation_refusals, row: 2}
  - operation: Creating a wallet
    refused_when: The person already holds a wallet
    business_reason: One person holds one wallet; asking again changes nothing.
    source_finding: {phase: p0, register: operation_refusals, row: 3}
  - operation: Recording a rejection
    refused_when: No grounds are stated
    business_reason: The business decided a rejection must say why.
    source_finding: {phase: p0, register: operation_refusals, row: 4}
  authority_deferrals:
  - business_object: Transaction ordering
    deferred_to: Transaction
    until: Transaction exists and needs it.
    source_finding: {phase: p0, register: authority_deferrals, row: 1}
  - business_object: Movement of value in and out of a wallet
    deferred_to: Transaction
    until: Transaction exists.
    source_finding: {phase: p0, register: authority_deferrals, row: 2}
  - business_object: Notifying a person that their wallet was created
    deferred_to: A later change
    until: The business decides who is told and how.
    source_finding: {phase: p0, register: authority_deferrals, row: 3}
  - business_object: Recovery of a wallet whose holder has lost access
    deferred_to: A later change
    until: The business decides what recovery means.
    source_finding: {phase: p0, register: authority_deferrals, row: 4}
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
