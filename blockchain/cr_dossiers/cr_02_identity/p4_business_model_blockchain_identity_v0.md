# Stage 4 — Business Model: blockchain / identity

## Machine

```yaml
document:
  phase: p4
  domain: blockchain
  subdomain: identity
  cr: cr_02_identity
  rule_set: transformation.schemas.REGISTER_SCHEMA_P4_V0
registers:
  actors:
  - actor: The person registering
    role: Reaches the business from outside, supplies their own identifying details and is told what happened. Not established to be who they claim.
    authority_class: Ordinary participant
    source_finding: {phase: p1, register: known_facts, row: 1}
  - actor: The authority
    role: Reaches the business from outside and records a decision about a registered actor. Names itself, and the claim is not checked.
    authority_class: External business authority
    source_finding: {phase: p1, register: known_facts, row: 43}
  - actor: Identity
    role: Holds the acts being reached, and decides what is offered and what is turned away.
    authority_class: Owning subdomain
    source_finding: {phase: p3, register: placement_decision, key: EXTEND}
  bm_entities:
  - entity: Offered Act
    description: An act the business has chosen to make reachable from outside, named by its business name.
    store_model: None — declared, not stored.
    source_finding: {phase: p3, register: analysis_findings, key: Q2}
  - entity: Request
    description: 'What a caller sends: the name of the act they want, and the details that act needs.'
    store_model: None — answered and not kept.
    source_finding: {phase: p3, register: analysis_findings, key: Q1}
  - entity: Answer
    description: What the business tells a caller in reply. One of three kinds, and never leaving the caller to guess which.
    store_model: None — composed for one caller; the record of what happened is the occurrence the act itself writes.
    source_finding: {phase: p3, register: analysis_findings, key: Q7}
  - entity: Carried Detail
    description: Something the person has just typed, held only to save them typing it again on the next page.
    store_model: None the business holds; it lives with whoever fills in the form and the business never reads it.
    source_finding: {phase: p3, register: analysis_findings, key: Q11}
  - entity: Actor
    description: A person known to the system. Named because the acts being reached are acts upon one; unchanged by this change.
    store_model: Already held by the acts, unchanged.
    source_finding: {phase: p3, register: analysis_findings, key: Q5}
  resources: []
  events:
  - event: NONE IDENTIFIED
    trigger: This change recognises no new moment. The moments identity recognises are unchanged and are named by the previous change.
    lifecycle_meaning: Nothing an actor undergoes is added, removed or altered by making the acts reachable.
    source_finding: {phase: p1, register: business_events, row: 1}
  relationships:
  - subject: A caller
    verb: names
    object: an offered act
    capability_need: Offer registering an actor to a caller outside the business
    source_finding: {phase: p3, register: authoring_decisions, key: Offer registering an actor to a caller outside the business}
  - subject: A caller
    verb: sends
    object: the details an act needs
    capability_need: Hold what an act requires and a caller must not send
    source_finding: {phase: p3, register: authoring_decisions, key: Hold what an act requires and a caller must not send}
  - subject: The business
    verb: turns away
    object: a request it does not offer or cannot read
    capability_need: Offer both acts through one way in
    source_finding: {phase: p3, register: authoring_decisions, key: Offer both acts through one way in}
  - subject: The business
    verb: tells
    object: a caller how their request ended
    capability_need: Tell a caller how their registration ended
    source_finding: {phase: p3, register: authoring_decisions, key: Tell a caller how their registration ended}
  - subject: A page
    verb: carries
    object: a detail to the next page
    capability_need: Carry a detail from one page to the next
    source_finding: {phase: p3, register: authoring_decisions, key: Carry a detail from one page to the next}
  - subject: The front page
    verb: names
    object: a function that is not yet available
    capability_need: Show the functions the business has not built
    source_finding: {phase: p3, register: authoring_decisions, key: Show the functions the business has not built}
  capability_graph:
  - capability: Admit a person's registration
    source_finding: {phase: p3, register: authoring_decisions, key: Admit a person's registration}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as-is and not amended. The act exists and runs; only the way in is new.
  - capability: Record an authority's decision
    source_finding: {phase: p3, register: authoring_decisions, key: Record an authority's decision}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as-is and not amended.
  - capability: Read a registration for absent or malformed details
    source_finding: {phase: p3, register: authoring_decisions, key: Read a registration for absent or malformed details}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as-is. The test takes the declaration it applies as an input, which is what makes it reusable without being restated.
  - capability: Offer both acts through one way in
    source_finding: {phase: p3, register: authoring_decisions, key: Offer both acts through one way in}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused. What binds a place to a name is configuration the boundary is pointed at, not an artifact of the composition.
  - capability: Offer registering an actor to a caller outside the business
    source_finding: {phase: p3, register: authoring_decisions, key: Offer registering an actor to a caller outside the business}
    status: CRITICAL
    gap_register_entry: GAP-01
    notes: The public name of the act and what a caller may send. Declared apart from the act it reaches, so the name outlives it.
  - capability: Offer recording a verification decision to a caller outside the business
    source_finding: {phase: p3, register: authoring_decisions, key: Offer recording a verification decision to a caller outside the business}
    status: CRITICAL
    gap_register_entry: GAP-02
    notes: A name of its own, because what a caller may send differs entirely from registration.
  - capability: Hold what an act requires and a caller must not send
    source_finding: {phase: p3, register: authoring_decisions, key: Hold what an act requires and a caller must not send}
    status: CRITICAL
    gap_register_entry: GAP-03
    notes: Held within the two admissions above, sealed in the snapshot and stated once. Better placed with the acts themselves, which GAP-11 records.
  - capability: Tell a caller how their registration ended
    source_finding: {phase: p3, register: authoring_decisions, key: Tell a caller how their registration ended}
    status: CRITICAL
    gap_register_entry: GAP-04
    notes: Which kind of answer each ending takes, and what of the act's result is exposed.
  - capability: Tell a caller how their decision ended
    source_finding: {phase: p3, register: authoring_decisions, key: Tell a caller how their decision ended}
    status: CRITICAL
    gap_register_entry: GAP-05
    notes: The same over that act's endings, including the absent actor, which is already a distinct kind.
  - capability: Declare where the boundary declarations are found
    source_finding: {phase: p3, register: authoring_decisions, key: Declare where the boundary declarations are found}
    status: CRITICAL
    gap_register_entry: GAP-06
    notes: The domain's build manifest admits both kinds while declaring no place they could be found.
  - capability: Show a person a form and its answer
    source_finding: {phase: p3, register: authoring_decisions, key: Show a person a form and its answer}
    status: CRITICAL
    gap_register_entry: GAP-07
    notes: Two forms. Lifted from the prior implementation, which holds no rules; what they say to the platform is replaced.
  - capability: Carry a detail from one page to the next
    source_finding: {phase: p3, register: authoring_decisions, key: Carry a detail from one page to the next}
    status: CRITICAL
    gap_register_entry: GAP-08
    notes: A convenience, bounded so that nothing the business does depends on it.
  - capability: Show the functions the business has not built
    source_finding: {phase: p3, register: authoring_decisions, key: Show the functions the business has not built}
    status: CRITICAL
    gap_register_entry: GAP-09
    notes: Four of six named and marked not yet available.
  - capability: Announce the moments an actor is registered, accepted and rejected
    source_finding: {phase: p3, register: authoring_decisions, key: 'Announce the moments an actor is registered, accepted and rejected'}
    status: CRITICAL
    gap_register_entry: GAP-10
    notes: The three moments are declared and cannot presently be announced. The cause is in construction, not in this domain, and nothing in this change depends on one being announced.
  dependency_graph:
  - from: identity
    to: blockchain::WF_REGISTER_ACTOR_V0
    dependency_type: act reached from outside
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The act that admits a person}
  - from: identity
    to: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    dependency_type: act reached from outside
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The act that records a decision}
  - from: identity
    to: blockchain::CC_VALIDATE_REGISTRATION_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Reading a record for absence and form}
  - from: identity
    to: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Reading a record for absence and form}
  - from: identity
    to: transport::CONSTITUTION_TRANSPORT_INGRESS_V0
    dependency_type: governed by
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The boundary's ingress and egress kinds}
  - from: identity
    to: transport::CONSTITUTION_TRANSPORT_EGRESS_V0
    dependency_type: governed by
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The boundary's ingress and egress kinds}
  - from: identity
    to: blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0
    dependency_type: build manifest
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: A source layer for the boundary declarations}
  - from: identity
    to: blockchain::AC_PARTICIPANT_V0
    dependency_type: actor declaration
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The act that admits a person}
  - from: identity
    to: workload::TI_COLLATZ_COMPUTE_V0
    dependency_type: worked precedent
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The name a caller uses for an act}
  - from: identity
    to: workload::TE_COLLATZ_COMPUTE_V0
    dependency_type: worked precedent
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The kinds of answer a caller is told}
  constraint_register:
  - number: '1'
    constraint: No business rule may live in the web page.
    source_finding: {phase: p1, register: constraints, row: 1}
    source: The business author
  - number: '2'
    constraint: The page may hold only what the person has just typed, and only to save them retyping it.
    source_finding: {phase: p1, register: constraints, row: 2}
    source: The business author
  - number: '3'
    constraint: The web page must not check details before sending them.
    source_finding: {phase: p1, register: constraints, row: 3}
    source: The business author
  - number: '4'
    constraint: The page must be plain and quick to load — a form and an answer, not an application.
    source_finding: {phase: p1, register: constraints, row: 4}
    source: The business author
  - number: '5'
    constraint: There is one way in, and the request names the act.
    source_finding: {phase: p1, register: constraints, row: 5}
    source: The business author
  - number: '6'
    constraint: The name of an act is the business's public word for it and must outlive changes to how the act is performed.
    source_finding: {phase: p1, register: constraints, row: 6}
    source: The business author
  - number: '7'
    constraint: The readability test must be the one the previous change defined, not a second one.
    source_finding: {phase: p1, register: constraints, row: 7}
    source: The business author
  - number: '8'
    constraint: Only acts the business has chosen to offer may be reached.
    source_finding: {phase: p1, register: constraints, row: 8}
    source: The business author
  - number: '9'
    constraint: The change introduces no identity behaviour and revisits no decision the previous change made.
    source_finding: {phase: p1, register: constraints, row: 9}
    source: The business author
  - number: '10'
    constraint: The kinds of answer a caller may be told are a closed governed set, which this change does not extend.
    source_finding: {phase: p3, register: analysis_findings, key: Q7}
    source: The platform's egress governance
  gap_register:
  - gap_code: GAP-01
    source_finding: {phase: p3, register: authoring_decisions, key: Offer registering an actor to a caller outside the business}
    capability: Offer registering an actor to a caller outside the business
    owner_subdomain: identity
    resolution: NEW
  - gap_code: GAP-02
    source_finding: {phase: p3, register: authoring_decisions, key: Offer recording a verification decision to a caller outside the business}
    capability: Offer recording a verification decision to a caller outside the business
    owner_subdomain: identity
    resolution: NEW
  - gap_code: GAP-03
    source_finding: {phase: p3, register: authoring_decisions, key: Hold what an act requires and a caller must not send}
    capability: Hold what an act requires and a caller must not send
    owner_subdomain: identity
    resolution: NEW
  - gap_code: GAP-04
    source_finding: {phase: p3, register: authoring_decisions, key: Tell a caller how their registration ended}
    capability: Tell a caller how their registration ended
    owner_subdomain: identity
    resolution: NEW
  - gap_code: GAP-05
    source_finding: {phase: p3, register: authoring_decisions, key: Tell a caller how their decision ended}
    capability: Tell a caller how their decision ended
    owner_subdomain: identity
    resolution: NEW
  - gap_code: GAP-06
    source_finding: {phase: p3, register: authoring_decisions, key: Declare where the boundary declarations are found}
    capability: Declare where the boundary declarations are found
    owner_subdomain: identity
    resolution: NEW
  - gap_code: GAP-07
    source_finding: {phase: p3, register: authoring_decisions, key: Show a person a form and its answer}
    capability: Show a person a form and its answer
    owner_subdomain: identity
    resolution: NEW
  - gap_code: GAP-08
    source_finding: {phase: p3, register: authoring_decisions, key: Carry a detail from one page to the next}
    capability: Carry a detail from one page to the next
    owner_subdomain: identity
    resolution: NEW
  - gap_code: GAP-09
    source_finding: {phase: p3, register: authoring_decisions, key: Show the functions the business has not built}
    capability: Show the functions the business has not built
    owner_subdomain: identity
    resolution: NEW
  - gap_code: GAP-10
    source_finding: {phase: p3, register: authoring_decisions, key: 'Announce the moments an actor is registered, accepted and rejected'}
    capability: Announce the moments an actor is registered, accepted and rejected
    owner_subdomain: construction — how artifacts are rendered, not identity
    resolution: DEFERRED
  - gap_code: GAP-11
    source_finding: {phase: p3, register: analysis_findings, key: Q5}
    capability: Hold what an act requires with the act that requires it
    owner_subdomain: identity, in a later change
    resolution: DEFERRED
  design_decisions:
  - number: '1'
    decision: Both acts share one way in, and the request names the act.
    source_finding: {phase: p3, register: analysis_findings, key: Q1}
    rationale: The business will add many acts and declines to hand callers a new address for each. Seventeen acts already share one way in.
    constraints_imposed: Adding a function later adds a name, never a place. The way in admits only names the business has offered.
  - number: '2'
    decision: The public name of an act is declared apart from the act it reaches.
    source_finding: {phase: p3, register: analysis_findings, key: Q2}
    rationale: The name is the business's word for what it does; the act is how it does it, and the business intends to stay free to change that.
    constraints_imposed: No caller may name an act by the workflow that performs it, and re-pointing an act may not change what a caller sends.
  - number: '3'
    decision: What an act requires but a caller must not send is held in the declaration that admits the request.
    source_finding: {phase: p3, register: analysis_findings, key: Q4}
    rationale: The acts take their own rules through the same door as the caller's data. Held at the boundary they are sealed in the snapshot and stated once, rather than supplied by whoever calls.
    constraints_imposed: The caller sends only their own details. Nothing the business judges by may reach it from outside, and none of it may live in the page.
  - number: '4'
    decision: Holding that configuration at the boundary is accepted as the wrong long-term placement.
    source_finding: {phase: p3, register: analysis_findings, key: Q5}
    rationale: Rules belong with the function that owns them, not with the door it is reached through. Moving them reopens two sealed acts, which this change states it does not do.
    constraints_imposed: Recorded as GAP-11. Until it is taken up, a change to those rules is a change to a boundary declaration.
  - number: '5'
    decision: The readability test is stated at the boundary and applied by the act, and the two statements name the same fields.
    source_finding: {phase: p3, register: analysis_findings, key: Q6}
    rationale: The business refuses to have two tests, and two tests for one question is how they come to disagree.
    constraints_imposed: Neither statement may be changed without the other.
  - number: '6'
    decision: Three of the four refusals carry distinct governed kinds; the remaining pair is distinguished by what the answer states.
    source_finding: {phase: p3, register: analysis_findings, key: Q8}
    rationale: The kinds of answer are a closed governed set with no kind for an act that ran and refused. Two answers differing in what they state are not the same answer.
    constraints_imposed: A caller turned away is told which fields were at fault; a caller the business refused is told the act ran. A kind for an act that refused is a change to the platform, not to this domain.
  - number: '7'
    decision: The pages are lifted from the prior implementation and what they say to the platform is replaced.
    source_finding: {phase: p3, register: authoring_decisions, key: Show a person a form and its answer}
    rationale: The existing pages already hold no rules, which is the constraint the business cares about. They name an act's implementation and read an answer this platform does not produce, and both must go.
    constraints_imposed: No page may validate, judge or keep a copy of what the business holds.
  - number: '8'
    decision: Nothing in this change depends on a moment being announced.
    source_finding: {phase: p3, register: analysis_findings, key: Q10}
    rationale: The caller is answered from the act's own result, and the trail of occurrences is written by the acts. The three declared moments cannot presently be announced, for a reason outside this domain.
    constraints_imposed: No artifact of this change may be reached by an announcement, and GAP-10 is not a prerequisite of it.
  authoring_scope:
  - capability: Offer registering an actor to a caller outside the business
    gap_register_ref: GAP-01
  - capability: Offer recording a verification decision to a caller outside the business
    gap_register_ref: GAP-02
  - capability: Hold what an act requires and a caller must not send
    gap_register_ref: GAP-03
  - capability: Tell a caller how their registration ended
    gap_register_ref: GAP-04
  - capability: Tell a caller how their decision ended
    gap_register_ref: GAP-05
  - capability: Declare where the boundary declarations are found
    gap_register_ref: GAP-06
  - capability: Show a person a form and its answer
    gap_register_ref: GAP-07
  - capability: Carry a detail from one page to the next
    gap_register_ref: GAP-08
  - capability: Show the functions the business has not built
    gap_register_ref: GAP-09
```

