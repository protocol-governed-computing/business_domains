# Stage 7 — Design Intent: causal_language_model / model_response

**Stage:** 7 — Design Intent
**CR:** cr_02_hosted_model
**Status:** DRAFT
**Feeds:** Stage 8 — Authoring Mandate

Every binding names a field the capability declares, read from the pinned baseline
`b8dd7145232e48f29575a00a5f056ba68930e1a34a7cf8aae5e3e6b23a02f1ef`.

The hosted way is three acts beside the test model's, which is not touched. The host drives them: it
begins a request on the requester's behalf, offers the model's candidates one step at a time, and asks
for release. The business chooses, records and releases. A hosted request's record trail is its state:
an opening entry at admission, a step entry per offer, and a closing entry on release or refusal.

---

## 1. Design Decisions Resolution

<!-- register:design_resolution optional -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|
| One act per step, driven by the host | The host proposes; the business chooses | Three workflows: begin, offer, release. The host calls them; nothing in them calls the host | S4 design_decisions #1 |
| Admission is the test model's | A hosted request is admitted under the same conditions | The begin act runs the four admission contracts and the reading check of the test model's way, unchanged and in the same order | S4 design_decisions #2 |
| The reported size is checked with each offer | The host counts what the model reads once it has it | The offer act compares the size the host reports with the capacity recorded at admission before anything is chosen, and records the report with the step | S4 design_decisions #3 |
| The trail is the state | One truth for a hosted request; an abandoned one stays visible | The opening entry holds what the model reads, the rules in force, the limits and the admitted fingerprint; each offer reads the trail and reduces it to the response as built; the existing record closes it | S4 design_decisions #4 |
| Tokens are joined as they are | A pattern split across tokens is not written | A new choice transform applies the test model's stopping and choosing to the text as built, with the permitted length | S4 design_decisions #5 |
| The permitted length is the smaller limit | The registered maximum and the rules' longest response both bind | The opening entry keeps both; the reduced state carries the smaller, and a token chosen at it that does not end the response refuses the request as unfinished | S4 design_decisions #6 |
| The fingerprint is compared at every step | An offer for another model is refused; the host is not authenticated | The offer act confirms the offered fingerprint is the admitted model's before choosing | S4 design_decisions #7 |
| Release closes the record with the business's text | The host never supplies what is released | The release act reads the trail, confirms the response complete, and records it with the text the trail holds | S4 design_decisions #8 |
| Grounding is a rule of the time in service | A time in service may require every number to be one the model read | The opening entry carries the stored rules' grounding beside the rules in force; the choice stops a number no number in the reading begins, or ends one that is not in it | S4 design_decisions #9 |
| A number's beginning is judged, and its lookalikes | A pattern judged only when complete lets its beginning through | The choice judges the compatibility form of the text, and stops the first digit of a forbidden number the model read unless it could still be a permitted one | S4 design_decisions #10 |

---

## 2. Artifact Inventory — Existing Artifacts

<!-- register:existing_inventory -->
| FQDN | Action (REPLACE, REUSE, EXTEND, REVIEW) | Summary | Reason | Source Finding |
|------|-----------------------------------------|---------|--------|----------------|
| capability_side_effects::CS_APPENDONLY_JSONL_V0 | REUSE |  | Appends every entry of a hosted request's trail and reads the trail back. | S6 pps_artifacts_requiring_action causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0 |
| capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | REUSE |  | Assembles the opening and step entries of a hosted request's trail. | S6 pps_artifacts_requiring_action causal_language_model::CC_RECORD_USER_PROMPT_V0 |
| capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | REUSE |  | Confirms the reported reading size against the capacity. | S6 pps_artifacts_requiring_action causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0 |
| capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 | REUSE |  | Confirms an offer names the admitted model's fingerprint. | S6 pps_artifacts_requiring_action causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0 |
| causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0 | REUSE |  | Reused unchanged by the hosted acts. | S6 pps_artifacts_requiring_action causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0 |
| causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0 | REUSE |  | Reused unchanged by the hosted acts. | S6 pps_artifacts_requiring_action causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0 |
| causal_language_model::CC_ADMIT_USER_PROMPT_V0 | REUSE |  | Reused unchanged by the hosted acts. | S6 pps_artifacts_requiring_action causal_language_model::CC_ADMIT_USER_PROMPT_V0 |
| causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 | REUSE |  | Reused unchanged by the hosted acts. | S6 pps_artifacts_requiring_action causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 |
| causal_language_model::CC_CONFIRM_READING_FITS_V0 | REUSE |  | Reused unchanged by the hosted acts. | S6 pps_artifacts_requiring_action causal_language_model::CC_CONFIRM_READING_FITS_V0 |
| causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0 | REUSE |  | Reused unchanged by the hosted acts. | S6 pps_artifacts_requiring_action causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0 |
| causal_language_model::CC_RECORD_USER_PROMPT_V0 | REUSE |  | Reused unchanged by the hosted acts. | S6 pps_artifacts_requiring_action causal_language_model::CC_RECORD_USER_PROMPT_V0 |
| causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0 | REUSE |  | Forms the rules in force when a hosted request's record opens. | S6 pps_artifacts_requiring_action causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0 |
| causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0 | REUSE |  | Binds the hosted acts to the subdomain's stores, as it binds the test model's. | S6 pps_artifacts_requiring_action causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0 |
| causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0 | REUSE |  | Declares the user prompt records the trail is kept in. | S6 pps_artifacts_requiring_action causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0 |
| causal_language_model::AC_REQUESTER_V0 | REUSE |  | The requester a hosted request is begun for. | S6 pps_artifacts_requiring_action causal_language_model::AC_REQUESTER_V0 |
| causal_language_model::EV_USER_PROMPT_RESPONDED_V0 | REUSE |  | Announced when a hosted response is released. | S6 pps_artifacts_requiring_action causal_language_model::EV_USER_PROMPT_RESPONDED_V0 |
| causal_language_model::EV_USER_PROMPT_REFUSED_V0 | REUSE |  | Announced when a hosted request is refused. | S6 pps_artifacts_requiring_action causal_language_model::EV_USER_PROMPT_REFUSED_V0 |

---

## 3. Artifact Family Mapping — New Artifacts

<!-- register:new_artifacts business_language=capability -->
| Capability | Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE) | Code | Summary | Owner Subdomain | Status | Source Finding |
|------------|---------------------------------------------------------------|------|---------|-----------------|--------|----------------|
| The host of a model in service, which proposes and holds no authority | AC | causal_language_model::AC_MODEL_HOST_V0 | The host of a model in service, which proposes and holds no authority | model_response | NEW | S5 provisional_codes AC_MODEL_HOST_V0 |
| A request to a hosted model on behalf of a customer | IN | causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0 | A request to a hosted model on behalf of a customer | model_response | NEW | S5 provisional_codes IN_BEGIN_HOSTED_RESPONSE_V0 |
| The candidates a hosted model could write next, naming its fingerprint | IN | causal_language_model::IN_OFFER_NEXT_TOKENS_V0 | The candidates a hosted model could write next, naming its fingerprint and the size of what it reads | model_response | NEW | S5 provisional_codes IN_OFFER_NEXT_TOKENS_V0 |
| A request to release a completed hosted response | IN | causal_language_model::IN_RELEASE_HOSTED_RESPONSE_V0 | A request to release a completed hosted response | model_response | NEW | S5 provisional_codes IN_RELEASE_HOSTED_RESPONSE_V0 |
| Admitting a hosted request and opening its record, or refusing it | WF | causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | Admitting a hosted request and opening its record, or refusing it | model_response | NEW | S5 provisional_codes WF_BEGIN_HOSTED_RESPONSE_V0 |
| Choosing a permitted token from an offer and recording the step, or refusing the request | WF | causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | Choosing a permitted token from an offer and recording the step, or refusing the request | model_response | NEW | S5 provisional_codes WF_OFFER_NEXT_TOKENS_V0 |
| Releasing a completed hosted response from the record | WF | causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0 | Releasing a completed hosted response from the record | model_response | NEW | S5 provisional_codes WF_RELEASE_HOSTED_RESPONSE_V0 |
| Refuse an offer whose reported reading size exceeds the model's capacity | CC | causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0 | Refuse an offer whose reported reading size exceeds the model's capacity | model_response | NEW | S5 provisional_codes CC_CONFIRM_HOSTED_READING_FITS_V0 |
| Form the rules in force and open the record of a hosted request | CC | causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | Form the rules in force and open the record of a hosted request | model_response | NEW | S5 provisional_codes CC_OPEN_HOSTED_RECORD_V0 |
| Read a hosted request's trail and reduce it to the response as built | CC | causal_language_model::CC_READ_HOSTED_STATE_V0 | Read a hosted request's trail and reduce it to the response as built | model_response | NEW | S5 provisional_codes CC_READ_HOSTED_STATE_V0 |
| Refuse an offer naming another model's fingerprint | CC | causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0 | Refuse an offer naming another model's fingerprint | model_response | NEW | S5 provisional_codes CC_CONFIRM_OFFER_FOR_MODEL_V0 |
| Choose a permitted token from an offer under the rules in force | CC | causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0 | Choose a permitted token from an offer under the rules in force | model_response | NEW | S5 provisional_codes CC_CHOOSE_PERMITTED_TOKEN_V0 |
| Record an offer and the choice made from it in the request's trail | CC | causal_language_model::CC_RECORD_HOSTED_STEP_V0 | Record an offer and the choice made from it in the request's trail | model_response | NEW | S5 provisional_codes CC_RECORD_HOSTED_STEP_V0 |
| Reduce a hosted request's trail to its state | CT | causal_language_model::CT_PURE_READ_HOSTED_STATE_V0 | Reduces a hosted request's trail to the response as built, its position, whether it is complete, and its permitted length | model_response | NEW | S5 provisional_codes CT_PURE_READ_HOSTED_STATE_V0 |
| Stop forbidden tokens and choose a permitted one | CT | causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | Stops forbidden tokens among those offered and chooses one permitted token, joined as it is, within the permitted length | model_response | NEW | S5 provisional_codes CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 |

---

## 4. Runtime Binding (RB) Declarations

<!-- register:rb_declarations -->
| RB Code | Binds WF | CS Bindings | Storage Structure | Source Finding |
|---------|----------|-------------|-------------------|----------------|
| causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0 | causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0 | S6 pps_artifacts_requiring_action causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0 |
| causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0 | causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0 | S6 pps_artifacts_requiring_action causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0 |
| causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0 | causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0 | S6 pps_artifacts_requiring_action causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0 |

---

## 5. Execution Topology

Every refusal is recorded before the act ends: the existing recording contract runs at one place per
refusal, each handed its outcome and reason. In the offer act, a step the rules or the length stopped
is recorded first, so the trail keeps the offer that ended the request; the step recording contract
runs at three places for that. The releasability contract runs at two places in the offer act and one
in the release act, each with its own condition.

