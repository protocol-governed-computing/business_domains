# Change Seed — ai_governance / ai_licensing, agent_governance

## Machine

```yaml
document:
  phase: p0
  domain: ai_governance
  subdomain:
  - ai_licensing
  - agent_governance
  cr: cr_05_refused_release_still_active
  rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0
registers:
  subdomain_purpose: The business governs its AI licensing and the AI agents acting for its people. AI licensing grants employees licenses for AI tools and takes back the ones nobody uses. Agent governance judges every action an AI agent proposes on a person's behalf, before any tool runs.
  cr_type:
  - subdomain: ai_licensing
    classification: MODIFY
    rationale: AI licensing grants employees licenses for AI tools within the cap the business sets, and takes back the ones nobody uses.
  - subdomain: agent_governance
    classification: MODIFY
    rationale: Agent governance judges every action an AI agent proposes on a person's behalf, before any tool runs, and audits every judgment.
  business_vocabulary:
  - term: Employee
    definition: Licenses go only to employees the business has registered, and only once their training is recorded.
  - term: License cap
    definition: The business limits how many licenses may be assigned at once, across both tiers.
  - term: License
    definition: The business keeps which employee holds which tier of license, when it was last used, and whether it was taken back.
  - term: Action
    definition: The business keeps each action an agent was authorized to take, registered once however often it is proposed.
  requested_outcomes:
  - outcome: 'Register employee: records a new employee.'
  - outcome: 'Record training completed: changes an employee''s training completed.'
  - outcome: 'Set license cap: records a new license cap.'
  - outcome: 'Provision license: records a new license.'
  - outcome: 'Record license usage: changes a license''s last used at.'
  - outcome: 'Reclaim license: moves a license from active to reclaimed.'
  - outcome: 'Govern agent action: records a new action.'
  known_facts:
  - fact: An employee is identified by its employee id.
    certainty: HIGH
  - fact: There is one license cap.
    certainty: HIGH
  - fact: A license is identified by its employee id.
    certainty: HIGH
  - fact: An action is identified by its tool name, requesting user id and domain context.
    certainty: HIGH
  system_beliefs:
  - belief: The current ai_licensing design names the records, entrances and requests its callers use today.
    why_it_matters: The derived design keeps those names, so a caller meets no change the ledger did not decide.
    verification_goal: Read the ai_licensing baseline design and find there each name the derived design carries.
  - belief: The current agent_governance design names the records, entrances and requests its callers use today.
    why_it_matters: The derived design keeps those names, so a caller meets no change the ledger did not decide.
    verification_goal: Read the agent_governance baseline design and find there each name the derived design carries.
  assumptions: []
  constraints: []
  business_invariants:
  - invariant: No two employees share their employee id.
  - invariant: No two licenses share their employee id, until reclaim license frees it.
  - invariant: No two actions share their tool name, requesting user id and domain context.
  - invariant: Every ai_licensing operation records employee id, license id, tier and reason on the ai_licensing trail, and no entry is changed or removed.
  - invariant: Every agent_governance operation records tool name, requesting user id and reason on the agent_governance trail, and no entry is changed or removed.
  lifecycle_states:
  - object: license
    state: active
    meaning: A license is active after provision license.
  - object: license
    state: reclaimed
    meaning: A license is reclaimed after reclaim license.
  business_events:
  - event: Employee registered
    when_it_occurs: When register employee completes
    significance: Others learn that register employee completed without reading the ai_licensing records.
  - event: Training completed
    when_it_occurs: When record training completed completes
    significance: Others learn that record training completed completed without reading the ai_licensing records.
  - event: License cap set
    when_it_occurs: When set license cap completes
    significance: Others learn that set license cap completed without reading the ai_licensing records.
  - event: License provisioned
    when_it_occurs: When provision license completes
    significance: Others learn that provision license completed without reading the ai_licensing records.
  - event: Usage recorded
    when_it_occurs: When record license usage completes
    significance: Others learn that record license usage completed without reading the ai_licensing records.
  - event: License revoked
    when_it_occurs: When reclaim license completes
    significance: Others learn that reclaim license completed without reading the ai_licensing records.
  - event: Agent action authorized
    when_it_occurs: When govern agent action completes
    significance: Others learn that govern agent action completed without reading the agent_governance records.
  authority_boundaries:
  - business_object: employee
    authoritative_owner: ai_licensing
  - business_object: license cap
    authoritative_owner: ai_licensing
  - business_object: license
    authoritative_owner: ai_licensing
  - business_object: action
    authoritative_owner: agent_governance
  out_of_scope:
  - item: Running the tool an agent proposes
    reason: Agent governance judges an action before any tool runs; running it is not the business's act here.
  - item: Reclaiming several licenses in one request
    reason: The system asks to reclaim one license at a time.
  - item: Recording a denial with a reason of the caller's own
    reason: A denial carries the reason the failed check gives, and nobody else's.
  governance_scope:
  - scope_item: ai_licensing
    relationship: MODIFIED
  - scope_item: agent_governance
    relationship: MODIFIED
  clarification_requests: []
  acceptance_criteria:
  - criterion: Register employee is refused when an employee that is the same is already recorded.
  - criterion: Record training completed is refused when the employee is not recorded.
  - criterion: Provision license is refused when a license that is the same is already recorded.
  - criterion: Provision license is refused when training completed does not hold.
  - criterion: Provision license is refused when tier admitted does not hold.
  - criterion: Provision license is refused when cap set does not hold.
  - criterion: Provision license is refused when under the cap does not hold.
  - criterion: Record license usage is refused when the license is not recorded.
  - criterion: Reclaim license is refused when the license is not recorded.
  - criterion: Reclaim license is refused when the license is not active.
  - criterion: Govern agent action is refused when tool declared does not hold.
  - criterion: Govern agent action is refused when license active does not hold.
  - criterion: Govern agent action is refused when tier grants tool does not hold.
  - criterion: Govern agent action is refused when parameters satisfy rules does not hold.
  identity_and_sameness:
  - business_object: employee
    identified_by: employee id
    two_are_the_same_when: they carry the same employee id
  - business_object: license cap
    identified_by: one
    two_are_the_same_when: There is one license cap
  - business_object: license
    identified_by: employee id
    two_are_the_same_when: they carry the same employee id
  - business_object: action
    identified_by: tool name, requesting user id and domain context
    two_are_the_same_when: they carry the same tool name, requesting user id and domain context
  lifecycle_transitions:
  - object: license
    from_state: active
    to_state: reclaimed
    triggered_by: reclaim license
    cascade: None
  operation_refusals:
  - operation: register employee
    refused_when: an employee that is the same is already recorded
    business_reason: Two employees that are the same would describe one employee twice.
  - operation: record training completed
    refused_when: the employee is not recorded
    business_reason: There is no employee to act on.
  - operation: provision license
    refused_when: a license that is the same is already recorded
    business_reason: Two licenses that are the same would describe one license twice.
  - operation: provision license
    refused_when: training completed does not hold
    business_reason: The business requires training completed before it acts.
  - operation: provision license
    refused_when: tier admitted does not hold
    business_reason: The business requires tier admitted before it acts.
  - operation: provision license
    refused_when: cap set does not hold
    business_reason: The business requires cap set before it acts.
  - operation: provision license
    refused_when: under the cap does not hold
    business_reason: The business requires under the cap before it acts.
  - operation: record license usage
    refused_when: the license is not recorded
    business_reason: There is no license to act on.
  - operation: reclaim license
    refused_when: the license is not recorded
    business_reason: There is no license to act on.
  - operation: reclaim license
    refused_when: the license is not active
    business_reason: Only an active license becomes reclaimed.
  - operation: govern agent action
    refused_when: tool declared does not hold
    business_reason: The business requires tool declared before it acts.
  - operation: govern agent action
    refused_when: license active does not hold
    business_reason: The business requires license active before it acts.
  - operation: govern agent action
    refused_when: tier grants tool does not hold
    business_reason: The business requires tier grants tool before it acts.
  - operation: govern agent action
    refused_when: parameters satisfy rules does not hold
    business_reason: The business requires parameters satisfy rules before it acts.
  authority_deferrals: []
```

Projected from the decision ledger. Business prose (the purpose, each vocabulary definition, what is out of scope) is the ledger's own, word for word; every other row is said from the ledger's structure and claims nothing it does not state.

---

## 0. Subdomain Purpose

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

## gov_projection — Governed Handoff to Stage 1

| Direction | Fields |
|-----------|--------|
| **Consumes** ← the decision ledger | the owner's answers |
| **Emits** → Stage 1 | subdomain_purpose · cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