Consolidation of Stages 1–3. Every capability committed at Stage 3 appears here with the status its
decision implies: what is reused already exists and runs, what is authored is a declared gap.
Nothing is re-litigated and nothing new is decided. Two gaps are owned outside this subdomain, which
the register records rather than hides.

---

## 1. Discovery Summary

### Actors (actors)

### Entities (bm_entities)

### Resources

### Events (events)

### Relationships (Candidate Capabilities)

## 2. Capability Graph (capability_graph)

## 3. Dependency Graph (dependency_graph)

## 4. Constraint Register (constraint_register)

## 5. Gap Register (gap_register)

## 6. Design Decisions (design_decisions)

## 7. Authoring Scope (authoring_scope)

### In Scope — This CR

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Announce the moments an actor is registered, accepted and rejected | GAP-10 is owned by construction rather than by identity. The three moments are already declared and correct; what cannot presently reach them is how artifacts are rendered, and a business domain does not author that. Nothing in this change depends on it. |
| Hold what an act requires with the act that requires it | GAP-11. Better placement, and it reopens two sealed acts, which this change states it does not do. |
| Establishing who a caller is, and what they are allowed to do | Deferred by the business with the question of who may be an authority, which the previous change already deferred. |
| Looking up an actor from outside | Deferred by the business; it would rather offer nothing than a reading surface whose shape it has not decided. |
| Telling a person anything after they leave the page | Deferred by the business; making the person wait for it is what caused the trouble before. |
| A way in for wallet, transaction, mempool, block, chain and consensus | Each comes with the function it belongs to. |
| A kind of answer for an act that ran and refused | A change to the platform's closed governed set, not to this domain. |

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 1 — Change Request & Input Elicitation | Classification + Problem + Outcome + Known Facts | COMPLETE |
| Stage 2 — Domain Model Discovery | Actors, Entities, Resources, Events, Relationships | COMPLETE |
| Stage 3 — Analysis Loop | Capability Graph, Dependency Graph, Constraints, Gap Register | COMPLETE — SATURATED |
| Stage 4 — Business Model | This document | COMPLETE |
| Stage 4b — Authoring Scope | IN/FUTURE CR boundary | PENDING |

---

## gov_projection — Governed Handoff to Stage 5

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 1 | cr_type · constraints · business_invariants · authority_boundaries · out_of_scope |
| **Consumes** ← Stage 2 | entities · entity_attributes · business_processes · pps_baseline_fqdns |
| **Consumes** ← Stage 3 | authoring_decisions · dependency_discoveries · placement_decision · saturation |
| **Emits** → Stage 5 | actors · bm_entities · events · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