<!-- register:execution_topology optional_columns=runs -->
| Workflow | Node | Runs | Node Type (IN, CC, EXIT, EXIT_SUCCESS) | Routing | Source Finding |
|----------|------|------|----------------------------------------|---------|----------------|
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0 |  | IN | ACK -> causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_BEGIN_HOSTED_RESPONSE_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0 |  | CC | SUCCESS -> causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_CLAIM_USER_PROMPT_IDENTITY_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0 |  | CC | SUCCESS -> causal_language_model::CC_ADMIT_USER_PROMPT_V0; VIOLATION -> RECORD_REFUSED_NOT_PERMITTED | S7 new_artifacts CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | causal_language_model::CC_ADMIT_USER_PROMPT_V0 |  | CC | SUCCESS -> causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0; NOT_FOUND -> RECORD_REFUSED_NOT_REGISTERED; VIOLATION -> RECORD_REFUSED_NOT_IN_SERVICE; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_ADMIT_USER_PROMPT_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 |  | CC | SUCCESS -> causal_language_model::CC_CONFIRM_READING_FITS_V0; NOT_FOUND -> RECORD_REFUSED_NOT_IN_SERVICE; VIOLATION -> RECORD_REFUSED_ABOVE_CEILING; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_CONFIRM_WITHIN_CEILING_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | causal_language_model::CC_CONFIRM_READING_FITS_V0 |  | CC | SUCCESS -> causal_language_model::CC_OPEN_HOSTED_RECORD_V0; VIOLATION -> RECORD_REFUSED_TOO_LONG_TO_READ | S7 new_artifacts CC_CONFIRM_READING_FITS_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | causal_language_model::CC_OPEN_HOSTED_RECORD_V0 |  | CC | SUCCESS -> EXIT_WRITING; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_OPEN_HOSTED_RECORD_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_NOT_PERMITTED | causal_language_model::CC_RECORD_USER_PROMPT_V0 | CC | SUCCESS -> EXIT_REFUSED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_RECORD_USER_PROMPT_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_NOT_REGISTERED | causal_language_model::CC_RECORD_USER_PROMPT_V0 | CC | SUCCESS -> EXIT_REFUSED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_RECORD_USER_PROMPT_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_NOT_IN_SERVICE | causal_language_model::CC_RECORD_USER_PROMPT_V0 | CC | SUCCESS -> EXIT_REFUSED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_RECORD_USER_PROMPT_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_ABOVE_CEILING | causal_language_model::CC_RECORD_USER_PROMPT_V0 | CC | SUCCESS -> EXIT_REFUSED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_RECORD_USER_PROMPT_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | causal_language_model::CC_RECORD_USER_PROMPT_V0 | CC | SUCCESS -> EXIT_REFUSED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_RECORD_USER_PROMPT_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | EXIT_WRITING |  | EXIT_SUCCESS | — | S7 execution_topology WF_BEGIN_HOSTED_RESPONSE_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | EXIT_REFUSED |  | EXIT | — | S7 execution_topology WF_BEGIN_HOSTED_RESPONSE_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | EXIT_REJECTED |  | EXIT | — | S7 execution_topology WF_BEGIN_HOSTED_RESPONSE_V0 |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | causal_language_model::IN_OFFER_NEXT_TOKENS_V0 |  | IN | ACK -> causal_language_model::CC_READ_HOSTED_STATE_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_OFFER_NEXT_TOKENS_V0 |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | causal_language_model::CC_READ_HOSTED_STATE_V0 |  | CC | SUCCESS -> causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_READ_HOSTED_STATE_V0 |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0 |  | CC | SUCCESS -> causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0; VIOLATION -> RECORD_REFUSED_OTHER_MODEL | S7 new_artifacts CC_CONFIRM_OFFER_FOR_MODEL_V0 |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0 |  | CC | SUCCESS -> causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0; VIOLATION -> RECORD_REFUSED_TOO_LONG_TO_READ | S7 new_artifacts CC_CONFIRM_HOSTED_READING_FITS_V0 |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0 |  | CC | SUCCESS -> CONFIRM_NO_RULE_STOPPED; VIOLATION -> EXIT_REJECTED | S7 new_artifacts CC_CHOOSE_PERMITTED_TOKEN_V0 |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | CONFIRM_NO_RULE_STOPPED | causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0 | CC | SUCCESS -> CONFIRM_WITHIN_LENGTH; VIOLATION -> RECORD_STOPPED_STEP | S7 new_artifacts CC_CONFIRM_RESPONSE_RELEASABLE_V0 |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | CONFIRM_WITHIN_LENGTH | causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0 | CC | SUCCESS -> RECORD_STEP; VIOLATION -> RECORD_UNFINISHED_STEP | S7 new_artifacts CC_CONFIRM_RESPONSE_RELEASABLE_V0 |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_STEP | causal_language_model::CC_RECORD_HOSTED_STEP_V0 | CC | SUCCESS -> EXIT_CHOSEN; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_RECORD_HOSTED_STEP_V0 |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_STOPPED_STEP | causal_language_model::CC_RECORD_HOSTED_STEP_V0 | CC | SUCCESS -> RECORD_REFUSED_BY_RULE; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_RECORD_HOSTED_STEP_V0 |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_UNFINISHED_STEP | causal_language_model::CC_RECORD_HOSTED_STEP_V0 | CC | SUCCESS -> RECORD_REFUSED_UNFINISHED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_RECORD_HOSTED_STEP_V0 |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_OTHER_MODEL | causal_language_model::CC_RECORD_USER_PROMPT_V0 | CC | SUCCESS -> EXIT_REFUSED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_RECORD_USER_PROMPT_V0 |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | causal_language_model::CC_RECORD_USER_PROMPT_V0 | CC | SUCCESS -> EXIT_REFUSED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_RECORD_USER_PROMPT_V0 |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_BY_RULE | causal_language_model::CC_RECORD_USER_PROMPT_V0 | CC | SUCCESS -> EXIT_REFUSED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_RECORD_USER_PROMPT_V0 |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_UNFINISHED | causal_language_model::CC_RECORD_USER_PROMPT_V0 | CC | SUCCESS -> EXIT_REFUSED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_RECORD_USER_PROMPT_V0 |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | EXIT_CHOSEN |  | EXIT_SUCCESS | — | S7 execution_topology WF_OFFER_NEXT_TOKENS_V0 |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | EXIT_REFUSED |  | EXIT | — | S7 execution_topology WF_OFFER_NEXT_TOKENS_V0 |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | EXIT_REJECTED |  | EXIT | — | S7 execution_topology WF_OFFER_NEXT_TOKENS_V0 |
| causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0 | causal_language_model::IN_RELEASE_HOSTED_RESPONSE_V0 |  | IN | ACK -> causal_language_model::CC_READ_HOSTED_STATE_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_RELEASE_HOSTED_RESPONSE_V0 |
| causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0 | causal_language_model::CC_READ_HOSTED_STATE_V0 |  | CC | SUCCESS -> CONFIRM_FINISHED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_READ_HOSTED_STATE_V0 |
| causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0 | CONFIRM_FINISHED | causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0 | CC | SUCCESS -> RECORD_RESPONDED; VIOLATION -> EXIT_REJECTED | S7 new_artifacts CC_CONFIRM_RESPONSE_RELEASABLE_V0 |
| causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0 | RECORD_RESPONDED | causal_language_model::CC_RECORD_USER_PROMPT_V0 | CC | SUCCESS -> EXIT_RESPONDED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_RECORD_USER_PROMPT_V0 |
| causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0 | EXIT_RESPONDED |  | EXIT_SUCCESS | — | S7 execution_topology WF_RELEASE_HOSTED_RESPONSE_V0 |
| causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0 | EXIT_REJECTED |  | EXIT | — | S7 execution_topology WF_RELEASE_HOSTED_RESPONSE_V0 |

---

## 6. Capability Composition

<!-- register:cc_composition optional -->
| CC Code | Step | Step Name | Capability | Kind (CT, CS) | Operation | Store | Consumes | Produces | Routing | Interpreted By | Semantic Status | Interface |
|---------|------|-----------|------------|---------------|-----------|-------|----------|----------|---------|----------------|-----------------|-----------|
| causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0 | 1 | confirm_reported_reading_fits | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | CT | VALIDATE_PARAMETER_RULES | — | reported_reading_size, reading_capacity | reading_fits | SUCCESS -> exit; VIOLATION -> exit | — | SUCCESS | in: parameters=reported_reading_size, rules=reading_capacity; out: valid=reading_fits |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | 1 | form_rules_in_force | causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0 | CT | FORM_RESPONSE_RULES | — | response_rules, account_numbers, seed | rules_in_force, positions | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: response_rules=response_rules, account_numbers=account_numbers, seed=seed; out: rules_in_force=rules_in_force, positions=positions |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | 2 | assemble_opening_record | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | CT | ASSEMBLE_RECORD | — | user_prompt_id, requester_id, customer_id, identity_key, kind, question, supporting_material, time_in_service_id, reading, fingerprint, reading_capacity, maximum_response_length, response_rules | opening_record | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: fields=opening_fields; out: record=opening_record |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | 3 | append_opening_record | capability_side_effects::CS_APPENDONLY_JSONL_V0 | CS | APPEND | USER_PROMPT_RECORDS | record, stream_id, actor_id | record_id, sequence_number | SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | — |
| causal_language_model::CC_READ_HOSTED_STATE_V0 | 1 | read_trail | capability_side_effects::CS_APPENDONLY_JSONL_V0 | CS | GET_ALL | USER_PROMPT_RECORDS | stream_id | entries | SUCCESS -> continue; BACKEND_ERROR -> exit | — | SUCCESS | — |
| causal_language_model::CC_READ_HOSTED_STATE_V0 | 2 | reduce_trail | causal_language_model::CT_PURE_READ_HOSTED_STATE_V0 | CT | READ_HOSTED_STATE | — | entries | state | SUCCESS -> exit; VIOLATION -> exit | — | SUCCESS | in: entries=entries; out: state=state |
| causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0 | 1 | confirm_same_model | capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 | CT | VALIDATE_SET_MEMBERSHIP | — | offered_fingerprint, admitted_fingerprint | offer_for_model | SUCCESS -> exit; VIOLATION -> exit | — | SUCCESS | in: value=offered_fingerprint, allowed_set=admitted_fingerprint; out: is_member=offer_for_model |
| causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0 | 1 | choose_token | causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | CT | CHOOSE_PERMITTED_TOKEN | — | state, candidates | step, text, finished, stopped_by, within_length | SUCCESS -> exit; VIOLATION -> exit | — | SUCCESS | in: state=state, candidates=candidates; out: step=step, text=text, finished=finished, stopped_by=stopped_by, within_length=within_length |
| causal_language_model::CC_RECORD_HOSTED_STEP_V0 | 1 | assemble_step_record | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | CT | ASSEMBLE_RECORD | — | user_prompt_id, host_id, fingerprint, reported_reading_size, step | step_record | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: fields=step_fields; out: record=step_record |
| causal_language_model::CC_RECORD_HOSTED_STEP_V0 | 2 | append_step_record | capability_side_effects::CS_APPENDONLY_JSONL_V0 | CS | APPEND | USER_PROMPT_RECORDS | record, stream_id, actor_id | record_id, sequence_number | SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | — |

---

## 7. Step Bindings

