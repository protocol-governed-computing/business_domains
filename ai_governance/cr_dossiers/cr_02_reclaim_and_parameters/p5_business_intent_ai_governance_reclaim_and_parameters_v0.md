# Stage 5 — Business Intent: ai_governance / reclaim and parameter result

## Machine

```yaml
document:
  phase: p5
  domain: ai_governance
  subdomain:
  - reclaim
  - parameter result
  cr: cr_02_reclaim_and_parameters
  rule_set: transformation.schemas.REGISTER_SCHEMA_P5_V0
registers:
  subdomain_purpose: |2

    The AI Licensing subdomain governs the business's licenses for AI tools: provisioning a license to an
    employee, and reclaiming a license that has gone unused for the business's threshold of days. The
    Agent Governance subdomain governs what an AI agent may do on the business's behalf: it judges an
    agent's proposed action, checks its parameters against the rules declared for the tool, and records
    every action it authorizes or denies. This change decides what a reclaim does when the registry
    refuses it and what the parameter check reports, and states each act it changes under a new identity.
  purpose_provenance:
  - source: CR seed §0 Subdomain Purpose
    disposition: INHERITED
    refinement: ''
  subdomain_purposes:
  - subdomain: ai_licensing
    purpose: Governs the business's AI tool licenses, and ends a reclaim the registry refuses with the license still assigned.
    source_finding: {phase: p4, register: actors, key: AI Licensing}
  - subdomain: agent_governance
    purpose: Checks an agent's action against the rules declared for its tool, and reports only what its checks receive.
    source_finding: {phase: p4, register: actors, key: Agent Governance}
  scope_boundary:
  - capability: End a reclaim the registry refuses
    status: IN_SCOPE
    notes: A next version of the reclaim, whose removal step ends the contract on a refused removal.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-01}
  - capability: Check an action's parameters
    status: IN_SCOPE
    notes: A next version of the parameter check.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-02}
  - capability: Tell a refused removal apart from a license still in use
    status: DEFERRED
    notes: Both leave the license assigned.
    source_finding: {phase: p4, register: authoring_scope, key: Tell a refused removal apart from a license still in use}
  business_objects:
  - store_name: License registry
    record_model: IDENTITY_REGISTRY
    business_rationale: Unchanged, and named because a refused removal from it now ends the reclaim.
    source_finding: {phase: p4, register: bm_entities, key: The Assignment}
  identity_semantics:
  - store_name: License registry
    identity_field: Employee
    source: Named by the reclaim request
    uniqueness_rule: One assignment per employee; unchanged by this change.
    cross_subdomain_relationship: None
    source_finding: {phase: p4, register: bm_entities, key: The Assignment}
  invariants:
  - invariant: No reclaim carries on past a removal the registry refused.
    business_reason: A step after a refused removal would act on an assignment still held.
    source_finding: {phase: p1, register: business_invariants, row: 1}
  - invariant: No license is reported reclaimed that the registry did not release.
    business_reason: A revocation announced for a license still held is false.
    source_finding: {phase: p1, register: business_invariants, row: 2}
  - invariant: A check reports only what it receives.
    business_reason: A reported result nobody received is no result.
    source_finding: {phase: p1, register: business_invariants, row: 3}
  - invariant: A published identity means what it meant when it was published.
    business_reason: A citation of v5 relies on what v5 said.
    source_finding: {phase: p1, register: business_invariants, row: 4}
  actions:
  - action: End
    object: A reclaim the registry refuses
    trigger: The registry refuses the removal
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: End a reclaim the registry refuses}
  - action: Check
    object: An action's parameters
    trigger: An agent proposes an action
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Check an action's parameters}
  provisional_codes:
  - subdomain: ai_licensing
    provisional_code: CC_RECLAIM_UNUSED_LICENSE_V1
    family: CC
    summary: Reclaim license from inactive user.
    source_finding: {phase: p4, register: design_decisions, row: 4}
  - subdomain: agent_governance
    provisional_code: CC_VALIDATE_TOOL_PARAMETERS_V1
    family: CC
    summary: Enforce declared parameter constraints for an authorized tool, reporting whether every rule passed.
    source_finding: {phase: p4, register: design_decisions, row: 4}
  cross_subdomain_refs: []
```

---

## 1. Subdomain Purpose

---

## 2. Scope Boundary

---

## 3. Business Objects

---

## 4. Identity Semantics

---

## 5. Invariants

---

## 6. Actions

---

## 7. Provisional Codes

---

## 8. Cross-Subdomain References

---

## gov_projection — Governed Handoff to Stage 6

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 4 | actors · bm_entities · events · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
| **Emits** → Stage 6 | subdomain_purpose · purpose_provenance · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
