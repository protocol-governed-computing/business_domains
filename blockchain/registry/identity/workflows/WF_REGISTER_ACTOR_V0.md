# WF_REGISTER_ACTOR_V0

## Header (Mandatory)

- **Artifact Code:** WF_REGISTER_ACTOR_V0
- **Artifact Kind:** workflow
- **Governed By:** CONSTITUTION_WORKFLOW_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

The governed sequence that admits a person as an unverified actor

---

## Machine

```yaml
fqdn: blockchain::WF_REGISTER_ACTOR_V0
artifact_kind: WORKFLOW
version: v0
governed_by: fb.workflow::CONSTITUTION_WORKFLOW_V0
runtime_binding: blockchain::RB_IDENTITY_BINDINGS_V0
subdomain: identity
structure: fb.execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: The governed sequence that admits a person as an unverified actor
  actor_context: blockchain::AC_PARTICIPANT_V0
  start_node: IN_ACTOR_REGISTERED_V0
  nodes:
    IN_ACTOR_REGISTERED_V0:
      type: IN
      code: IN_ACTOR_REGISTERED_V0
      next:
        ACK: CC_VALIDATE_REGISTRATION_V0
        NACK: EXIT_REJECTED
    CC_VALIDATE_REGISTRATION_V0:
      type: CC
      code: CC_VALIDATE_REGISTRATION_V0
      inputs:
        actor_record: $.payload.actor_record
        registration_schema: $.payload.registration_schema
      next:
        SUCCESS: CC_CLAIM_CONTACT_ADDRESS_V0
        VIOLATION: EXIT_REJECTED
    CC_CLAIM_CONTACT_ADDRESS_V0:
      type: CC
      code: CC_CLAIM_CONTACT_ADDRESS_V0
      inputs:
        actor_record: $.payload.actor_record
        address_path: $.payload.address_path
        address_type: $.payload.address_type
      next:
        SUCCESS: CC_REGISTER_ACTOR_V0
        ALREADY_EXISTS: CC_APPEND_ACTOR_OCCURRENCE_V0
        VIOLATION: EXIT_REJECTED
    CC_REGISTER_ACTOR_V0:
      type: CC
      code: CC_REGISTER_ACTOR_V0
      inputs:
        actor_fields: $.payload.actor_record
        contact_address: $.results.CC_CLAIM_CONTACT_ADDRESS_V0.result
      next:
        SUCCESS: CC_APPEND_ACTOR_OCCURRENCE_V0
        VIOLATION: EXIT_REJECTED
    CC_APPEND_ACTOR_OCCURRENCE_V0:
      type: CC
      code: CC_APPEND_ACTOR_OCCURRENCE_V0
      inputs:
        occurrence_fields: $.payload.occurrence_fields
        stream_id: $.payload.stream_id
        contact_address: $.results.CC_CLAIM_CONTACT_ADDRESS_V0.result
      next:
        SUCCESS: EXIT_SUCCESS
        VIOLATION: EXIT_REJECTED
    EXIT_REJECTED:
      type: EXIT
    EXIT_SUCCESS:
      type: EXIT
```
