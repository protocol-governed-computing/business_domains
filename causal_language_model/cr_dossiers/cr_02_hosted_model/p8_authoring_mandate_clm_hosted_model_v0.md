# Stage 8 — Authoring Mandate: causal_language_model / model_response

**Stage:** 8 — Authoring Mandate
**CR:** cr_02_hosted_model
**Status:** DRAFT
**Feeds:** Artifact Authoring

The 15 artifacts Stage 7 designed, scheduled in dependency order. Nothing is added here and
nothing is dropped: the mandate orders the build, it does not decide it. Every artifact the design
reuses already exists in the composition and is named only as a dependency.

---

## 1. Build Dependency Order

<!-- register:build_order -->
| Wave | Step | Code | Action (REPLACE, EXTEND, NEW) | Subdomain | Depends On |
|------|------|------|-------------------------------|-----------|------------|
| 1 | 1 | causal_language_model::AC_MODEL_HOST_V0 | NEW | model_response | — |
| 1 | 2 | causal_language_model::CT_PURE_READ_HOSTED_STATE_V0 | NEW | model_response | — |
| 1 | 3 | causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | NEW | model_response | — |
| 1 | 4 | causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0 | NEW | model_response | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 |
| 1 | 5 | causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | NEW | model_response | causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0, capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0, causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0 |
| 1 | 6 | causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0 | NEW | model_response | capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 |
| 1 | 7 | causal_language_model::CC_RECORD_HOSTED_STEP_V0 | NEW | model_response | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0, causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0 |
| 1 | 8 | causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0 | NEW | model_response | — |
| 1 | 9 | causal_language_model::IN_OFFER_NEXT_TOKENS_V0 | NEW | model_response | — |
| 1 | 10 | causal_language_model::IN_RELEASE_HOSTED_RESPONSE_V0 | NEW | model_response | — |
| 2 | 11 | causal_language_model::CC_READ_HOSTED_STATE_V0 | NEW | model_response | capability_side_effects::CS_APPENDONLY_JSONL_V0, causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0, causal_language_model::CT_PURE_READ_HOSTED_STATE_V0 |
| 2 | 12 | causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0 | NEW | model_response | causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 |
| 2 | 13 | causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | NEW | model_response | causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0, causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0, causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0, causal_language_model::CC_ADMIT_USER_PROMPT_V0, causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0, causal_language_model::CC_CONFIRM_READING_FITS_V0, causal_language_model::CC_OPEN_HOSTED_RECORD_V0, causal_language_model::CC_RECORD_USER_PROMPT_V0, causal_language_model::EV_USER_PROMPT_REFUSED_V0 |
| 3 | 14 | causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | NEW | model_response | causal_language_model::IN_OFFER_NEXT_TOKENS_V0, causal_language_model::CC_READ_HOSTED_STATE_V0, causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0, causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0, causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0, causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0, causal_language_model::CC_RECORD_HOSTED_STEP_V0, causal_language_model::CC_RECORD_USER_PROMPT_V0, causal_language_model::EV_USER_PROMPT_REFUSED_V0 |
| 3 | 15 | causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0 | NEW | model_response | causal_language_model::IN_RELEASE_HOSTED_RESPONSE_V0, causal_language_model::CC_READ_HOSTED_STATE_V0, causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0, causal_language_model::CC_RECORD_USER_PROMPT_V0, causal_language_model::EV_USER_PROMPT_RESPONDED_V0 |

Each artifact sits in the earliest wave its authored dependencies allow. Wave 1 holds the host, the
three entry points, the two atoms and the three contracts built from reused transforms alone. Wave 2
adds the contracts built on the new atoms. The three workflows come last, each waiting on the contracts
it runs.

---

## 2. Critical Path

<!-- register:critical_path -->
| Position | Code |
|----------|------|
| 1 | causal_language_model::CT_PURE_READ_HOSTED_STATE_V0 |
| 2 | causal_language_model::CC_READ_HOSTED_STATE_V0 |
| 3 | causal_language_model::WF_OFFER_NEXT_TOKENS_V0 |

The longest chain runs from the atom that reads the trail, through the contract that reads it, to the
offer act. No hosted response can be written until it is complete.

---

## 3. Artifact Summary

<!-- register:mandate_artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Count | Description |
|-------------------------------|-------|-------------|
| NEW | 15 | 1 AC, 3 IN, 3 WF, 6 CC, 2 CT — every identity Stage 7 assigned |

---

## 4. Subdomain Field Declarations

<!-- register:field_declarations -->
| Code | Subdomain Field |
|------|-----------------|
| causal_language_model::AC_MODEL_HOST_V0 | model_response |
| causal_language_model::CT_PURE_READ_HOSTED_STATE_V0 | model_response |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | model_response |
| causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0 | model_response |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | model_response |
| causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0 | model_response |
| causal_language_model::CC_RECORD_HOSTED_STEP_V0 | model_response |
| causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0 | model_response |
| causal_language_model::IN_OFFER_NEXT_TOKENS_V0 | model_response |
| causal_language_model::IN_RELEASE_HOSTED_RESPONSE_V0 | model_response |
| causal_language_model::CC_READ_HOSTED_STATE_V0 | model_response |
| causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0 | model_response |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | model_response |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | model_response |
| causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0 | model_response |

---

## 5. New Capabilities

<!-- register:new_capabilities optional -->
| Code | Purpose | Inputs | Outputs |
|------|---------|--------|---------|
| causal_language_model::CT_PURE_READ_HOSTED_STATE_V0 | Reduce a hosted request's trail to its state | entries:array | state:object |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | Stop forbidden tokens and choose a permitted one | state:object, candidates:array | step:object, text:string, finished:boolean, stopped_by:string, within_length:boolean |

---

## 6. New Intents

<!-- register:new_intents optional -->
| Code | Purpose | Workflow | Inputs |
|------|---------|----------|--------|
| causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0 | A request to a hosted model on behalf of a customer | causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | user_prompt_id:string, requester_id:string, permitted_customers:array, customer_id:string, account_numbers:array, identity_key:string, kind:string, question:string, supporting_material:string, seed:integer |
| causal_language_model::IN_OFFER_NEXT_TOKENS_V0 | The candidates a hosted model could write next, naming its fingerprint | causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | user_prompt_id:string, host_id:string, fingerprint:string, reported_reading_size:integer, candidates:array |
| causal_language_model::IN_RELEASE_HOSTED_RESPONSE_V0 | A request to release a completed hosted response | causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0 | user_prompt_id:string, host_id:string |

---

## 7. Cross-Subdomain Notes

<!-- register:cross_subdomain_notes optional -->
| Code | Note |
|------|------|
| causal_language_model::AC_MODEL_HOST_V0 | Names a host as it names itself. The host holds no authority and is not authenticated; each offer is checked against the admitted request, and a false one refuses the request. |

No model_response artifact writes into a store another subdomain owns.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 7 — Design Intent | p7_design_intent_clm_hosted_model_v0.md | GATE 1 APPROVED |
| Stage 8 — Authoring Mandate | This document | PENDING GATE 2 APPROVAL |
| Artifact Authoring | per build_order | PENDING |