<!-- register:step_bindings optional -->
| Owner | Step | Direction (INPUT, OUTPUT) | Field | Bound To | Source Finding |
|-------|------|---------------------------|-------|----------|----------------|
| causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0 | confirm_reported_reading_fits | INPUT | parameters | {'reported_reading_size': '$.inputs.reported_reading_size'} | S7 cc_composition confirm_reported_reading_fits |
| causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0 | confirm_reported_reading_fits | INPUT | rules | [{'field': 'reported_reading_size', 'op': 'lte', 'value': '$.inputs.reading_capacity'}] | S7 cc_composition confirm_reported_reading_fits |
| causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0 | confirm_reported_reading_fits | OUTPUT | reading_fits | capability_result.valid | S7 cc_composition confirm_reported_reading_fits |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | form_rules_in_force | INPUT | response_rules | inputs.response_rules | S7 cc_composition form_rules_in_force |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | form_rules_in_force | INPUT | account_numbers | inputs.account_numbers | S7 cc_composition form_rules_in_force |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | form_rules_in_force | INPUT | seed | inputs.seed | S7 cc_composition form_rules_in_force |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | form_rules_in_force | OUTPUT | rules_in_force | capability_result.rules_in_force | S7 cc_composition form_rules_in_force |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | form_rules_in_force | OUTPUT | positions | capability_result.positions | S7 cc_composition form_rules_in_force |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | assemble_opening_record | INPUT | fields | {'user_prompt_id': '$.inputs.user_prompt_id', 'requester_id': '$.inputs.requester_id', 'customer_id': '$.inputs.customer_id', 'identity_key': '$.inputs.identity_key', 'kind': '$.inputs.kind', 'question': '$.inputs.question', 'supporting_material': '$.inputs.supporting_material', 'time_in_service_id': '$.inputs.time_in_service_id', 'reading': '$.inputs.reading', 'fingerprint': '$.inputs.fingerprint', 'reading_capacity': '$.inputs.reading_capacity', 'maximum_response_length': '$.inputs.maximum_response_length', 'rules_in_force': '$.results.form_rules_in_force.rules_in_force', 'ground_numbers': '$.inputs.response_rules.ground_numbers', 'longest_response': '$.inputs.response_rules.longest_response', 'outcome': 'WRITING'} | S7 cc_composition assemble_opening_record |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | assemble_opening_record | OUTPUT | opening_record | capability_result.record | S7 cc_composition assemble_opening_record |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | append_opening_record | INPUT | record | results.assemble_opening_record.opening_record | S7 cc_composition append_opening_record |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | append_opening_record | INPUT | stream_id | inputs.user_prompt_id | S7 cc_composition append_opening_record |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | append_opening_record | INPUT | actor_id | inputs.requester_id | S7 cc_composition append_opening_record |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | append_opening_record | OUTPUT | record_id | capability_result.record_id | S7 cc_composition append_opening_record |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | append_opening_record | OUTPUT | sequence_number | capability_result.sequence_number | S7 cc_composition append_opening_record |
| causal_language_model::CC_READ_HOSTED_STATE_V0 | read_trail | INPUT | stream_id | inputs.user_prompt_id | S7 cc_composition read_trail |
| causal_language_model::CC_READ_HOSTED_STATE_V0 | read_trail | OUTPUT | entries | capability_result.entries | S7 cc_composition read_trail |
| causal_language_model::CC_READ_HOSTED_STATE_V0 | read_trail | OUTPUT | result_status | result_status | S7 cc_composition read_trail |
| causal_language_model::CC_READ_HOSTED_STATE_V0 | reduce_trail | INPUT | entries | results.read_trail.entries | S7 cc_composition reduce_trail |
| causal_language_model::CC_READ_HOSTED_STATE_V0 | reduce_trail | OUTPUT | state | capability_result.state | S7 cc_composition reduce_trail |
| causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0 | confirm_same_model | INPUT | value | inputs.offered_fingerprint | S7 cc_composition confirm_same_model |
| causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0 | confirm_same_model | INPUT | allowed_set | ['$.inputs.admitted_fingerprint'] | S7 cc_composition confirm_same_model |
| causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0 | confirm_same_model | OUTPUT | offer_for_model | capability_result.is_member | S7 cc_composition confirm_same_model |
| causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0 | choose_token | INPUT | state | inputs.state | S7 cc_composition choose_token |
| causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0 | choose_token | INPUT | candidates | inputs.candidates | S7 cc_composition choose_token |
| causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0 | choose_token | OUTPUT | step | capability_result.step | S7 cc_composition choose_token |
| causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0 | choose_token | OUTPUT | text | capability_result.text | S7 cc_composition choose_token |
| causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0 | choose_token | OUTPUT | finished | capability_result.finished | S7 cc_composition choose_token |
| causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0 | choose_token | OUTPUT | stopped_by | capability_result.stopped_by | S7 cc_composition choose_token |
| causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0 | choose_token | OUTPUT | within_length | capability_result.within_length | S7 cc_composition choose_token |
| causal_language_model::CC_RECORD_HOSTED_STEP_V0 | assemble_step_record | INPUT | fields | {'user_prompt_id': '$.inputs.user_prompt_id', 'outcome': 'STEP', 'host_id': '$.inputs.host_id', 'fingerprint': '$.inputs.fingerprint', 'reported_reading_size': '$.inputs.reported_reading_size', 'position': '$.inputs.step.position', 'candidates': '$.inputs.step.candidates', 'chosen': '$.inputs.step.chosen', 'stopped': '$.inputs.step.stopped', 'stopped_by': '$.inputs.step.stopped_by', 'finished': '$.inputs.step.finished', 'within_length': '$.inputs.step.within_length'} | S7 cc_composition assemble_step_record |
| causal_language_model::CC_RECORD_HOSTED_STEP_V0 | assemble_step_record | OUTPUT | step_record | capability_result.record | S7 cc_composition assemble_step_record |
| causal_language_model::CC_RECORD_HOSTED_STEP_V0 | append_step_record | INPUT | record | results.assemble_step_record.step_record | S7 cc_composition append_step_record |
| causal_language_model::CC_RECORD_HOSTED_STEP_V0 | append_step_record | INPUT | stream_id | inputs.user_prompt_id | S7 cc_composition append_step_record |
| causal_language_model::CC_RECORD_HOSTED_STEP_V0 | append_step_record | INPUT | actor_id | inputs.host_id | S7 cc_composition append_step_record |
| causal_language_model::CC_RECORD_HOSTED_STEP_V0 | append_step_record | OUTPUT | record_id | capability_result.record_id | S7 cc_composition append_step_record |
| causal_language_model::CC_RECORD_HOSTED_STEP_V0 | append_step_record | OUTPUT | sequence_number | capability_result.sequence_number | S7 cc_composition append_step_record |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0 | INPUT | user_prompt_id | payload.user_prompt_id | S7 execution_topology CC_CLAIM_USER_PROMPT_IDENTITY_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0 | INPUT | customer_id | payload.customer_id | S7 execution_topology CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0 | INPUT | permitted_customers | payload.permitted_customers | S7 execution_topology CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | causal_language_model::CC_ADMIT_USER_PROMPT_V0 | INPUT | identity_key | payload.identity_key | S7 execution_topology CC_ADMIT_USER_PROMPT_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 | INPUT | time_in_service_id | results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id | S7 execution_topology CC_CONFIRM_WITHIN_CEILING_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 | INPUT | kind | payload.kind | S7 execution_topology CC_CONFIRM_WITHIN_CEILING_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | causal_language_model::CC_CONFIRM_READING_FITS_V0 | INPUT | system_prompt | results.CC_CONFIRM_WITHIN_CEILING_V0.time_in_service.system_prompt | S7 execution_topology CC_CONFIRM_READING_FITS_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | causal_language_model::CC_CONFIRM_READING_FITS_V0 | INPUT | question | payload.question | S7 execution_topology CC_CONFIRM_READING_FITS_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | causal_language_model::CC_CONFIRM_READING_FITS_V0 | INPUT | supporting_material | payload.supporting_material | S7 execution_topology CC_CONFIRM_READING_FITS_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | causal_language_model::CC_CONFIRM_READING_FITS_V0 | INPUT | reading_capacity | results.CC_ADMIT_USER_PROMPT_V0.model_record.description.reading_capacity | S7 execution_topology CC_CONFIRM_READING_FITS_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | INPUT | user_prompt_id | payload.user_prompt_id | S7 execution_topology CC_OPEN_HOSTED_RECORD_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | INPUT | requester_id | payload.requester_id | S7 execution_topology CC_OPEN_HOSTED_RECORD_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | INPUT | customer_id | payload.customer_id | S7 execution_topology CC_OPEN_HOSTED_RECORD_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | INPUT | identity_key | payload.identity_key | S7 execution_topology CC_OPEN_HOSTED_RECORD_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | INPUT | kind | payload.kind | S7 execution_topology CC_OPEN_HOSTED_RECORD_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | INPUT | question | payload.question | S7 execution_topology CC_OPEN_HOSTED_RECORD_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | INPUT | supporting_material | payload.supporting_material | S7 execution_topology CC_OPEN_HOSTED_RECORD_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | INPUT | account_numbers | payload.account_numbers | S7 execution_topology CC_OPEN_HOSTED_RECORD_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | INPUT | seed | payload.seed | S7 execution_topology CC_OPEN_HOSTED_RECORD_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | INPUT | time_in_service_id | results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id | S7 execution_topology CC_OPEN_HOSTED_RECORD_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | INPUT | reading | results.CC_CONFIRM_READING_FITS_V0.reading | S7 execution_topology CC_OPEN_HOSTED_RECORD_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | INPUT | response_rules | results.CC_CONFIRM_WITHIN_CEILING_V0.time_in_service.response_rules | S7 execution_topology CC_OPEN_HOSTED_RECORD_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | INPUT | fingerprint | results.CC_ADMIT_USER_PROMPT_V0.model_record.fingerprint | S7 execution_topology CC_OPEN_HOSTED_RECORD_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | INPUT | reading_capacity | results.CC_ADMIT_USER_PROMPT_V0.model_record.description.reading_capacity | S7 execution_topology CC_OPEN_HOSTED_RECORD_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | INPUT | maximum_response_length | results.CC_ADMIT_USER_PROMPT_V0.model_record.description.maximum_response_length | S7 execution_topology CC_OPEN_HOSTED_RECORD_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_NOT_PERMITTED | INPUT | user_prompt_id | payload.user_prompt_id | S7 execution_topology RECORD_REFUSED_NOT_PERMITTED |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_NOT_PERMITTED | INPUT | requester_id | payload.requester_id | S7 execution_topology RECORD_REFUSED_NOT_PERMITTED |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_NOT_PERMITTED | INPUT | customer_id | payload.customer_id | S7 execution_topology RECORD_REFUSED_NOT_PERMITTED |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_NOT_PERMITTED | INPUT | identity_key | payload.identity_key | S7 execution_topology RECORD_REFUSED_NOT_PERMITTED |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_NOT_PERMITTED | INPUT | kind | payload.kind | S7 execution_topology RECORD_REFUSED_NOT_PERMITTED |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_NOT_PERMITTED | INPUT | question | payload.question | S7 execution_topology RECORD_REFUSED_NOT_PERMITTED |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_NOT_PERMITTED | INPUT | supporting_material | payload.supporting_material | S7 execution_topology RECORD_REFUSED_NOT_PERMITTED |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_NOT_PERMITTED | INPUT | outcome | REFUSED | S7 execution_topology RECORD_REFUSED_NOT_PERMITTED |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_NOT_PERMITTED | INPUT | reason | requester_not_permitted_for_customer | S7 execution_topology RECORD_REFUSED_NOT_PERMITTED |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_NOT_REGISTERED | INPUT | user_prompt_id | payload.user_prompt_id | S7 execution_topology RECORD_REFUSED_NOT_REGISTERED |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_NOT_REGISTERED | INPUT | requester_id | payload.requester_id | S7 execution_topology RECORD_REFUSED_NOT_REGISTERED |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_NOT_REGISTERED | INPUT | customer_id | payload.customer_id | S7 execution_topology RECORD_REFUSED_NOT_REGISTERED |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_NOT_REGISTERED | INPUT | identity_key | payload.identity_key | S7 execution_topology RECORD_REFUSED_NOT_REGISTERED |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_NOT_REGISTERED | INPUT | kind | payload.kind | S7 execution_topology RECORD_REFUSED_NOT_REGISTERED |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_NOT_REGISTERED | INPUT | question | payload.question | S7 execution_topology RECORD_REFUSED_NOT_REGISTERED |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_NOT_REGISTERED | INPUT | supporting_material | payload.supporting_material | S7 execution_topology RECORD_REFUSED_NOT_REGISTERED |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_NOT_REGISTERED | INPUT | outcome | REFUSED | S7 execution_topology RECORD_REFUSED_NOT_REGISTERED |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_NOT_REGISTERED | INPUT | reason | model_not_registered | S7 execution_topology RECORD_REFUSED_NOT_REGISTERED |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_NOT_IN_SERVICE | INPUT | user_prompt_id | payload.user_prompt_id | S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_NOT_IN_SERVICE | INPUT | requester_id | payload.requester_id | S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_NOT_IN_SERVICE | INPUT | customer_id | payload.customer_id | S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_NOT_IN_SERVICE | INPUT | identity_key | payload.identity_key | S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_NOT_IN_SERVICE | INPUT | kind | payload.kind | S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_NOT_IN_SERVICE | INPUT | question | payload.question | S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_NOT_IN_SERVICE | INPUT | supporting_material | payload.supporting_material | S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_NOT_IN_SERVICE | INPUT | outcome | REFUSED | S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_NOT_IN_SERVICE | INPUT | reason | model_not_in_service | S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_ABOVE_CEILING | INPUT | user_prompt_id | payload.user_prompt_id | S7 execution_topology RECORD_REFUSED_ABOVE_CEILING |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_ABOVE_CEILING | INPUT | requester_id | payload.requester_id | S7 execution_topology RECORD_REFUSED_ABOVE_CEILING |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_ABOVE_CEILING | INPUT | customer_id | payload.customer_id | S7 execution_topology RECORD_REFUSED_ABOVE_CEILING |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_ABOVE_CEILING | INPUT | identity_key | payload.identity_key | S7 execution_topology RECORD_REFUSED_ABOVE_CEILING |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_ABOVE_CEILING | INPUT | kind | payload.kind | S7 execution_topology RECORD_REFUSED_ABOVE_CEILING |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_ABOVE_CEILING | INPUT | question | payload.question | S7 execution_topology RECORD_REFUSED_ABOVE_CEILING |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_ABOVE_CEILING | INPUT | supporting_material | payload.supporting_material | S7 execution_topology RECORD_REFUSED_ABOVE_CEILING |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_ABOVE_CEILING | INPUT | time_in_service_id | results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id | S7 execution_topology RECORD_REFUSED_ABOVE_CEILING |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_ABOVE_CEILING | INPUT | outcome | REFUSED | S7 execution_topology RECORD_REFUSED_ABOVE_CEILING |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_ABOVE_CEILING | INPUT | reason | kind_above_sensitivity_ceiling | S7 execution_topology RECORD_REFUSED_ABOVE_CEILING |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | INPUT | user_prompt_id | payload.user_prompt_id | S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | INPUT | requester_id | payload.requester_id | S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | INPUT | customer_id | payload.customer_id | S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | INPUT | identity_key | payload.identity_key | S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | INPUT | kind | payload.kind | S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | INPUT | question | payload.question | S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | INPUT | supporting_material | payload.supporting_material | S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | INPUT | time_in_service_id | results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id | S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | INPUT | outcome | REFUSED | S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | INPUT | reason | reading_longer_than_model_can_read | S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | causal_language_model::CC_READ_HOSTED_STATE_V0 | INPUT | user_prompt_id | payload.user_prompt_id | S7 execution_topology CC_READ_HOSTED_STATE_V0 |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0 | INPUT | offered_fingerprint | payload.fingerprint | S7 execution_topology CC_CONFIRM_OFFER_FOR_MODEL_V0 |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0 | INPUT | admitted_fingerprint | results.CC_READ_HOSTED_STATE_V0.state.opening.fingerprint | S7 execution_topology CC_CONFIRM_OFFER_FOR_MODEL_V0 |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0 | INPUT | reported_reading_size | payload.reported_reading_size | S7 execution_topology CC_CONFIRM_HOSTED_READING_FITS_V0 |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0 | INPUT | reading_capacity | results.CC_READ_HOSTED_STATE_V0.state.opening.reading_capacity | S7 execution_topology CC_CONFIRM_HOSTED_READING_FITS_V0 |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0 | INPUT | state | results.CC_READ_HOSTED_STATE_V0.state | S7 execution_topology CC_CHOOSE_PERMITTED_TOKEN_V0 |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0 | INPUT | candidates | payload.candidates | S7 execution_topology CC_CHOOSE_PERMITTED_TOKEN_V0 |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | CONFIRM_NO_RULE_STOPPED | INPUT | release_facts | {'stopped_by': '$.results.CC_CHOOSE_PERMITTED_TOKEN_V0.stopped_by'} | S7 execution_topology CONFIRM_NO_RULE_STOPPED |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | CONFIRM_NO_RULE_STOPPED | INPUT | release_rules | [{'field': 'stopped_by', 'op': 'eq', 'value': 'none'}] | S7 execution_topology CONFIRM_NO_RULE_STOPPED |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | CONFIRM_WITHIN_LENGTH | INPUT | release_facts | {'within_length': '$.results.CC_CHOOSE_PERMITTED_TOKEN_V0.within_length'} | S7 execution_topology CONFIRM_WITHIN_LENGTH |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | CONFIRM_WITHIN_LENGTH | INPUT | release_rules | [{'field': 'within_length', 'op': 'eq', 'value': True}] | S7 execution_topology CONFIRM_WITHIN_LENGTH |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_STEP | INPUT | user_prompt_id | payload.user_prompt_id | S7 execution_topology RECORD_STEP |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_STEP | INPUT | host_id | payload.host_id | S7 execution_topology RECORD_STEP |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_STEP | INPUT | fingerprint | payload.fingerprint | S7 execution_topology RECORD_STEP |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_STEP | INPUT | reported_reading_size | payload.reported_reading_size | S7 execution_topology RECORD_STEP |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_STEP | INPUT | step | results.CC_CHOOSE_PERMITTED_TOKEN_V0.step | S7 execution_topology RECORD_STEP |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_STOPPED_STEP | INPUT | user_prompt_id | payload.user_prompt_id | S7 execution_topology RECORD_STOPPED_STEP |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_STOPPED_STEP | INPUT | host_id | payload.host_id | S7 execution_topology RECORD_STOPPED_STEP |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_STOPPED_STEP | INPUT | fingerprint | payload.fingerprint | S7 execution_topology RECORD_STOPPED_STEP |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_STOPPED_STEP | INPUT | reported_reading_size | payload.reported_reading_size | S7 execution_topology RECORD_STOPPED_STEP |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_STOPPED_STEP | INPUT | step | results.CC_CHOOSE_PERMITTED_TOKEN_V0.step | S7 execution_topology RECORD_STOPPED_STEP |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_UNFINISHED_STEP | INPUT | user_prompt_id | payload.user_prompt_id | S7 execution_topology RECORD_UNFINISHED_STEP |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_UNFINISHED_STEP | INPUT | host_id | payload.host_id | S7 execution_topology RECORD_UNFINISHED_STEP |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_UNFINISHED_STEP | INPUT | fingerprint | payload.fingerprint | S7 execution_topology RECORD_UNFINISHED_STEP |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_UNFINISHED_STEP | INPUT | reported_reading_size | payload.reported_reading_size | S7 execution_topology RECORD_UNFINISHED_STEP |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_UNFINISHED_STEP | INPUT | step | results.CC_CHOOSE_PERMITTED_TOKEN_V0.step | S7 execution_topology RECORD_UNFINISHED_STEP |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_OTHER_MODEL | INPUT | user_prompt_id | payload.user_prompt_id | S7 execution_topology RECORD_REFUSED_OTHER_MODEL |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_OTHER_MODEL | INPUT | requester_id | results.CC_READ_HOSTED_STATE_V0.state.opening.requester_id | S7 execution_topology RECORD_REFUSED_OTHER_MODEL |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_OTHER_MODEL | INPUT | customer_id | results.CC_READ_HOSTED_STATE_V0.state.opening.customer_id | S7 execution_topology RECORD_REFUSED_OTHER_MODEL |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_OTHER_MODEL | INPUT | identity_key | results.CC_READ_HOSTED_STATE_V0.state.opening.identity_key | S7 execution_topology RECORD_REFUSED_OTHER_MODEL |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_OTHER_MODEL | INPUT | kind | results.CC_READ_HOSTED_STATE_V0.state.opening.kind | S7 execution_topology RECORD_REFUSED_OTHER_MODEL |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_OTHER_MODEL | INPUT | question | results.CC_READ_HOSTED_STATE_V0.state.opening.question | S7 execution_topology RECORD_REFUSED_OTHER_MODEL |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_OTHER_MODEL | INPUT | supporting_material | results.CC_READ_HOSTED_STATE_V0.state.opening.supporting_material | S7 execution_topology RECORD_REFUSED_OTHER_MODEL |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_OTHER_MODEL | INPUT | time_in_service_id | results.CC_READ_HOSTED_STATE_V0.state.opening.time_in_service_id | S7 execution_topology RECORD_REFUSED_OTHER_MODEL |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_OTHER_MODEL | INPUT | reading | results.CC_READ_HOSTED_STATE_V0.state.opening.reading | S7 execution_topology RECORD_REFUSED_OTHER_MODEL |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_OTHER_MODEL | INPUT | rules_in_force | results.CC_READ_HOSTED_STATE_V0.state.opening.rules_in_force | S7 execution_topology RECORD_REFUSED_OTHER_MODEL |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_OTHER_MODEL | INPUT | outcome | REFUSED | S7 execution_topology RECORD_REFUSED_OTHER_MODEL |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_OTHER_MODEL | INPUT | reason | offer_for_another_model | S7 execution_topology RECORD_REFUSED_OTHER_MODEL |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | INPUT | user_prompt_id | payload.user_prompt_id | S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | INPUT | requester_id | results.CC_READ_HOSTED_STATE_V0.state.opening.requester_id | S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | INPUT | customer_id | results.CC_READ_HOSTED_STATE_V0.state.opening.customer_id | S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | INPUT | identity_key | results.CC_READ_HOSTED_STATE_V0.state.opening.identity_key | S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | INPUT | kind | results.CC_READ_HOSTED_STATE_V0.state.opening.kind | S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | INPUT | question | results.CC_READ_HOSTED_STATE_V0.state.opening.question | S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | INPUT | supporting_material | results.CC_READ_HOSTED_STATE_V0.state.opening.supporting_material | S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | INPUT | time_in_service_id | results.CC_READ_HOSTED_STATE_V0.state.opening.time_in_service_id | S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | INPUT | reading | results.CC_READ_HOSTED_STATE_V0.state.opening.reading | S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | INPUT | rules_in_force | results.CC_READ_HOSTED_STATE_V0.state.opening.rules_in_force | S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | INPUT | outcome | REFUSED | S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | INPUT | reason | reading_longer_than_model_can_read | S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_BY_RULE | INPUT | user_prompt_id | payload.user_prompt_id | S7 execution_topology RECORD_REFUSED_BY_RULE |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_BY_RULE | INPUT | requester_id | results.CC_READ_HOSTED_STATE_V0.state.opening.requester_id | S7 execution_topology RECORD_REFUSED_BY_RULE |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_BY_RULE | INPUT | customer_id | results.CC_READ_HOSTED_STATE_V0.state.opening.customer_id | S7 execution_topology RECORD_REFUSED_BY_RULE |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_BY_RULE | INPUT | identity_key | results.CC_READ_HOSTED_STATE_V0.state.opening.identity_key | S7 execution_topology RECORD_REFUSED_BY_RULE |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_BY_RULE | INPUT | kind | results.CC_READ_HOSTED_STATE_V0.state.opening.kind | S7 execution_topology RECORD_REFUSED_BY_RULE |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_BY_RULE | INPUT | question | results.CC_READ_HOSTED_STATE_V0.state.opening.question | S7 execution_topology RECORD_REFUSED_BY_RULE |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_BY_RULE | INPUT | supporting_material | results.CC_READ_HOSTED_STATE_V0.state.opening.supporting_material | S7 execution_topology RECORD_REFUSED_BY_RULE |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_BY_RULE | INPUT | time_in_service_id | results.CC_READ_HOSTED_STATE_V0.state.opening.time_in_service_id | S7 execution_topology RECORD_REFUSED_BY_RULE |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_BY_RULE | INPUT | reading | results.CC_READ_HOSTED_STATE_V0.state.opening.reading | S7 execution_topology RECORD_REFUSED_BY_RULE |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_BY_RULE | INPUT | rules_in_force | results.CC_READ_HOSTED_STATE_V0.state.opening.rules_in_force | S7 execution_topology RECORD_REFUSED_BY_RULE |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_BY_RULE | INPUT | outcome | REFUSED | S7 execution_topology RECORD_REFUSED_BY_RULE |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_BY_RULE | INPUT | reason | results.CC_CHOOSE_PERMITTED_TOKEN_V0.stopped_by | S7 execution_topology RECORD_REFUSED_BY_RULE |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_UNFINISHED | INPUT | user_prompt_id | payload.user_prompt_id | S7 execution_topology RECORD_REFUSED_UNFINISHED |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_UNFINISHED | INPUT | requester_id | results.CC_READ_HOSTED_STATE_V0.state.opening.requester_id | S7 execution_topology RECORD_REFUSED_UNFINISHED |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_UNFINISHED | INPUT | customer_id | results.CC_READ_HOSTED_STATE_V0.state.opening.customer_id | S7 execution_topology RECORD_REFUSED_UNFINISHED |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_UNFINISHED | INPUT | identity_key | results.CC_READ_HOSTED_STATE_V0.state.opening.identity_key | S7 execution_topology RECORD_REFUSED_UNFINISHED |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_UNFINISHED | INPUT | kind | results.CC_READ_HOSTED_STATE_V0.state.opening.kind | S7 execution_topology RECORD_REFUSED_UNFINISHED |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_UNFINISHED | INPUT | question | results.CC_READ_HOSTED_STATE_V0.state.opening.question | S7 execution_topology RECORD_REFUSED_UNFINISHED |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_UNFINISHED | INPUT | supporting_material | results.CC_READ_HOSTED_STATE_V0.state.opening.supporting_material | S7 execution_topology RECORD_REFUSED_UNFINISHED |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_UNFINISHED | INPUT | time_in_service_id | results.CC_READ_HOSTED_STATE_V0.state.opening.time_in_service_id | S7 execution_topology RECORD_REFUSED_UNFINISHED |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_UNFINISHED | INPUT | reading | results.CC_READ_HOSTED_STATE_V0.state.opening.reading | S7 execution_topology RECORD_REFUSED_UNFINISHED |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_UNFINISHED | INPUT | rules_in_force | results.CC_READ_HOSTED_STATE_V0.state.opening.rules_in_force | S7 execution_topology RECORD_REFUSED_UNFINISHED |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_UNFINISHED | INPUT | outcome | REFUSED | S7 execution_topology RECORD_REFUSED_UNFINISHED |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_UNFINISHED | INPUT | reason | longest_response_reached | S7 execution_topology RECORD_REFUSED_UNFINISHED |
| causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0 | causal_language_model::CC_READ_HOSTED_STATE_V0 | INPUT | user_prompt_id | payload.user_prompt_id | S7 execution_topology CC_READ_HOSTED_STATE_V0 |
| causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0 | CONFIRM_FINISHED | INPUT | release_facts | {'finished': '$.results.CC_READ_HOSTED_STATE_V0.state.finished'} | S7 execution_topology CONFIRM_FINISHED |
| causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0 | CONFIRM_FINISHED | INPUT | release_rules | [{'field': 'finished', 'op': 'eq', 'value': True}] | S7 execution_topology CONFIRM_FINISHED |
| causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0 | RECORD_RESPONDED | INPUT | user_prompt_id | payload.user_prompt_id | S7 execution_topology RECORD_RESPONDED |
| causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0 | RECORD_RESPONDED | INPUT | requester_id | results.CC_READ_HOSTED_STATE_V0.state.opening.requester_id | S7 execution_topology RECORD_RESPONDED |
| causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0 | RECORD_RESPONDED | INPUT | customer_id | results.CC_READ_HOSTED_STATE_V0.state.opening.customer_id | S7 execution_topology RECORD_RESPONDED |
| causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0 | RECORD_RESPONDED | INPUT | identity_key | results.CC_READ_HOSTED_STATE_V0.state.opening.identity_key | S7 execution_topology RECORD_RESPONDED |
| causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0 | RECORD_RESPONDED | INPUT | kind | results.CC_READ_HOSTED_STATE_V0.state.opening.kind | S7 execution_topology RECORD_RESPONDED |
| causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0 | RECORD_RESPONDED | INPUT | question | results.CC_READ_HOSTED_STATE_V0.state.opening.question | S7 execution_topology RECORD_RESPONDED |
| causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0 | RECORD_RESPONDED | INPUT | supporting_material | results.CC_READ_HOSTED_STATE_V0.state.opening.supporting_material | S7 execution_topology RECORD_RESPONDED |
| causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0 | RECORD_RESPONDED | INPUT | time_in_service_id | results.CC_READ_HOSTED_STATE_V0.state.opening.time_in_service_id | S7 execution_topology RECORD_RESPONDED |
| causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0 | RECORD_RESPONDED | INPUT | reading | results.CC_READ_HOSTED_STATE_V0.state.opening.reading | S7 execution_topology RECORD_RESPONDED |
| causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0 | RECORD_RESPONDED | INPUT | rules_in_force | results.CC_READ_HOSTED_STATE_V0.state.opening.rules_in_force | S7 execution_topology RECORD_RESPONDED |
| causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0 | RECORD_RESPONDED | INPUT | outcome | RESPONDED | S7 execution_topology RECORD_RESPONDED |
| causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0 | RECORD_RESPONDED | INPUT | response | results.CC_READ_HOSTED_STATE_V0.state.text | S7 execution_topology RECORD_RESPONDED |

