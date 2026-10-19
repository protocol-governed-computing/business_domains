# WF_BEGIN_HOSTED_RESPONSE_V0

## Machine

```yaml
fqdn: causal_language_model::WF_BEGIN_HOSTED_RESPONSE_V0
artifact_kind: WORKFLOW
version: v0
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: model_response
runtime_binding: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
subdomain: model_response
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: Admitting a hosted request and opening its record, or refusing it
  actor_context: causal_language_model::AC_MODEL_HOST_V0
  start_node: IN_BEGIN_HOSTED_RESPONSE_V0
  nodes:
    IN_BEGIN_HOSTED_RESPONSE_V0:
      type: IN
      code: IN_BEGIN_HOSTED_RESPONSE_V0
      next:
        ACK: CC_CLAIM_USER_PROMPT_IDENTITY_V0
        NACK: EXIT_REJECTED
    CC_CLAIM_USER_PROMPT_IDENTITY_V0:
      type: CC
      code: CC_CLAIM_USER_PROMPT_IDENTITY_V0
      inputs:
        user_prompt_id: $.payload.user_prompt_id
      next:
        SUCCESS: CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
        ALREADY_EXISTS: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0:
      type: CC
      code: CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
      inputs:
        customer_id: $.payload.customer_id
        permitted_customers: $.payload.permitted_customers
      next:
        SUCCESS: CC_ADMIT_USER_PROMPT_V0
        VIOLATION: RECORD_REFUSED_NOT_PERMITTED
    CC_ADMIT_USER_PROMPT_V0:
      type: CC
      code: CC_ADMIT_USER_PROMPT_V0
      inputs:
        identity_key: $.payload.identity_key
      next:
        SUCCESS: CC_CONFIRM_WITHIN_CEILING_V0
        NOT_FOUND: RECORD_REFUSED_NOT_REGISTERED
        VIOLATION: RECORD_REFUSED_NOT_IN_SERVICE
        BACKEND_ERROR: EXIT_REJECTED
    CC_CONFIRM_WITHIN_CEILING_V0:
      type: CC
      code: CC_CONFIRM_WITHIN_CEILING_V0
      inputs:
        time_in_service_id: $.results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
        kind: $.payload.kind
      next:
        SUCCESS: CC_CONFIRM_READING_FITS_V0
        NOT_FOUND: RECORD_REFUSED_NOT_IN_SERVICE
        VIOLATION: RECORD_REFUSED_ABOVE_CEILING
        BACKEND_ERROR: EXIT_REJECTED
    CC_CONFIRM_READING_FITS_V0:
      type: CC
      code: CC_CONFIRM_READING_FITS_V0
      inputs:
        system_prompt: $.results.CC_CONFIRM_WITHIN_CEILING_V0.time_in_service.system_prompt
        question: $.payload.question
        supporting_material: $.payload.supporting_material
        reading_capacity: $.results.CC_ADMIT_USER_PROMPT_V0.model_record.description.reading_capacity
      next:
        SUCCESS: CC_OPEN_HOSTED_RECORD_V0
        VIOLATION: RECORD_REFUSED_TOO_LONG_TO_READ
    CC_OPEN_HOSTED_RECORD_V0:
      type: CC
      code: CC_OPEN_HOSTED_RECORD_V0
      inputs:
        user_prompt_id: $.payload.user_prompt_id
        requester_id: $.payload.requester_id
        customer_id: $.payload.customer_id
        identity_key: $.payload.identity_key
        kind: $.payload.kind
        question: $.payload.question
        supporting_material: $.payload.supporting_material
        account_numbers: $.payload.account_numbers
        seed: $.payload.seed
        time_in_service_id: $.results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
        reading: $.results.CC_CONFIRM_READING_FITS_V0.reading
        response_rules: $.results.CC_CONFIRM_WITHIN_CEILING_V0.time_in_service.response_rules
        fingerprint: $.results.CC_ADMIT_USER_PROMPT_V0.model_record.fingerprint
        reading_capacity: $.results.CC_ADMIT_USER_PROMPT_V0.model_record.description.reading_capacity
        maximum_response_length: $.results.CC_ADMIT_USER_PROMPT_V0.model_record.description.maximum_response_length
      next:
        SUCCESS: EXIT_WRITING
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    RECORD_REFUSED_NOT_PERMITTED:
      type: CC
      code: CC_RECORD_USER_PROMPT_V0
      inputs:
        user_prompt_id: $.payload.user_prompt_id
        requester_id: $.payload.requester_id
        customer_id: $.payload.customer_id
        identity_key: $.payload.identity_key
        kind: $.payload.kind
        question: $.payload.question
        supporting_material: $.payload.supporting_material
        outcome: REFUSED
        reason: requester_not_permitted_for_customer
      next:
        SUCCESS: EXIT_REFUSED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    RECORD_REFUSED_NOT_REGISTERED:
      type: CC
      code: CC_RECORD_USER_PROMPT_V0
      inputs:
        user_prompt_id: $.payload.user_prompt_id
        requester_id: $.payload.requester_id
        customer_id: $.payload.customer_id
        identity_key: $.payload.identity_key
        kind: $.payload.kind
        question: $.payload.question
        supporting_material: $.payload.supporting_material
        outcome: REFUSED
        reason: model_not_registered
      next:
        SUCCESS: EXIT_REFUSED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    RECORD_REFUSED_NOT_IN_SERVICE:
      type: CC
      code: CC_RECORD_USER_PROMPT_V0
      inputs:
        user_prompt_id: $.payload.user_prompt_id
        requester_id: $.payload.requester_id
        customer_id: $.payload.customer_id
        identity_key: $.payload.identity_key
        kind: $.payload.kind
        question: $.payload.question
        supporting_material: $.payload.supporting_material
        outcome: REFUSED
        reason: model_not_in_service
      next:
        SUCCESS: EXIT_REFUSED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    RECORD_REFUSED_ABOVE_CEILING:
      type: CC
      code: CC_RECORD_USER_PROMPT_V0
      inputs:
        user_prompt_id: $.payload.user_prompt_id
        requester_id: $.payload.requester_id
        customer_id: $.payload.customer_id
        identity_key: $.payload.identity_key
        kind: $.payload.kind
        question: $.payload.question
        supporting_material: $.payload.supporting_material
        time_in_service_id: $.results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
        outcome: REFUSED
        reason: kind_above_sensitivity_ceiling
      next:
        SUCCESS: EXIT_REFUSED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    RECORD_REFUSED_TOO_LONG_TO_READ:
      type: CC
      code: CC_RECORD_USER_PROMPT_V0
      inputs:
        user_prompt_id: $.payload.user_prompt_id
        requester_id: $.payload.requester_id
        customer_id: $.payload.customer_id
        identity_key: $.payload.identity_key
        kind: $.payload.kind
        question: $.payload.question
        supporting_material: $.payload.supporting_material
        time_in_service_id: $.results.CC_ADMIT_USER_PROMPT_V0.model_record.time_in_service_id
        outcome: REFUSED
        reason: reading_longer_than_model_can_read
      next:
        SUCCESS: EXIT_REFUSED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    EXIT_WRITING:
      type: EXIT
    EXIT_REFUSED:
      type: EXIT
      emit: causal_language_model::EV_USER_PROMPT_REFUSED_V0
    EXIT_REJECTED:
      type: EXIT
```

---

## Intent

Admitting a hosted request and opening its record, or refusing it
