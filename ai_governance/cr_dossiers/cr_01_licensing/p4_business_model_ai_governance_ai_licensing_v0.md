# Stage 4 — Business Model: ai_governance / ai_licensing

## Machine

```yaml
document:
  phase: p4
  domain: ai_governance
  subdomain: ai_licensing
  cr: cr_01_licensing
  rule_set: transformation.schemas.REGISTER_SCHEMA_P4_V0
registers:
  actors:
  - actor: The build
    role: Runs every stated case against its check.
    authority_class: Platform
    source_finding: {phase: p2, register: business_processes, row: 1}
  - actor: AI Licensing
    role: Holds the checks and now their cases.
    authority_class: Owning subdomain
    source_finding: {phase: p3, register: placement_decision, key: EXTEND}
  bm_entities:
  - entity: The Check
    description: One of the three decisions, unchanged.
    store_model: None; computed.
    source_finding: {phase: p2, register: entities, row: 1}
  - entity: The Case
    description: What a check is given and what it answers, or that it refuses.
    store_model: Stated beside its check.
    source_finding: {phase: p2, register: entities, row: 4}
  resources: []
  events:
  - event: NONE IDENTIFIED
    trigger: This change recognises no new moment.
    lifecycle_meaning: Nothing is announced.
    source_finding: {phase: p1, register: business_events, row: 1}
  relationships:
  - subject: The build
    verb: proves
    object: each check by its cases
    capability_need: Prove the license check
    source_finding: {phase: p3, register: authoring_decisions, key: Prove the license check}
  capability_graph:
  - capability: Prove the license check
    source_finding: {phase: p3, register: authoring_decisions, key: Prove the license check}
    status: CRITICAL
    gap_register_entry: GAP-01
    notes: The check is stated with its cases.
  - capability: Prove the training check
    source_finding: {phase: p3, register: authoring_decisions, key: Prove the training check}
    status: CRITICAL
    gap_register_entry: GAP-02
    notes: The check is stated with its cases.
  - capability: Prove the inactivity check
    source_finding: {phase: p3, register: authoring_decisions, key: Prove the inactivity check}
    status: CRITICAL
    gap_register_entry: GAP-03
    notes: The check is stated with its cases.
  - capability: Compile the cases stated beside each check
    source_finding: {phase: p3, register: authoring_decisions, key: Compile the cases stated beside each check}
    status: CRITICAL
    gap_register_entry: GAP-04
    notes: The configuration is regenerated.
  dependency_graph:
  - from: ai_licensing
    to: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    dependency_type: amended transform
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The license check}
  - from: ai_licensing
    to: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
    dependency_type: amended transform
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The training check}
  - from: ai_licensing
    to: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    dependency_type: amended transform
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The inactivity check}
  - from: ai_licensing
    to: ai_governance::STRUCTURE_BUILD_AI_GOVERNANCE_CONFIG_V0
    dependency_type: generated structure
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The build configuration}
  constraint_register:
  - number: '1'
    constraint: What each check decides, and every act that uses them, is unchanged.
    source_finding: {phase: p1, register: constraints, row: 1}
    source: The business author
  gap_register:
  - gap_code: GAP-01
    source_finding: {phase: p3, register: authoring_decisions, key: Prove the license check}
    capability: Prove the license check
    owner_subdomain: ai_licensing
    resolution: EXTEND
  - gap_code: GAP-02
    source_finding: {phase: p3, register: authoring_decisions, key: Prove the training check}
    capability: Prove the training check
    owner_subdomain: ai_licensing
    resolution: EXTEND
  - gap_code: GAP-03
    source_finding: {phase: p3, register: authoring_decisions, key: Prove the inactivity check}
    capability: Prove the inactivity check
    owner_subdomain: ai_licensing
    resolution: EXTEND
  - gap_code: GAP-04
    source_finding: {phase: p3, register: authoring_decisions, key: Compile the cases stated beside each check}
    capability: Compile the cases stated beside each check
    owner_subdomain: ai_licensing
    resolution: EXTEND
  design_decisions:
  - number: '1'
    decision: Each check is stated whole, as it stands, with its cases.
    source_finding: {phase: p3, register: analysis_findings, key: Q1}
    rationale: A case belongs to a transform the design names.
    constraints_imposed: No check changes what it decides.
  - number: '2'
    decision: A no case expects a refusal; a yes case keeps its answer.
    source_finding: {phase: p3, register: analysis_findings, key: Q2}
    rationale: The checks refuse, as the business decided.
    constraints_imposed: Every no case is a VIOLATION case.
  - number: '3'
    decision: The earlier values stay, under this system's names, with one boundary case added.
    source_finding: {phase: p3, register: analysis_findings, key: Q4}
    rationale: The author answered both.
    constraints_imposed: Nothing beyond the earlier cases and the boundary.
  - number: '4'
    decision: The build configuration is reached through its generator.
    source_finding: {phase: p3, register: analysis_findings, key: Q5}
    rationale: It is derived from the design.
    constraints_imposed: No hand edit.
  authoring_scope:
  - capability: Prove the license check
    gap_register_ref: GAP-01
  - capability: Prove the training check
    gap_register_ref: GAP-02
  - capability: Prove the inactivity check
    gap_register_ref: GAP-03
  - capability: Compile the cases stated beside each check
    gap_register_ref: GAP-04
```

Consolidation of Stages 1–3. Every capability committed at Stage 3 appears here with the status its
decision implies. Nothing is re-litigated and nothing new is decided.

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
