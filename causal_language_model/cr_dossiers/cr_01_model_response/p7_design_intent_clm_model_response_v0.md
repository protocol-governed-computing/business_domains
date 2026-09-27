# Stage 7 — Design Intent: causal_language_model / model_response

**Stage:** 7 — Design Intent
**CR:** cr_01_model_response
**Status:** DRAFT
**Feeds:** Stage 8 — Authoring Mandate

Every binding names a field the capability declares, read from the pinned baseline
`f6cfaac48c1fba78ab92d38a65828b91a105ae56f0be78040cfc6b71701b13e6`.

---

## 1. Design Decisions Resolution

<!-- register:design_resolution optional -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|
| model_response is a new subdomain | Nothing in the composition registers a model or governs how one writes | A new subdomain of the causal_language_model namespace with its own two actors, five stores, one binding and five operations | S4 design_decisions #1 |
| Writing is a molecule of two declared steps per pass | The rules must act while the model writes, visibly to governance | One pass is a molecule of the model's offer and the rules' choice; the response is a molecule whose loop runs one pass per position up to the longest response | S4 design_decisions #2 |
| Determinism ends at the model's step | A reader must see exactly where determinism ends | Only the offer is declared ct_impure; the choice emits each pass's result, so nothing is decided on the model's offer | S4 design_decisions #3 |
| A trace is reproduced from its record | A user prompt's trace must be reproducible from what was recorded | The platform records each offer where it is produced; the writing molecule's vectors state recorded offers and are proven by substituting them | S4 design_decisions #4 |
| The seed is a recorded input | Anyone reading the record can re-derive each chosen word | The user prompt states a seed; it enters the rules in force, which the user prompt record keeps whole | S4 design_decisions #5 |
| The test model is a realization of the model's step | The rules must be shown to hold against a model that tries to break them | The offer's implementation is the test model, which offers another customer's account number first | S4 design_decisions #6 |
| The customer's account numbers travel with the user prompt | The rule against another customer's account number is formed per user prompt | The rules in force add one forbidden pattern, the account-number shape, excepting the customer's own numbers | S4 design_decisions #7 |
| Uniqueness by a formed key | Two registrations with the same description and fingerprint are the same model | A pure transform forms one key from the description and fingerprint; the registry claims it atomically, and ALREADY_EXISTS is the duplicate refusal | S4 design_decisions #8 |
| State is data on the record | A model moves into and out of service repeatedly | The model record carries its state and the open time in service; placement and withdrawal update both records in place | S4 design_decisions #9 |
| Membership before order | Membership is mechanism; the comparison is this subdomain's rule | The stated kind is confirmed a declared kind, then compared with the ceiling by the declared order | S4 design_decisions #10 |
| Retrieval raises no event | Nothing reacts to a read | Retrieval appends to the operation trail and declares no business moment | S4 design_decisions #11 |
| Authorization is read, never granted | Which staff are model staff and who may act for which customer is decided elsewhere | Model staff credentials are checked against supplied rules; the requester's permitted customers arrive with the user prompt; no store of either is declared | S4 design_decisions #12 |
| Every refusal is recorded with its reason | Every user prompt is recorded, whether responded to or refused | Each refusal routes to its own place in the submission, where the recording contract runs with that refusal's reason; a submission is traced by its user prompt record, which names the requester | S4 constraint_register #9 |

---

## 2. Artifact Inventory — Existing Artifacts

<!-- register:existing_inventory -->
| FQDN | Action (REPLACE, REUSE, EXTEND, REVIEW) | Summary | Reason | Source Finding |
|------|-----------------------------------------|---------|--------|----------------|
| capability_side_effects::CS_MUTABLE_JSON_V0 | REUSE |  | Holds the model record and the time in service record, read and updated in place. | S6 pps_artifacts_requiring_action capability_side_effects::CS_MUTABLE_JSON_V0 |
| capability_side_effects::CS_REGISTRY_V0 | REUSE |  | Register-if-absent gives the atomic claim duplicate prevention needs, on a key the subdomain forms. | S6 pps_artifacts_requiring_action capability_side_effects::CS_REGISTRY_V0 |
| capability_side_effects::CS_APPENDONLY_JSONL_V0 | REUSE |  | Appends the user prompt record and the operation trail, neither of which can be amended. | S6 pps_artifacts_requiring_action capability_side_effects::CS_APPENDONLY_JSONL_V0 |
| capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | REUSE |  | Assembles the model, time in service and user prompt records from supplied values. | S6 pps_artifacts_requiring_action capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 |
| capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | REUSE |  | Confirms a model description carries the fields registration requires. | S6 pps_artifacts_requiring_action capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 |
| capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | REUSE |  | Confirms model staff credentials, a model's state and a response's release conditions against declared rules, and interprets each into a decision. | S6 pps_artifacts_requiring_action capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 |
| capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 | REUSE |  | Confirms a stated kind of information is a declared kind, and that a requester may act for the customer. | S6 pps_artifacts_requiring_action capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 |
| capability_transforms::CT_PURE_FILTER_RECORDS_V0 | REUSE |  | Selects the one user prompt record retrieved, and interprets a record not found into a refusal. | S6 ownership Append an entry to a trail that cannot be amended |
| capability_transforms::CONSTITUTION_MOLECULES_V0 | REUSE |  | Governs the two writing molecules and runs the loop's body once per pass. | S6 pps_artifacts_requiring_action capability_transforms::CONSTITUTION_MOLECULES_V0 |
| capability_transforms::CONSTITUTION_NONDETERMINISTIC_ATOMS_V0 | REUSE |  | Governs the model's offer: recorded when produced, replayed from the record, offered to a deterministic step. | S6 pps_artifacts_requiring_action capability_transforms::CONSTITUTION_NONDETERMINISTIC_ATOMS_V0 |

---

## 3. Artifact Family Mapping — New Artifacts

<!-- register:new_artifacts business_language=capability -->
| Capability | Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE) | Code | Summary | Owner Subdomain | Status | Source Finding |
|------------|---------------------------------------------------------------|------|---------|-----------------|--------|----------------|
| The authorized model staff member who registers, places, withdraws and retrieves | AC | causal_language_model::AC_MODEL_STAFF_V0 | The actor whose authorization every model staff operation binds | model_response | NEW | S5 provisional_codes AC_MODEL_STAFF_V0 |
| The authorized requester who submits a user prompt on behalf of a customer | AC | causal_language_model::AC_REQUESTER_V0 | The actor who submits a user prompt for one customer | model_response | NEW | S5 provisional_codes AC_REQUESTER_V0 |
| A request to register a model with its description and fingerprint | IN | causal_language_model::IN_REGISTER_MODEL_V0 | A request to register a model with its description and fingerprint | model_response | NEW | S5 provisional_codes IN_REGISTER_MODEL_V0 |
| A request to place a registered model in service with its ceiling, system prompt and response rules | IN | causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0 | A request to place a registered model in service with its ceiling, system prompt and response rules | model_response | NEW | S5 provisional_codes IN_PLACE_MODEL_IN_SERVICE_V0 |
| A request to withdraw a model from service | IN | causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0 | A request to withdraw a model from service | model_response | NEW | S5 provisional_codes IN_WITHDRAW_MODEL_FROM_SERVICE_V0 |
| A user prompt submitted on behalf of a customer | IN | causal_language_model::IN_SUBMIT_USER_PROMPT_V0 | A user prompt submitted on behalf of a customer | model_response | NEW | S5 provisional_codes IN_SUBMIT_USER_PROMPT_V0 |
| A request to retrieve the record of a user prompt | IN | causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0 | A request to retrieve the record of a user prompt | model_response | NEW | S5 provisional_codes IN_RETRIEVE_USER_PROMPT_RECORD_V0 |
| Registering a model, refusing a second registration of the same model | WF | causal_language_model::WF_REGISTER_MODEL_V0 | Registering a model, refusing a second registration of the same model | model_response | NEW | S5 provisional_codes WF_REGISTER_MODEL_V0 |
| Opening a time in service for a registered model not already in service | WF | causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0 | Opening a time in service for a registered model not already in service | model_response | NEW | S5 provisional_codes WF_PLACE_MODEL_IN_SERVICE_V0 |
| Closing a model's time in service | WF | causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0 | Closing a model's time in service | model_response | NEW | S5 provisional_codes WF_WITHDRAW_MODEL_FROM_SERVICE_V0 |
| Admitting a user prompt, writing the response under the rules, releasing or refusing it, and recording it | WF | causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | Admitting a user prompt, writing the response under the rules, releasing or refusing it, and recording it | model_response | NEW | S5 provisional_codes WF_SUBMIT_USER_PROMPT_V0 |
| Reading a user prompt record and recording that it was read | WF | causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0 | Reading a user prompt record and recording that it was read | model_response | NEW | S5 provisional_codes WF_RETRIEVE_USER_PROMPT_RECORD_V0 |
| Confirm the staff member is model staff | CC | causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 | Confirm the staff member is model staff | model_response | NEW | S5 provisional_codes CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 |
| Confirm the requester may act for the customer the user prompt is for | CC | causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0 | Confirm the requester may act for the customer the user prompt is for | model_response | NEW | S5 provisional_codes CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0 |
| Claim a model's identity so a second registration of the same model is refused | CC | causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0 | Claim a model's identity so a second registration of the same model is refused | model_response | NEW | S5 provisional_codes CC_CLAIM_MODEL_IDENTITY_V0 |
| Record a model's description and fingerprint as its record, registered | CC | causal_language_model::CC_REGISTER_MODEL_V0 | Record a model's description and fingerprint as its record, registered | model_response | NEW | S5 provisional_codes CC_REGISTER_MODEL_V0 |
| Open a time in service with its ceiling, system prompt and response rules, and mark the model in service | CC | causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | Open a time in service with its ceiling, system prompt and response rules, and mark the model in service | model_response | NEW | S5 provisional_codes CC_PLACE_MODEL_IN_SERVICE_V0 |
| Close the time in service and mark the model registered | CC | causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0 | Close the time in service and mark the model registered | model_response | NEW | S5 provisional_codes CC_WITHDRAW_MODEL_FROM_SERVICE_V0 |
| Refuse a user prompt whose model is not registered or not in service | CC | causal_language_model::CC_ADMIT_USER_PROMPT_V0 | Refuse a user prompt before the model sees it when its model is not registered or not in service | model_response | NEW | S5 provisional_codes CC_ADMIT_USER_PROMPT_V0 |
| Refuse a user prompt whose kind of information is above the model's ceiling | CC | causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 | Refuse a user prompt before the model sees it when it states a kind more sensitive than the ceiling | model_response | NEW | S5 provisional_codes CC_ADMIT_USER_PROMPT_V0 |
| Refuse a user prompt longer than the model can read at once | CC | causal_language_model::CC_CONFIRM_READING_FITS_V0 | Assemble exactly what the model reads and refuse it before the model sees it when it is too long | model_response | NEW | S5 provisional_codes CC_ADMIT_USER_PROMPT_V0 |
| Write the response word by word under the rules in force | CC | causal_language_model::CC_WRITE_MODEL_RESPONSE_V0 | Form the rules in force and write the response word by word under them | model_response | NEW | S5 provisional_codes CC_WRITE_MODEL_RESPONSE_V0 |
| Release a written response only when it finished and no rule stopped it | CC | causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0 | Confirm one release condition of a written response, refusing it otherwise | model_response | NEW | S5 provisional_codes CC_WRITE_MODEL_RESPONSE_V0 |
| Append the user prompt record with what the model read, the rules in force and the outcome | CC | causal_language_model::CC_RECORD_USER_PROMPT_V0 | Append the user prompt record with what the model read, the rules in force and the outcome | model_response | NEW | S5 provisional_codes CC_RECORD_USER_PROMPT_V0 |
| Read the record of a user prompt | CC | causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0 | Read the record of a user prompt | model_response | NEW | S5 provisional_codes CC_RETRIEVE_USER_PROMPT_RECORD_V0 |
| Append a durable account of a performed operation to the subdomain's own trail | CC | causal_language_model::CC_APPEND_MODEL_OPERATION_V0 | Append a durable account of a performed operation to the subdomain's own trail | model_response | NEW | S5 provisional_codes CC_APPEND_MODEL_OPERATION_V0 |
| Form the single key claimed for a model from its description and fingerprint | CT | causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0 | Forms the single key claimed for a model from its description and fingerprint | model_response | NEW | S5 provisional_codes CT_PURE_FORM_MODEL_IDENTITY_KEY_V0 |
| Decide whether a kind of information is no more sensitive than a ceiling | CT | causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0 | Decides whether a kind of information is no more sensitive than a ceiling, by the declared order | model_response | NEW | S5 provisional_codes CT_PURE_COMPARE_SENSITIVITY_V0 |
| Assemble exactly what the model reads and decide whether it fits | CT | causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0 | Assembles exactly what the model reads and decides whether it fits what the model can read at once | model_response | NEW | S5 provisional_codes CT_PURE_ASSEMBLE_MODEL_READING_V0 |
| Form the response rules in force for one user prompt | CT | causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0 | Forms the response rules in force for one user prompt from the time in service and the customer's account numbers | model_response | NEW | S5 provisional_codes CT_PURE_FORM_RESPONSE_RULES_V0 |
| The model's offer of its next words | CT | causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0 | The model's step: offers its next words given the response so far; the one step whose result is not determined by its inputs | model_response | NEW | S5 provisional_codes CT_IMPURE_OFFER_NEXT_WORDS_V0 |
| Stop forbidden words and choose one permitted word | CT | causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | Stops forbidden words among those offered and chooses one permitted word under the freedom of word choice and a stated seed | model_response | NEW | S5 provisional_codes CT_PURE_CHOOSE_PERMITTED_WORD_V0 |
| One pass of writing: the model's offer, then the rules' choice | CT | causal_language_model::CT_WRITE_NEXT_WORD_V0 | One pass of writing, composed of the model's offer and the rules' choice | model_response | NEW | S5 provisional_codes CT_WRITE_NEXT_WORD_V0 |
| Write a response one pass per word, up to the longest response | CT | causal_language_model::CT_WRITE_RESPONSE_V0 | Writes a response by repeating one pass per word, up to the longest response, carrying the response so far and the words stopped | model_response | NEW | S5 provisional_codes CT_WRITE_RESPONSE_V0 |
| The moment the business records a model | EV | causal_language_model::EV_MODEL_REGISTERED_V0 | The moment the business records a model | model_response | NEW | S5 provisional_codes EV_MODEL_REGISTERED_V0 |
| The moment a model is placed in service and a time in service begins | EV | causal_language_model::EV_MODEL_SERVICE_STARTED_V0 | The moment a model is placed in service and a time in service begins | model_response | NEW | S5 provisional_codes EV_MODEL_SERVICE_STARTED_V0 |
| The moment a model is withdrawn from service and its time in service ends | EV | causal_language_model::EV_MODEL_SERVICE_ENDED_V0 | The moment a model is withdrawn from service and its time in service ends | model_response | NEW | S5 provisional_codes EV_MODEL_SERVICE_ENDED_V0 |
| The moment a model response is released | EV | causal_language_model::EV_USER_PROMPT_RESPONDED_V0 | The moment a model response is released | model_response | NEW | S5 provisional_codes EV_USER_PROMPT_RESPONDED_V0 |
| The moment a user prompt yields no response | EV | causal_language_model::EV_USER_PROMPT_REFUSED_V0 | The moment a user prompt yields no response | model_response | NEW | S5 provisional_codes EV_USER_PROMPT_REFUSED_V0 |
| The kinds of information, least sensitive first | VOCAB | causal_language_model::VOCAB_KIND_OF_INFORMATION_V0 | The kinds of information, least sensitive first: public, internal, confidential, restricted | model_response | NEW | S5 provisional_codes VOCAB_KIND_OF_INFORMATION_V0 |
| Bind the subdomain's operations to the stores and mechanisms they use | RB | causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0 | Binds every model response workflow to the mechanisms and stores it uses | model_response | NEW | S5 provisional_codes RB_MODEL_RESPONSE_BINDINGS_V0 |
| Declare the stores the subdomain owns | STRUCTURE | causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0 | Declares the five stores the subdomain owns and the paths they occupy | model_response | NEW | S5 provisional_codes STRUCTURE_MODEL_RESPONSE_STORAGE_V0 |

