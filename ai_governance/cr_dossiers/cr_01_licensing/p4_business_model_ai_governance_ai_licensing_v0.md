# Stage 4 — Business Model: ai_governance / ai_licensing

**Stage:** 4 — Business Model

**CR:** cr_01_licensing

**Status:** DRAFT

**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3. Every capability committed at Stage 3 appears here with the status its
decision implies. Nothing is re-litigated and nothing new is decided.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| The build | Runs every stated case against its check. | Platform | S2 business_processes #1 |
| AI Licensing | Holds the checks and now their cases. | Owning subdomain | S3 placement_decision EXTEND |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| The Check | One of the three decisions, unchanged. | None; computed. | S2 entities #1 |
| The Case | What a check is given and what it answers, or that it refuses. | Stated beside its check. | S2 entities #4 |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| NONE IDENTIFIED |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| NONE IDENTIFIED | This change recognises no new moment. | Nothing is announced. | S1 business_events #1 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| The build | proves | each check by its cases | Prove the license check | S3 authoring_decisions Prove the license check |

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Prove the license check | S3 authoring_decisions Prove the license check | CRITICAL | GAP-01 | The check is stated with its cases. |
| Prove the training check | S3 authoring_decisions Prove the training check | CRITICAL | GAP-02 | The check is stated with its cases. |
| Prove the inactivity check | S3 authoring_decisions Prove the inactivity check | CRITICAL | GAP-03 | The check is stated with its cases. |
| Compile the cases stated beside each check | S3 authoring_decisions Compile the cases stated beside each check | CRITICAL | GAP-04 | The configuration is regenerated. |

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| ai_licensing | ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0 | amended transform | SATISFIED | S3 dependency_discoveries The license check |
| ai_licensing | ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0 | amended transform | SATISFIED | S3 dependency_discoveries The training check |
| ai_licensing | ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 | amended transform | SATISFIED | S3 dependency_discoveries The inactivity check |
| ai_licensing | ai_governance::STRUCTURE_BUILD_AI_GOVERNANCE_CONFIG_V0 | generated structure | SATISFIED | S3 dependency_discoveries The build configuration |

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|------------|----------------|--------|
| 1 | What each check decides, and every act that uses them, is unchanged. | S1 constraints #1 | The business author |

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-01 | S3 authoring_decisions Prove the license check | Prove the license check | ai_licensing | EXTEND |
| GAP-02 | S3 authoring_decisions Prove the training check | Prove the training check | ai_licensing | EXTEND |
| GAP-03 | S3 authoring_decisions Prove the inactivity check | Prove the inactivity check | ai_licensing | EXTEND |
| GAP-04 | S3 authoring_decisions Compile the cases stated beside each check | Compile the cases stated beside each check | ai_licensing | EXTEND |

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | Each check is stated whole, as it stands, with its cases. | S3 analysis_findings Q1 | A case belongs to a transform the design names. | No check changes what it decides. |
| 2 | A no case expects a refusal; a yes case keeps its answer. | S3 analysis_findings Q2 | The checks refuse, as the business decided. | Every no case is a VIOLATION case. |
| 3 | The earlier values stay, under this system's names, with one boundary case added. | S3 analysis_findings Q4 | The author answered both. | Nothing beyond the earlier cases and the boundary. |
| 4 | The build configuration is reached through its generator. | S3 analysis_findings Q5 | It is derived from the design. | No hand edit. |

## 7. Authoring Scope (authoring_scope)

<!-- register:authoring_scope -->
### In Scope — This CR
| Capability | Gap Register Ref |
|-----------|-----------------|
| Prove the license check | GAP-01 |
| Prove the training check | GAP-02 |
| Prove the inactivity check | GAP-03 |
| Compile the cases stated beside each check | GAP-04 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| NONE IDENTIFIED | |

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 4 — Business Model | This document | COMPLETE |

---

## gov_projection — Governed Handoff to Stage 5

| Direction | Fields |
|-----------|--------|
| **Emits** → Stage 5 | actors · bm_entities · events · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