---

## 8. Interface Fields

<!-- register:interface_fields optional -->
| Artifact | Direction (INPUT, OUTPUT, ATTRIBUTE) | Field | Type | Required (YES, NO) | Default | Meaning |
|----------|--------------------------------------|-------|------|--------------------|---------|---------|
| causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0 | INPUT | user_prompt_id | string | YES |  | The request's identity, named by the requester and claimed once |
| causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0 | INPUT | requester_id | string | YES |  | The requester who submits the request |
| causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0 | INPUT | permitted_customers | array | YES |  | The customers the requester may act for, as the business's existing arrangements state |
| causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0 | INPUT | customer_id | string | YES |  | The customer the request is for |
| causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0 | INPUT | account_numbers | array | YES |  | The customer's own account numbers, from the business's existing records |
| causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0 | INPUT | identity_key | string | YES |  | The key of the hosted model the request is for |
| causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0 | INPUT | kind | string | YES |  | The most sensitive kind of information the question and its material contain |
| causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0 | INPUT | question | string | YES |  | What the requester asks on the customer's behalf |
| causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0 | INPUT | supporting_material | string | YES |  | Material carried with the question for the model to read |
| causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0 | INPUT | seed | integer | YES |  | The seed each adventurous choice is drawn from |
| causal_language_model::IN_OFFER_NEXT_TOKENS_V0 | INPUT | user_prompt_id | string | YES |  | The request's identity, named by the requester and claimed once |
| causal_language_model::IN_OFFER_NEXT_TOKENS_V0 | INPUT | host_id | string | YES |  | The host offering, as it names itself; recorded, not authenticated |
| causal_language_model::IN_OFFER_NEXT_TOKENS_V0 | INPUT | fingerprint | string | YES |  | The fingerprint of the model the offer is claimed to come from |
| causal_language_model::IN_OFFER_NEXT_TOKENS_V0 | INPUT | reported_reading_size | integer | YES |  | How many tokens the host reports the model reads for this request |
| causal_language_model::IN_OFFER_NEXT_TOKENS_V0 | INPUT | candidates | array | YES |  | The tokens the model could write next, each with its likelihood |
| causal_language_model::IN_RELEASE_HOSTED_RESPONSE_V0 | INPUT | user_prompt_id | string | YES |  | The request's identity, named by the requester and claimed once |
| causal_language_model::IN_RELEASE_HOSTED_RESPONSE_V0 | INPUT | host_id | string | YES |  | The host offering, as it names itself; recorded, not authenticated |
| causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0 | INPUT | reported_reading_size | integer | YES |  | How many tokens the host reports the model reads for this request |
| causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0 | INPUT | reading_capacity | integer | YES |  | How many tokens the model can read in one request |
| causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0 | OUTPUT | reading_fits | boolean | YES |  | Whether the reported size is within the capacity |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | INPUT | user_prompt_id | string | YES |  | The request's identity, named by the requester and claimed once |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | INPUT | requester_id | string | YES |  | The requester who submits the request |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | INPUT | customer_id | string | YES |  | The customer the request is for |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | INPUT | identity_key | string | YES |  | The key of the hosted model the request is for |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | INPUT | kind | string | YES |  | The most sensitive kind of information the question and its material contain |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | INPUT | question | string | YES |  | What the requester asks on the customer's behalf |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | INPUT | supporting_material | string | YES |  | Material carried with the question for the model to read |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | INPUT | time_in_service_id | string | YES |  | The model's open time in service |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | INPUT | reading | object | YES |  | Exactly what the model reads |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | INPUT | response_rules | object | YES |  | The time in service's forbidden words and patterns, account-number shape, freedom and longest response |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | INPUT | account_numbers | array | YES |  | The customer's own account numbers, from the business's existing records |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | INPUT | seed | integer | YES |  | The seed each adventurous choice is drawn from |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | INPUT | fingerprint | string | YES |  | The fingerprint of the model the offer is claimed to come from |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | INPUT | reading_capacity | integer | YES |  | How many tokens the model can read in one request |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | INPUT | maximum_response_length | integer | YES |  | The most tokens a response of the model may have |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | OUTPUT | rules_in_force | object | YES |  | The response rules in force for this request, with its seed |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | OUTPUT | positions | array | YES |  | One position per token up to the rules' longest response |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | OUTPUT | opening_record | object | YES |  | The opening entry of the request's trail, with what the model reads |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | OUTPUT | record_id | string | YES |  | The identity of the opening entry |
| causal_language_model::CC_OPEN_HOSTED_RECORD_V0 | OUTPUT | sequence_number | integer | YES |  | The opening entry's position in the user prompt records |
| causal_language_model::CC_READ_HOSTED_STATE_V0 | INPUT | user_prompt_id | string | YES |  | The request's identity, named by the requester and claimed once |
| causal_language_model::CC_READ_HOSTED_STATE_V0 | OUTPUT | entries | array | YES |  | The request's trail as recorded |
| causal_language_model::CC_READ_HOSTED_STATE_V0 | OUTPUT | state | object | YES |  | The hosted request's response as built, its position, whether it is complete, and its permitted length |
| causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0 | INPUT | offered_fingerprint | string | YES |  | The fingerprint an offer names |
| causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0 | INPUT | admitted_fingerprint | string | YES |  | The fingerprint of the model the request was admitted for |
| causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0 | OUTPUT | offer_for_model | boolean | YES |  | Whether the offer names the admitted model's fingerprint |
| causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0 | INPUT | state | object | YES |  | The hosted request's response as built, its position, whether it is complete, and its permitted length |
| causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0 | INPUT | candidates | array | YES |  | The tokens the model could write next, each with its likelihood |
| causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0 | OUTPUT | step | object | YES |  | One offer and the choice made from it |
| causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0 | OUTPUT | text | string | YES |  | The response with the chosen token |
| causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0 | OUTPUT | finished | boolean | YES |  | Whether the chosen token ends the response |
| causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0 | OUTPUT | stopped_by | string | YES |  | The rule that left no permitted token, or none |
| causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0 | OUTPUT | within_length | boolean | YES |  | Whether the response is still within its permitted length |
| causal_language_model::CC_RECORD_HOSTED_STEP_V0 | INPUT | user_prompt_id | string | YES |  | The request's identity, named by the requester and claimed once |
| causal_language_model::CC_RECORD_HOSTED_STEP_V0 | INPUT | host_id | string | YES |  | The host offering, as it names itself; recorded, not authenticated |
| causal_language_model::CC_RECORD_HOSTED_STEP_V0 | INPUT | fingerprint | string | YES |  | The fingerprint of the model the offer is claimed to come from |
| causal_language_model::CC_RECORD_HOSTED_STEP_V0 | INPUT | reported_reading_size | integer | YES |  | How many tokens the host reports the model reads for this request |
| causal_language_model::CC_RECORD_HOSTED_STEP_V0 | INPUT | step | object | YES |  | One offer and the choice made from it |
| causal_language_model::CC_RECORD_HOSTED_STEP_V0 | OUTPUT | step_record | object | YES |  | The step entry appended to the request's trail |
| causal_language_model::CC_RECORD_HOSTED_STEP_V0 | OUTPUT | record_id | string | YES |  | The identity of the step entry |
| causal_language_model::CC_RECORD_HOSTED_STEP_V0 | OUTPUT | sequence_number | integer | YES |  | The step entry's position in the user prompt records |
| causal_language_model::CT_PURE_READ_HOSTED_STATE_V0 | INPUT | entries | array | YES |  | The request's trail as recorded |
| causal_language_model::CT_PURE_READ_HOSTED_STATE_V0 | OUTPUT | state | object | YES |  | The hosted request's response as built, its position, whether it is complete, and its permitted length |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | INPUT | state | object | YES |  | The hosted request's response as built, its position, whether it is complete, and its permitted length |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | INPUT | candidates | array | YES |  | The tokens the model could write next, each with its likelihood |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | OUTPUT | step | object | YES |  | One offer and the choice made from it |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | OUTPUT | text | string | YES |  | The response with the chosen token |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | OUTPUT | finished | boolean | YES |  | Whether the chosen token ends the response |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | OUTPUT | stopped_by | string | YES |  | The rule that left no permitted token, or none |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | OUTPUT | within_length | boolean | YES |  | Whether the response is still within its permitted length |
| causal_language_model::AC_MODEL_HOST_V0 | ATTRIBUTE | host_id | string | YES |  | The host's name for itself; recorded against every offer, not authenticated |