---

## 4. Runtime Binding (RB) Declarations

<!-- register:rb_declarations -->
| RB Code | Binds WF | CS Bindings | Storage Structure | Source Finding |
|---------|----------|-------------|-------------------|----------------|
| causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0 | causal_language_model::WF_REGISTER_MODEL_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0 | S6 storage_governance A durable record of every model the business holds |
| causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0 | causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0 | S6 storage_governance A durable record of every model the business holds |
| causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0 | causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0 | S6 storage_governance A durable record of every model the business holds |
| causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0 | causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0 | S6 storage_governance A durable record of every model the business holds |
| causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0 | causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0 | capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_APPENDONLY_JSONL_V0 | causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0 | S6 storage_governance A durable record of every model the business holds |

---

## 5. Execution Topology

Every refusal of a submission is recorded before the act ends. The recording contract runs at eight
places in the submission, one per outcome, each handed its own outcome and reason; `Runs` names the
contract and `Node` names the place. The two release conditions run one contract at two places the
same way.

<!-- register:execution_topology optional_columns=runs -->
| Workflow | Node | Runs | Node Type (IN, CC, EXIT, EXIT_SUCCESS) | Routing | Source Finding |
|----------|------|------|----------------------------------------|---------|----------------|
| causal_language_model::WF_REGISTER_MODEL_V0 | causal_language_model::IN_REGISTER_MODEL_V0 |  | IN | ACK -> causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_REGISTER_MODEL_V0 |
| causal_language_model::WF_REGISTER_MODEL_V0 | causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 |  | CC | SUCCESS -> causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0; VIOLATION -> EXIT_REJECTED | S7 new_artifacts CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 |
| causal_language_model::WF_REGISTER_MODEL_V0 | causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0 |  | CC | SUCCESS -> causal_language_model::CC_REGISTER_MODEL_V0; ALREADY_EXISTS -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_CLAIM_MODEL_IDENTITY_V0 |
| causal_language_model::WF_REGISTER_MODEL_V0 | causal_language_model::CC_REGISTER_MODEL_V0 |  | CC | SUCCESS -> causal_language_model::CC_APPEND_MODEL_OPERATION_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_REGISTER_MODEL_V0 |
| causal_language_model::WF_REGISTER_MODEL_V0 | causal_language_model::CC_APPEND_MODEL_OPERATION_V0 |  | CC | SUCCESS -> EXIT_REGISTERED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_APPEND_MODEL_OPERATION_V0 |
| causal_language_model::WF_REGISTER_MODEL_V0 | EXIT_REGISTERED |  | EXIT_SUCCESS | — | S7 execution_topology WF_REGISTER_MODEL_V0 |
| causal_language_model::WF_REGISTER_MODEL_V0 | EXIT_REJECTED |  | EXIT | — | S7 execution_topology WF_REGISTER_MODEL_V0 |
| causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0 | causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0 |  | IN | ACK -> causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_PLACE_MODEL_IN_SERVICE_V0 |
| causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0 | causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 |  | CC | SUCCESS -> causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0; VIOLATION -> EXIT_REJECTED | S7 new_artifacts CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 |
| causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0 | causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 |  | CC | SUCCESS -> causal_language_model::CC_APPEND_MODEL_OPERATION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_PLACE_MODEL_IN_SERVICE_V0 |
| causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0 | causal_language_model::CC_APPEND_MODEL_OPERATION_V0 |  | CC | SUCCESS -> EXIT_PLACED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_APPEND_MODEL_OPERATION_V0 |
| causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0 | EXIT_PLACED |  | EXIT_SUCCESS | — | S7 execution_topology WF_PLACE_MODEL_IN_SERVICE_V0 |
| causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0 | EXIT_REJECTED |  | EXIT | — | S7 execution_topology WF_PLACE_MODEL_IN_SERVICE_V0 |
| causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0 | causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0 |  | IN | ACK -> causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_WITHDRAW_MODEL_FROM_SERVICE_V0 |
| causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0 | causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 |  | CC | SUCCESS -> causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0; VIOLATION -> EXIT_REJECTED | S7 new_artifacts CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 |
| causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0 | causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0 |  | CC | SUCCESS -> causal_language_model::CC_APPEND_MODEL_OPERATION_V0; NOT_FOUND -> EXIT_REJECTED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_WITHDRAW_MODEL_FROM_SERVICE_V0 |
| causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0 | causal_language_model::CC_APPEND_MODEL_OPERATION_V0 |  | CC | SUCCESS -> EXIT_WITHDRAWN; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_APPEND_MODEL_OPERATION_V0 |
| causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0 | EXIT_WITHDRAWN |  | EXIT_SUCCESS | — | S7 execution_topology WF_WITHDRAW_MODEL_FROM_SERVICE_V0 |
| causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0 | EXIT_REJECTED |  | EXIT | — | S7 execution_topology WF_WITHDRAW_MODEL_FROM_SERVICE_V0 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | causal_language_model::IN_SUBMIT_USER_PROMPT_V0 |  | IN | ACK -> causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_SUBMIT_USER_PROMPT_V0 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0 |  | CC | SUCCESS -> causal_language_model::CC_ADMIT_USER_PROMPT_V0; VIOLATION -> RECORD_REFUSED_NOT_PERMITTED | S7 new_artifacts CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | causal_language_model::CC_ADMIT_USER_PROMPT_V0 |  | CC | SUCCESS -> causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0; NOT_FOUND -> RECORD_REFUSED_NOT_REGISTERED; VIOLATION -> RECORD_REFUSED_NOT_IN_SERVICE; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_ADMIT_USER_PROMPT_V0 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 |  | CC | SUCCESS -> causal_language_model::CC_CONFIRM_READING_FITS_V0; NOT_FOUND -> RECORD_REFUSED_NOT_IN_SERVICE; VIOLATION -> RECORD_REFUSED_ABOVE_CEILING; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_CONFIRM_WITHIN_CEILING_V0 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | causal_language_model::CC_CONFIRM_READING_FITS_V0 |  | CC | SUCCESS -> causal_language_model::CC_WRITE_MODEL_RESPONSE_V0; VIOLATION -> RECORD_REFUSED_TOO_LONG_TO_READ | S7 new_artifacts CC_CONFIRM_READING_FITS_V0 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | causal_language_model::CC_WRITE_MODEL_RESPONSE_V0 |  | CC | SUCCESS -> CONFIRM_NO_RULE_STOPPED; VIOLATION -> EXIT_REJECTED | S7 new_artifacts CC_WRITE_MODEL_RESPONSE_V0 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | CONFIRM_NO_RULE_STOPPED | causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0 | CC | SUCCESS -> CONFIRM_FINISHED; VIOLATION -> RECORD_REFUSED_BY_RULE | S7 new_artifacts CC_CONFIRM_RESPONSE_RELEASABLE_V0 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | CONFIRM_FINISHED | causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0 | CC | SUCCESS -> RECORD_RESPONDED; VIOLATION -> RECORD_REFUSED_UNFINISHED | S7 new_artifacts CC_CONFIRM_RESPONSE_RELEASABLE_V0 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_RESPONDED | causal_language_model::CC_RECORD_USER_PROMPT_V0 | CC | SUCCESS -> EXIT_RESPONDED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_RECORD_USER_PROMPT_V0 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_NOT_PERMITTED | causal_language_model::CC_RECORD_USER_PROMPT_V0 | CC | SUCCESS -> EXIT_REFUSED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_RECORD_USER_PROMPT_V0 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_NOT_REGISTERED | causal_language_model::CC_RECORD_USER_PROMPT_V0 | CC | SUCCESS -> EXIT_REFUSED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_RECORD_USER_PROMPT_V0 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_NOT_IN_SERVICE | causal_language_model::CC_RECORD_USER_PROMPT_V0 | CC | SUCCESS -> EXIT_REFUSED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_RECORD_USER_PROMPT_V0 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_ABOVE_CEILING | causal_language_model::CC_RECORD_USER_PROMPT_V0 | CC | SUCCESS -> EXIT_REFUSED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_RECORD_USER_PROMPT_V0 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | causal_language_model::CC_RECORD_USER_PROMPT_V0 | CC | SUCCESS -> EXIT_REFUSED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_RECORD_USER_PROMPT_V0 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_BY_RULE | causal_language_model::CC_RECORD_USER_PROMPT_V0 | CC | SUCCESS -> EXIT_REFUSED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_RECORD_USER_PROMPT_V0 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_UNFINISHED | causal_language_model::CC_RECORD_USER_PROMPT_V0 | CC | SUCCESS -> EXIT_REFUSED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_RECORD_USER_PROMPT_V0 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | EXIT_RESPONDED |  | EXIT_SUCCESS | — | S7 execution_topology WF_SUBMIT_USER_PROMPT_V0 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | EXIT_REFUSED |  | EXIT | — | S7 execution_topology WF_SUBMIT_USER_PROMPT_V0 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | EXIT_REJECTED |  | EXIT | — | S7 execution_topology WF_SUBMIT_USER_PROMPT_V0 |
| causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0 | causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0 |  | IN | ACK -> causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0; NACK -> EXIT_REJECTED | S7 new_artifacts IN_RETRIEVE_USER_PROMPT_RECORD_V0 |
| causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0 | causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 |  | CC | SUCCESS -> causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0; VIOLATION -> EXIT_REJECTED | S7 new_artifacts CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 |
| causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0 | causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0 |  | CC | SUCCESS -> causal_language_model::CC_APPEND_MODEL_OPERATION_V0; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_RETRIEVE_USER_PROMPT_RECORD_V0 |
| causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0 | causal_language_model::CC_APPEND_MODEL_OPERATION_V0 |  | CC | SUCCESS -> EXIT_RETRIEVED; VIOLATION -> EXIT_REJECTED; BACKEND_ERROR -> EXIT_REJECTED | S7 new_artifacts CC_APPEND_MODEL_OPERATION_V0 |
| causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0 | EXIT_RETRIEVED |  | EXIT_SUCCESS | — | S7 execution_topology WF_RETRIEVE_USER_PROMPT_RECORD_V0 |
| causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0 | EXIT_REJECTED |  | EXIT | — | S7 execution_topology WF_RETRIEVE_USER_PROMPT_RECORD_V0 |

---

## 6. Capability Composition

