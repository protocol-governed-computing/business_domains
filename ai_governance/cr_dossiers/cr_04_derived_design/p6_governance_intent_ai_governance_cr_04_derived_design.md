# Stage 6 — Governance Intent — ai_governance / ai_licensing, agent_governance

## Machine

```yaml
document:
  phase: p6
  domain: ai_governance
  subdomain:
  - ai_licensing
  - agent_governance
  cr: cr_04_derived_design
  rule_set: transformation.schemas.REGISTER_SCHEMA_P6_V0
registers:
  ownership:
  - capability: Register employee
    owner_subdomain: ai_licensing
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 1}
  - capability: Record training completed
    owner_subdomain: ai_licensing
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 2}
  - capability: Set license cap
    owner_subdomain: ai_licensing
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 3}
  - capability: Provision license
    owner_subdomain: ai_licensing
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 4}
  - capability: Record license usage
    owner_subdomain: ai_licensing
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 5}
  - capability: Reclaim license
    owner_subdomain: ai_licensing
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 6}
  - capability: Govern agent action
    owner_subdomain: agent_governance
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 7}
  - capability: Running the tool an agent proposes
    owner_subdomain: ai_licensing
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 8}
  - capability: Reclaiming several licenses in one request
    owner_subdomain: ai_licensing
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 9}
  - capability: Recording a denial with a reason of the caller's own
    owner_subdomain: ai_licensing
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 10}
  storage_governance:
  - storage_need: A durable employee record
    purpose: Licenses go only to employees the business has registered, and only once their training is recorded.
    subdomain: ai_licensing
    source_finding: {phase: p5, register: business_objects, row: 1}
  - storage_need: A durable employee identity registry
    purpose: Telling one employee from another needs a claim on its identity at the moment it is recorded.
    subdomain: ai_licensing
    source_finding: {phase: p5, register: business_objects, row: 2}
  - storage_need: A durable license cap record
    purpose: The business limits how many licenses may be assigned at once, across both tiers.
    subdomain: ai_licensing
    source_finding: {phase: p5, register: business_objects, row: 3}
  - storage_need: A durable license record
    purpose: The business keeps which employee holds which tier of license, when it was last used, and whether it was taken back.
    subdomain: ai_licensing
    source_finding: {phase: p5, register: business_objects, row: 4}
  - storage_need: A durable license identity registry
    purpose: Telling one license from another needs a claim on its identity at the moment it is recorded.
    subdomain: ai_licensing
    source_finding: {phase: p5, register: business_objects, row: 5}
  - storage_need: A durable action record
    purpose: The business keeps each action an agent was authorized to take, registered once however often it is proposed.
    subdomain: agent_governance
    source_finding: {phase: p5, register: business_objects, row: 6}
  - storage_need: A durable action identity registry
    purpose: Telling one action from another needs a claim on its identity at the moment it is recorded.
    subdomain: agent_governance
    source_finding: {phase: p5, register: business_objects, row: 7}
  - storage_need: A durable audit trail of ai_licensing
    purpose: Every operation must be traceable afterwards, and a trail that could be amended would not be evidence.
    subdomain: ai_licensing
    source_finding: {phase: p5, register: business_objects, row: 8}
  - storage_need: A durable audit trail of agent_governance
    purpose: Every operation must be traceable afterwards, and a trail that could be amended would not be evidence.
    subdomain: agent_governance
    source_finding: {phase: p5, register: business_objects, row: 9}
  cross_subdomain_deps:
  - dependency: Govern agent action reads the licenses ai_licensing keeps, and never writes them
    direction: agent_governance -> ai_licensing
    existing_artifact: ai_governance::RB_LICENSE_BINDINGS_V0
    status: SATISFIED
    source_finding: {phase: p5, register: actions, row: 7}
  pps_artifacts_requiring_action: []
  boundary_rules:
  - rule_name: AI_LICENSING_OWNS_ITS_RECORDS
    statement: Every record ai_licensing keeps is written only by ai_licensing's own operations.
    source_finding: {phase: p5, register: subdomain_purposes, row: 1}
  - rule_name: AGENT_GOVERNANCE_OWNS_ITS_RECORDS
    statement: Every record agent_governance keeps is written only by agent_governance's own operations.
    source_finding: {phase: p5, register: subdomain_purposes, row: 2}
  - rule_name: AGENT_GOVERNANCE_READS_AI_LICENSING_NEVER_WRITES
    statement: Govern agent action reads what ai_licensing keeps and leaves it exactly as it was, including when it is refused.
    source_finding: {phase: p5, register: actions, row: 7}
  governance_outcome:
  - capability: Register employee
    owner_subdomain: ai_licensing
    source_finding: {phase: p6, register: ownership, key: Register employee}
  - capability: Record training completed
    owner_subdomain: ai_licensing
    source_finding: {phase: p6, register: ownership, key: Record training completed}
  - capability: Set license cap
    owner_subdomain: ai_licensing
    source_finding: {phase: p6, register: ownership, key: Set license cap}
  - capability: Provision license
    owner_subdomain: ai_licensing
    source_finding: {phase: p6, register: ownership, key: Provision license}
  - capability: Record license usage
    owner_subdomain: ai_licensing
    source_finding: {phase: p6, register: ownership, key: Record license usage}
  - capability: Reclaim license
    owner_subdomain: ai_licensing
    source_finding: {phase: p6, register: ownership, key: Reclaim license}
  - capability: Govern agent action
    owner_subdomain: agent_governance
    source_finding: {phase: p6, register: ownership, key: Govern agent action}
```

Projected from the business intent. Every row cites the business-intent row it places.

---

## 1. Subdomain Boundary — Ownership

---

## 2. Storage Governance Requirements

---

## 3. Cross-Subdomain Dependency Declaration

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
| **Consumes** ← Stage 5 | boundary_rules · cross_subdomain_deps · governance_outcome · ownership · pps_artifacts_requiring_action · storage_governance |
| **Emits** → Stage 7 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