---

## 9. Implementation Bindings

The state is read from the trail and nowhere else: the opening entry, then the steps in the order they
were appended. A trail with no opening entry, or with a closing one, is refused. The chosen tokens are
joined as they are into the response so far; the end marker `<end>` ends it.

The choice stops a candidate when a forbidden rule's pattern matches the response so far joined to the
candidate, at a match that reaches into the candidate, unless the matched characters with spaces and
dashes removed are among the rule's exceptions. Text is judged in its compatibility form, so a
lookalike digit is the digit it looks like. A number is judged on its digits, spaces, commas, dots and
dashes between them being separators. A number the model read is not begun unless it could be a
permitted one: a candidate is stopped when it writes digits that begin a number a rule forbids in what
the model read, and begin no other number the model read. Where the opening sets grounding, a number
may not be begun unless a number the model read begins with its digits, nor ended unless it is one, and
a candidate that would do either is stopped by `numbers_from_the_reading`. It chooses among the
permitted candidates, most likely first and ties in offered order: of the first freedom-plus-one, the
one at position (seed plus the token's position) modulo their count. A response may have at most its
permitted length in tokens, the end marker not counted; a token that would take it past that leaves it
outside its length. An offer for a complete response is refused.

<!-- register:implementation_bindings optional -->
| CT Code | Module | Callable | Operation | Kind (atom, molecule) | Purity (ct_pure, ct_impure) | Refusal (raises, returns, never) | Source Finding |
|---------|--------|----------|-----------|-----------------------|-----------------------------|----------------------------------|----------------|
| causal_language_model::CT_PURE_READ_HOSTED_STATE_V0 | causal_language_model.implementation.capability_transforms.atoms.ct_pure_read_hosted_state_v0 | execute | READ_HOSTED_STATE | atom | ct_pure | raises | S7 new_artifacts CT_PURE_READ_HOSTED_STATE_V0 |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | causal_language_model.implementation.capability_transforms.atoms.ct_pure_choose_permitted_token_v0 | execute | CHOOSE_PERMITTED_TOKEN | atom | ct_pure | raises | S7 new_artifacts CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 |

---

## 10. Vocabulary Extensions

<!-- register:vocabulary_extensions optional -->
| Vocabulary Code | Extends | Group | Casing | Value | Meaning | Source Finding |
|-----------------|---------|-------|--------|-------|---------|----------------|
| NONE IDENTIFIED |

---

## 11. Runtime Policies

<!-- register:runtime_policies optional -->
| RB Code | Capability | Key | Value | Source Finding |
|---------|------------|-----|-------|----------------|
| NONE IDENTIFIED |

---

## 12. Artifact Properties

<!-- register:artifact_properties optional -->
| Artifact | Property | Value | Source Finding |
|----------|----------|-------|----------------|
| causal_language_model::AC_MODEL_HOST_V0 | type | ENDUSER | S5 provisional_codes AC_MODEL_HOST_V0 |
| causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0 | emit.EXIT_REFUSED | causal_language_model::EV_USER_PROMPT_REFUSED_V0 | S1 business_events #2 |
| causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | emit.EXIT_REFUSED | causal_language_model::EV_USER_PROMPT_REFUSED_V0 | S1 business_events #2 |
| causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0 | emit.EXIT_RESPONDED | causal_language_model::EV_USER_PROMPT_RESPONDED_V0 | S1 business_events #1 |
| causal_language_model::EV_USER_PROMPT_REFUSED_V0 | moment | refusal | S1 business_events #2 |

---

## 13. STRUCTURE Stores

The trail is kept in the user prompt records the subdomain already declares; no store is added.

<!-- register:structure_stores optional -->
| Store Name | Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0) | Proposed Path | Used By | Source Finding |
|------------|---------------------------------------------------------------------------|---------------|---------|----------------|
| NONE IDENTIFIED |