<!-- register:cc_composition optional -->
| CC Code | Step | Step Name | Capability | Kind (CT, CS) | Operation | Store | Consumes | Produces | Routing | Interpreted By | Semantic Status | Interface |
|---------|------|-----------|------------|---------------|-----------|-------|----------|----------|---------|----------------|-----------------|-----------|
| causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 | 1 | confirm_authorization | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | CT | VALIDATE_PARAMETER_RULES | — | staff_credentials, authorization_rules | is_authorized | SUCCESS -> exit; VIOLATION -> exit | — | SUCCESS | in: parameters=staff_credentials, rules=authorization_rules; out: valid=is_authorized |
| causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0 | 1 | confirm_acts_for_customer | capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 | CT | VALIDATE_SET_MEMBERSHIP | — | customer_id, permitted_customers | acts_for_customer | SUCCESS -> exit; VIOLATION -> exit | — | SUCCESS | in: value=customer_id, allowed_set=permitted_customers; out: is_member=acts_for_customer |
| causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0 | 1 | form_identity_key | causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0 | CT | FORM_MODEL_IDENTITY_KEY | — | description, fingerprint | identity_key | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: description=description, fingerprint=fingerprint; out: identity_key=identity_key |
| causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0 | 2 | claim_identity | capability_side_effects::CS_REGISTRY_V0 | CS | REGISTER | MODEL_IDENTITY_REGISTRY | key, target_cs, target_ref | address | SUCCESS -> exit; ALREADY_EXISTS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | ALREADY_EXISTS | — |
| causal_language_model::CC_REGISTER_MODEL_V0 | 1 | validate_description | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | CT | VALIDATE_RECORD_STRUCTURE | — | description, description_schema | violations | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: record=description, schema=description_schema; out: violations=violations |
| causal_language_model::CC_REGISTER_MODEL_V0 | 2 | assemble_model_record | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | CT | ASSEMBLE_RECORD | — | identity_key, description, fingerprint | model_record | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: fields=model_fields; out: record=model_record |
| causal_language_model::CC_REGISTER_MODEL_V0 | 3 | write_model_record | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | WRITE | MODELS | key, value | result_status | SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | — |
| causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | 1 | read_model_record | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | READ | MODELS | key | model_record | SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | NOT_FOUND | — |
| causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | 2 | require_registered | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | CT | VALIDATE_PARAMETER_RULES | — | model_record | valid | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: parameters=model_state, rules=state_rules; out: valid=valid |
| causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | 3 | confirm_ceiling_declared | capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 | CT | VALIDATE_SET_MEMBERSHIP | — | ceiling | ceiling_declared | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: value=ceiling, allowed_set=kinds; out: is_member=ceiling_declared |
| causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | 4 | assemble_time_in_service | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | CT | ASSEMBLE_RECORD | — | time_in_service_id, identity_key, ceiling, system_prompt, response_rules | time_in_service | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: fields=time_in_service_fields; out: record=time_in_service |
| causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | 5 | write_time_in_service | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | WRITE | TIMES_IN_SERVICE | key, value | result_status | SUCCESS -> continue; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | — |
| causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | 6 | mark_in_service | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | UPDATE | MODELS | key, updates | result_status | SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | — |
| causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0 | 1 | read_model_record | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | READ | MODELS | key | model_record | SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | NOT_FOUND | — |
| causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0 | 2 | require_in_service | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | CT | VALIDATE_PARAMETER_RULES | — | model_record | valid | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: parameters=model_state, rules=state_rules; out: valid=valid |
| causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0 | 3 | close_time_in_service | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | UPDATE | TIMES_IN_SERVICE | key, updates | result_status | SUCCESS -> continue; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | — |
| causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0 | 4 | mark_registered | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | UPDATE | MODELS | key, updates | result_status | SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | — |
| causal_language_model::CC_ADMIT_USER_PROMPT_V0 | 1 | read_model_record | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | READ | MODELS | key | model_record | SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | NOT_FOUND | — |
| causal_language_model::CC_ADMIT_USER_PROMPT_V0 | 2 | require_in_service | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | CT | VALIDATE_PARAMETER_RULES | — | model_record | valid | SUCCESS -> exit; VIOLATION -> exit | — | SUCCESS | in: parameters=model_state, rules=state_rules; out: valid=valid |
| causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 | 1 | read_time_in_service | capability_side_effects::CS_MUTABLE_JSON_V0 | CS | READ | TIMES_IN_SERVICE | key | time_in_service | SUCCESS -> continue; NOT_FOUND -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | NOT_FOUND | — |
| causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 | 2 | confirm_kind_declared | capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 | CT | VALIDATE_SET_MEMBERSHIP | — | kind | kind_declared | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: value=kind, allowed_set=kinds; out: is_member=kind_declared |
| causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 | 3 | compare_sensitivity | causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0 | CT | COMPARE_SENSITIVITY | — | kind, time_in_service | within_ceiling | SUCCESS -> exit; VIOLATION -> exit | — | SUCCESS | in: kind=kind, ceiling=ceiling, kinds=kinds; out: within_ceiling=within_ceiling |
| causal_language_model::CC_CONFIRM_READING_FITS_V0 | 1 | assemble_reading | causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0 | CT | ASSEMBLE_MODEL_READING | — | system_prompt, question, supporting_material, reading_capacity | reading, reading_length | SUCCESS -> exit; VIOLATION -> exit | — | SUCCESS | in: system_prompt=system_prompt, question=question, supporting_material=supporting_material, reading_capacity=reading_capacity; out: reading=reading, reading_length=reading_length |
| causal_language_model::CC_WRITE_MODEL_RESPONSE_V0 | 1 | form_rules_in_force | causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0 | CT | FORM_RESPONSE_RULES | — | response_rules, account_numbers, seed | rules_in_force, positions | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: response_rules=response_rules, account_numbers=account_numbers, seed=seed; out: rules_in_force=rules_in_force, positions=positions |
| causal_language_model::CC_WRITE_MODEL_RESPONSE_V0 | 2 | write_response | causal_language_model::CT_WRITE_RESPONSE_V0 | CT | WRITE_RESPONSE | — | reading, rules_in_force, positions | written_response | SUCCESS -> exit; VIOLATION -> exit | — | SUCCESS | in: reading=reading, rules_in_force=rules_in_force, positions=positions; out: result=written_response |
| causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0 | 1 | confirm_releasable | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | CT | VALIDATE_PARAMETER_RULES | — | release_facts, release_rules | releasable | SUCCESS -> exit; VIOLATION -> exit | — | SUCCESS | in: parameters=release_facts, rules=release_rules; out: valid=releasable |
| causal_language_model::CC_RECORD_USER_PROMPT_V0 | 1 | assemble_user_prompt_record | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | CT | ASSEMBLE_RECORD | — | user_prompt_id, requester_id, customer_id, identity_key, kind, question, supporting_material, outcome, time_in_service_id, reading, rules_in_force, response, reason | user_prompt_record | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: fields=user_prompt_fields; out: record=user_prompt_record |
| causal_language_model::CC_RECORD_USER_PROMPT_V0 | 2 | append_user_prompt_record | capability_side_effects::CS_APPENDONLY_JSONL_V0 | CS | APPEND | USER_PROMPT_RECORDS | record, stream_id, actor_id | record_id, sequence_number | SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | — |
| causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0 | 1 | read_user_prompt_entries | capability_side_effects::CS_APPENDONLY_JSONL_V0 | CS | GET_ALL | USER_PROMPT_RECORDS | stream_id | entries | SUCCESS -> continue; BACKEND_ERROR -> exit | — | SUCCESS | — |
| causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0 | 2 | select_user_prompt_record | capability_transforms::CT_PURE_FILTER_RECORDS_V0 | CT | FILTER_RECORDS | — | entries, record_criteria | user_prompt_record | SUCCESS -> exit; VIOLATION -> exit | — | SUCCESS | in: source=entries, filter=record_criteria; out: extracted=user_prompt_record |
| causal_language_model::CC_APPEND_MODEL_OPERATION_V0 | 1 | append_operation | capability_side_effects::CS_APPENDONLY_JSONL_V0 | CS | APPEND | MODEL_OPERATIONS | record, stream_id, actor_id | record_id, sequence_number | SUCCESS -> exit; VIOLATION -> exit; BACKEND_ERROR -> exit | — | SUCCESS | — |

---

## 7. Step Bindings

