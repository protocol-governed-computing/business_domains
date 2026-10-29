# Stage 1 — Change Request: Clarification & Fact Capture: ai_governance / ai_licensing, agent_governance

## Machine

```yaml
document:
  phase: p1
  domain: ai_governance
  subdomain:
  - ai_licensing
  - agent_governance
  cr: cr_04_derived_design
  rule_set: transformation.schemas.REGISTER_SCHEMA_P1_V0
registers:
  cr_type:
  - subdomain: ai_licensing
    classification: MODIFY
    rationale: AI licensing grants employees licenses for AI tools within the cap the business sets, and takes back the ones nobody uses.
    source_finding: {phase: p0, register: cr_type, row: 1}
  - subdomain: agent_governance
    classification: MODIFY
    rationale: Agent governance judges every action an AI agent proposes on a person's behalf, before any tool runs, and audits every judgment.
    source_finding: {phase: p0, register: cr_type, row: 2}
  business_vocabulary:
  - term: Employee
    definition: Licenses go only to employees the business has registered, and only once their training is recorded.
    source_finding: {phase: p0, register: business_vocabulary, row: 1}
  - term: License cap
    definition: The business limits how many licenses may be assigned at once, across both tiers.
    source_finding: {phase: p0, register: business_vocabulary, row: 2}
  - term: License
    definition: The business keeps which employee holds which tier of license, when it was last used, and whether it was taken back.
    source_finding: {phase: p0, register: business_vocabulary, row: 3}
  - term: Action
    definition: The business keeps each action an agent was authorized to take, registered once however often it is proposed.
    source_finding: {phase: p0, register: business_vocabulary, row: 4}
  requested_outcomes:
  - outcome: 'Register employee: records a new employee.'
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - outcome: 'Record training completed: changes an employee''s training completed.'
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - outcome: 'Set license cap: records a new license cap.'
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  - outcome: 'Provision license: records a new license.'
    source_finding: {phase: p0, register: requested_outcomes, row: 4}
  - outcome: 'Record license usage: changes a license''s last used at.'
    source_finding: {phase: p0, register: requested_outcomes, row: 5}
  - outcome: 'Reclaim license: moves a license from active to reclaimed.'
    source_finding: {phase: p0, register: requested_outcomes, row: 6}
  - outcome: 'Govern agent action: records a new action.'
    source_finding: {phase: p0, register: requested_outcomes, row: 7}
  known_facts:
  - fact: An employee is identified by its employee id.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 1}
  - fact: There is one license cap.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 2}
  - fact: A license is identified by its employee id.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 3}
  - fact: An action is identified by its tool name, requesting user id and domain context.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 4}
  system_beliefs:
  - belief: The current ai_licensing design names the records, entrances and requests its callers use today.
    why_it_matters: The derived design keeps those names, so a caller meets no change the ledger did not decide.
    verification_goal: Read the ai_licensing baseline design and find there each name the derived design carries.
    source_finding: {phase: p0, register: system_beliefs, row: 1}
  - belief: The current agent_governance design names the records, entrances and requests its callers use today.
    why_it_matters: The derived design keeps those names, so a caller meets no change the ledger did not decide.
    verification_goal: Read the agent_governance baseline design and find there each name the derived design carries.
    source_finding: {phase: p0, register: system_beliefs, row: 2}
  assumptions: []
  constraints: []
  business_invariants:
  - invariant: No two employees share their employee id.
    source_finding: {phase: p0, register: business_invariants, row: 1}
  - invariant: No two licenses share their employee id, until reclaim license frees it.
    source_finding: {phase: p0, register: business_invariants, row: 2}
  - invariant: No two actions share their tool name, requesting user id and domain context.
    source_finding: {phase: p0, register: business_invariants, row: 3}
  - invariant: Every ai_licensing operation records employee id, license id, tier and reason on the ai_licensing trail, and no entry is changed or removed.
    source_finding: {phase: p0, register: business_invariants, row: 4}
  - invariant: Every agent_governance operation records tool name, requesting user id and reason on the agent_governance trail, and no entry is changed or removed.
    source_finding: {phase: p0, register: business_invariants, row: 5}
  lifecycle_states:
  - object: license
    state: active
    meaning: A license is active after provision license.
    source_finding: {phase: p0, register: lifecycle_states, row: 1}
  - object: license
    state: reclaimed
    meaning: A license is reclaimed after reclaim license.
    source_finding: {phase: p0, register: lifecycle_states, row: 2}
  business_events:
  - event: Employee registered
    when_it_occurs: When register employee completes
    significance: Others learn that register employee completed without reading the ai_licensing records.
    source_finding: {phase: p0, register: business_events, row: 1}
  - event: Training completed
    when_it_occurs: When record training completed completes
    significance: Others learn that record training completed completed without reading the ai_licensing records.
    source_finding: {phase: p0, register: business_events, row: 2}
  - event: License cap set
    when_it_occurs: When set license cap completes
    significance: Others learn that set license cap completed without reading the ai_licensing records.
    source_finding: {phase: p0, register: business_events, row: 3}
  - event: License provisioned
    when_it_occurs: When provision license completes
    significance: Others learn that provision license completed without reading the ai_licensing records.
    source_finding: {phase: p0, register: business_events, row: 4}
  - event: Usage recorded
    when_it_occurs: When record license usage completes
    significance: Others learn that record license usage completed without reading the ai_licensing records.
    source_finding: {phase: p0, register: business_events, row: 5}
  - event: License revoked
    when_it_occurs: When reclaim license completes
    significance: Others learn that reclaim license completed without reading the ai_licensing records.
    source_finding: {phase: p0, register: business_events, row: 6}
  - event: Agent action authorized
    when_it_occurs: When govern agent action completes
    significance: Others learn that govern agent action completed without reading the agent_governance records.
    source_finding: {phase: p0, register: business_events, row: 7}
  authority_boundaries:
  - business_object: employee
    authoritative_owner: ai_licensing
    source_finding: {phase: p0, register: authority_boundaries, row: 1}
  - business_object: license cap
    authoritative_owner: ai_licensing
    source_finding: {phase: p0, register: authority_boundaries, row: 2}
  - business_object: license
    authoritative_owner: ai_licensing
    source_finding: {phase: p0, register: authority_boundaries, row: 3}
  - business_object: action
    authoritative_owner: agent_governance
    source_finding: {phase: p0, register: authority_boundaries, row: 4}
  out_of_scope:
  - item: Running the tool an agent proposes
    reason: Agent governance judges an action before any tool runs; running it is not the business's act here.
    source_finding: {phase: p0, register: out_of_scope, row: 1}
  - item: Reclaiming several licenses in one request
    reason: The system asks to reclaim one license at a time.
    source_finding: {phase: p0, register: out_of_scope, row: 2}
  - item: Recording a denial with a reason of the caller's own
    reason: A denial carries the reason the failed check gives, and nobody else's.
    source_finding: {phase: p0, register: out_of_scope, row: 3}
  governance_scope:
  - scope_item: ai_licensing
    relationship: MODIFIED
    source_finding: {phase: p0, register: governance_scope, row: 1}
  - scope_item: agent_governance
    relationship: MODIFIED
    source_finding: {phase: p0, register: governance_scope, row: 2}
  clarification_requests: []
  acceptance_criteria:
  - criterion: Register employee is refused when an employee that is the same is already recorded.
    source_finding: {phase: p0, register: acceptance_criteria, row: 1}
  - criterion: Record training completed is refused when the employee is not recorded.
    source_finding: {phase: p0, register: acceptance_criteria, row: 2}
  - criterion: Provision license is refused when a license that is the same is already recorded.
    source_finding: {phase: p0, register: acceptance_criteria, row: 3}
  - criterion: Provision license is refused when training completed does not hold.
    source_finding: {phase: p0, register: acceptance_criteria, row: 4}
  - criterion: Provision license is refused when tier admitted does not hold.
    source_finding: {phase: p0, register: acceptance_criteria, row: 5}
  - criterion: Provision license is refused when cap set does not hold.
    source_finding: {phase: p0, register: acceptance_criteria, row: 6}
  - criterion: Provision license is refused when under the cap does not hold.
    source_finding: {phase: p0, register: acceptance_criteria, row: 7}
  - criterion: Record license usage is refused when the license is not recorded.
    source_finding: {phase: p0, register: acceptance_criteria, row: 8}
  - criterion: Reclaim license is refused when the license is not recorded.
    source_finding: {phase: p0, register: acceptance_criteria, row: 9}
  - criterion: Reclaim license is refused when the license is not active.
    source_finding: {phase: p0, register: acceptance_criteria, row: 10}
  - criterion: Govern agent action is refused when tool declared does not hold.
    source_finding: {phase: p0, register: acceptance_criteria, row: 11}
  - criterion: Govern agent action is refused when license active does not hold.
    source_finding: {phase: p0, register: acceptance_criteria, row: 12}
  - criterion: Govern agent action is refused when tier grants tool does not hold.
    source_finding: {phase: p0, register: acceptance_criteria, row: 13}
  - criterion: Govern agent action is refused when parameters satisfy rules does not hold.
    source_finding: {phase: p0, register: acceptance_criteria, row: 14}
  identity_and_sameness:
  - business_object: employee
    identified_by: employee id
    two_are_the_same_when: they carry the same employee id
    source_finding: {phase: p0, register: identity_and_sameness, row: 1}
  - business_object: license cap
    identified_by: one
    two_are_the_same_when: There is one license cap
    source_finding: {phase: p0, register: identity_and_sameness, row: 2}
  - business_object: license
    identified_by: employee id
    two_are_the_same_when: they carry the same employee id
    source_finding: {phase: p0, register: identity_and_sameness, row: 3}
  - business_object: action
    identified_by: tool name, requesting user id and domain context
    two_are_the_same_when: they carry the same tool name, requesting user id and domain context
    source_finding: {phase: p0, register: identity_and_sameness, row: 4}
  lifecycle_transitions:
  - object: license
    from_state: active
    to_state: reclaimed
    triggered_by: reclaim license
    cascade: None
    source_finding: {phase: p0, register: lifecycle_transitions, row: 1}
  operation_refusals:
  - operation: register employee
    refused_when: an employee that is the same is already recorded
    business_reason: Two employees that are the same would describe one employee twice.
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: record training completed
    refused_when: the employee is not recorded
    business_reason: There is no employee to act on.
    source_finding: {phase: p0, register: operation_refusals, row: 2}
  - operation: provision license
    refused_when: a license that is the same is already recorded
    business_reason: Two licenses that are the same would describe one license twice.
    source_finding: {phase: p0, register: operation_refusals, row: 3}
  - operation: provision license
    refused_when: training completed does not hold
    business_reason: The business requires training completed before it acts.
    source_finding: {phase: p0, register: operation_refusals, row: 4}
  - operation: provision license
    refused_when: tier admitted does not hold
    business_reason: The business requires tier admitted before it acts.
    source_finding: {phase: p0, register: operation_refusals, row: 5}
  - operation: provision license
    refused_when: cap set does not hold
    business_reason: The business requires cap set before it acts.
    source_finding: {phase: p0, register: operation_refusals, row: 6}
  - operation: provision license
    refused_when: under the cap does not hold
    business_reason: The business requires under the cap before it acts.
    source_finding: {phase: p0, register: operation_refusals, row: 7}
  - operation: record license usage
    refused_when: the license is not recorded
    business_reason: There is no license to act on.
    source_finding: {phase: p0, register: operation_refusals, row: 8}
  - operation: reclaim license
    refused_when: the license is not recorded
    business_reason: There is no license to act on.
    source_finding: {phase: p0, register: operation_refusals, row: 9}
  - operation: reclaim license
    refused_when: the license is not active
    business_reason: Only an active license becomes reclaimed.
    source_finding: {phase: p0, register: operation_refusals, row: 10}
  - operation: govern agent action
    refused_when: tool declared does not hold
    business_reason: The business requires tool declared before it acts.
    source_finding: {phase: p0, register: operation_refusals, row: 11}
  - operation: govern agent action
    refused_when: license active does not hold
    business_reason: The business requires license active before it acts.
    source_finding: {phase: p0, register: operation_refusals, row: 12}
  - operation: govern agent action
    refused_when: tier grants tool does not hold
    business_reason: The business requires tier grants tool before it acts.
    source_finding: {phase: p0, register: operation_refusals, row: 13}
  - operation: govern agent action
    refused_when: parameters satisfy rules does not hold
    business_reason: The business requires parameters satisfy rules before it acts.
    source_finding: {phase: p0, register: operation_refusals, row: 14}
  authority_deferrals: []
```

Projected from the change seed. Every row is the seed's own, cited to the section it was
said in. S1 interrogates and does not author: a question raised by restating the seed
amends the seed and is projected again, so no row here states business content the seed
does not.

---

## 1. CR Type

---

## 2. Business Vocabulary

---

## 3. Requested Outcomes

---

## 4. Known Facts — Business Truths

---

## 5. Existing-System Beliefs — Requiring Verification

---

## 6. Assumptions

---

## 7. Constraints

---

## 8. Business Invariants

---

## 9. Lifecycle States

---

## 10. Business Events

---

## 11. Authority Boundaries

---

## 12. Out of Scope

---

## 13. Governance Scope

---

## 14. Clarification Requests

---

## 15. Acceptance Criteria

---

## 16. Identity and Sameness

---

## 17. Lifecycle Transitions

---

## 18. Operation Refusals

---

## 19. Authority Deferrals

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
