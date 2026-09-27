# WF_SUBMIT_USER_PROMPT_V0

## Machine

```yaml
fqdn: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
artifact_kind: WORKFLOW
version: v0
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: model_response
runtime_binding: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
subdomain: model_response
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: Admitting a user prompt, writing the response under the rules, releasing or refusing it, and
    recording it
  actor_context: causal_language_model::AC_MODEL_STAFF_V0
  start_node: IN_SUBMIT_USER_PROMPT_V0
  nodes:
    IN_SUBMIT_USER_PROMPT_V0:
      type: IN
      code: IN_SUBMIT_USER_PROMPT_V0
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
        BACKEND_ERROR: RECORD_FAILED_BEFORE_READING
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
        BACKEND_ERROR: RECORD_FAILED_BEFORE_READING
    CC_CONFIRM_READING_FITS_V0:
      type: CC
      code: CC_CONFIRM_READING_FITS_V0
      inputs:
        system_prompt: $.results.CC_CONFIRM_WITHIN_CEILING_V0.time_in_service.system_prompt
        question: $.payload.question
        supporting_material: $.payload.supporting_material
        reading_capacity: $.results.CC_ADMIT_USER_PROMPT_V0.model_record.description.reading_capacity
      next:
        SUCCESS: CC_WRITE_MODEL_RESPONSE_V0
        VIOLATION: RECORD_REFUSED_TOO_LONG_TO_READ
    CC_WRITE_MODEL_RESPONSE_V0:
      type: CC
      code: CC_WRITE_MODEL_RESPONSE_V0
      inputs:
        response_rules: $.results.CC_CONFIRM_WITHIN_CEILING_V0.time_in_service.response_rules
        account_numbers: $.payload.account_numbers
        seed: $.payload.seed
        reading: $.results.CC_CONFIRM_READING_FITS_V0.reading
      next:
        SUCCESS: CONFIRM_NO_RULE_STOPPED
        VIOLATION: RECORD_FAILED_WHILE_WRITING
    CONFIRM_NO_RULE_STOPPED:
      type: CC
      code: CC_CONFIRM_RESPONSE_RELEASABLE_V0
      inputs:
        release_facts:
          stopped_by: $.results.CC_WRITE_MODEL_RESPONSE_V0.written_response.stopped_by
        release_rules:
        - field: stopped_by
          op: eq
          value: none
      next:
        SUCCESS: CONFIRM_FINISHED
        VIOLATION: RECORD_REFUSED_BY_RULE
    CONFIRM_FINISHED:
      type: CC
      code: CC_CONFIRM_RESPONSE_RELEASABLE_V0
      inputs:
        release_facts:
          finished: $.results.CC_WRITE_MODEL_RESPONSE_V0.written_response.finished
        release_rules:
        - field: finished
          op: eq
          value: true
      next:
        SUCCESS: RECORD_RESPONDED
        VIOLATION: RECORD_REFUSED_UNFINISHED
    RECORD_RESPONDED:
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
        reading: $.results.CC_CONFIRM_READING_FITS_V0.reading
        rules_in_force: $.results.CC_WRITE_MODEL_RESPONSE_V0.rules_in_force
        response: $.results.CC_WRITE_MODEL_RESPONSE_V0.written_response.text
        outcome: RESPONDED
      next:
        SUCCESS: EXIT_RESPONDED
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
    RECORD_REFUSED_BY_RULE:
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
        reading: $.results.CC_CONFIRM_READING_FITS_V0.reading
        rules_in_force: $.results.CC_WRITE_MODEL_RESPONSE_V0.rules_in_force
        outcome: REFUSED
        reason: $.results.CC_WRITE_MODEL_RESPONSE_V0.written_response.stopped_by
      next:
        SUCCESS: EXIT_REFUSED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    RECORD_REFUSED_UNFINISHED:
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
        reading: $.results.CC_CONFIRM_READING_FITS_V0.reading
        rules_in_force: $.results.CC_WRITE_MODEL_RESPONSE_V0.rules_in_force
        outcome: REFUSED
        reason: longest_response_reached
      next:
        SUCCESS: EXIT_REFUSED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    RECORD_FAILED_BEFORE_READING:
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
        outcome: FAILED
        reason: store_failed_before_the_model_read
      next:
        SUCCESS: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    RECORD_FAILED_WHILE_WRITING:
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
        reading: $.results.CC_CONFIRM_READING_FITS_V0.reading
        outcome: FAILED
        reason: writing_failed
      next:
        SUCCESS: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    EXIT_RESPONDED:
      type: EXIT
      emit: causal_language_model::EV_USER_PROMPT_RESPONDED_V0
    EXIT_REFUSED:
      type: EXIT
      emit: causal_language_model::EV_USER_PROMPT_REFUSED_V0
    EXIT_REJECTED:
      type: EXIT
```

---

## Intent

Admitting a user prompt, writing the response under the rules, releasing or refusing it, and recording it