<!-- register:step_bindings optional -->
| Owner | Step | Direction (INPUT, OUTPUT) | Field | Bound To | Source Finding |
|-------|------|---------------------------|-------|----------|----------------|
| causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 | confirm_authorization | INPUT | parameters | inputs.staff_credentials | S7 cc_composition confirm_authorization |
| causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 | confirm_authorization | INPUT | rules | inputs.authorization_rules | S7 cc_composition confirm_authorization |
| causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 | confirm_authorization | OUTPUT | is_authorized | capability_result.valid | S7 cc_composition confirm_authorization |
| causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0 | confirm_acts_for_customer | INPUT | value | inputs.customer_id | S7 cc_composition confirm_acts_for_customer |
| causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0 | confirm_acts_for_customer | INPUT | allowed_set | inputs.permitted_customers | S7 cc_composition confirm_acts_for_customer |
| causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0 | confirm_acts_for_customer | OUTPUT | acts_for_customer | capability_result.is_member | S7 cc_composition confirm_acts_for_customer |
| causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0 | form_identity_key | INPUT | description | inputs.description | S7 cc_composition form_identity_key |
| causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0 | form_identity_key | INPUT | fingerprint | inputs.fingerprint | S7 cc_composition form_identity_key |
| causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0 | form_identity_key | OUTPUT | identity_key | capability_result.identity_key | S7 cc_composition form_identity_key |
| causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0 | claim_identity | INPUT | key | results.form_identity_key.identity_key | S7 cc_composition claim_identity |
| causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0 | claim_identity | INPUT | target_cs | CS_MUTABLE_JSON_V0 | S7 cc_composition claim_identity |
| causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0 | claim_identity | INPUT | target_ref | MODELS | S7 cc_composition claim_identity |
| causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0 | claim_identity | OUTPUT | address | capability_result.address | S7 cc_composition claim_identity |
| causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0 | claim_identity | OUTPUT | result_status | result_status | S7 cc_composition claim_identity |
| causal_language_model::CC_REGISTER_MODEL_V0 | validate_description | INPUT | record | inputs.description | S7 cc_composition validate_description |
| causal_language_model::CC_REGISTER_MODEL_V0 | validate_description | INPUT | schema | inputs.description_schema | S7 cc_composition validate_description |
| causal_language_model::CC_REGISTER_MODEL_V0 | validate_description | OUTPUT | violations | capability_result.violations | S7 cc_composition validate_description |
| causal_language_model::CC_REGISTER_MODEL_V0 | assemble_model_record | INPUT | fields | {'identity_key': '$.inputs.identity_key', 'description': '$.inputs.description', 'fingerprint': '$.inputs.fingerprint', 'state': 'REGISTERED', 'time_in_service_id': ''} | S7 cc_composition assemble_model_record |
| causal_language_model::CC_REGISTER_MODEL_V0 | assemble_model_record | OUTPUT | model_record | capability_result.record | S7 cc_composition assemble_model_record |
| causal_language_model::CC_REGISTER_MODEL_V0 | write_model_record | INPUT | key | inputs.identity_key | S7 cc_composition write_model_record |
| causal_language_model::CC_REGISTER_MODEL_V0 | write_model_record | INPUT | value | results.assemble_model_record.model_record | S7 cc_composition write_model_record |
| causal_language_model::CC_REGISTER_MODEL_V0 | write_model_record | OUTPUT | result_status | result_status | S7 cc_composition write_model_record |
| causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | read_model_record | INPUT | key | inputs.identity_key | S7 cc_composition read_model_record |
| causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | read_model_record | OUTPUT | model_record | capability_result.value | S7 cc_composition read_model_record |
| causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | read_model_record | OUTPUT | result_status | result_status | S7 cc_composition read_model_record |
| causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | require_registered | INPUT | parameters | {'state': '$.results.read_model_record.model_record.state'} | S7 cc_composition require_registered |
| causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | require_registered | INPUT | rules | [{'field': 'state', 'op': 'eq', 'value': 'REGISTERED'}] | S7 cc_composition require_registered |
| causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | require_registered | OUTPUT | valid | capability_result.valid | S7 cc_composition require_registered |
| causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | confirm_ceiling_declared | INPUT | value | inputs.ceiling | S7 cc_composition confirm_ceiling_declared |
| causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | confirm_ceiling_declared | INPUT | allowed_set | ['public', 'internal', 'confidential', 'restricted'] | S7 cc_composition confirm_ceiling_declared |
| causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | confirm_ceiling_declared | OUTPUT | ceiling_declared | capability_result.is_member | S7 cc_composition confirm_ceiling_declared |
| causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | assemble_time_in_service | INPUT | fields | {'time_in_service_id': '$.inputs.time_in_service_id', 'identity_key': '$.inputs.identity_key', 'ceiling': '$.inputs.ceiling', 'system_prompt': '$.inputs.system_prompt', 'response_rules': '$.inputs.response_rules', 'state': 'OPEN'} | S7 cc_composition assemble_time_in_service |
| causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | assemble_time_in_service | OUTPUT | time_in_service | capability_result.record | S7 cc_composition assemble_time_in_service |
| causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | write_time_in_service | INPUT | key | inputs.time_in_service_id | S7 cc_composition write_time_in_service |
| causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | write_time_in_service | INPUT | value | results.assemble_time_in_service.time_in_service | S7 cc_composition write_time_in_service |
| causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | write_time_in_service | OUTPUT | result_status | result_status | S7 cc_composition write_time_in_service |
| causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | mark_in_service | INPUT | key | inputs.identity_key | S7 cc_composition mark_in_service |
| causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | mark_in_service | INPUT | updates | {'state': 'IN_SERVICE', 'time_in_service_id': '$.inputs.time_in_service_id'} | S7 cc_composition mark_in_service |
| causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | mark_in_service | OUTPUT | result_status | result_status | S7 cc_composition mark_in_service |
| causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0 | read_model_record | INPUT | key | inputs.identity_key | S7 cc_composition read_model_record |
| causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0 | read_model_record | OUTPUT | model_record | capability_result.value | S7 cc_composition read_model_record |
| causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0 | read_model_record | OUTPUT | result_status | result_status | S7 cc_composition read_model_record |
| causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0 | require_in_service | INPUT | parameters | {'state': '$.results.read_model_record.model_record.state'} | S7 cc_composition require_in_service |
| causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0 | require_in_service | INPUT | rules | [{'field': 'state', 'op': 'eq', 'value': 'IN_SERVICE'}] | S7 cc_composition require_in_service |
| causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0 | require_in_service | OUTPUT | valid | capability_result.valid | S7 cc_composition require_in_service |
| causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0 | close_time_in_service | INPUT | key | results.read_model_record.model_record.time_in_service_id | S7 cc_composition close_time_in_service |
| causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0 | close_time_in_service | INPUT | updates | {'state': 'CLOSED'} | S7 cc_composition close_time_in_service |
| causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0 | close_time_in_service | OUTPUT | result_status | result_status | S7 cc_composition close_time_in_service |
| causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0 | mark_registered | INPUT | key | inputs.identity_key | S7 cc_composition mark_registered |
| causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0 | mark_registered | INPUT | updates | {'state': 'REGISTERED', 'time_in_service_id': ''} | S7 cc_composition mark_registered |
| causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0 | mark_registered | OUTPUT | result_status | result_status | S7 cc_composition mark_registered |
| causal_language_model::CC_ADMIT_USER_PROMPT_V0 | read_model_record | INPUT | key | inputs.identity_key | S7 cc_composition read_model_record |
| causal_language_model::CC_ADMIT_USER_PROMPT_V0 | read_model_record | OUTPUT | model_record | capability_result.value | S7 cc_composition read_model_record |
| causal_language_model::CC_ADMIT_USER_PROMPT_V0 | read_model_record | OUTPUT | result_status | result_status | S7 cc_composition read_model_record |
| causal_language_model::CC_ADMIT_USER_PROMPT_V0 | require_in_service | INPUT | parameters | {'state': '$.results.read_model_record.model_record.state'} | S7 cc_composition require_in_service |
| causal_language_model::CC_ADMIT_USER_PROMPT_V0 | require_in_service | INPUT | rules | [{'field': 'state', 'op': 'eq', 'value': 'IN_SERVICE'}] | S7 cc_composition require_in_service |
| causal_language_model::CC_ADMIT_USER_PROMPT_V0 | require_in_service | OUTPUT | valid | capability_result.valid | S7 cc_composition require_in_service |
| causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 | read_time_in_service | INPUT | key | inputs.time_in_service_id | S7 cc_composition read_time_in_service |
| causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 | read_time_in_service | OUTPUT | time_in_service | capability_result.value | S7 cc_composition read_time_in_service |
| causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 | read_time_in_service | OUTPUT | result_status | result_status | S7 cc_composition read_time_in_service |
| causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 | confirm_kind_declared | INPUT | value | inputs.kind | S7 cc_composition confirm_kind_declared |
| causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 | confirm_kind_declared | INPUT | allowed_set | ['public', 'internal', 'confidential', 'restricted'] | S7 cc_composition confirm_kind_declared |
| causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 | confirm_kind_declared | OUTPUT | kind_declared | capability_result.is_member | S7 cc_composition confirm_kind_declared |
| causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 | compare_sensitivity | INPUT | kind | inputs.kind | S7 cc_composition compare_sensitivity |
| causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 | compare_sensitivity | INPUT | ceiling | results.read_time_in_service.time_in_service.ceiling | S7 cc_composition compare_sensitivity |
| causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 | compare_sensitivity | INPUT | kinds | ['public', 'internal', 'confidential', 'restricted'] | S7 cc_composition compare_sensitivity |
| causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 | compare_sensitivity | OUTPUT | within_ceiling | capability_result.within_ceiling | S7 cc_composition compare_sensitivity |
| causal_language_model::CC_CONFIRM_READING_FITS_V0 | assemble_reading | INPUT | system_prompt | inputs.system_prompt | S7 cc_composition assemble_reading |
| causal_language_model::CC_CONFIRM_READING_FITS_V0 | assemble_reading | INPUT | question | inputs.question | S7 cc_composition assemble_reading |
| causal_language_model::CC_CONFIRM_READING_FITS_V0 | assemble_reading | INPUT | supporting_material | inputs.supporting_material | S7 cc_composition assemble_reading |
| causal_language_model::CC_CONFIRM_READING_FITS_V0 | assemble_reading | INPUT | reading_capacity | inputs.reading_capacity | S7 cc_composition assemble_reading |
| causal_language_model::CC_CONFIRM_READING_FITS_V0 | assemble_reading | OUTPUT | reading | capability_result.reading | S7 cc_composition assemble_reading |
| causal_language_model::CC_CONFIRM_READING_FITS_V0 | assemble_reading | OUTPUT | reading_length | capability_result.reading_length | S7 cc_composition assemble_reading |
| causal_language_model::CC_WRITE_MODEL_RESPONSE_V0 | form_rules_in_force | INPUT | response_rules | inputs.response_rules | S7 cc_composition form_rules_in_force |
| causal_language_model::CC_WRITE_MODEL_RESPONSE_V0 | form_rules_in_force | INPUT | account_numbers | inputs.account_numbers | S7 cc_composition form_rules_in_force |
| causal_language_model::CC_WRITE_MODEL_RESPONSE_V0 | form_rules_in_force | INPUT | seed | inputs.seed | S7 cc_composition form_rules_in_force |
| causal_language_model::CC_WRITE_MODEL_RESPONSE_V0 | form_rules_in_force | OUTPUT | rules_in_force | capability_result.rules_in_force | S7 cc_composition form_rules_in_force |
| causal_language_model::CC_WRITE_MODEL_RESPONSE_V0 | form_rules_in_force | OUTPUT | positions | capability_result.positions | S7 cc_composition form_rules_in_force |
| causal_language_model::CC_WRITE_MODEL_RESPONSE_V0 | write_response | INPUT | reading | inputs.reading | S7 cc_composition write_response |
| causal_language_model::CC_WRITE_MODEL_RESPONSE_V0 | write_response | INPUT | rules_in_force | results.form_rules_in_force.rules_in_force | S7 cc_composition write_response |
| causal_language_model::CC_WRITE_MODEL_RESPONSE_V0 | write_response | INPUT | positions | results.form_rules_in_force.positions | S7 cc_composition write_response |
| causal_language_model::CC_WRITE_MODEL_RESPONSE_V0 | write_response | OUTPUT | written_response | capability_result.result | S7 cc_composition write_response |
| causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0 | confirm_releasable | INPUT | parameters | inputs.release_facts | S7 cc_composition confirm_releasable |
| causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0 | confirm_releasable | INPUT | rules | inputs.release_rules | S7 cc_composition confirm_releasable |
| causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0 | confirm_releasable | OUTPUT | releasable | capability_result.valid | S7 cc_composition confirm_releasable |
| causal_language_model::CC_RECORD_USER_PROMPT_V0 | assemble_user_prompt_record | INPUT | fields | {'user_prompt_id': '$.inputs.user_prompt_id', 'requester_id': '$.inputs.requester_id', 'customer_id': '$.inputs.customer_id', 'identity_key': '$.inputs.identity_key', 'kind': '$.inputs.kind', 'question': '$.inputs.question', 'supporting_material': '$.inputs.supporting_material', 'outcome': '$.inputs.outcome', 'time_in_service_id': '$.inputs.time_in_service_id', 'reading': '$.inputs.reading', 'rules_in_force': '$.inputs.rules_in_force', 'response': '$.inputs.response', 'reason': '$.inputs.reason'} | S7 cc_composition assemble_user_prompt_record |
| causal_language_model::CC_RECORD_USER_PROMPT_V0 | assemble_user_prompt_record | OUTPUT | user_prompt_record | capability_result.record | S7 cc_composition assemble_user_prompt_record |
| causal_language_model::CC_RECORD_USER_PROMPT_V0 | append_user_prompt_record | INPUT | record | results.assemble_user_prompt_record.user_prompt_record | S7 cc_composition append_user_prompt_record |
| causal_language_model::CC_RECORD_USER_PROMPT_V0 | append_user_prompt_record | INPUT | stream_id | inputs.user_prompt_id | S7 cc_composition append_user_prompt_record |
| causal_language_model::CC_RECORD_USER_PROMPT_V0 | append_user_prompt_record | INPUT | actor_id | inputs.requester_id | S7 cc_composition append_user_prompt_record |
| causal_language_model::CC_RECORD_USER_PROMPT_V0 | append_user_prompt_record | OUTPUT | record_id | capability_result.record_id | S7 cc_composition append_user_prompt_record |
| causal_language_model::CC_RECORD_USER_PROMPT_V0 | append_user_prompt_record | OUTPUT | sequence_number | capability_result.sequence_number | S7 cc_composition append_user_prompt_record |
| causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0 | read_user_prompt_entries | INPUT | stream_id | inputs.user_prompt_id | S7 cc_composition read_user_prompt_entries |
| causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0 | read_user_prompt_entries | OUTPUT | entries | capability_result.entries | S7 cc_composition read_user_prompt_entries |
| causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0 | read_user_prompt_entries | OUTPUT | result_status | result_status | S7 cc_composition read_user_prompt_entries |
| causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0 | select_user_prompt_record | INPUT | source | results.read_user_prompt_entries.entries | S7 cc_composition select_user_prompt_record |
| causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0 | select_user_prompt_record | INPUT | filter | {'stream_id': '$.inputs.user_prompt_id'} | S7 cc_composition select_user_prompt_record |
| causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0 | select_user_prompt_record | OUTPUT | user_prompt_record | capability_result.extracted | S7 cc_composition select_user_prompt_record |
| causal_language_model::CC_APPEND_MODEL_OPERATION_V0 | append_operation | INPUT | record | inputs.record | S7 cc_composition append_operation |
| causal_language_model::CC_APPEND_MODEL_OPERATION_V0 | append_operation | INPUT | stream_id | MODEL_OPERATIONS | S7 cc_composition append_operation |
| causal_language_model::CC_APPEND_MODEL_OPERATION_V0 | append_operation | INPUT | actor_id | inputs.staff_id | S7 cc_composition append_operation |
| causal_language_model::CC_APPEND_MODEL_OPERATION_V0 | append_operation | OUTPUT | record_id | capability_result.record_id | S7 cc_composition append_operation |
| causal_language_model::CC_APPEND_MODEL_OPERATION_V0 | append_operation | OUTPUT | sequence_number | capability_result.sequence_number | S7 cc_composition append_operation |
| causal_language_model::WF_REGISTER_MODEL_V0 | causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 | INPUT | staff_credentials | payload.staff_credentials | S7 execution_topology CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 |
| causal_language_model::WF_REGISTER_MODEL_V0 | causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 | INPUT | authorization_rules | payload.authorization_rules | S7 execution_topology CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 |
| causal_language_model::WF_REGISTER_MODEL_V0 | causal_language_model::CC_APPEND_MODEL_OPERATION_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology CC_APPEND_MODEL_OPERATION_V0 |
| causal_language_model::WF_REGISTER_MODEL_V0 | causal_language_model::CC_APPEND_MODEL_OPERATION_V0 | INPUT | operation | REGISTER_MODEL | S7 execution_topology CC_APPEND_MODEL_OPERATION_V0 |
| causal_language_model::WF_REGISTER_MODEL_V0 | causal_language_model::CC_APPEND_MODEL_OPERATION_V0 | INPUT | record | {'operation': 'REGISTER_MODEL', 'staff_id': '$.payload.staff_id', 'subject': '$.results.CC_CLAIM_MODEL_IDENTITY_V0.identity_key'} | S7 execution_topology CC_APPEND_MODEL_OPERATION_V0 |
| causal_language_model::WF_REGISTER_MODEL_V0 | causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0 | INPUT | description | payload.description | S7 execution_topology CC_CLAIM_MODEL_IDENTITY_V0 |
| causal_language_model::WF_REGISTER_MODEL_V0 | causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0 | INPUT | fingerprint | payload.fingerprint | S7 execution_topology CC_CLAIM_MODEL_IDENTITY_V0 |
| causal_language_model::WF_REGISTER_MODEL_V0 | causal_language_model::CC_REGISTER_MODEL_V0 | INPUT | identity_key | results.CC_CLAIM_MODEL_IDENTITY_V0.identity_key | S7 execution_topology CC_REGISTER_MODEL_V0 |
| causal_language_model::WF_REGISTER_MODEL_V0 | causal_language_model::CC_REGISTER_MODEL_V0 | INPUT | description | payload.description | S7 execution_topology CC_REGISTER_MODEL_V0 |
| causal_language_model::WF_REGISTER_MODEL_V0 | causal_language_model::CC_REGISTER_MODEL_V0 | INPUT | description_schema | payload.description_schema | S7 execution_topology CC_REGISTER_MODEL_V0 |
| causal_language_model::WF_REGISTER_MODEL_V0 | causal_language_model::CC_REGISTER_MODEL_V0 | INPUT | fingerprint | payload.fingerprint | S7 execution_topology CC_REGISTER_MODEL_V0 |
| causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0 | causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 | INPUT | staff_credentials | payload.staff_credentials | S7 execution_topology CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 |
| causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0 | causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 | INPUT | authorization_rules | payload.authorization_rules | S7 execution_topology CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 |
| causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0 | causal_language_model::CC_APPEND_MODEL_OPERATION_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology CC_APPEND_MODEL_OPERATION_V0 |
| causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0 | causal_language_model::CC_APPEND_MODEL_OPERATION_V0 | INPUT | operation | PLACE_MODEL_IN_SERVICE | S7 execution_topology CC_APPEND_MODEL_OPERATION_V0 |
| causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0 | causal_language_model::CC_APPEND_MODEL_OPERATION_V0 | INPUT | record | {'operation': 'PLACE_MODEL_IN_SERVICE', 'staff_id': '$.payload.staff_id', 'subject': '$.payload.identity_key'} | S7 execution_topology CC_APPEND_MODEL_OPERATION_V0 |
| causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0 | causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | INPUT | identity_key | payload.identity_key | S7 execution_topology CC_PLACE_MODEL_IN_SERVICE_V0 |
| causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0 | causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | INPUT | time_in_service_id | payload.time_in_service_id | S7 execution_topology CC_PLACE_MODEL_IN_SERVICE_V0 |
| causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0 | causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | INPUT | ceiling | payload.ceiling | S7 execution_topology CC_PLACE_MODEL_IN_SERVICE_V0 |
| causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0 | causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | INPUT | system_prompt | payload.system_prompt | S7 execution_topology CC_PLACE_MODEL_IN_SERVICE_V0 |
| causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0 | causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | INPUT | response_rules | payload.response_rules | S7 execution_topology CC_PLACE_MODEL_IN_SERVICE_V0 |
| causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0 | causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 | INPUT | staff_credentials | payload.staff_credentials | S7 execution_topology CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 |
| causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0 | causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 | INPUT | authorization_rules | payload.authorization_rules | S7 execution_topology CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 |
| causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0 | causal_language_model::CC_APPEND_MODEL_OPERATION_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology CC_APPEND_MODEL_OPERATION_V0 |
| causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0 | causal_language_model::CC_APPEND_MODEL_OPERATION_V0 | INPUT | operation | WITHDRAW_MODEL_FROM_SERVICE | S7 execution_topology CC_APPEND_MODEL_OPERATION_V0 |
| causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0 | causal_language_model::CC_APPEND_MODEL_OPERATION_V0 | INPUT | record | {'operation': 'WITHDRAW_MODEL_FROM_SERVICE', 'staff_id': '$.payload.staff_id', 'subject': '$.payload.identity_key'} | S7 execution_topology CC_APPEND_MODEL_OPERATION_V0 |
| causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0 | causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0 | INPUT | identity_key | payload.identity_key | S7 execution_topology CC_WITHDRAW_MODEL_FROM_SERVICE_V0 |
| causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0 | causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 | INPUT | staff_credentials | payload.staff_credentials | S7 execution_topology CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 |
| causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0 | causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 | INPUT | authorization_rules | payload.authorization_rules | S7 execution_topology CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 |
| causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0 | causal_language_model::CC_APPEND_MODEL_OPERATION_V0 | INPUT | staff_id | payload.staff_id | S7 execution_topology CC_APPEND_MODEL_OPERATION_V0 |
| causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0 | causal_language_model::CC_APPEND_MODEL_OPERATION_V0 | INPUT | operation | RETRIEVE_USER_PROMPT_RECORD | S7 execution_topology CC_APPEND_MODEL_OPERATION_V0 |
| causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0 | causal_language_model::CC_APPEND_MODEL_OPERATION_V0 | INPUT | record | {'operation': 'RETRIEVE_USER_PROMPT_RECORD', 'staff_id': '$.payload.staff_id', 'subject': '$.payload.user_prompt_id'} | S7 execution_topology CC_APPEND_MODEL_OPERATION_V0 |
| causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0 | causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0 | INPUT | user_prompt_id | payload.user_prompt_id | S7 execution_topology CC_RETRIEVE_USER_PROMPT_RECORD_V0 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0 | INPUT | customer_id | payload.customer_id | S7 execution_topology CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0 | INPUT | permitted_customers | payload.permitted_customers | S7 execution_topology CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | causal_language_model::CC_ADMIT_USER_PROMPT_V0 | INPUT | identity_key | payload.identity_key | S7 execution_topology CC_ADMIT_USER_PROMPT_V0 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 | INPUT | time_in_service_id | results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id | S7 execution_topology CC_CONFIRM_WITHIN_CEILING_V0 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 | INPUT | kind | payload.kind | S7 execution_topology CC_CONFIRM_WITHIN_CEILING_V0 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | causal_language_model::CC_CONFIRM_READING_FITS_V0 | INPUT | system_prompt | results.CC_CONFIRM_WITHIN_CEILING_V0.time_in_service.system_prompt | S7 execution_topology CC_CONFIRM_READING_FITS_V0 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | causal_language_model::CC_CONFIRM_READING_FITS_V0 | INPUT | question | payload.question | S7 execution_topology CC_CONFIRM_READING_FITS_V0 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | causal_language_model::CC_CONFIRM_READING_FITS_V0 | INPUT | supporting_material | payload.supporting_material | S7 execution_topology CC_CONFIRM_READING_FITS_V0 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | causal_language_model::CC_CONFIRM_READING_FITS_V0 | INPUT | reading_capacity | results.CC_ADMIT_USER_PROMPT_V0.model_record.description.reading_capacity | S7 execution_topology CC_CONFIRM_READING_FITS_V0 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | causal_language_model::CC_WRITE_MODEL_RESPONSE_V0 | INPUT | response_rules | results.CC_CONFIRM_WITHIN_CEILING_V0.time_in_service.response_rules | S7 execution_topology CC_WRITE_MODEL_RESPONSE_V0 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | causal_language_model::CC_WRITE_MODEL_RESPONSE_V0 | INPUT | account_numbers | payload.account_numbers | S7 execution_topology CC_WRITE_MODEL_RESPONSE_V0 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | causal_language_model::CC_WRITE_MODEL_RESPONSE_V0 | INPUT | seed | payload.seed | S7 execution_topology CC_WRITE_MODEL_RESPONSE_V0 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | causal_language_model::CC_WRITE_MODEL_RESPONSE_V0 | INPUT | reading | results.CC_CONFIRM_READING_FITS_V0.reading | S7 execution_topology CC_WRITE_MODEL_RESPONSE_V0 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | CONFIRM_NO_RULE_STOPPED | INPUT | release_facts | {'stopped_by': '$.results.CC_WRITE_MODEL_RESPONSE_V0.written_response.stopped_by'} | S7 execution_topology CONFIRM_NO_RULE_STOPPED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | CONFIRM_NO_RULE_STOPPED | INPUT | release_rules | [{'field': 'stopped_by', 'op': 'eq', 'value': ''}] | S7 execution_topology CONFIRM_NO_RULE_STOPPED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | CONFIRM_FINISHED | INPUT | release_facts | {'finished': '$.results.CC_WRITE_MODEL_RESPONSE_V0.written_response.finished'} | S7 execution_topology CONFIRM_FINISHED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | CONFIRM_FINISHED | INPUT | release_rules | [{'field': 'finished', 'op': 'eq', 'value': True}] | S7 execution_topology CONFIRM_FINISHED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_RESPONDED | INPUT | user_prompt_id | payload.user_prompt_id | S7 execution_topology RECORD_RESPONDED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_RESPONDED | INPUT | requester_id | payload.requester_id | S7 execution_topology RECORD_RESPONDED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_RESPONDED | INPUT | customer_id | payload.customer_id | S7 execution_topology RECORD_RESPONDED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_RESPONDED | INPUT | identity_key | payload.identity_key | S7 execution_topology RECORD_RESPONDED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_RESPONDED | INPUT | kind | payload.kind | S7 execution_topology RECORD_RESPONDED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_RESPONDED | INPUT | question | payload.question | S7 execution_topology RECORD_RESPONDED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_RESPONDED | INPUT | supporting_material | payload.supporting_material | S7 execution_topology RECORD_RESPONDED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_RESPONDED | INPUT | time_in_service_id | results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id | S7 execution_topology RECORD_RESPONDED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_RESPONDED | INPUT | reading | results.CC_CONFIRM_READING_FITS_V0.reading | S7 execution_topology RECORD_RESPONDED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_RESPONDED | INPUT | rules_in_force | results.CC_WRITE_MODEL_RESPONSE_V0.rules_in_force | S7 execution_topology RECORD_RESPONDED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_RESPONDED | INPUT | response | results.CC_WRITE_MODEL_RESPONSE_V0.written_response.text | S7 execution_topology RECORD_RESPONDED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_RESPONDED | INPUT | outcome | RESPONDED | S7 execution_topology RECORD_RESPONDED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_NOT_PERMITTED | INPUT | user_prompt_id | payload.user_prompt_id | S7 execution_topology RECORD_REFUSED_NOT_PERMITTED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_NOT_PERMITTED | INPUT | requester_id | payload.requester_id | S7 execution_topology RECORD_REFUSED_NOT_PERMITTED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_NOT_PERMITTED | INPUT | customer_id | payload.customer_id | S7 execution_topology RECORD_REFUSED_NOT_PERMITTED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_NOT_PERMITTED | INPUT | identity_key | payload.identity_key | S7 execution_topology RECORD_REFUSED_NOT_PERMITTED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_NOT_PERMITTED | INPUT | kind | payload.kind | S7 execution_topology RECORD_REFUSED_NOT_PERMITTED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_NOT_PERMITTED | INPUT | question | payload.question | S7 execution_topology RECORD_REFUSED_NOT_PERMITTED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_NOT_PERMITTED | INPUT | supporting_material | payload.supporting_material | S7 execution_topology RECORD_REFUSED_NOT_PERMITTED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_NOT_PERMITTED | INPUT | outcome | REFUSED | S7 execution_topology RECORD_REFUSED_NOT_PERMITTED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_NOT_PERMITTED | INPUT | reason | requester_not_permitted_for_customer | S7 execution_topology RECORD_REFUSED_NOT_PERMITTED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_NOT_REGISTERED | INPUT | user_prompt_id | payload.user_prompt_id | S7 execution_topology RECORD_REFUSED_NOT_REGISTERED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_NOT_REGISTERED | INPUT | requester_id | payload.requester_id | S7 execution_topology RECORD_REFUSED_NOT_REGISTERED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_NOT_REGISTERED | INPUT | customer_id | payload.customer_id | S7 execution_topology RECORD_REFUSED_NOT_REGISTERED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_NOT_REGISTERED | INPUT | identity_key | payload.identity_key | S7 execution_topology RECORD_REFUSED_NOT_REGISTERED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_NOT_REGISTERED | INPUT | kind | payload.kind | S7 execution_topology RECORD_REFUSED_NOT_REGISTERED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_NOT_REGISTERED | INPUT | question | payload.question | S7 execution_topology RECORD_REFUSED_NOT_REGISTERED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_NOT_REGISTERED | INPUT | supporting_material | payload.supporting_material | S7 execution_topology RECORD_REFUSED_NOT_REGISTERED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_NOT_REGISTERED | INPUT | outcome | REFUSED | S7 execution_topology RECORD_REFUSED_NOT_REGISTERED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_NOT_REGISTERED | INPUT | reason | model_not_registered | S7 execution_topology RECORD_REFUSED_NOT_REGISTERED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_NOT_IN_SERVICE | INPUT | user_prompt_id | payload.user_prompt_id | S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_NOT_IN_SERVICE | INPUT | requester_id | payload.requester_id | S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_NOT_IN_SERVICE | INPUT | customer_id | payload.customer_id | S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_NOT_IN_SERVICE | INPUT | identity_key | payload.identity_key | S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_NOT_IN_SERVICE | INPUT | kind | payload.kind | S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_NOT_IN_SERVICE | INPUT | question | payload.question | S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_NOT_IN_SERVICE | INPUT | supporting_material | payload.supporting_material | S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_NOT_IN_SERVICE | INPUT | outcome | REFUSED | S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_NOT_IN_SERVICE | INPUT | reason | model_not_in_service | S7 execution_topology RECORD_REFUSED_NOT_IN_SERVICE |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_ABOVE_CEILING | INPUT | user_prompt_id | payload.user_prompt_id | S7 execution_topology RECORD_REFUSED_ABOVE_CEILING |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_ABOVE_CEILING | INPUT | requester_id | payload.requester_id | S7 execution_topology RECORD_REFUSED_ABOVE_CEILING |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_ABOVE_CEILING | INPUT | customer_id | payload.customer_id | S7 execution_topology RECORD_REFUSED_ABOVE_CEILING |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_ABOVE_CEILING | INPUT | identity_key | payload.identity_key | S7 execution_topology RECORD_REFUSED_ABOVE_CEILING |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_ABOVE_CEILING | INPUT | kind | payload.kind | S7 execution_topology RECORD_REFUSED_ABOVE_CEILING |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_ABOVE_CEILING | INPUT | question | payload.question | S7 execution_topology RECORD_REFUSED_ABOVE_CEILING |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_ABOVE_CEILING | INPUT | supporting_material | payload.supporting_material | S7 execution_topology RECORD_REFUSED_ABOVE_CEILING |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_ABOVE_CEILING | INPUT | time_in_service_id | results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id | S7 execution_topology RECORD_REFUSED_ABOVE_CEILING |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_ABOVE_CEILING | INPUT | outcome | REFUSED | S7 execution_topology RECORD_REFUSED_ABOVE_CEILING |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_ABOVE_CEILING | INPUT | reason | kind_above_sensitivity_ceiling | S7 execution_topology RECORD_REFUSED_ABOVE_CEILING |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | INPUT | user_prompt_id | payload.user_prompt_id | S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | INPUT | requester_id | payload.requester_id | S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | INPUT | customer_id | payload.customer_id | S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | INPUT | identity_key | payload.identity_key | S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | INPUT | kind | payload.kind | S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | INPUT | question | payload.question | S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | INPUT | supporting_material | payload.supporting_material | S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | INPUT | time_in_service_id | results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id | S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | INPUT | outcome | REFUSED | S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | INPUT | reason | reading_longer_than_model_can_read | S7 execution_topology RECORD_REFUSED_TOO_LONG_TO_READ |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_BY_RULE | INPUT | user_prompt_id | payload.user_prompt_id | S7 execution_topology RECORD_REFUSED_BY_RULE |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_BY_RULE | INPUT | requester_id | payload.requester_id | S7 execution_topology RECORD_REFUSED_BY_RULE |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_BY_RULE | INPUT | customer_id | payload.customer_id | S7 execution_topology RECORD_REFUSED_BY_RULE |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_BY_RULE | INPUT | identity_key | payload.identity_key | S7 execution_topology RECORD_REFUSED_BY_RULE |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_BY_RULE | INPUT | kind | payload.kind | S7 execution_topology RECORD_REFUSED_BY_RULE |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_BY_RULE | INPUT | question | payload.question | S7 execution_topology RECORD_REFUSED_BY_RULE |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_BY_RULE | INPUT | supporting_material | payload.supporting_material | S7 execution_topology RECORD_REFUSED_BY_RULE |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_BY_RULE | INPUT | time_in_service_id | results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id | S7 execution_topology RECORD_REFUSED_BY_RULE |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_BY_RULE | INPUT | reading | results.CC_CONFIRM_READING_FITS_V0.reading | S7 execution_topology RECORD_REFUSED_BY_RULE |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_BY_RULE | INPUT | rules_in_force | results.CC_WRITE_MODEL_RESPONSE_V0.rules_in_force | S7 execution_topology RECORD_REFUSED_BY_RULE |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_BY_RULE | INPUT | outcome | REFUSED | S7 execution_topology RECORD_REFUSED_BY_RULE |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_BY_RULE | INPUT | reason | results.CC_WRITE_MODEL_RESPONSE_V0.written_response.stopped_by | S7 execution_topology RECORD_REFUSED_BY_RULE |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_UNFINISHED | INPUT | user_prompt_id | payload.user_prompt_id | S7 execution_topology RECORD_REFUSED_UNFINISHED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_UNFINISHED | INPUT | requester_id | payload.requester_id | S7 execution_topology RECORD_REFUSED_UNFINISHED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_UNFINISHED | INPUT | customer_id | payload.customer_id | S7 execution_topology RECORD_REFUSED_UNFINISHED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_UNFINISHED | INPUT | identity_key | payload.identity_key | S7 execution_topology RECORD_REFUSED_UNFINISHED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_UNFINISHED | INPUT | kind | payload.kind | S7 execution_topology RECORD_REFUSED_UNFINISHED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_UNFINISHED | INPUT | question | payload.question | S7 execution_topology RECORD_REFUSED_UNFINISHED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_UNFINISHED | INPUT | supporting_material | payload.supporting_material | S7 execution_topology RECORD_REFUSED_UNFINISHED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_UNFINISHED | INPUT | time_in_service_id | results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id | S7 execution_topology RECORD_REFUSED_UNFINISHED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_UNFINISHED | INPUT | reading | results.CC_CONFIRM_READING_FITS_V0.reading | S7 execution_topology RECORD_REFUSED_UNFINISHED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_UNFINISHED | INPUT | rules_in_force | results.CC_WRITE_MODEL_RESPONSE_V0.rules_in_force | S7 execution_topology RECORD_REFUSED_UNFINISHED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_UNFINISHED | INPUT | outcome | REFUSED | S7 execution_topology RECORD_REFUSED_UNFINISHED |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_UNFINISHED | INPUT | reason | longest_response_reached | S7 execution_topology RECORD_REFUSED_UNFINISHED |

