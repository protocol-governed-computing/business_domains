# Stage 8 — Authoring Mandate: causal_language_model / model_response

**Stage:** 8 — Authoring Mandate
**CR:** cr_01_model_response
**Status:** DRAFT
**Feeds:** Artifact Authoring

The 43 artifacts Stage 7 designed, scheduled in dependency order. Nothing is added here and
nothing is dropped: the mandate orders the build, it does not decide it. Every artifact the design
reuses already exists in the composition and is named only as a dependency.

---

## 1. Build Dependency Order

<!-- register:build_order -->
| Wave | Step | Code | Action (REPLACE, EXTEND, NEW) | Subdomain | Depends On |
|------|------|------|-------------------------------|-----------|------------|
| 1 | 1 | causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0 | NEW | model_response | — |
| 1 | 2 | causal_language_model::VOCAB_KIND_OF_INFORMATION_V0 | NEW | model_response | — |
| 1 | 3 | causal_language_model::AC_MODEL_STAFF_V0 | NEW | model_response | — |
| 1 | 4 | causal_language_model::AC_REQUESTER_V0 | NEW | model_response | — |
| 1 | 5 | causal_language_model::EV_MODEL_REGISTERED_V0 | NEW | model_response | — |
| 1 | 6 | causal_language_model::EV_MODEL_SERVICE_STARTED_V0 | NEW | model_response | — |
| 1 | 7 | causal_language_model::EV_MODEL_SERVICE_ENDED_V0 | NEW | model_response | — |
| 1 | 8 | causal_language_model::EV_USER_PROMPT_RESPONDED_V0 | NEW | model_response | — |
| 1 | 9 | causal_language_model::EV_USER_PROMPT_REFUSED_V0 | NEW | model_response | — |
| 1 | 10 | causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0 | NEW | model_response | — |
| 1 | 11 | causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0 | NEW | model_response | — |
| 1 | 12 | causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0 | NEW | model_response | — |
| 1 | 13 | causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0 | NEW | model_response | — |
| 1 | 14 | causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0 | NEW | model_response | — |
| 1 | 15 | causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | NEW | model_response | — |
| 1 | 16 | causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 | NEW | model_response | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 |
| 1 | 17 | causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0 | NEW | model_response | capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 |
| 1 | 18 | causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0 | NEW | model_response | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 |
| 1 | 19 | causal_language_model::IN_REGISTER_MODEL_V0 | NEW | model_response | — |
| 1 | 20 | causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0 | NEW | model_response | — |
| 1 | 21 | causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0 | NEW | model_response | — |
| 1 | 22 | causal_language_model::IN_SUBMIT_USER_PROMPT_V0 | NEW | model_response | — |
| 1 | 23 | causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0 | NEW | model_response | — |
| 2 | 24 | causal_language_model::CT_WRITE_NEXT_WORD_V0 | NEW | model_response | causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0, causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 |
| 2 | 25 | causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0 | NEW | model_response | capability_side_effects::CS_REGISTRY_V0, causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0 |
| 2 | 26 | causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0 | NEW | model_response | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0, capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0, causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0, capability_side_effects::CS_REGISTRY_V0, causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0 |
| 2 | 27 | causal_language_model::CC_REGISTER_MODEL_V0 | NEW | model_response | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0, capability_side_effects::CS_MUTABLE_JSON_V0, causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0 |
| 2 | 28 | causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | NEW | model_response | capability_side_effects::CS_MUTABLE_JSON_V0, causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0, capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0, capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0, capability_side_effects::CS_REGISTRY_V0, capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 |
| 2 | 29 | causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0 | NEW | model_response | capability_side_effects::CS_MUTABLE_JSON_V0, causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0, capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 |
| 2 | 30 | causal_language_model::CC_ADMIT_USER_PROMPT_V0 | NEW | model_response | capability_side_effects::CS_MUTABLE_JSON_V0, causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0, capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 |
| 2 | 31 | causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 | NEW | model_response | capability_side_effects::CS_MUTABLE_JSON_V0, causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0, capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0, causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0 |
| 2 | 32 | causal_language_model::CC_CONFIRM_READING_FITS_V0 | NEW | model_response | causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0 |
| 2 | 33 | causal_language_model::CC_RECORD_USER_PROMPT_V0 | NEW | model_response | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0, causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0 |
| 2 | 34 | causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0 | NEW | model_response | capability_side_effects::CS_APPENDONLY_JSONL_V0, causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0, capability_transforms::CT_PURE_FILTER_RECORDS_V0 |
| 2 | 35 | causal_language_model::CC_APPEND_MODEL_OPERATION_V0 | NEW | model_response | capability_side_effects::CS_APPENDONLY_JSONL_V0, causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0 |
| 3 | 36 | causal_language_model::CT_WRITE_RESPONSE_V0 | NEW | model_response | causal_language_model::CT_WRITE_NEXT_WORD_V0 |
| 3 | 37 | causal_language_model::WF_REGISTER_MODEL_V0 | NEW | model_response | causal_language_model::IN_REGISTER_MODEL_V0, causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0, causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0, causal_language_model::CC_REGISTER_MODEL_V0, causal_language_model::CC_APPEND_MODEL_OPERATION_V0, causal_language_model::EV_MODEL_REGISTERED_V0 |
| 3 | 38 | causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0 | NEW | model_response | causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0, causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0, causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0, causal_language_model::CC_APPEND_MODEL_OPERATION_V0, causal_language_model::EV_MODEL_SERVICE_STARTED_V0 |
| 3 | 39 | causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0 | NEW | model_response | causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0, causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0, causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0, causal_language_model::CC_APPEND_MODEL_OPERATION_V0, causal_language_model::EV_MODEL_SERVICE_ENDED_V0 |
| 3 | 40 | causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0 | NEW | model_response | causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0, causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0, causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0, causal_language_model::CC_APPEND_MODEL_OPERATION_V0 |
| 4 | 41 | causal_language_model::CC_WRITE_MODEL_RESPONSE_V0 | NEW | model_response | causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0, causal_language_model::CT_WRITE_RESPONSE_V0 |
| 5 | 42 | causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | NEW | model_response | causal_language_model::IN_SUBMIT_USER_PROMPT_V0, causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0, causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0, causal_language_model::CC_ADMIT_USER_PROMPT_V0, causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0, causal_language_model::CC_CONFIRM_READING_FITS_V0, causal_language_model::CC_WRITE_MODEL_RESPONSE_V0, causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0, causal_language_model::CC_RECORD_USER_PROMPT_V0, causal_language_model::EV_USER_PROMPT_RESPONDED_V0, causal_language_model::EV_USER_PROMPT_REFUSED_V0 |
| 6 | 43 | causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0 | NEW | model_response | causal_language_model::WF_REGISTER_MODEL_V0, causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0, causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0, causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0, causal_language_model::WF_SUBMIT_USER_PROMPT_V0, causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0 |