---

## 14. Transport Bindings

<!-- register:transport_bindings optional -->
| Artifact | Direction (INGRESS, EGRESS) | Operation | Handler Kind (WF_INVOCATION, SNAPSHOT_READ) | Handler Target | Field | Bound To | Source Finding |
|----------|-----------------------------|-----------|---------------------------------------------|----------------|-------|----------|----------------|
| NONE IDENTIFIED |

## 15. Artifact Summary

<!-- register:artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Subdomain | Count | Artifacts |
|-------------------------------|-----------|-------|-----------|
| NEW | model_response | 15 | 1 AC, 3 IN, 3 WF, 6 CC, 2 CT |

---

## 16. Generation Provenance

<!-- register:generation_provenance optional -->
| Artifact | Generator | Generator Sources | Source Finding |
|----------|-----------|-------------------|----------------|
| NONE IDENTIFIED |

---

## 17. Declared Reach

Every act reads only what model_response owns.

<!-- register:declared_reach optional -->
| Act | Consults | Source Finding |
|-----|----------|----------------|
| NONE IDENTIFIED |

---

## 18. Refusal Discharge

A refusal that closes the request is discharged at the place that records it, whose success ends the
act at `EXIT_REFUSED`. An offer for a request not being written, and a release of an incomplete
response, change nothing and end at `EXIT_REJECTED`.

<!-- register:refusal_discharge optional -->
| Operation | Refused When | Act | Step | Outcome | Source Finding |
|-----------|--------------|-----|------|---------|----------------|
| Offer candidates | The reported reading size exceeds the model's reading capacity. | causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | SUCCESS | S0 operation_refusals #1 |
| Offer candidates | The offer names a fingerprint other than the model's the request was admitted for. | causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_OTHER_MODEL | SUCCESS | S0 operation_refusals #2 |
| Offer candidates | The request is not being written. | causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | causal_language_model::CC_READ_HOSTED_STATE_V0 | VIOLATION | S0 operation_refusals #3 |
| Offer candidates | Every candidate is forbidden. | causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_BY_RULE | SUCCESS | S0 operation_refusals #4 |
| Offer candidates | The response reaches its permitted length before it is complete. | causal_language_model::WF_OFFER_NEXT_TOKENS_V0 | RECORD_REFUSED_UNFINISHED | SUCCESS | S0 operation_refusals #5 |
| Release a response | The response is not complete. | causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0 | CONFIRM_FINISHED | VIOLATION | S0 operation_refusals #6 |

---

## 19. Refusal Deferrals

<!-- register:refusal_deferrals optional -->
| Operation | Refused When | Deferred To | Until | Source Finding |
|-----------|--------------|-------------|-------|----------------|
| NONE IDENTIFIED |

---

## 20. Refusal — Governance-Surface Discharge