---

## 8. Interface Fields

<!-- register:interface_fields optional -->
| Artifact | Direction (INPUT, OUTPUT, ATTRIBUTE) | Field | Type | Required (YES, NO) | Default | Meaning |
|----------|--------------------------------------|-------|------|--------------------|---------|---------|
| causal_language_model::IN_REGISTER_MODEL_V0 | INPUT | staff_credentials | object | YES |  | Who is performing the operation, as the subdomain receives it |
| causal_language_model::IN_REGISTER_MODEL_V0 | INPUT | authorization_rules | array | YES |  | The rules the staff member's credentials are checked against |
| causal_language_model::IN_REGISTER_MODEL_V0 | INPUT | staff_id | string | YES |  | The staff member recorded against the operation in the operation trail |
| causal_language_model::IN_REGISTER_MODEL_V0 | INPUT | description | object | YES |  | How the model is built, including the amount of text it can read at once |
| causal_language_model::IN_REGISTER_MODEL_V0 | INPUT | description_schema | object | YES |  | The fields a model description must carry |
| causal_language_model::IN_REGISTER_MODEL_V0 | INPUT | fingerprint | string | YES |  | The training fingerprint, the provider's claim |
| causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0 | INPUT | staff_credentials | object | YES |  | Who is performing the operation, as the subdomain receives it |
| causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0 | INPUT | authorization_rules | array | YES |  | The rules the staff member's credentials are checked against |
| causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0 | INPUT | staff_id | string | YES |  | The staff member recorded against the operation in the operation trail |
| causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0 | INPUT | identity_key | string | YES |  | The key formed from a model's description and fingerprint |
| causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0 | INPUT | time_in_service_id | string | YES |  | The time in service, assigned at placement |
| causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0 | INPUT | ceiling | string | YES |  | The most sensitive kind of information the model may read |
| causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0 | INPUT | system_prompt | string | YES |  | The business's standing instructions to the model for its time in service |
| causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0 | INPUT | response_rules | object | YES |  | The forbidden words and patterns, the account-number shape, the freedom of word choice and the longest response |
| causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0 | INPUT | staff_credentials | object | YES |  | Who is performing the operation, as the subdomain receives it |
| causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0 | INPUT | authorization_rules | array | YES |  | The rules the staff member's credentials are checked against |
| causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0 | INPUT | staff_id | string | YES |  | The staff member recorded against the operation in the operation trail |
| causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0 | INPUT | identity_key | string | YES |  | The key formed from a model's description and fingerprint |
| causal_language_model::IN_SUBMIT_USER_PROMPT_V0 | INPUT | user_prompt_id | string | YES |  | The user prompt, as the requester names it |
| causal_language_model::IN_SUBMIT_USER_PROMPT_V0 | INPUT | requester_id | string | YES |  | The requester who submits the user prompt |
| causal_language_model::IN_SUBMIT_USER_PROMPT_V0 | INPUT | permitted_customers | array | YES |  | The customers the requester may act for, as the business's existing arrangements state |
| causal_language_model::IN_SUBMIT_USER_PROMPT_V0 | INPUT | customer_id | string | YES |  | The customer the user prompt is for |
| causal_language_model::IN_SUBMIT_USER_PROMPT_V0 | INPUT | account_numbers | array | YES |  | The customer's own account numbers, from the business's existing records |
| causal_language_model::IN_SUBMIT_USER_PROMPT_V0 | INPUT | identity_key | string | YES |  | The key formed from a model's description and fingerprint |
| causal_language_model::IN_SUBMIT_USER_PROMPT_V0 | INPUT | kind | string | YES |  | The most sensitive kind of information the question and its material contain |
| causal_language_model::IN_SUBMIT_USER_PROMPT_V0 | INPUT | question | string | YES |  | What the requester asks on the customer's behalf |
| causal_language_model::IN_SUBMIT_USER_PROMPT_V0 | INPUT | supporting_material | string | YES |  | Material carried with the question for the model to read |
| causal_language_model::IN_SUBMIT_USER_PROMPT_V0 | INPUT | seed | integer | YES |  | The seed each adventurous word choice is drawn from |
| causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0 | INPUT | staff_credentials | object | YES |  | Who is performing the operation, as the subdomain receives it |
| causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0 | INPUT | authorization_rules | array | YES |  | The rules the staff member's credentials are checked against |
| causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0 | INPUT | staff_id | string | YES |  | The staff member recorded against the operation in the operation trail |
| causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0 | INPUT | user_prompt_id | string | YES |  | The user prompt, as the requester names it |
| causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 | INPUT | staff_credentials | object | YES |  | Who is performing the operation, as the subdomain receives it |
| causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 | INPUT | authorization_rules | array | YES |  | The rules the staff member's credentials are checked against |
| causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 | OUTPUT | is_authorized | boolean | YES |  | Whether the staff member is model staff |
| causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0 | INPUT | customer_id | string | YES |  | The customer the user prompt is for |
| causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0 | INPUT | permitted_customers | array | YES |  | The customers the requester may act for, as the business's existing arrangements state |
| causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0 | OUTPUT | acts_for_customer | boolean | YES |  | Whether the requester may act for the customer |
| causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0 | INPUT | description | object | YES |  | How the model is built, including the amount of text it can read at once |
| causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0 | INPUT | fingerprint | string | YES |  | The training fingerprint, the provider's claim |
| causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0 | OUTPUT | identity_key | string | YES |  | The key formed from a model's description and fingerprint |
| causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0 | OUTPUT | address | string | YES |  | Where the claimed key resolves to |
| causal_language_model::CC_REGISTER_MODEL_V0 | INPUT | identity_key | string | YES |  | The key formed from a model's description and fingerprint |
| causal_language_model::CC_REGISTER_MODEL_V0 | INPUT | description | object | YES |  | How the model is built, including the amount of text it can read at once |
| causal_language_model::CC_REGISTER_MODEL_V0 | INPUT | description_schema | object | YES |  | The fields a model description must carry |
| causal_language_model::CC_REGISTER_MODEL_V0 | INPUT | fingerprint | string | YES |  | The training fingerprint, the provider's claim |
| causal_language_model::CC_REGISTER_MODEL_V0 | OUTPUT | model_record | object | YES |  | The model's record, registered |
| causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | INPUT | identity_key | string | YES |  | The key formed from a model's description and fingerprint |
| causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | INPUT | time_in_service_id | string | YES |  | The time in service, assigned at placement |
| causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | INPUT | ceiling | string | YES |  | The most sensitive kind of information the model may read |
| causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | INPUT | system_prompt | string | YES |  | The business's standing instructions to the model for its time in service |
| causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | INPUT | response_rules | object | YES |  | The forbidden words and patterns, the account-number shape, the freedom of word choice and the longest response |
| causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | OUTPUT | time_in_service | object | YES |  | The time in service opened |
| causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0 | INPUT | identity_key | string | YES |  | The key formed from a model's description and fingerprint |
| causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0 | OUTPUT | model_record | object | YES |  | The model's record as it stood before withdrawal |
| causal_language_model::CC_ADMIT_USER_PROMPT_V0 | INPUT | identity_key | string | YES |  | The key formed from a model's description and fingerprint |
| causal_language_model::CC_ADMIT_USER_PROMPT_V0 | OUTPUT | model_record | object | YES |  | The record of the model the user prompt names, in service |
| causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 | INPUT | time_in_service_id | string | YES |  | The time in service, assigned at placement |
| causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 | INPUT | kind | string | YES |  | The most sensitive kind of information the question and its material contain |
| causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 | OUTPUT | time_in_service | object | YES |  | The model's open time in service, with its ceiling, system prompt and response rules |
| causal_language_model::CC_CONFIRM_READING_FITS_V0 | INPUT | system_prompt | string | YES |  | The business's standing instructions to the model for its time in service |
| causal_language_model::CC_CONFIRM_READING_FITS_V0 | INPUT | question | string | YES |  | What the requester asks on the customer's behalf |
| causal_language_model::CC_CONFIRM_READING_FITS_V0 | INPUT | supporting_material | string | YES |  | Material carried with the question for the model to read |
| causal_language_model::CC_CONFIRM_READING_FITS_V0 | INPUT | reading_capacity | integer | YES |  | How many words the model can read at once |
| causal_language_model::CC_CONFIRM_READING_FITS_V0 | OUTPUT | reading | object | YES |  | Exactly what the model reads |
| causal_language_model::CC_CONFIRM_READING_FITS_V0 | OUTPUT | reading_length | integer | YES |  | How long what the model reads is, in words |
| causal_language_model::CC_WRITE_MODEL_RESPONSE_V0 | INPUT | response_rules | object | YES |  | The forbidden words and patterns, the account-number shape, the freedom of word choice and the longest response |
| causal_language_model::CC_WRITE_MODEL_RESPONSE_V0 | INPUT | account_numbers | array | YES |  | The customer's own account numbers, from the business's existing records |
| causal_language_model::CC_WRITE_MODEL_RESPONSE_V0 | INPUT | seed | integer | YES |  | The seed each adventurous word choice is drawn from |
| causal_language_model::CC_WRITE_MODEL_RESPONSE_V0 | INPUT | reading | object | YES |  | Exactly what the model read, when it read anything |
| causal_language_model::CC_WRITE_MODEL_RESPONSE_V0 | OUTPUT | rules_in_force | object | YES |  | The response rules in force for this user prompt, with its seed |
| causal_language_model::CC_WRITE_MODEL_RESPONSE_V0 | OUTPUT | written_response | object | YES |  | The response as written, whether it finished, the rule that stopped it and the words stopped |
| causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0 | INPUT | release_facts | object | YES |  | The facts of the written response one release condition reads |
| causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0 | INPUT | release_rules | array | YES |  | The release condition, as a rule over those facts |
| causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0 | OUTPUT | releasable | boolean | YES |  | Whether the condition for release holds |
| causal_language_model::CC_RECORD_USER_PROMPT_V0 | INPUT | user_prompt_id | string | YES |  | The user prompt, as the requester names it |
| causal_language_model::CC_RECORD_USER_PROMPT_V0 | INPUT | requester_id | string | YES |  | The requester who submits the user prompt |
| causal_language_model::CC_RECORD_USER_PROMPT_V0 | INPUT | customer_id | string | YES |  | The customer the user prompt is for |
| causal_language_model::CC_RECORD_USER_PROMPT_V0 | INPUT | identity_key | string | YES |  | The key formed from a model's description and fingerprint |
| causal_language_model::CC_RECORD_USER_PROMPT_V0 | INPUT | kind | string | YES |  | The most sensitive kind of information the question and its material contain |
| causal_language_model::CC_RECORD_USER_PROMPT_V0 | INPUT | question | string | YES |  | What the requester asks on the customer's behalf |
| causal_language_model::CC_RECORD_USER_PROMPT_V0 | INPUT | supporting_material | string | YES |  | Material carried with the question for the model to read |
| causal_language_model::CC_RECORD_USER_PROMPT_V0 | INPUT | outcome | string | YES |  | RESPONDED or REFUSED |
| causal_language_model::CC_RECORD_USER_PROMPT_V0 | INPUT | time_in_service_id | string | NO |  | The time in service, assigned at placement |
| causal_language_model::CC_RECORD_USER_PROMPT_V0 | INPUT | reading | object | NO |  | Exactly what the model read, when it read anything |
| causal_language_model::CC_RECORD_USER_PROMPT_V0 | INPUT | rules_in_force | object | NO |  | The response rules in force, when the model wrote |
| causal_language_model::CC_RECORD_USER_PROMPT_V0 | INPUT | response | string | NO |  | The model response released |
| causal_language_model::CC_RECORD_USER_PROMPT_V0 | INPUT | reason | string | NO |  | Why the user prompt was refused |
| causal_language_model::CC_RECORD_USER_PROMPT_V0 | OUTPUT | record_id | string | YES |  | The identity of the appended user prompt record |
| causal_language_model::CC_RECORD_USER_PROMPT_V0 | OUTPUT | sequence_number | integer | YES |  | The record's position in the user prompt records |
| causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0 | INPUT | user_prompt_id | string | YES |  | The user prompt, as the requester names it |
| causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0 | OUTPUT | user_prompt_record | array | YES |  | The record of the user prompt |
| causal_language_model::CC_APPEND_MODEL_OPERATION_V0 | INPUT | record | object | YES |  | The account of the performed operation |
| causal_language_model::CC_APPEND_MODEL_OPERATION_V0 | INPUT | staff_id | string | YES |  | The staff member recorded against the operation in the operation trail |
| causal_language_model::CC_APPEND_MODEL_OPERATION_V0 | INPUT | operation | string | YES |  | The operation performed |
| causal_language_model::CC_APPEND_MODEL_OPERATION_V0 | OUTPUT | record_id | string | YES |  | The identity of the appended trail entry |
| causal_language_model::CC_APPEND_MODEL_OPERATION_V0 | OUTPUT | sequence_number | integer | YES |  | The entry's position in the trail |
| causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0 | INPUT | description | object | YES |  | How the model is built, including the amount of text it can read at once |
| causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0 | INPUT | fingerprint | string | YES |  | The training fingerprint, the provider's claim |
| causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0 | OUTPUT | identity_key | string | YES |  | The key formed from a model's description and fingerprint |
| causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0 | INPUT | kind | string | YES |  | The kind of information stated |
| causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0 | INPUT | ceiling | string | YES |  | The most sensitive kind of information the model may read |
| causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0 | INPUT | kinds | array | YES |  | The declared kinds, least sensitive first |
| causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0 | OUTPUT | within_ceiling | boolean | YES |  | Whether the kind is no more sensitive than the ceiling |
| causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0 | INPUT | system_prompt | string | YES |  | The business's standing instructions to the model for its time in service |
| causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0 | INPUT | question | string | YES |  | What the requester asks on the customer's behalf |
| causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0 | INPUT | supporting_material | string | YES |  | Material carried with the question for the model to read |
| causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0 | INPUT | reading_capacity | integer | YES |  | How many words the model can read at once |
| causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0 | OUTPUT | reading | object | YES |  | Exactly what the model reads |
| causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0 | OUTPUT | reading_length | integer | YES |  | How long it is, in words |
| causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0 | INPUT | response_rules | object | YES |  | The forbidden words and patterns, the account-number shape, the freedom of word choice and the longest response |
| causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0 | INPUT | account_numbers | array | YES |  | The customer's own account numbers, from the business's existing records |
| causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0 | INPUT | seed | integer | YES |  | The seed each adventurous word choice is drawn from |
| causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0 | OUTPUT | rules_in_force | object | YES |  | The forbidden rules, the freedom of word choice and the seed in force |
| causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0 | OUTPUT | positions | array | YES |  | One position per word up to the longest response |
| causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0 | INPUT | reading | object | YES |  | Exactly what the model reads |
| causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0 | INPUT | text | string | YES |  | The response so far |
| causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0 | OUTPUT | candidates | array | YES |  | The words the model offers next, each with its likelihood |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | INPUT | candidates | array | YES |  | The words offered, each with its likelihood |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | INPUT | rules_in_force | object | YES |  | The response rules in force |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | INPUT | position | integer | YES |  | Which word this is |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | INPUT | text | string | YES |  | The response so far |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | INPUT | finished | boolean | YES |  | Whether the response has finished |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | INPUT | stopped_by | string | YES |  | The rule that left no permitted word, or empty |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | INPUT | stopped | array | YES |  | The words stopped so far, each with its position and rule |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | OUTPUT | text | string | YES |  | The response so far, with the chosen word |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | OUTPUT | finished | boolean | YES |  | Whether the chosen word ends the response |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | OUTPUT | stopped_by | string | YES |  | The rule that left no permitted word, or empty |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | OUTPUT | stopped | array | YES |  | The words stopped so far, with those stopped this pass |
| causal_language_model::CT_WRITE_NEXT_WORD_V0 | INPUT | reading | object | YES |  | Exactly what the model reads |
| causal_language_model::CT_WRITE_NEXT_WORD_V0 | INPUT | rules_in_force | object | YES |  | The response rules in force |
| causal_language_model::CT_WRITE_NEXT_WORD_V0 | INPUT | position | integer | YES |  | Which word this is |
| causal_language_model::CT_WRITE_NEXT_WORD_V0 | INPUT | text | string | YES |  | The response so far |
| causal_language_model::CT_WRITE_NEXT_WORD_V0 | INPUT | finished | boolean | YES |  | Whether the response has finished |
| causal_language_model::CT_WRITE_NEXT_WORD_V0 | INPUT | stopped_by | string | YES |  | The rule that left no permitted word, or empty |
| causal_language_model::CT_WRITE_NEXT_WORD_V0 | INPUT | stopped | array | YES |  | The words stopped so far |
| causal_language_model::CT_WRITE_NEXT_WORD_V0 | OUTPUT | result | object | YES |  | The response so far, whether it finished, the rule that stopped it and the words stopped |
| causal_language_model::CT_WRITE_RESPONSE_V0 | INPUT | reading | object | YES |  | Exactly what the model reads |
| causal_language_model::CT_WRITE_RESPONSE_V0 | INPUT | rules_in_force | object | YES |  | The response rules in force |
| causal_language_model::CT_WRITE_RESPONSE_V0 | INPUT | positions | array | YES |  | One position per word up to the longest response |
| causal_language_model::CT_WRITE_RESPONSE_V0 | OUTPUT | result | object | YES |  | The response as written, whether it finished, the rule that stopped it and the words stopped |
| causal_language_model::EV_MODEL_REGISTERED_V0 | OUTPUT | identity_key | string | YES |  | The key formed from a model's description and fingerprint |
| causal_language_model::EV_MODEL_REGISTERED_V0 | OUTPUT | staff_id | string | YES |  | The staff member recorded against the operation in the operation trail |
| causal_language_model::EV_MODEL_SERVICE_STARTED_V0 | OUTPUT | identity_key | string | YES |  | The key formed from a model's description and fingerprint |
| causal_language_model::EV_MODEL_SERVICE_STARTED_V0 | OUTPUT | time_in_service_id | string | YES |  | The time in service, assigned at placement |
| causal_language_model::EV_MODEL_SERVICE_STARTED_V0 | OUTPUT | staff_id | string | YES |  | The staff member recorded against the operation in the operation trail |
| causal_language_model::EV_MODEL_SERVICE_ENDED_V0 | OUTPUT | identity_key | string | YES |  | The key formed from a model's description and fingerprint |
| causal_language_model::EV_MODEL_SERVICE_ENDED_V0 | OUTPUT | staff_id | string | YES |  | The staff member recorded against the operation in the operation trail |
| causal_language_model::EV_USER_PROMPT_RESPONDED_V0 | OUTPUT | user_prompt_id | string | YES |  | The user prompt, as the requester names it |
| causal_language_model::EV_USER_PROMPT_RESPONDED_V0 | OUTPUT | identity_key | string | YES |  | The key formed from a model's description and fingerprint |
| causal_language_model::EV_USER_PROMPT_RESPONDED_V0 | OUTPUT | requester_id | string | YES |  | The requester who submits the user prompt |
| causal_language_model::EV_USER_PROMPT_REFUSED_V0 | OUTPUT | user_prompt_id | string | YES |  | The user prompt, as the requester names it |
| causal_language_model::EV_USER_PROMPT_REFUSED_V0 | OUTPUT | identity_key | string | YES |  | The key formed from a model's description and fingerprint |
| causal_language_model::EV_USER_PROMPT_REFUSED_V0 | OUTPUT | requester_id | string | YES |  | The requester who submits the user prompt |
| causal_language_model::AC_MODEL_STAFF_V0 | ATTRIBUTE | staff_id | string | YES |  | The staff member's identity as the business knows it |
| causal_language_model::AC_MODEL_STAFF_V0 | ATTRIBUTE | authorized | boolean | NO | false | Whether the staff member is model staff; decided by the business's existing arrangements, read here |
| causal_language_model::AC_REQUESTER_V0 | ATTRIBUTE | requester_id | string | YES |  | The requester's identity as the business knows it |
| causal_language_model::AC_REQUESTER_V0 | ATTRIBUTE | permitted_customers | array | NO | [] | The customers the requester may act for; decided by the business's existing arrangements, read here |