Each artifact sits in the earliest wave its authored dependencies allow. Wave 1 holds everything that
depends only on the platform: the store declaration, the vocabulary, the actors, the business moments,
the six atoms, the entry points and the three contracts built from reused transforms alone. Wave 2 adds
the pass molecule and the contracts that address a store or a new atom. Wave 3 adds the response
molecule and the four staff workflows. The writing contract waits on the response molecule, the
submission workflow on the writing contract, and the runtime binding, which binds every workflow,
comes last.

---

## 2. Critical Path

<!-- register:critical_path -->
| Position | Code |
|----------|------|
| 1 | causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0 |
| 2 | causal_language_model::CT_WRITE_NEXT_WORD_V0 |
| 3 | causal_language_model::CT_WRITE_RESPONSE_V0 |
| 4 | causal_language_model::CC_WRITE_MODEL_RESPONSE_V0 |
| 5 | causal_language_model::WF_SUBMIT_USER_PROMPT_V0 |
| 6 | causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0 |

The longest chain runs from the model's offer through both writing molecules, the writing contract
and the submission workflow to the runtime binding. No user prompt can be answered until it is
complete.

---

## 3. Artifact Summary

<!-- register:mandate_artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Count | Description |
|-------------------------------|-------|-------------|
| NEW | 43 | 2 AC, 5 IN, 5 WF, 15 CC, 8 CT, 5 EV, 1 VOCAB, 1 RB, 1 STRUCTURE — every identity Stage 7 assigned |

---

## 4. Subdomain Field Declarations