<!-- register:refusal_governance_discharge optional -->
| Operation | Refused When | Phase | Governing Rule | Source Finding |
|-----------|--------------|-------|----------------|----------------|
| NONE IDENTIFIED |

---

## 21. Molecule Steps

<!-- register:molecule_steps optional -->
| CT Code | Step | Kind (atom, molecule, loop) | Target | Over | Iterator | Emits | Source Finding |
|---------|------|-----------------------------|--------|------|----------|-------|----------------|
| NONE IDENTIFIED |

---

## 22. Molecule Step Bindings

<!-- register:molecule_step_bindings optional -->
| CT Code | Step | Role (INPUT, CARRY, UPDATE) | Field | Bound To | Source Finding |
|---------|------|-----------------------------|-------|----------|----------------|
| NONE IDENTIFIED |

---

## 23. Test Cases

<!-- register:test_cases optional -->
| CT Code | Case | Expected Outcome (SUCCESS, VIOLATION) | Source Finding |
|---------|------|---------------------------------------|----------------|
| causal_language_model::CT_PURE_READ_HOSTED_STATE_V0 | reduces_the_trail_to_the_response_as_built | SUCCESS | human decision |
| causal_language_model::CT_PURE_READ_HOSTED_STATE_V0 | refuses_a_request_never_admitted | VIOLATION | human decision |
| causal_language_model::CT_PURE_READ_HOSTED_STATE_V0 | refuses_a_closed_request | VIOLATION | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | stops_an_account_number_split_across_tokens | SUCCESS | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | writes_the_customers_own_account_across_tokens | SUCCESS | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | names_the_rule_when_no_permitted_token_remains | SUCCESS | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | passes_the_permitted_length_unfinished | SUCCESS | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | finishes_on_the_end_of_the_response | SUCCESS | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | judges_a_lookalike_digit_as_the_digit | SUCCESS | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | does_not_begin_a_forbidden_number_the_model_read | SUCCESS | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | begins_a_number_the_model_read_that_is_permitted | SUCCESS | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | grounded_writes_a_number_it_read | SUCCESS | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | grounded_does_not_change_a_value_it_read | SUCCESS | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | ungrounded_writes_a_number_it_did_not_read | SUCCESS | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | refuses_an_offer_for_a_complete_response | VIOLATION | human decision |

---

## 24. Test Case Values

