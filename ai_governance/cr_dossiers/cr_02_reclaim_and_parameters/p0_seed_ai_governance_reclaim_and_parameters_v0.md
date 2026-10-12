# Change Seed — ai_governance / reclaim and parameter result

## Machine

```yaml
document:
  phase: p0
  domain: ai_governance
  subdomain:
  - reclaim
  - parameter result
  cr: cr_02_reclaim_and_parameters
  rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0
registers:
  subdomain_purpose: |2

    The AI Licensing subdomain governs the business's licenses for AI tools: provisioning a license to an
    employee, and reclaiming a license that has gone unused for the business's threshold of days. The
    Agent Governance subdomain governs what an AI agent may do on the business's behalf: it judges an
    agent's proposed action, checks its parameters against the rules declared for the tool, and records
    every action it authorizes or denies. This change decides what a reclaim does when the registry
    refuses it and what the parameter check reports, and states each act it changes under a new identity.
  cr_type:
  - subdomain: ai_licensing
    classification: MODIFY
    rationale: A reclaim does not say what happens when the license registry refuses to remove an assignment. Nothing is added to what a reclaim does.
  - subdomain: agent_governance
    classification: MODIFY
    rationale: The parameter check reports a result it never receives.
  business_vocabulary:
  - term: Reclaim
    definition: Taking back a license that has gone unused for the business's threshold of days.
  - term: Assignment
    definition: The registry's record that a license belongs to an employee.
  - term: Refused removal
    definition: The registry's answer to a malformed request to remove an assignment.
  - term: Governed action
    definition: An agent's proposed action, judged and recorded by the business.
  - term: Parameter check
    definition: The step that checks an action's parameters against the rules declared for its tool.
  - term: Parameter result
    definition: 'What the parameter check reports: whether every declared rule passed.'
  - term: Published
    definition: Sealed into a composition that was released and cited.
  - term: Successor
    definition: The new identity that states what an act does after this change.
  - term: Stood down
    definition: Replaced by a declared successor, kept in the record and out of reach.
  requested_outcomes:
  - outcome: A reclaim the registry refuses ends with the license left assigned.
  - outcome: The parameter check reports whether every declared rule passed.
  - outcome: Each act whose meaning this changes has a successor, and its published identity is stood down unchanged.
  - outcome: Everything in force that runs a stood-down act runs its successor.
  - outcome: Every other reclaim, and every governed action, decides as it does today.
  known_facts:
  - fact: A reclaim ends as reclaimed, still active, or in error.
    certainty: HIGH
  - fact: A license the registry did not release stays with the employee.
    certainty: HIGH
  - fact: A reclaim the registry refused ends as still active.
    certainty: HIGH
  - fact: A parameter that breaks a declared rule denies the action.
    certainty: HIGH
  - fact: The check underneath answers only whether every rule passed; a broken rule denies the action.
    certainty: HIGH
  - fact: Nothing reads the parameter result today.
    certainty: HIGH
  - fact: Identity is fixed at publication; a change of meaning is a new identity.
    certainty: HIGH
  - fact: A published identity stays in the record, stood down, when a successor replaces it.
    certainty: HIGH
  - fact: A re-point changes which act a referrer runs, and nothing else about it.
    certainty: HIGH
  system_beliefs:
  - belief: The step that removes an assignment does not answer a refused removal.
    why_it_matters: An unanswered refusal is carried past.
    verification_goal: Establish which answers of the registry the removal step answers.
  - belief: The reclaim already ends as still active for a license that is not inactive.
    why_it_matters: A refused removal can end there without a new ending.
    verification_goal: Establish where the reclaim sends its still-active answer.
  - belief: The parameter check reads its result from a place the check underneath never writes.
    why_it_matters: The reported result is always empty.
    verification_goal: Establish what the check underneath returns and what the parameter check reads.
  - belief: Both acts this change touches were published in v5.
    why_it_matters: Each one it changes needs a successor.
    verification_goal: Establish which touched acts the v5 composition holds.
  - belief: One workflow runs each of the two contracts.
    why_it_matters: Everything that runs a replaced contract must run its successor.
    verification_goal: Establish everything that names each contract, by full name and by short code.
  assumptions: []
  constraints:
  - constraint: Every reclaim the registry does not refuse ends exactly as it did before this change.
    source: Business author
  - constraint: No ending is added.
    source: Business author
  - constraint: The governed action decides exactly as it does today.
    source: Business author
  - constraint: No published identity changes what it says, except to be stood down.
    source: Business author — identity is fixed at publication.
  business_invariants:
  - invariant: No reclaim carries on past a removal the registry refused.
  - invariant: No license is reported reclaimed that the registry did not release.
  - invariant: A check reports only what it receives.
  - invariant: A published identity means what it meant when it was published.
  lifecycle_states:
  - object: License
    state: Assigned
    meaning: Held by an employee. Unchanged by this change.
  - object: License
    state: Reclaimed
    meaning: Taken back after going unused. Unchanged by this change.
  - object: Published act
    state: In force
    meaning: Run when a request reaches it.
  - object: Published act
    state: Stood down
    meaning: Replaced by its successor, kept in the record as published.
  business_events:
  - event: A license was revoked
    when_it_occurs: When a reclaim removes an assignment
    significance: Unchanged; it is not announced when the registry refuses the removal.
  authority_boundaries:
  - business_object: What a reclaim does when the registry refuses it
    authoritative_owner: AI Licensing
  - business_object: The rules declared for each tool
    authoritative_owner: Agent Governance
  - business_object: What the check underneath answers
    authoritative_owner: The platform
  out_of_scope:
  - item: Telling a refused removal apart from a license still in use
    reason: The business keeps three endings; both leave the license assigned.
  - item: Provisioning a license
    reason: Not this change.
  - item: Which rules each tool declares
    reason: Unchanged.
  - item: Reporting which rule failed
    reason: The check underneath denies rather than returns it.
  - item: The licence-cap check nothing runs
    reason: It stays as v5 published it.
  governance_scope:
  - scope_item: ai_licensing
    relationship: MODIFIED
  - scope_item: agent_governance
    relationship: MODIFIED
  clarification_requests: []
  acceptance_criteria:
  - criterion: A reclaim the registry refuses ends as still active, the license stays assigned, and no revocation is announced.
  - criterion: Every reclaim the registry does not refuse ends exactly as it did before this change.
  - criterion: An action whose parameters satisfy every rule is authorized, and the parameter result says every rule passed.
  - criterion: An action whose parameters break a rule is denied and audited, as today.
  - criterion: Each act whose meaning this changes is stated under a new identity, and the published identity is unchanged except for its stand-down.
  - criterion: Nothing in force runs a stood-down act.
  identity_and_sameness:
  - business_object: Act
    identified_by: Its identity
    two_are_the_same_when: Its declaration means what the published declaration meant
  lifecycle_transitions:
  - object: Published act
    from_state: In force
    to_state: Stood down
    triggered_by: This change adds its successor
    cascade: Whatever runs it is re-pointed
  operation_refusals:
  - operation: Reclaiming a license
    refused_when: The registry refuses to remove the assignment
    business_reason: A license the registry did not release stays with the employee.
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
