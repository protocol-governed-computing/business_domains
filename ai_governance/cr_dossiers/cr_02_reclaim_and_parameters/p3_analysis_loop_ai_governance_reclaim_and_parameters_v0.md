# Stage 3 — Analysis Loop: ai_governance / reclaim and parameter result

**Stage:** 3 — Analysis Loop

**CR:** cr_02_reclaim_and_parameters

**Status:** DRAFT

**Feeds:** Stage 4 — Business Model

The gaps carried from Stage 2 are driven to committed decisions against the pinned composition.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| Q1 | The removal step answers VIOLATION by ending the contract with it, as it already ends the contract on every other answer. | No reclaim carries on past a refused removal. | OBSERVED | HIGH | CLOSED | S2 belief_verification #1 |
| Q2 | The contract already declares VIOLATION, and the reclaim act already routes it to EXIT_ACTIVE. A refused removal ends there, with the license still assigned, as the business decided. | No contract outcome and no route changes. | OBSERVED | HIGH | CLOSED | S2 belief_verification #2; S1 known_facts #3 |
| Q3 | Every reclaim the registry does not refuse takes exactly the route it takes today; the change adds one answer and touches no other. | Nothing else a reclaim does changes. | OBSERVED | HIGH | CLOSED | S1 constraints #1 |
| Q4 | The new parameter check reports `validation_result` from the check's `valid`: whether every declared rule passed. It is a boolean. Its steps, rules and routes are otherwise those of the old check. | The check reports only what it receives. | OBSERVED | HIGH | CLOSED | S2 gaps #2 |
| Q5 | Each of the two contracts changes what it means: the reclaim gains an answer, and the parameter check reports something else. Both were published in v5, so each is a next version that the published one is replaced by, and the published one stays in the record, stood down, as v5 published it. | A citation of v5 still names what v5 said. | OBSERVED | HIGH | CLOSED | S2 belief_verification #4; S2 gaps #3; S1 known_facts #7 |
| Q6 | The reclaim act and the governed action are re-pointed: the contract each one's place runs becomes its next version, and the place's label and routes are unchanged. | Each act decides exactly as today. | OBSERVED | HIGH | CLOSED | S2 architectural_observations #3; S2 belief_verification #5; S2 gaps #4 |

## 2. Verification Results

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------------------------------|----------|
| The step that removes an assignment does not answer a refused removal. | S2 belief_verification #1 | CONFIRMED | Resolved in Q1 |
| The reclaim already ends as still active for a license that is not inactive. | S2 belief_verification #2 | CONFIRMED | Resolved in Q2 |
| The parameter check reads its result from a place the check underneath never writes. | S2 belief_verification #3 | CONFIRMED | Resolved in Q4 |
| Both acts this change touches were published in v5. | S2 belief_verification #4 | CONFIRMED | Resolved in Q5 |
| One workflow runs each of the two contracts. | S2 belief_verification #5 | CONFIRMED | Resolved in Q6 |
| The removal step does not answer a refused removal. | S2 gaps #1 | CONFIRMED | Resolved in Q1 |
| The parameter check reports a result it never receives. | S2 gaps #2 | CONFIRMED | Resolved in Q4 |
| Two published acts would mean something v5 did not say if changed in place. | S2 gaps #3 | CONFIRMED | Resolved in Q5 |
| Two workflows run the published acts. | S2 gaps #4 | CONFIRMED | Resolved in Q6 |
| The reclaim has never been stated in a design. | S2 discovery_concerns #1 | CONFIRMED | Resolved by stating its next version whole in this design |

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|------------------------|----------|
| Reclaiming a license | Capability contract | AUTHOR_NEW | ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 is replaced by its next version, which answers a refused removal |
| The license registry | Platform capability | REUSE | capability_side_effects::CS_REGISTRY_V0, unchanged |
| The inactivity check | Capability transform | REUSE | ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0, unchanged |
| The reclaim act | Workflow | EXISTING | ai_governance::WF_AUTO_RECLAIM_V0, re-pointed |
| The parameter check | Capability contract | AUTHOR_NEW | ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0 is replaced by its next version |
| Checking against rules | Capability transform | REUSE | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0, unchanged |
| Looking up a tool's rules | Capability transform | REUSE | capability_transforms::CT_PURE_LOOKUP_V0, unchanged |
| Governing an action | Workflow | EXISTING | ai_governance::WF_GOVERN_AGENT_ACTION_V0, re-pointed |

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 | Stood down and replaced by its next version; run by one workflow | 2 | si.topology.impact impacted_count 2 |
| ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0 | Stood down and replaced by its next version; run by one workflow | 1 | The record names ai_governance::WF_GOVERN_AGENT_ACTION_V0 only |

## 5. Authoring Decisions

<!-- register:authoring_decisions business_language=capability -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|------------|----------|-----------|----------------------|----------------|
| End a reclaim the registry refuses | AUTHOR_NEW | A next version of the reclaim, whose removal step ends the contract on a refused removal; the act sends it to still active. | A separate ending was checked and rejected by the business: the license stays assigned, which is what still active says. Amending the published reclaim in place was rejected: it changes what a published act means. | S3 analysis_findings Q1; S3 analysis_findings Q5 |
| Check an action's parameters | AUTHOR_NEW | A next version that reports what it receives. | Amending the check in place was rejected: it changes what a published check reports. | S3 analysis_findings Q4; S3 analysis_findings Q5 |

## 6. Placement Decision

<!-- register:placement_decision business_language=rationale -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| EXTEND | ai_licensing | The reclaim is AI Licensing's own. | S3 analysis_findings Q1 |
| EXTEND | agent_governance | The parameter check is Agent Governance's. | S3 analysis_findings Q4 |

## 7. Saturation Assessment

<!-- register:saturation business_language=criterion -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| No unresolved CRITICAL gaps | SATISFIED | The two CRITICAL gaps resolve in Q4 and Q5 |
| No open analyst questions | SATISFIED | All six findings are CLOSED. The business answered where a refused removal ends, at the seed |
| No dependency expansion in the last pass | SATISFIED | A second pass found the reclaim act's route for VIOLATION already in place, and the record names one referrer of each contract |
| Verification pass complete, no OVERTURNED item unresolved | SATISFIED | All ten items re-grounded and CONFIRMED |
| Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried forward with a reason | SATISFIED | Every finding is OBSERVED |
