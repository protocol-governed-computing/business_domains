# WF_REGISTER_MODEL_V0

## Machine

```yaml
fqdn: causal_language_model::WF_REGISTER_MODEL_V0
artifact_kind: WORKFLOW
version: v0
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: model_response
runtime_binding: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
subdomain: model_response
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: Registering a model, refusing a second registration of the same model
  actor_context: causal_language_model::AC_MODEL_STAFF_V0
  start_node: IN_REGISTER_MODEL_V0
  nodes:
    IN_REGISTER_MODEL_V0:
      type: IN
      code: IN_REGISTER_MODEL_V0
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
        SUCCESS: CC_CLAIM_MODEL_IDENTITY_V0
        VIOLATION: EXIT_REJECTED
    CC_CLAIM_MODEL_IDENTITY_V0:
      type: CC
      code: CC_CLAIM_MODEL_IDENTITY_V0
      inputs:
        description: $.payload.description
        fingerprint: $.payload.fingerprint
        description_schema:
          reading_capacity:
            type: integer
            required: true
      next:
        SUCCESS: CC_REGISTER_MODEL_V0
        ALREADY_EXISTS: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_REGISTER_MODEL_V0:
      type: CC
      code: CC_REGISTER_MODEL_V0
      inputs:
        identity_key: $.results.CC_CLAIM_MODEL_IDENTITY_V0.identity_key
        description: $.payload.description
        fingerprint: $.payload.fingerprint
      next:
        SUCCESS: CC_APPEND_MODEL_OPERATION_V0
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_APPEND_MODEL_OPERATION_V0:
      type: CC
      code: CC_APPEND_MODEL_OPERATION_V0
      inputs:
        staff_id: $.payload.staff_id
        operation: REGISTER_MODEL
        record:
          operation: REGISTER_MODEL
          staff_id: $.payload.staff_id
          subject: $.results.CC_CLAIM_MODEL_IDENTITY_V0.identity_key
      next:
        SUCCESS: EXIT_REGISTERED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    EXIT_REGISTERED:
      type: EXIT
      emit: causal_language_model::EV_MODEL_REGISTERED_V0
    EXIT_REJECTED:
      type: EXIT
```

---

## Intent

Registering a model, refusing a second registration of the same model