---

## 9. Implementation Bindings

The offer's implementation is the test model: it offers another customer's account number first, then
the words of the supporting material, then the end of the response. A real model later joins it as a
second realization of the same declared step.

<!-- register:implementation_bindings optional -->
| CT Code | Module | Callable | Operation | Kind (atom, molecule) | Purity (ct_pure, ct_impure) | Refusal (raises, returns, never) | Source Finding |
|---------|--------|----------|-----------|-----------------------|-----------------------------|----------------------------------|----------------|
| causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0 | causal_language_model.implementation.capability_transforms.atoms.ct_pure_form_model_identity_key_v0 | execute | FORM_MODEL_IDENTITY_KEY | atom | ct_pure | never | S7 new_artifacts CT_PURE_FORM_MODEL_IDENTITY_KEY_V0 |
| causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0 | causal_language_model.implementation.capability_transforms.atoms.ct_pure_compare_sensitivity_v0 | execute | COMPARE_SENSITIVITY | atom | ct_pure | raises | S7 new_artifacts CT_PURE_COMPARE_SENSITIVITY_V0 |
| causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0 | causal_language_model.implementation.capability_transforms.atoms.ct_pure_assemble_model_reading_v0 | execute | ASSEMBLE_MODEL_READING | atom | ct_pure | raises | S7 new_artifacts CT_PURE_ASSEMBLE_MODEL_READING_V0 |
| causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0 | causal_language_model.implementation.capability_transforms.atoms.ct_pure_form_response_rules_v0 | execute | FORM_RESPONSE_RULES | atom | ct_pure | never | S7 new_artifacts CT_PURE_FORM_RESPONSE_RULES_V0 |
| causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0 | causal_language_model.implementation.capability_transforms.atoms.ct_impure_offer_next_words_v0 | execute | OFFER_NEXT_WORDS | atom | ct_impure | never | S7 new_artifacts CT_IMPURE_OFFER_NEXT_WORDS_V0 |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | causal_language_model.implementation.capability_transforms.atoms.ct_pure_choose_permitted_word_v0 | execute | CHOOSE_PERMITTED_WORD | atom | ct_pure | returns | S7 new_artifacts CT_PURE_CHOOSE_PERMITTED_WORD_V0 |
| causal_language_model::CT_WRITE_NEXT_WORD_V0 |  |  | WRITE_NEXT_WORD | molecule | ct_impure | returns | S7 new_artifacts CT_WRITE_NEXT_WORD_V0 |
| causal_language_model::CT_WRITE_RESPONSE_V0 |  |  | WRITE_RESPONSE | molecule | ct_impure | returns | S7 new_artifacts CT_WRITE_RESPONSE_V0 |

