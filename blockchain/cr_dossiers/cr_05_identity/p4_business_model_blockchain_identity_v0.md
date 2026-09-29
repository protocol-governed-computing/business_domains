# Stage 4 — Business Model: blockchain / identity

**Stage:** 4 — Business Model

**CR:** cr_05_identity

**Status:** DRAFT

**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3. Every capability committed at Stage 3 appears here with the status its
decision implies. Nothing is re-litigated and nothing new is decided. Every capability that changes
is an extension of one identity already has: each step keeps doing what it does, and holds the rule
it applies instead of being handed it.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| The person registering | Supplies a registration and is held unverified. | Ordinary participant | S1 known_facts #1 |
| The authority | Records a decision about an unverified person, never about themselves. | External business authority | S1 known_facts #5 |
| Identity | Holds the record, and now holds every rule it applies to it. | Owning subdomain | S3 placement_decision EXTEND |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| The Record | What the business holds about a person: their registration, their state and the decision made about them. | One keyed store, one record per contact address, unchanged. | S2 entities #1 |
| The Registration | The name and the address a person is reached at, both required. | Held in the record when the person is registered unverified. | S3 analysis_findings Q6 |
| The Decision | An acceptance or a rejection, the authority, and the grounds. | Written into the record's decided parts, built from the decision identity checked. | S3 analysis_findings Q5 |
| The Business's Rules | What a registration must contain, which states admit a decision, which decisions may be recorded, that an authority does not decide about themselves, and that a rejection states grounds. | Held by the identity steps that apply them. Held by nothing today. | S3 analysis_findings Q1 |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| NONE IDENTIFIED |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| NONE IDENTIFIED | This change recognises no new moment. | The moments identity records are unchanged in when they occur and in what they mean. | S1 business_events #1 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Identity | refuses | a registration missing what it must contain | Check a registration and refuse an incomplete one | S3 authoring_decisions Check a registration and refuse an incomplete one |
| Identity | records | a person as unverified when they register | Register a person unverified | S3 authoring_decisions Register a person unverified |
| An authority | records | an acceptance or a rejection about an unverified person | Record a decision only about an unverified person, and only an acceptance or a rejection | S3 authoring_decisions Record a decision only about an unverified person, and only an acceptance or a rejection |
| Identity | refuses | an authority deciding about themselves | Refuse an authority deciding about themselves | S3 authoring_decisions Refuse an authority deciding about themselves |
| Identity | refuses | a rejection stating no grounds | Refuse a rejection stating no grounds | S3 authoring_decisions Refuse a rejection stating no grounds |

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Check a registration and refuse an incomplete one | S3 authoring_decisions Check a registration and refuse an incomplete one | CRITICAL | GAP-01 | The check finds what is missing today and refuses nothing. It holds what a registration must contain and refuses on what it finds. |
| Record a decision only about an unverified person, and only an acceptance or a rejection | S3 authoring_decisions Record a decision only about an unverified person, and only an acceptance or a rejection | CRITICAL | GAP-02 | The deciding step holds both sets and builds the record from the decision it checked. |
| Refuse an authority deciding about themselves | S3 authoring_decisions Refuse an authority deciding about themselves | CRITICAL | GAP-03 | A comparison of the authority with the person, and a fixed rule on its result. |
| Refuse a rejection stating no grounds | S3 authoring_decisions Refuse a rejection stating no grounds | CRITICAL | GAP-04 | The grounds step holds its own rules. |
| Fix the decision each act records | S3 authoring_decisions Fix the decision each act records | CRITICAL | GAP-05 | The acceptance act records an acceptance, the rejection act a rejection. |
| Register a person unverified | S3 authoring_decisions Register a person unverified | CRITICAL | GAP-06 | The registration act writes the state unverified as its own. |
| Reach identity from outside | S3 authoring_decisions Reach identity from outside | CRITICAL | GAP-07 | The entrances stop supplying what identity now holds; a caller sends and is told what they are today. |
| Admit an acceptance with its grounds | S3 authoring_decisions Admit an acceptance with its grounds | CRITICAL | GAP-08 | The acceptance gate declares the optional grounds the act reads. |
| Record the moment of each act | S3 authoring_decisions Record the moment of each act | SATISFIED |  | Unchanged; the moment stays the request's to name, outside this change. |

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| identity | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | platform transform | SATISFIED | S3 dependency_discoveries Checking a record's structure |
| identity | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | platform transform | SATISFIED | S3 dependency_discoveries Refusing on a list of rules |
| identity | capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 | platform transform | SATISFIED | S3 dependency_discoveries Refusing a value outside a set |
| identity | capability_transforms::CT_PURE_COMPARE_EQUAL_V0 | platform transform | SATISFIED | S3 dependency_discoveries Comparing two values |
| identity | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | platform transform | SATISFIED | S3 dependency_discoveries Assembling a record from fields |
| identity | blockchain::CC_RESOLVE_ACTOR_V0 | capability contract | SATISFIED | S3 dependency_discoveries Resolving the person, claiming the address, writing the record, appending the moment |
| identity | blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | capability contract | SATISFIED | S3 dependency_discoveries Resolving the person, claiming the address, writing the record, appending the moment |
| identity | blockchain::CC_REGISTER_ACTOR_V0 | capability contract | SATISFIED | S3 dependency_discoveries Resolving the person, claiming the address, writing the record, appending the moment |
| identity | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | capability contract | SATISFIED | S3 dependency_discoveries Resolving the person, claiming the address, writing the record, appending the moment |
| identity | blockchain::CC_VALIDATE_REGISTRATION_V0 | amended contract | SATISFIED | S3 dependency_discoveries Checking a registration |
| identity | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | amended contract | SATISFIED | S3 dependency_discoveries Recording a decision |
| identity | blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 | amended contract | SATISFIED | S3 dependency_discoveries Requiring rejection grounds |

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|------------|----------------|--------|
| 1 | Nothing a caller sees through the public entrance changes: the same requests are admitted and refused, with the same answers. | S1 constraints #1 | The business author |
| 2 | Records made under a request's own rules stay as they were made. | S1 constraints #2 | The business author |
| 3 | What a request says about the business's rules is ignored, not refused. | S1 known_facts #9 | The business author |
| 4 | A refusal changes no record. | S1 known_facts #10 | The business author |

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-01 | S3 authoring_decisions Check a registration and refuse an incomplete one | Check a registration and refuse an incomplete one | identity | EXTEND |
| GAP-02 | S3 authoring_decisions Record a decision only about an unverified person, and only an acceptance or a rejection | Record a decision only about an unverified person, and only an acceptance or a rejection | identity | EXTEND |
| GAP-03 | S3 authoring_decisions Refuse an authority deciding about themselves | Refuse an authority deciding about themselves | identity | EXTEND |
| GAP-04 | S3 authoring_decisions Refuse a rejection stating no grounds | Refuse a rejection stating no grounds | identity | EXTEND |
| GAP-05 | S3 authoring_decisions Fix the decision each act records | Fix the decision each act records | identity | EXTEND |
| GAP-06 | S3 authoring_decisions Register a person unverified | Register a person unverified | identity | EXTEND |
| GAP-07 | S3 authoring_decisions Reach identity from outside | Reach identity from outside | identity | EXTEND |
| GAP-08 | S3 authoring_decisions Admit an acceptance with its grounds | Admit an acceptance with its grounds | identity | EXTEND |
| GAP-09 | S3 analysis_findings Q9 | Record the moment of each act as the act's own | identity, in a later change | DEFERRED |

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | Each rule is held by the step that applies it, as a fixed value. | S3 analysis_findings Q3 | A rule written where it is applied holds for every act that composes the step, and no act or request can widen it. | Nothing may hand identity a rule identity holds. |
| 2 | The registration check is followed by a rule refusing when it found anything. | S3 analysis_findings Q2 | The platform check stays a reporter, as ruled; the business's contract decides. | The check's report is consumed, never left unread. |
| 3 | The self-decision rule is a comparison followed by a fixed rule on its result. | S3 analysis_findings Q4 | The rule checker compares a field only against a fixed value, and the platform already offers the comparison. | No platform transform is changed or added. |
| 4 | The decided record is built from the decision the step checked, and each act fixes its decision. | S3 analysis_findings Q5 | The state recorded must be the decision admitted, and a rejection must pass the rejection act's grounds rule. | No part of the decided record may come from the request except the authority and the grounds. |
| 5 | Registration writes the state unverified as its own. | S3 analysis_findings Q6 | The business's lifecycle has one way in, and it leads to unverified. | No request can register a person in any other state. |
| 6 | The entrances stop supplying what identity holds, and change nothing a caller sends or is told. | S3 analysis_findings Q7 | Constants nothing reads would read as the rule. | Every request the entrance admits today reaches the same outcome afterwards. |
| 7 | Records made before this change are left as they are. | S3 analysis_findings Q10 | The record is added to and never rewritten. | No migration, backfill or repair step may be authored. |

## 7. Authoring Scope (authoring_scope)

<!-- register:authoring_scope -->
### In Scope — This CR
| Capability | Gap Register Ref |
|-----------|-----------------|
| Check a registration and refuse an incomplete one | GAP-01 |
| Record a decision only about an unverified person, and only an acceptance or a rejection | GAP-02 |
| Refuse an authority deciding about themselves | GAP-03 |
| Refuse a rejection stating no grounds | GAP-04 |
| Fix the decision each act records | GAP-05 |
| Register a person unverified | GAP-06 |
| Reach identity from outside | GAP-07 |
| Admit an acceptance with its grounds | GAP-08 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Record the moment of each act as the act's own | GAP-09. The moment and its stream come from the request; no rule of the business names them, and this change does not ask. |
| Records made under a request's own rules | Declined by the business: the record is added to and never rewritten. |

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
