# Stage 4 — Business Model: blockchain / identity

**Stage:** 4 — Business Model
**CR:** cr_02_identity
**Status:** DRAFT
**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3. Every capability committed at Stage 3 appears here with the status its
decision implies: what is reused already exists and runs, what is authored is a declared gap.
Nothing is re-litigated and nothing new is decided. Two gaps are owned outside this subdomain, which
the register records rather than hides.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| The person registering | Reaches the business from outside, supplies their own identifying details and is told what happened. Not established to be who they claim. | Ordinary participant | S1 known_facts #1 |
| The authority | Reaches the business from outside and records a decision about a registered actor. Names itself, and the claim is not checked. | External business authority | S1 known_facts #43 |
| Identity | Holds the acts being reached, and decides what is offered and what is turned away. | Owning subdomain | S3 placement_decision EXTEND |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| Offered Act | An act the business has chosen to make reachable from outside, named by its business name. | None — declared, not stored. | S3 analysis_findings Q2 |
| Request | What a caller sends: the name of the act they want, and the details that act needs. | None — answered and not kept. | S3 analysis_findings Q1 |
| Answer | What the business tells a caller in reply. One of three kinds, and never leaving the caller to guess which. | None — composed for one caller; the record of what happened is the occurrence the act itself writes. | S3 analysis_findings Q7 |
| Carried Detail | Something the person has just typed, held only to save them typing it again on the next page. | None the business holds; it lives with whoever fills in the form and the business never reads it. | S3 analysis_findings Q11 |
| Actor | A person known to the system. Named because the acts being reached are acts upon one; unchanged by this change. | Already held by the acts, unchanged. | S3 analysis_findings Q5 |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| NONE IDENTIFIED |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| NONE IDENTIFIED | This change recognises no new moment. The moments identity recognises are unchanged and are named by the previous change. | Nothing an actor undergoes is added, removed or altered by making the acts reachable. | S1 business_events #1 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| A caller | names | an offered act | Offer registering an actor to a caller outside the business | S3 authoring_decisions Offer registering an actor to a caller outside the business |
| A caller | sends | the details an act needs | Hold what an act requires and a caller must not send | S3 authoring_decisions Hold what an act requires and a caller must not send |
| The business | turns away | a request it does not offer or cannot read | Offer both acts through one way in | S3 authoring_decisions Offer both acts through one way in |
| The business | tells | a caller how their request ended | Tell a caller how their registration ended | S3 authoring_decisions Tell a caller how their registration ended |
| A page | carries | a detail to the next page | Carry a detail from one page to the next | S3 authoring_decisions Carry a detail from one page to the next |
| The front page | names | a function that is not yet available | Show the functions the business has not built | S3 authoring_decisions Show the functions the business has not built |

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Admit a person's registration | S3 authoring_decisions Admit a person's registration | SATISFIED |  | Reused as-is and not amended. The act exists and runs; only the way in is new. |
| Record an authority's decision | S3 authoring_decisions Record an authority's decision | SATISFIED |  | Reused as-is and not amended. |
| Read a registration for absent or malformed details | S3 authoring_decisions Read a registration for absent or malformed details | SATISFIED |  | Reused as-is. The test takes the declaration it applies as an input, which is what makes it reusable without being restated. |
| Offer both acts through one way in | S3 authoring_decisions Offer both acts through one way in | SATISFIED |  | Reused. What binds a place to a name is configuration the boundary is pointed at, not an artifact of the composition. |
| Offer registering an actor to a caller outside the business | S3 authoring_decisions Offer registering an actor to a caller outside the business | CRITICAL | GAP-01 | The public name of the act and what a caller may send. Declared apart from the act it reaches, so the name outlives it. |
| Offer recording a verification decision to a caller outside the business | S3 authoring_decisions Offer recording a verification decision to a caller outside the business | CRITICAL | GAP-02 | A name of its own, because what a caller may send differs entirely from registration. |
| Hold what an act requires and a caller must not send | S3 authoring_decisions Hold what an act requires and a caller must not send | CRITICAL | GAP-03 | Held within the two admissions above, sealed in the snapshot and stated once. Better placed with the acts themselves, which GAP-11 records. |
| Tell a caller how their registration ended | S3 authoring_decisions Tell a caller how their registration ended | CRITICAL | GAP-04 | Which kind of answer each ending takes, and what of the act's result is exposed. |
| Tell a caller how their decision ended | S3 authoring_decisions Tell a caller how their decision ended | CRITICAL | GAP-05 | The same over that act's endings, including the absent actor, which is already a distinct kind. |
| Declare where the boundary declarations are found | S3 authoring_decisions Declare where the boundary declarations are found | CRITICAL | GAP-06 | The domain's build manifest admits both kinds while declaring no place they could be found. |
| Show a person a form and its answer | S3 authoring_decisions Show a person a form and its answer | CRITICAL | GAP-07 | Two forms. Lifted from the prior implementation, which holds no rules; what they say to the platform is replaced. |
| Carry a detail from one page to the next | S3 authoring_decisions Carry a detail from one page to the next | CRITICAL | GAP-08 | A convenience, bounded so that nothing the business does depends on it. |
| Show the functions the business has not built | S3 authoring_decisions Show the functions the business has not built | CRITICAL | GAP-09 | Four of six named and marked not yet available. |
| Announce the moments an actor is registered, accepted and rejected | S3 authoring_decisions Announce the moments an actor is registered, accepted and rejected | CRITICAL | GAP-10 | The three moments are declared and cannot presently be announced. The cause is in construction, not in this domain, and nothing in this change depends on one being announced. |

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| identity | blockchain::WF_REGISTER_ACTOR_V0 | act reached from outside | SATISFIED | S3 dependency_discoveries The act that admits a person |
| identity | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | act reached from outside | SATISFIED | S3 dependency_discoveries The act that records a decision |
| identity | blockchain::CC_VALIDATE_REGISTRATION_V0 | capability call | SATISFIED | S3 dependency_discoveries Reading a record for absence and form |
| identity | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | capability call | SATISFIED | S3 dependency_discoveries Reading a record for absence and form |
| identity | fb.transport::CONSTITUTION_TRANSPORT_INGRESS_V0 | governed by | SATISFIED | S3 dependency_discoveries The boundary's ingress and egress kinds |
| identity | fb.transport::CONSTITUTION_TRANSPORT_EGRESS_V0 | governed by | SATISFIED | S3 dependency_discoveries The boundary's ingress and egress kinds |
| identity | blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 | build manifest | SATISFIED | S3 dependency_discoveries A source layer for the boundary declarations |
| identity | blockchain::AC_PARTICIPANT_V0 | actor declaration | SATISFIED | S3 dependency_discoveries The act that admits a person |
| identity | workload::TI_COLLATZ_COMPUTE_V0 | worked precedent | SATISFIED | S3 dependency_discoveries The name a caller uses for an act |
| identity | workload::TE_COLLATZ_COMPUTE_V0 | worked precedent | SATISFIED | S3 dependency_discoveries The kinds of answer a caller is told |

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|------------|----------------|--------|
| 1 | No business rule may live in the web page. | S1 constraints #1 | The business author |
| 2 | The page may hold only what the person has just typed, and only to save them retyping it. | S1 constraints #2 | The business author |
| 3 | The web page must not check details before sending them. | S1 constraints #3 | The business author |
| 4 | The page must be plain and quick to load — a form and an answer, not an application. | S1 constraints #4 | The business author |
| 5 | There is one way in, and the request names the act. | S1 constraints #5 | The business author |
| 6 | The name of an act is the business's public word for it and must outlive changes to how the act is performed. | S1 constraints #6 | The business author |
| 7 | The readability test must be the one the previous change defined, not a second one. | S1 constraints #7 | The business author |
| 8 | Only acts the business has chosen to offer may be reached. | S1 constraints #8 | The business author |
| 9 | The change introduces no identity behaviour and revisits no decision the previous change made. | S1 constraints #9 | The business author |
| 10 | The kinds of answer a caller may be told are a closed governed set, which this change does not extend. | S3 analysis_findings Q7 | The platform's egress governance |

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-01 | S3 authoring_decisions Offer registering an actor to a caller outside the business | Offer registering an actor to a caller outside the business | identity | NEW |
| GAP-02 | S3 authoring_decisions Offer recording a verification decision to a caller outside the business | Offer recording a verification decision to a caller outside the business | identity | NEW |
| GAP-03 | S3 authoring_decisions Hold what an act requires and a caller must not send | Hold what an act requires and a caller must not send | identity | NEW |
| GAP-04 | S3 authoring_decisions Tell a caller how their registration ended | Tell a caller how their registration ended | identity | NEW |
| GAP-05 | S3 authoring_decisions Tell a caller how their decision ended | Tell a caller how their decision ended | identity | NEW |
| GAP-06 | S3 authoring_decisions Declare where the boundary declarations are found | Declare where the boundary declarations are found | identity | NEW |
| GAP-07 | S3 authoring_decisions Show a person a form and its answer | Show a person a form and its answer | identity | NEW |
| GAP-08 | S3 authoring_decisions Carry a detail from one page to the next | Carry a detail from one page to the next | identity | NEW |
| GAP-09 | S3 authoring_decisions Show the functions the business has not built | Show the functions the business has not built | identity | NEW |
| GAP-10 | S3 authoring_decisions Announce the moments an actor is registered, accepted and rejected | Announce the moments an actor is registered, accepted and rejected | construction — how artifacts are rendered, not identity | DEFERRED |
| GAP-11 | S3 analysis_findings Q5 | Hold what an act requires with the act that requires it | identity, in a later change | DEFERRED |

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | Both acts share one way in, and the request names the act. | S3 analysis_findings Q1 | The business will add many acts and declines to hand callers a new address for each. Seventeen acts already share one way in. | Adding a function later adds a name, never a place. The way in admits only names the business has offered. |
| 2 | The public name of an act is declared apart from the act it reaches. | S3 analysis_findings Q2 | The name is the business's word for what it does; the act is how it does it, and the business intends to stay free to change that. | No caller may name an act by the workflow that performs it, and re-pointing an act may not change what a caller sends. |
| 3 | What an act requires but a caller must not send is held in the declaration that admits the request. | S3 analysis_findings Q4 | The acts take their own rules through the same door as the caller's data. Held at the boundary they are sealed in the snapshot and stated once, rather than supplied by whoever calls. | The caller sends only their own details. Nothing the business judges by may reach it from outside, and none of it may live in the page. |
| 4 | Holding that configuration at the boundary is accepted as the wrong long-term placement. | S3 analysis_findings Q5 | Rules belong with the function that owns them, not with the door it is reached through. Moving them reopens two sealed acts, which this change states it does not do. | Recorded as GAP-11. Until it is taken up, a change to those rules is a change to a boundary declaration. |
| 5 | The readability test is stated at the boundary and applied by the act, and the two statements name the same fields. | S3 analysis_findings Q6 | The business refuses to have two tests, and two tests for one question is how they come to disagree. | Neither statement may be changed without the other. |
| 6 | Three of the four refusals carry distinct governed kinds; the remaining pair is distinguished by what the answer states. | S3 analysis_findings Q8 | The kinds of answer are a closed governed set with no kind for an act that ran and refused. Two answers differing in what they state are not the same answer. | A caller turned away is told which fields were at fault; a caller the business refused is told the act ran. A kind for an act that refused is a change to the platform, not to this domain. |
| 7 | The pages are lifted from the prior implementation and what they say to the platform is replaced. | S3 authoring_decisions Show a person a form and its answer | The existing pages already hold no rules, which is the constraint the business cares about. They name an act's implementation and read an answer this platform does not produce, and both must go. | No page may validate, judge or keep a copy of what the business holds. |
| 8 | Nothing in this change depends on a moment being announced. | S3 analysis_findings Q10 | The caller is answered from the act's own result, and the trail of occurrences is written by the acts. The three declared moments cannot presently be announced, for a reason outside this domain. | No artifact of this change may be reached by an announcement, and GAP-10 is not a prerequisite of it. |

## 7. Authoring Scope (authoring_scope)

<!-- register:authoring_scope -->
### In Scope — This CR
| Capability | Gap Register Ref |
|-----------|-----------------|
| Offer registering an actor to a caller outside the business | GAP-01 |
| Offer recording a verification decision to a caller outside the business | GAP-02 |
| Hold what an act requires and a caller must not send | GAP-03 |
| Tell a caller how their registration ended | GAP-04 |
| Tell a caller how their decision ended | GAP-05 |
| Declare where the boundary declarations are found | GAP-06 |
| Show a person a form and its answer | GAP-07 |
| Carry a detail from one page to the next | GAP-08 |
| Show the functions the business has not built | GAP-09 |

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
