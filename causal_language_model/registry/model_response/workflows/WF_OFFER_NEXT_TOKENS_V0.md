# WF_OFFER_NEXT_TOKENS_V0

## Machine

```yaml
fqdn: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
artifact_kind: WORKFLOW
version: v0
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: model_response
runtime_binding: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
subdomain: model_response
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: Choosing a permitted token from an offer and recording the step, or refusing the request
  actor_context: causal_language_model::AC_MODEL_HOST_V0
  start_node: IN_OFFER_NEXT_TOKENS_V0
  nodes:
    IN_OFFER_NEXT_TOKENS_V0:
      type: IN
      code: IN_OFFER_NEXT_TOKENS_V0
      next:
        ACK: CC_READ_HOSTED_STATE_V0
        NACK: EXIT_REJECTED
    CC_READ_HOSTED_STATE_V0:
      type: CC
      code: CC_READ_HOSTED_STATE_V0
      inputs:
        user_prompt_id: $.payload.user_prompt_id
      next:
        SUCCESS: CC_CONFIRM_OFFER_FOR_MODEL_V0
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_CONFIRM_OFFER_FOR_MODEL_V0:
      type: CC
      code: CC_CONFIRM_OFFER_FOR_MODEL_V0
      inputs:
        offered_fingerprint: $.payload.fingerprint
        admitted_fingerprint: $.results.CC_READ_HOSTED_STATE_V0.state.opening.fingerprint
      next:
        SUCCESS: CC_CONFIRM_HOSTED_READING_FITS_V0
        VIOLATION: RECORD_REFUSED_OTHER_MODEL
    CC_CONFIRM_HOSTED_READING_FITS_V0:
      type: CC
      code: CC_CONFIRM_HOSTED_READING_FITS_V0
      inputs:
        reported_reading_size: $.payload.reported_reading_size
        reading_capacity: $.results.CC_READ_HOSTED_STATE_V0.state.opening.reading_capacity
      next:
        SUCCESS: CC_CHOOSE_PERMITTED_TOKEN_V0
        VIOLATION: RECORD_REFUSED_TOO_LONG_TO_READ
    CC_CHOOSE_PERMITTED_TOKEN_V0:
      type: CC
      code: CC_CHOOSE_PERMITTED_TOKEN_V0
      inputs:
        state: $.results.CC_READ_HOSTED_STATE_V0.state
        candidates: $.payload.candidates
      next:
        SUCCESS: CONFIRM_NO_RULE_STOPPED
        VIOLATION: EXIT_REJECTED
    CONFIRM_NO_RULE_STOPPED:
      type: CC
      code: CC_CONFIRM_RESPONSE_RELEASABLE_V0
      inputs:
        release_facts:
          stopped_by: $.results.CC_CHOOSE_PERMITTED_TOKEN_V0.stopped_by
        release_rules:
        - field: stopped_by
          op: eq
          value: none
      next:
        SUCCESS: CONFIRM_WITHIN_LENGTH
        VIOLATION: RECORD_STOPPED_STEP
    CONFIRM_WITHIN_LENGTH:
      type: CC
      code: CC_CONFIRM_RESPONSE_RELEASABLE_V0
      inputs:
        release_facts:
          within_length: $.results.CC_CHOOSE_PERMITTED_TOKEN_V0.within_length
        release_rules:
        - field: within_length
          op: eq
          value: true
      next:
        SUCCESS: RECORD_STEP
        VIOLATION: RECORD_UNFINISHED_STEP
    RECORD_STEP:
      type: CC
      code: CC_RECORD_HOSTED_STEP_V0
      inputs:
        user_prompt_id: $.payload.user_prompt_id
        host_id: $.payload.host_id
        fingerprint: $.payload.fingerprint
        reported_reading_size: $.payload.reported_reading_size
        step: $.results.CC_CHOOSE_PERMITTED_TOKEN_V0.step
      next:
        SUCCESS: EXIT_CHOSEN
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    RECORD_STOPPED_STEP:
      type: CC
      code: CC_RECORD_HOSTED_STEP_V0
      inputs:
        user_prompt_id: $.payload.user_prompt_id
        host_id: $.payload.host_id
        fingerprint: $.payload.fingerprint
        reported_reading_size: $.payload.reported_reading_size
        step: $.results.CC_CHOOSE_PERMITTED_TOKEN_V0.step
      next:
        SUCCESS: RECORD_REFUSED_BY_RULE
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    RECORD_UNFINISHED_STEP:
      type: CC
      code: CC_RECORD_HOSTED_STEP_V0
      inputs:
        user_prompt_id: $.payload.user_prompt_id
        host_id: $.payload.host_id
        fingerprint: $.payload.fingerprint
        reported_reading_size: $.payload.reported_reading_size
        step: $.results.CC_CHOOSE_PERMITTED_TOKEN_V0.step
      next:
        SUCCESS: RECORD_REFUSED_UNFINISHED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    RECORD_REFUSED_OTHER_MODEL:
      type: CC
      code: CC_RECORD_USER_PROMPT_V0
      inputs:
        user_prompt_id: $.payload.user_prompt_id
        requester_id: $.results.CC_READ_HOSTED_STATE_V0.state.opening.requester_id
        customer_id: $.results.CC_READ_HOSTED_STATE_V0.state.opening.customer_id
        identity_key: $.results.CC_READ_HOSTED_STATE_V0.state.opening.identity_key
        kind: $.results.CC_READ_HOSTED_STATE_V0.state.opening.kind
        question: $.results.CC_READ_HOSTED_STATE_V0.state.opening.question
        supporting_material: $.results.CC_READ_HOSTED_STATE_V0.state.opening.supporting_material
        time_in_service_id: $.results.CC_READ_HOSTED_STATE_V0.state.opening.time_in_service_id
        reading: $.results.CC_READ_HOSTED_STATE_V0.state.opening.reading
        rules_in_force: $.results.CC_READ_HOSTED_STATE_V0.state.opening.rules_in_force
        outcome: REFUSED
        reason: offer_for_another_model
      next:
        SUCCESS: EXIT_REFUSED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    RECORD_REFUSED_TOO_LONG_TO_READ:
      type: CC
      code: CC_RECORD_USER_PROMPT_V0
      inputs:
        user_prompt_id: $.payload.user_prompt_id
        requester_id: $.results.CC_READ_HOSTED_STATE_V0.state.opening.requester_id
        customer_id: $.results.CC_READ_HOSTED_STATE_V0.state.opening.customer_id
        identity_key: $.results.CC_READ_HOSTED_STATE_V0.state.opening.identity_key
        kind: $.results.CC_READ_HOSTED_STATE_V0.state.opening.kind
        question: $.results.CC_READ_HOSTED_STATE_V0.state.opening.question
        supporting_material: $.results.CC_READ_HOSTED_STATE_V0.state.opening.supporting_material
        time_in_service_id: $.results.CC_READ_HOSTED_STATE_V0.state.opening.time_in_service_id
        reading: $.results.CC_READ_HOSTED_STATE_V0.state.opening.reading
        rules_in_force: $.results.CC_READ_HOSTED_STATE_V0.state.opening.rules_in_force
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
        requester_id: $.results.CC_READ_HOSTED_STATE_V0.state.opening.requester_id
        customer_id: $.results.CC_READ_HOSTED_STATE_V0.state.opening.customer_id
        identity_key: $.results.CC_READ_HOSTED_STATE_V0.state.opening.identity_key
        kind: $.results.CC_READ_HOSTED_STATE_V0.state.opening.kind
        question: $.results.CC_READ_HOSTED_STATE_V0.state.opening.question
        supporting_material: $.results.CC_READ_HOSTED_STATE_V0.state.opening.supporting_material
        time_in_service_id: $.results.CC_READ_HOSTED_STATE_V0.state.opening.time_in_service_id
        reading: $.results.CC_READ_HOSTED_STATE_V0.state.opening.reading
        rules_in_force: $.results.CC_READ_HOSTED_STATE_V0.state.opening.rules_in_force
        outcome: REFUSED
        reason: $.results.CC_CHOOSE_PERMITTED_TOKEN_V0.stopped_by
      next:
        SUCCESS: EXIT_REFUSED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    RECORD_REFUSED_UNFINISHED:
      type: CC
      code: CC_RECORD_USER_PROMPT_V0
      inputs:
        user_prompt_id: $.payload.user_prompt_id
        requester_id: $.results.CC_READ_HOSTED_STATE_V0.state.opening.requester_id
        customer_id: $.results.CC_READ_HOSTED_STATE_V0.state.opening.customer_id
        identity_key: $.results.CC_READ_HOSTED_STATE_V0.state.opening.identity_key
        kind: $.results.CC_READ_HOSTED_STATE_V0.state.opening.kind
        question: $.results.CC_READ_HOSTED_STATE_V0.state.opening.question
        supporting_material: $.results.CC_READ_HOSTED_STATE_V0.state.opening.supporting_material
        time_in_service_id: $.results.CC_READ_HOSTED_STATE_V0.state.opening.time_in_service_id
        reading: $.results.CC_READ_HOSTED_STATE_V0.state.opening.reading
        rules_in_force: $.results.CC_READ_HOSTED_STATE_V0.state.opening.rules_in_force
        outcome: REFUSED
        reason: longest_response_reached
      next:
        SUCCESS: EXIT_REFUSED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    EXIT_CHOSEN:
      type: EXIT
    EXIT_REFUSED:
      type: EXIT
      emit: causal_language_model::EV_USER_PROMPT_REFUSED_V0
    EXIT_REJECTED:
      type: EXIT
```

---

## Intent

Choosing a permitted token from an offer and recording the step, or refusing the request
