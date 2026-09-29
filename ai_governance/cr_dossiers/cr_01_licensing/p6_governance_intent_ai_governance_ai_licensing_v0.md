# Stage 6 — Governance Intent: ai_governance / ai_licensing

**Stage:** 6 — Governance Intent

**CR:** cr_01_licensing

**Status:** DRAFT

**Feeds:** Stage 7 — Design Intent

Nothing moves and nothing is added: each check stays where it is and gains the cases that prove it.

---

## 1. Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Prove the license check | ai_licensing | OWNED |  | S5 scope_boundary Prove the license check |
| Prove the training check | ai_licensing | OWNED |  | S5 scope_boundary Prove the training check |
| Prove the inactivity check | ai_licensing | OWNED |  | S5 scope_boundary Prove the inactivity check |
| Compile the cases stated beside each check | ai_licensing | OWNED |  | S5 scope_boundary Compile the cases stated beside each check |

---

## 2. Storage Governance

<!-- register:storage_governance business_language=storage_need,purpose -->
| Storage Need | Purpose | Subdomain | Source Finding |
|--------------|---------|-----------|----------------|
| NONE IDENTIFIED | | | |

---

## 3. Cross-Subdomain Dependencies

<!-- register:cross_subdomain_deps optional -->
| Dependency | Direction | Existing Artifact | Status (SATISFIED, GAP) | Source Finding |
|------------|-----------|-------------------|-------------------------|----------------|
| NONE IDENTIFIED | | | | |

---

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE, EXTEND) | Source Finding |
|------|----------------|----------------------------------|----------------|
| ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0 | Present; unproven | EXTEND | S3 dependency_discoveries The license check |
| ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0 | Present; unproven | EXTEND | S3 dependency_discoveries The training check |
| ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 | Present; unproven | EXTEND | S3 dependency_discoveries The inactivity check |
| ai_governance::STRUCTURE_BUILD_AI_GOVERNANCE_CONFIG_V0 | Present; does not compile stated cases | EXTEND | S3 dependency_discoveries The build configuration |
| ai_governance::CC_VALIDATE_ELIGIBILITY_V0 | Present and reused unchanged | REUSE | S3 dependency_discoveries The acts using the checks |
| ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 | Present and reused unchanged | REUSE | S3 dependency_discoveries The acts using the checks |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| A_CHECK_IS_PROVEN_BESIDE_ITSELF | Each check's cases are stated with it and run on every build. | S4 design_decisions #1 |
| A_NO_IS_A_REFUSAL | Every no case expects a refusal. | S4 design_decisions #2 |
| THE_CONFIGURATION_IS_GENERATED | The build configuration is reached through its generator. | S4 design_decisions #4 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Prove the license check | ai_licensing | S6 ownership Prove the license check |
| Prove the training check | ai_licensing | S6 ownership Prove the training check |
| Prove the inactivity check | ai_licensing | S6 ownership Prove the inactivity check |
| Compile the cases stated beside each check | ai_licensing | S6 ownership Compile the cases stated beside each check |
