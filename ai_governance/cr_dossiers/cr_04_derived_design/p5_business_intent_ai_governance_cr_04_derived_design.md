# Stage 5 — Business Intent — ai_governance / ai_licensing, agent_governance

## Machine

```yaml
document:
  phase: p5
  domain: ai_governance
  subdomain:
  - ai_licensing
  - agent_governance
  cr: cr_04_derived_design
  rule_set: transformation.schemas.REGISTER_SCHEMA_P5_V0
registers:
  subdomain_purpose: The business governs its AI licensing and the AI agents acting for its people. AI licensing grants employees licenses for AI tools and takes back the ones nobody uses. Agent governance judges every action an AI agent proposes on a person's behalf, before any tool runs.
  purpose_provenance:
  - source: Change seed §0 Subdomain Purpose
    disposition: INHERITED
    refinement: null
  subdomain_purposes:
  - subdomain: ai_licensing
    purpose: AI licensing grants employees licenses for AI tools within the cap the business sets, and takes back the ones nobody uses.
    source_finding: {phase: p0, register: cr_type, row: 1}
  - subdomain: agent_governance
    purpose: Agent governance judges every action an AI agent proposes on a person's behalf, before any tool runs, and audits every judgment.
    source_finding: {phase: p0, register: cr_type, row: 2}
  scope_boundary:
  - capability: Register employee
    status: IN_SCOPE
    notes: Records a new employee
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - capability: Record training completed
    status: IN_SCOPE
    notes: Changes an employee's training completed
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - capability: Set license cap
    status: IN_SCOPE
    notes: Records a new license cap
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  - capability: Provision license
    status: IN_SCOPE
    notes: Records a new license
    source_finding: {phase: p0, register: requested_outcomes, row: 4}
  - capability: Record license usage
    status: IN_SCOPE
    notes: Changes a license's last used at
    source_finding: {phase: p0, register: requested_outcomes, row: 5}
  - capability: Reclaim license
    status: IN_SCOPE
    notes: Moves a license from active to reclaimed
    source_finding: {phase: p0, register: requested_outcomes, row: 6}
  - capability: Govern agent action
    status: IN_SCOPE
    notes: Records a new action
    source_finding: {phase: p0, register: requested_outcomes, row: 7}
  - capability: Running the tool an agent proposes
    status: DEFERRED
    notes: Agent governance judges an action before any tool runs; running it is not the business's act here.
    source_finding: {phase: p0, register: out_of_scope, row: 1}
  - capability: Reclaiming several licenses in one request
    status: DEFERRED
    notes: The system asks to reclaim one license at a time.
    source_finding: {phase: p0, register: out_of_scope, row: 2}
  - capability: Recording a denial with a reason of the caller's own
    status: DEFERRED
    notes: A denial carries the reason the failed check gives, and nobody else's.
    source_finding: {phase: p0, register: out_of_scope, row: 3}
  business_objects:
  - store_name: Employee record
    record_model: MUTABLE_STATE
    business_rationale: Licenses go only to employees the business has registered, and only once their training is recorded.
    source_finding: {phase: p0, register: business_vocabulary, row: 1}
  - store_name: Employee identity registry
    record_model: IDENTITY_REGISTRY
    business_rationale: Telling one employee from another needs a claim on its identity at the moment it is recorded.
    source_finding: {phase: p0, register: identity_and_sameness, row: 1}
  - store_name: License cap record
    record_model: MUTABLE_STATE
    business_rationale: The business limits how many licenses may be assigned at once, across both tiers.
    source_finding: {phase: p0, register: business_vocabulary, row: 2}
  - store_name: License record
    record_model: MUTABLE_STATE
    business_rationale: The business keeps which employee holds which tier of license, when it was last used, and whether it was taken back.
    source_finding: {phase: p0, register: business_vocabulary, row: 3}
  - store_name: License identity registry
    record_model: IDENTITY_REGISTRY
    business_rationale: Telling one license from another needs a claim on its identity at the moment it is recorded.
    source_finding: {phase: p0, register: identity_and_sameness, row: 3}
  - store_name: Action record
    record_model: MUTABLE_STATE
    business_rationale: The business keeps each action an agent was authorized to take, registered once however often it is proposed.
    source_finding: {phase: p0, register: business_vocabulary, row: 4}
  - store_name: Action identity registry
    record_model: IDENTITY_REGISTRY
    business_rationale: Telling one action from another needs a claim on its identity at the moment it is recorded.
    source_finding: {phase: p0, register: identity_and_sameness, row: 4}
  - store_name: Audit trail of ai_licensing
    record_model: APPEND_ONLY_JOURNAL
    business_rationale: Every operation must be traceable afterwards, and a trail that could be amended would not be evidence.
    source_finding: {phase: p0, register: business_invariants, row: 4}
  - store_name: Audit trail of agent_governance
    record_model: APPEND_ONLY_JOURNAL
    business_rationale: Every operation must be traceable afterwards, and a trail that could be amended would not be evidence.
    source_finding: {phase: p0, register: business_invariants, row: 5}
  identity_semantics:
  - store_name: Employee record
    identity_field: Employee id
    source: Supplied with the request
    uniqueness_rule: Two employees are the same when they carry the same employee id.
    cross_subdomain_relationship: None
    source_finding: {phase: p0, register: identity_and_sameness, row: 1}
  - store_name: License cap record
    identity_field: One
    source: Formed by the business
    uniqueness_rule: There is one license cap.
    cross_subdomain_relationship: None
    source_finding: {phase: p0, register: identity_and_sameness, row: 2}
  - store_name: License record
    identity_field: Employee id
    source: Formed by the business
    uniqueness_rule: Two licenses are the same when they carry the same employee id, until reclaim license frees it.
    cross_subdomain_relationship: None
    source_finding: {phase: p0, register: identity_and_sameness, row: 3}
  - store_name: Action record
    identity_field: Tool name, requesting user id and domain context
    source: Formed by the business
    uniqueness_rule: Two actions are the same when they carry the same tool name, requesting user id and domain context.
    cross_subdomain_relationship: None
    source_finding: {phase: p0, register: identity_and_sameness, row: 4}
  invariants:
  - invariant: No two employees share their employee id.
    business_reason: Two employees that are the same would describe one employee twice.
    source_finding: {phase: p0, register: business_invariants, row: 1}
  - invariant: No two licenses share their employee id, until reclaim license frees it.
    business_reason: Two licenses that are the same would describe one license twice.
    source_finding: {phase: p0, register: business_invariants, row: 2}
  - invariant: No two actions share their tool name, requesting user id and domain context.
    business_reason: Two actions that are the same would describe one action twice.
    source_finding: {phase: p0, register: business_invariants, row: 3}
  - invariant: Every ai_licensing operation records employee id, license id, tier and reason on the ai_licensing trail, and no entry is changed or removed.
    business_reason: Every operation must be traceable afterwards, and a trail that could be amended would not be evidence.
    source_finding: {phase: p0, register: business_invariants, row: 4}
  - invariant: Every agent_governance operation records tool name, requesting user id and reason on the agent_governance trail, and no entry is changed or removed.
    business_reason: Every operation must be traceable afterwards, and a trail that could be amended would not be evidence.
    source_finding: {phase: p0, register: business_invariants, row: 5}
  actions:
  - action: Register employee
    object: employee
    trigger: Requested by the system
    status: IN_SCOPE
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - action: Record training completed
    object: employee
    trigger: Requested by the system
    status: IN_SCOPE
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - action: Set license cap
    object: license cap
    trigger: Requested by the system
    status: IN_SCOPE
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  - action: Provision license
    object: license
    trigger: Requested by the employee
    status: IN_SCOPE
    source_finding: {phase: p0, register: requested_outcomes, row: 4}
  - action: Record license usage
    object: license
    trigger: Requested by the employee
    status: IN_SCOPE
    source_finding: {phase: p0, register: requested_outcomes, row: 5}
  - action: Reclaim license
    object: license
    trigger: Requested by the system
    status: IN_SCOPE
    source_finding: {phase: p0, register: requested_outcomes, row: 6}
  - action: Govern agent action
    object: action
    trigger: Requested by the agent
    status: IN_SCOPE
    source_finding: {phase: p0, register: requested_outcomes, row: 7}
  provisional_codes:
  - subdomain: ai_licensing
    provisional_code: WF_REGISTER_EMPLOYEE_V0
    family: WF
    summary: Records a new employee
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - subdomain: ai_licensing
    provisional_code: WF_RECORD_TRAINING_COMPLETED_V0
    family: WF
    summary: Changes an employee's training completed
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - subdomain: ai_licensing
    provisional_code: WF_SET_LICENSE_CAP_V0
    family: WF
    summary: Records a new license cap
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  - subdomain: ai_licensing
    provisional_code: WF_PROVISION_LICENSE_V0
    family: WF
    summary: Records a new license
    source_finding: {phase: p0, register: requested_outcomes, row: 4}
  - subdomain: ai_licensing
    provisional_code: WF_RECORD_LICENSE_USAGE_V0
    family: WF
    summary: Changes a license's last used at
    source_finding: {phase: p0, register: requested_outcomes, row: 5}
  - subdomain: ai_licensing
    provisional_code: WF_RECLAIM_LICENSE_V0
    family: WF
    summary: Moves a license from active to reclaimed
    source_finding: {phase: p0, register: requested_outcomes, row: 6}
  - subdomain: agent_governance
    provisional_code: WF_GOVERN_AGENT_ACTION_V0
    family: WF
    summary: Records a new action
    source_finding: {phase: p0, register: requested_outcomes, row: 7}
  cross_subdomain_refs: []
```

Projected from the change seed, which is projected from the decision ledger. Every row cites the seed row it restates.

---

## 1. Subdomain Purpose

---

## 2. Scope Boundary

---

## 3. Business Objects

---

## 4. Identity Semantics

---

## 5. Business Invariants

---

## 6. Business Actions

---

## 7. Provisional Artifact Codes

---

## 8. Cross-Subdomain References

---

## gov_projection — Governed Handoff to Stage 6

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Change seed | actions · business_objects · cross_subdomain_refs · identity_semantics · invariants · provisional_codes · purpose_provenance · scope_boundary · subdomain_purpose · subdomain_purposes |
| **Emits** → Stage 6 | subdomain_purpose · purpose_provenance · subdomain_purposes · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
