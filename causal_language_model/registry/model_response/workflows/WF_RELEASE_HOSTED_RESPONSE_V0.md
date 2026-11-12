# WF_RELEASE_HOSTED_RESPONSE_V0

## Machine

```yaml
fqdn: causal_language_model::WF_RELEASE_HOSTED_RESPONSE_V0
artifact_kind: WORKFLOW
version: v0
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: model_response
runtime_binding: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
subdomain: model_response
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: Releasing a completed hosted response from the record
  actor_context: causal_language_model::AC_MODEL_HOST_V0
  start_node: IN_RELEASE_HOSTED_RESPONSE_V0
  nodes:
    IN_RELEASE_HOSTED_RESPONSE_V0:
      type: IN
      code: IN_RELEASE_HOSTED_RESPONSE_V0
      next:
        ACK: CC_READ_HOSTED_STATE_V0
        NACK: EXIT_REJECTED
    CC_READ_HOSTED_STATE_V0:
      type: CC
      code: CC_READ_HOSTED_STATE_V0
      inputs:
        user_prompt_id: $.payload.user_prompt_id
      next:
        SUCCESS: CONFIRM_FINISHED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CONFIRM_FINISHED:
      type: CC
      code: CC_CONFIRM_RESPONSE_RELEASABLE_V0
      inputs:
        release_facts:
          finished: $.results.CC_READ_HOSTED_STATE_V0.state.finished
        release_rules:
        - field: finished
          op: eq
          value: true
      next:
        SUCCESS: RECORD_RESPONDED
        VIOLATION: EXIT_REJECTED
    RECORD_RESPONDED:
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
        outcome: RESPONDED
        response: $.results.CC_READ_HOSTED_STATE_V0.state.text
      next:
        SUCCESS: EXIT_RESPONDED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    EXIT_RESPONDED:
      type: EXIT
      emit: causal_language_model::EV_USER_PROMPT_RESPONDED_V0
    EXIT_REJECTED:
      type: EXIT
```

---

## Intent

Releasing a completed hosted response from the record