<!-- register:field_declarations -->
| Code | Subdomain Field |
|------|-----------------|
| causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0 | model_response |
| causal_language_model::VOCAB_KIND_OF_INFORMATION_V0 | model_response |
| causal_language_model::AC_MODEL_STAFF_V0 | model_response |
| causal_language_model::AC_REQUESTER_V0 | model_response |
| causal_language_model::EV_MODEL_REGISTERED_V0 | model_response |
| causal_language_model::EV_MODEL_SERVICE_STARTED_V0 | model_response |
| causal_language_model::EV_MODEL_SERVICE_ENDED_V0 | model_response |
| causal_language_model::EV_USER_PROMPT_RESPONDED_V0 | model_response |
| causal_language_model::EV_USER_PROMPT_REFUSED_V0 | model_response |
| causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0 | model_response |
| causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0 | model_response |
| causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0 | model_response |
| causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0 | model_response |
| causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0 | model_response |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | model_response |
| causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 | model_response |
| causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0 | model_response |
| causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0 | model_response |
| causal_language_model::IN_REGISTER_MODEL_V0 | model_response |
| causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0 | model_response |
| causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0 | model_response |
| causal_language_model::IN_SUBMIT_USER_PROMPT_V0 | model_response |
| causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0 | model_response |
| causal_language_model::CT_WRITE_NEXT_WORD_V0 | model_response |
| causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0 | model_response |
| causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0 | model_response |
| causal_language_model::CC_REGISTER_MODEL_V0 | model_response |
| causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | model_response |
| causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0 | model_response |
| causal_language_model::CC_ADMIT_USER_PROMPT_V0 | model_response |
| causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 | model_response |
| causal_language_model::CC_CONFIRM_READING_FITS_V0 | model_response |
| causal_language_model::CC_RECORD_USER_PROMPT_V0 | model_response |
| causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0 | model_response |
| causal_language_model::CC_APPEND_MODEL_OPERATION_V0 | model_response |
| causal_language_model::CT_WRITE_RESPONSE_V0 | model_response |
| causal_language_model::WF_REGISTER_MODEL_V0 | model_response |
| causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0 | model_response |
| causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0 | model_response |
| causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0 | model_response |
| causal_language_model::CC_WRITE_MODEL_RESPONSE_V0 | model_response |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | model_response |
| causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0 | model_response |

---

## 5. New Capabilities

<!-- register:new_capabilities optional -->
| Code | Purpose | Inputs | Outputs |
|------|---------|--------|---------|
| causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0 | Form the single key claimed for a model from its description and fingerprint | description:object, fingerprint:string | identity_key:string |
| causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0 | Decide whether a kind of information is no more sensitive than a ceiling | kind:string, ceiling:string, kinds:array | within_ceiling:boolean |
| causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0 | Assemble exactly what the model reads and decide whether it fits | system_prompt:string, question:string, supporting_material:string, reading_capacity:integer | reading:object, reading_length:integer |
| causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0 | Form the response rules in force for one user prompt | response_rules:object, account_numbers:array, seed:integer | rules_in_force:object, positions:array |
| causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0 | The model's offer of its next words | reading:object, text:string, finished:boolean, stopped_by:string | candidates:array |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | Stop forbidden words and choose one permitted word | candidates:array, rules_in_force:object, position:integer, text:string, finished:boolean, stopped_by:string, stopped:array | text:string, finished:boolean, stopped_by:string, stopped:array |
| causal_language_model::CT_WRITE_NEXT_WORD_V0 | One pass of writing: the model's offer, then the rules' choice | reading:object, rules_in_force:object, position:integer, text:string, finished:boolean, stopped_by:string, stopped:array | result:object |
| causal_language_model::CT_WRITE_RESPONSE_V0 | Write a response one pass per word, up to the longest response | reading:object, rules_in_force:object, positions:array | result:object |

---

## 6. New Intents

<!-- register:new_intents optional -->
| Code | Purpose | Workflow | Inputs |
|------|---------|----------|--------|
| causal_language_model::IN_REGISTER_MODEL_V0 | A request to register a model with its description and fingerprint | causal_language_model::WF_REGISTER_MODEL_V0 | staff_credentials:object, staff_id:string, description:object, fingerprint:string |
| causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0 | A request to place a registered model in service with its ceiling, system prompt and response rules | causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0 | staff_credentials:object, staff_id:string, identity_key:string, time_in_service_id:string, ceiling:string, system_prompt:string, response_rules:object |
| causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0 | A request to withdraw a model from service | causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0 | staff_credentials:object, staff_id:string, identity_key:string |
| causal_language_model::IN_SUBMIT_USER_PROMPT_V0 | A user prompt submitted on behalf of a customer | causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | user_prompt_id:string, requester_id:string, permitted_customers:array, customer_id:string, account_numbers:array, identity_key:string, kind:string, question:string, supporting_material:string, seed:integer |
| causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0 | A request to retrieve the record of a user prompt | causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0 | staff_credentials:object, staff_id:string, user_prompt_id:string |

---

## 7. Cross-Subdomain Notes

<!-- register:cross_subdomain_notes optional -->
| Code | Note |
|------|------|
| causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 | Checks the staff member's asserted credentials against rules this design fixes, and grants nothing. Who is model staff is decided by the business's existing arrangements, which assert it through the ingress. |
| causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0 | Checks the customer against the requester's permitted customers as the business's existing arrangements assert them, and grants nothing. |

No model_response artifact writes into a store another subdomain owns.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 7 — Design Intent | p7_design_intent_clm_model_response_v0.md | GATE 1 APPROVED |
| Stage 8 — Authoring Mandate | This document | PENDING GATE 2 APPROVAL |
| Artifact Authoring | per build_order | PENDING |
