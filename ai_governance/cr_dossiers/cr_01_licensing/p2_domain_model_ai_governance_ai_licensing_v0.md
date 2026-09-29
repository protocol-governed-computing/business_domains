# Stage 2 — Domain Model Verification: ai_governance / ai_licensing

**Stage:** 2 — Domain Model Verification
**CR:** cr_01_licensing
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief the change request declared is resolved against the pinned composition. What is
verified here is whether each of the three checks is proven, what each does with a no answer, and the
names each takes and gives.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| The License Check | Whether a license is available under the cap. | None; a check computes from what it is given. | OBSERVED | S1 known_facts #2 |
| The Training Check | Whether an employee's required training is complete. | None; a check computes from what it is given. | OBSERVED | S1 known_facts #3 |
| The Inactivity Check | Whether a license has gone unused for the threshold. | None; a check computes from what it is given. | OBSERVED | S1 known_facts #4 |
| The Case | What a check is given and what it must answer, or that it must refuse. | Stated beside the check; stated for none of the three today. | OBSERVED | S2 belief_verification #1 |

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| The License Check | Assigned count and cap | What it is given. | OBSERVED | S2 belief_verification #3 |
| The License Check | Available and remaining | What it answers when a license is available. | OBSERVED | S2 belief_verification #3 |
| The Training Check | Training completed | What it is given. | OBSERVED | S2 belief_verification #3 |
| The Training Check | Training eligible | What it answers when training is complete. | OBSERVED | S2 belief_verification #3 |
| The Inactivity Check | Last active date, evaluation date and threshold | What it is given. | OBSERVED | S2 belief_verification #3 |
| The Inactivity Check | Inactive and days inactive | What it answers when the license is inactive. | OBSERVED | S2 belief_verification #3 |

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Prove a check | Every build | Each case stated beside the check is run against it, and the build refuses one that fails. | OBSERVED | S1 requested_outcomes #1 |

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Prove a check | 1 | Run each case stated beside the check. | A proven or refused verdict for the check. | OBSERVED | S2 belief_verification #1 |

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| None of the three checks is proven. | VERIFIED | The domain's transform conformance reports ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0, ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0 and ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 unproven, with no case stated for any. They are the domain's only transforms. Its build configuration, ai_governance::STRUCTURE_BUILD_AI_GOVERNANCE_CONFIG_V0, does not compile the family cases are stated in. | S1 system_beliefs #1 |
| Each check refuses when its answer is no. | VERIFIED | Each declares `refusal: raises`, and each implementation raises when its answer is no: the cap reached, the training incomplete, the license used within the threshold. A plain return is SUCCESS, so a check answering no would let its act continue. | S1 system_beliefs #2 |
| The earlier cases name the inactivity check's evaluation date and the training check's answer differently from this system. | VERIFIED | The earlier cases give the inactivity check `current_date`, and the check takes `evaluation_date`; they expect the training check to answer `is_eligible`, and it answers `training_eligible`. The license check's names agree. | S1 system_beliefs #3 |

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| License check | ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0 | Answers that a license is available, with how many remain; refuses at the cap. | PARTIAL | Nothing proves it. |
| Training check | ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0 | Answers that an employee is eligible; refuses without the training. | PARTIAL | Nothing proves it. |
| Inactivity check | ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 | Answers that a license is inactive, with how many days; refuses one used within the threshold. | PARTIAL | Nothing proves it. |
| Eligibility contract | ai_governance::CC_VALIDATE_ELIGIBILITY_V0 | Runs the training and license checks for a provisioning request. | EXACT | Nothing; unchanged by this change. |
| Reclamation contract | ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 | Runs the inactivity check before a license is reclaimed. | EXACT | Nothing; unchanged by this change. |
| Build configuration | ai_governance::STRUCTURE_BUILD_AI_GOVERNANCE_CONFIG_V0 | Declares what the domain compiles. | PARTIAL | It does not compile stated cases. |

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| No check is proven. | MAJOR | A check could change what it decides and every build would still pass. | OBSERVED | S2 belief_verification #1 |
| The earlier cases disagree with the checks. | MINOR | Lifted as they stand, every no case and two names would fail. | OBSERVED | S2 belief_verification #3 |

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| Another domain states cases beside its transforms, and every build runs them. | The causal language model domain compiles its cases and its transforms are proven. | OBSERVED | S2 pps_baseline_fqdns #6 |

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| The build configuration must change for cases to compile. | It is derived from the design rather than authored, so this change reaches it through its generator. | MINOR | OBSERVED | S2 pps_baseline_fqdns #6 |

## 8. Open Questions

<!-- register:open_questions -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
