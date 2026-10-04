# WF_WITHDRAW_MODEL_FROM_SERVICE_V0

## Machine

```yaml
fqdn: causal_language_model::WF_WITHDRAW_MODEL_FROM_SERVICE_V0
artifact_kind: WORKFLOW
version: v0
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: model_response
runtime_binding: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
subdomain: model_response
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: Closing a model's time in service
  actor_context: causal_language_model::AC_MODEL_STAFF_V0
  start_node: IN_WITHDRAW_MODEL_FROM_SERVICE_V0
  nodes:
    IN_WITHDRAW_MODEL_FROM_SERVICE_V0:
      type: IN
      code: IN_WITHDRAW_MODEL_FROM_SERVICE_V0
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
        SUCCESS: CC_WITHDRAW_MODEL_FROM_SERVICE_V0
        VIOLATION: EXIT_REJECTED
    CC_WITHDRAW_MODEL_FROM_SERVICE_V0:
      type: CC
      code: CC_WITHDRAW_MODEL_FROM_SERVICE_V0
      inputs:
        identity_key: $.payload.identity_key
      next:
        SUCCESS: CC_APPEND_MODEL_OPERATION_V0
        NOT_FOUND: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_APPEND_MODEL_OPERATION_V0:
      type: CC
      code: CC_APPEND_MODEL_OPERATION_V0
      inputs:
        staff_id: $.payload.staff_id
        operation: WITHDRAW_MODEL_FROM_SERVICE
        record:
          operation: WITHDRAW_MODEL_FROM_SERVICE
          staff_id: $.payload.staff_id
          subject: $.payload.identity_key
      next:
        SUCCESS: EXIT_WITHDRAWN
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    EXIT_WITHDRAWN:
      type: EXIT
      emit: causal_language_model::EV_MODEL_SERVICE_ENDED_V0
    EXIT_REJECTED:
      type: EXIT
```

---

## Intent

Closing a model's time in service
