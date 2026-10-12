# Change Seed — blockchain / identity

## Machine

```yaml
document:
  phase: p0
  domain: blockchain
  subdomain: identity
  cr: cr_01_identity
  rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0
registers:
  subdomain_purpose: |2

    The Identity subdomain governs who an actor is and whether the business trusts them. It exists
    because every other blockchain function names an actor: a wallet belongs to someone, a transaction is
    submitted by someone, a validator is someone the chain has agreed to trust, and none of those can be
    said accurately until the business can say who an actor is and whether it has accepted them. The
    business needs to let people join before it knows anything about them, and to decide afterwards
    whether to trust them. Those are two decisions made by two different parties at two different times,
    and treating them as one is what this subdomain exists to prevent. A person supplies their own
    details and is admitted immediately but unverified — known to the system, not yet trusted by it.
    Separately an authority within the business reviews them and records a decision. Identity says who an
    actor is and whether they are trusted; it does not say what a trusted actor may then do.
  cr_type:
  - classification: NEW_SUBDOMAIN
    rationale: The change establishes the identity function of the blockchain project. Nothing in this domain exists yet, so the change introduces a function rather than extending one. Identity is the first of the project's functions because every other one names an actor.
  business_vocabulary:
  - term: blockchain
    definition: The project being established, across seven functions of which identity is the first.
  - term: Identity
    definition: The function governing who an actor is and whether the business trusts them.
  - term: Actor
    definition: A person known to the system, whether or not the business has accepted them.
  - term: Registration
    definition: The act by which a person supplies their own details and is admitted to the system unverified.
  - term: Unverified
    definition: The state of an actor the business has recorded and not yet accepted. Trusted with nothing.
  - term: Verification Decision
    definition: The act by which an authority accepts or rejects a registered actor.
  - term: Accepted
    definition: The outcome of a verification decision in which the authority trusts the actor.
  - term: Rejected
    definition: The outcome of a verification decision in which the authority does not trust the actor. Trusted with nothing.
  - term: Authority
    definition: A party within the business empowered to make a verification decision about an actor, identified outside the identity function and never registered through it.
  - term: Contact Address
    definition: The address a person registers with, which is what identifies them as an actor.
  - term: Grounds
    definition: The reason an authority states for a verification decision.
  - term: Occurrence
    definition: A recorded moment in an actor's history, written when it happens and never rewritten.
  - term: Preference
    definition: A convenience recorded at registration — preferred currency or preferred language — bearing on neither identity nor the verification decision. Absent, it is recorded as the default.
  - term: Default Preference
    definition: BACHI for currency and English for language; what an actor is recorded as preferring when it states nothing.
  requested_outcomes:
  - outcome: A person can register themselves, supplying their own identifying details, and is admitted in an unverified state.
  - outcome: An authority can record a verification decision against a registered person, accepting or rejecting them.
  - outcome: The business can show, for any actor, who registered and when, every time they registered, whether a decision was made, by which authority, what it was, when, and the grounds stated for it.
  - outcome: An unverified or rejected actor is trusted with nothing and can be read as trusted with nothing.
  known_facts:
  - fact: An unverified actor is a claim the business has recorded and not yet accepted.
    certainty: HIGH
  - fact: An unverified actor may hold no wallet and submit no transaction.
    certainty: HIGH
  - fact: An unverified actor is not a lesser actor but a different thing; the business would rather say it has not decided than imply a decision it has not made.
    certainty: HIGH
  - fact: A person registers themselves; the details are their own claim about who they are.
    certainty: HIGH
  - fact: Registration may be refused only for details the business cannot read, such as a missing name or a missing contact address.
    certainty: HIGH
  - fact: A detail is unreadable when it is absent or is not of the form the business asked for; everything else is a matter of belief.
    certainty: HIGH
  - fact: Whether a person controls the address they registered with, and whether the name is theirs, are matters of belief and never of registration.
    certainty: HIGH
  - fact: An actor is identified by the contact address they register with.
    certainty: HIGH
  - fact: Two registrations carrying the same contact address are the same person.
    certainty: HIGH
  - fact: A repeated registration does not create a second actor and does not fail.
    certainty: HIGH
  - fact: A repeated registration is recorded as a distinct occurrence against the same actor.
    certainty: HIGH
  - fact: A repeated registration does not reset a decision already made.
    certainty: HIGH
  - fact: A second registration may carry details differing from the first, and the details the actor was admitted with prevail.
    certainty: HIGH
  - fact: The differing details of a second registration are recorded as part of the occurrence and change the actor in no respect.
    certainty: HIGH
  - fact: A verification decision is made by an authority within the business, acting as a distinct kind of actor from the person decided about.
    certainty: HIGH
  - fact: A person may never verify themselves.
    certainty: HIGH
  - fact: An authority is identified outside the identity function and is not an actor this function holds or resolves.
    certainty: HIGH
  - fact: A verification decision is either acceptance or rejection; there is no third outcome and no deferral.
    certainty: HIGH
  - fact: An authority that is not ready to decide has not decided, and the actor stays unverified.
    certainty: HIGH
  - fact: A verification decision may only be made against a registration that exists.
    certainty: HIGH
  - fact: A rejection is its own occurrence, distinct in kind from an acceptance.
    certainty: HIGH
  - fact: A rejected actor is trusted with nothing and is recorded among the actors the business has accepted in no sense whatever.
    certainty: HIGH
  - fact: An actor is decided about once.
    certainty: HIGH
  - fact: Grounds are required for a rejection and optional for an acceptance.
    certainty: HIGH
  - fact: The deciding authority is recorded on every decision, acceptance and rejection alike.
    certainty: HIGH
  - fact: Every recorded occurrence carries the time it actually happened, determined at the moment it occurs.
    certainty: HIGH
  - fact: A record whose times do not advance is regarded by the business as no record at all.
    certainty: HIGH
  - fact: The record is added to and never rewritten; a correction is a further occurrence, not an edit.
    certainty: HIGH
  - fact: Two preferences are collected at registration — preferred currency and preferred language — each having a default.
    certainty: HIGH
  - fact: The default preferred currency is BACHI and the default preferred language is English.
    certainty: HIGH
  - fact: A person who states no preference is recorded as preferring the defaults, rather than as having stated nothing.
    certainty: HIGH
  - fact: Preferences bear on neither identity nor the verification decision.
    certainty: HIGH
  - fact: Two registrations differing only in preference are the same person.
    certainty: HIGH
  system_beliefs:
  - belief: The business author believes nothing in the blockchain domain exists yet, so identity is established rather than extended.
    why_it_matters: If any blockchain function is already governed, this change is an extension and its classification is wrong.
    verification_goal: Establish whether the composition holds any artifact belonging to the blockchain domain.
  - belief: The business author believes the platform already offers a way to record occurrences that is added to and never rewritten.
    why_it_matters: The record being append-only is a business requirement; if the platform provides no such facility this change must ask for one rather than assume it.
    verification_goal: Establish whether the composition offers an append-only recording capability identity can use.
  - belief: The business author believes the platform already offers a way to hold a registry of business objects that can be looked up by their identifier.
    why_it_matters: Resolving an actor from a contact address, and refusing a decision about an actor that does not exist, both depend on it.
    verification_goal: Establish whether the composition offers a registry capability identity can use.
  - belief: The business author believes the platform already offers a way to generate an identifier for a newly admitted business object.
    why_it_matters: An actor is admitted before it has any identifier of its own beyond the details it supplied.
    verification_goal: Establish whether the composition offers an identifier generation capability identity can use.
  - belief: The business author believes the platform already distinguishes a kind of actor empowered to act on the business's behalf from an ordinary participant.
    why_it_matters: A person may never verify themselves, which requires the two kinds to be distinguishable.
    verification_goal: Establish whether the composition declares a system or authority actor distinct from an end-user actor.
  assumptions:
  - assumption: A contact address supplied at registration is one the person controls.
    basis: The business admits the person unverified precisely because their claims are not yet established; the address is treated as identifying without being treated as proven.
  - assumption: A person will register before an authority has occasion to decide about them.
    basis: The business author states a decision may only be made against a registration that exists, and describes no path by which an authority would encounter a person otherwise.
  - assumption: The set of authorities is small enough that recording which one decided is meaningful without governing who may be one.
    basis: The business author defers authority over verifiers to a later change while still requiring the deciding authority to be recorded.
  constraints:
  - constraint: Registration and the verification decision are separate acts, made by different parties at different times.
    source: The business author's statement that treating them as one is what this change exists to prevent.
  - constraint: An unverified or rejected actor may hold no wallet and submit no transaction.
    source: The business author's statement of what an unverified actor is permitted to be.
  - constraint: A recorded occurrence may never be altered or removed.
    source: The business author's statement that the record is added to and never rewritten.
  - constraint: The time of an occurrence is determined at the moment it occurs.
    source: The business author's statement that a record whose times do not advance is no record at all.
  - constraint: Identity governs who an actor is and whether they are trusted, and nothing about what a trusted actor may do.
    source: The business author's statement of what identity does not decide.
  business_invariants:
  - invariant: An actor is identified by exactly one contact address.
  - invariant: Two actors never share a contact address.
  - invariant: An actor is either unverified, accepted or rejected, and never more than one of those at a time.
  - invariant: An actor that has not been decided about is unverified.
  - invariant: A verification decision exists only against a registration that exists.
  - invariant: A verification decision names the authority that made it.
  - invariant: A rejection states grounds.
  - invariant: An actor is never accepted and rejected both.
  - invariant: A person never makes the verification decision about themselves.
  - invariant: Neither an unverified nor a rejected actor is trusted with anything.
  - invariant: Every recorded occurrence carries the time it occurred.
  - invariant: No recorded occurrence is altered or removed once written.
  lifecycle_states:
  - object: Actor
    state: Unverified
    meaning: The business has recorded the person's claim about themselves and has not yet accepted it. The actor is trusted with nothing.
  - object: Actor
    state: Accepted
    meaning: An authority has reviewed the actor and trusts them.
  - object: Actor
    state: Rejected
    meaning: An authority has reviewed the actor and does not trust them. The actor is trusted with nothing.
  - object: Verification Decision
    state: Recorded
    meaning: An authority has stated an outcome against a registered actor, and the business holds it as evidence.
  business_events:
  - event: Actor Registered Unverified
    when_it_occurs: A person supplies their identifying details and is admitted.
    significance: The business now knows of the person and trusts them with nothing. It is the occurrence a verification decision is made against.
  - event: Actor Registered Again
    when_it_occurs: A person already known registers a second time.
    significance: The actor is unchanged, but that the person registered twice is a fact about them the business keeps.
  - event: Actor Accepted
    when_it_occurs: An authority records a decision to trust a registered actor.
    significance: The actor becomes trusted. It is the moment from which the other blockchain functions may name them.
  - event: Actor Rejected
    when_it_occurs: An authority records a decision not to trust a registered actor.
    significance: The actor remains trusted with nothing, and the business can afterwards ask who has been rejected and receive an answer.
  authority_boundaries:
  - business_object: Actor
    authoritative_owner: The identity function of the blockchain project.
  - business_object: The details an actor registers with
    authoritative_owner: The person themselves.
  - business_object: Verification Decision
    authoritative_owner: An authority within the business, through the identity function. The authority itself is owned outside it.
  - business_object: The record of occurrences against an actor
    authoritative_owner: The identity function of the blockchain project.
  out_of_scope:
  - item: What a trusted actor may then do
    reason: Identity says who an actor is and whether they are trusted, not what trust permits.
  - item: Permissions and roles beyond the distinction between an ordinary participant and an authority
    reason: Named by the business author as outside this change.
  - item: An actor's standing changing through their conduct
    reason: Named by the business author as outside this change.
  - item: Re-application after rejection
    reason: Rests on what a rejection is taken to mean, which this change is the first to state.
  - item: Revocation of a verified actor
    reason: A governed change of its own, including what happens to what the actor did while trusted.
  - item: Which persons may be an authority, and how that permission is granted or removed
    reason: This change records which authority decided; it does not govern who may be one.
  - item: The material an authority examined when deciding
    reason: A separate need with its own retention and privacy consequences.
  - item: Correcting an actor's own details after registration
    reason: Not answerable until a decision is defined.
  - item: Wallets, transactions, mempool, blocks, chain and consensus
    reason: Later functions of the project, excluded except where they depend on identity behaviour.
  governance_scope:
  - scope_item: Identity
    relationship: CREATED
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
  - criterion: A person who supplies a name and a contact address is admitted, and is afterwards unverified.
  - criterion: A person who supplies no contact address is refused, and no actor exists afterwards.
  - criterion: A person who registers twice is one actor afterwards, and the business can show two registrations against them.
  - criterion: A verification decision against a person who never registered is refused.
  - criterion: An accepted actor can be shown as accepted, with the deciding authority and the time recorded.
  - criterion: A rejected actor can be shown as rejected, with the deciding authority, the grounds and the time recorded, and cannot be read as accepted by any means.
  - criterion: The business can list the actors that have been rejected.
  - criterion: A rejection stating no grounds is refused.
  - criterion: Two occurrences recorded at different moments carry different times.
  - criterion: No sequence of operations changes or removes an occurrence already recorded.
  - criterion: A decision made against an actor already decided about is refused.
  - criterion: An actor that is unverified or rejected holds no wallet and has submitted no transaction.
  identity_and_sameness:
  - business_object: Actor
    identified_by: The contact address they register with.
    two_are_the_same_when: Their contact addresses match, whatever else differs.
  - business_object: Verification Decision
    identified_by: The actor it was made against.
    two_are_the_same_when: They were made against the same actor, which is why there is only ever one.
  - business_object: Occurrence
    identified_by: The actor it was recorded against and the moment it happened.
    two_are_the_same_when: Never — two occurrences at different moments are different occurrences even when they say the same thing.
  lifecycle_transitions:
  - object: Actor
    from_state: null
    to_state: Unverified
    triggered_by: A person supplies their identifying details and is admitted.
    cascade: None — admission grants nothing and obliges no authority to decide.
  - object: Actor
    from_state: Unverified
    to_state: Unverified
    triggered_by: The same person registers a second time.
    cascade: None — the state is unchanged and any decision already made stands. A second occurrence is recorded.
  - object: Actor
    from_state: Unverified
    to_state: Accepted
    triggered_by: An authority records a decision to trust the actor.
    cascade: None within identity. The actor becoming nameable by the other blockchain functions is a consequence those functions own, not one identity performs.
  - object: Actor
    from_state: Unverified
    to_state: Rejected
    triggered_by: An authority records a decision not to trust the actor.
    cascade: None — nothing is removed, nothing is notified, and the actor remains recorded.
  - object: Verification Decision
    from_state: null
    to_state: Recorded
    triggered_by: An authority states an outcome against a registered actor.
    cascade: None beyond the actor's state changing with it.
  operation_refusals:
  - operation: Register a person
    refused_when: No name is supplied.
    business_reason: Registration may be refused for details the business cannot read.
  - operation: Register a person
    refused_when: No contact address is supplied.
    business_reason: An actor is identified by the contact address they register with, so without one there is no actor.
  - operation: Register a person
    refused_when: The contact address supplied is not of the form the business asked for.
    business_reason: A detail is unreadable when it is absent or not of the form asked for.
  - operation: Register a person
    refused_when: On the business's judgement of the person, including whether they control the address or the name is theirs.
    business_reason: Those are matters of belief, which is the verification decision's business; refusing on them here would be making that decision early and by the wrong party.
  - operation: Record a verification decision
    refused_when: The actor it names never registered.
    business_reason: The decision is a decision on a registration; without one it is not an incomplete decision but a meaningless one.
  - operation: Record a verification decision
    refused_when: The actor has already been decided about.
    business_reason: An actor is decided about once.
  - operation: Record a verification decision
    refused_when: The authority making it is the actor being decided about.
    business_reason: A person may never verify themselves.
  - operation: Record a verification decision
    refused_when: The outcome is neither acceptance nor rejection.
    business_reason: There is no third outcome and no deferral.
  - operation: Record a verification decision
    refused_when: The deciding authority is not named.
    business_reason: A decision whose author is unknown is not evidence.
  - operation: Record a rejection
    refused_when: No grounds are stated.
    business_reason: The grounds are the substance of a rejection.
  - operation: Alter or remove a recorded occurrence
    refused_when: Always.
    business_reason: The record is added to and never rewritten; a correction is a further occurrence.
  authority_deferrals:
  - business_object: Re-application by a rejected actor
    deferred_to: A follow-on governed change for re-application
    until: This change states what a rejection means.
  - business_object: Revocation of an accepted actor
    deferred_to: A follow-on governed change for revocation
    until: The business chooses to take it up.
  - business_object: Which persons may be an authority, and the resolution of an authority named on a decision
    deferred_to: A follow-on governed change for authority over verifiers
    until: The business chooses to take it up. Identity records the name and does not resolve it.
  - business_object: The material an authority examined when deciding
    deferred_to: A follow-on governed change for identity evidence
    until: The business settles its retention and privacy consequences.
  - business_object: Correcting an actor's own details after registration
    deferred_to: A follow-on governed change for correction
    until: This change defines a verification decision.
  - business_object: What a trusted actor may do
    deferred_to: The wallet, transaction and consensus functions
    until: Those functions are taken up.
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

---

## gov_projection — Governed Handoff to Stage 1

| Direction | Fields |
|-----------|--------|
| **Consumes** ← human | business problem statement |
| **Emits** → Stage 1 | subdomain_purpose · cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
