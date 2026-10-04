# WF_RETRIEVE_USER_PROMPT_RECORD_V0

## Machine

```yaml
fqdn: causal_language_model::WF_RETRIEVE_USER_PROMPT_RECORD_V0
artifact_kind: WORKFLOW
version: v0
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: model_response
runtime_binding: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
subdomain: model_response
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: Reading a user prompt record and recording that it was read
  actor_context: causal_language_model::AC_MODEL_STAFF_V0
  start_node: IN_RETRIEVE_USER_PROMPT_RECORD_V0
  nodes:
    IN_RETRIEVE_USER_PROMPT_RECORD_V0:
      type: IN
      code: IN_RETRIEVE_USER_PROMPT_RECORD_V0
      next:
        ACK: CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
        NACK: EXIT_REJECTED
    CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0:
      type: CC
      code: CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
      inputs:
        staff_credentials: $.payload.staff_credentials
        authorization_rules:
        - field: role
          op: eq
          value: model_staff
      next:
        SUCCESS: CC_APPEND_MODEL_OPERATION_V0
        VIOLATION: EXIT_REJECTED
    CC_APPEND_MODEL_OPERATION_V0:
      type: CC
      code: CC_APPEND_MODEL_OPERATION_V0
      inputs:
        staff_id: $.payload.staff_id
        operation: RETRIEVE_USER_PROMPT_RECORD
        record:
          operation: RETRIEVE_USER_PROMPT_RECORD
          staff_id: $.payload.staff_id
          subject: $.payload.user_prompt_id
      next:
        SUCCESS: CC_RETRIEVE_USER_PROMPT_RECORD_V0
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_RETRIEVE_USER_PROMPT_RECORD_V0:
      type: CC
      code: CC_RETRIEVE_USER_PROMPT_RECORD_V0
      inputs:
        user_prompt_id: $.payload.user_prompt_id
      next:
        SUCCESS: EXIT_RETRIEVED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    EXIT_RETRIEVED:
      type: EXIT
    EXIT_REJECTED:
      type: EXIT
```

---

## Intent

Reading a user prompt record and recording that it was read
