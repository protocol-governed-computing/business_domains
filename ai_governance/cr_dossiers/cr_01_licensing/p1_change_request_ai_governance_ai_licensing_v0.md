# Stage 1 — Change Request: Clarification & Fact Capture: ai_governance / ai_licensing

## Machine

```yaml
document:
  phase: p1
  domain: ai_governance
  subdomain: ai_licensing
  cr: cr_01_licensing
  rule_set: transformation.schemas.REGISTER_SCHEMA_P1_V0
registers:
  cr_type:
  - subdomain: ai_licensing
    classification: MODIFY
    rationale: The three checks are built and run. Nothing proves them; cases are stated beside each so that every build proves it. What each check decides does not change.
    source_finding: {phase: p0, register: cr_type, row: 1}
  business_vocabulary:
  - term: Check
    definition: 'One of the three decisions: whether a license is available, whether an employee is eligible, whether a license is inactive.'
    source_finding: {phase: p0, register: business_vocabulary, row: 1}
  - term: Case
    definition: What a check is given, and what it must answer or that it must refuse.
    source_finding: {phase: p0, register: business_vocabulary, row: 2}
  - term: Cap
    definition: The number of licenses the business allows to be assigned.
    source_finding: {phase: p0, register: business_vocabulary, row: 3}
  - term: Threshold
    definition: The number of days a license may go unused before it is reclaimed.
    source_finding: {phase: p0, register: business_vocabulary, row: 4}
  requested_outcomes:
  - outcome: 'Beside each of the three checks are the cases that prove it: a case it admits, with what it answers, and a case it refuses.'
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - outcome: The cases are the ones the business already had, restated to expect a refusal where the answer is no, and to use this system's names.
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - outcome: What each check decides, and every act that uses them, is unchanged.
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  known_facts:
  - fact: A check whose answer is no refuses.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 1}
  - fact: A license is available while fewer are assigned than the cap. At the cap, none is.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 2}
  - fact: An employee is eligible once their required training is complete.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 3}
  - fact: A license is inactive once it has gone unused for the threshold of days or more.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 4}
  - fact: The earlier cases expect a no answer where this system refuses.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 5}
  - fact: The earlier cases' no case becomes a refusal case, and the yes case keeps its answer.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 6}
  - fact: The earlier cases keep their values under this system's names.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 7}
  - fact: A license unused for exactly the threshold is inactive, and is proven as a case.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 8}
  system_beliefs:
  - belief: None of the three checks is proven.
    why_it_matters: A check nothing proves can change what it decides without anyone seeing.
    verification_goal: Establish whether each check carries cases that every build runs.
    source_finding: {phase: p0, register: system_beliefs, row: 1}
  - belief: Each check refuses when its answer is no.
    why_it_matters: The cases must expect what the check does.
    verification_goal: Establish what each check does with a no answer.
    source_finding: {phase: p0, register: system_beliefs, row: 2}
  - belief: The earlier cases name the inactivity check's evaluation date and the training check's answer differently from this system.
    why_it_matters: A case naming what a check does not take or give proves nothing.
    verification_goal: Establish the names each check takes and gives.
    source_finding: {phase: p0, register: system_beliefs, row: 3}
  assumptions: []
  constraints:
  - constraint: What each check decides, and every act that uses them, is unchanged.
    source: Business author
    source_finding: {phase: p0, register: constraints, row: 1}
  business_invariants:
  - invariant: No check answers no; a no is a refusal.
    source_finding: {phase: p0, register: business_invariants, row: 1}
  - invariant: Every check is proven on every build by the cases stated beside it.
    source_finding: {phase: p0, register: business_invariants, row: 2}
  lifecycle_states:
  - object: Check
    state: Proven
    meaning: Its cases are stated beside it and hold on every build.
    source_finding: {phase: p0, register: lifecycle_states, row: 1}
  - object: Check
    state: Unproven
    meaning: Nothing states what it must answer. This change ends that state for all three.
    source_finding: {phase: p0, register: lifecycle_states, row: 2}
  business_events:
  - event: NONE IDENTIFIED
    when_it_occurs: ''
    significance: This change announces nothing new.
    source_finding: {phase: p0, register: business_events, row: 1}
  authority_boundaries:
  - business_object: The three checks and their cases
    authoritative_owner: AI Licensing
    source_finding: {phase: p0, register: authority_boundaries, row: 1}
  - business_object: The cap, the training required and the threshold
    authoritative_owner: The acts that use the checks
    source_finding: {phase: p0, register: authority_boundaries, row: 2}
  out_of_scope:
  - item: The cap, the training required and the threshold
    reason: Each is stated by the act that uses the check, and none changes.
    source_finding: {phase: p0, register: out_of_scope, row: 1}
  - item: The agent_governance subdomain
    reason: Not this change.
    source_finding: {phase: p0, register: out_of_scope, row: 2}
  governance_scope:
  - scope_item: ai_licensing
    relationship: MODIFIED
    source_finding: {phase: p0, register: governance_scope, row: 1}
  - scope_item: agent_governance
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 2}
  clarification_requests: []
  acceptance_criteria:
  - criterion: Each of the three checks is proven on every build.
    source_finding: {phase: p0, register: acceptance_criteria, row: 1}
  - criterion: A license check with fewer assigned than the cap answers that one is available, with how many remain; at the cap it refuses.
    source_finding: {phase: p0, register: acceptance_criteria, row: 2}
  - criterion: A training check for an employee with training complete answers that they are eligible; without it, it refuses.
    source_finding: {phase: p0, register: acceptance_criteria, row: 3}
  - criterion: An inactivity check for a license unused for the threshold or more answers that it is inactive, with how many days; for one used more recently, it refuses.
    source_finding: {phase: p0, register: acceptance_criteria, row: 4}
  - criterion: Every act that uses the checks behaves as it did before this change.
    source_finding: {phase: p0, register: acceptance_criteria, row: 5}
  identity_and_sameness: []
  lifecycle_transitions:
  - object: Check
    from_state: Unproven
    to_state: Proven
    triggered_by: Its cases being stated beside it
    cascade: None.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 1}
  operation_refusals: []
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