<!-- register:test_case_values optional -->
| CT Code | Case | Role (INPUT, EXPECTED, ASSERT, RECORDED) | Field | Value | Source Finding |
|---------|------|------------------------------------------|-------|-------|----------------|
| causal_language_model::CT_PURE_READ_HOSTED_STATE_V0 | reduces_the_trail_to_the_response_as_built | INPUT | entries | [{sequence_number: 1, record: {outcome: WRITING, fingerprint: fp-host, reading: {system_prompt: 'Answer only from the supporting material.', question: 'What is my balance?', supporting_material: 'Account 12345678 balance 40. Spouse account 87654321.'}, rules_in_force: {forbidden: [{rule: no_guarantees, pattern: '\bguaranteed\b'}, {rule: another_customers_account_number, pattern: '[0-9](?:[ -]?[0-9]){7}', except: ['12345678']}], freedom: 0, seed: 7}, ground_numbers: false, maximum_response_length: 3, longest_response: 5}}, {sequence_number: 2, record: {outcome: STEP, chosen: 'Your'}}, {sequence_number: 3, record: {outcome: STEP, chosen: ' balance'}}] | human decision |
| causal_language_model::CT_PURE_READ_HOSTED_STATE_V0 | reduces_the_trail_to_the_response_as_built | EXPECTED | state | {opening: {outcome: WRITING, fingerprint: fp-host, reading: {system_prompt: 'Answer only from the supporting material.', question: 'What is my balance?', supporting_material: 'Account 12345678 balance 40. Spouse account 87654321.'}, rules_in_force: {forbidden: [{rule: no_guarantees, pattern: '\bguaranteed\b'}, {rule: another_customers_account_number, pattern: '[0-9](?:[ -]?[0-9]){7}', except: ['12345678']}], freedom: 0, seed: 7}, ground_numbers: false, maximum_response_length: 3, longest_response: 5}, position: 2, text: 'Your balance', finished: false, limit: 3} | human decision |
| causal_language_model::CT_PURE_READ_HOSTED_STATE_V0 | refuses_a_request_never_admitted | INPUT | entries | [{sequence_number: 1, record: {outcome: REFUSED, reason: model_not_registered}}] | human decision |
| causal_language_model::CT_PURE_READ_HOSTED_STATE_V0 | refuses_a_closed_request | INPUT | entries | [{sequence_number: 1, record: {outcome: WRITING, fingerprint: fp-host, reading: {system_prompt: 'Answer only from the supporting material.', question: 'What is my balance?', supporting_material: 'Account 12345678 balance 40. Spouse account 87654321.'}, rules_in_force: {forbidden: [{rule: no_guarantees, pattern: '\bguaranteed\b'}, {rule: another_customers_account_number, pattern: '[0-9](?:[ -]?[0-9]){7}', except: ['12345678']}], freedom: 0, seed: 7}, ground_numbers: false, maximum_response_length: 3, longest_response: 5}}, {sequence_number: 2, record: {outcome: RESPONDED}}] | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | stops_an_account_number_split_across_tokens | INPUT | state | {opening: {outcome: WRITING, fingerprint: fp-host, reading: {system_prompt: 'Answer only from the supporting material.', question: 'What is my balance?', supporting_material: 'Account 12345678 balance 40. Spouse account 87654321.'}, rules_in_force: {forbidden: [{rule: no_guarantees, pattern: '\bguaranteed\b'}, {rule: another_customers_account_number, pattern: '[0-9](?:[ -]?[0-9]){7}', except: ['12345678']}], freedom: 0, seed: 7}, ground_numbers: false, maximum_response_length: 3, longest_response: 5}, position: 1, text: 'Account 8765', finished: false, limit: 3} | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | stops_an_account_number_split_across_tokens | INPUT | candidates | [{token: '4321', likelihood: 0.7}, {token: ' is', likelihood: 0.2}] | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | stops_an_account_number_split_across_tokens | EXPECTED | text | Account 8765 is | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | stops_an_account_number_split_across_tokens | EXPECTED | finished | false | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | stops_an_account_number_split_across_tokens | EXPECTED | stopped_by | none | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | stops_an_account_number_split_across_tokens | EXPECTED | within_length | true | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | stops_an_account_number_split_across_tokens | EXPECTED | step | {position: 2, candidates: [{token: '4321', likelihood: 0.7}, {token: ' is', likelihood: 0.2}], chosen: ' is', stopped: [{token: '4321', rule: another_customers_account_number}], stopped_by: none, finished: false, within_length: true} | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | writes_the_customers_own_account_across_tokens | INPUT | state | {opening: {outcome: WRITING, fingerprint: fp-host, reading: {system_prompt: 'Answer only from the supporting material.', question: 'What is my balance?', supporting_material: 'Account 12345678 balance 40. Spouse account 87654321.'}, rules_in_force: {forbidden: [{rule: no_guarantees, pattern: '\bguaranteed\b'}, {rule: another_customers_account_number, pattern: '[0-9](?:[ -]?[0-9]){7}', except: ['12345678']}], freedom: 0, seed: 7}, ground_numbers: false, maximum_response_length: 3, longest_response: 5}, position: 1, text: 'Account 1234', finished: false, limit: 3} | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | writes_the_customers_own_account_across_tokens | INPUT | candidates | [{token: '5678', likelihood: 0.8}] | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | writes_the_customers_own_account_across_tokens | EXPECTED | text | Account 12345678 | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | writes_the_customers_own_account_across_tokens | EXPECTED | stopped_by | none | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | writes_the_customers_own_account_across_tokens | EXPECTED | step | {position: 2, candidates: [{token: '5678', likelihood: 0.8}], chosen: '5678', stopped: [], stopped_by: none, finished: false, within_length: true} | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | writes_the_customers_own_account_across_tokens | EXPECTED | finished | false | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | writes_the_customers_own_account_across_tokens | EXPECTED | within_length | true | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | names_the_rule_when_no_permitted_token_remains | INPUT | state | {opening: {outcome: WRITING, fingerprint: fp-host, reading: {system_prompt: 'Answer only from the supporting material.', question: 'What is my balance?', supporting_material: 'Account 12345678 balance 40. Spouse account 87654321.'}, rules_in_force: {forbidden: [{rule: no_guarantees, pattern: '\bguaranteed\b'}, {rule: another_customers_account_number, pattern: '[0-9](?:[ -]?[0-9]){7}', except: ['12345678']}], freedom: 0, seed: 7}, ground_numbers: false, maximum_response_length: 3, longest_response: 5}, position: 0, text: '', finished: false, limit: 3} | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | names_the_rule_when_no_permitted_token_remains | INPUT | candidates | [{token: '87654321', likelihood: 0.9}] | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | names_the_rule_when_no_permitted_token_remains | EXPECTED | text | "" | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | names_the_rule_when_no_permitted_token_remains | EXPECTED | stopped_by | another_customers_account_number | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | names_the_rule_when_no_permitted_token_remains | EXPECTED | finished | false | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | names_the_rule_when_no_permitted_token_remains | EXPECTED | step | {position: 1, candidates: [{token: '87654321', likelihood: 0.9}], chosen: null, stopped: [{token: '87654321', rule: another_customers_account_number}], stopped_by: another_customers_account_number, finished: false, within_length: true} | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | names_the_rule_when_no_permitted_token_remains | EXPECTED | within_length | true | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | passes_the_permitted_length_unfinished | INPUT | state | {opening: {outcome: WRITING, fingerprint: fp-host, reading: {system_prompt: 'Answer only from the supporting material.', question: 'What is my balance?', supporting_material: 'Account 12345678 balance 40. Spouse account 87654321.'}, rules_in_force: {forbidden: [{rule: no_guarantees, pattern: '\bguaranteed\b'}, {rule: another_customers_account_number, pattern: '[0-9](?:[ -]?[0-9]){7}', except: ['12345678']}], freedom: 0, seed: 7}, ground_numbers: false, maximum_response_length: 3, longest_response: 5}, position: 3, text: 'Your balance is', finished: false, limit: 3} | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | passes_the_permitted_length_unfinished | INPUT | candidates | [{token: ' today', likelihood: 0.9}] | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | passes_the_permitted_length_unfinished | EXPECTED | text | Your balance is today | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | passes_the_permitted_length_unfinished | EXPECTED | within_length | false | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | passes_the_permitted_length_unfinished | EXPECTED | finished | false | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | passes_the_permitted_length_unfinished | EXPECTED | step | {position: 4, candidates: [{token: ' today', likelihood: 0.9}], chosen: ' today', stopped: [], stopped_by: none, finished: false, within_length: false} | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | passes_the_permitted_length_unfinished | EXPECTED | stopped_by | none | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | finishes_on_the_end_of_the_response | INPUT | state | {opening: {outcome: WRITING, fingerprint: fp-host, reading: {system_prompt: 'Answer only from the supporting material.', question: 'What is my balance?', supporting_material: 'Account 12345678 balance 40. Spouse account 87654321.'}, rules_in_force: {forbidden: [{rule: no_guarantees, pattern: '\bguaranteed\b'}, {rule: another_customers_account_number, pattern: '[0-9](?:[ -]?[0-9]){7}', except: ['12345678']}], freedom: 0, seed: 7}, ground_numbers: false, maximum_response_length: 3, longest_response: 5}, position: 2, text: 'Your balance', finished: false, limit: 3} | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | finishes_on_the_end_of_the_response | INPUT | candidates | [{token: <end>, likelihood: 0.9}] | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | finishes_on_the_end_of_the_response | EXPECTED | text | Your balance | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | finishes_on_the_end_of_the_response | EXPECTED | finished | true | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | finishes_on_the_end_of_the_response | EXPECTED | within_length | true | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | finishes_on_the_end_of_the_response | EXPECTED | step | {position: 3, candidates: [{token: <end>, likelihood: 0.9}], chosen: <end>, stopped: [], stopped_by: none, finished: true, within_length: true} | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | finishes_on_the_end_of_the_response | EXPECTED | stopped_by | none | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | judges_a_lookalike_digit_as_the_digit | INPUT | state | {opening: {outcome: WRITING, fingerprint: fp-host, reading: {system_prompt: 'Answer only from the supporting material.', question: 'What is my balance?', supporting_material: 'Account 12345678 balance 40. Spouse account 87654321.'}, rules_in_force: {forbidden: [{rule: no_guarantees, pattern: '\bguaranteed\b'}, {rule: another_customers_account_number, pattern: '[0-9](?:[ -]?[0-9]){7}', except: ['12345678']}], freedom: 0, seed: 7}, ground_numbers: false, maximum_response_length: 3, longest_response: 5}, position: 2, text: 'Spouse account 8765432', finished: false, limit: 3} | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | judges_a_lookalike_digit_as_the_digit | INPUT | candidates | [{token: '₁', likelihood: 0.8}, {token: '.', likelihood: 0.1}] | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | judges_a_lookalike_digit_as_the_digit | EXPECTED | text | Spouse account 8765432. | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | judges_a_lookalike_digit_as_the_digit | EXPECTED | stopped_by | none | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | judges_a_lookalike_digit_as_the_digit | EXPECTED | step | {position: 3, candidates: [{token: "\u2081", likelihood: 0.8}, {token: ., likelihood: 0.1}], chosen: ., stopped: [{token: "\u2081", rule: another_customers_account_number}], stopped_by: none, finished: false, within_length: true} | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | judges_a_lookalike_digit_as_the_digit | EXPECTED | finished | false | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | judges_a_lookalike_digit_as_the_digit | EXPECTED | within_length | true | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | does_not_begin_a_forbidden_number_the_model_read | INPUT | state | {opening: {outcome: WRITING, fingerprint: fp-host, reading: {system_prompt: 'Answer only from the supporting material.', question: 'What is my balance?', supporting_material: 'Account 12345678 balance 40. Spouse account 87654321.'}, rules_in_force: {forbidden: [{rule: no_guarantees, pattern: '\bguaranteed\b'}, {rule: another_customers_account_number, pattern: '[0-9](?:[ -]?[0-9]){7}', except: ['12345678']}], freedom: 0, seed: 7}, ground_numbers: false, maximum_response_length: 3, longest_response: 5}, position: 2, text: 'Spouse account ', finished: false, limit: 3} | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | does_not_begin_a_forbidden_number_the_model_read | INPUT | candidates | [{token: '8', likelihood: 0.8}, {token: withheld, likelihood: 0.1}] | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | does_not_begin_a_forbidden_number_the_model_read | EXPECTED | text | Spouse account withheld | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | does_not_begin_a_forbidden_number_the_model_read | EXPECTED | stopped_by | none | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | does_not_begin_a_forbidden_number_the_model_read | EXPECTED | step | {position: 3, candidates: [{token: '8', likelihood: 0.8}, {token: withheld, likelihood: 0.1}], chosen: withheld, stopped: [{token: '8', rule: another_customers_account_number}], stopped_by: none, finished: false, within_length: true} | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | does_not_begin_a_forbidden_number_the_model_read | EXPECTED | finished | false | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | does_not_begin_a_forbidden_number_the_model_read | EXPECTED | within_length | true | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | begins_a_number_the_model_read_that_is_permitted | INPUT | state | {opening: {outcome: WRITING, fingerprint: fp-host, reading: {system_prompt: 'Answer only from the supporting material.', question: 'What is my balance?', supporting_material: 'Account 12345678 balance 40. Spouse account 87654321.'}, rules_in_force: {forbidden: [{rule: no_guarantees, pattern: '\bguaranteed\b'}, {rule: another_customers_account_number, pattern: '[0-9](?:[ -]?[0-9]){7}', except: ['12345678']}], freedom: 0, seed: 7}, ground_numbers: false, maximum_response_length: 3, longest_response: 5}, position: 2, text: 'Balance ', finished: false, limit: 3} | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | begins_a_number_the_model_read_that_is_permitted | INPUT | candidates | [{token: '4', likelihood: 0.8}] | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | begins_a_number_the_model_read_that_is_permitted | EXPECTED | text | Balance 4 | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | begins_a_number_the_model_read_that_is_permitted | EXPECTED | stopped_by | none | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | begins_a_number_the_model_read_that_is_permitted | EXPECTED | step | {position: 3, candidates: [{token: '4', likelihood: 0.8}], chosen: '4', stopped: [], stopped_by: none, finished: false, within_length: true} | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | begins_a_number_the_model_read_that_is_permitted | EXPECTED | finished | false | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | begins_a_number_the_model_read_that_is_permitted | EXPECTED | within_length | true | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | grounded_writes_a_number_it_read | INPUT | state | {opening: {outcome: WRITING, fingerprint: fp-host, reading: {system_prompt: 'Answer only from the supporting material.', question: 'What is my balance?', supporting_material: 'Account 12345678 balance 40. Spouse account 87654321.'}, rules_in_force: {forbidden: [{rule: no_guarantees, pattern: '\bguaranteed\b'}, {rule: another_customers_account_number, pattern: '[0-9](?:[ -]?[0-9]){7}', except: ['12345678']}], freedom: 0, seed: 7}, ground_numbers: true, maximum_response_length: 3, longest_response: 5}, position: 2, text: 'Balance 4', finished: false, limit: 3} | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | grounded_writes_a_number_it_read | INPUT | candidates | [{token: '9', likelihood: 0.8}, {token: '0', likelihood: 0.1}] | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | grounded_writes_a_number_it_read | EXPECTED | text | Balance 40 | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | grounded_writes_a_number_it_read | EXPECTED | stopped_by | none | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | grounded_writes_a_number_it_read | EXPECTED | step | {position: 3, candidates: [{token: '9', likelihood: 0.8}, {token: '0', likelihood: 0.1}], chosen: '0', stopped: [{token: '9', rule: numbers_from_the_reading}], stopped_by: none, finished: false, within_length: true} | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | grounded_writes_a_number_it_read | EXPECTED | finished | false | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | grounded_writes_a_number_it_read | EXPECTED | within_length | true | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | grounded_does_not_change_a_value_it_read | INPUT | state | {opening: {outcome: WRITING, fingerprint: fp-host, reading: {system_prompt: 'Answer only from the supporting material.', question: 'What is my balance?', supporting_material: 'Account 12345678 balance 40. Spouse account 87654321.'}, rules_in_force: {forbidden: [{rule: no_guarantees, pattern: '\bguaranteed\b'}, {rule: another_customers_account_number, pattern: '[0-9](?:[ -]?[0-9]){7}', except: ['12345678']}], freedom: 0, seed: 7}, ground_numbers: true, maximum_response_length: 3, longest_response: 5}, position: 2, text: 'Balance 4', finished: false, limit: 3} | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | grounded_does_not_change_a_value_it_read | INPUT | candidates | [{token: ' dollars', likelihood: 0.8}, {token: <end>, likelihood: 0.1}] | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | grounded_does_not_change_a_value_it_read | EXPECTED | text | Balance 4 | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | grounded_does_not_change_a_value_it_read | EXPECTED | stopped_by | numbers_from_the_reading | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | grounded_does_not_change_a_value_it_read | EXPECTED | step | {position: 3, candidates: [{token: ' dollars', likelihood: 0.8}, {token: <end>, likelihood: 0.1}], chosen: null, stopped: [{token: ' dollars', rule: numbers_from_the_reading}, {token: <end>, rule: numbers_from_the_reading}], stopped_by: numbers_from_the_reading, finished: false, within_length: true} | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | grounded_does_not_change_a_value_it_read | EXPECTED | finished | false | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | grounded_does_not_change_a_value_it_read | EXPECTED | within_length | true | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | ungrounded_writes_a_number_it_did_not_read | INPUT | state | {opening: {outcome: WRITING, fingerprint: fp-host, reading: {system_prompt: 'Answer only from the supporting material.', question: 'What is my balance?', supporting_material: 'Account 12345678 balance 40. Spouse account 87654321.'}, rules_in_force: {forbidden: [{rule: no_guarantees, pattern: '\bguaranteed\b'}, {rule: another_customers_account_number, pattern: '[0-9](?:[ -]?[0-9]){7}', except: ['12345678']}], freedom: 0, seed: 7}, ground_numbers: false, maximum_response_length: 3, longest_response: 5}, position: 2, text: 'Balance ', finished: false, limit: 3} | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | ungrounded_writes_a_number_it_did_not_read | INPUT | candidates | [{token: '9', likelihood: 0.8}] | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | ungrounded_writes_a_number_it_did_not_read | EXPECTED | text | Balance 9 | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | ungrounded_writes_a_number_it_did_not_read | EXPECTED | stopped_by | none | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | ungrounded_writes_a_number_it_did_not_read | EXPECTED | step | {position: 3, candidates: [{token: '9', likelihood: 0.8}], chosen: '9', stopped: [], stopped_by: none, finished: false, within_length: true} | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | ungrounded_writes_a_number_it_did_not_read | EXPECTED | finished | false | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | ungrounded_writes_a_number_it_did_not_read | EXPECTED | within_length | true | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | refuses_an_offer_for_a_complete_response | INPUT | state | {opening: {outcome: WRITING, fingerprint: fp-host, reading: {system_prompt: 'Answer only from the supporting material.', question: 'What is my balance?', supporting_material: 'Account 12345678 balance 40. Spouse account 87654321.'}, rules_in_force: {forbidden: [{rule: no_guarantees, pattern: '\bguaranteed\b'}, {rule: another_customers_account_number, pattern: '[0-9](?:[ -]?[0-9]){7}', except: ['12345678']}], freedom: 0, seed: 7}, ground_numbers: false, maximum_response_length: 3, longest_response: 5}, position: 2, text: 'Your balance', finished: true, limit: 3} | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | refuses_an_offer_for_a_complete_response | INPUT | candidates | [{token: ' more', likelihood: 0.9}] | human decision |

---

## 25. Withdrawn Facts

<!-- register:withdrawn_facts optional -->
| Artifact | Fact | Reason | Source Finding |
|----------|------|--------|----------------|
| NONE IDENTIFIED |

---

## gov_projection — Governed Handoff to Stage 8

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 6 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
| **Emits** → Stage 8 | design_resolution · existing_inventory · new_artifacts · rb_declarations · execution_topology · cc_composition · step_bindings · interface_fields · implementation_bindings · vocabulary_extensions · runtime_policies · artifact_properties · structure_stores · artifact_summary · generation_provenance |
