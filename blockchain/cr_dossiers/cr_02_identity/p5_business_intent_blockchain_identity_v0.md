# Stage 5 — Business Intent: blockchain / identity

## Machine

```yaml
document:
  phase: p5
  domain: blockchain
  subdomain: identity
  cr: cr_02_identity
  rule_set: transformation.schemas.REGISTER_SCHEMA_P5_V0
registers:
  subdomain_purpose: |2

    The Identity subdomain governs who an actor is and whether the business trusts them. It holds one
    record for each person known to the system, the state that says whether the business has accepted
    them, and the record of every moment in their history. It establishes the authority to say that a
    person exists and that they are trusted. It also decides what of itself the business offers to
    callers outside it, and what it turns away at the door: three acts are offered by name — a person
    registering themselves, an authority accepting a registered actor, and an authority rejecting one —
    and anything else is refused as an act the business does not offer. Accepting and rejecting are
    offered separately because the business already holds them to be distinct in kind, not one act
    carrying an outcome. It exists because the business must admit people before it knows
    anything about them and decide afterwards whether to trust them, and because both of those acts are
    performed by parties who are not inside the business and must be able to reach it. It does not
    govern what a trusted actor may then do, which persons may be an authority, or who a caller is.
  purpose_provenance:
  - source: CR seed §0 Subdomain Purpose
    disposition: REFINED
    refinement: 'The seed states that identity''s two acts are performed by parties outside the business and that today neither can reach it. This states the subdomain that results: alongside the records it holds and the authority it establishes, it now owns what it offers to the outside and what it turns away. Nothing here contradicts the seed or the previous change; what it adds is the standing description of a function that is reachable, rather than the reason for making it so. The seed speaks of two acts offered; three names are offered, because the seed and the previous change both hold acceptance and rejection to be distinct in kind, and naming them together would be the door presenting as one act what the business records as two.'
  scope_boundary:
  - capability: Offer registering an actor to a caller outside the business
    status: IN_SCOPE
    notes: The public name of the act and what a caller may send.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-01}
  - capability: Offer recording a verification decision to a caller outside the business
    status: IN_SCOPE
    notes: A name of its own; what a caller sends differs entirely from registration.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-02}
  - capability: Hold what an act requires and a caller must not send
    status: IN_SCOPE
    notes: Held within the two admissions, sealed and stated once.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-03}
  - capability: Tell a caller how their registration ended
    status: IN_SCOPE
    notes: Which kind of answer each ending takes, and what of the result is exposed.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-04}
  - capability: Tell a caller how their decision ended
    status: IN_SCOPE
    notes: The same over that act's endings, including the actor that does not exist.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-05}
  - capability: Declare where the boundary declarations are found
    status: IN_SCOPE
    notes: The domain's build manifest admits both kinds and declares no place for them.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-06}
  - capability: Show a person a form and its answer
    status: IN_SCOPE
    notes: Two forms, holding no rules.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-07}
  - capability: Carry a detail from one page to the next
    status: IN_SCOPE
    notes: A convenience; nothing the business does depends on it.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-08}
  - capability: Show the functions the business has not built
    status: IN_SCOPE
    notes: Four of six named and marked not yet available.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-09}
  - capability: Announce the moments an actor is registered, accepted and rejected
    status: DEFERRED
    notes: Owned by construction rather than by identity; the moments are already declared and correct.
    source_finding: {phase: p4, register: authoring_scope, key: 'Announce the moments an actor is registered, accepted and rejected'}
  - capability: Hold what an act requires with the act that requires it
    status: DEFERRED
    notes: Better placement, and it reopens two sealed acts.
    source_finding: {phase: p4, register: authoring_scope, key: Hold what an act requires with the act that requires it}
  - capability: Establishing who a caller is, and what they are allowed to do
    status: DEFERRED
    notes: Deferred by the business with the question of who may be an authority.
    source_finding: {phase: p4, register: authoring_scope, key: 'Establishing who a caller is, and what they are allowed to do'}
  - capability: Looking up an actor from outside
    status: DEFERRED
    notes: The business would rather offer nothing than a reading surface it has not decided the shape of.
    source_finding: {phase: p4, register: authoring_scope, key: Looking up an actor from outside}
  - capability: Telling a person anything after they leave the page
    status: DEFERRED
    notes: Making the person wait for it is what caused the trouble before.
    source_finding: {phase: p4, register: authoring_scope, key: Telling a person anything after they leave the page}
  - capability: A way in for wallet, transaction, mempool, block, chain and consensus
    status: DEFERRED
    notes: Each comes with the function it belongs to.
    source_finding: {phase: p4, register: authoring_scope, key: 'A way in for wallet, transaction, mempool, block, chain and consensus'}
  - capability: A kind of answer for an act that ran and refused
    status: DEFERRED
    notes: A change to the platform's closed governed set, not to this domain.
    source_finding: {phase: p4, register: authoring_scope, key: A kind of answer for an act that ran and refused}
  business_objects: null
  identity_semantics:
  - store_name: NONE IDENTIFIED
    identity_field: The public name of an offered act
    source: Chosen by the business as its word for the act
    uniqueness_rule: One name denotes one act; two acts never share a name, and a name outlives the act it currently reaches
    cross_subdomain_relationship: Names an act of this subdomain and of no other; a later function's acts take names of their own under the same shared way in
    source_finding: {phase: p4, register: design_decisions, row: 2}
  invariants:
  - invariant: Only an act the business has chosen to offer can be reached from outside.
    business_reason: An act is reachable because the business decided to offer it, never because it happens to exist. Without this there is no door, only a wall with holes in it.
    source_finding: {phase: p1, register: business_invariants, row: 1}
  - invariant: Every request receives an answer.
    business_reason: A caller who is told nothing cannot know whether they registered, and would try again.
    source_finding: {phase: p1, register: business_invariants, row: 2}
  - invariant: 'Every answer is exactly one of three kinds: the act was done, the act was turned away, or something went wrong inside the business.'
    business_reason: The caller must never have to work out which happened, because each calls for something different from them.
    source_finding: {phase: p1, register: business_invariants, row: 3}
  - invariant: An answer that turns a request away states which of the two reasons it was.
    business_reason: Told only "no", a caller can correct nothing, and the business gains nothing by withholding it.
    source_finding: {phase: p1, register: business_invariants, row: 4}
  - invariant: A request turned away creates no record of an actor.
    business_reason: Nothing happened to an actor. The record of who registered must not fill with people who did not.
    source_finding: {phase: p1, register: business_invariants, row: 5}
  - invariant: A request whose details can be read is passed to the act, and nothing further is judged beforehand.
    business_reason: Anything judged before the act is the act's decision made early and by the wrong party.
    source_finding: {phase: p1, register: business_invariants, row: 6}
  - invariant: No business rule is held by the web page.
    business_reason: A rule in two places is two rules that will disagree, and nobody will know which is right.
    source_finding: {phase: p1, register: business_invariants, row: 7}
  - invariant: Nothing the business holds is copied into the web page.
    business_reason: What the business holds is the business's, and a copy outside it is neither governed nor current.
    source_finding: {phase: p1, register: business_invariants, row: 8}
  - invariant: No act of the business depends on a detail the page carried forward.
    business_reason: The convenience must stay a convenience; the moment something depends on it, it is hidden state.
    source_finding: {phase: p1, register: business_invariants, row: 9}
  - invariant: Being turned away and being decided against are never reported as the same answer.
    business_reason: One means the business did not start, the other that it started and refused. Telling someone to fix their details when the business has decided about them misleads them.
    source_finding: {phase: p1, register: business_invariants, row: 10}
  actions:
  - action: Offer
    object: The act of registering an actor, under the business's own name for it
    trigger: The business decides to make the act reachable from outside
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Offer registering an actor to a caller outside the business}
  - action: Offer
    object: The act of accepting a registered actor, under the business's own name for it
    trigger: The business decides to make the act reachable from outside
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Offer recording a verification decision to a caller outside the business}
  - action: Offer
    object: The act of rejecting a registered actor, under the business's own name for it
    trigger: The business decides to make the act reachable from outside
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Offer recording a verification decision to a caller outside the business}
  - action: Turn away
    object: A request naming an act the business does not offer
    trigger: A caller asks for something the business has not offered
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Offer both acts through one way in}
  - action: Turn away
    object: A request whose details the business cannot read
    trigger: A caller sends details that are missing or not of the form asked for
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Hold what an act requires and a caller must not send}
  - action: Answer
    object: A caller whose registration ran, whichever way it ended
    trigger: The act of registering reaches an ending
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Tell a caller how their registration ended}
  - action: Answer
    object: A caller whose decision ran, whichever way it ended
    trigger: The act of recording a decision reaches an ending
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Tell a caller how their decision ended}
  - action: Show
    object: The six functions of the project, four of them not yet available
    trigger: A caller opens the front page
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Show the functions the business has not built}
  - action: Carry
    object: A detail the person has just typed, to the next page
    trigger: A person moves from one form to another
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Carry a detail from one page to the next}
  - action: Establish
    object: Who a caller is, and what they are permitted to ask for
    trigger: A caller reaches the business
    status: DEFERRED
    source_finding: {phase: p4, register: authoring_scope, key: 'Establishing who a caller is, and what they are allowed to do'}
  - action: Look up
    object: What the business already knows about an actor
    trigger: A caller asks about an actor rather than acting on one
    status: DEFERRED
    source_finding: {phase: p4, register: authoring_scope, key: Looking up an actor from outside}
  - action: Notify
    object: A person, after they have left the page
    trigger: A registration or a decision completes
    status: DEFERRED
    source_finding: {phase: p4, register: authoring_scope, key: Telling a person anything after they leave the page}
  provisional_codes:
  - provisional_code: TI_REGISTER_ACTOR_V0
    family: TI
    summary: Offers registering an actor under the business's public name for it, states what a caller may send, and holds what the act requires and a caller must not
    source_finding: {phase: p4, register: gap_register, key: GAP-01}
  - provisional_code: TE_REGISTER_ACTOR_V0
    family: TE
    summary: States which kind of answer each ending of registering an actor takes, and what of the result the caller is told
    source_finding: {phase: p4, register: gap_register, key: GAP-04}
  - provisional_code: TI_ACCEPT_ACTOR_V0
    family: TI
    summary: Offers accepting a registered actor under the business's public name for it, states what a caller may send, and holds what the act requires and a caller must not
    source_finding: {phase: p4, register: gap_register, key: GAP-02}
  - provisional_code: TE_ACCEPT_ACTOR_V0
    family: TE
    summary: States which kind of answer each ending of accepting an actor takes, including the actor that does not exist, and what of the result the caller is told
    source_finding: {phase: p4, register: gap_register, key: GAP-05}
  - provisional_code: TI_REJECT_ACTOR_V0
    family: TI
    summary: Offers rejecting a registered actor under the business's public name for it, states what a caller may send, and holds what the act requires and a caller must not
    source_finding: {phase: p4, register: gap_register, key: GAP-02}
  - provisional_code: TE_REJECT_ACTOR_V0
    family: TE
    summary: States which kind of answer each ending of rejecting an actor takes, including the actor that does not exist, and what of the result the caller is told
    source_finding: {phase: p4, register: gap_register, key: GAP-05}
  cross_subdomain_refs: []
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
