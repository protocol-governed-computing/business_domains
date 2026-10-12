# Change Seed — ai_governance / ai_licensing

## Machine

```yaml
document:
  phase: p0
  domain: ai_governance
  subdomain: ai_licensing
  cr: cr_01_licensing
  rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0
registers:
  subdomain_purpose: |2

    The AI Licensing subdomain governs the business's licenses for AI tools: provisioning a license to an
    employee while licenses remain under the business's cap and once the employee has completed the
    required training, and reclaiming a license that has gone unused for the business's threshold of
    days. Each of its checks refuses when its answer is no. It does not govern what an agent may do,
    which employees exist, or which tools the business licenses.
  cr_type:
  - subdomain: ai_licensing
    classification: MODIFY
    rationale: The three checks are built and run. Nothing proves them; cases are stated beside each so that every build proves it. What each check decides does not change.
  business_vocabulary:
  - term: Check
    definition: 'One of the three decisions: whether a license is available, whether an employee is eligible, whether a license is inactive.'
  - term: Case
    definition: What a check is given, and what it must answer or that it must refuse.
  - term: Cap
    definition: The number of licenses the business allows to be assigned.
  - term: Threshold
    definition: The number of days a license may go unused before it is reclaimed.
  requested_outcomes:
  - outcome: 'Beside each of the three checks are the cases that prove it: a case it admits, with what it answers, and a case it refuses.'
  - outcome: The cases are the ones the business already had, restated to expect a refusal where the answer is no, and to use this system's names.
  - outcome: What each check decides, and every act that uses them, is unchanged.
  known_facts:
  - fact: A check whose answer is no refuses.
    certainty: HIGH
  - fact: A license is available while fewer are assigned than the cap. At the cap, none is.
    certainty: HIGH
  - fact: An employee is eligible once their required training is complete.
    certainty: HIGH
  - fact: A license is inactive once it has gone unused for the threshold of days or more.
    certainty: HIGH
  - fact: The earlier cases expect a no answer where this system refuses.
    certainty: HIGH
  - fact: The earlier cases' no case becomes a refusal case, and the yes case keeps its answer.
    certainty: HIGH
  - fact: The earlier cases keep their values under this system's names.
    certainty: HIGH
  - fact: A license unused for exactly the threshold is inactive, and is proven as a case.
    certainty: HIGH
  system_beliefs:
  - belief: None of the three checks is proven.
    why_it_matters: A check nothing proves can change what it decides without anyone seeing.
    verification_goal: Establish whether each check carries cases that every build runs.
  - belief: Each check refuses when its answer is no.
    why_it_matters: The cases must expect what the check does.
    verification_goal: Establish what each check does with a no answer.
  - belief: The earlier cases name the inactivity check's evaluation date and the training check's answer differently from this system.
    why_it_matters: A case naming what a check does not take or give proves nothing.
    verification_goal: Establish the names each check takes and gives.
  assumptions: []
  constraints:
  - constraint: What each check decides, and every act that uses them, is unchanged.
    source: Business author
  business_invariants:
  - invariant: No check answers no; a no is a refusal.
  - invariant: Every check is proven on every build by the cases stated beside it.
  lifecycle_states:
  - object: Check
    state: Proven
    meaning: Its cases are stated beside it and hold on every build.
  - object: Check
    state: Unproven
    meaning: Nothing states what it must answer. This change ends that state for all three.
  business_events:
  - event: NONE IDENTIFIED
    when_it_occurs: ''
    significance: This change announces nothing new.
  authority_boundaries:
  - business_object: The three checks and their cases
    authoritative_owner: AI Licensing
  - business_object: The cap, the training required and the threshold
    authoritative_owner: The acts that use the checks
  out_of_scope:
  - item: The cap, the training required and the threshold
    reason: Each is stated by the act that uses the check, and none changes.
  - item: The agent_governance subdomain
    reason: Not this change.
  governance_scope:
  - scope_item: ai_licensing
    relationship: MODIFIED
  - scope_item: agent_governance
    relationship: ADJACENT
  clarification_requests: []
  acceptance_criteria:
  - criterion: Each of the three checks is proven on every build.
  - criterion: A license check with fewer assigned than the cap answers that one is available, with how many remain; at the cap it refuses.
  - criterion: A training check for an employee with training complete answers that they are eligible; without it, it refuses.
  - criterion: An inactivity check for a license unused for the threshold or more answers that it is inactive, with how many days; for one used more recently, it refuses.
  - criterion: Every act that uses the checks behaves as it did before this change.
  identity_and_sameness: []
  lifecycle_transitions:
  - object: Check
    from_state: Unproven
    to_state: Proven
    triggered_by: Its cases being stated beside it
    cascade: None.
  operation_refusals: []
  authority_deferrals: []
```

Reorganized faithfully from `p0_business_problem_statement.md`, including the clarifications its
author answered. Human input only — nothing here was added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

## 1. CR Type

## 2. Business Vocabulary

## 3. Requested Outcomes

## 4. Known Facts — Business Truths

## 5. Existing-System Beliefs — Requiring Verification

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

## 6. Assumptions

## 7. Constraints

## 8. Business Invariants

## 9. Lifecycle States

## 10. Business Events

## 11. Authority Boundaries

## 12. Out of Scope

## 13. Governance Scope

## 14. Clarification Requests

## 15. Acceptance Criteria

## 16. Identity and Sameness

## 17. Lifecycle Transitions

## 18. Operation Refusals

## 19. Authority Deferrals
