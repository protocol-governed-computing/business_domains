# Stage 4 — Business Model: ai_governance / ai_licensing

**Stage:** 4 — Business Model

**CR:** cr_02_reclaim_closure

**Status:** DRAFT

**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3. Nothing is re-litigated and nothing new is decided.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| The business | Reclaims licenses on its schedule. Unchanged by this change. | Owning business | S2 business_processes #1 |
| AI Licensing | Ends a reclaim the registry refuses, with the license still assigned. | Owning subdomain | S3 placement_decision EXTEND |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| The Assignment | A license held by an employee. | One registry, unchanged. | S2 entities #1 |
| The Reclaim | Taking back an unused license. | An act, announced when it removes an assignment. | S2 entities #2 |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| NONE IDENTIFIED |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| NONE IDENTIFIED | This change recognises no new moment. | A revocation is not announced for a refused removal. | S1 business_events #1 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| AI Licensing | ends | a reclaim the registry refuses | End a reclaim the registry refuses | S3 authoring_decisions End a reclaim the registry refuses |

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| End a reclaim the registry refuses | S3 authoring_decisions End a reclaim the registry refuses | CRITICAL | GAP-01 | The removal step ends the contract on a refused removal. |

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| ai_licensing | ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 | amended contract | SATISFIED | S3 dependency_discoveries Reclaiming a license |
| ai_licensing | capability_side_effects::CS_REGISTRY_V0 | platform capability | SATISFIED | S3 dependency_discoveries The license registry |
| ai_licensing | ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 | capability transform | SATISFIED | S3 dependency_discoveries The inactivity check |
| ai_licensing | ai_governance::WF_AUTO_RECLAIM_V0 | workflow | SATISFIED | S3 dependency_discoveries The reclaim act |

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|------------|----------------|--------|
| 1 | Every reclaim the registry does not refuse ends exactly as it did before this change. | S1 constraints #1 | The business author |
| 2 | No ending is added. | S1 constraints #2 | The business author |

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-01 | S3 authoring_decisions End a reclaim the registry refuses | End a reclaim the registry refuses | ai_licensing | EXTEND |

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | The removal step ends the contract on a refused removal. | S3 analysis_findings Q1 | A reclaim must not carry on past a removal the registry refused. | The removal step answers every outcome the registry declares. |
| 2 | A refused removal ends as still active. | S3 analysis_findings Q2 | The license stays assigned, which is what that ending says. | No route and no ending changes. |

## 7. Authoring Scope (authoring_scope)

<!-- register:authoring_scope -->
### In Scope — This CR
| Capability | Gap Register Ref |
|-----------|-----------------|
| End a reclaim the registry refuses | GAP-01 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Tell a refused removal apart from a license still in use | Declined for now by the business: both leave the license assigned. |

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
