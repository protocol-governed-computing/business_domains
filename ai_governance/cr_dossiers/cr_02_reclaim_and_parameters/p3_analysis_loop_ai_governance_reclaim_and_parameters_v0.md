# Stage 3 — Analysis Loop: ai_governance / reclaim and parameter result

## Machine

```yaml
document:
  phase: p3
  domain: ai_governance
  subdomain:
  - reclaim
  - parameter result
  cr: cr_02_reclaim_and_parameters
  rule_set: transformation.schemas.REGISTER_SCHEMA_P3_V0
registers:
  analysis_findings:
  - question_id: Q1
    finding: The removal step answers VIOLATION by ending the contract with it, as it already ends the contract on every other answer.
    impact: No reclaim carries on past a refused removal.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'S2 belief_verification #1'
  - question_id: Q2
    finding: The contract already declares VIOLATION, and the reclaim act already routes it to EXIT_ACTIVE. A refused removal ends there, with the license still assigned, as the business decided.
    impact: No contract outcome and no route changes.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'S2 belief_verification #2; S1 known_facts #3'
  - question_id: Q3
    finding: Every reclaim the registry does not refuse takes exactly the route it takes today; the change adds one answer and touches no other.
    impact: Nothing else a reclaim does changes.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'S1 constraints #1'
  - question_id: Q4
    finding: 'The new parameter check reports `validation_result` from the check''s `valid`: whether every declared rule passed. It is a boolean. Its steps, rules and routes are otherwise those of the old check.'
    impact: The check reports only what it receives.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'S2 gaps #2'
  - question_id: Q5
    finding: 'Each of the two contracts changes what it means: the reclaim gains an answer, and the parameter check reports something else. Both were published in v5, so each is a next version that the published one is replaced by, and the published one stays in the record, stood down, as v5 published it.'
    impact: A citation of v5 still names what v5 said.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'S2 belief_verification #4; S2 gaps #3; S1 known_facts #7'
  - question_id: Q6
    finding: 'The reclaim act and the governed action are re-pointed: the contract each one''s place runs becomes its next version, and the place''s label and routes are unchanged.'
    impact: Each act decides exactly as today.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'S2 architectural_observations #3; S2 belief_verification #5; S2 gaps #4'
  verification_results:
  - item: The step that removes an assignment does not answer a refused removal.
    origin: {phase: p2, register: belief_verification, row: 1}
    result: CONFIRMED
    evidence: Resolved in Q1
  - item: The reclaim already ends as still active for a license that is not inactive.
    origin: {phase: p2, register: belief_verification, row: 2}
    result: CONFIRMED
    evidence: Resolved in Q2
  - item: The parameter check reads its result from a place the check underneath never writes.
    origin: {phase: p2, register: belief_verification, row: 3}
    result: CONFIRMED
    evidence: Resolved in Q4
  - item: Both acts this change touches were published in v5.
    origin: {phase: p2, register: belief_verification, row: 4}
    result: CONFIRMED
    evidence: Resolved in Q5
  - item: One workflow runs each of the two contracts.
    origin: {phase: p2, register: belief_verification, row: 5}
    result: CONFIRMED
    evidence: Resolved in Q6
  - item: The removal step does not answer a refused removal.
    origin: {phase: p2, register: gaps, row: 1}
    result: CONFIRMED
    evidence: Resolved in Q1
  - item: The parameter check reports a result it never receives.
    origin: {phase: p2, register: gaps, row: 2}
    result: CONFIRMED
    evidence: Resolved in Q4
  - item: Two published acts would mean something v5 did not say if changed in place.
    origin: {phase: p2, register: gaps, row: 3}
    result: CONFIRMED
    evidence: Resolved in Q5
  - item: Two workflows run the published acts.
    origin: {phase: p2, register: gaps, row: 4}
    result: CONFIRMED
    evidence: Resolved in Q6
  - item: The reclaim has never been stated in a design.
    origin: {phase: p2, register: discovery_concerns, row: 1}
    result: CONFIRMED
    evidence: Resolved by stating its next version whole in this design
  dependency_discoveries:
  - dependency: Reclaiming a license
    type: Capability contract
    disposition: AUTHOR_NEW
    evidence: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 is replaced by its next version, which answers a refused removal
  - dependency: The license registry
    type: Platform capability
    disposition: REUSE
    evidence: capability_side_effects::CS_REGISTRY_V0, unchanged
  - dependency: The inactivity check
    type: Capability transform
    disposition: REUSE
    evidence: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0, unchanged
  - dependency: The reclaim act
    type: Workflow
    disposition: EXISTING
    evidence: ai_governance::WF_AUTO_RECLAIM_V0, re-pointed
  - dependency: The parameter check
    type: Capability contract
    disposition: AUTHOR_NEW
    evidence: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0 is replaced by its next version
  - dependency: Checking against rules
    type: Capability transform
    disposition: REUSE
    evidence: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0, unchanged
  - dependency: Looking up a tool's rules
    type: Capability transform
    disposition: REUSE
    evidence: capability_transforms::CT_PURE_LOOKUP_V0, unchanged
  - dependency: Governing an action
    type: Workflow
    disposition: EXISTING
    evidence: ai_governance::WF_GOVERN_AGENT_ACTION_V0, re-pointed
  impact_analysis:
  - artifact: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
    impact_scope: Stood down and replaced by its next version; run by one workflow
    consumer_count: '2'
    evidence: si.topology.impact impacted_count 2
  - artifact: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0
    impact_scope: Stood down and replaced by its next version; run by one workflow
    consumer_count: '1'
    evidence: The record names ai_governance::WF_GOVERN_AGENT_ACTION_V0 only
  authoring_decisions:
  - capability: End a reclaim the registry refuses
    decision: AUTHOR_NEW
    rationale: A next version of the reclaim, whose removal step ends the contract on a refused removal; the act sends it to still active.
    alternatives_checked: 'A separate ending was checked and rejected by the business: the license stays assigned, which is what still active says. Amending the published reclaim in place was rejected: it changes what a published act means.'
    source_finding:
    - {phase: p3, register: analysis_findings, key: Q1}
    - {phase: p3, register: analysis_findings, key: Q5}
  - capability: Check an action's parameters
    decision: AUTHOR_NEW
    rationale: A next version that reports what it receives.
    alternatives_checked: 'Amending the check in place was rejected: it changes what a published check reports.'
    source_finding:
    - {phase: p3, register: analysis_findings, key: Q4}
    - {phase: p3, register: analysis_findings, key: Q5}
  placement_decision:
  - decision: EXTEND
    subdomain: ai_licensing
    rationale: The reclaim is AI Licensing's own.
    source_finding: {phase: p3, register: analysis_findings, key: Q1}
  - decision: EXTEND
    subdomain: agent_governance
    rationale: The parameter check is Agent Governance's.
    source_finding: {phase: p3, register: analysis_findings, key: Q4}
  saturation:
  - criterion: No unresolved CRITICAL gaps
    status: SATISFIED
    evidence: The two CRITICAL gaps resolve in Q4 and Q5
  - criterion: No open analyst questions
    status: SATISFIED
    evidence: All six findings are CLOSED. The business answered where a refused removal ends, at the seed
  - criterion: No dependency expansion in the last pass
    status: SATISFIED
    evidence: A second pass found the reclaim act's route for VIOLATION already in place, and the record names one referrer of each contract
  - criterion: Verification pass complete, no OVERTURNED item unresolved
    status: SATISFIED
    evidence: All ten items re-grounded and CONFIRMED
  - criterion: Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried forward with a reason
    status: SATISFIED
    evidence: Every finding is OBSERVED
```

The gaps carried from Stage 2 are driven to committed decisions against the pinned composition.

---

## 1. Analysis Findings

## 2. Verification Results

## 3. Dependency Discoveries

## 4. Impact Analysis

## 5. Authoring Decisions

## 6. Placement Decision

## 7. Saturation Assessment
