# Stage 1 — Change Request: Clarification & Fact Capture: ai_governance / reclaim and parameter result

## Machine

```yaml
document:
  phase: p1
  domain: ai_governance
  subdomain:
  - reclaim
  - parameter result
  cr: cr_02_reclaim_and_parameters
  rule_set: transformation.schemas.REGISTER_SCHEMA_P1_V0
registers:
  cr_type:
  - subdomain: ai_licensing
    classification: MODIFY
    rationale: A reclaim does not say what happens when the license registry refuses to remove an assignment. Nothing is added to what a reclaim does.
    source_finding: {phase: p0, register: cr_type, row: 1}
  - subdomain: agent_governance
    classification: MODIFY
    rationale: The parameter check reports a result it never receives.
    source_finding: {phase: p0, register: cr_type, row: 2}
  business_vocabulary:
  - term: Reclaim
    definition: Taking back a license that has gone unused for the business's threshold of days.
    source_finding: {phase: p0, register: business_vocabulary, row: 1}
  - term: Assignment
    definition: The registry's record that a license belongs to an employee.
    source_finding: {phase: p0, register: business_vocabulary, row: 2}
  - term: Refused removal
    definition: The registry's answer to a malformed request to remove an assignment.
    source_finding: {phase: p0, register: business_vocabulary, row: 3}
  - term: Governed action
    definition: An agent's proposed action, judged and recorded by the business.
    source_finding: {phase: p0, register: business_vocabulary, row: 4}
  - term: Parameter check
    definition: The step that checks an action's parameters against the rules declared for its tool.
    source_finding: {phase: p0, register: business_vocabulary, row: 5}
  - term: Parameter result
    definition: 'What the parameter check reports: whether every declared rule passed.'
    source_finding: {phase: p0, register: business_vocabulary, row: 6}
  - term: Published
    definition: Sealed into a composition that was released and cited.
    source_finding: {phase: p0, register: business_vocabulary, row: 7}
  - term: Successor
    definition: The new identity that states what an act does after this change.
    source_finding: {phase: p0, register: business_vocabulary, row: 8}
  - term: Stood down
    definition: Replaced by a declared successor, kept in the record and out of reach.
    source_finding: {phase: p0, register: business_vocabulary, row: 9}
  requested_outcomes:
  - outcome: A reclaim the registry refuses ends with the license left assigned.
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - outcome: The parameter check reports whether every declared rule passed.
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - outcome: Each act whose meaning this changes has a successor, and its published identity is stood down unchanged.
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  - outcome: Everything in force that runs a stood-down act runs its successor.
    source_finding: {phase: p0, register: requested_outcomes, row: 4}
  - outcome: Every other reclaim, and every governed action, decides as it does today.
    source_finding: {phase: p0, register: requested_outcomes, row: 5}
  known_facts:
  - fact: A reclaim ends as reclaimed, still active, or in error.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 1}
  - fact: A license the registry did not release stays with the employee.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 2}
  - fact: A reclaim the registry refused ends as still active.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 3}
  - fact: A parameter that breaks a declared rule denies the action.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 4}
  - fact: The check underneath answers only whether every rule passed; a broken rule denies the action.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 5}
  - fact: Nothing reads the parameter result today.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 6}
  - fact: Identity is fixed at publication; a change of meaning is a new identity.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 7}
  - fact: A published identity stays in the record, stood down, when a successor replaces it.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 8}
  - fact: A re-point changes which act a referrer runs, and nothing else about it.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 9}
  system_beliefs:
  - belief: The step that removes an assignment does not answer a refused removal.
    why_it_matters: An unanswered refusal is carried past.
    verification_goal: Establish which answers of the registry the removal step answers.
    source_finding: {phase: p0, register: system_beliefs, row: 1}
  - belief: The reclaim already ends as still active for a license that is not inactive.
    why_it_matters: A refused removal can end there without a new ending.
    verification_goal: Establish where the reclaim sends its still-active answer.
    source_finding: {phase: p0, register: system_beliefs, row: 2}
  - belief: The parameter check reads its result from a place the check underneath never writes.
    why_it_matters: The reported result is always empty.
    verification_goal: Establish what the check underneath returns and what the parameter check reads.
    source_finding: {phase: p0, register: system_beliefs, row: 3}
  - belief: Both acts this change touches were published in v5.
    why_it_matters: Each one it changes needs a successor.
    verification_goal: Establish which touched acts the v5 composition holds.
    source_finding: {phase: p0, register: system_beliefs, row: 4}
  - belief: One workflow runs each of the two contracts.
    why_it_matters: Everything that runs a replaced contract must run its successor.
    verification_goal: Establish everything that names each contract, by full name and by short code.
    source_finding: {phase: p0, register: system_beliefs, row: 5}
  assumptions: []
  constraints:
  - constraint: Every reclaim the registry does not refuse ends exactly as it did before this change.
    source: Business author
    source_finding: {phase: p0, register: constraints, row: 1}
  - constraint: No ending is added.
    source: Business author
    source_finding: {phase: p0, register: constraints, row: 2}
  - constraint: The governed action decides exactly as it does today.
    source: Business author
    source_finding: {phase: p0, register: constraints, row: 3}
  - constraint: No published identity changes what it says, except to be stood down.
    source: Business author — identity is fixed at publication.
    source_finding: {phase: p0, register: constraints, row: 4}
  business_invariants:
  - invariant: No reclaim carries on past a removal the registry refused.
    source_finding: {phase: p0, register: business_invariants, row: 1}
  - invariant: No license is reported reclaimed that the registry did not release.
    source_finding: {phase: p0, register: business_invariants, row: 2}
  - invariant: A check reports only what it receives.
    source_finding: {phase: p0, register: business_invariants, row: 3}
  - invariant: A published identity means what it meant when it was published.
    source_finding: {phase: p0, register: business_invariants, row: 4}
  lifecycle_states:
  - object: License
    state: Assigned
    meaning: Held by an employee. Unchanged by this change.
    source_finding: {phase: p0, register: lifecycle_states, row: 1}
  - object: License
    state: Reclaimed
    meaning: Taken back after going unused. Unchanged by this change.
    source_finding: {phase: p0, register: lifecycle_states, row: 2}
  - object: Published act
    state: In force
    meaning: Run when a request reaches it.
    source_finding: {phase: p0, register: lifecycle_states, row: 3}
  - object: Published act
    state: Stood down
    meaning: Replaced by its successor, kept in the record as published.
    source_finding: {phase: p0, register: lifecycle_states, row: 4}
  business_events:
  - event: A license was revoked
    when_it_occurs: When a reclaim removes an assignment
    significance: Unchanged; it is not announced when the registry refuses the removal.
    source_finding: {phase: p0, register: business_events, row: 1}
  authority_boundaries:
  - business_object: What a reclaim does when the registry refuses it
    authoritative_owner: AI Licensing
    source_finding: {phase: p0, register: authority_boundaries, row: 1}
  - business_object: The rules declared for each tool
    authoritative_owner: Agent Governance
    source_finding: {phase: p0, register: authority_boundaries, row: 2}
  - business_object: What the check underneath answers
    authoritative_owner: The platform
    source_finding: {phase: p0, register: authority_boundaries, row: 3}
  out_of_scope:
  - item: Telling a refused removal apart from a license still in use
    reason: The business keeps three endings; both leave the license assigned.
    source_finding: {phase: p0, register: out_of_scope, row: 1}
  - item: Provisioning a license
    reason: Not this change.
    source_finding: {phase: p0, register: out_of_scope, row: 2}
  - item: Which rules each tool declares
    reason: Unchanged.
    source_finding: {phase: p0, register: out_of_scope, row: 3}
  - item: Reporting which rule failed
    reason: The check underneath denies rather than returns it.
    source_finding: {phase: p0, register: out_of_scope, row: 4}
  - item: The licence-cap check nothing runs
    reason: It stays as v5 published it.
    source_finding: {phase: p0, register: out_of_scope, row: 5}
  governance_scope:
  - scope_item: ai_licensing
    relationship: MODIFIED
    source_finding: {phase: p0, register: governance_scope, row: 1}
  - scope_item: agent_governance
    relationship: MODIFIED
    source_finding: {phase: p0, register: governance_scope, row: 2}
  clarification_requests: []
  acceptance_criteria:
  - criterion: A reclaim the registry refuses ends as still active, the license stays assigned, and no revocation is announced.
    source_finding: {phase: p0, register: acceptance_criteria, row: 1}
  - criterion: Every reclaim the registry does not refuse ends exactly as it did before this change.
    source_finding: {phase: p0, register: acceptance_criteria, row: 2}
  - criterion: An action whose parameters satisfy every rule is authorized, and the parameter result says every rule passed.
    source_finding: {phase: p0, register: acceptance_criteria, row: 3}
  - criterion: An action whose parameters break a rule is denied and audited, as today.
    source_finding: {phase: p0, register: acceptance_criteria, row: 4}
  - criterion: Each act whose meaning this changes is stated under a new identity, and the published identity is unchanged except for its stand-down.
    source_finding: {phase: p0, register: acceptance_criteria, row: 5}
  - criterion: Nothing in force runs a stood-down act.
    source_finding: {phase: p0, register: acceptance_criteria, row: 6}
  identity_and_sameness:
  - business_object: Act
    identified_by: Its identity
    two_are_the_same_when: Its declaration means what the published declaration meant
    source_finding: {phase: p0, register: identity_and_sameness, row: 1}
  lifecycle_transitions:
  - object: Published act
    from_state: In force
    to_state: Stood down
    triggered_by: This change adds its successor
    cascade: Whatever runs it is re-pointed
    source_finding: {phase: p0, register: lifecycle_transitions, row: 1}
  operation_refusals:
  - operation: Reclaiming a license
    refused_when: The registry refuses to remove the assignment
    business_reason: A license the registry did not release stays with the employee.
    source_finding: {phase: p0, register: operation_refusals, row: 1}
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
