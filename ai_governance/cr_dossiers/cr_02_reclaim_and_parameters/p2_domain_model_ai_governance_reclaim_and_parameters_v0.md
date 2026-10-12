# Stage 2 — Domain Model Verification: ai_governance / reclaim and parameter result

## Machine

```yaml
document:
  phase: p2
  domain: ai_governance
  subdomain:
  - reclaim
  - parameter result
  cr: cr_02_reclaim_and_parameters
  rule_set: transformation.schemas.REGISTER_SCHEMA_P2_V0
registers:
  entities:
  - entity: The Assignment
    description: The registry's record that a license belongs to an employee.
    store_model: One registry, one entry per employee, unchanged by this change.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: business_vocabulary, row: 2}
  - entity: The Reclaim
    description: Taking back a license gone unused for the threshold of days.
    store_model: Not stored; an act. Announced when it removes an assignment.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: business_vocabulary, row: 1}
  - entity: The Governed Action
    description: An agent's proposed action, judged and recorded by the business.
    store_model: Recorded in the governance audit. Unchanged by this change.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: business_vocabulary, row: 4}
  - entity: The Parameter Check
    description: The step that checks an action's parameters against the rules declared for its tool.
    store_model: Not stored; run by the governed action.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: business_vocabulary, row: 5}
  entity_attributes:
  - entity: The Assignment
    attribute: The registry's answer to a removal
    meaning: Removed, not found, refused, or unreachable.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - entity: The Parameter Check
    attribute: Its result
    meaning: 'What it reports: today always empty.'
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  business_processes:
  - process: Reclaim an unused license
    initiator: The business, on its schedule
    outcome: The license is reclaimed, stays active, or the reclaim ends in error.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 1}
  - process: Govern an agent's action
    initiator: An agent
    outcome: The action is authorized and recorded, or denied and audited.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 3}
  process_steps:
  - process: Reclaim an unused license
    step: '1'
    action: Check whether the license has gone unused for the threshold of days, and refuse if not.
    record_produced: None.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 1}
  - process: Reclaim an unused license
    step: '2'
    action: Remove the employee's assignment from the registry.
    record_produced: The assignment, removed.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 1}
  - process: Reclaim an unused license
    step: '3'
    action: Record that the license was revoked.
    record_produced: An audit entry.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 2}
  - process: Govern an agent's action
    step: '1'
    action: Look up the rules declared for the tool.
    record_produced: None.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - process: Govern an agent's action
    step: '2'
    action: Check the parameters against them; a broken rule denies the action.
    record_produced: None.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  belief_verification:
  - belief: The step that removes an assignment does not answer a refused removal.
    result: VERIFIED
    evidence: capability_side_effects::CS_REGISTRY_V0 declares SUCCESS, NOT_FOUND, VIOLATION and BACKEND_ERROR for DEREGISTER. The deregister_license step of ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 answers SUCCESS, NOT_FOUND and BACKEND_ERROR, and not VIOLATION.
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - belief: The reclaim already ends as still active for a license that is not inactive.
    result: VERIFIED
    evidence: The inactivity check reports VIOLATION for a license still in use. ai_governance::WF_AUTO_RECLAIM_V0 routes the contract's VIOLATION to EXIT_ACTIVE, and the contract already declares VIOLATION among the outcomes it can end with.
    source_finding: {phase: p1, register: system_beliefs, row: 2}
  - belief: The parameter check reads its result from a place the check underneath never writes.
    result: VERIFIED
    evidence: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0 maps `validation_result` from the check's `value`. capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 declares two outputs, `valid`, always true when it returns, and `failed_rule`, always null, and raises when a rule fails. Running the governed action, the result was empty every time.
    source_finding: {phase: p1, register: system_beliefs, row: 3}
  - belief: Both acts this change touches were published in v5.
    result: VERIFIED
    evidence: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 and ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0 are each in the sealed v5 composition.
    source_finding: {phase: p1, register: system_beliefs, row: 4}
  - belief: One workflow runs each of the two contracts.
    result: VERIFIED
    evidence: 'ai_governance::WF_AUTO_RECLAIM_V0 runs the reclaim at one place, by short code, and is the only artifact whose declaration names it; ai_governance::IN_RECLAIM_LICENSE_V0 reaches it only by a routing edge. The composition''s record names one artifact whose declaration names the parameter check: ai_governance::WF_GOVERN_AGENT_ACTION_V0, which runs it at one place, by short code. Inspection also reports ai_governance::CC_BIND_LICENSE_TO_TOOL_SURFACE_V0, through the workflow''s route from the place it runs to this one; its declaration does not name the check.'
    source_finding: {phase: p1, register: system_beliefs, row: 5}
  pps_baseline_fqdns:
  - capability: Reclaiming a license
    fqdn: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
    what_it_does: Checks inactivity, then removes the assignment.
    fit: PARTIAL
    cannot_do: Its removal step does not answer a refused removal.
  - capability: Recording the revocation
    fqdn: ai_governance::WF_AUTO_RECLAIM_V0
    what_it_does: Runs the reclaim and records a revocation when it succeeds.
    fit: PARTIAL
    cannot_do: It already routes VIOLATION to still active; it names the published reclaim.
  - capability: Checking parameters
    fqdn: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0
    what_it_does: Looks up the tool's rules and checks the parameters against them.
    fit: PARTIAL
    cannot_do: Reports a result it never receives.
  - capability: Checking against rules
    fqdn: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    what_it_does: Returns that every rule passed, or denies.
    fit: EXACT
    cannot_do: Nothing for this purpose.
  - capability: Looking up a tool's rules
    fqdn: capability_transforms::CT_PURE_LOOKUP_V0
    what_it_does: Returns the rules declared for a tool.
    fit: EXACT
    cannot_do: Nothing for this purpose.
  - capability: Governing an action
    fqdn: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    what_it_does: Runs the five governance steps and audits each decision.
    fit: PARTIAL
    cannot_do: It names the published parameter check; it runs whichever check it names.
  gaps:
  - gap: The removal step does not answer a refused removal.
    severity: MAJOR
    impact: A reclaim the registry refused would carry on, and be recorded as a revocation.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - gap: The parameter check reports a result it never receives.
    severity: CRITICAL
    impact: Once the platform refuses a result that was never received, every governed action is refused.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - gap: Two published acts would mean something v5 did not say if changed in place.
    severity: CRITICAL
    impact: A citation of v5 would name a reclaim and a parameter check that answer differently.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 4}
  - gap: Two workflows run the published acts.
    severity: MAJOR
    impact: Once the acts are stood down, they would still be run.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  architectural_observations:
  - observation: One answer ends the reclaim two ways.
    evidence: A refused removal and a license still in use both end the contract with VIOLATION, so both reach EXIT_ACTIVE. Both leave the license assigned, which is what that ending says.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 2}
  - observation: The open standard now requires the closure.
    evidence: '`v1` Change 3 of the Open PGC Standard requires a composed step to answer every outcome its capability declares.'
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - observation: The governed action names the check at one place, and labels and routes to that place by the same spelling.
    evidence: Its place, its route and the check it runs are all written `CC_VALIDATE_TOOL_PARAMETERS_V0`; only the last names the check.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  - observation: A workflow's place keeps its label when the contract it runs is replaced.
    evidence: The compiler maps each place's label to the contract it runs, so a binding that reads a place keeps working when only the contract's identity changes.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  discovery_concerns:
  - concern: The reclaim has never been stated in a design.
    evidence: The first licensing change reused the reclaim unchanged, so this change states it whole for the first time.
    severity: MINOR
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 1}
  open_questions: null
```

Every belief the change request declared is resolved against the pinned composition. The registry's
declaration was read for the answers its removal can give, the reclaim contract for the answers its
removal step handles, and the reclaim act for where it sends each answer.

---

## 1. Business Entities

## 2. Business Processes

## 3. Belief Verification — THE SPINE

## 4. PPS Baseline — What Already Exists

## 5. Gap Analysis — What Is Missing

## 6. Architectural Observations

## 7. Discovery Concerns

## 8. Open Questions
