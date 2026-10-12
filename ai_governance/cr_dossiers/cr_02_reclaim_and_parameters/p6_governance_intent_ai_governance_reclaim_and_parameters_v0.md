# Stage 6 — Governance Intent: ai_governance / reclaim and parameter result

## Machine

```yaml
document:
  phase: p6
  domain: ai_governance
  subdomain:
  - reclaim
  - parameter result
  cr: cr_02_reclaim_and_parameters
  rule_set: transformation.schemas.REGISTER_SCHEMA_P6_V0
registers:
  ownership:
  - capability: End a reclaim the registry refuses
    owner_subdomain: ai_licensing
    disposition: OWNED
    existing_artifact: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
    source_finding: {phase: p5, register: scope_boundary, key: End a reclaim the registry refuses}
  - capability: Tell a refused removal apart from a license still in use
    owner_subdomain: ai_licensing, in a later change
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Tell a refused removal apart from a license still in use}
  - capability: Check an action's parameters
    owner_subdomain: agent_governance
    disposition: OWNED
    existing_artifact: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0
    source_finding: {phase: p5, register: scope_boundary, key: Check an action's parameters}
  storage_governance:
  - storage_need: A durable record of which employee holds which license
    purpose: Unchanged; a refused removal from it now ends the reclaim
    subdomain: ai_licensing
    source_finding: {phase: p5, register: business_objects, key: License registry}
  cross_subdomain_deps:
  - dependency: Keeping the license registry
    direction: ai_licensing -> platform
    existing_artifact: capability_side_effects::CS_REGISTRY_V0
    status: SATISFIED
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_side_effects::CS_REGISTRY_V0'}
  - dependency: Checking against rules
    direction: agent_governance -> capability_transforms
    existing_artifact: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    status: SATISFIED
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0'}
  - dependency: Looking up a tool's rules
    direction: agent_governance -> capability_transforms
    existing_artifact: capability_transforms::CT_PURE_LOOKUP_V0
    status: SATISFIED
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_transforms::CT_PURE_LOOKUP_V0'}
  pps_artifacts_requiring_action:
  - fqdn: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
    current_status: Present; its removal step does not answer a refused removal; published in v5
    action: REPLACE
    source_finding: {phase: p4, register: design_decisions, row: 4}
  - fqdn: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    current_status: Present and reused unchanged
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0'}
  - fqdn: ai_governance::WF_AUTO_RECLAIM_V0
    current_status: Present; already routes VIOLATION to still active; runs the reclaim being replaced
    action: REVIEW
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - fqdn: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0
    current_status: Present; reports a result it never receives; published in v5
    action: REPLACE
    source_finding: {phase: p4, register: design_decisions, row: 4}
  - fqdn: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    current_status: Present; runs the parameter check being replaced
    action: REVIEW
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - fqdn: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    current_status: Present and reused unchanged
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0'}
  - fqdn: capability_transforms::CT_PURE_LOOKUP_V0
    current_status: Present and reused unchanged
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_transforms::CT_PURE_LOOKUP_V0'}
  boundary_rules:
  - rule_name: A_STEP_ANSWERS_FOR_ITS_STORE
    statement: The removal step answers every outcome the registry declares, and ends the contract on each.
    source_finding: {phase: p4, register: design_decisions, row: 1}
  - rule_name: A_LICENSE_NOT_RELEASED_IS_STILL_ACTIVE
    statement: A reclaim the registry refused ends as still active.
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - rule_name: REPORT_ONLY_WHAT_IS_RECEIVED
    statement: A check's declared result is read from what the check underneath returns.
    source_finding: {phase: p4, register: design_decisions, row: 3}
  - rule_name: RE_POINT_THE_RUNNER
    statement: The reclaim act and the governed action run the next versions; nothing else about them changes.
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - rule_name: A_PUBLISHED_ACT_IS_REPLACED_NOT_AMENDED
    statement: An act whose meaning changes is stated under its next version; the published version is stood down unchanged.
    source_finding: {phase: p4, register: design_decisions, row: 4}
  governance_outcome:
  - capability: End a reclaim the registry refuses
    owner_subdomain: ai_licensing
    source_finding: {phase: p6, register: ownership, key: End a reclaim the registry refuses}
  - capability: Check an action's parameters
    owner_subdomain: agent_governance
    source_finding: {phase: p6, register: ownership, key: Check an action's parameters}
```

Placement of rules. Nothing moves and nothing is added: the reclaim belongs to AI Licensing.

---

## 1. Ownership

---

## 2. Storage Governance

---

## 3. Cross-Subdomain Dependencies

---

## 4. PPS Artifacts Requiring Action

---

## 5. Governance Boundary Rules

---

## 6. Governance Outcome

---

## gov_projection — Governed Handoff to Stage 7

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | subdomain_purpose · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
| **Emits** → Stage 7 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
