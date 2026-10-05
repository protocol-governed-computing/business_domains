# Stage 4 — Business Model: ai_governance / agent_governance

**Stage:** 4 — Business Model

**CR:** cr_03_parameter_result

**Status:** DRAFT

**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3. Nothing is re-litigated and nothing new is decided.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| Agent Governance | Checks an agent's action against the rules declared for its tool. | Owning subdomain | S3 placement_decision agent_governance |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| The Governed Action | An agent's proposed action, judged and recorded. | Recorded in the governance audit. | S2 entities #1 |
| The Parameter Check | The step that checks an action's parameters. | Run by the governed action. | S2 entities #2 |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| NONE IDENTIFIED |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| NONE IDENTIFIED | This change recognises no new moment. | | S1 business_events #1 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Agent Governance | checks | an action's parameters | Check an action's parameters | S3 authoring_decisions Check an action's parameters |

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Check an action's parameters | S3 authoring_decisions Check an action's parameters | CRITICAL | GAP-01 | A new version that reports what it receives. |

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| agent_governance | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | transform | SATISFIED | S3 dependency_discoveries Checking against rules |
| agent_governance | capability_transforms::CT_PURE_LOOKUP_V0 | transform | SATISFIED | S3 dependency_discoveries Looking up a tool's rules |

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|------------|----------------|--------|
| 1 | The governed action decides exactly as it does today. | S1 constraints #1 | The business author |

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-01 | S3 authoring_decisions Check an action's parameters | Check an action's parameters | agent_governance | AUTHOR_NEW |

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | The new parameter check reports whether every declared rule passed, from the check's own answer. | S3 analysis_findings Q1 | A check reports only what it receives. | Its steps, rules and routes are those of the old check. |
| 2 | The old parameter check is replaced by the new version. | S3 analysis_findings Q2 | A change of what a check reports is a new version. | The old check stays in the record and out of reach. |
| 3 | The governed action is re-pointed to the new version. | S3 analysis_findings Q3 | It decides exactly as today. | Only the check its place runs changes. |

## 7. Authoring Scope (authoring_scope)

<!-- register:authoring_scope -->
### In Scope — This CR
| Capability | Gap Register Ref |
|-----------|-----------------|
| Check an action's parameters | GAP-01 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| NONE IDENTIFIED | |

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