---

## 10. Vocabulary Extensions

Every status this design routes on — ACK, NACK, SUCCESS, NOT_FOUND, ALREADY_EXISTS, VIOLATION,
BACKEND_ERROR — is already admitted. The one vocabulary authored is the kinds of information, in their
declared order.

<!-- register:vocabulary_extensions optional -->
| Vocabulary Code | Extends | Group | Casing | Value | Meaning | Source Finding |
|-----------------|---------|-------|--------|-------|---------|----------------|
| causal_language_model::VOCAB_KIND_OF_INFORMATION_V0 | NONE | kind_of_information | lower_snake | public | The least sensitive kind | S5 provisional_codes VOCAB_KIND_OF_INFORMATION_V0 |
| causal_language_model::VOCAB_KIND_OF_INFORMATION_V0 | NONE | kind_of_information | lower_snake | internal | More sensitive than public | S5 provisional_codes VOCAB_KIND_OF_INFORMATION_V0 |
| causal_language_model::VOCAB_KIND_OF_INFORMATION_V0 | NONE | kind_of_information | lower_snake | confidential | More sensitive than internal | S5 provisional_codes VOCAB_KIND_OF_INFORMATION_V0 |
| causal_language_model::VOCAB_KIND_OF_INFORMATION_V0 | NONE | kind_of_information | lower_snake | restricted | The most sensitive kind | S5 provisional_codes VOCAB_KIND_OF_INFORMATION_V0 |

---

## 11. Runtime Policies

<!-- register:runtime_policies optional -->
| RB Code | Capability | Key | Value | Source Finding |
|---------|------------|-----|-------|----------------|
| causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0 | capability_side_effects::CS_MUTABLE_JSON_V0 | structure | causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0 | S7 rb_declarations RB_MODEL_RESPONSE_BINDINGS_V0 |
| causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0 | capability_side_effects::CS_REGISTRY_V0 | structure | causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0 | S7 rb_declarations RB_MODEL_RESPONSE_BINDINGS_V0 |
| causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0 | capability_side_effects::CS_APPENDONLY_JSONL_V0 | structure | causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0 | S7 rb_declarations RB_MODEL_RESPONSE_BINDINGS_V0 |

---

## 12. Artifact Properties

<!-- register:artifact_properties optional -->
| Artifact | Property | Value | Source Finding |
|----------|----------|-------|----------------|
| causal_language_model::AC_MODEL_STAFF_V0 | type | ENDUSER | S5 provisional_codes AC_MODEL_STAFF_V0 |
| causal_language_model::AC_REQUESTER_V0 | type | ENDUSER | S5 provisional_codes AC_REQUESTER_V0 |
| causal_language_model::WF_REGISTER_MODEL_V0 | emit.EXIT_REGISTERED | causal_language_model::EV_MODEL_REGISTERED_V0 | S4 gap_register GAP-20 |
| causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0 | emit.EXIT_PLACED | causal_language_model::EV_MODEL_SERVICE_STARTED_V0 | S4 gap_register GAP-20 |
| causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0 | emit.EXIT_WITHDRAWN | causal_language_model::EV_MODEL_SERVICE_ENDED_V0 | S4 gap_register GAP-20 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | emit.EXIT_RESPONDED | causal_language_model::EV_USER_PROMPT_RESPONDED_V0 | S4 gap_register GAP-20 |
| causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | emit.EXIT_REFUSED | causal_language_model::EV_USER_PROMPT_REFUSED_V0 | S4 gap_register GAP-20 |
| causal_language_model::EV_USER_PROMPT_REFUSED_V0 | moment | refusal | S0 business_events User Prompt Refused |

---

## 13. STRUCTURE Stores

<!-- register:structure_stores optional -->
| Store Name | Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0) | Proposed Path | Used By | Source Finding |
|------------|---------------------------------------------------------------------------|---------------|---------|----------------|
| MODELS | CS_MUTABLE_JSON_V0 | causal_language_model/model_response/models.json | causal_language_model::CC_REGISTER_MODEL_V0 | S6 storage_governance A durable record of every model the business holds |
| MODEL_IDENTITY_REGISTRY | CS_REGISTRY_V0 | causal_language_model/model_response/model_identity_registry.jsonl | causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0 | S6 storage_governance A claim on each model's identity, held once |
| TIMES_IN_SERVICE | CS_MUTABLE_JSON_V0 | causal_language_model/model_response/times_in_service.json | causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | S6 storage_governance A durable record of every time in service |
| USER_PROMPT_RECORDS | CS_APPENDONLY_JSONL_V0 | causal_language_model/model_response/user_prompt_records.jsonl | causal_language_model::CC_RECORD_USER_PROMPT_V0 | S6 storage_governance A record of every user prompt that cannot be amended |
| MODEL_OPERATIONS | CS_APPENDONLY_JSONL_V0 | causal_language_model/model_response/model_operations.jsonl | causal_language_model::CC_APPEND_MODEL_OPERATION_V0 | S6 storage_governance A trail of performed operations that cannot be amended |

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
| NEW | model_response | 42 | 2 AC, 5 IN, 5 WF, 14 CC, 8 CT, 5 EV, 1 VOCAB, 1 RB, 1 STRUCTURE |

---

## 16. Generation Provenance

*Every artifact this design schedules is authored: construction renders it from the registers
above and it is its own source of truth. Nothing here is reached by invoking a generator.*

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

A submission's refusal is discharged at the place that records it: that place's success ends the act
at `EXIT_REFUSED`, which refuses. The check that found the refusal routes there and nowhere else.

<!-- register:refusal_discharge optional -->
| Operation | Refused When | Act | Step | Outcome | Source Finding |
|-----------|--------------|-----|------|---------|----------------|
| Register a model | Its description and fingerprint match a registered model. | causal_language_model::WF_REGISTER_MODEL_V0 | causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0 | ALREADY_EXISTS | S0 operation_refusals #1 |
| Place a model in service | The model is not registered. | causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0 | causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | NOT_FOUND | S0 operation_refusals #2 |
| Place a model in service | The model is already in service. | causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0 | causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 | VIOLATION | S0 operation_refusals #3 |
| Withdraw a model from service | The model is not in service. | causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0 | causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0 | VIOLATION | S0 operation_refusals #4 |
| Withdraw a model from service | The model is not in service. | causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0 | causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0 | NOT_FOUND | S0 operation_refusals #4 |
| Submit a user prompt | The model is not registered. | causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_NOT_REGISTERED | SUCCESS | S0 operation_refusals #5 |
| Submit a user prompt | The model is not in service. | causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_NOT_IN_SERVICE | SUCCESS | S0 operation_refusals #6 |
| Submit a user prompt | The user prompt contains a more sensitive kind of information than the model may read. | causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_ABOVE_CEILING | SUCCESS | S0 operation_refusals #7 |
| Submit a user prompt | What the model would read is longer than the model can read at once. | causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_TOO_LONG_TO_READ | SUCCESS | S0 operation_refusals #8 |
| Submit a user prompt | The requester is not permitted to act for the customer. | causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_NOT_PERMITTED | SUCCESS | S0 operation_refusals #9 |
| Submit a user prompt | The model cannot finish a response without breaking a response rule. | causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_BY_RULE | SUCCESS | S0 operation_refusals #10 |
| Submit a user prompt | The response reaches the longest response before it is finished. | causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | RECORD_REFUSED_UNFINISHED | SUCCESS | S0 operation_refusals #11 |
| Register a model, place in service, withdraw, retrieve a record | The staff member is not authorized model staff. | causal_language_model::WF_REGISTER_MODEL_V0 | causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 | VIOLATION | S0 operation_refusals #12 |
| Register a model, place in service, withdraw, retrieve a record | The staff member is not authorized model staff. | causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0 | causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 | VIOLATION | S0 operation_refusals #12 |
| Register a model, place in service, withdraw, retrieve a record | The staff member is not authorized model staff. | causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0 | causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 | VIOLATION | S0 operation_refusals #12 |
| Register a model, place in service, withdraw, retrieve a record | The staff member is not authorized model staff. | causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0 | causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 | VIOLATION | S0 operation_refusals #12 |

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
| causal_language_model::CT_WRITE_NEXT_WORD_V0 | offered | atom | causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0 | — | — | — | S4 design_decisions #2 |
| causal_language_model::CT_WRITE_NEXT_WORD_V0 | chosen | atom | causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | — | — | result | S4 design_decisions #3 |
| causal_language_model::CT_WRITE_RESPONSE_V0 | written | loop | causal_language_model::CT_WRITE_NEXT_WORD_V0 | inputs.positions | position | result | S4 design_decisions #2 |

---

## 22. Molecule Step Bindings

<!-- register:molecule_step_bindings optional -->
| CT Code | Step | Role (INPUT, CARRY, UPDATE) | Field | Bound To | Source Finding |
|---------|------|-----------------------------|-------|----------|----------------|
| causal_language_model::CT_WRITE_NEXT_WORD_V0 | offered | INPUT | reading | inputs.reading | S4 design_decisions #2 |
| causal_language_model::CT_WRITE_NEXT_WORD_V0 | offered | INPUT | text | inputs.text | S4 design_decisions #2 |
| causal_language_model::CT_WRITE_NEXT_WORD_V0 | chosen | INPUT | candidates | results.offered.candidates | S4 design_decisions #2 |
| causal_language_model::CT_WRITE_NEXT_WORD_V0 | chosen | INPUT | rules_in_force | inputs.rules_in_force | S4 design_decisions #2 |
| causal_language_model::CT_WRITE_NEXT_WORD_V0 | chosen | INPUT | position | inputs.position | S4 design_decisions #2 |
| causal_language_model::CT_WRITE_NEXT_WORD_V0 | chosen | INPUT | text | inputs.text | S4 design_decisions #2 |
| causal_language_model::CT_WRITE_NEXT_WORD_V0 | chosen | INPUT | finished | inputs.finished | S4 design_decisions #2 |
| causal_language_model::CT_WRITE_NEXT_WORD_V0 | chosen | INPUT | stopped_by | inputs.stopped_by | S4 design_decisions #2 |
| causal_language_model::CT_WRITE_NEXT_WORD_V0 | chosen | INPUT | stopped | inputs.stopped | S4 design_decisions #2 |
| causal_language_model::CT_WRITE_RESPONSE_V0 | written | CARRY | text | "" | S4 design_decisions #2 |
| causal_language_model::CT_WRITE_RESPONSE_V0 | written | CARRY | finished | false | S4 design_decisions #2 |
| causal_language_model::CT_WRITE_RESPONSE_V0 | written | CARRY | stopped_by | "" | S4 design_decisions #2 |
| causal_language_model::CT_WRITE_RESPONSE_V0 | written | CARRY | stopped | [] | S4 design_decisions #2 |
| causal_language_model::CT_WRITE_RESPONSE_V0 | written | INPUT | position | iterator | S4 design_decisions #2 |
| causal_language_model::CT_WRITE_RESPONSE_V0 | written | INPUT | reading | inputs.reading | S4 design_decisions #2 |
| causal_language_model::CT_WRITE_RESPONSE_V0 | written | INPUT | rules_in_force | inputs.rules_in_force | S4 design_decisions #2 |
| causal_language_model::CT_WRITE_RESPONSE_V0 | written | INPUT | text | accumulator.text | S4 design_decisions #2 |
| causal_language_model::CT_WRITE_RESPONSE_V0 | written | INPUT | finished | accumulator.finished | S4 design_decisions #2 |
| causal_language_model::CT_WRITE_RESPONSE_V0 | written | INPUT | stopped_by | accumulator.stopped_by | S4 design_decisions #2 |
| causal_language_model::CT_WRITE_RESPONSE_V0 | written | INPUT | stopped | accumulator.stopped | S4 design_decisions #2 |
| causal_language_model::CT_WRITE_RESPONSE_V0 | written | UPDATE | text | results.text | S4 design_decisions #2 |
| causal_language_model::CT_WRITE_RESPONSE_V0 | written | UPDATE | finished | results.finished | S4 design_decisions #2 |
| causal_language_model::CT_WRITE_RESPONSE_V0 | written | UPDATE | stopped_by | results.stopped_by | S4 design_decisions #2 |
| causal_language_model::CT_WRITE_RESPONSE_V0 | written | UPDATE | stopped | results.stopped | S4 design_decisions #2 |

