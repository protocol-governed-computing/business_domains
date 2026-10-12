# Stage 4 — Business Model: ai_governance / reclaim and parameter result

## Machine

```yaml
document:
  phase: p4
  domain: ai_governance
  subdomain:
  - reclaim
  - parameter result
  cr: cr_02_reclaim_and_parameters
  rule_set: transformation.schemas.REGISTER_SCHEMA_P4_V0
registers:
  actors:
  - actor: The business
    role: Reclaims licenses on its schedule. Unchanged by this change.
    authority_class: Owning business
    source_finding: {phase: p2, register: business_processes, row: 1}
  - actor: An agent
    role: Proposes an action. Unchanged by this change.
    authority_class: Ordinary participant
    source_finding: {phase: p2, register: business_processes, row: 2}
  - actor: AI Licensing
    role: Ends a reclaim the registry refuses, with the license still assigned.
    authority_class: Owning subdomain
    source_finding: {phase: p3, register: placement_decision, key: ai_licensing}
  - actor: Agent Governance
    role: Checks an agent's action against the rules declared for its tool.
    authority_class: Owning subdomain
    source_finding: {phase: p3, register: placement_decision, key: agent_governance}
  bm_entities:
  - entity: The Assignment
    description: A license held by an employee.
    store_model: One registry, unchanged.
    source_finding: {phase: p2, register: entities, row: 1}
  - entity: The Reclaim
    description: Taking back an unused license.
    store_model: An act, announced when it removes an assignment.
    source_finding: {phase: p2, register: entities, row: 2}
  - entity: The Governed Action
    description: An agent's proposed action, judged and recorded.
    store_model: Recorded in the governance audit.
    source_finding: {phase: p2, register: entities, row: 3}
  - entity: The Parameter Check
    description: The step that checks an action's parameters.
    store_model: Run by the governed action.
    source_finding: {phase: p2, register: entities, row: 4}
  resources: []
  events:
  - event: NONE IDENTIFIED
    trigger: This change recognises no new moment.
    lifecycle_meaning: A revocation is not announced for a refused removal.
    source_finding: {phase: p1, register: business_events, row: 1}
  relationships:
  - subject: AI Licensing
    verb: ends
    object: a reclaim the registry refuses
    capability_need: End a reclaim the registry refuses
    source_finding: {phase: p3, register: authoring_decisions, key: End a reclaim the registry refuses}
  - subject: Agent Governance
    verb: checks
    object: an action's parameters
    capability_need: Check an action's parameters
    source_finding: {phase: p3, register: authoring_decisions, key: Check an action's parameters}
  capability_graph:
  - capability: End a reclaim the registry refuses
    source_finding: {phase: p3, register: authoring_decisions, key: End a reclaim the registry refuses}
    status: CRITICAL
    gap_register_entry: GAP-01
    notes: A next version of the reclaim, whose removal step ends the contract on a refused removal.
  - capability: Check an action's parameters
    source_finding: {phase: p3, register: authoring_decisions, key: Check an action's parameters}
    status: CRITICAL
    gap_register_entry: GAP-02
    notes: A next version that reports what it receives.
  dependency_graph:
  - from: ai_licensing
    to: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
    dependency_type: contract replaced by its next version
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Reclaiming a license}
  - from: ai_licensing
    to: capability_side_effects::CS_REGISTRY_V0
    dependency_type: platform capability
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The license registry}
  - from: ai_licensing
    to: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    dependency_type: capability transform
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The inactivity check}
  - from: ai_licensing
    to: ai_governance::WF_AUTO_RECLAIM_V0
    dependency_type: workflow, re-pointed
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The reclaim act}
  - from: agent_governance
    to: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0
    dependency_type: contract replaced by its next version
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The parameter check}
  - from: agent_governance
    to: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    dependency_type: transform
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Checking against rules}
  - from: agent_governance
    to: capability_transforms::CT_PURE_LOOKUP_V0
    dependency_type: transform
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Looking up a tool's rules}
  - from: agent_governance
    to: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    dependency_type: workflow, re-pointed
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Governing an action}
  constraint_register:
  - number: '1'
    constraint: Every reclaim the registry does not refuse ends exactly as it did before this change.
    source_finding: {phase: p1, register: constraints, row: 1}
    source: The business author
  - number: '2'
    constraint: No ending is added.
    source_finding: {phase: p1, register: constraints, row: 2}
    source: The business author
  - number: '3'
    constraint: The governed action decides exactly as it does today.
    source_finding: {phase: p1, register: constraints, row: 3}
    source: The business author
  - number: '4'
    constraint: No published identity changes what it says, except to be stood down.
    source_finding: {phase: p1, register: constraints, row: 4}
    source: The business author
  gap_register:
  - gap_code: GAP-01
    source_finding: {phase: p3, register: authoring_decisions, key: End a reclaim the registry refuses}
    capability: End a reclaim the registry refuses
    owner_subdomain: ai_licensing
    resolution: AUTHOR_NEW
  - gap_code: GAP-02
    source_finding: {phase: p3, register: authoring_decisions, key: Check an action's parameters}
    capability: Check an action's parameters
    owner_subdomain: agent_governance
    resolution: AUTHOR_NEW
  design_decisions:
  - number: '1'
    decision: The removal step ends the contract on a refused removal.
    source_finding: {phase: p3, register: analysis_findings, key: Q1}
    rationale: A reclaim must not carry on past a removal the registry refused.
    constraints_imposed: The removal step answers every outcome the registry declares.
  - number: '2'
    decision: A refused removal ends as still active.
    source_finding: {phase: p3, register: analysis_findings, key: Q2}
    rationale: The license stays assigned, which is what that ending says.
    constraints_imposed: No route and no ending changes.
  - number: '3'
    decision: The new parameter check reports whether every declared rule passed, from the check's own answer.
    source_finding: {phase: p3, register: analysis_findings, key: Q4}
    rationale: A check reports only what it receives.
    constraints_imposed: Its steps, rules and routes are those of the old check.
  - number: '4'
    decision: Each of the two contracts is stated under a next version, and its published version is stood down unchanged.
    source_finding: {phase: p3, register: analysis_findings, key: Q5}
    rationale: A change of meaning is a new identity, and identity is fixed at publication.
    constraints_imposed: The published declaration gains only its stand-down.
  - number: '5'
    decision: The reclaim act and the governed action are re-pointed to the next versions.
    source_finding: {phase: p3, register: analysis_findings, key: Q6}
    rationale: Each decides exactly as today.
    constraints_imposed: Only the contract each one's place runs changes.
  authoring_scope:
  - capability: End a reclaim the registry refuses
    gap_register_ref: GAP-01
  - capability: Check an action's parameters
    gap_register_ref: GAP-02
```

Consolidation of Stages 1–3. Nothing is re-litigated and nothing new is decided.

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
