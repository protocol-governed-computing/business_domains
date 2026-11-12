# WF_REGISTER_ACTOR_V3

## Machine

```yaml
fqdn: blockchain::WF_REGISTER_ACTOR_V3
artifact_kind: WORKFLOW
version: v3
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: identity
supersedes: blockchain::WF_REGISTER_ACTOR_V2
runtime_binding: blockchain::RB_IDENTITY_BINDINGS_V0
subdomain: identity
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: 'The governed sequence that performs: register actor'
  actor_context: blockchain::AC_PARTICIPANT_V0
  start_node: IN_ACTOR_REGISTERED_V0
  nodes:
    IN_ACTOR_REGISTERED_V0:
      type: IN
      code: IN_ACTOR_REGISTERED_V0
      next:
        ACK: CC_CHECK_REGISTER_ACTOR_SUBMISSION_V0
        NACK: EXIT_REJECTED
    CC_CHECK_REGISTER_ACTOR_SUBMISSION_V0:
      type: CC
      code: CC_CHECK_REGISTER_ACTOR_SUBMISSION_V0
      inputs:
        submission: $.payload.actor_record
      next:
        SUCCESS: CC_CLAIM_ACTOR_CONTACT_ADDRESS_V0
        VIOLATION: EXIT_REJECTED
    CC_CLAIM_ACTOR_CONTACT_ADDRESS_V0:
      type: CC
      code: CC_CLAIM_ACTOR_CONTACT_ADDRESS_V0
      inputs:
        contact_address: $.payload.actor_record.contact_address
      next:
        SUCCESS: CC_WRITE_ACTOR_V0
        ALREADY_EXISTS: CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_WRITE_ACTOR_V0:
      type: CC
      code: CC_WRITE_ACTOR_V0
      inputs:
        contact_address: $.payload.actor_record.contact_address
        submission: $.payload.actor_record
      next:
        SUCCESS: CC_RECORD_IDENTITY_MOMENT_V0
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_RECORD_IDENTITY_MOMENT_V0:
      type: CC
      code: CC_RECORD_IDENTITY_MOMENT_V0
      inputs:
        occurrence: ACTOR_REGISTERED_UNVERIFIED
        contact_address: $.payload.actor_record.contact_address
        verifying_authority: $.payload.actor_record.verifying_authority
        grounds: $.payload.actor_record.grounds
      next:
        SUCCESS: EXIT_COMPLETED
        BACKEND_ERROR: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
    CC_RECORD_IDENTITY_REPEATED_MOMENT_V0:
      type: CC
      code: CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
      inputs:
        occurrence: ACTOR_REGISTERED_UNVERIFIED
        contact_address: $.payload.actor_record.contact_address
        verifying_authority: $.payload.actor_record.verifying_authority
        grounds: $.payload.actor_record.grounds
        name: $.payload.actor_record.name
        currency_preference: $.payload.actor_record.currency_preference
        language: $.payload.actor_record.language
      next:
        SUCCESS: EXIT_REPEATED
        BACKEND_ERROR: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
    EXIT_COMPLETED:
      type: EXIT
      emit: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
    EXIT_REJECTED:
      type: EXIT
    EXIT_REPEATED:
      type: EXIT
      emit: blockchain::EV_ACTOR_REGISTERED_AGAIN_V0
```

---

## Intent

The governed sequence that performs: register actor
