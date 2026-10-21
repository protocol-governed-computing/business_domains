# Design Intent — causal_language_model, baseline

## Machine

```yaml
document:
  phase: p7
  domain: causal_language_model
  subdomain:
  - model_response
  cr: baseline
  rule_set: transformation.schemas.REGISTER_SCHEMA_P7_V0
registers:
  design_resolution: []
  existing_inventory: []
  new_artifacts:
  - family: AC
    code: causal_language_model::AC_MODEL_HOST_V0
    summary: The host of a model in service, which proposes and holds no authority
    owner_subdomain: model_response
    status: NEW
  - family: AC
    code: causal_language_model::AC_MODEL_STAFF_V0
    summary: The actor whose authorization every model staff operation binds
    owner_subdomain: model_response
    status: NEW
  - family: AC
    code: causal_language_model::AC_REQUESTER_V0
    summary: The actor who submits a user prompt for one customer
    owner_subdomain: model_response
    status: NEW
  - family: CC
    code: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    summary: Refuse a user prompt before the model sees it when its model is not registered or not in
      service
    owner_subdomain: model_response
    status: NEW
  - family: CC
    code: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    summary: Append a durable account of a performed operation to the subdomain's own trail
    owner_subdomain: model_response
    status: NEW
  - family: CC
    code: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    summary: Choose a permitted token from an offer under the rules in force
    owner_subdomain: model_response
    status: NEW
  - family: CC
    code: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    summary: Claim a model's identity so a second registration of the same model is refused
    owner_subdomain: model_response
    status: NEW
  - family: CC
    code: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    summary: Claim a user prompt's identity so a second submission under it is refused
    owner_subdomain: model_response
    status: NEW
  - family: CC
    code: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
    summary: Refuse an offer whose reported reading size exceeds the model's capacity
    owner_subdomain: model_response
    status: NEW
  - family: CC
    code: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    summary: Confirm the staff member is model staff
    owner_subdomain: model_response
    status: NEW
  - family: CC
    code: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
    summary: Refuse an offer naming another model's fingerprint
    owner_subdomain: model_response
    status: NEW
  - family: CC
    code: causal_language_model::CC_CONFIRM_READING_FITS_V0
    summary: Assemble exactly what the model reads and refuse it before the model sees it when it is too
      long
    owner_subdomain: model_response
    status: NEW
  - family: CC
    code: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    summary: Confirm the requester may act for the customer the user prompt is for
    owner_subdomain: model_response
    status: NEW
  - family: CC
    code: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
    summary: Confirm one release condition of a written response, refusing it otherwise
    owner_subdomain: model_response
    status: NEW
  - family: CC
    code: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    summary: Refuse a user prompt before the model sees it when it states a kind more sensitive than the
      ceiling
    owner_subdomain: model_response
    status: NEW
  - family: CC
    code: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    summary: Form the rules in force and open the record of a hosted request
    owner_subdomain: model_response
    status: NEW
  - family: CC
    code: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    summary: Open a time in service with its ceiling, system prompt and response rules, and mark the model
      in service
    owner_subdomain: model_response
    status: NEW
  - family: CC
    code: causal_language_model::CC_READ_HOSTED_STATE_V0
    summary: Read a hosted request's trail and reduce it to the response as built
    owner_subdomain: model_response
    status: NEW
  - family: CC
    code: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    summary: Record an offer and the choice made from it in the request's trail
    owner_subdomain: model_response
    status: NEW
  - family: CC
    code: causal_language_model::CC_RECORD_USER_PROMPT_V0
    summary: Append the user prompt record with what the model read, the rules in force and the outcome
    owner_subdomain: model_response
    status: NEW
  - family: CC
    code: causal_language_model::CC_REGISTER_MODEL_V0
    summary: Record a model's description and fingerprint as its record, registered
    owner_subdomain: model_response
    status: NEW
  - family: CC
    code: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
    summary: Read the record of a user prompt
    owner_subdomain: model_response
    status: NEW
  - family: CC
    code: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    summary: Close the time in service and mark the model registered
    owner_subdomain: model_response
    status: NEW
  - family: CC
    code: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    summary: Form the rules in force and write the response word by word under them
    owner_subdomain: model_response
    status: NEW
  - family: CT
    code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    summary: 'The model''s step: offers its next words given the response so far; the one step whose result
      is not determined by its inputs'
    owner_subdomain: model_response
    status: NEW
  - family: CT
    code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    summary: Assembles exactly what the model reads and decides whether it fits what the model can read
      at once
    owner_subdomain: model_response
    status: NEW
  - family: CT
    code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    summary: Stops forbidden tokens among those offered and chooses one permitted token, joined as it
      is, within the permitted length
    owner_subdomain: model_response
    status: NEW
  - family: CT
    code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    summary: Stops forbidden words among those offered and chooses one permitted word under the freedom
      of word choice and a stated seed
    owner_subdomain: model_response
    status: NEW
  - family: CT
    code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    summary: Decides whether a kind of information is no more sensitive than a ceiling, by the declared
      order
    owner_subdomain: model_response
    status: NEW
  - family: CT
    code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    summary: Forms the single key claimed for a model from its description and fingerprint
    owner_subdomain: model_response
    status: NEW
  - family: CT
    code: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    summary: Forms the response rules in force for one user prompt from the time in service and the customer's
      account numbers
    owner_subdomain: model_response
    status: NEW
  - family: CT
    code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
    summary: Reduces a hosted request's trail to the response as built, its position, whether it is complete,
      and its permitted length
    owner_subdomain: model_response
    status: NEW
  - family: CT
    code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    summary: One pass of writing, composed of the model's offer and the rules' choice
    owner_subdomain: model_response
    status: NEW
  - family: CT
    code: causal_language_model::CT_WRITE_RESPONSE_V0
    summary: Writes a response by repeating one pass per word, up to the longest response, carrying the
      response so far and the words stopped
    owner_subdomain: model_response
    status: NEW
  - family: EV
    code: causal_language_model::EV_MODEL_REGISTERED_V0
    summary: The moment the business records a model
    owner_subdomain: model_response
    status: NEW
  - family: EV
    code: causal_language_model::EV_MODEL_SERVICE_ENDED_V0
    summary: The moment a model is withdrawn from service and its time in service ends
    owner_subdomain: model_response
    status: NEW
  - family: EV
    code: causal_language_model::EV_MODEL_SERVICE_STARTED_V0
    summary: The moment a model is placed in service and a time in service begins
    owner_subdomain: model_response
    status: NEW
  - family: EV
    code: causal_language_model::EV_USER_PROMPT_REFUSED_V0
    summary: The moment a user prompt yields no response
    owner_subdomain: model_response
    status: NEW
  - family: EV
    code: causal_language_model::EV_USER_PROMPT_RESPONDED_V0
    summary: The moment a model response is released
    owner_subdomain: model_response
    status: NEW
  - family: IN
    code: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
    summary: A request to a hosted model on behalf of a customer
    owner_subdomain: model_response
    status: NEW
  - family: IN
    code: causal_language_model::IN_OFFER_NEXT_TOKENS_V0
    summary: The candidates a hosted model could write next, naming its fingerprint and the size of what
      it reads
    owner_subdomain: model_response
    status: NEW
  - family: IN
    code: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
    summary: A request to place a registered model in service with its ceiling, system prompt and response
      rules
    owner_subdomain: model_response
    status: NEW
  - family: IN
    code: causal_language_model::IN_REGISTER_MODEL_V0
    summary: A request to register a model with its description and fingerprint
    owner_subdomain: model_response
    status: NEW
  - family: IN
    code: causal_language_model::IN_RELEASE_HOSTED_RESPONSE_V0
    summary: A request to release a completed hosted response
    owner_subdomain: model_response
    status: NEW
  - family: IN
    code: causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0
    summary: A request to retrieve the record of a user prompt
    owner_subdomain: model_response
    status: NEW
  - family: IN
    code: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
    summary: A user prompt submitted on behalf of a customer
    owner_subdomain: model_response
    status: NEW
  - family: IN
    code: causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0
    summary: A request to withdraw a model from service
    owner_subdomain: model_response
    status: NEW
  - family: STRUCTURE
    code: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    summary: Declares the seven stores the subdomain owns and the paths they occupy
    owner_subdomain: model_response
    status: NEW
  - family: RB
    code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    summary: Binds every model response workflow to the mechanisms and stores it uses
    owner_subdomain: model_response
    status: NEW
  - family: VOCAB
    code: causal_language_model::VOCAB_KIND_OF_INFORMATION_V0
    summary: ''
    owner_subdomain: model_response
    status: NEW
  - family: WF
    code: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    summary: Admitting a hosted request and opening its record, or refusing it
    owner_subdomain: model_response
    status: NEW
  - family: WF
    code: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    summary: Choosing a permitted token from an offer and recording the step, or refusing the request
    owner_subdomain: model_response
    status: NEW
  - family: WF
    code: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    summary: Opening a time in service for a registered model not already in service
    owner_subdomain: model_response
    status: NEW
  - family: WF
    code: causal_language_model::WF_REGISTER_MODEL_V0
    summary: Registering a model, refusing a second registration of the same model
    owner_subdomain: model_response
    status: NEW
  - family: WF
    code: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    summary: Releasing a completed hosted response from the record
    owner_subdomain: model_response
    status: NEW
  - family: WF
    code: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    summary: Reading a user prompt record and recording that it was read
    owner_subdomain: model_response
    status: NEW
  - family: WF
    code: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    summary: Admitting a user prompt, writing the response under the rules, releasing or refusing it,
      and recording it
    owner_subdomain: model_response
    status: NEW
  - family: WF
    code: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    summary: Closing a model's time in service
    owner_subdomain: model_response
    status: NEW
  rb_declarations:
  - rb_code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    binds_wf: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
  - rb_code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    binds_wf: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
  - rb_code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    binds_wf: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
  - rb_code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    binds_wf: causal_language_model::WF_REGISTER_MODEL_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
  - rb_code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    binds_wf: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
  - rb_code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    binds_wf: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
  - rb_code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    binds_wf: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
  - rb_code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    binds_wf: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
  execution_topology:
  - workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    node: IN_BEGIN_HOSTED_RESPONSE_V0
    node_type: IN
    routing:
      ACK: CC_CLAIM_USER_PROMPT_IDENTITY_V0
      NACK: EXIT_REJECTED
  - workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    node: CC_CLAIM_USER_PROMPT_IDENTITY_V0
    node_type: CC
    routing:
      SUCCESS: CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
      ALREADY_EXISTS: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    node: CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    node_type: CC
    routing:
      SUCCESS: CC_ADMIT_USER_PROMPT_V0
      VIOLATION: RECORD_REFUSED_NOT_PERMITTED
  - workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    node: CC_ADMIT_USER_PROMPT_V0
    node_type: CC
    routing:
      SUCCESS: CC_CONFIRM_WITHIN_CEILING_V0
      NOT_FOUND: RECORD_REFUSED_NOT_REGISTERED
      VIOLATION: RECORD_REFUSED_NOT_IN_SERVICE
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    node: CC_CONFIRM_WITHIN_CEILING_V0
    node_type: CC
    routing:
      SUCCESS: CC_CONFIRM_READING_FITS_V0
      NOT_FOUND: RECORD_REFUSED_NOT_IN_SERVICE
      VIOLATION: RECORD_REFUSED_ABOVE_CEILING
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    node: CC_CONFIRM_READING_FITS_V0
    node_type: CC
    routing:
      SUCCESS: CC_OPEN_HOSTED_RECORD_V0
      VIOLATION: RECORD_REFUSED_TOO_LONG_TO_READ
  - workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    node: CC_OPEN_HOSTED_RECORD_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_WRITING
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    node: RECORD_REFUSED_NOT_PERMITTED
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_USER_PROMPT_V0
  - workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    node: RECORD_REFUSED_NOT_REGISTERED
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_USER_PROMPT_V0
  - workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    node: RECORD_REFUSED_NOT_IN_SERVICE
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_USER_PROMPT_V0
  - workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    node: RECORD_REFUSED_ABOVE_CEILING
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_USER_PROMPT_V0
  - workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    node: RECORD_REFUSED_TOO_LONG_TO_READ
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_USER_PROMPT_V0
  - workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    node: EXIT_WRITING
    node_type: EXIT
    routing: null
  - workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    node: EXIT_REFUSED
    node_type: EXIT
    routing: null
  - workflow: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: IN_OFFER_NEXT_TOKENS_V0
    node_type: IN
    routing:
      ACK: CC_READ_HOSTED_STATE_V0
      NACK: EXIT_REJECTED
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: CC_READ_HOSTED_STATE_V0
    node_type: CC
    routing:
      SUCCESS: CC_CONFIRM_OFFER_FOR_MODEL_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: CC_CONFIRM_OFFER_FOR_MODEL_V0
    node_type: CC
    routing:
      SUCCESS: CC_CONFIRM_HOSTED_READING_FITS_V0
      VIOLATION: RECORD_REFUSED_OTHER_MODEL
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: CC_CONFIRM_HOSTED_READING_FITS_V0
    node_type: CC
    routing:
      SUCCESS: CC_CHOOSE_PERMITTED_TOKEN_V0
      VIOLATION: RECORD_REFUSED_TOO_LONG_TO_READ
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: CC_CHOOSE_PERMITTED_TOKEN_V0
    node_type: CC
    routing:
      SUCCESS: CONFIRM_NO_RULE_STOPPED
      VIOLATION: EXIT_REJECTED
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: CONFIRM_NO_RULE_STOPPED
    node_type: CC
    routing:
      SUCCESS: CONFIRM_WITHIN_LENGTH
      VIOLATION: RECORD_STOPPED_STEP
    runs: CC_CONFIRM_RESPONSE_RELEASABLE_V0
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: CONFIRM_WITHIN_LENGTH
    node_type: CC
    routing:
      SUCCESS: RECORD_STEP
      VIOLATION: RECORD_UNFINISHED_STEP
    runs: CC_CONFIRM_RESPONSE_RELEASABLE_V0
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: RECORD_STEP
    node_type: CC
    routing:
      SUCCESS: EXIT_CHOSEN
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_HOSTED_STEP_V0
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: RECORD_STOPPED_STEP
    node_type: CC
    routing:
      SUCCESS: RECORD_REFUSED_BY_RULE
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_HOSTED_STEP_V0
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: RECORD_UNFINISHED_STEP
    node_type: CC
    routing:
      SUCCESS: RECORD_REFUSED_UNFINISHED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_HOSTED_STEP_V0
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: RECORD_REFUSED_OTHER_MODEL
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_USER_PROMPT_V0
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: RECORD_REFUSED_TOO_LONG_TO_READ
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_USER_PROMPT_V0
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: RECORD_REFUSED_BY_RULE
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_USER_PROMPT_V0
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: RECORD_REFUSED_UNFINISHED
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_USER_PROMPT_V0
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: EXIT_CHOSEN
    node_type: EXIT
    routing: null
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: EXIT_REFUSED
    node_type: EXIT
    routing: null
  - workflow: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    node: IN_PLACE_MODEL_IN_SERVICE_V0
    node_type: IN
    routing:
      ACK: CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
  - workflow: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    node: CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    node_type: CC
    routing:
      SUCCESS: CC_PLACE_MODEL_IN_SERVICE_V0
      VIOLATION: EXIT_REJECTED
  - workflow: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    node: CC_PLACE_MODEL_IN_SERVICE_V0
    node_type: CC
    routing:
      SUCCESS: CC_APPEND_MODEL_OPERATION_V0
      NOT_FOUND: EXIT_REJECTED
      ALREADY_EXISTS: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    node: CC_APPEND_MODEL_OPERATION_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_PLACED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    node: EXIT_PLACED
    node_type: EXIT
    routing: null
  - workflow: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: causal_language_model::WF_REGISTER_MODEL_V0
    node: IN_REGISTER_MODEL_V0
    node_type: IN
    routing:
      ACK: CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
  - workflow: causal_language_model::WF_REGISTER_MODEL_V0
    node: CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    node_type: CC
    routing:
      SUCCESS: CC_CLAIM_MODEL_IDENTITY_V0
      VIOLATION: EXIT_REJECTED
  - workflow: causal_language_model::WF_REGISTER_MODEL_V0
    node: CC_CLAIM_MODEL_IDENTITY_V0
    node_type: CC
    routing:
      SUCCESS: CC_REGISTER_MODEL_V0
      ALREADY_EXISTS: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: causal_language_model::WF_REGISTER_MODEL_V0
    node: CC_REGISTER_MODEL_V0
    node_type: CC
    routing:
      SUCCESS: CC_APPEND_MODEL_OPERATION_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: causal_language_model::WF_REGISTER_MODEL_V0
    node: CC_APPEND_MODEL_OPERATION_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_REGISTERED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: causal_language_model::WF_REGISTER_MODEL_V0
    node: EXIT_REGISTERED
    node_type: EXIT
    routing: null
  - workflow: causal_language_model::WF_REGISTER_MODEL_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    node: IN_RELEASE_HOSTED_RESPONSE_V0
    node_type: IN
    routing:
      ACK: CC_READ_HOSTED_STATE_V0
      NACK: EXIT_REJECTED
  - workflow: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    node: CC_READ_HOSTED_STATE_V0
    node_type: CC
    routing:
      SUCCESS: CONFIRM_FINISHED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    node: CONFIRM_FINISHED
    node_type: CC
    routing:
      SUCCESS: RECORD_RESPONDED
      VIOLATION: EXIT_REJECTED
    runs: CC_CONFIRM_RESPONSE_RELEASABLE_V0
  - workflow: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    node: RECORD_RESPONDED
    node_type: CC
    routing:
      SUCCESS: EXIT_RESPONDED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_USER_PROMPT_V0
  - workflow: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    node: EXIT_RESPONDED
    node_type: EXIT
    routing: null
  - workflow: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    node: IN_RETRIEVE_USER_PROMPT_RECORD_V0
    node_type: IN
    routing:
      ACK: CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
  - workflow: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    node: CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    node_type: CC
    routing:
      SUCCESS: CC_APPEND_MODEL_OPERATION_V0
      VIOLATION: EXIT_REJECTED
  - workflow: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    node: CC_APPEND_MODEL_OPERATION_V0
    node_type: CC
    routing:
      SUCCESS: CC_RETRIEVE_USER_PROMPT_RECORD_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    node: CC_RETRIEVE_USER_PROMPT_RECORD_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_RETRIEVED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    node: EXIT_RETRIEVED
    node_type: EXIT
    routing: null
  - workflow: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: IN_SUBMIT_USER_PROMPT_V0
    node_type: IN
    routing:
      ACK: CC_CLAIM_USER_PROMPT_IDENTITY_V0
      NACK: EXIT_REJECTED
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: CC_CLAIM_USER_PROMPT_IDENTITY_V0
    node_type: CC
    routing:
      SUCCESS: CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
      ALREADY_EXISTS: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    node_type: CC
    routing:
      SUCCESS: CC_ADMIT_USER_PROMPT_V0
      VIOLATION: RECORD_REFUSED_NOT_PERMITTED
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: CC_ADMIT_USER_PROMPT_V0
    node_type: CC
    routing:
      SUCCESS: CC_CONFIRM_WITHIN_CEILING_V0
      NOT_FOUND: RECORD_REFUSED_NOT_REGISTERED
      VIOLATION: RECORD_REFUSED_NOT_IN_SERVICE
      BACKEND_ERROR: RECORD_FAILED_BEFORE_READING
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: CC_CONFIRM_WITHIN_CEILING_V0
    node_type: CC
    routing:
      SUCCESS: CC_CONFIRM_READING_FITS_V0
      NOT_FOUND: RECORD_REFUSED_NOT_IN_SERVICE
      VIOLATION: RECORD_REFUSED_ABOVE_CEILING
      BACKEND_ERROR: RECORD_FAILED_BEFORE_READING
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: CC_CONFIRM_READING_FITS_V0
    node_type: CC
    routing:
      SUCCESS: CC_WRITE_MODEL_RESPONSE_V0
      VIOLATION: RECORD_REFUSED_TOO_LONG_TO_READ
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: CC_WRITE_MODEL_RESPONSE_V0
    node_type: CC
    routing:
      SUCCESS: CONFIRM_NO_RULE_STOPPED
      VIOLATION: RECORD_FAILED_WHILE_WRITING
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: CONFIRM_NO_RULE_STOPPED
    node_type: CC
    routing:
      SUCCESS: CONFIRM_FINISHED
      VIOLATION: RECORD_REFUSED_BY_RULE
    runs: CC_CONFIRM_RESPONSE_RELEASABLE_V0
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: CONFIRM_FINISHED
    node_type: CC
    routing:
      SUCCESS: RECORD_RESPONDED
      VIOLATION: RECORD_REFUSED_UNFINISHED
    runs: CC_CONFIRM_RESPONSE_RELEASABLE_V0
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: RECORD_RESPONDED
    node_type: CC
    routing:
      SUCCESS: EXIT_RESPONDED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_USER_PROMPT_V0
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: RECORD_REFUSED_NOT_PERMITTED
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_USER_PROMPT_V0
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: RECORD_REFUSED_NOT_REGISTERED
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_USER_PROMPT_V0
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: RECORD_REFUSED_NOT_IN_SERVICE
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_USER_PROMPT_V0
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: RECORD_REFUSED_ABOVE_CEILING
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_USER_PROMPT_V0
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: RECORD_REFUSED_TOO_LONG_TO_READ
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_USER_PROMPT_V0
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: RECORD_REFUSED_BY_RULE
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_USER_PROMPT_V0
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: RECORD_REFUSED_UNFINISHED
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_USER_PROMPT_V0
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: RECORD_FAILED_BEFORE_READING
    node_type: CC
    routing:
      SUCCESS: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_USER_PROMPT_V0
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: RECORD_FAILED_WHILE_WRITING
    node_type: CC
    routing:
      SUCCESS: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_USER_PROMPT_V0
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: EXIT_RESPONDED
    node_type: EXIT
    routing: null
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: EXIT_REFUSED
    node_type: EXIT
    routing: null
  - workflow: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    node: IN_WITHDRAW_MODEL_FROM_SERVICE_V0
    node_type: IN
    routing:
      ACK: CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
  - workflow: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    node: CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    node_type: CC
    routing:
      SUCCESS: CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      VIOLATION: EXIT_REJECTED
  - workflow: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    node: CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    node_type: CC
    routing:
      SUCCESS: CC_APPEND_MODEL_OPERATION_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    node: CC_APPEND_MODEL_OPERATION_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_WITHDRAWN
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    node: EXIT_WITHDRAWN
    node_type: EXIT
    routing: null
  - workflow: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  cc_composition:
  - cc_code: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    step: '1'
    step_name: read_model_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: READ
    store: MODELS
    consumes:
    - key
    produces:
    - model_record
    - result_status
    routing:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
      out:
        model_record: model_record
        result_status: result_status
  - cc_code: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    step: '2'
    step_name: require_in_service
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - parameters
    - rules
    produces:
    - valid
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: parameters
        rules: rules
      out:
        valid: valid
  - cc_code: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    step: '1'
    step_name: append_operation
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    kind: CS
    operation: APPEND
    store: MODEL_OPERATIONS
    consumes:
    - record
    - stream_id
    - actor_id
    produces:
    - record_id
    - sequence_number
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        record: record
        stream_id: stream_id
        actor_id: actor_id
      out:
        record_id: record_id
        sequence_number: sequence_number
  - cc_code: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    step: '1'
    step_name: choose_token
    capability: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - state
    - candidates
    produces:
    - step
    - text
    - finished
    - stopped_by
    - within_length
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        state: state
        candidates: candidates
      out:
        step: step
        text: text
        finished: finished
        stopped_by: stopped_by
        within_length: within_length
  - cc_code: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: '1'
    step_name: validate_description
    capability: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - record
    - schema
    produces:
    - violations
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        record: record
        schema: schema
      out:
        violations: violations
  - cc_code: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: '2'
    step_name: require_description_complete
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - parameters
    - rules
    produces:
    - valid
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: parameters
        rules: rules
      out:
        valid: valid
  - cc_code: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: '3'
    step_name: form_identity_key
    capability: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - description
    - fingerprint
    produces:
    - identity_key
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        description: description
        fingerprint: fingerprint
      out:
        identity_key: identity_key
  - cc_code: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: '4'
    step_name: claim_identity
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: REGISTER
    store: MODEL_IDENTITY_REGISTRY
    consumes:
    - key
    - target_cs
    - target_ref
    produces:
    - address
    - result_status
    routing:
      SUCCESS: exit
      ALREADY_EXISTS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
        target_cs: target_cs
        target_ref: target_ref
      out:
        address: address
        result_status: result_status
  - cc_code: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    step: '1'
    step_name: claim_user_prompt
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: REGISTER
    store: USER_PROMPT_REGISTRY
    consumes:
    - key
    - target_cs
    - target_ref
    produces:
    - address
    - result_status
    routing:
      SUCCESS: exit
      ALREADY_EXISTS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
        target_cs: target_cs
        target_ref: target_ref
      out:
        address: address
        result_status: result_status
  - cc_code: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
    step: '1'
    step_name: confirm_reported_reading_fits
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - parameters
    - rules
    produces:
    - reading_fits
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: parameters
        rules: rules
      out:
        reading_fits: reading_fits
  - cc_code: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    step: '1'
    step_name: confirm_authorization
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - parameters
    - rules
    produces:
    - is_authorized
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: parameters
        rules: rules
      out:
        is_authorized: is_authorized
  - cc_code: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
    step: '1'
    step_name: confirm_same_model
    capability: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - value
    - allowed_set
    produces:
    - offer_for_model
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        value: value
        allowed_set: allowed_set
      out:
        offer_for_model: offer_for_model
  - cc_code: causal_language_model::CC_CONFIRM_READING_FITS_V0
    step: '1'
    step_name: assemble_reading
    capability: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - system_prompt
    - question
    - supporting_material
    - reading_capacity
    produces:
    - reading
    - reading_length
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        system_prompt: system_prompt
        question: question
        supporting_material: supporting_material
        reading_capacity: reading_capacity
      out:
        reading: reading
        reading_length: reading_length
  - cc_code: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    step: '1'
    step_name: confirm_acts_for_customer
    capability: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - value
    - allowed_set
    produces:
    - acts_for_customer
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        value: value
        allowed_set: allowed_set
      out:
        acts_for_customer: acts_for_customer
  - cc_code: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
    step: '1'
    step_name: confirm_releasable
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - parameters
    - rules
    produces:
    - releasable
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: parameters
        rules: rules
      out:
        releasable: releasable
  - cc_code: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    step: '1'
    step_name: read_time_in_service
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: READ
    store: TIMES_IN_SERVICE
    consumes:
    - key
    produces:
    - time_in_service
    - result_status
    routing:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
      out:
        time_in_service: time_in_service
        result_status: result_status
  - cc_code: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    step: '2'
    step_name: confirm_kind_declared
    capability: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - value
    - allowed_set
    produces:
    - kind_declared
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        value: value
        allowed_set: allowed_set
      out:
        kind_declared: kind_declared
  - cc_code: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    step: '3'
    step_name: compare_sensitivity
    capability: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - kind
    - ceiling
    - kinds
    produces:
    - within_ceiling
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        kind: kind
        ceiling: ceiling
        kinds: kinds
      out:
        within_ceiling: within_ceiling
  - cc_code: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    step: '1'
    step_name: form_rules_in_force
    capability: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - response_rules
    - account_numbers
    - seed
    produces:
    - rules_in_force
    - positions
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        response_rules: response_rules
        account_numbers: account_numbers
        seed: seed
      out:
        rules_in_force: rules_in_force
        positions: positions
  - cc_code: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    step: '2'
    step_name: assemble_opening_record
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - fields
    produces:
    - opening_record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: fields
      out:
        opening_record: opening_record
  - cc_code: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    step: '3'
    step_name: append_opening_record
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    kind: CS
    operation: APPEND
    store: USER_PROMPT_RECORDS
    consumes:
    - record
    - stream_id
    - actor_id
    produces:
    - record_id
    - sequence_number
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        record: record
        stream_id: stream_id
        actor_id: actor_id
      out:
        record_id: record_id
        sequence_number: sequence_number
  - cc_code: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: '1'
    step_name: read_model_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: READ
    store: MODELS
    consumes:
    - key
    produces:
    - model_record
    - result_status
    routing:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
      out:
        model_record: model_record
        result_status: result_status
  - cc_code: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: '2'
    step_name: require_registered
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - parameters
    - rules
    produces:
    - valid
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: parameters
        rules: rules
      out:
        valid: valid
  - cc_code: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: '3'
    step_name: confirm_ceiling_declared
    capability: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - value
    - allowed_set
    produces:
    - ceiling_declared
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        value: value
        allowed_set: allowed_set
      out:
        ceiling_declared: ceiling_declared
  - cc_code: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: '4'
    step_name: claim_time_in_service
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: REGISTER
    store: TIME_IN_SERVICE_REGISTRY
    consumes:
    - key
    - target_cs
    - target_ref
    produces:
    - address
    - result_status
    routing:
      SUCCESS: continue
      ALREADY_EXISTS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
        target_cs: target_cs
        target_ref: target_ref
      out:
        address: address
        result_status: result_status
  - cc_code: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: '5'
    step_name: mark_in_service
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: UPDATE_WHERE
    store: MODELS
    consumes:
    - filter
    - updates
    produces:
    - matched_keys
    - updated_count
    - result_status
    routing:
      SUCCESS: continue
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        filter: filter
        updates: updates
      out:
        matched_keys: matched_keys
        updated_count: updated_count
        result_status: result_status
  - cc_code: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: '6'
    step_name: require_transition
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - parameters
    - rules
    produces:
    - valid
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: parameters
        rules: rules
      out:
        valid: valid
  - cc_code: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: '7'
    step_name: assemble_time_in_service
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - fields
    produces:
    - time_in_service
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: fields
      out:
        time_in_service: time_in_service
  - cc_code: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: '8'
    step_name: write_time_in_service
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: WRITE
    store: TIMES_IN_SERVICE
    consumes:
    - key
    - value
    produces:
    - result_status
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
        value: value
      out:
        result_status: result_status
  - cc_code: causal_language_model::CC_READ_HOSTED_STATE_V0
    step: '1'
    step_name: read_trail
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    kind: CS
    operation: GET_ALL
    store: USER_PROMPT_RECORDS
    consumes:
    - stream_id
    produces:
    - entries
    - result_status
    routing:
      SUCCESS: continue
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        stream_id: stream_id
      out:
        entries: entries
        result_status: result_status
  - cc_code: causal_language_model::CC_READ_HOSTED_STATE_V0
    step: '2'
    step_name: reduce_trail
    capability: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - entries
    produces:
    - state
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        entries: entries
      out:
        state: state
  - cc_code: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    step: '1'
    step_name: assemble_step_record
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - fields
    produces:
    - step_record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: fields
      out:
        step_record: step_record
  - cc_code: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    step: '2'
    step_name: append_step_record
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    kind: CS
    operation: APPEND
    store: USER_PROMPT_RECORDS
    consumes:
    - record
    - stream_id
    - actor_id
    produces:
    - record_id
    - sequence_number
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        record: record
        stream_id: stream_id
        actor_id: actor_id
      out:
        record_id: record_id
        sequence_number: sequence_number
  - cc_code: causal_language_model::CC_RECORD_USER_PROMPT_V0
    step: '1'
    step_name: assemble_user_prompt_record
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - fields
    produces:
    - user_prompt_record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: fields
      out:
        user_prompt_record: user_prompt_record
  - cc_code: causal_language_model::CC_RECORD_USER_PROMPT_V0
    step: '2'
    step_name: append_user_prompt_record
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    kind: CS
    operation: APPEND
    store: USER_PROMPT_RECORDS
    consumes:
    - record
    - stream_id
    - actor_id
    produces:
    - record_id
    - sequence_number
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        record: record
        stream_id: stream_id
        actor_id: actor_id
      out:
        record_id: record_id
        sequence_number: sequence_number
  - cc_code: causal_language_model::CC_REGISTER_MODEL_V0
    step: '1'
    step_name: assemble_model_record
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - fields
    produces:
    - model_record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: fields
      out:
        model_record: model_record
  - cc_code: causal_language_model::CC_REGISTER_MODEL_V0
    step: '2'
    step_name: write_model_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: WRITE
    store: MODELS
    consumes:
    - key
    - value
    produces:
    - result_status
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
        value: value
      out:
        result_status: result_status
  - cc_code: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
    step: '1'
    step_name: read_user_prompt_entries
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    kind: CS
    operation: GET_ALL
    store: USER_PROMPT_RECORDS
    consumes:
    - stream_id
    produces:
    - entries
    - result_status
    routing:
      SUCCESS: continue
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        stream_id: stream_id
      out:
        entries: entries
        result_status: result_status
  - cc_code: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
    step: '2'
    step_name: select_user_prompt_record
    capability: capability_transforms::CT_PURE_FILTER_RECORDS_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - source
    - filter
    produces:
    - user_prompt_record
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        source: source
        filter: filter
      out:
        user_prompt_record: user_prompt_record
  - cc_code: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: '1'
    step_name: read_model_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: READ
    store: MODELS
    consumes:
    - key
    produces:
    - model_record
    - result_status
    routing:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
      out:
        model_record: model_record
        result_status: result_status
  - cc_code: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: '2'
    step_name: require_in_service
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - parameters
    - rules
    produces:
    - valid
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: parameters
        rules: rules
      out:
        valid: valid
  - cc_code: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: '3'
    step_name: mark_registered
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: UPDATE_WHERE
    store: MODELS
    consumes:
    - filter
    - updates
    produces:
    - matched_keys
    - updated_count
    - result_status
    routing:
      SUCCESS: continue
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        filter: filter
        updates: updates
      out:
        matched_keys: matched_keys
        updated_count: updated_count
        result_status: result_status
  - cc_code: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: '4'
    step_name: require_transition
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - parameters
    - rules
    produces:
    - valid
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: parameters
        rules: rules
      out:
        valid: valid
  - cc_code: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: '5'
    step_name: close_time_in_service
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: UPDATE
    store: TIMES_IN_SERVICE
    consumes:
    - key
    - updates
    produces:
    - result_status
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
        updates: updates
      out:
        result_status: result_status
  - cc_code: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    step: '1'
    step_name: form_rules_in_force
    capability: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - response_rules
    - account_numbers
    - seed
    produces:
    - rules_in_force
    - positions
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        response_rules: response_rules
        account_numbers: account_numbers
        seed: seed
      out:
        rules_in_force: rules_in_force
        positions: positions
  - cc_code: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    step: '2'
    step_name: write_response
    capability: causal_language_model::CT_WRITE_RESPONSE_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - reading
    - rules_in_force
    - positions
    produces:
    - written_response
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        reading: reading
        rules_in_force: rules_in_force
        positions: positions
      out:
        written_response: written_response
  step_bindings:
  - owner: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    step: read_model_record
    direction: INPUT
    field: key
    bound_to: inputs.identity_key
  - owner: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    step: read_model_record
    direction: OUTPUT
    field: model_record
    bound_to: capability_result.value
  - owner: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    step: read_model_record
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    step: require_in_service
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        state: $.results.read_model_record.model_record.state
  - owner: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    step: require_in_service
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: state
        op: eq
        value: IN_SERVICE
  - owner: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    step: require_in_service
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
  - owner: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    step: append_operation
    direction: INPUT
    field: record
    bound_to: inputs.record
  - owner: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    step: append_operation
    direction: INPUT
    field: stream_id
    bound_to:
      literal: MODEL_OPERATIONS
  - owner: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    step: append_operation
    direction: INPUT
    field: actor_id
    bound_to: inputs.staff_id
  - owner: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    step: append_operation
    direction: OUTPUT
    field: record_id
    bound_to: capability_result.record_id
  - owner: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    step: append_operation
    direction: OUTPUT
    field: sequence_number
    bound_to: capability_result.sequence_number
  - owner: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    step: choose_token
    direction: INPUT
    field: state
    bound_to: inputs.state
  - owner: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    step: choose_token
    direction: INPUT
    field: candidates
    bound_to: inputs.candidates
  - owner: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    step: choose_token
    direction: OUTPUT
    field: step
    bound_to: capability_result.step
  - owner: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    step: choose_token
    direction: OUTPUT
    field: text
    bound_to: capability_result.text
  - owner: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    step: choose_token
    direction: OUTPUT
    field: finished
    bound_to: capability_result.finished
  - owner: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    step: choose_token
    direction: OUTPUT
    field: stopped_by
    bound_to: capability_result.stopped_by
  - owner: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    step: choose_token
    direction: OUTPUT
    field: within_length
    bound_to: capability_result.within_length
  - owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: validate_description
    direction: INPUT
    field: record
    bound_to: inputs.description
  - owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: validate_description
    direction: INPUT
    field: schema
    bound_to: inputs.description_schema
  - owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: validate_description
    direction: OUTPUT
    field: violations
    bound_to: capability_result.violations
  - owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: require_description_complete
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        violations: $.results.validate_description.violations
  - owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: require_description_complete
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: violations
        op: eq
        value: []
  - owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: require_description_complete
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
  - owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: form_identity_key
    direction: INPUT
    field: description
    bound_to: inputs.description
  - owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: form_identity_key
    direction: INPUT
    field: fingerprint
    bound_to: inputs.fingerprint
  - owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: form_identity_key
    direction: OUTPUT
    field: identity_key
    bound_to: capability_result.identity_key
  - owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: claim_identity
    direction: INPUT
    field: key
    bound_to: results.form_identity_key.identity_key
  - owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: claim_identity
    direction: INPUT
    field: target_cs
    bound_to:
      literal: capability_side_effects::CS_MUTABLE_JSON_V0
  - owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: claim_identity
    direction: INPUT
    field: target_ref
    bound_to:
      literal: MODELS
  - owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: claim_identity
    direction: OUTPUT
    field: address
    bound_to: capability_result.address
  - owner: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    step: claim_identity
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    step: claim_user_prompt
    direction: INPUT
    field: key
    bound_to: inputs.user_prompt_id
  - owner: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    step: claim_user_prompt
    direction: INPUT
    field: target_cs
    bound_to:
      literal: capability_side_effects::CS_APPENDONLY_JSONL_V0
  - owner: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    step: claim_user_prompt
    direction: INPUT
    field: target_ref
    bound_to:
      literal: USER_PROMPT_RECORDS
  - owner: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    step: claim_user_prompt
    direction: OUTPUT
    field: address
    bound_to: capability_result.address
  - owner: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    step: claim_user_prompt
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
    step: confirm_reported_reading_fits
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        reported_reading_size: $.inputs.reported_reading_size
  - owner: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
    step: confirm_reported_reading_fits
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: reported_reading_size
        op: lte
        value: $.inputs.reading_capacity
  - owner: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
    step: confirm_reported_reading_fits
    direction: OUTPUT
    field: reading_fits
    bound_to: capability_result.valid
  - owner: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    step: confirm_authorization
    direction: INPUT
    field: parameters
    bound_to: inputs.staff_credentials
  - owner: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    step: confirm_authorization
    direction: INPUT
    field: rules
    bound_to: inputs.authorization_rules
  - owner: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    step: confirm_authorization
    direction: OUTPUT
    field: is_authorized
    bound_to: capability_result.valid
  - owner: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
    step: confirm_same_model
    direction: INPUT
    field: value
    bound_to: inputs.offered_fingerprint
  - owner: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
    step: confirm_same_model
    direction: INPUT
    field: allowed_set
    bound_to:
      literal:
      - $.inputs.admitted_fingerprint
  - owner: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
    step: confirm_same_model
    direction: OUTPUT
    field: offer_for_model
    bound_to: capability_result.is_member
  - owner: causal_language_model::CC_CONFIRM_READING_FITS_V0
    step: assemble_reading
    direction: INPUT
    field: system_prompt
    bound_to: inputs.system_prompt
  - owner: causal_language_model::CC_CONFIRM_READING_FITS_V0
    step: assemble_reading
    direction: INPUT
    field: question
    bound_to: inputs.question
  - owner: causal_language_model::CC_CONFIRM_READING_FITS_V0
    step: assemble_reading
    direction: INPUT
    field: supporting_material
    bound_to: inputs.supporting_material
  - owner: causal_language_model::CC_CONFIRM_READING_FITS_V0
    step: assemble_reading
    direction: INPUT
    field: reading_capacity
    bound_to: inputs.reading_capacity
  - owner: causal_language_model::CC_CONFIRM_READING_FITS_V0
    step: assemble_reading
    direction: OUTPUT
    field: reading
    bound_to: capability_result.reading
  - owner: causal_language_model::CC_CONFIRM_READING_FITS_V0
    step: assemble_reading
    direction: OUTPUT
    field: reading_length
    bound_to: capability_result.reading_length
  - owner: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    step: confirm_acts_for_customer
    direction: INPUT
    field: value
    bound_to: inputs.customer_id
  - owner: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    step: confirm_acts_for_customer
    direction: INPUT
    field: allowed_set
    bound_to: inputs.permitted_customers
  - owner: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    step: confirm_acts_for_customer
    direction: OUTPUT
    field: acts_for_customer
    bound_to: capability_result.is_member
  - owner: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
    step: confirm_releasable
    direction: INPUT
    field: parameters
    bound_to: inputs.release_facts
  - owner: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
    step: confirm_releasable
    direction: INPUT
    field: rules
    bound_to: inputs.release_rules
  - owner: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
    step: confirm_releasable
    direction: OUTPUT
    field: releasable
    bound_to: capability_result.valid
  - owner: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    step: read_time_in_service
    direction: INPUT
    field: key
    bound_to: inputs.time_in_service_id
  - owner: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    step: read_time_in_service
    direction: OUTPUT
    field: time_in_service
    bound_to: capability_result.value
  - owner: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    step: read_time_in_service
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    step: confirm_kind_declared
    direction: INPUT
    field: value
    bound_to: inputs.kind
  - owner: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    step: confirm_kind_declared
    direction: INPUT
    field: allowed_set
    bound_to:
      literal:
      - public
      - internal
      - confidential
      - restricted
  - owner: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    step: confirm_kind_declared
    direction: OUTPUT
    field: kind_declared
    bound_to: capability_result.is_member
  - owner: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    step: compare_sensitivity
    direction: INPUT
    field: kind
    bound_to: inputs.kind
  - owner: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    step: compare_sensitivity
    direction: INPUT
    field: ceiling
    bound_to: results.read_time_in_service.time_in_service.ceiling
  - owner: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    step: compare_sensitivity
    direction: INPUT
    field: kinds
    bound_to:
      literal:
      - public
      - internal
      - confidential
      - restricted
  - owner: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    step: compare_sensitivity
    direction: OUTPUT
    field: within_ceiling
    bound_to: capability_result.within_ceiling
  - owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    step: form_rules_in_force
    direction: INPUT
    field: response_rules
    bound_to: inputs.response_rules
  - owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    step: form_rules_in_force
    direction: INPUT
    field: account_numbers
    bound_to: inputs.account_numbers
  - owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    step: form_rules_in_force
    direction: INPUT
    field: seed
    bound_to: inputs.seed
  - owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    step: form_rules_in_force
    direction: OUTPUT
    field: rules_in_force
    bound_to: capability_result.rules_in_force
  - owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    step: form_rules_in_force
    direction: OUTPUT
    field: positions
    bound_to: capability_result.positions
  - owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    step: assemble_opening_record
    direction: INPUT
    field: fields
    bound_to:
      literal:
        user_prompt_id: $.inputs.user_prompt_id
        requester_id: $.inputs.requester_id
        customer_id: $.inputs.customer_id
        identity_key: $.inputs.identity_key
        kind: $.inputs.kind
        question: $.inputs.question
        supporting_material: $.inputs.supporting_material
        time_in_service_id: $.inputs.time_in_service_id
        reading: $.inputs.reading
        fingerprint: $.inputs.fingerprint
        reading_capacity: $.inputs.reading_capacity
        maximum_response_length: $.inputs.maximum_response_length
        rules_in_force: $.results.form_rules_in_force.rules_in_force
        ground_numbers: $.inputs.response_rules.ground_numbers
        longest_response: $.inputs.response_rules.longest_response
        outcome: WRITING
  - owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    step: assemble_opening_record
    direction: OUTPUT
    field: opening_record
    bound_to: capability_result.record
  - owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    step: append_opening_record
    direction: INPUT
    field: record
    bound_to: results.assemble_opening_record.opening_record
  - owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    step: append_opening_record
    direction: INPUT
    field: stream_id
    bound_to: inputs.user_prompt_id
  - owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    step: append_opening_record
    direction: INPUT
    field: actor_id
    bound_to: inputs.requester_id
  - owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    step: append_opening_record
    direction: OUTPUT
    field: record_id
    bound_to: capability_result.record_id
  - owner: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    step: append_opening_record
    direction: OUTPUT
    field: sequence_number
    bound_to: capability_result.sequence_number
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: read_model_record
    direction: INPUT
    field: key
    bound_to: inputs.identity_key
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: read_model_record
    direction: OUTPUT
    field: model_record
    bound_to: capability_result.value
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: read_model_record
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: require_registered
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        state: $.results.read_model_record.model_record.state
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: require_registered
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: state
        op: eq
        value: REGISTERED
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: require_registered
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: confirm_ceiling_declared
    direction: INPUT
    field: value
    bound_to: inputs.ceiling
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: confirm_ceiling_declared
    direction: INPUT
    field: allowed_set
    bound_to:
      literal:
      - public
      - internal
      - confidential
      - restricted
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: confirm_ceiling_declared
    direction: OUTPUT
    field: ceiling_declared
    bound_to: capability_result.is_member
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: claim_time_in_service
    direction: INPUT
    field: key
    bound_to: inputs.time_in_service_id
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: claim_time_in_service
    direction: INPUT
    field: target_cs
    bound_to:
      literal: capability_side_effects::CS_MUTABLE_JSON_V0
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: claim_time_in_service
    direction: INPUT
    field: target_ref
    bound_to:
      literal: TIMES_IN_SERVICE
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: claim_time_in_service
    direction: OUTPUT
    field: address
    bound_to: capability_result.address
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: claim_time_in_service
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: mark_in_service
    direction: INPUT
    field: filter
    bound_to:
      literal:
        identity_key: $.inputs.identity_key
        state: REGISTERED
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: mark_in_service
    direction: INPUT
    field: updates
    bound_to:
      literal:
        state: IN_SERVICE
        time_in_service_id: $.inputs.time_in_service_id
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: mark_in_service
    direction: OUTPUT
    field: matched_keys
    bound_to: capability_result.matched_keys
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: mark_in_service
    direction: OUTPUT
    field: updated_count
    bound_to: capability_result.updated_count
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: mark_in_service
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: require_transition
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        updated_count: $.results.mark_in_service.updated_count
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: require_transition
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: updated_count
        op: eq
        value: 1
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: require_transition
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: assemble_time_in_service
    direction: INPUT
    field: fields
    bound_to:
      literal:
        time_in_service_id: $.inputs.time_in_service_id
        identity_key: $.inputs.identity_key
        ceiling: $.inputs.ceiling
        system_prompt: $.inputs.system_prompt
        response_rules: $.inputs.response_rules
        state: OPEN
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: assemble_time_in_service
    direction: OUTPUT
    field: time_in_service
    bound_to: capability_result.record
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: write_time_in_service
    direction: INPUT
    field: key
    bound_to: inputs.time_in_service_id
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: write_time_in_service
    direction: INPUT
    field: value
    bound_to: results.assemble_time_in_service.time_in_service
  - owner: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    step: write_time_in_service
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: causal_language_model::CC_READ_HOSTED_STATE_V0
    step: read_trail
    direction: INPUT
    field: stream_id
    bound_to: inputs.user_prompt_id
  - owner: causal_language_model::CC_READ_HOSTED_STATE_V0
    step: read_trail
    direction: OUTPUT
    field: entries
    bound_to: capability_result.entries
  - owner: causal_language_model::CC_READ_HOSTED_STATE_V0
    step: read_trail
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: causal_language_model::CC_READ_HOSTED_STATE_V0
    step: reduce_trail
    direction: INPUT
    field: entries
    bound_to: results.read_trail.entries
  - owner: causal_language_model::CC_READ_HOSTED_STATE_V0
    step: reduce_trail
    direction: OUTPUT
    field: state
    bound_to: capability_result.state
  - owner: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    step: assemble_step_record
    direction: INPUT
    field: fields
    bound_to:
      literal:
        user_prompt_id: $.inputs.user_prompt_id
        outcome: STEP
        host_id: $.inputs.host_id
        fingerprint: $.inputs.fingerprint
        reported_reading_size: $.inputs.reported_reading_size
        position: $.inputs.step.position
        candidates: $.inputs.step.candidates
        chosen: $.inputs.step.chosen
        stopped: $.inputs.step.stopped
        stopped_by: $.inputs.step.stopped_by
        finished: $.inputs.step.finished
        within_length: $.inputs.step.within_length
  - owner: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    step: assemble_step_record
    direction: OUTPUT
    field: step_record
    bound_to: capability_result.record
  - owner: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    step: append_step_record
    direction: INPUT
    field: record
    bound_to: results.assemble_step_record.step_record
  - owner: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    step: append_step_record
    direction: INPUT
    field: stream_id
    bound_to: inputs.user_prompt_id
  - owner: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    step: append_step_record
    direction: INPUT
    field: actor_id
    bound_to: inputs.host_id
  - owner: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    step: append_step_record
    direction: OUTPUT
    field: record_id
    bound_to: capability_result.record_id
  - owner: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    step: append_step_record
    direction: OUTPUT
    field: sequence_number
    bound_to: capability_result.sequence_number
  - owner: causal_language_model::CC_RECORD_USER_PROMPT_V0
    step: assemble_user_prompt_record
    direction: INPUT
    field: fields
    bound_to:
      literal:
        user_prompt_id: $.inputs.user_prompt_id
        requester_id: $.inputs.requester_id
        customer_id: $.inputs.customer_id
        identity_key: $.inputs.identity_key
        kind: $.inputs.kind
        question: $.inputs.question
        supporting_material: $.inputs.supporting_material
        outcome: $.inputs.outcome
        time_in_service_id: $.inputs.time_in_service_id
        reading: $.inputs.reading
        rules_in_force: $.inputs.rules_in_force
        response: $.inputs.response
        reason: $.inputs.reason
  - owner: causal_language_model::CC_RECORD_USER_PROMPT_V0
    step: assemble_user_prompt_record
    direction: OUTPUT
    field: user_prompt_record
    bound_to: capability_result.record
  - owner: causal_language_model::CC_RECORD_USER_PROMPT_V0
    step: append_user_prompt_record
    direction: INPUT
    field: record
    bound_to: results.assemble_user_prompt_record.user_prompt_record
  - owner: causal_language_model::CC_RECORD_USER_PROMPT_V0
    step: append_user_prompt_record
    direction: INPUT
    field: stream_id
    bound_to: inputs.user_prompt_id
  - owner: causal_language_model::CC_RECORD_USER_PROMPT_V0
    step: append_user_prompt_record
    direction: INPUT
    field: actor_id
    bound_to: inputs.requester_id
  - owner: causal_language_model::CC_RECORD_USER_PROMPT_V0
    step: append_user_prompt_record
    direction: OUTPUT
    field: record_id
    bound_to: capability_result.record_id
  - owner: causal_language_model::CC_RECORD_USER_PROMPT_V0
    step: append_user_prompt_record
    direction: OUTPUT
    field: sequence_number
    bound_to: capability_result.sequence_number
  - owner: causal_language_model::CC_REGISTER_MODEL_V0
    step: assemble_model_record
    direction: INPUT
    field: fields
    bound_to:
      literal:
        identity_key: $.inputs.identity_key
        description: $.inputs.description
        fingerprint: $.inputs.fingerprint
        state: REGISTERED
        time_in_service_id: ''
  - owner: causal_language_model::CC_REGISTER_MODEL_V0
    step: assemble_model_record
    direction: OUTPUT
    field: model_record
    bound_to: capability_result.record
  - owner: causal_language_model::CC_REGISTER_MODEL_V0
    step: write_model_record
    direction: INPUT
    field: key
    bound_to: inputs.identity_key
  - owner: causal_language_model::CC_REGISTER_MODEL_V0
    step: write_model_record
    direction: INPUT
    field: value
    bound_to: results.assemble_model_record.model_record
  - owner: causal_language_model::CC_REGISTER_MODEL_V0
    step: write_model_record
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
    step: read_user_prompt_entries
    direction: INPUT
    field: stream_id
    bound_to: inputs.user_prompt_id
  - owner: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
    step: read_user_prompt_entries
    direction: OUTPUT
    field: entries
    bound_to: capability_result.entries
  - owner: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
    step: read_user_prompt_entries
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
    step: select_user_prompt_record
    direction: INPUT
    field: source
    bound_to: results.read_user_prompt_entries.entries
  - owner: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
    step: select_user_prompt_record
    direction: INPUT
    field: filter
    bound_to:
      literal:
        stream_id: $.inputs.user_prompt_id
  - owner: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
    step: select_user_prompt_record
    direction: OUTPUT
    field: user_prompt_record
    bound_to: capability_result.extracted
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: read_model_record
    direction: INPUT
    field: key
    bound_to: inputs.identity_key
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: read_model_record
    direction: OUTPUT
    field: model_record
    bound_to: capability_result.value
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: read_model_record
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: require_in_service
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        state: $.results.read_model_record.model_record.state
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: require_in_service
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: state
        op: eq
        value: IN_SERVICE
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: require_in_service
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: mark_registered
    direction: INPUT
    field: filter
    bound_to:
      literal:
        identity_key: $.inputs.identity_key
        state: IN_SERVICE
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: mark_registered
    direction: INPUT
    field: updates
    bound_to:
      literal:
        state: REGISTERED
        time_in_service_id: ''
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: mark_registered
    direction: OUTPUT
    field: matched_keys
    bound_to: capability_result.matched_keys
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: mark_registered
    direction: OUTPUT
    field: updated_count
    bound_to: capability_result.updated_count
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: mark_registered
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: require_transition
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        updated_count: $.results.mark_registered.updated_count
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: require_transition
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: updated_count
        op: eq
        value: 1
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: require_transition
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: close_time_in_service
    direction: INPUT
    field: key
    bound_to: results.read_model_record.model_record.time_in_service_id
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: close_time_in_service
    direction: INPUT
    field: updates
    bound_to:
      literal:
        state: CLOSED
  - owner: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: close_time_in_service
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    step: form_rules_in_force
    direction: INPUT
    field: response_rules
    bound_to: inputs.response_rules
  - owner: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    step: form_rules_in_force
    direction: INPUT
    field: account_numbers
    bound_to: inputs.account_numbers
  - owner: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    step: form_rules_in_force
    direction: INPUT
    field: seed
    bound_to: inputs.seed
  - owner: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    step: form_rules_in_force
    direction: OUTPUT
    field: rules_in_force
    bound_to: capability_result.rules_in_force
  - owner: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    step: form_rules_in_force
    direction: OUTPUT
    field: positions
    bound_to: capability_result.positions
  - owner: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    step: write_response
    direction: INPUT
    field: reading
    bound_to: inputs.reading
  - owner: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    step: write_response
    direction: INPUT
    field: rules_in_force
    bound_to: results.form_rules_in_force.rules_in_force
  - owner: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    step: write_response
    direction: INPUT
    field: positions
    bound_to: results.form_rules_in_force.positions
  - owner: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    step: write_response
    direction: OUTPUT
    field: written_response
    bound_to: capability_result.result
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: CC_CLAIM_USER_PROMPT_IDENTITY_V0
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    direction: INPUT
    field: permitted_customers
    bound_to: payload.permitted_customers
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: CC_ADMIT_USER_PROMPT_V0
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: CC_CONFIRM_WITHIN_CEILING_V0
    direction: INPUT
    field: time_in_service_id
    bound_to: results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: CC_CONFIRM_WITHIN_CEILING_V0
    direction: INPUT
    field: kind
    bound_to: payload.kind
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: CC_CONFIRM_READING_FITS_V0
    direction: INPUT
    field: system_prompt
    bound_to: results.CC_CONFIRM_WITHIN_CEILING_V0.time_in_service.system_prompt
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: CC_CONFIRM_READING_FITS_V0
    direction: INPUT
    field: question
    bound_to: payload.question
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: CC_CONFIRM_READING_FITS_V0
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: CC_CONFIRM_READING_FITS_V0
    direction: INPUT
    field: reading_capacity
    bound_to: results.CC_ADMIT_USER_PROMPT_V0.model_record.description.reading_capacity
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: requester_id
    bound_to: payload.requester_id
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: kind
    bound_to: payload.kind
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: question
    bound_to: payload.question
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: account_numbers
    bound_to: payload.account_numbers
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: seed
    bound_to: payload.seed
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: time_in_service_id
    bound_to: results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: reading
    bound_to: results.CC_CONFIRM_READING_FITS_V0.reading
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: response_rules
    bound_to: results.CC_CONFIRM_WITHIN_CEILING_V0.time_in_service.response_rules
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: fingerprint
    bound_to: results.CC_ADMIT_USER_PROMPT_V0.model_record.fingerprint
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: reading_capacity
    bound_to: results.CC_ADMIT_USER_PROMPT_V0.model_record.description.reading_capacity
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: maximum_response_length
    bound_to: results.CC_ADMIT_USER_PROMPT_V0.model_record.description.maximum_response_length
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: requester_id
    bound_to: payload.requester_id
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: kind
    bound_to: payload.kind
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: question
    bound_to: payload.question
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: outcome
    bound_to:
      literal: REFUSED
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: reason
    bound_to:
      literal: requester_not_permitted_for_customer
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: requester_id
    bound_to: payload.requester_id
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: kind
    bound_to: payload.kind
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: question
    bound_to: payload.question
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: outcome
    bound_to:
      literal: REFUSED
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: reason
    bound_to:
      literal: model_not_registered
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: requester_id
    bound_to: payload.requester_id
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: kind
    bound_to: payload.kind
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: question
    bound_to: payload.question
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: outcome
    bound_to:
      literal: REFUSED
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: reason
    bound_to:
      literal: model_not_in_service
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: requester_id
    bound_to: payload.requester_id
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: kind
    bound_to: payload.kind
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: question
    bound_to: payload.question
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: time_in_service_id
    bound_to: results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: outcome
    bound_to:
      literal: REFUSED
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: reason
    bound_to:
      literal: kind_above_sensitivity_ceiling
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: requester_id
    bound_to: payload.requester_id
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: kind
    bound_to: payload.kind
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: question
    bound_to: payload.question
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: time_in_service_id
    bound_to: results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: outcome
    bound_to:
      literal: REFUSED
  - owner: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: reason
    bound_to:
      literal: reading_longer_than_model_can_read
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: CC_READ_HOSTED_STATE_V0
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: CC_CONFIRM_OFFER_FOR_MODEL_V0
    direction: INPUT
    field: offered_fingerprint
    bound_to: payload.fingerprint
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: CC_CONFIRM_OFFER_FOR_MODEL_V0
    direction: INPUT
    field: admitted_fingerprint
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.fingerprint
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: CC_CONFIRM_HOSTED_READING_FITS_V0
    direction: INPUT
    field: reported_reading_size
    bound_to: payload.reported_reading_size
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: CC_CONFIRM_HOSTED_READING_FITS_V0
    direction: INPUT
    field: reading_capacity
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.reading_capacity
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: CC_CHOOSE_PERMITTED_TOKEN_V0
    direction: INPUT
    field: state
    bound_to: results.CC_READ_HOSTED_STATE_V0.state
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: CC_CHOOSE_PERMITTED_TOKEN_V0
    direction: INPUT
    field: candidates
    bound_to: payload.candidates
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: CONFIRM_NO_RULE_STOPPED
    direction: INPUT
    field: release_facts
    bound_to:
      literal:
        stopped_by: $.results.CC_CHOOSE_PERMITTED_TOKEN_V0.stopped_by
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: CONFIRM_NO_RULE_STOPPED
    direction: INPUT
    field: release_rules
    bound_to:
      literal:
      - field: stopped_by
        op: eq
        value: none
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: CONFIRM_WITHIN_LENGTH
    direction: INPUT
    field: release_facts
    bound_to:
      literal:
        within_length: $.results.CC_CHOOSE_PERMITTED_TOKEN_V0.within_length
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: CONFIRM_WITHIN_LENGTH
    direction: INPUT
    field: release_rules
    bound_to:
      literal:
      - field: within_length
        op: eq
        value: true
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_STEP
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_STEP
    direction: INPUT
    field: host_id
    bound_to: payload.host_id
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_STEP
    direction: INPUT
    field: fingerprint
    bound_to: payload.fingerprint
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_STEP
    direction: INPUT
    field: reported_reading_size
    bound_to: payload.reported_reading_size
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_STEP
    direction: INPUT
    field: step
    bound_to: results.CC_CHOOSE_PERMITTED_TOKEN_V0.step
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_STOPPED_STEP
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_STOPPED_STEP
    direction: INPUT
    field: host_id
    bound_to: payload.host_id
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_STOPPED_STEP
    direction: INPUT
    field: fingerprint
    bound_to: payload.fingerprint
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_STOPPED_STEP
    direction: INPUT
    field: reported_reading_size
    bound_to: payload.reported_reading_size
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_STOPPED_STEP
    direction: INPUT
    field: step
    bound_to: results.CC_CHOOSE_PERMITTED_TOKEN_V0.step
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_UNFINISHED_STEP
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_UNFINISHED_STEP
    direction: INPUT
    field: host_id
    bound_to: payload.host_id
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_UNFINISHED_STEP
    direction: INPUT
    field: fingerprint
    bound_to: payload.fingerprint
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_UNFINISHED_STEP
    direction: INPUT
    field: reported_reading_size
    bound_to: payload.reported_reading_size
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_UNFINISHED_STEP
    direction: INPUT
    field: step
    bound_to: results.CC_CHOOSE_PERMITTED_TOKEN_V0.step
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_OTHER_MODEL
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_OTHER_MODEL
    direction: INPUT
    field: requester_id
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.requester_id
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_OTHER_MODEL
    direction: INPUT
    field: customer_id
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.customer_id
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_OTHER_MODEL
    direction: INPUT
    field: identity_key
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.identity_key
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_OTHER_MODEL
    direction: INPUT
    field: kind
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.kind
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_OTHER_MODEL
    direction: INPUT
    field: question
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.question
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_OTHER_MODEL
    direction: INPUT
    field: supporting_material
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.supporting_material
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_OTHER_MODEL
    direction: INPUT
    field: time_in_service_id
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.time_in_service_id
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_OTHER_MODEL
    direction: INPUT
    field: reading
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.reading
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_OTHER_MODEL
    direction: INPUT
    field: rules_in_force
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.rules_in_force
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_OTHER_MODEL
    direction: INPUT
    field: outcome
    bound_to:
      literal: REFUSED
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_OTHER_MODEL
    direction: INPUT
    field: reason
    bound_to:
      literal: offer_for_another_model
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: requester_id
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.requester_id
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: customer_id
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.customer_id
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: identity_key
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.identity_key
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: kind
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.kind
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: question
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.question
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: supporting_material
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.supporting_material
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: time_in_service_id
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.time_in_service_id
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: reading
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.reading
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: rules_in_force
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.rules_in_force
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: outcome
    bound_to:
      literal: REFUSED
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: reason
    bound_to:
      literal: reading_longer_than_model_can_read
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: requester_id
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.requester_id
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: customer_id
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.customer_id
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: identity_key
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.identity_key
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: kind
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.kind
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: question
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.question
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: supporting_material
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.supporting_material
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: time_in_service_id
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.time_in_service_id
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: reading
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.reading
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: rules_in_force
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.rules_in_force
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: outcome
    bound_to:
      literal: REFUSED
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: reason
    bound_to: results.CC_CHOOSE_PERMITTED_TOKEN_V0.stopped_by
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: requester_id
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.requester_id
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: customer_id
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.customer_id
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: identity_key
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.identity_key
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: kind
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.kind
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: question
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.question
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: supporting_material
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.supporting_material
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: time_in_service_id
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.time_in_service_id
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: reading
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.reading
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: rules_in_force
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.rules_in_force
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: outcome
    bound_to:
      literal: REFUSED
  - owner: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: reason
    bound_to:
      literal: longest_response_reached
  - owner: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    step: CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
  - owner: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    step: CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: authorization_rules
    bound_to:
      literal:
      - field: role
        op: eq
        value: model_staff
  - owner: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    step: CC_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
  - owner: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    step: CC_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: time_in_service_id
    bound_to: payload.time_in_service_id
  - owner: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    step: CC_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: ceiling
    bound_to: payload.ceiling
  - owner: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    step: CC_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: system_prompt
    bound_to: payload.system_prompt
  - owner: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    step: CC_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: response_rules
    bound_to: payload.response_rules
  - owner: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    step: CC_APPEND_MODEL_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
  - owner: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    step: CC_APPEND_MODEL_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: PLACE_MODEL_IN_SERVICE
  - owner: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    step: CC_APPEND_MODEL_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: PLACE_MODEL_IN_SERVICE
        staff_id: $.payload.staff_id
        subject: $.payload.identity_key
  - owner: causal_language_model::WF_REGISTER_MODEL_V0
    step: CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
  - owner: causal_language_model::WF_REGISTER_MODEL_V0
    step: CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: authorization_rules
    bound_to:
      literal:
      - field: role
        op: eq
        value: model_staff
  - owner: causal_language_model::WF_REGISTER_MODEL_V0
    step: CC_CLAIM_MODEL_IDENTITY_V0
    direction: INPUT
    field: description
    bound_to: payload.description
  - owner: causal_language_model::WF_REGISTER_MODEL_V0
    step: CC_CLAIM_MODEL_IDENTITY_V0
    direction: INPUT
    field: fingerprint
    bound_to: payload.fingerprint
  - owner: causal_language_model::WF_REGISTER_MODEL_V0
    step: CC_CLAIM_MODEL_IDENTITY_V0
    direction: INPUT
    field: description_schema
    bound_to:
      literal:
        reading_capacity:
          type: integer
          required: true
  - owner: causal_language_model::WF_REGISTER_MODEL_V0
    step: CC_REGISTER_MODEL_V0
    direction: INPUT
    field: identity_key
    bound_to: results.CC_CLAIM_MODEL_IDENTITY_V0.identity_key
  - owner: causal_language_model::WF_REGISTER_MODEL_V0
    step: CC_REGISTER_MODEL_V0
    direction: INPUT
    field: description
    bound_to: payload.description
  - owner: causal_language_model::WF_REGISTER_MODEL_V0
    step: CC_REGISTER_MODEL_V0
    direction: INPUT
    field: fingerprint
    bound_to: payload.fingerprint
  - owner: causal_language_model::WF_REGISTER_MODEL_V0
    step: CC_APPEND_MODEL_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
  - owner: causal_language_model::WF_REGISTER_MODEL_V0
    step: CC_APPEND_MODEL_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: REGISTER_MODEL
  - owner: causal_language_model::WF_REGISTER_MODEL_V0
    step: CC_APPEND_MODEL_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: REGISTER_MODEL
        staff_id: $.payload.staff_id
        subject: $.results.CC_CLAIM_MODEL_IDENTITY_V0.identity_key
  - owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    step: CC_READ_HOSTED_STATE_V0
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
  - owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    step: CONFIRM_FINISHED
    direction: INPUT
    field: release_facts
    bound_to:
      literal:
        finished: $.results.CC_READ_HOSTED_STATE_V0.state.finished
  - owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    step: CONFIRM_FINISHED
    direction: INPUT
    field: release_rules
    bound_to:
      literal:
      - field: finished
        op: eq
        value: true
  - owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
  - owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: requester_id
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.requester_id
  - owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: customer_id
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.customer_id
  - owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: identity_key
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.identity_key
  - owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: kind
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.kind
  - owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: question
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.question
  - owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: supporting_material
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.supporting_material
  - owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: time_in_service_id
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.time_in_service_id
  - owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: reading
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.reading
  - owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: rules_in_force
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.opening.rules_in_force
  - owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: outcome
    bound_to:
      literal: RESPONDED
  - owner: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: response
    bound_to: results.CC_READ_HOSTED_STATE_V0.state.text
  - owner: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    step: CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
  - owner: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    step: CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: authorization_rules
    bound_to:
      literal:
      - field: role
        op: eq
        value: model_staff
  - owner: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    step: CC_APPEND_MODEL_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
  - owner: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    step: CC_APPEND_MODEL_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: RETRIEVE_USER_PROMPT_RECORD
  - owner: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    step: CC_APPEND_MODEL_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: RETRIEVE_USER_PROMPT_RECORD
        staff_id: $.payload.staff_id
        subject: $.payload.user_prompt_id
  - owner: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    step: CC_RETRIEVE_USER_PROMPT_RECORD_V0
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: CC_CLAIM_USER_PROMPT_IDENTITY_V0
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    direction: INPUT
    field: permitted_customers
    bound_to: payload.permitted_customers
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: CC_ADMIT_USER_PROMPT_V0
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: CC_CONFIRM_WITHIN_CEILING_V0
    direction: INPUT
    field: time_in_service_id
    bound_to: results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: CC_CONFIRM_WITHIN_CEILING_V0
    direction: INPUT
    field: kind
    bound_to: payload.kind
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: CC_CONFIRM_READING_FITS_V0
    direction: INPUT
    field: system_prompt
    bound_to: results.CC_CONFIRM_WITHIN_CEILING_V0.time_in_service.system_prompt
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: CC_CONFIRM_READING_FITS_V0
    direction: INPUT
    field: question
    bound_to: payload.question
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: CC_CONFIRM_READING_FITS_V0
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: CC_CONFIRM_READING_FITS_V0
    direction: INPUT
    field: reading_capacity
    bound_to: results.CC_ADMIT_USER_PROMPT_V0.model_record.description.reading_capacity
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: CC_WRITE_MODEL_RESPONSE_V0
    direction: INPUT
    field: response_rules
    bound_to: results.CC_CONFIRM_WITHIN_CEILING_V0.time_in_service.response_rules
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: CC_WRITE_MODEL_RESPONSE_V0
    direction: INPUT
    field: account_numbers
    bound_to: payload.account_numbers
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: CC_WRITE_MODEL_RESPONSE_V0
    direction: INPUT
    field: seed
    bound_to: payload.seed
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: CC_WRITE_MODEL_RESPONSE_V0
    direction: INPUT
    field: reading
    bound_to: results.CC_CONFIRM_READING_FITS_V0.reading
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: CONFIRM_NO_RULE_STOPPED
    direction: INPUT
    field: release_facts
    bound_to:
      literal:
        stopped_by: $.results.CC_WRITE_MODEL_RESPONSE_V0.written_response.stopped_by
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: CONFIRM_NO_RULE_STOPPED
    direction: INPUT
    field: release_rules
    bound_to:
      literal:
      - field: stopped_by
        op: eq
        value: none
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: CONFIRM_FINISHED
    direction: INPUT
    field: release_facts
    bound_to:
      literal:
        finished: $.results.CC_WRITE_MODEL_RESPONSE_V0.written_response.finished
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: CONFIRM_FINISHED
    direction: INPUT
    field: release_rules
    bound_to:
      literal:
      - field: finished
        op: eq
        value: true
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: requester_id
    bound_to: payload.requester_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: kind
    bound_to: payload.kind
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: question
    bound_to: payload.question
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: time_in_service_id
    bound_to: results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: reading
    bound_to: results.CC_CONFIRM_READING_FITS_V0.reading
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: rules_in_force
    bound_to: results.CC_WRITE_MODEL_RESPONSE_V0.rules_in_force
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: response
    bound_to: results.CC_WRITE_MODEL_RESPONSE_V0.written_response.text
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_RESPONDED
    direction: INPUT
    field: outcome
    bound_to:
      literal: RESPONDED
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: requester_id
    bound_to: payload.requester_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: kind
    bound_to: payload.kind
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: question
    bound_to: payload.question
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: outcome
    bound_to:
      literal: REFUSED
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_PERMITTED
    direction: INPUT
    field: reason
    bound_to:
      literal: requester_not_permitted_for_customer
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: requester_id
    bound_to: payload.requester_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: kind
    bound_to: payload.kind
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: question
    bound_to: payload.question
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: outcome
    bound_to:
      literal: REFUSED
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_REGISTERED
    direction: INPUT
    field: reason
    bound_to:
      literal: model_not_registered
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: requester_id
    bound_to: payload.requester_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: kind
    bound_to: payload.kind
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: question
    bound_to: payload.question
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: outcome
    bound_to:
      literal: REFUSED
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_NOT_IN_SERVICE
    direction: INPUT
    field: reason
    bound_to:
      literal: model_not_in_service
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: requester_id
    bound_to: payload.requester_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: kind
    bound_to: payload.kind
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: question
    bound_to: payload.question
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: time_in_service_id
    bound_to: results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: outcome
    bound_to:
      literal: REFUSED
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_ABOVE_CEILING
    direction: INPUT
    field: reason
    bound_to:
      literal: kind_above_sensitivity_ceiling
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: requester_id
    bound_to: payload.requester_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: kind
    bound_to: payload.kind
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: question
    bound_to: payload.question
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: time_in_service_id
    bound_to: results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: outcome
    bound_to:
      literal: REFUSED
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_TOO_LONG_TO_READ
    direction: INPUT
    field: reason
    bound_to:
      literal: reading_longer_than_model_can_read
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: requester_id
    bound_to: payload.requester_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: kind
    bound_to: payload.kind
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: question
    bound_to: payload.question
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: time_in_service_id
    bound_to: results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: reading
    bound_to: results.CC_CONFIRM_READING_FITS_V0.reading
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: rules_in_force
    bound_to: results.CC_WRITE_MODEL_RESPONSE_V0.rules_in_force
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: outcome
    bound_to:
      literal: REFUSED
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_BY_RULE
    direction: INPUT
    field: reason
    bound_to: results.CC_WRITE_MODEL_RESPONSE_V0.written_response.stopped_by
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: requester_id
    bound_to: payload.requester_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: kind
    bound_to: payload.kind
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: question
    bound_to: payload.question
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: time_in_service_id
    bound_to: results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: reading
    bound_to: results.CC_CONFIRM_READING_FITS_V0.reading
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: rules_in_force
    bound_to: results.CC_WRITE_MODEL_RESPONSE_V0.rules_in_force
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: outcome
    bound_to:
      literal: REFUSED
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_REFUSED_UNFINISHED
    direction: INPUT
    field: reason
    bound_to:
      literal: longest_response_reached
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_BEFORE_READING
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_BEFORE_READING
    direction: INPUT
    field: requester_id
    bound_to: payload.requester_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_BEFORE_READING
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_BEFORE_READING
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_BEFORE_READING
    direction: INPUT
    field: kind
    bound_to: payload.kind
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_BEFORE_READING
    direction: INPUT
    field: question
    bound_to: payload.question
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_BEFORE_READING
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_BEFORE_READING
    direction: INPUT
    field: outcome
    bound_to:
      literal: FAILED
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_BEFORE_READING
    direction: INPUT
    field: reason
    bound_to:
      literal: store_failed_before_the_model_read
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_WHILE_WRITING
    direction: INPUT
    field: user_prompt_id
    bound_to: payload.user_prompt_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_WHILE_WRITING
    direction: INPUT
    field: requester_id
    bound_to: payload.requester_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_WHILE_WRITING
    direction: INPUT
    field: customer_id
    bound_to: payload.customer_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_WHILE_WRITING
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_WHILE_WRITING
    direction: INPUT
    field: kind
    bound_to: payload.kind
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_WHILE_WRITING
    direction: INPUT
    field: question
    bound_to: payload.question
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_WHILE_WRITING
    direction: INPUT
    field: supporting_material
    bound_to: payload.supporting_material
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_WHILE_WRITING
    direction: INPUT
    field: time_in_service_id
    bound_to: results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_WHILE_WRITING
    direction: INPUT
    field: reading
    bound_to: results.CC_CONFIRM_READING_FITS_V0.reading
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_WHILE_WRITING
    direction: INPUT
    field: outcome
    bound_to:
      literal: FAILED
  - owner: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    step: RECORD_FAILED_WHILE_WRITING
    direction: INPUT
    field: reason
    bound_to:
      literal: writing_failed
  - owner: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
  - owner: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: authorization_rules
    bound_to:
      literal:
      - field: role
        op: eq
        value: model_staff
  - owner: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
  - owner: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: CC_APPEND_MODEL_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
  - owner: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: CC_APPEND_MODEL_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: WITHDRAW_MODEL_FROM_SERVICE
  - owner: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    step: CC_APPEND_MODEL_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: WITHDRAW_MODEL_FROM_SERVICE
        staff_id: $.payload.staff_id
        subject: $.payload.identity_key
  interface_fields:
  - artifact: causal_language_model::AC_MODEL_HOST_V0
    direction: ATTRIBUTE
    field: host_id
    type: string
    required: 'YES'
    default: null
    meaning: host id
  - artifact: causal_language_model::AC_MODEL_STAFF_V0
    direction: ATTRIBUTE
    field: staff_id
    type: string
    required: 'YES'
    default: null
    meaning: staff id
  - artifact: causal_language_model::AC_MODEL_STAFF_V0
    direction: ATTRIBUTE
    field: authorized
    type: boolean
    required: 'NO'
    default: false
    meaning: authorized
  - artifact: causal_language_model::AC_REQUESTER_V0
    direction: ATTRIBUTE
    field: requester_id
    type: string
    required: 'YES'
    default: null
    meaning: requester id
  - artifact: causal_language_model::AC_REQUESTER_V0
    direction: ATTRIBUTE
    field: permitted_customers
    type: array
    required: 'NO'
    default: '[]'
    meaning: permitted customers
  - artifact: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    direction: OUTPUT
    field: model_record
    type: object
    required: 'YES'
    default: null
    meaning: model record
  - artifact: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    direction: INPUT
    field: record
    type: object
    required: 'YES'
    default: null
    meaning: record
  - artifact: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: null
    meaning: staff id
  - artifact: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    direction: INPUT
    field: operation
    type: string
    required: 'YES'
    default: null
    meaning: operation
  - artifact: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    direction: OUTPUT
    field: record_id
    type: string
    required: 'YES'
    default: null
    meaning: record id
  - artifact: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    direction: OUTPUT
    field: sequence_number
    type: integer
    required: 'YES'
    default: null
    meaning: sequence number
  - artifact: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    direction: INPUT
    field: state
    type: object
    required: 'YES'
    default: null
    meaning: state
  - artifact: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    direction: INPUT
    field: candidates
    type: array
    required: 'YES'
    default: null
    meaning: candidates
  - artifact: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    direction: OUTPUT
    field: step
    type: object
    required: 'YES'
    default: null
    meaning: step
  - artifact: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    direction: OUTPUT
    field: text
    type: string
    required: 'YES'
    default: null
    meaning: text
  - artifact: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    direction: OUTPUT
    field: finished
    type: boolean
    required: 'YES'
    default: null
    meaning: finished
  - artifact: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    direction: OUTPUT
    field: stopped_by
    type: string
    required: 'YES'
    default: null
    meaning: stopped by
  - artifact: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    direction: OUTPUT
    field: within_length
    type: boolean
    required: 'YES'
    default: null
    meaning: within length
  - artifact: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    direction: INPUT
    field: description
    type: object
    required: 'YES'
    default: null
    meaning: description
  - artifact: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    direction: INPUT
    field: description_schema
    type: object
    required: 'YES'
    default: null
    meaning: description schema
  - artifact: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    direction: INPUT
    field: fingerprint
    type: string
    required: 'YES'
    default: null
    meaning: fingerprint
  - artifact: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    direction: OUTPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    direction: OUTPUT
    field: address
    type: string
    required: 'YES'
    default: null
    meaning: address
  - artifact: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    direction: INPUT
    field: user_prompt_id
    type: string
    required: 'YES'
    default: null
    meaning: user prompt id
  - artifact: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    direction: OUTPUT
    field: address
    type: string
    required: 'YES'
    default: null
    meaning: address
  - artifact: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
    direction: INPUT
    field: reported_reading_size
    type: integer
    required: 'YES'
    default: null
    meaning: reported reading size
  - artifact: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
    direction: INPUT
    field: reading_capacity
    type: integer
    required: 'YES'
    default: null
    meaning: reading capacity
  - artifact: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
    direction: OUTPUT
    field: reading_fits
    type: boolean
    required: 'YES'
    default: null
    meaning: reading fits
  - artifact: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: null
    meaning: staff credentials
  - artifact: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: authorization_rules
    type: array
    required: 'YES'
    default: null
    meaning: authorization rules
  - artifact: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    direction: OUTPUT
    field: is_authorized
    type: boolean
    required: 'YES'
    default: null
    meaning: is authorized
  - artifact: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
    direction: INPUT
    field: offered_fingerprint
    type: string
    required: 'YES'
    default: null
    meaning: offered fingerprint
  - artifact: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
    direction: INPUT
    field: admitted_fingerprint
    type: string
    required: 'YES'
    default: null
    meaning: admitted fingerprint
  - artifact: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
    direction: OUTPUT
    field: offer_for_model
    type: boolean
    required: 'YES'
    default: null
    meaning: offer for model
  - artifact: causal_language_model::CC_CONFIRM_READING_FITS_V0
    direction: INPUT
    field: system_prompt
    type: string
    required: 'YES'
    default: null
    meaning: system prompt
  - artifact: causal_language_model::CC_CONFIRM_READING_FITS_V0
    direction: INPUT
    field: question
    type: string
    required: 'YES'
    default: null
    meaning: question
  - artifact: causal_language_model::CC_CONFIRM_READING_FITS_V0
    direction: INPUT
    field: supporting_material
    type: string
    required: 'YES'
    default: null
    meaning: supporting material
  - artifact: causal_language_model::CC_CONFIRM_READING_FITS_V0
    direction: INPUT
    field: reading_capacity
    type: integer
    required: 'YES'
    default: null
    meaning: reading capacity
  - artifact: causal_language_model::CC_CONFIRM_READING_FITS_V0
    direction: OUTPUT
    field: reading
    type: object
    required: 'YES'
    default: null
    meaning: reading
  - artifact: causal_language_model::CC_CONFIRM_READING_FITS_V0
    direction: OUTPUT
    field: reading_length
    type: integer
    required: 'YES'
    default: null
    meaning: reading length
  - artifact: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    direction: INPUT
    field: customer_id
    type: string
    required: 'YES'
    default: null
    meaning: customer id
  - artifact: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    direction: INPUT
    field: permitted_customers
    type: array
    required: 'YES'
    default: null
    meaning: permitted customers
  - artifact: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    direction: OUTPUT
    field: acts_for_customer
    type: boolean
    required: 'YES'
    default: null
    meaning: acts for customer
  - artifact: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
    direction: INPUT
    field: release_facts
    type: object
    required: 'YES'
    default: null
    meaning: release facts
  - artifact: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
    direction: INPUT
    field: release_rules
    type: array
    required: 'YES'
    default: null
    meaning: release rules
  - artifact: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
    direction: OUTPUT
    field: releasable
    type: boolean
    required: 'YES'
    default: null
    meaning: releasable
  - artifact: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    direction: INPUT
    field: time_in_service_id
    type: string
    required: 'YES'
    default: null
    meaning: time in service id
  - artifact: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    direction: INPUT
    field: kind
    type: string
    required: 'YES'
    default: null
    meaning: kind
  - artifact: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    direction: OUTPUT
    field: time_in_service
    type: object
    required: 'YES'
    default: null
    meaning: time in service
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: user_prompt_id
    type: string
    required: 'YES'
    default: null
    meaning: user prompt id
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: requester_id
    type: string
    required: 'YES'
    default: null
    meaning: requester id
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: customer_id
    type: string
    required: 'YES'
    default: null
    meaning: customer id
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: kind
    type: string
    required: 'YES'
    default: null
    meaning: kind
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: question
    type: string
    required: 'YES'
    default: null
    meaning: question
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: supporting_material
    type: string
    required: 'YES'
    default: null
    meaning: supporting material
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: time_in_service_id
    type: string
    required: 'YES'
    default: null
    meaning: time in service id
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: reading
    type: object
    required: 'YES'
    default: null
    meaning: reading
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: response_rules
    type: object
    required: 'YES'
    default: null
    meaning: response rules
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: account_numbers
    type: array
    required: 'YES'
    default: null
    meaning: account numbers
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: seed
    type: integer
    required: 'YES'
    default: null
    meaning: seed
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: fingerprint
    type: string
    required: 'YES'
    default: null
    meaning: fingerprint
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: reading_capacity
    type: integer
    required: 'YES'
    default: null
    meaning: reading capacity
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: INPUT
    field: maximum_response_length
    type: integer
    required: 'YES'
    default: null
    meaning: maximum response length
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: OUTPUT
    field: rules_in_force
    type: object
    required: 'YES'
    default: null
    meaning: rules in force
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: OUTPUT
    field: positions
    type: array
    required: 'YES'
    default: null
    meaning: positions
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: OUTPUT
    field: opening_record
    type: object
    required: 'YES'
    default: null
    meaning: opening record
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: OUTPUT
    field: record_id
    type: string
    required: 'YES'
    default: null
    meaning: record id
  - artifact: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    direction: OUTPUT
    field: sequence_number
    type: integer
    required: 'YES'
    default: null
    meaning: sequence number
  - artifact: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: time_in_service_id
    type: string
    required: 'YES'
    default: null
    meaning: time in service id
  - artifact: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: ceiling
    type: string
    required: 'YES'
    default: null
    meaning: ceiling
  - artifact: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: system_prompt
    type: string
    required: 'YES'
    default: null
    meaning: system prompt
  - artifact: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: response_rules
    type: object
    required: 'YES'
    default: null
    meaning: response rules
  - artifact: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    direction: OUTPUT
    field: time_in_service
    type: object
    required: 'YES'
    default: null
    meaning: time in service
  - artifact: causal_language_model::CC_READ_HOSTED_STATE_V0
    direction: INPUT
    field: user_prompt_id
    type: string
    required: 'YES'
    default: null
    meaning: user prompt id
  - artifact: causal_language_model::CC_READ_HOSTED_STATE_V0
    direction: OUTPUT
    field: entries
    type: array
    required: 'YES'
    default: null
    meaning: entries
  - artifact: causal_language_model::CC_READ_HOSTED_STATE_V0
    direction: OUTPUT
    field: state
    type: object
    required: 'YES'
    default: null
    meaning: state
  - artifact: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    direction: INPUT
    field: user_prompt_id
    type: string
    required: 'YES'
    default: null
    meaning: user prompt id
  - artifact: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    direction: INPUT
    field: host_id
    type: string
    required: 'YES'
    default: null
    meaning: host id
  - artifact: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    direction: INPUT
    field: fingerprint
    type: string
    required: 'YES'
    default: null
    meaning: fingerprint
  - artifact: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    direction: INPUT
    field: reported_reading_size
    type: integer
    required: 'YES'
    default: null
    meaning: reported reading size
  - artifact: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    direction: INPUT
    field: step
    type: object
    required: 'YES'
    default: null
    meaning: step
  - artifact: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    direction: OUTPUT
    field: step_record
    type: object
    required: 'YES'
    default: null
    meaning: step record
  - artifact: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    direction: OUTPUT
    field: record_id
    type: string
    required: 'YES'
    default: null
    meaning: record id
  - artifact: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    direction: OUTPUT
    field: sequence_number
    type: integer
    required: 'YES'
    default: null
    meaning: sequence number
  - artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
    direction: INPUT
    field: user_prompt_id
    type: string
    required: 'YES'
    default: null
    meaning: user prompt id
  - artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
    direction: INPUT
    field: requester_id
    type: string
    required: 'YES'
    default: null
    meaning: requester id
  - artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
    direction: INPUT
    field: customer_id
    type: string
    required: 'YES'
    default: null
    meaning: customer id
  - artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
    direction: INPUT
    field: kind
    type: string
    required: 'YES'
    default: null
    meaning: kind
  - artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
    direction: INPUT
    field: question
    type: string
    required: 'YES'
    default: null
    meaning: question
  - artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
    direction: INPUT
    field: supporting_material
    type: string
    required: 'YES'
    default: null
    meaning: supporting material
  - artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
    direction: INPUT
    field: outcome
    type: string
    required: 'YES'
    default: null
    meaning: outcome
  - artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
    direction: INPUT
    field: time_in_service_id
    type: string
    required: 'NO'
    default: null
    meaning: time in service id
  - artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
    direction: INPUT
    field: reading
    type: object
    required: 'NO'
    default: null
    meaning: reading
  - artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
    direction: INPUT
    field: rules_in_force
    type: object
    required: 'NO'
    default: null
    meaning: rules in force
  - artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
    direction: INPUT
    field: response
    type: string
    required: 'NO'
    default: null
    meaning: response
  - artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
    direction: INPUT
    field: reason
    type: string
    required: 'NO'
    default: null
    meaning: reason
  - artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
    direction: OUTPUT
    field: record_id
    type: string
    required: 'YES'
    default: null
    meaning: record id
  - artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
    direction: OUTPUT
    field: sequence_number
    type: integer
    required: 'YES'
    default: null
    meaning: sequence number
  - artifact: causal_language_model::CC_REGISTER_MODEL_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: causal_language_model::CC_REGISTER_MODEL_V0
    direction: INPUT
    field: description
    type: object
    required: 'YES'
    default: null
    meaning: description
  - artifact: causal_language_model::CC_REGISTER_MODEL_V0
    direction: INPUT
    field: fingerprint
    type: string
    required: 'YES'
    default: null
    meaning: fingerprint
  - artifact: causal_language_model::CC_REGISTER_MODEL_V0
    direction: OUTPUT
    field: model_record
    type: object
    required: 'YES'
    default: null
    meaning: model record
  - artifact: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
    direction: INPUT
    field: user_prompt_id
    type: string
    required: 'YES'
    default: null
    meaning: user prompt id
  - artifact: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
    direction: OUTPUT
    field: user_prompt_record
    type: array
    required: 'YES'
    default: null
    meaning: user prompt record
  - artifact: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    direction: OUTPUT
    field: model_record
    type: object
    required: 'YES'
    default: null
    meaning: model record
  - artifact: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    direction: INPUT
    field: response_rules
    type: object
    required: 'YES'
    default: null
    meaning: response rules
  - artifact: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    direction: INPUT
    field: account_numbers
    type: array
    required: 'YES'
    default: null
    meaning: account numbers
  - artifact: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    direction: INPUT
    field: seed
    type: integer
    required: 'YES'
    default: null
    meaning: seed
  - artifact: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    direction: INPUT
    field: reading
    type: object
    required: 'YES'
    default: null
    meaning: reading
  - artifact: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    direction: OUTPUT
    field: rules_in_force
    type: object
    required: 'YES'
    default: null
    meaning: rules in force
  - artifact: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    direction: OUTPUT
    field: written_response
    type: object
    required: 'YES'
    default: null
    meaning: written response
  - artifact: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    direction: INPUT
    field: reading
    type: object
    required: 'YES'
    default: null
    meaning: reading
  - artifact: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    direction: INPUT
    field: text
    type: string
    required: 'YES'
    default: null
    meaning: text
  - artifact: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    direction: INPUT
    field: finished
    type: boolean
    required: 'YES'
    default: null
    meaning: finished
  - artifact: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    direction: INPUT
    field: stopped_by
    type: string
    required: 'YES'
    default: null
    meaning: stopped by
  - artifact: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    direction: OUTPUT
    field: candidates
    type: array
    required: 'YES'
    default: null
    meaning: candidates
  - artifact: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    direction: INPUT
    field: system_prompt
    type: string
    required: 'YES'
    default: null
    meaning: system prompt
  - artifact: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    direction: INPUT
    field: question
    type: string
    required: 'YES'
    default: null
    meaning: question
  - artifact: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    direction: INPUT
    field: supporting_material
    type: string
    required: 'YES'
    default: null
    meaning: supporting material
  - artifact: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    direction: INPUT
    field: reading_capacity
    type: integer
    required: 'YES'
    default: null
    meaning: reading capacity
  - artifact: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    direction: OUTPUT
    field: reading
    type: object
    required: 'YES'
    default: null
    meaning: reading
  - artifact: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    direction: OUTPUT
    field: reading_length
    type: integer
    required: 'YES'
    default: null
    meaning: reading length
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    direction: INPUT
    field: state
    type: object
    required: 'YES'
    default: null
    meaning: state
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    direction: INPUT
    field: candidates
    type: array
    required: 'YES'
    default: null
    meaning: candidates
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    direction: OUTPUT
    field: step
    type: object
    required: 'YES'
    default: null
    meaning: step
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    direction: OUTPUT
    field: text
    type: string
    required: 'YES'
    default: null
    meaning: text
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    direction: OUTPUT
    field: finished
    type: boolean
    required: 'YES'
    default: null
    meaning: finished
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    direction: OUTPUT
    field: stopped_by
    type: string
    required: 'YES'
    default: null
    meaning: stopped by
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    direction: OUTPUT
    field: within_length
    type: boolean
    required: 'YES'
    default: null
    meaning: within length
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    direction: INPUT
    field: candidates
    type: array
    required: 'YES'
    default: null
    meaning: candidates
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    direction: INPUT
    field: rules_in_force
    type: object
    required: 'YES'
    default: null
    meaning: rules in force
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    direction: INPUT
    field: position
    type: integer
    required: 'YES'
    default: null
    meaning: position
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    direction: INPUT
    field: text
    type: string
    required: 'YES'
    default: null
    meaning: text
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    direction: INPUT
    field: finished
    type: boolean
    required: 'YES'
    default: null
    meaning: finished
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    direction: INPUT
    field: stopped_by
    type: string
    required: 'YES'
    default: null
    meaning: stopped by
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    direction: INPUT
    field: stopped
    type: array
    required: 'YES'
    default: null
    meaning: stopped
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    direction: OUTPUT
    field: text
    type: string
    required: 'YES'
    default: null
    meaning: text
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    direction: OUTPUT
    field: finished
    type: boolean
    required: 'YES'
    default: null
    meaning: finished
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    direction: OUTPUT
    field: stopped_by
    type: string
    required: 'YES'
    default: null
    meaning: stopped by
  - artifact: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    direction: OUTPUT
    field: stopped
    type: array
    required: 'YES'
    default: null
    meaning: stopped
  - artifact: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    direction: INPUT
    field: kind
    type: string
    required: 'YES'
    default: null
    meaning: kind
  - artifact: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    direction: INPUT
    field: ceiling
    type: string
    required: 'YES'
    default: null
    meaning: ceiling
  - artifact: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    direction: INPUT
    field: kinds
    type: array
    required: 'YES'
    default: null
    meaning: kinds
  - artifact: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    direction: OUTPUT
    field: within_ceiling
    type: boolean
    required: 'YES'
    default: null
    meaning: within ceiling
  - artifact: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    direction: INPUT
    field: description
    type: object
    required: 'YES'
    default: null
    meaning: description
  - artifact: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    direction: INPUT
    field: fingerprint
    type: string
    required: 'YES'
    default: null
    meaning: fingerprint
  - artifact: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    direction: OUTPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    direction: INPUT
    field: response_rules
    type: object
    required: 'YES'
    default: null
    meaning: response rules
  - artifact: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    direction: INPUT
    field: account_numbers
    type: array
    required: 'YES'
    default: null
    meaning: account numbers
  - artifact: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    direction: INPUT
    field: seed
    type: integer
    required: 'YES'
    default: null
    meaning: seed
  - artifact: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    direction: OUTPUT
    field: rules_in_force
    type: object
    required: 'YES'
    default: null
    meaning: rules in force
  - artifact: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    direction: OUTPUT
    field: positions
    type: array
    required: 'YES'
    default: null
    meaning: positions
  - artifact: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
    direction: INPUT
    field: entries
    type: array
    required: 'YES'
    default: null
    meaning: entries
  - artifact: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
    direction: OUTPUT
    field: state
    type: object
    required: 'YES'
    default: null
    meaning: state
  - artifact: causal_language_model::CT_WRITE_NEXT_WORD_V0
    direction: INPUT
    field: reading
    type: object
    required: 'YES'
    default: null
    meaning: reading
  - artifact: causal_language_model::CT_WRITE_NEXT_WORD_V0
    direction: INPUT
    field: rules_in_force
    type: object
    required: 'YES'
    default: null
    meaning: rules in force
  - artifact: causal_language_model::CT_WRITE_NEXT_WORD_V0
    direction: INPUT
    field: position
    type: integer
    required: 'YES'
    default: null
    meaning: position
  - artifact: causal_language_model::CT_WRITE_NEXT_WORD_V0
    direction: INPUT
    field: text
    type: string
    required: 'YES'
    default: null
    meaning: text
  - artifact: causal_language_model::CT_WRITE_NEXT_WORD_V0
    direction: INPUT
    field: finished
    type: boolean
    required: 'YES'
    default: null
    meaning: finished
  - artifact: causal_language_model::CT_WRITE_NEXT_WORD_V0
    direction: INPUT
    field: stopped_by
    type: string
    required: 'YES'
    default: null
    meaning: stopped by
  - artifact: causal_language_model::CT_WRITE_NEXT_WORD_V0
    direction: INPUT
    field: stopped
    type: array
    required: 'YES'
    default: null
    meaning: stopped
  - artifact: causal_language_model::CT_WRITE_NEXT_WORD_V0
    direction: OUTPUT
    field: result
    type: object
    required: 'YES'
    default: null
    meaning: result
  - artifact: causal_language_model::CT_WRITE_RESPONSE_V0
    direction: INPUT
    field: reading
    type: object
    required: 'YES'
    default: null
    meaning: reading
  - artifact: causal_language_model::CT_WRITE_RESPONSE_V0
    direction: INPUT
    field: rules_in_force
    type: object
    required: 'YES'
    default: null
    meaning: rules in force
  - artifact: causal_language_model::CT_WRITE_RESPONSE_V0
    direction: INPUT
    field: positions
    type: array
    required: 'YES'
    default: null
    meaning: positions
  - artifact: causal_language_model::CT_WRITE_RESPONSE_V0
    direction: OUTPUT
    field: result
    type: object
    required: 'YES'
    default: null
    meaning: result
  - artifact: causal_language_model::EV_MODEL_REGISTERED_V0
    direction: OUTPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: causal_language_model::EV_MODEL_REGISTERED_V0
    direction: OUTPUT
    field: staff_id
    type: string
    required: 'YES'
    default: null
    meaning: staff id
  - artifact: causal_language_model::EV_MODEL_REGISTERED_V0
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: When the moment occurred
    format: date-time
  - artifact: causal_language_model::EV_MODEL_SERVICE_ENDED_V0
    direction: OUTPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: causal_language_model::EV_MODEL_SERVICE_ENDED_V0
    direction: OUTPUT
    field: staff_id
    type: string
    required: 'YES'
    default: null
    meaning: staff id
  - artifact: causal_language_model::EV_MODEL_SERVICE_ENDED_V0
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: When the moment occurred
    format: date-time
  - artifact: causal_language_model::EV_MODEL_SERVICE_STARTED_V0
    direction: OUTPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: causal_language_model::EV_MODEL_SERVICE_STARTED_V0
    direction: OUTPUT
    field: time_in_service_id
    type: string
    required: 'YES'
    default: null
    meaning: time in service id
  - artifact: causal_language_model::EV_MODEL_SERVICE_STARTED_V0
    direction: OUTPUT
    field: staff_id
    type: string
    required: 'YES'
    default: null
    meaning: staff id
  - artifact: causal_language_model::EV_MODEL_SERVICE_STARTED_V0
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: When the moment occurred
    format: date-time
  - artifact: causal_language_model::EV_USER_PROMPT_REFUSED_V0
    direction: OUTPUT
    field: user_prompt_id
    type: string
    required: 'YES'
    default: null
    meaning: user prompt id
  - artifact: causal_language_model::EV_USER_PROMPT_REFUSED_V0
    direction: OUTPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: causal_language_model::EV_USER_PROMPT_REFUSED_V0
    direction: OUTPUT
    field: requester_id
    type: string
    required: 'YES'
    default: null
    meaning: requester id
  - artifact: causal_language_model::EV_USER_PROMPT_REFUSED_V0
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: When the moment occurred
    format: date-time
  - artifact: causal_language_model::EV_USER_PROMPT_RESPONDED_V0
    direction: OUTPUT
    field: user_prompt_id
    type: string
    required: 'YES'
    default: null
    meaning: user prompt id
  - artifact: causal_language_model::EV_USER_PROMPT_RESPONDED_V0
    direction: OUTPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: causal_language_model::EV_USER_PROMPT_RESPONDED_V0
    direction: OUTPUT
    field: requester_id
    type: string
    required: 'YES'
    default: null
    meaning: requester id
  - artifact: causal_language_model::EV_USER_PROMPT_RESPONDED_V0
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: When the moment occurred
    format: date-time
  - artifact: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
    direction: INPUT
    field: user_prompt_id
    type: string
    required: 'YES'
    default: null
    meaning: user prompt id
  - artifact: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
    direction: INPUT
    field: requester_id
    type: string
    required: 'YES'
    default: null
    meaning: requester id
  - artifact: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
    direction: INPUT
    field: permitted_customers
    type: array
    required: 'YES'
    default: null
    meaning: permitted customers
  - artifact: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
    direction: INPUT
    field: customer_id
    type: string
    required: 'YES'
    default: null
    meaning: customer id
  - artifact: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
    direction: INPUT
    field: account_numbers
    type: array
    required: 'YES'
    default: null
    meaning: account numbers
  - artifact: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
    direction: INPUT
    field: kind
    type: string
    required: 'YES'
    default: null
    meaning: kind
  - artifact: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
    direction: INPUT
    field: question
    type: string
    required: 'YES'
    default: null
    meaning: question
  - artifact: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
    direction: INPUT
    field: supporting_material
    type: string
    required: 'YES'
    default: null
    meaning: supporting material
  - artifact: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
    direction: INPUT
    field: seed
    type: integer
    required: 'YES'
    default: null
    meaning: seed
  - artifact: causal_language_model::IN_OFFER_NEXT_TOKENS_V0
    direction: INPUT
    field: user_prompt_id
    type: string
    required: 'YES'
    default: null
    meaning: user prompt id
  - artifact: causal_language_model::IN_OFFER_NEXT_TOKENS_V0
    direction: INPUT
    field: host_id
    type: string
    required: 'YES'
    default: null
    meaning: host id
  - artifact: causal_language_model::IN_OFFER_NEXT_TOKENS_V0
    direction: INPUT
    field: fingerprint
    type: string
    required: 'YES'
    default: null
    meaning: fingerprint
  - artifact: causal_language_model::IN_OFFER_NEXT_TOKENS_V0
    direction: INPUT
    field: reported_reading_size
    type: integer
    required: 'YES'
    default: null
    meaning: reported reading size
  - artifact: causal_language_model::IN_OFFER_NEXT_TOKENS_V0
    direction: INPUT
    field: candidates
    type: array
    required: 'YES'
    default: null
    meaning: candidates
  - artifact: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: null
    meaning: staff credentials
  - artifact: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: null
    meaning: staff id
  - artifact: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: time_in_service_id
    type: string
    required: 'YES'
    default: null
    meaning: time in service id
  - artifact: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: ceiling
    type: string
    required: 'YES'
    default: null
    meaning: ceiling
  - artifact: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: system_prompt
    type: string
    required: 'YES'
    default: null
    meaning: system prompt
  - artifact: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
    direction: INPUT
    field: response_rules
    type: object
    required: 'YES'
    default: null
    meaning: response rules
  - artifact: causal_language_model::IN_REGISTER_MODEL_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: null
    meaning: staff credentials
  - artifact: causal_language_model::IN_REGISTER_MODEL_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: null
    meaning: staff id
  - artifact: causal_language_model::IN_REGISTER_MODEL_V0
    direction: INPUT
    field: description
    type: object
    required: 'YES'
    default: null
    meaning: description
  - artifact: causal_language_model::IN_REGISTER_MODEL_V0
    direction: INPUT
    field: fingerprint
    type: string
    required: 'YES'
    default: null
    meaning: fingerprint
  - artifact: causal_language_model::IN_RELEASE_HOSTED_RESPONSE_V0
    direction: INPUT
    field: user_prompt_id
    type: string
    required: 'YES'
    default: null
    meaning: user prompt id
  - artifact: causal_language_model::IN_RELEASE_HOSTED_RESPONSE_V0
    direction: INPUT
    field: host_id
    type: string
    required: 'YES'
    default: null
    meaning: host id
  - artifact: causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: null
    meaning: staff credentials
  - artifact: causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: null
    meaning: staff id
  - artifact: causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0
    direction: INPUT
    field: user_prompt_id
    type: string
    required: 'YES'
    default: null
    meaning: user prompt id
  - artifact: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
    direction: INPUT
    field: user_prompt_id
    type: string
    required: 'YES'
    default: null
    meaning: user prompt id
  - artifact: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
    direction: INPUT
    field: requester_id
    type: string
    required: 'YES'
    default: null
    meaning: requester id
  - artifact: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
    direction: INPUT
    field: permitted_customers
    type: array
    required: 'YES'
    default: null
    meaning: permitted customers
  - artifact: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
    direction: INPUT
    field: customer_id
    type: string
    required: 'YES'
    default: null
    meaning: customer id
  - artifact: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
    direction: INPUT
    field: account_numbers
    type: array
    required: 'YES'
    default: null
    meaning: account numbers
  - artifact: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
    direction: INPUT
    field: kind
    type: string
    required: 'YES'
    default: null
    meaning: kind
  - artifact: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
    direction: INPUT
    field: question
    type: string
    required: 'YES'
    default: null
    meaning: question
  - artifact: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
    direction: INPUT
    field: supporting_material
    type: string
    required: 'YES'
    default: null
    meaning: supporting material
  - artifact: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
    direction: INPUT
    field: seed
    type: integer
    required: 'YES'
    default: null
    meaning: seed
  - artifact: causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: null
    meaning: staff credentials
  - artifact: causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: null
    meaning: staff id
  - artifact: causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  implementation_bindings:
  - ct_code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    callable: execute
    operation: OFFER_NEXT_WORDS
    kind: atom
    purity: ct_impure
    refusal: never
  - ct_code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    callable: execute
    operation: ASSEMBLE_MODEL_READING
    kind: atom
    purity: ct_pure
    refusal: raises
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    callable: execute
    operation: CHOOSE_PERMITTED_TOKEN
    kind: atom
    purity: ct_pure
    refusal: raises
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    callable: execute
    operation: CHOOSE_PERMITTED_WORD
    kind: atom
    purity: ct_pure
    refusal: returns
  - ct_code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    callable: execute
    operation: COMPARE_SENSITIVITY
    kind: atom
    purity: ct_pure
    refusal: raises
  - ct_code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    callable: execute
    operation: FORM_MODEL_IDENTITY_KEY
    kind: atom
    purity: ct_pure
    refusal: never
  - ct_code: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    callable: execute
    operation: FORM_RESPONSE_RULES
    kind: atom
    purity: ct_pure
    refusal: never
  - ct_code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
    callable: execute
    operation: READ_HOSTED_STATE
    kind: atom
    purity: ct_pure
    refusal: raises
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    callable: null
    operation: WRITE_NEXT_WORD
    kind: molecule
    purity: ct_impure
    refusal: returns
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    callable: null
    operation: WRITE_RESPONSE
    kind: molecule
    purity: ct_impure
    refusal: returns
  vocabulary_extensions:
  - vocabulary_code: causal_language_model::VOCAB_KIND_OF_INFORMATION_V0
    extends: null
    group: kind_of_information
    casing: lower_snake
    value: public
    meaning: public
  - vocabulary_code: causal_language_model::VOCAB_KIND_OF_INFORMATION_V0
    extends: null
    group: kind_of_information
    casing: lower_snake
    value: internal
    meaning: internal
  - vocabulary_code: causal_language_model::VOCAB_KIND_OF_INFORMATION_V0
    extends: null
    group: kind_of_information
    casing: lower_snake
    value: confidential
    meaning: confidential
  - vocabulary_code: causal_language_model::VOCAB_KIND_OF_INFORMATION_V0
    extends: null
    group: kind_of_information
    casing: lower_snake
    value: restricted
    meaning: restricted
  runtime_policies:
  - rb_code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    key: structure
    value: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
  - rb_code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    capability: capability_side_effects::CS_REGISTRY_V0
    key: structure
    value: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
  - rb_code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    key: structure
    value: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
  artifact_properties:
  - artifact: causal_language_model::AC_MODEL_HOST_V0
    property: type
    value: ENDUSER
  - artifact: causal_language_model::AC_MODEL_STAFF_V0
    property: type
    value: ENDUSER
  - artifact: causal_language_model::AC_REQUESTER_V0
    property: type
    value: ENDUSER
  - artifact: causal_language_model::EV_USER_PROMPT_REFUSED_V0
    property: moment
    value: refusal
  - artifact: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    property: layer
    value: DOMAINS
  - artifact: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    property: actor_context
    value: causal_language_model::AC_MODEL_HOST_V0
  - artifact: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    property: emit.EXIT_REFUSED
    value:
    - causal_language_model::EV_USER_PROMPT_REFUSED_V0
  - artifact: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    property: actor_context
    value: causal_language_model::AC_MODEL_HOST_V0
  - artifact: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    property: emit.EXIT_REFUSED
    value:
    - causal_language_model::EV_USER_PROMPT_REFUSED_V0
  - artifact: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    property: actor_context
    value: causal_language_model::AC_MODEL_STAFF_V0
  - artifact: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    property: emit.EXIT_PLACED
    value:
    - causal_language_model::EV_MODEL_SERVICE_STARTED_V0
  - artifact: causal_language_model::WF_REGISTER_MODEL_V0
    property: actor_context
    value: causal_language_model::AC_MODEL_STAFF_V0
  - artifact: causal_language_model::WF_REGISTER_MODEL_V0
    property: emit.EXIT_REGISTERED
    value:
    - causal_language_model::EV_MODEL_REGISTERED_V0
  - artifact: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    property: actor_context
    value: causal_language_model::AC_MODEL_HOST_V0
  - artifact: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    property: emit.EXIT_RESPONDED
    value:
    - causal_language_model::EV_USER_PROMPT_RESPONDED_V0
  - artifact: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    property: actor_context
    value: causal_language_model::AC_MODEL_STAFF_V0
  - artifact: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    property: actor_context
    value: causal_language_model::AC_REQUESTER_V0
  - artifact: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    property: emit.EXIT_RESPONDED
    value:
    - causal_language_model::EV_USER_PROMPT_RESPONDED_V0
  - artifact: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    property: emit.EXIT_REFUSED
    value:
    - causal_language_model::EV_USER_PROMPT_REFUSED_V0
  - artifact: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    property: actor_context
    value: causal_language_model::AC_MODEL_STAFF_V0
  - artifact: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    property: emit.EXIT_WITHDRAWN
    value:
    - causal_language_model::EV_MODEL_SERVICE_ENDED_V0
  structure_stores:
  - store_name: MODELS
    storage_type: CS_MUTABLE_JSON_V0
    proposed_path: causal_language_model/model_response/models.json
    used_by: causal_language_model::CC_ADMIT_USER_PROMPT_V0, causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0,
      causal_language_model::CC_REGISTER_MODEL_V0, causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
  - store_name: MODEL_IDENTITY_REGISTRY
    storage_type: CS_REGISTRY_V0
    proposed_path: causal_language_model/model_response/model_identity_registry.jsonl
    used_by: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
  - store_name: TIME_IN_SERVICE_REGISTRY
    storage_type: CS_REGISTRY_V0
    proposed_path: causal_language_model/model_response/time_in_service_registry.jsonl
    used_by: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
  - store_name: USER_PROMPT_REGISTRY
    storage_type: CS_REGISTRY_V0
    proposed_path: causal_language_model/model_response/user_prompt_registry.jsonl
    used_by: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
  - store_name: TIMES_IN_SERVICE
    storage_type: CS_MUTABLE_JSON_V0
    proposed_path: causal_language_model/model_response/times_in_service.json
    used_by: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0, causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0,
      causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
  - store_name: USER_PROMPT_RECORDS
    storage_type: CS_APPENDONLY_JSONL_V0
    proposed_path: causal_language_model/model_response/user_prompt_records.jsonl
    used_by: causal_language_model::CC_OPEN_HOSTED_RECORD_V0, causal_language_model::CC_READ_HOSTED_STATE_V0,
      causal_language_model::CC_RECORD_HOSTED_STEP_V0, causal_language_model::CC_RECORD_USER_PROMPT_V0,
      causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
    structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
  - store_name: MODEL_OPERATIONS
    storage_type: CS_APPENDONLY_JSONL_V0
    proposed_path: causal_language_model/model_response/model_operations.jsonl
    used_by: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
  transport_bindings: []
  declared_reach: []
  molecule_steps:
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    step: offered
    kind: atom
    target: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    over: null
    iterator: null
    emits: null
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    step: chosen
    kind: atom
    target: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    over: null
    iterator: null
    emits: result
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    step: written
    kind: loop
    target: causal_language_model::CT_WRITE_NEXT_WORD_V0
    over: inputs.positions
    iterator: position
    emits: result
  molecule_step_bindings:
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    step: offered
    role: INPUT
    field: reading
    bound_to: inputs.reading
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    step: offered
    role: INPUT
    field: text
    bound_to: inputs.text
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    step: offered
    role: INPUT
    field: finished
    bound_to: inputs.finished
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    step: offered
    role: INPUT
    field: stopped_by
    bound_to: inputs.stopped_by
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    step: chosen
    role: INPUT
    field: candidates
    bound_to: results.offered.candidates
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    step: chosen
    role: INPUT
    field: rules_in_force
    bound_to: inputs.rules_in_force
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    step: chosen
    role: INPUT
    field: position
    bound_to: inputs.position
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    step: chosen
    role: INPUT
    field: text
    bound_to: inputs.text
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    step: chosen
    role: INPUT
    field: finished
    bound_to: inputs.finished
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    step: chosen
    role: INPUT
    field: stopped_by
    bound_to: inputs.stopped_by
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    step: chosen
    role: INPUT
    field: stopped
    bound_to: inputs.stopped
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    step: written
    role: CARRY
    field: text
    bound_to:
      literal: ''
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    step: written
    role: CARRY
    field: finished
    bound_to:
      literal: false
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    step: written
    role: CARRY
    field: stopped_by
    bound_to:
      literal: none
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    step: written
    role: CARRY
    field: stopped
    bound_to:
      literal: []
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    step: written
    role: INPUT
    field: position
    bound_to: iterator
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    step: written
    role: INPUT
    field: reading
    bound_to: inputs.reading
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    step: written
    role: INPUT
    field: rules_in_force
    bound_to: inputs.rules_in_force
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    step: written
    role: INPUT
    field: text
    bound_to: accumulator.text
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    step: written
    role: INPUT
    field: finished
    bound_to: accumulator.finished
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    step: written
    role: INPUT
    field: stopped_by
    bound_to: accumulator.stopped_by
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    step: written
    role: INPUT
    field: stopped
    bound_to: accumulator.stopped
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    step: written
    role: UPDATE
    field: text
    bound_to: results.text
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    step: written
    role: UPDATE
    field: finished
    bound_to: results.finished
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    step: written
    role: UPDATE
    field: stopped_by
    bound_to: results.stopped_by
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    step: written
    role: UPDATE
    field: stopped
    bound_to: results.stopped
  test_cases:
  - ct_code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    case: offers_candidates
    expected_outcome: SUCCESS
  - ct_code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    case: assembles_what_fits
    expected_outcome: SUCCESS
  - ct_code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    case: refuses_reading_too_long
    expected_outcome: VIOLATION
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: stops_an_account_number_split_across_tokens
    expected_outcome: SUCCESS
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: writes_the_customers_own_account_across_tokens
    expected_outcome: SUCCESS
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: names_the_rule_when_no_permitted_token_remains
    expected_outcome: SUCCESS
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: passes_the_permitted_length_unfinished
    expected_outcome: SUCCESS
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: finishes_on_the_end_of_the_response
    expected_outcome: SUCCESS
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: judges_a_lookalike_digit_as_the_digit
    expected_outcome: SUCCESS
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: does_not_begin_a_forbidden_number_the_model_read
    expected_outcome: SUCCESS
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: begins_a_number_the_model_read_that_is_permitted
    expected_outcome: SUCCESS
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: grounded_writes_a_number_it_read
    expected_outcome: SUCCESS
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: grounded_does_not_change_a_value_it_read
    expected_outcome: SUCCESS
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: ungrounded_writes_a_number_it_did_not_read
    expected_outcome: SUCCESS
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: refuses_an_offer_for_a_complete_response
    expected_outcome: VIOLATION
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_another_customers_account_and_continues
    expected_outcome: SUCCESS
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_an_account_number_written_across_two_words
    expected_outcome: SUCCESS
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: writes_the_customers_own_account_across_two_words
    expected_outcome: SUCCESS
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: names_the_rule_when_no_permitted_word_remains
    expected_outcome: SUCCESS
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: draws_an_adventurous_word_from_the_seed
    expected_outcome: SUCCESS
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: finishes_on_the_end_of_the_response
    expected_outcome: SUCCESS
  - ct_code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    case: admits_kind_within_ceiling
    expected_outcome: SUCCESS
  - ct_code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    case: refuses_kind_above_ceiling
    expected_outcome: VIOLATION
  - ct_code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    case: forms_key_from_description_and_fingerprint
    expected_outcome: SUCCESS
  - ct_code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    case: refuses_blank_fingerprint
    expected_outcome: VIOLATION
  - ct_code: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    case: adds_the_account_rule_and_positions
    expected_outcome: SUCCESS
  - ct_code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
    case: reduces_the_trail_to_the_response_as_built
    expected_outcome: SUCCESS
  - ct_code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
    case: refuses_a_request_never_admitted
    expected_outcome: VIOLATION
  - ct_code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
    case: refuses_a_closed_request
    expected_outcome: VIOLATION
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    case: writes_one_permitted_word_from_a_recorded_offer
    expected_outcome: SUCCESS
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    case: writes_a_finished_response_and_offers_nothing_after
    expected_outcome: SUCCESS
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    case: stops_unfinished_at_the_longest_response
    expected_outcome: SUCCESS
  test_case_values:
  - ct_code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    case: offers_candidates
    role: INPUT
    field: reading
    value:
      system_prompt: Answer briefly.
      question: What is my balance?
      supporting_material: Account 12345678 balance 40.
  - ct_code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    case: offers_candidates
    role: INPUT
    field: text
    value: ''
  - ct_code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    case: offers_candidates
    role: INPUT
    field: finished
    value: false
  - ct_code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    case: offers_candidates
    role: INPUT
    field: stopped_by
    value: none
  - ct_code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    case: offers_candidates
    role: ASSERT
    field: candidates
    value:
      mode: property
      type: non_zero
  - ct_code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    case: assembles_what_fits
    role: INPUT
    field: system_prompt
    value: Answer briefly.
  - ct_code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    case: assembles_what_fits
    role: INPUT
    field: question
    value: What is my balance?
  - ct_code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    case: assembles_what_fits
    role: INPUT
    field: supporting_material
    value: Account 12345678 balance 40.
  - ct_code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    case: assembles_what_fits
    role: INPUT
    field: reading_capacity
    value: 20
  - ct_code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    case: assembles_what_fits
    role: EXPECTED
    field: reading
    value:
      system_prompt: Answer briefly.
      question: What is my balance?
      supporting_material: Account 12345678 balance 40.
  - ct_code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    case: assembles_what_fits
    role: EXPECTED
    field: reading_length
    value: 10
  - ct_code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    case: refuses_reading_too_long
    role: INPUT
    field: system_prompt
    value: Answer briefly.
  - ct_code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    case: refuses_reading_too_long
    role: INPUT
    field: question
    value: What is my balance?
  - ct_code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    case: refuses_reading_too_long
    role: INPUT
    field: supporting_material
    value: Account 12345678 balance 40.
  - ct_code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    case: refuses_reading_too_long
    role: INPUT
    field: reading_capacity
    value: 5
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: stops_an_account_number_split_across_tokens
    role: INPUT
    field: state
    value:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
        rules_in_force:
          forbidden:
          - rule: no_guarantees
            pattern: \bguaranteed\b
          - rule: another_customers_account_number
            pattern: '[0-9](?:[ -]?[0-9]){7}'
            except:
            - '12345678'
          freedom: 0
          seed: 7
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
      position: 1
      text: Account 8765
      finished: false
      limit: 3
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: stops_an_account_number_split_across_tokens
    role: INPUT
    field: candidates
    value:
    - token: '4321'
      likelihood: 0.7
    - token: ' is'
      likelihood: 0.2
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: stops_an_account_number_split_across_tokens
    role: EXPECTED
    field: text
    value: Account 8765 is
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: stops_an_account_number_split_across_tokens
    role: EXPECTED
    field: finished
    value: false
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: stops_an_account_number_split_across_tokens
    role: EXPECTED
    field: stopped_by
    value: none
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: stops_an_account_number_split_across_tokens
    role: EXPECTED
    field: within_length
    value: true
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: stops_an_account_number_split_across_tokens
    role: EXPECTED
    field: step
    value:
      position: 2
      candidates:
      - token: '4321'
        likelihood: 0.7
      - token: ' is'
        likelihood: 0.2
      chosen: ' is'
      stopped:
      - token: '4321'
        rule: another_customers_account_number
      stopped_by: none
      finished: false
      within_length: true
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: writes_the_customers_own_account_across_tokens
    role: INPUT
    field: state
    value:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
        rules_in_force:
          forbidden:
          - rule: no_guarantees
            pattern: \bguaranteed\b
          - rule: another_customers_account_number
            pattern: '[0-9](?:[ -]?[0-9]){7}'
            except:
            - '12345678'
          freedom: 0
          seed: 7
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
      position: 1
      text: Account 1234
      finished: false
      limit: 3
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: writes_the_customers_own_account_across_tokens
    role: INPUT
    field: candidates
    value:
    - token: '5678'
      likelihood: 0.8
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: writes_the_customers_own_account_across_tokens
    role: EXPECTED
    field: text
    value: Account 12345678
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: writes_the_customers_own_account_across_tokens
    role: EXPECTED
    field: stopped_by
    value: none
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: writes_the_customers_own_account_across_tokens
    role: EXPECTED
    field: step
    value:
      position: 2
      candidates:
      - token: '5678'
        likelihood: 0.8
      chosen: '5678'
      stopped: []
      stopped_by: none
      finished: false
      within_length: true
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: writes_the_customers_own_account_across_tokens
    role: EXPECTED
    field: finished
    value: false
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: writes_the_customers_own_account_across_tokens
    role: EXPECTED
    field: within_length
    value: true
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: names_the_rule_when_no_permitted_token_remains
    role: INPUT
    field: state
    value:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
        rules_in_force:
          forbidden:
          - rule: no_guarantees
            pattern: \bguaranteed\b
          - rule: another_customers_account_number
            pattern: '[0-9](?:[ -]?[0-9]){7}'
            except:
            - '12345678'
          freedom: 0
          seed: 7
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
      position: 0
      text: ''
      finished: false
      limit: 3
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: names_the_rule_when_no_permitted_token_remains
    role: INPUT
    field: candidates
    value:
    - token: '87654321'
      likelihood: 0.9
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: names_the_rule_when_no_permitted_token_remains
    role: EXPECTED
    field: text
    value: ''
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: names_the_rule_when_no_permitted_token_remains
    role: EXPECTED
    field: stopped_by
    value: another_customers_account_number
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: names_the_rule_when_no_permitted_token_remains
    role: EXPECTED
    field: finished
    value: false
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: names_the_rule_when_no_permitted_token_remains
    role: EXPECTED
    field: step
    value:
      position: 1
      candidates:
      - token: '87654321'
        likelihood: 0.9
      chosen: null
      stopped:
      - token: '87654321'
        rule: another_customers_account_number
      stopped_by: another_customers_account_number
      finished: false
      within_length: true
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: names_the_rule_when_no_permitted_token_remains
    role: EXPECTED
    field: within_length
    value: true
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: passes_the_permitted_length_unfinished
    role: INPUT
    field: state
    value:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
        rules_in_force:
          forbidden:
          - rule: no_guarantees
            pattern: \bguaranteed\b
          - rule: another_customers_account_number
            pattern: '[0-9](?:[ -]?[0-9]){7}'
            except:
            - '12345678'
          freedom: 0
          seed: 7
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
      position: 3
      text: Your balance is
      finished: false
      limit: 3
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: passes_the_permitted_length_unfinished
    role: INPUT
    field: candidates
    value:
    - token: ' today'
      likelihood: 0.9
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: passes_the_permitted_length_unfinished
    role: EXPECTED
    field: text
    value: Your balance is today
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: passes_the_permitted_length_unfinished
    role: EXPECTED
    field: within_length
    value: false
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: passes_the_permitted_length_unfinished
    role: EXPECTED
    field: finished
    value: false
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: passes_the_permitted_length_unfinished
    role: EXPECTED
    field: step
    value:
      position: 4
      candidates:
      - token: ' today'
        likelihood: 0.9
      chosen: ' today'
      stopped: []
      stopped_by: none
      finished: false
      within_length: false
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: passes_the_permitted_length_unfinished
    role: EXPECTED
    field: stopped_by
    value: none
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: finishes_on_the_end_of_the_response
    role: INPUT
    field: state
    value:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
        rules_in_force:
          forbidden:
          - rule: no_guarantees
            pattern: \bguaranteed\b
          - rule: another_customers_account_number
            pattern: '[0-9](?:[ -]?[0-9]){7}'
            except:
            - '12345678'
          freedom: 0
          seed: 7
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
      position: 2
      text: Your balance
      finished: false
      limit: 3
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: finishes_on_the_end_of_the_response
    role: INPUT
    field: candidates
    value:
    - token: <end>
      likelihood: 0.9
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: finishes_on_the_end_of_the_response
    role: EXPECTED
    field: text
    value: Your balance
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: finishes_on_the_end_of_the_response
    role: EXPECTED
    field: finished
    value: true
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: finishes_on_the_end_of_the_response
    role: EXPECTED
    field: within_length
    value: true
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: finishes_on_the_end_of_the_response
    role: EXPECTED
    field: step
    value:
      position: 3
      candidates:
      - token: <end>
        likelihood: 0.9
      chosen: <end>
      stopped: []
      stopped_by: none
      finished: true
      within_length: true
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: finishes_on_the_end_of_the_response
    role: EXPECTED
    field: stopped_by
    value: none
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: judges_a_lookalike_digit_as_the_digit
    role: INPUT
    field: state
    value:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
        rules_in_force:
          forbidden:
          - rule: no_guarantees
            pattern: \bguaranteed\b
          - rule: another_customers_account_number
            pattern: '[0-9](?:[ -]?[0-9]){7}'
            except:
            - '12345678'
          freedom: 0
          seed: 7
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
      position: 2
      text: Spouse account 8765432
      finished: false
      limit: 3
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: judges_a_lookalike_digit_as_the_digit
    role: INPUT
    field: candidates
    value:
    - token: ₁
      likelihood: 0.8
    - token: .
      likelihood: 0.1
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: judges_a_lookalike_digit_as_the_digit
    role: EXPECTED
    field: text
    value: Spouse account 8765432.
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: judges_a_lookalike_digit_as_the_digit
    role: EXPECTED
    field: stopped_by
    value: none
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: judges_a_lookalike_digit_as_the_digit
    role: EXPECTED
    field: step
    value:
      position: 3
      candidates:
      - token: ₁
        likelihood: 0.8
      - token: .
        likelihood: 0.1
      chosen: .
      stopped:
      - token: ₁
        rule: another_customers_account_number
      stopped_by: none
      finished: false
      within_length: true
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: judges_a_lookalike_digit_as_the_digit
    role: EXPECTED
    field: finished
    value: false
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: judges_a_lookalike_digit_as_the_digit
    role: EXPECTED
    field: within_length
    value: true
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: does_not_begin_a_forbidden_number_the_model_read
    role: INPUT
    field: state
    value:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
        rules_in_force:
          forbidden:
          - rule: no_guarantees
            pattern: \bguaranteed\b
          - rule: another_customers_account_number
            pattern: '[0-9](?:[ -]?[0-9]){7}'
            except:
            - '12345678'
          freedom: 0
          seed: 7
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
      position: 2
      text: 'Spouse account '
      finished: false
      limit: 3
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: does_not_begin_a_forbidden_number_the_model_read
    role: INPUT
    field: candidates
    value:
    - token: '8'
      likelihood: 0.8
    - token: withheld
      likelihood: 0.1
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: does_not_begin_a_forbidden_number_the_model_read
    role: EXPECTED
    field: text
    value: Spouse account withheld
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: does_not_begin_a_forbidden_number_the_model_read
    role: EXPECTED
    field: stopped_by
    value: none
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: does_not_begin_a_forbidden_number_the_model_read
    role: EXPECTED
    field: step
    value:
      position: 3
      candidates:
      - token: '8'
        likelihood: 0.8
      - token: withheld
        likelihood: 0.1
      chosen: withheld
      stopped:
      - token: '8'
        rule: another_customers_account_number
      stopped_by: none
      finished: false
      within_length: true
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: does_not_begin_a_forbidden_number_the_model_read
    role: EXPECTED
    field: finished
    value: false
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: does_not_begin_a_forbidden_number_the_model_read
    role: EXPECTED
    field: within_length
    value: true
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: begins_a_number_the_model_read_that_is_permitted
    role: INPUT
    field: state
    value:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
        rules_in_force:
          forbidden:
          - rule: no_guarantees
            pattern: \bguaranteed\b
          - rule: another_customers_account_number
            pattern: '[0-9](?:[ -]?[0-9]){7}'
            except:
            - '12345678'
          freedom: 0
          seed: 7
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
      position: 2
      text: 'Balance '
      finished: false
      limit: 3
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: begins_a_number_the_model_read_that_is_permitted
    role: INPUT
    field: candidates
    value:
    - token: '4'
      likelihood: 0.8
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: begins_a_number_the_model_read_that_is_permitted
    role: EXPECTED
    field: text
    value: Balance 4
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: begins_a_number_the_model_read_that_is_permitted
    role: EXPECTED
    field: stopped_by
    value: none
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: begins_a_number_the_model_read_that_is_permitted
    role: EXPECTED
    field: step
    value:
      position: 3
      candidates:
      - token: '4'
        likelihood: 0.8
      chosen: '4'
      stopped: []
      stopped_by: none
      finished: false
      within_length: true
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: begins_a_number_the_model_read_that_is_permitted
    role: EXPECTED
    field: finished
    value: false
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: begins_a_number_the_model_read_that_is_permitted
    role: EXPECTED
    field: within_length
    value: true
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: grounded_writes_a_number_it_read
    role: INPUT
    field: state
    value:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
        rules_in_force:
          forbidden:
          - rule: no_guarantees
            pattern: \bguaranteed\b
          - rule: another_customers_account_number
            pattern: '[0-9](?:[ -]?[0-9]){7}'
            except:
            - '12345678'
          freedom: 0
          seed: 7
        ground_numbers: true
        maximum_response_length: 3
        longest_response: 5
      position: 2
      text: Balance 4
      finished: false
      limit: 3
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: grounded_writes_a_number_it_read
    role: INPUT
    field: candidates
    value:
    - token: '9'
      likelihood: 0.8
    - token: '0'
      likelihood: 0.1
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: grounded_writes_a_number_it_read
    role: EXPECTED
    field: text
    value: Balance 40
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: grounded_writes_a_number_it_read
    role: EXPECTED
    field: stopped_by
    value: none
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: grounded_writes_a_number_it_read
    role: EXPECTED
    field: step
    value:
      position: 3
      candidates:
      - token: '9'
        likelihood: 0.8
      - token: '0'
        likelihood: 0.1
      chosen: '0'
      stopped:
      - token: '9'
        rule: numbers_from_the_reading
      stopped_by: none
      finished: false
      within_length: true
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: grounded_writes_a_number_it_read
    role: EXPECTED
    field: finished
    value: false
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: grounded_writes_a_number_it_read
    role: EXPECTED
    field: within_length
    value: true
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: grounded_does_not_change_a_value_it_read
    role: INPUT
    field: state
    value:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
        rules_in_force:
          forbidden:
          - rule: no_guarantees
            pattern: \bguaranteed\b
          - rule: another_customers_account_number
            pattern: '[0-9](?:[ -]?[0-9]){7}'
            except:
            - '12345678'
          freedom: 0
          seed: 7
        ground_numbers: true
        maximum_response_length: 3
        longest_response: 5
      position: 2
      text: Balance 4
      finished: false
      limit: 3
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: grounded_does_not_change_a_value_it_read
    role: INPUT
    field: candidates
    value:
    - token: ' dollars'
      likelihood: 0.8
    - token: <end>
      likelihood: 0.1
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: grounded_does_not_change_a_value_it_read
    role: EXPECTED
    field: text
    value: Balance 4
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: grounded_does_not_change_a_value_it_read
    role: EXPECTED
    field: stopped_by
    value: numbers_from_the_reading
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: grounded_does_not_change_a_value_it_read
    role: EXPECTED
    field: step
    value:
      position: 3
      candidates:
      - token: ' dollars'
        likelihood: 0.8
      - token: <end>
        likelihood: 0.1
      chosen: null
      stopped:
      - token: ' dollars'
        rule: numbers_from_the_reading
      - token: <end>
        rule: numbers_from_the_reading
      stopped_by: numbers_from_the_reading
      finished: false
      within_length: true
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: grounded_does_not_change_a_value_it_read
    role: EXPECTED
    field: finished
    value: false
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: grounded_does_not_change_a_value_it_read
    role: EXPECTED
    field: within_length
    value: true
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: ungrounded_writes_a_number_it_did_not_read
    role: INPUT
    field: state
    value:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
        rules_in_force:
          forbidden:
          - rule: no_guarantees
            pattern: \bguaranteed\b
          - rule: another_customers_account_number
            pattern: '[0-9](?:[ -]?[0-9]){7}'
            except:
            - '12345678'
          freedom: 0
          seed: 7
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
      position: 2
      text: 'Balance '
      finished: false
      limit: 3
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: ungrounded_writes_a_number_it_did_not_read
    role: INPUT
    field: candidates
    value:
    - token: '9'
      likelihood: 0.8
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: ungrounded_writes_a_number_it_did_not_read
    role: EXPECTED
    field: text
    value: Balance 9
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: ungrounded_writes_a_number_it_did_not_read
    role: EXPECTED
    field: stopped_by
    value: none
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: ungrounded_writes_a_number_it_did_not_read
    role: EXPECTED
    field: step
    value:
      position: 3
      candidates:
      - token: '9'
        likelihood: 0.8
      chosen: '9'
      stopped: []
      stopped_by: none
      finished: false
      within_length: true
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: ungrounded_writes_a_number_it_did_not_read
    role: EXPECTED
    field: finished
    value: false
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: ungrounded_writes_a_number_it_did_not_read
    role: EXPECTED
    field: within_length
    value: true
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: refuses_an_offer_for_a_complete_response
    role: INPUT
    field: state
    value:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
        rules_in_force:
          forbidden:
          - rule: no_guarantees
            pattern: \bguaranteed\b
          - rule: another_customers_account_number
            pattern: '[0-9](?:[ -]?[0-9]){7}'
            except:
            - '12345678'
          freedom: 0
          seed: 7
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
      position: 2
      text: Your balance
      finished: true
      limit: 3
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    case: refuses_an_offer_for_a_complete_response
    role: INPUT
    field: candidates
    value:
    - token: ' more'
      likelihood: 0.9
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_another_customers_account_and_continues
    role: INPUT
    field: candidates
    value:
    - word: '87654321'
      likelihood: 0.6
    - word: Your
      likelihood: 0.3
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_another_customers_account_and_continues
    role: INPUT
    field: rules_in_force
    value:
      forbidden:
      - rule: no_guarantees
        pattern: \bguaranteed\b
      - rule: another_customers_account_number
        pattern: '[0-9](?:[ -]?[0-9]){7}'
        except:
        - '12345678'
      freedom: 0
      seed: 7
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_another_customers_account_and_continues
    role: INPUT
    field: position
    value: 1
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_another_customers_account_and_continues
    role: INPUT
    field: text
    value: ''
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_another_customers_account_and_continues
    role: INPUT
    field: finished
    value: false
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_another_customers_account_and_continues
    role: INPUT
    field: stopped_by
    value: none
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_another_customers_account_and_continues
    role: INPUT
    field: stopped
    value: []
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_another_customers_account_and_continues
    role: EXPECTED
    field: text
    value: Your
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_another_customers_account_and_continues
    role: EXPECTED
    field: finished
    value: false
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_another_customers_account_and_continues
    role: EXPECTED
    field: stopped_by
    value: none
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_another_customers_account_and_continues
    role: EXPECTED
    field: stopped
    value:
    - position: 1
      word: '87654321'
      rule: another_customers_account_number
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_an_account_number_written_across_two_words
    role: INPUT
    field: candidates
    value:
    - word: '4321'
      likelihood: 0.7
    - word: is
      likelihood: 0.2
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_an_account_number_written_across_two_words
    role: INPUT
    field: rules_in_force
    value:
      forbidden:
      - rule: no_guarantees
        pattern: \bguaranteed\b
      - rule: another_customers_account_number
        pattern: '[0-9](?:[ -]?[0-9]){7}'
        except:
        - '12345678'
      freedom: 0
      seed: 7
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_an_account_number_written_across_two_words
    role: INPUT
    field: position
    value: 3
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_an_account_number_written_across_two_words
    role: INPUT
    field: text
    value: Account 8765
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_an_account_number_written_across_two_words
    role: INPUT
    field: finished
    value: false
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_an_account_number_written_across_two_words
    role: INPUT
    field: stopped_by
    value: none
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_an_account_number_written_across_two_words
    role: INPUT
    field: stopped
    value: []
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_an_account_number_written_across_two_words
    role: EXPECTED
    field: text
    value: Account 8765 is
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_an_account_number_written_across_two_words
    role: EXPECTED
    field: finished
    value: false
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_an_account_number_written_across_two_words
    role: EXPECTED
    field: stopped_by
    value: none
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: stops_an_account_number_written_across_two_words
    role: EXPECTED
    field: stopped
    value:
    - position: 3
      word: '4321'
      rule: another_customers_account_number
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: writes_the_customers_own_account_across_two_words
    role: INPUT
    field: candidates
    value:
    - word: '5678'
      likelihood: 0.8
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: writes_the_customers_own_account_across_two_words
    role: INPUT
    field: rules_in_force
    value:
      forbidden:
      - rule: no_guarantees
        pattern: \bguaranteed\b
      - rule: another_customers_account_number
        pattern: '[0-9](?:[ -]?[0-9]){7}'
        except:
        - '12345678'
      freedom: 0
      seed: 7
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: writes_the_customers_own_account_across_two_words
    role: INPUT
    field: position
    value: 3
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: writes_the_customers_own_account_across_two_words
    role: INPUT
    field: text
    value: Account 1234
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: writes_the_customers_own_account_across_two_words
    role: INPUT
    field: finished
    value: false
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: writes_the_customers_own_account_across_two_words
    role: INPUT
    field: stopped_by
    value: none
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: writes_the_customers_own_account_across_two_words
    role: INPUT
    field: stopped
    value: []
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: writes_the_customers_own_account_across_two_words
    role: EXPECTED
    field: text
    value: Account 1234 5678
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: writes_the_customers_own_account_across_two_words
    role: EXPECTED
    field: finished
    value: false
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: writes_the_customers_own_account_across_two_words
    role: EXPECTED
    field: stopped_by
    value: none
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: writes_the_customers_own_account_across_two_words
    role: EXPECTED
    field: stopped
    value: []
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: names_the_rule_when_no_permitted_word_remains
    role: INPUT
    field: candidates
    value:
    - word: '87654321'
      likelihood: 0.9
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: names_the_rule_when_no_permitted_word_remains
    role: INPUT
    field: rules_in_force
    value:
      forbidden:
      - rule: no_guarantees
        pattern: \bguaranteed\b
      - rule: another_customers_account_number
        pattern: '[0-9](?:[ -]?[0-9]){7}'
        except:
        - '12345678'
      freedom: 0
      seed: 7
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: names_the_rule_when_no_permitted_word_remains
    role: INPUT
    field: position
    value: 1
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: names_the_rule_when_no_permitted_word_remains
    role: INPUT
    field: text
    value: ''
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: names_the_rule_when_no_permitted_word_remains
    role: INPUT
    field: finished
    value: false
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: names_the_rule_when_no_permitted_word_remains
    role: INPUT
    field: stopped_by
    value: none
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: names_the_rule_when_no_permitted_word_remains
    role: INPUT
    field: stopped
    value: []
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: names_the_rule_when_no_permitted_word_remains
    role: EXPECTED
    field: text
    value: ''
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: names_the_rule_when_no_permitted_word_remains
    role: EXPECTED
    field: finished
    value: false
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: names_the_rule_when_no_permitted_word_remains
    role: EXPECTED
    field: stopped_by
    value: another_customers_account_number
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: names_the_rule_when_no_permitted_word_remains
    role: EXPECTED
    field: stopped
    value:
    - position: 1
      word: '87654321'
      rule: another_customers_account_number
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: draws_an_adventurous_word_from_the_seed
    role: INPUT
    field: candidates
    value:
    - word: balance
      likelihood: 0.6
    - word: savings
      likelihood: 0.3
    - word: loan
      likelihood: 0.1
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: draws_an_adventurous_word_from_the_seed
    role: INPUT
    field: rules_in_force
    value:
      forbidden:
      - rule: no_guarantees
        pattern: \bguaranteed\b
      - rule: another_customers_account_number
        pattern: '[0-9](?:[ -]?[0-9]){7}'
        except:
        - '12345678'
      freedom: 1
      seed: 7
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: draws_an_adventurous_word_from_the_seed
    role: INPUT
    field: position
    value: 2
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: draws_an_adventurous_word_from_the_seed
    role: INPUT
    field: text
    value: Your
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: draws_an_adventurous_word_from_the_seed
    role: INPUT
    field: finished
    value: false
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: draws_an_adventurous_word_from_the_seed
    role: INPUT
    field: stopped_by
    value: none
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: draws_an_adventurous_word_from_the_seed
    role: INPUT
    field: stopped
    value: []
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: draws_an_adventurous_word_from_the_seed
    role: EXPECTED
    field: text
    value: Your savings
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: draws_an_adventurous_word_from_the_seed
    role: EXPECTED
    field: finished
    value: false
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: draws_an_adventurous_word_from_the_seed
    role: EXPECTED
    field: stopped_by
    value: none
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: draws_an_adventurous_word_from_the_seed
    role: EXPECTED
    field: stopped
    value: []
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: finishes_on_the_end_of_the_response
    role: INPUT
    field: candidates
    value:
    - word: <end>
      likelihood: 0.9
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: finishes_on_the_end_of_the_response
    role: INPUT
    field: rules_in_force
    value:
      forbidden:
      - rule: no_guarantees
        pattern: \bguaranteed\b
      - rule: another_customers_account_number
        pattern: '[0-9](?:[ -]?[0-9]){7}'
        except:
        - '12345678'
      freedom: 0
      seed: 7
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: finishes_on_the_end_of_the_response
    role: INPUT
    field: position
    value: 3
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: finishes_on_the_end_of_the_response
    role: INPUT
    field: text
    value: Your balance
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: finishes_on_the_end_of_the_response
    role: INPUT
    field: finished
    value: false
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: finishes_on_the_end_of_the_response
    role: INPUT
    field: stopped_by
    value: none
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: finishes_on_the_end_of_the_response
    role: INPUT
    field: stopped
    value: []
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: finishes_on_the_end_of_the_response
    role: EXPECTED
    field: text
    value: Your balance
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: finishes_on_the_end_of_the_response
    role: EXPECTED
    field: finished
    value: true
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: finishes_on_the_end_of_the_response
    role: EXPECTED
    field: stopped_by
    value: none
  - ct_code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    case: finishes_on_the_end_of_the_response
    role: EXPECTED
    field: stopped
    value: []
  - ct_code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    case: admits_kind_within_ceiling
    role: INPUT
    field: kind
    value: internal
  - ct_code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    case: admits_kind_within_ceiling
    role: INPUT
    field: ceiling
    value: confidential
  - ct_code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    case: admits_kind_within_ceiling
    role: INPUT
    field: kinds
    value:
    - public
    - internal
    - confidential
    - restricted
  - ct_code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    case: admits_kind_within_ceiling
    role: EXPECTED
    field: within_ceiling
    value: true
  - ct_code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    case: refuses_kind_above_ceiling
    role: INPUT
    field: kind
    value: restricted
  - ct_code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    case: refuses_kind_above_ceiling
    role: INPUT
    field: ceiling
    value: internal
  - ct_code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    case: refuses_kind_above_ceiling
    role: INPUT
    field: kinds
    value:
    - public
    - internal
    - confidential
    - restricted
  - ct_code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    case: forms_key_from_description_and_fingerprint
    role: INPUT
    field: description
    value:
      reading_capacity: 64
      layers: 2
  - ct_code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    case: forms_key_from_description_and_fingerprint
    role: INPUT
    field: fingerprint
    value: sha256:ab12
  - ct_code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    case: forms_key_from_description_and_fingerprint
    role: EXPECTED
    field: identity_key
    value: '{"layers":2,"reading_capacity":64}|sha256:ab12'
  - ct_code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    case: refuses_blank_fingerprint
    role: INPUT
    field: description
    value:
      reading_capacity: 64
      layers: 2
  - ct_code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    case: refuses_blank_fingerprint
    role: INPUT
    field: fingerprint
    value: ' '
  - ct_code: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    case: adds_the_account_rule_and_positions
    role: INPUT
    field: response_rules
    value:
      forbidden:
      - rule: no_guarantees
        pattern: \bguaranteed\b
      account_number_pattern: '[0-9](?:[ -]?[0-9]){7}'
      freedom: 0
      longest_response: 3
  - ct_code: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    case: adds_the_account_rule_and_positions
    role: INPUT
    field: account_numbers
    value:
    - '12345678'
  - ct_code: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    case: adds_the_account_rule_and_positions
    role: INPUT
    field: seed
    value: 7
  - ct_code: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    case: adds_the_account_rule_and_positions
    role: EXPECTED
    field: rules_in_force
    value:
      forbidden:
      - rule: no_guarantees
        pattern: \bguaranteed\b
      - rule: another_customers_account_number
        pattern: '[0-9](?:[ -]?[0-9]){7}'
        except:
        - '12345678'
      freedom: 0
      seed: 7
  - ct_code: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    case: adds_the_account_rule_and_positions
    role: EXPECTED
    field: positions
    value:
    - 1
    - 2
    - 3
  - ct_code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
    case: reduces_the_trail_to_the_response_as_built
    role: INPUT
    field: entries
    value:
    - sequence_number: 1
      record:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
        rules_in_force:
          forbidden:
          - rule: no_guarantees
            pattern: \bguaranteed\b
          - rule: another_customers_account_number
            pattern: '[0-9](?:[ -]?[0-9]){7}'
            except:
            - '12345678'
          freedom: 0
          seed: 7
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
    - sequence_number: 2
      record:
        outcome: STEP
        chosen: Your
    - sequence_number: 3
      record:
        outcome: STEP
        chosen: ' balance'
  - ct_code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
    case: reduces_the_trail_to_the_response_as_built
    role: EXPECTED
    field: state
    value:
      opening:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
        rules_in_force:
          forbidden:
          - rule: no_guarantees
            pattern: \bguaranteed\b
          - rule: another_customers_account_number
            pattern: '[0-9](?:[ -]?[0-9]){7}'
            except:
            - '12345678'
          freedom: 0
          seed: 7
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
      position: 2
      text: Your balance
      finished: false
      limit: 3
  - ct_code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
    case: refuses_a_request_never_admitted
    role: INPUT
    field: entries
    value:
    - sequence_number: 1
      record:
        outcome: REFUSED
        reason: model_not_registered
  - ct_code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
    case: refuses_a_closed_request
    role: INPUT
    field: entries
    value:
    - sequence_number: 1
      record:
        outcome: WRITING
        fingerprint: fp-host
        reading:
          system_prompt: Answer only from the supporting material.
          question: What is my balance?
          supporting_material: Account 12345678 balance 40. Spouse account 87654321.
        rules_in_force:
          forbidden:
          - rule: no_guarantees
            pattern: \bguaranteed\b
          - rule: another_customers_account_number
            pattern: '[0-9](?:[ -]?[0-9]){7}'
            except:
            - '12345678'
          freedom: 0
          seed: 7
        ground_numbers: false
        maximum_response_length: 3
        longest_response: 5
    - sequence_number: 2
      record:
        outcome: RESPONDED
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    case: writes_one_permitted_word_from_a_recorded_offer
    role: INPUT
    field: reading
    value:
      system_prompt: Answer briefly.
      question: What is my balance?
      supporting_material: Account 12345678 balance 40.
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    case: writes_one_permitted_word_from_a_recorded_offer
    role: INPUT
    field: rules_in_force
    value:
      forbidden:
      - rule: no_guarantees
        pattern: \bguaranteed\b
      - rule: another_customers_account_number
        pattern: '[0-9](?:[ -]?[0-9]){7}'
        except:
        - '12345678'
      freedom: 0
      seed: 7
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    case: writes_one_permitted_word_from_a_recorded_offer
    role: INPUT
    field: position
    value: 1
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    case: writes_one_permitted_word_from_a_recorded_offer
    role: INPUT
    field: text
    value: ''
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    case: writes_one_permitted_word_from_a_recorded_offer
    role: INPUT
    field: finished
    value: false
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    case: writes_one_permitted_word_from_a_recorded_offer
    role: INPUT
    field: stopped_by
    value: none
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    case: writes_one_permitted_word_from_a_recorded_offer
    role: INPUT
    field: stopped
    value: []
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    case: writes_one_permitted_word_from_a_recorded_offer
    role: EXPECTED
    field: result
    value:
      text: Your
      finished: false
      stopped_by: none
      stopped:
      - position: 1
        word: '87654321'
        rule: another_customers_account_number
  - ct_code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    case: writes_one_permitted_word_from_a_recorded_offer
    role: RECORDED
    field: offered
    value:
      candidates:
      - word: '87654321'
        likelihood: 0.6
      - word: Your
        likelihood: 0.3
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    case: writes_a_finished_response_and_offers_nothing_after
    role: INPUT
    field: reading
    value:
      system_prompt: Answer briefly.
      question: What is my balance?
      supporting_material: Account 12345678 balance 40.
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    case: writes_a_finished_response_and_offers_nothing_after
    role: INPUT
    field: rules_in_force
    value:
      forbidden:
      - rule: no_guarantees
        pattern: \bguaranteed\b
      - rule: another_customers_account_number
        pattern: '[0-9](?:[ -]?[0-9]){7}'
        except:
        - '12345678'
      freedom: 0
      seed: 7
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    case: writes_a_finished_response_and_offers_nothing_after
    role: INPUT
    field: positions
    value:
    - 1
    - 2
    - 3
    - 4
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    case: writes_a_finished_response_and_offers_nothing_after
    role: EXPECTED
    field: result
    value:
      text: Your balance
      finished: true
      stopped_by: none
      stopped:
      - position: 1
        word: '87654321'
        rule: another_customers_account_number
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    case: writes_a_finished_response_and_offers_nothing_after
    role: RECORDED
    field: written[0]/offered
    value:
      candidates:
      - word: '87654321'
        likelihood: 0.6
      - word: Your
        likelihood: 0.3
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    case: writes_a_finished_response_and_offers_nothing_after
    role: RECORDED
    field: written[1]/offered
    value:
      candidates:
      - word: balance
        likelihood: 0.9
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    case: writes_a_finished_response_and_offers_nothing_after
    role: RECORDED
    field: written[2]/offered
    value:
      candidates:
      - word: <end>
        likelihood: 0.9
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    case: writes_a_finished_response_and_offers_nothing_after
    role: RECORDED
    field: written[3]/offered
    value:
      candidates: []
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    case: stops_unfinished_at_the_longest_response
    role: INPUT
    field: reading
    value:
      system_prompt: Answer briefly.
      question: What is my balance?
      supporting_material: Account 12345678 balance 40.
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    case: stops_unfinished_at_the_longest_response
    role: INPUT
    field: rules_in_force
    value:
      forbidden:
      - rule: no_guarantees
        pattern: \bguaranteed\b
      - rule: another_customers_account_number
        pattern: '[0-9](?:[ -]?[0-9]){7}'
        except:
        - '12345678'
      freedom: 0
      seed: 7
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    case: stops_unfinished_at_the_longest_response
    role: INPUT
    field: positions
    value:
    - 1
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    case: stops_unfinished_at_the_longest_response
    role: EXPECTED
    field: result
    value:
      text: Your
      finished: false
      stopped_by: none
      stopped: []
  - ct_code: causal_language_model::CT_WRITE_RESPONSE_V0
    case: stops_unfinished_at_the_longest_response
    role: RECORDED
    field: written[0]/offered
    value:
      candidates:
      - word: Your
        likelihood: 0.9
  generation_provenance: []
  artifact_summary:
  - action: NEW
    subdomain: model_response
    count: '58'
    artifacts: causal_language_model::AC_MODEL_HOST_V0, causal_language_model::AC_MODEL_STAFF_V0, causal_language_model::AC_REQUESTER_V0,
      causal_language_model::CC_ADMIT_USER_PROMPT_V0, causal_language_model::CC_APPEND_MODEL_OPERATION_V0,
      causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0, causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0,
      causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0, causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0,
      causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0, causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0,
      causal_language_model::CC_CONFIRM_READING_FITS_V0, causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0,
      causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0, causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0,
      causal_language_model::CC_OPEN_HOSTED_RECORD_V0, causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0,
      causal_language_model::CC_READ_HOSTED_STATE_V0, causal_language_model::CC_RECORD_HOSTED_STEP_V0,
      causal_language_model::CC_RECORD_USER_PROMPT_V0, causal_language_model::CC_REGISTER_MODEL_V0, causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0,
      causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0, causal_language_model::CC_WRITE_MODEL_RESPONSE_V0,
      causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0, causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0,
      causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0, causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0,
      causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0, causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0,
      causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0, causal_language_model::CT_PURE_READ_HOSTED_STATE_V0,
      causal_language_model::CT_WRITE_NEXT_WORD_V0, causal_language_model::CT_WRITE_RESPONSE_V0, causal_language_model::EV_MODEL_REGISTERED_V0,
      causal_language_model::EV_MODEL_SERVICE_ENDED_V0, causal_language_model::EV_MODEL_SERVICE_STARTED_V0,
      causal_language_model::EV_USER_PROMPT_REFUSED_V0, causal_language_model::EV_USER_PROMPT_RESPONDED_V0,
      causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0, causal_language_model::IN_OFFER_NEXT_TOKENS_V0,
      causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0, causal_language_model::IN_REGISTER_MODEL_V0,
      causal_language_model::IN_RELEASE_HOSTED_RESPONSE_V0, causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0,
      causal_language_model::IN_SUBMIT_USER_PROMPT_V0, causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0,
      causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0, causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0,
      causal_language_model::VOCAB_KIND_OF_INFORMATION_V0, causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0,
      causal_language_model::WF_OFFER_NEXT_TOKENS_V0, causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0,
      causal_language_model::WF_REGISTER_MODEL_V0, causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0,
      causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0, causal_language_model::WF_SUBMIT_USER_PROMPT_V0,
      causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
  refusal_discharge: []
  refusal_deferrals: []
  refusal_governance_discharge: []
  withdrawn_facts: null
```

The design of record of `causal_language_model`: every artifact its registry holds, stated in the design language.
Written by `python -m transformation.record` from the registry. Construction of this design and its
mandate reproduces the registry, and `construction_acceptance` asks whether it does. A change to
`causal_language_model` is a dossier designed against the composition.