---

## 23. Test Cases

<!-- register:test_cases optional -->
| CT Code | Case | Expected Outcome (SUCCESS, VIOLATION) | Source Finding |
|---------|------|---------------------------------------|----------------|
| causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0 | forms_key_from_description_and_fingerprint | SUCCESS | human decision |
| causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0 | refuses_blank_fingerprint | VIOLATION | human decision |
| causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0 | admits_kind_within_ceiling | SUCCESS | human decision |
| causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0 | refuses_kind_above_ceiling | VIOLATION | human decision |
| causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0 | assembles_what_fits | SUCCESS | human decision |
| causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0 | refuses_reading_too_long | VIOLATION | human decision |
| causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0 | adds_the_account_rule_and_positions | SUCCESS | human decision |
| causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0 | offers_candidates | SUCCESS | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | stops_another_customers_account_and_continues | SUCCESS | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | writes_the_customers_own_account | SUCCESS | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | names_the_rule_when_no_permitted_word_remains | SUCCESS | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | finishes_on_the_end_of_the_response | SUCCESS | human decision |
| causal_language_model::CT_WRITE_NEXT_WORD_V0 | writes_one_permitted_word_from_a_recorded_offer | SUCCESS | human decision |
| causal_language_model::CT_WRITE_RESPONSE_V0 | writes_a_finished_response_from_recorded_offers | SUCCESS | human decision |
| causal_language_model::CT_WRITE_RESPONSE_V0 | stops_unfinished_at_the_longest_response | SUCCESS | human decision |

---

## 24. Test Case Values

<!-- register:test_case_values optional -->
| CT Code | Case | Role (INPUT, EXPECTED, ASSERT, RECORDED) | Field | Value | Source Finding |
|---------|------|------------------------------------------|-------|-------|----------------|
| causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0 | forms_key_from_description_and_fingerprint | INPUT | description | {reading_capacity: 64, layers: 2} | human decision |
| causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0 | forms_key_from_description_and_fingerprint | INPUT | fingerprint | sha256:ab12 | human decision |
| causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0 | forms_key_from_description_and_fingerprint | EXPECTED | identity_key | '{"layers":2,"reading_capacity":64}\|sha256:ab12' | human decision |
| causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0 | refuses_blank_fingerprint | INPUT | description | {reading_capacity: 64, layers: 2} | human decision |
| causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0 | refuses_blank_fingerprint | INPUT | fingerprint | " " | human decision |
| causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0 | admits_kind_within_ceiling | INPUT | kind | internal | human decision |
| causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0 | admits_kind_within_ceiling | INPUT | ceiling | confidential | human decision |
| causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0 | admits_kind_within_ceiling | INPUT | kinds | [public, internal, confidential, restricted] | human decision |
| causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0 | admits_kind_within_ceiling | EXPECTED | within_ceiling | true | human decision |
| causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0 | refuses_kind_above_ceiling | INPUT | kind | restricted | human decision |
| causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0 | refuses_kind_above_ceiling | INPUT | ceiling | internal | human decision |
| causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0 | refuses_kind_above_ceiling | INPUT | kinds | [public, internal, confidential, restricted] | human decision |
| causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0 | assembles_what_fits | INPUT | system_prompt | Answer briefly. | human decision |
| causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0 | assembles_what_fits | INPUT | question | What is my balance? | human decision |
| causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0 | assembles_what_fits | INPUT | supporting_material | Account 12345678 balance 40. | human decision |
| causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0 | assembles_what_fits | INPUT | reading_capacity | 20 | human decision |
| causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0 | assembles_what_fits | EXPECTED | reading | {system_prompt: Answer briefly., question: What is my balance?, supporting_material: Account 12345678 balance 40.} | human decision |
| causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0 | assembles_what_fits | EXPECTED | reading_length | 11 | human decision |
| causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0 | refuses_reading_too_long | INPUT | system_prompt | Answer briefly. | human decision |
| causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0 | refuses_reading_too_long | INPUT | question | What is my balance? | human decision |
| causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0 | refuses_reading_too_long | INPUT | supporting_material | Account 12345678 balance 40. | human decision |
| causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0 | refuses_reading_too_long | INPUT | reading_capacity | 5 | human decision |
| causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0 | adds_the_account_rule_and_positions | INPUT | response_rules | {forbidden: [{rule: no_guarantees, pattern: '^guaranteed$'}], account_number_pattern: '^[0-9]{8}$', freedom: 0, longest_response: 3} | human decision |
| causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0 | adds_the_account_rule_and_positions | INPUT | account_numbers | ['12345678'] | human decision |
| causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0 | adds_the_account_rule_and_positions | INPUT | seed | 7 | human decision |
| causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0 | adds_the_account_rule_and_positions | EXPECTED | rules_in_force | {forbidden: [{rule: no_guarantees, pattern: '^guaranteed$'}, {rule: another_customers_account_number, pattern: '^[0-9]{8}$', except: ['12345678']}], freedom: 0, seed: 7} | human decision |
| causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0 | adds_the_account_rule_and_positions | EXPECTED | positions | [1, 2, 3] | human decision |
| causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0 | offers_candidates | INPUT | reading | {system_prompt: Answer briefly., question: What is my balance?, supporting_material: Account 12345678 balance 40.} | human decision |
| causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0 | offers_candidates | INPUT | text | "" | human decision |
| causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0 | offers_candidates | ASSERT | candidates | {mode: property, type: non_zero} | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | stops_another_customers_account_and_continues | INPUT | candidates | [{word: '87654321', likelihood: 0.6}, {word: Your, likelihood: 0.3}] | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | stops_another_customers_account_and_continues | INPUT | rules_in_force | {forbidden: [{rule: no_guarantees, pattern: '^guaranteed$'}, {rule: another_customers_account_number, pattern: '^[0-9]{8}$', except: ['12345678']}], freedom: 0, seed: 7} | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | stops_another_customers_account_and_continues | INPUT | position | 1 | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | stops_another_customers_account_and_continues | INPUT | text | "" | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | stops_another_customers_account_and_continues | INPUT | finished | false | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | stops_another_customers_account_and_continues | INPUT | stopped_by | "" | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | stops_another_customers_account_and_continues | INPUT | stopped | [] | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | stops_another_customers_account_and_continues | EXPECTED | text | Your | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | stops_another_customers_account_and_continues | EXPECTED | finished | false | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | stops_another_customers_account_and_continues | EXPECTED | stopped_by | "" | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | stops_another_customers_account_and_continues | EXPECTED | stopped | [{position: 1, word: '87654321', rule: another_customers_account_number}] | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | writes_the_customers_own_account | INPUT | candidates | [{word: '12345678', likelihood: 0.8}] | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | writes_the_customers_own_account | INPUT | rules_in_force | {forbidden: [{rule: no_guarantees, pattern: '^guaranteed$'}, {rule: another_customers_account_number, pattern: '^[0-9]{8}$', except: ['12345678']}], freedom: 0, seed: 7} | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | writes_the_customers_own_account | INPUT | position | 2 | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | writes_the_customers_own_account | INPUT | text | Account | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | writes_the_customers_own_account | INPUT | finished | false | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | writes_the_customers_own_account | INPUT | stopped_by | "" | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | writes_the_customers_own_account | INPUT | stopped | [] | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | writes_the_customers_own_account | EXPECTED | text | Account 12345678 | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | writes_the_customers_own_account | EXPECTED | finished | false | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | writes_the_customers_own_account | EXPECTED | stopped_by | "" | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | writes_the_customers_own_account | EXPECTED | stopped | [] | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | names_the_rule_when_no_permitted_word_remains | INPUT | candidates | [{word: '87654321', likelihood: 0.9}] | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | names_the_rule_when_no_permitted_word_remains | INPUT | rules_in_force | {forbidden: [{rule: no_guarantees, pattern: '^guaranteed$'}, {rule: another_customers_account_number, pattern: '^[0-9]{8}$', except: ['12345678']}], freedom: 0, seed: 7} | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | names_the_rule_when_no_permitted_word_remains | INPUT | position | 1 | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | names_the_rule_when_no_permitted_word_remains | INPUT | text | "" | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | names_the_rule_when_no_permitted_word_remains | INPUT | finished | false | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | names_the_rule_when_no_permitted_word_remains | INPUT | stopped_by | "" | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | names_the_rule_when_no_permitted_word_remains | INPUT | stopped | [] | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | names_the_rule_when_no_permitted_word_remains | EXPECTED | text | "" | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | names_the_rule_when_no_permitted_word_remains | EXPECTED | finished | false | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | names_the_rule_when_no_permitted_word_remains | EXPECTED | stopped_by | another_customers_account_number | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | names_the_rule_when_no_permitted_word_remains | EXPECTED | stopped | [{position: 1, word: '87654321', rule: another_customers_account_number}] | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | finishes_on_the_end_of_the_response | INPUT | candidates | [{word: <end>, likelihood: 0.9}] | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | finishes_on_the_end_of_the_response | INPUT | rules_in_force | {forbidden: [{rule: no_guarantees, pattern: '^guaranteed$'}, {rule: another_customers_account_number, pattern: '^[0-9]{8}$', except: ['12345678']}], freedom: 0, seed: 7} | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | finishes_on_the_end_of_the_response | INPUT | position | 3 | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | finishes_on_the_end_of_the_response | INPUT | text | Your balance | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | finishes_on_the_end_of_the_response | INPUT | finished | false | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | finishes_on_the_end_of_the_response | INPUT | stopped_by | "" | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | finishes_on_the_end_of_the_response | INPUT | stopped | [] | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | finishes_on_the_end_of_the_response | EXPECTED | text | Your balance | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | finishes_on_the_end_of_the_response | EXPECTED | finished | true | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | finishes_on_the_end_of_the_response | EXPECTED | stopped_by | "" | human decision |
| causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | finishes_on_the_end_of_the_response | EXPECTED | stopped | [] | human decision |
| causal_language_model::CT_WRITE_NEXT_WORD_V0 | writes_one_permitted_word_from_a_recorded_offer | INPUT | reading | {system_prompt: Answer briefly., question: What is my balance?, supporting_material: Account 12345678 balance 40.} | human decision |
| causal_language_model::CT_WRITE_NEXT_WORD_V0 | writes_one_permitted_word_from_a_recorded_offer | INPUT | rules_in_force | {forbidden: [{rule: no_guarantees, pattern: '^guaranteed$'}, {rule: another_customers_account_number, pattern: '^[0-9]{8}$', except: ['12345678']}], freedom: 0, seed: 7} | human decision |
| causal_language_model::CT_WRITE_NEXT_WORD_V0 | writes_one_permitted_word_from_a_recorded_offer | INPUT | position | 1 | human decision |
| causal_language_model::CT_WRITE_NEXT_WORD_V0 | writes_one_permitted_word_from_a_recorded_offer | INPUT | text | "" | human decision |
| causal_language_model::CT_WRITE_NEXT_WORD_V0 | writes_one_permitted_word_from_a_recorded_offer | INPUT | finished | false | human decision |
| causal_language_model::CT_WRITE_NEXT_WORD_V0 | writes_one_permitted_word_from_a_recorded_offer | INPUT | stopped_by | "" | human decision |
| causal_language_model::CT_WRITE_NEXT_WORD_V0 | writes_one_permitted_word_from_a_recorded_offer | INPUT | stopped | [] | human decision |
| causal_language_model::CT_WRITE_NEXT_WORD_V0 | writes_one_permitted_word_from_a_recorded_offer | RECORDED | offered | {candidates: [{word: '87654321', likelihood: 0.6}, {word: Your, likelihood: 0.3}]} | human decision |
| causal_language_model::CT_WRITE_NEXT_WORD_V0 | writes_one_permitted_word_from_a_recorded_offer | EXPECTED | result | {text: Your, finished: false, stopped_by: '', stopped: [{position: 1, word: '87654321', rule: another_customers_account_number}]} | human decision |
| causal_language_model::CT_WRITE_RESPONSE_V0 | writes_a_finished_response_from_recorded_offers | INPUT | reading | {system_prompt: Answer briefly., question: What is my balance?, supporting_material: Account 12345678 balance 40.} | human decision |
| causal_language_model::CT_WRITE_RESPONSE_V0 | writes_a_finished_response_from_recorded_offers | INPUT | rules_in_force | {forbidden: [{rule: no_guarantees, pattern: '^guaranteed$'}, {rule: another_customers_account_number, pattern: '^[0-9]{8}$', except: ['12345678']}], freedom: 0, seed: 7} | human decision |
| causal_language_model::CT_WRITE_RESPONSE_V0 | writes_a_finished_response_from_recorded_offers | INPUT | positions | [1, 2, 3] | human decision |
| causal_language_model::CT_WRITE_RESPONSE_V0 | writes_a_finished_response_from_recorded_offers | RECORDED | written[0]/offered | {candidates: [{word: '87654321', likelihood: 0.6}, {word: Your, likelihood: 0.3}]} | human decision |
| causal_language_model::CT_WRITE_RESPONSE_V0 | writes_a_finished_response_from_recorded_offers | RECORDED | written[1]/offered | {candidates: [{word: balance, likelihood: 0.9}]} | human decision |
| causal_language_model::CT_WRITE_RESPONSE_V0 | writes_a_finished_response_from_recorded_offers | RECORDED | written[2]/offered | {candidates: [{word: <end>, likelihood: 0.9}]} | human decision |
| causal_language_model::CT_WRITE_RESPONSE_V0 | writes_a_finished_response_from_recorded_offers | EXPECTED | result | {text: Your balance, finished: true, stopped_by: '', stopped: [{position: 1, word: '87654321', rule: another_customers_account_number}]} | human decision |
| causal_language_model::CT_WRITE_RESPONSE_V0 | stops_unfinished_at_the_longest_response | INPUT | reading | {system_prompt: Answer briefly., question: What is my balance?, supporting_material: Account 12345678 balance 40.} | human decision |
| causal_language_model::CT_WRITE_RESPONSE_V0 | stops_unfinished_at_the_longest_response | INPUT | rules_in_force | {forbidden: [{rule: no_guarantees, pattern: '^guaranteed$'}, {rule: another_customers_account_number, pattern: '^[0-9]{8}$', except: ['12345678']}], freedom: 0, seed: 7} | human decision |
| causal_language_model::CT_WRITE_RESPONSE_V0 | stops_unfinished_at_the_longest_response | INPUT | positions | [1] | human decision |
| causal_language_model::CT_WRITE_RESPONSE_V0 | stops_unfinished_at_the_longest_response | RECORDED | written[0]/offered | {candidates: [{word: Your, likelihood: 0.9}]} | human decision |
| causal_language_model::CT_WRITE_RESPONSE_V0 | stops_unfinished_at_the_longest_response | EXPECTED | result | {text: Your, finished: false, stopped_by: '', stopped: []} | human decision |

---

## gov_projection — Governed Handoff to Stage 8

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 6 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
| **Emits** → Stage 8 | design_resolution · existing_inventory · new_artifacts · rb_declarations · execution_topology · cc_composition · step_bindings · interface_fields · implementation_bindings · vocabulary_extensions · runtime_policies · artifact_properties · structure_stores · artifact_summary · generation_provenance |
