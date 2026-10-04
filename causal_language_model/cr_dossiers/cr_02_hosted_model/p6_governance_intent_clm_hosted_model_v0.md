# Stage 6 — Governance Intent: causal_language_model / model_response

**Stage:** 6 — Governance Intent

**CR:** cr_02_hosted_model

**Status:** DRAFT

**Feeds:** Stage 7 — Design Intent

The hosted way is placed beside the test model's in model_response. It reuses admission, the rules,
releasability and the record, and adds three acts the host drives. No store is added.

---

## 1. Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Begin a hosted request | model_response | OWNED |  | S5 scope_boundary Begin a hosted request |
| Confirm a hosted reading fits | model_response | OWNED |  | S5 scope_boundary Confirm a hosted reading fits |
| Open the record of a hosted request | model_response | OWNED |  | S5 scope_boundary Open the record of a hosted request |
| Read the state of a hosted request | model_response | OWNED |  | S5 scope_boundary Read the state of a hosted request |
| Choose a permitted token | model_response | OWNED |  | S5 scope_boundary Choose a permitted token |
| Offer the next candidates | model_response | OWNED |  | S5 scope_boundary Offer the next candidates |
| Release a hosted response | model_response | OWNED |  | S5 scope_boundary Release a hosted response |
| Authenticate the host | model_response | DEFERRED |  | S5 scope_boundary Authenticate the host |

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
| causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0 | Present; reused unchanged | REUSE | S3 dependency_discoveries Admission |
| causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0 | Present; reused unchanged | REUSE | S3 dependency_discoveries Admission |
| causal_language_model::CC_ADMIT_USER_PROMPT_V0 | Present; reused unchanged | REUSE | S3 dependency_discoveries Admission |
| causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 | Present; reused unchanged | REUSE | S3 dependency_discoveries Admission |
| causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0 | Present; reused unchanged | REUSE | S3 dependency_discoveries Forming the rules in force |
| causal_language_model::CC_CONFIRM_READING_FITS_V0 | Present; reused unchanged | REUSE | S3 dependency_discoveries Assembling what the model reads |
| causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0 | Present; reused unchanged | REUSE | S3 dependency_discoveries Releasability and the record |
| causal_language_model::CC_RECORD_USER_PROMPT_V0 | Present; reused unchanged | REUSE | S3 dependency_discoveries Releasability and the record |
| causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0 | Present; binds the subdomain's stores | REUSE | S3 dependency_discoveries The record trail |
| causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0 | Present; declares the user prompt records | REUSE | S3 dependency_discoveries The record trail |
| causal_language_model::AC_REQUESTER_V0 | Present; the requester | REUSE | S3 dependency_discoveries The three hosted acts, their gates and the host |
| causal_language_model::EV_USER_PROMPT_RESPONDED_V0 | Present; announced on release | REUSE | S3 dependency_discoveries The three hosted acts, their gates and the host |
| causal_language_model::EV_USER_PROMPT_REFUSED_V0 | Present; announced on refusal | REUSE | S3 dependency_discoveries The three hosted acts, their gates and the host |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| THE_HOST_PROPOSES | The host offers and asks; the business chooses, records and releases. | S4 design_decisions #1 |
| ONE_TRUTH_FOR_A_HOSTED_REQUEST | The record trail is the hosted request's state; no store copies it. | S4 design_decisions #4 |
| THE_TEST_MODEL_WAY_IS_UNCHANGED | No artifact of the test model's way of answering is redeclared. | S4 constraint_register #1 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Begin a hosted request | model_response | S6 ownership Begin a hosted request |
| Confirm a hosted reading fits | model_response | S6 ownership Confirm a hosted reading fits |
| Open the record of a hosted request | model_response | S6 ownership Open the record of a hosted request |
| Read the state of a hosted request | model_response | S6 ownership Read the state of a hosted request |
| Choose a permitted token | model_response | S6 ownership Choose a permitted token |
| Offer the next candidates | model_response | S6 ownership Offer the next candidates |
| Release a hosted response | model_response | S6 ownership Release a hosted response |
