# Authoring Mandate — causal_language_model, baseline

## Machine

```yaml
document:
  phase: p8
  domain: causal_language_model
  subdomain:
  - model_response
  cr: baseline
  rule_set: transformation.schemas.REGISTER_SCHEMA_P8_V0
registers:
  build_order:
  - wave: '1'
    step: '1'
    code: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '2'
    code: causal_language_model::VOCAB_KIND_OF_INFORMATION_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '3'
    code: causal_language_model::AC_MODEL_HOST_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '4'
    code: causal_language_model::AC_MODEL_STAFF_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '5'
    code: causal_language_model::AC_REQUESTER_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '6'
    code: causal_language_model::EV_MODEL_REGISTERED_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '7'
    code: causal_language_model::EV_MODEL_SERVICE_ENDED_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '8'
    code: causal_language_model::EV_MODEL_SERVICE_STARTED_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '9'
    code: causal_language_model::EV_USER_PROMPT_REFUSED_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '10'
    code: causal_language_model::EV_USER_PROMPT_RESPONDED_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '11'
    code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '12'
    code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '13'
    code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '14'
    code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '15'
    code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '16'
    code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '17'
    code: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '18'
    code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '19'
    code: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '20'
    code: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '21'
    code: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '22'
    code: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '23'
    code: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '24'
    code: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '25'
    code: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '26'
    code: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '27'
    code: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '28'
    code: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '29'
    code: causal_language_model::CC_RECORD_USER_PROMPT_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '30'
    code: causal_language_model::CC_REGISTER_MODEL_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '31'
    code: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '32'
    code: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '33'
    code: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '34'
    code: causal_language_model::IN_OFFER_NEXT_TOKENS_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '35'
    code: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '36'
    code: causal_language_model::IN_REGISTER_MODEL_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '37'
    code: causal_language_model::IN_RELEASE_HOSTED_RESPONSE_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '38'
    code: causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '39'
    code: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '1'
    step: '40'
    code: causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0
    action: NEW
    subdomain: model_response
    depends_on: null
  - wave: '2'
    step: '41'
    code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    - causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
  - wave: '2'
    step: '42'
    code: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
  - wave: '2'
    step: '43'
    code: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
  - wave: '2'
    step: '44'
    code: causal_language_model::CC_CONFIRM_READING_FITS_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
  - wave: '2'
    step: '45'
    code: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
  - wave: '2'
    step: '46'
    code: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
  - wave: '2'
    step: '47'
    code: causal_language_model::CC_READ_HOSTED_STATE_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
  - wave: '2'
    step: '48'
    code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
  - wave: '3'
    step: '49'
    code: causal_language_model::CT_WRITE_RESPONSE_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - causal_language_model::CT_WRITE_NEXT_WORD_V0
  - wave: '3'
    step: '50'
    code: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    - causal_language_model::AC_MODEL_HOST_V0
    - causal_language_model::EV_USER_PROMPT_REFUSED_V0
    - causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
    - causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    - causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    - causal_language_model::CC_ADMIT_USER_PROMPT_V0
    - causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    - causal_language_model::CC_CONFIRM_READING_FITS_V0
    - causal_language_model::CC_OPEN_HOSTED_RECORD_V0
  - wave: '3'
    step: '51'
    code: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    - causal_language_model::AC_MODEL_HOST_V0
    - causal_language_model::EV_USER_PROMPT_REFUSED_V0
    - causal_language_model::IN_OFFER_NEXT_TOKENS_V0
    - causal_language_model::CC_READ_HOSTED_STATE_V0
    - causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
    - causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
    - causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
  - wave: '3'
    step: '52'
    code: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    - causal_language_model::AC_MODEL_STAFF_V0
    - causal_language_model::EV_MODEL_SERVICE_STARTED_V0
    - causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
    - causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    - causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    - causal_language_model::CC_APPEND_MODEL_OPERATION_V0
  - wave: '3'
    step: '53'
    code: causal_language_model::WF_REGISTER_MODEL_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    - causal_language_model::AC_MODEL_STAFF_V0
    - causal_language_model::EV_MODEL_REGISTERED_V0
    - causal_language_model::IN_REGISTER_MODEL_V0
    - causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    - causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    - causal_language_model::CC_REGISTER_MODEL_V0
    - causal_language_model::CC_APPEND_MODEL_OPERATION_V0
  - wave: '3'
    step: '54'
    code: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    - causal_language_model::AC_MODEL_HOST_V0
    - causal_language_model::EV_USER_PROMPT_RESPONDED_V0
    - causal_language_model::IN_RELEASE_HOSTED_RESPONSE_V0
    - causal_language_model::CC_READ_HOSTED_STATE_V0
  - wave: '3'
    step: '55'
    code: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    - causal_language_model::AC_MODEL_STAFF_V0
    - causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0
    - causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    - causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    - causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
  - wave: '3'
    step: '56'
    code: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    - causal_language_model::AC_MODEL_STAFF_V0
    - causal_language_model::EV_MODEL_SERVICE_ENDED_V0
    - causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0
    - causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    - causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    - causal_language_model::CC_APPEND_MODEL_OPERATION_V0
  - wave: '4'
    step: '57'
    code: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    - causal_language_model::CT_WRITE_RESPONSE_V0
  - wave: '5'
    step: '58'
    code: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    action: NEW
    subdomain: model_response
    depends_on:
    - causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    - causal_language_model::AC_REQUESTER_V0
    - causal_language_model::EV_USER_PROMPT_RESPONDED_V0
    - causal_language_model::EV_USER_PROMPT_REFUSED_V0
    - causal_language_model::IN_SUBMIT_USER_PROMPT_V0
    - causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    - causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    - causal_language_model::CC_ADMIT_USER_PROMPT_V0
    - causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    - causal_language_model::CC_CONFIRM_READING_FITS_V0
    - causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
  critical_path:
  - position: '1'
    code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
  - position: '2'
    code: causal_language_model::CT_WRITE_NEXT_WORD_V0
  - position: '3'
    code: causal_language_model::CT_WRITE_RESPONSE_V0
  - position: '4'
    code: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
  - position: '5'
    code: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
  mandate_artifact_summary:
  - action: NEW
    count: '58'
    description: 1 STRUCTURE, 1 VOCAB, 3 AC, 5 EV, 10 CT, 21 CC, 8 IN, 8 WF, 1 RB
  field_declarations:
  - code: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    subdomain_field: model_response
  - code: causal_language_model::VOCAB_KIND_OF_INFORMATION_V0
    subdomain_field: model_response
  - code: causal_language_model::AC_MODEL_HOST_V0
    subdomain_field: model_response
  - code: causal_language_model::AC_MODEL_STAFF_V0
    subdomain_field: model_response
  - code: causal_language_model::AC_REQUESTER_V0
    subdomain_field: model_response
  - code: causal_language_model::EV_MODEL_REGISTERED_V0
    subdomain_field: model_response
  - code: causal_language_model::EV_MODEL_SERVICE_ENDED_V0
    subdomain_field: model_response
  - code: causal_language_model::EV_MODEL_SERVICE_STARTED_V0
    subdomain_field: model_response
  - code: causal_language_model::EV_USER_PROMPT_REFUSED_V0
    subdomain_field: model_response
  - code: causal_language_model::EV_USER_PROMPT_RESPONDED_V0
    subdomain_field: model_response
  - code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    subdomain_field: model_response
  - code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    subdomain_field: model_response
  - code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    subdomain_field: model_response
  - code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    subdomain_field: model_response
  - code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    subdomain_field: model_response
  - code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    subdomain_field: model_response
  - code: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    subdomain_field: model_response
  - code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_CONFIRM_OFFER_FOR_MODEL_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_RECORD_HOSTED_STEP_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_RECORD_USER_PROMPT_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_REGISTER_MODEL_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    subdomain_field: model_response
  - code: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
    subdomain_field: model_response
  - code: causal_language_model::IN_OFFER_NEXT_TOKENS_V0
    subdomain_field: model_response
  - code: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
    subdomain_field: model_response
  - code: causal_language_model::IN_REGISTER_MODEL_V0
    subdomain_field: model_response
  - code: causal_language_model::IN_RELEASE_HOSTED_RESPONSE_V0
    subdomain_field: model_response
  - code: causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0
    subdomain_field: model_response
  - code: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
    subdomain_field: model_response
  - code: causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0
    subdomain_field: model_response
  - code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_CONFIRM_READING_FITS_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_READ_HOSTED_STATE_V0
    subdomain_field: model_response
  - code: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
    subdomain_field: model_response
  - code: causal_language_model::CT_WRITE_RESPONSE_V0
    subdomain_field: model_response
  - code: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
    subdomain_field: model_response
  - code: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    subdomain_field: model_response
  - code: causal_language_model::WF_PLACE_MODEL_IN_SERVICE_V0
    subdomain_field: model_response
  - code: causal_language_model::WF_REGISTER_MODEL_V0
    subdomain_field: model_response
  - code: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
    subdomain_field: model_response
  - code: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
    subdomain_field: model_response
  - code: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    subdomain_field: model_response
  - code: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
    subdomain_field: model_response
  - code: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    subdomain_field: model_response
  new_capabilities:
  - code: causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0
    purpose: 'The model''s step: offers its next words given the response so far; the one step whose result
      is not determined by its inputs'
    inputs: reading:object, text:string, finished:boolean, stopped_by:string
    outputs: candidates:array
  - code: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    purpose: Assembles exactly what the model reads and decides whether it fits what the model can read
      at once
    inputs: system_prompt:string, question:string, supporting_material:string, reading_capacity:integer
    outputs: reading:object, reading_length:integer
  - code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    purpose: Stops forbidden tokens among those offered and chooses one permitted token, joined as it
      is, within the permitted length
    inputs: state:object, candidates:array
    outputs: step:object, text:string, finished:boolean, stopped_by:string, within_length:boolean
  - code: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    purpose: Stops forbidden words among those offered and chooses one permitted word under the freedom
      of word choice and a stated seed
    inputs: candidates:array, rules_in_force:object, position:integer, text:string, finished:boolean,
      stopped_by:string, stopped:array
    outputs: text:string, finished:boolean, stopped_by:string, stopped:array
  - code: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    purpose: Decides whether a kind of information is no more sensitive than a ceiling, by the declared
      order
    inputs: kind:string, ceiling:string, kinds:array
    outputs: within_ceiling:boolean
  - code: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    purpose: Forms the single key claimed for a model from its description and fingerprint
    inputs: description:object, fingerprint:string
    outputs: identity_key:string
  - code: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    purpose: Forms the response rules in force for one user prompt from the time in service and the customer's
      account numbers
    inputs: response_rules:object, account_numbers:array, seed:integer
    outputs: rules_in_force:object, positions:array
  - code: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
    purpose: Reduces a hosted request's trail to the response as built, its position, whether it is complete,
      and its permitted length
    inputs: entries:array
    outputs: state:object
  - code: causal_language_model::CT_WRITE_NEXT_WORD_V0
    purpose: One pass of writing, composed of the model's offer and the rules' choice
    inputs: reading:object, rules_in_force:object, position:integer, text:string, finished:boolean, stopped_by:string,
      stopped:array
    outputs: result:object
  - code: causal_language_model::CT_WRITE_RESPONSE_V0
    purpose: Writes a response by repeating one pass per word, up to the longest response, carrying the
      response so far and the words stopped
    inputs: reading:object, rules_in_force:object, positions:array
    outputs: result:object
  new_intents:
  - code: causal_language_model::IN_BEGIN_HOSTED_RESPONSE_V0
    purpose: A request to a hosted model on behalf of a customer
    workflow: WF_BEGIN_HOSTED_RESPONSE_V0
    inputs: user_prompt_id:string, requester_id:string, permitted_customers:array, customer_id:string,
      account_numbers:array, identity_key:string, kind:string, question:string, supporting_material:string,
      seed:integer
  - code: causal_language_model::IN_OFFER_NEXT_TOKENS_V0
    purpose: The candidates a hosted model could write next, naming its fingerprint and the size of what
      it reads
    workflow: WF_OFFER_NEXT_TOKENS_V0
    inputs: user_prompt_id:string, host_id:string, fingerprint:string, reported_reading_size:integer,
      candidates:array
  - code: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
    purpose: A request to place a registered model in service with its ceiling, system prompt and response
      rules
    workflow: WF_PLACE_MODEL_IN_SERVICE_V0
    inputs: staff_credentials:object, staff_id:string, identity_key:string, time_in_service_id:string,
      ceiling:string, system_prompt:string, response_rules:object
  - code: causal_language_model::IN_REGISTER_MODEL_V0
    purpose: A request to register a model with its description and fingerprint
    workflow: WF_REGISTER_MODEL_V0
    inputs: staff_credentials:object, staff_id:string, description:object, fingerprint:string
  - code: causal_language_model::IN_RELEASE_HOSTED_RESPONSE_V0
    purpose: A request to release a completed hosted response
    workflow: WF_RELEASE_HOSTED_RESPONSE_V0
    inputs: user_prompt_id:string, host_id:string
  - code: causal_language_model::IN_RETRIEVE_USER_PROMPT_RECORD_V0
    purpose: A request to retrieve the record of a user prompt
    workflow: WF_RETRIEVE_USER_PROMPT_RECORD_V0
    inputs: staff_credentials:object, staff_id:string, user_prompt_id:string
  - code: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
    purpose: A user prompt submitted on behalf of a customer
    workflow: WF_SUBMIT_USER_PROMPT_V0
    inputs: user_prompt_id:string, requester_id:string, permitted_customers:array, customer_id:string,
      account_numbers:array, identity_key:string, kind:string, question:string, supporting_material:string,
      seed:integer
  - code: causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0
    purpose: A request to withdraw a model from service
    workflow: WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    inputs: staff_credentials:object, staff_id:string, identity_key:string
  cross_subdomain_notes: []
```

The 58 artifacts of `causal_language_model`'s design of record, scheduled in dependency order. Written by
`python -m transformation.record` from the P7 beside it. The mandate orders the build; it decides
nothing.
