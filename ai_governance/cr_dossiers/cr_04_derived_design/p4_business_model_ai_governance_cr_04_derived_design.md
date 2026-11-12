# Stage 4 — Business Model — ai_governance / ai_licensing, agent_governance

## Machine

```yaml
document:
  phase: p4
  domain: ai_governance
  subdomain:
  - ai_licensing
  - agent_governance
  cr: cr_04_derived_design
  rule_set: transformation.schemas.REGISTER_SCHEMA_P4_V0
registers:
  actors:
  - actor: Employee
    role: Requests provision license and record license usage
    authority_class: Operator
    source_finding: {phase: p2, register: business_processes, row: 4}
  - actor: System
    role: Requests register employee, record training completed, set license cap and reclaim license
    authority_class: System
    source_finding: {phase: p2, register: business_processes, row: 1}
  - actor: Agent
    role: Requests govern agent action
    authority_class: Agent
    source_finding: {phase: p2, register: business_processes, row: 7}
  bm_entities:
  - entity: Employee
    description: Licenses go only to employees the business has registered, and only once their training is recorded.
    store_model: One durable record per employee, addressed by its employee id, updated in place.
    source_finding: {phase: p2, register: entities, row: 1}
  - entity: License cap
    description: The business limits how many licenses may be assigned at once, across both tiers.
    store_model: One durable record of the license cap.
    source_finding: {phase: p2, register: entities, row: 2}
  - entity: License
    description: The business keeps which employee holds which tier of license, when it was last used, and whether it was taken back.
    store_model: One durable record per license, addressed by its employee id, updated in place, carrying its own state (active and reclaimed).
    source_finding: {phase: p2, register: entities, row: 3}
  - entity: Action
    description: The business keeps each action an agent was authorized to take, registered once however often it is proposed.
    store_model: One durable record per action, addressed by its tool name, requesting user id and domain context.
    source_finding: {phase: p2, register: entities, row: 4}
  resources:
  - resource: Employees records
    description: Licenses go only to employees the business has registered, and only once their training is recorded.
    source_finding: {phase: p2, register: entities, row: 1}
  - resource: License caps records
    description: The business limits how many licenses may be assigned at once, across both tiers.
    source_finding: {phase: p2, register: entities, row: 2}
  - resource: Licenses records
    description: The business keeps which employee holds which tier of license, when it was last used, and whether it was taken back.
    source_finding: {phase: p2, register: entities, row: 3}
  - resource: Actions records
    description: The business keeps each action an agent was authorized to take, registered once however often it is proposed.
    source_finding: {phase: p2, register: entities, row: 4}
  events:
  - event: Employee registered
    trigger: When register employee completes
    lifecycle_meaning: Others learn that register employee completed without reading the ai_licensing records.
    source_finding: {phase: p1, register: business_events, row: 1}
  - event: Training completed
    trigger: When record training completed completes
    lifecycle_meaning: Others learn that record training completed completed without reading the ai_licensing records.
    source_finding: {phase: p1, register: business_events, row: 2}
  - event: License cap set
    trigger: When set license cap completes
    lifecycle_meaning: Others learn that set license cap completed without reading the ai_licensing records.
    source_finding: {phase: p1, register: business_events, row: 3}
  - event: License provisioned
    trigger: When provision license completes
    lifecycle_meaning: Others learn that provision license completed without reading the ai_licensing records.
    source_finding: {phase: p1, register: business_events, row: 4}
  - event: Usage recorded
    trigger: When record license usage completes
    lifecycle_meaning: Others learn that record license usage completed without reading the ai_licensing records.
    source_finding: {phase: p1, register: business_events, row: 5}
  - event: License revoked
    trigger: When reclaim license completes
    lifecycle_meaning: Others learn that reclaim license completed without reading the ai_licensing records.
    source_finding: {phase: p1, register: business_events, row: 6}
  - event: Agent action authorized
    trigger: When govern agent action completes
    lifecycle_meaning: Others learn that govern agent action completed without reading the agent_governance records.
    source_finding: {phase: p1, register: business_events, row: 7}
  relationships:
  - subject: Employee
    verb: is identified by
    object: Employee id
    capability_need: Tell one employee from another when it is recorded
    source_finding: {phase: p1, register: identity_and_sameness, row: 1}
  - subject: License
    verb: is identified by
    object: Employee id
    capability_need: Tell one license from another when it is recorded
    source_finding: {phase: p1, register: identity_and_sameness, row: 3}
  - subject: Action
    verb: is identified by
    object: Tool name, requesting user id and domain context
    capability_need: Tell one action from another when it is recorded
    source_finding: {phase: p1, register: identity_and_sameness, row: 4}
  capability_graph:
  - capability: Appendonly jsonl side effect, as the platform declares it
    source_finding: {phase: p3, register: authoring_decisions, row: 1}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: Clock side effect, as the platform declares it
    source_finding: {phase: p3, register: authoring_decisions, row: 2}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: Mutable json side effect, as the platform declares it
    source_finding: {phase: p3, register: authoring_decisions, row: 3}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: Registry side effect, as the platform declares it
    source_finding: {phase: p3, register: authoring_decisions, row: 4}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: Assemble record transform, as the platform declares it
    source_finding: {phase: p3, register: authoring_decisions, row: 5}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: Generate id transform, as the platform declares it
    source_finding: {phase: p3, register: authoring_decisions, row: 6}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: Lookup transform, as the platform declares it
    source_finding: {phase: p3, register: authoring_decisions, row: 7}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: Validate parameter rules transform, as the platform declares it
    source_finding: {phase: p3, register: authoring_decisions, row: 8}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: Validate record structure transform, as the platform declares it
    source_finding: {phase: p3, register: authoring_decisions, row: 9}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: Validate set membership transform, as the platform declares it
    source_finding: {phase: p3, register: authoring_decisions, row: 10}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: The register employee workflow
    source_finding: {phase: p3, register: authoring_decisions, row: 11}
    status: CRITICAL
    gap_register_entry: GAP-01
    notes: No workflow in the composition does what the ledger decides for register employee.
  - capability: The record training completed workflow
    source_finding: {phase: p3, register: authoring_decisions, row: 12}
    status: CRITICAL
    gap_register_entry: GAP-02
    notes: No workflow in the composition does what the ledger decides for record training completed.
  - capability: The set license cap workflow
    source_finding: {phase: p3, register: authoring_decisions, row: 13}
    status: CRITICAL
    gap_register_entry: GAP-03
    notes: No workflow in the composition does what the ledger decides for set license cap.
  - capability: The provision license workflow
    source_finding: {phase: p3, register: authoring_decisions, row: 14}
    status: CRITICAL
    gap_register_entry: GAP-04
    notes: The workflow the composition holds for provision license means something other than the ledger decides, so its successor takes the next unused version.
  - capability: The record license usage workflow
    source_finding: {phase: p3, register: authoring_decisions, row: 15}
    status: CRITICAL
    gap_register_entry: GAP-05
    notes: No workflow in the composition does what the ledger decides for record license usage.
  - capability: The reclaim license workflow
    source_finding: {phase: p3, register: authoring_decisions, row: 16}
    status: CRITICAL
    gap_register_entry: GAP-06
    notes: The workflow the composition holds for reclaim license means something other than the ledger decides, so its successor takes the next unused version.
  - capability: The govern agent action workflow
    source_finding: {phase: p3, register: authoring_decisions, row: 17}
    status: CRITICAL
    gap_register_entry: GAP-07
    notes: The workflow the composition holds for govern agent action means something other than the ledger decides, so its successor takes the next unused version.
  gap_register:
  - gap_code: GAP-01
    source_finding: {phase: p3, register: authoring_decisions, row: 11}
    capability: The register employee workflow
    owner_subdomain: ai_licensing
    resolution: NEW
  - gap_code: GAP-02
    source_finding: {phase: p3, register: authoring_decisions, row: 12}
    capability: The record training completed workflow
    owner_subdomain: ai_licensing
    resolution: NEW
  - gap_code: GAP-03
    source_finding: {phase: p3, register: authoring_decisions, row: 13}
    capability: The set license cap workflow
    owner_subdomain: ai_licensing
    resolution: NEW
  - gap_code: GAP-04
    source_finding: {phase: p3, register: authoring_decisions, row: 14}
    capability: The provision license workflow
    owner_subdomain: ai_licensing
    resolution: EXTEND
  - gap_code: GAP-05
    source_finding: {phase: p3, register: authoring_decisions, row: 15}
    capability: The record license usage workflow
    owner_subdomain: ai_licensing
    resolution: NEW
  - gap_code: GAP-06
    source_finding: {phase: p3, register: authoring_decisions, row: 16}
    capability: The reclaim license workflow
    owner_subdomain: ai_licensing
    resolution: EXTEND
  - gap_code: GAP-07
    source_finding: {phase: p3, register: authoring_decisions, row: 17}
    capability: The govern agent action workflow
    owner_subdomain: agent_governance
    resolution: EXTEND
  authoring_scope:
  - capability: The register employee workflow
    gap_register_ref: GAP-01
  - capability: The record training completed workflow
    gap_register_ref: GAP-02
  - capability: The set license cap workflow
    gap_register_ref: GAP-03
  - capability: The provision license workflow
    gap_register_ref: GAP-04
  - capability: The record license usage workflow
    gap_register_ref: GAP-05
  - capability: The reclaim license workflow
    gap_register_ref: GAP-06
  - capability: The govern agent action workflow
    gap_register_ref: GAP-07
  dependency_graph:
  - from: ai_governance
    to: capability_side_effects::CS_APPENDONLY_JSONL_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 1}
  - from: ai_governance
    to: capability_side_effects::CS_CLOCK_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 2}
  - from: ai_governance
    to: capability_side_effects::CS_MUTABLE_JSON_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 3}
  - from: ai_governance
    to: capability_side_effects::CS_REGISTRY_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 4}
  - from: ai_governance
    to: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 5}
  - from: ai_governance
    to: capability_transforms::CT_PURE_GENERATE_ID_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 6}
  - from: ai_governance
    to: capability_transforms::CT_PURE_LOOKUP_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 7}
  - from: ai_governance
    to: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 8}
  - from: ai_governance
    to: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 9}
  - from: ai_governance
    to: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 10}
  constraint_register:
  - number: '1'
    constraint: No two employees share their employee id.
    source_finding: {phase: p1, register: business_invariants, row: 1}
    source: invariant
  - number: '2'
    constraint: No two licenses share their employee id, until reclaim license frees it.
    source_finding: {phase: p1, register: business_invariants, row: 2}
    source: invariant
  - number: '3'
    constraint: No two actions share their tool name, requesting user id and domain context.
    source_finding: {phase: p1, register: business_invariants, row: 3}
    source: invariant
  - number: '4'
    constraint: Every ai_licensing operation records employee id, license id, tier and reason on the ai_licensing trail, and no entry is changed or removed.
    source_finding: {phase: p1, register: business_invariants, row: 4}
    source: invariant
  - number: '5'
    constraint: Every agent_governance operation records tool name, requesting user id and reason on the agent_governance trail, and no entry is changed or removed.
    source_finding: {phase: p1, register: business_invariants, row: 5}
    source: invariant
  design_decisions:
  - number: '1'
    decision: ai_licensing stays the subdomain it is; the derived design extends it.
    source_finding: {phase: p3, register: placement_decision, row: 1}
    rationale: The composition already holds ai_licensing; the derived design keeps its binding and its entrances.
    constraints_imposed: The binding and entrances callers meet keep their names.
  - number: '2'
    decision: agent_governance stays the subdomain it is; the derived design extends it.
    source_finding: {phase: p3, register: placement_decision, row: 2}
    rationale: The composition already holds agent_governance; the derived design keeps its binding and its entrances.
    constraints_imposed: The binding and entrances callers meet keep their names.
  - number: '3'
    decision: Each artifact keeps its identity when its meaning is unchanged, and takes the next unused version when it changes.
    source_finding: {phase: p3, register: analysis_findings, row: 1}
    rationale: A caller relying on an identity relies on what it means.
    constraints_imposed: A caller dispatching by identity follows supersedes.
```

Projected from the analysis loop. Every row cites what it consolidates.

---

## 1. Discovery Summary

---

## 2. Capability Graph (capability_graph)

---

## 3. Dependency Graph (dependency_graph)

---

## 4. Constraint Register (constraint_register)

---

## 5. Gap Register (gap_register)

---

## 6. Design Decisions (design_decisions)

---

## 7. Authoring Scope (authoring_scope)

---

## gov_projection — Governed Handoff to Stage 5

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 3 | actors · authoring_scope · bm_entities · capability_graph · constraint_register · dependency_graph · design_decisions · events · gap_register · relationships · resources |
| **Emits** → Stage 5 | actors · bm_entities · resources · events · relationships · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
