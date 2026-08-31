# Stage 4 — Business Model: blockchain / identity

**Stage:** 4 — Business Model

**CR:** cr_03_identity

**Status:** DRAFT

**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3. Every capability committed at Stage 3 appears here with the status its
decision implies. Nothing is re-litigated and nothing new is decided. One capability is extended and
every other is satisfied by an artifact already in the composition, which is what a defect
correction looks like when the design was right and the artifact was not.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| The person registering | Supplies the details that are theirs and stay theirs. Takes no part in this change and is the party it exists for. | Ordinary participant | S1 known_facts #2 |
| The authority | Records a decision, which may change three things about a person and nothing else. | External business authority | S1 known_facts #10 |
| Identity | Holds the record and owns how a decision is written into it. | Owning subdomain | S3 placement_decision EXTEND |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| The Record | What the business holds about a person: their admitted details together with their decided details. | One keyed store, one record per contact address, declared once and read by one artifact. | S2 belief_verification #3 |
| Admitted Details | The name, contact address and preferences a person supplied at registration. | Held in the record, written when the person is admitted, and — today — removed when a decision is recorded. | S2 belief_verification #1 |
| Decided Details | The state, the deciding authority and the grounds: the three things a decision may change. | Held in the same record, written by the deciding act. | S3 analysis_findings Q4 |
| Thinned Record | A record a decision has already stripped of its admitted details. | The same store, left as it is. | S3 analysis_findings Q9 |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| NONE IDENTIFIED |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| NONE IDENTIFIED | This change recognises no new moment. | The moments the business records are unchanged in when they occur and in what they mean; the trail is unchanged by constraint. | S1 business_events #1 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| A decision | changes | the person's state, the deciding authority and the grounds | State which of a person's details a decision may change | S3 authoring_decisions State which of a person's details a decision may change |
| A decision | leaves | everything else the business holds about the person | Change part of a held record without replacing it | S3 authoring_decisions Change part of a held record without replacing it |
| An authority | records | a decision against a registered person | Record a decision against a registered person | S3 authoring_decisions Record a decision against a registered person |
| A person | keeps | the details they were admitted with | Change part of a held record without replacing it | S3 authoring_decisions Change part of a held record without replacing it |

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Record a decision against a registered person | S3 authoring_decisions Record a decision against a registered person | CRITICAL | GAP-01 | Right in every respect but one. Its refusals, inputs and result statuses are unchanged; the step that writes is replaced. |
| Change part of a held record without replacing it | S3 authoring_decisions Change part of a held record without replacing it | SATISFIED |  | The capability publishes a keyed update, and the domain already binds that capability because its keyed write is what the step uses today. |
| State which of a person's details a decision may change | S3 authoring_decisions State which of a person's details a decision may change | CRITICAL | GAP-02 | Realised as the set of fields the update sets. What is not in the set is what a decision may not touch. |
| Assemble the record a decision writes | S3 authoring_decisions Assemble the record a decision writes | CRITICAL | GAP-03 | Retained unchanged, and left without a consumer by GAP-01. Recorded rather than resolved. |
| Resolve the actor before a decision is recorded | S3 authoring_decisions Resolve the actor before a decision is recorded | SATISFIED |  | Unchanged, and the reason the two operations never disagree in practice. |
| Reach the decision from outside | S3 authoring_decisions Reach the decision from outside | SATISFIED |  | The four boundary declarations name the workflow, not the contract, and are untouched. |
| Restore details already lost | S3 authoring_decisions Restore details already lost | SATISFIED |  | Nothing is authored. The business declines to rewrite records already written. |

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| identity | capability_side_effects::CS_MUTABLE_JSON_V0 | capability call | SATISFIED | S3 dependency_discoveries Partial update of a held record at a key |
| identity | blockchain::STRUCTURE_IDENTITY_STORAGE_V0 | store declaration | SATISFIED | S3 dependency_discoveries The store the decision writes |
| identity | blockchain::RB_IDENTITY_BINDINGS_V0 | runtime binding | SATISFIED | S3 dependency_discoveries The binding that reaches the store |
| identity | blockchain::CC_RESOLVE_ACTOR_V0 | capability contract | SATISFIED | S3 dependency_discoveries Resolving the actor before deciding |
| identity | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | composing workflow | SATISFIED | S3 dependency_discoveries The workflows that compose the deciding contract |
| identity | blockchain::TI_ACCEPT_ACTOR_V0 | boundary declaration | SATISFIED | S3 dependency_discoveries What a caller may send and is told |
| identity | blockchain::TI_REJECT_ACTOR_V0 | boundary declaration | SATISFIED | S3 dependency_discoveries What a caller may send and is told |
| identity | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | amended contract | SATISFIED | S3 analysis_findings Q1 |

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|------------|----------------|--------|
| 1 | A decision may change only the person's state, the authority who decided, and the grounds stated. | S1 constraints #1 | The business author |
| 2 | A decision may change none of a person's own details. | S1 constraints #2 | The business author |
| 3 | What a caller sends and is told back is unchanged. | S1 constraints #3 | The business author |
| 4 | Records already written are never rewritten, including thin ones. | S1 constraints #4 | The business author |
| 5 | Grounds are required to reject and optional to accept. | S1 constraints #5 | Carried from the change that established the decision |
| 6 | What is recorded in the trail is unchanged. | S1 constraints #6 | The business author |

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-01 | S3 authoring_decisions Record a decision against a registered person | Record a decision against a registered person | identity | EXTEND |
| GAP-02 | S3 authoring_decisions State which of a person's details a decision may change | State which of a person's details a decision may change | identity | EXTEND |
| GAP-03 | S3 authoring_decisions Assemble the record a decision writes | Assemble the record a decision writes | identity, in a later change | DEFERRED |
| GAP-04 | S3 analysis_findings Q10 | Say which artifacts consume a store | the components that build and publish the composition's indexes, not identity | DEFERRED |

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | The deciding contract's write becomes a partial update, and nothing else about the contract changes. | S3 analysis_findings Q1 | Four of its five steps are correct. The defect is that one step writes a whole record where it must change part of one. | No refusal, input or result status of the contract may change, or the correction stops being a correction. |
| 2 | The fields the update sets are the three a decision is entitled to change. | S3 analysis_findings Q4 | Stating the rule as the set of updated fields puts it where a mechanism reads it. Stated only as an invariant it has been true and unenforced since the function was built. | Adding a field to that set is a business change, not a technical one. |
| 3 | The record is addressed by the key that identifies it, and the correction depends on no rule of this domain. | S3 analysis_findings Q3 | The store now offers a keyed update as well as a keyed write, so changing part of a record needs neither a replacement nor a filter. A correction that leaned on identity's uniqueness rule would have carried that rule wherever it was copied. | The correction is portable: any domain changing part of a record it did not create uses the same operation, with no invariant to re-establish. |
| 4 | A decision that reaches an actor the store does not hold now refuses instead of creating one. | S3 analysis_findings Q6 | The two operations disagree about an absent subject, and the disagreement is in the safe direction. | Nothing may rely on a decision creating the person it decides about. |
| 5 | The assembling step is retained though its output loses its consumer. | S3 analysis_findings Q5 | The business asked for the smallest correction that ends the data loss, and removing a step changes the contract's shape more than the defect requires. | A step whose output nothing reads is recorded as GAP-03 and not left unremarked. |
| 6 | Records already thinned are left as they are. | S3 analysis_findings Q9 | The record is added to and never rewritten, and that holds even when what was written is thin. | No migration, backfill or repair step may be authored. |

## 7. Authoring Scope (authoring_scope)

<!-- register:authoring_scope -->
### In Scope — This CR
| Capability | Gap Register Ref |
|-----------|-----------------|
| Record a decision against a registered person | GAP-01 |
| State which of a person's details a decision may change | GAP-02 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Assemble the record a decision writes | GAP-03. Its output loses its only consumer with this change. Removing it alters the contract's shape more than ending the data loss requires, and the business asked for the smallest correction. |
| Say which artifacts consume a store | GAP-04 is owned by the components that build and publish the composition's indexes. A business domain does not author them, and this change needed the answer and obtained it by reading the contracts instead. |
| Restoring details lost from records already thinned | Declined by the business: the record is added to and never rewritten. |
| Correcting a person's own details | Deferred by the business and unchanged. |
| Enforcing that a rejection states grounds inside the business | Unchanged by this change and enforced at the boundary only. |

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
