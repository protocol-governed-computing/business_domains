# Stage 2 — Domain Model Verification: ai_governance / ai_licensing

## Machine

```yaml
document:
  phase: p2
  domain: ai_governance
  subdomain: ai_licensing
  cr: cr_01_licensing
  rule_set: transformation.schemas.REGISTER_SCHEMA_P2_V0
registers:
  entities:
  - entity: The License Check
    description: Whether a license is available under the cap.
    store_model: None; a check computes from what it is given.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 2}
  - entity: The Training Check
    description: Whether an employee's required training is complete.
    store_model: None; a check computes from what it is given.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 3}
  - entity: The Inactivity Check
    description: Whether a license has gone unused for the threshold.
    store_model: None; a check computes from what it is given.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 4}
  - entity: The Case
    description: What a check is given and what it must answer, or that it must refuse.
    store_model: Stated beside the check; stated for none of the three today.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  entity_attributes:
  - entity: The License Check
    attribute: Assigned count and cap
    meaning: What it is given.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - entity: The License Check
    attribute: Available and remaining
    meaning: What it answers when a license is available.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - entity: The Training Check
    attribute: Training completed
    meaning: What it is given.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - entity: The Training Check
    attribute: Training eligible
    meaning: What it answers when training is complete.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - entity: The Inactivity Check
    attribute: Last active date, evaluation date and threshold
    meaning: What it is given.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - entity: The Inactivity Check
    attribute: Inactive and days inactive
    meaning: What it answers when the license is inactive.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  business_processes:
  - process: Prove a check
    initiator: Every build
    outcome: Each case stated beside the check is run against it, and the build refuses one that fails.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  process_steps:
  - process: Prove a check
    step: '1'
    action: Run each case stated beside the check.
    record_produced: A proven or refused verdict for the check.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  belief_verification:
  - belief: None of the three checks is proven.
    result: VERIFIED
    evidence: The domain's transform conformance reports ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0, ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0 and ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 unproven, with no case stated for any. They are the domain's only transforms. Its build configuration, ai_governance::STRUCTURE_BUILD_AI_GOVERNANCE_CONFIG_V0, does not compile the family cases are stated in.
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - belief: Each check refuses when its answer is no.
    result: VERIFIED
    evidence: 'Each declares `refusal: raises`, and each implementation raises when its answer is no: the cap reached, the training incomplete, the license used within the threshold. A plain return is SUCCESS, so a check answering no would let its act continue.'
    source_finding: {phase: p1, register: system_beliefs, row: 2}
  - belief: The earlier cases name the inactivity check's evaluation date and the training check's answer differently from this system.
    result: VERIFIED
    evidence: The earlier cases give the inactivity check `current_date`, and the check takes `evaluation_date`; they expect the training check to answer `is_eligible`, and it answers `training_eligible`. The license check's names agree.
    source_finding: {phase: p1, register: system_beliefs, row: 3}
  pps_baseline_fqdns:
  - capability: License check
    fqdn: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    what_it_does: Answers that a license is available, with how many remain; refuses at the cap.
    fit: PARTIAL
    cannot_do: Nothing proves it.
  - capability: Training check
    fqdn: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
    what_it_does: Answers that an employee is eligible; refuses without the training.
    fit: PARTIAL
    cannot_do: Nothing proves it.
  - capability: Inactivity check
    fqdn: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    what_it_does: Answers that a license is inactive, with how many days; refuses one used within the threshold.
    fit: PARTIAL
    cannot_do: Nothing proves it.
  - capability: Eligibility contract
    fqdn: ai_governance::CC_VALIDATE_ELIGIBILITY_V0
    what_it_does: Runs the training and license checks for a provisioning request.
    fit: EXACT
    cannot_do: Nothing; unchanged by this change.
  - capability: Reclamation contract
    fqdn: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
    what_it_does: Runs the inactivity check before a license is reclaimed.
    fit: EXACT
    cannot_do: Nothing; unchanged by this change.
  - capability: Build configuration
    fqdn: ai_governance::STRUCTURE_BUILD_AI_GOVERNANCE_CONFIG_V0
    what_it_does: Declares what the domain compiles.
    fit: PARTIAL
    cannot_do: It does not compile stated cases.
  gaps:
  - gap: No check is proven.
    severity: MAJOR
    impact: A check could change what it decides and every build would still pass.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - gap: The earlier cases disagree with the checks.
    severity: MINOR
    impact: Lifted as they stand, every no case and two names would fail.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  architectural_observations:
  - observation: Another domain states cases beside its transforms, and every build runs them.
    evidence: The causal language model domain compiles its cases and its transforms are proven.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 6}
  discovery_concerns:
  - concern: The build configuration must change for cases to compile.
    evidence: It is derived from the design rather than authored, so this change reaches it through its generator.
    severity: MINOR
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 6}
  open_questions: null
```

Every belief the change request declared is resolved against the pinned composition. What is
verified here is whether each of the three checks is proven, what each does with a no answer, and the
names each takes and gives.

---

## 1. Business Entities

## 2. Business Processes

## 3. Belief Verification — THE SPINE

## 4. PPS Baseline — What Already Exists

## 5. Gap Analysis — What Is Missing

## 6. Architectural Observations

## 7. Discovery Concerns

## 8. Open Questions
