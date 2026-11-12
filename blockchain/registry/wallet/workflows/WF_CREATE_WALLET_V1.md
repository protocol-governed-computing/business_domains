# WF_CREATE_WALLET_V1

## Machine

```yaml
fqdn: blockchain::WF_CREATE_WALLET_V1
artifact_kind: WORKFLOW
version: v1
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: wallet
supersedes: blockchain::WF_CREATE_WALLET_V0
runtime_binding: blockchain::RB_WALLET_BINDINGS_V1
consults:
- blockchain::RB_IDENTITY_BINDINGS_V0
subdomain: wallet
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: 'The governed sequence that performs: create wallet'
  actor_context: blockchain::AC_PARTICIPANT_V0
  start_node: IN_WALLET_CREATION_V0
  nodes:
    IN_WALLET_CREATION_V0:
      type: IN
      code: IN_WALLET_CREATION_V0
      next:
        ACK: CC_RESOLVE_ACTOR_IDENTITY_V0
        NACK: EXIT_REJECTED
    CC_RESOLVE_ACTOR_IDENTITY_V0:
      type: CC
      code: CC_RESOLVE_ACTOR_IDENTITY_V0
      inputs:
        contact_address: $.payload.contact_address
      next:
        SUCCESS: CC_REQUIRE_ACCEPTED_ACTOR_V0
        NOT_FOUND: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_REQUIRE_ACCEPTED_ACTOR_V0:
      type: CC
      code: CC_REQUIRE_ACCEPTED_ACTOR_V0
      inputs:
        state: $.results.CC_RESOLVE_ACTOR_IDENTITY_V0.actor_record.state
      next:
        SUCCESS: CC_DERIVE_WALLET_ADDRESS_V0
        VIOLATION: EXIT_REJECTED
    CC_DERIVE_WALLET_ADDRESS_V0:
      type: CC
      code: CC_DERIVE_WALLET_ADDRESS_V0
      inputs:
        key_material: $.payload.key_material
      next:
        SUCCESS: CC_REQUIRE_WALLET_ADDRESS_FREE_V0
        VIOLATION: EXIT_REJECTED
    CC_REQUIRE_WALLET_ADDRESS_FREE_V0:
      type: CC
      code: CC_REQUIRE_WALLET_ADDRESS_FREE_V0
      inputs:
        address: $.results.CC_DERIVE_WALLET_ADDRESS_V0.address
      next:
        SUCCESS: CC_CLAIM_WALLET_IDENTITY_V1
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_CLAIM_WALLET_IDENTITY_V1:
      type: CC
      code: CC_CLAIM_WALLET_IDENTITY_V1
      inputs:
        holder: $.results.CC_RESOLVE_ACTOR_IDENTITY_V0.actor_record.contact_address
      next:
        SUCCESS: CC_CLAIM_WALLET_ADDRESS_V0
        VIOLATION: EXIT_REJECTED
        ALREADY_EXISTS: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_CLAIM_WALLET_ADDRESS_V0:
      type: CC
      code: CC_CLAIM_WALLET_ADDRESS_V0
      inputs:
        address: $.results.CC_DERIVE_WALLET_ADDRESS_V0.address
      next:
        SUCCESS: CC_WRITE_WALLET_V0
        ALREADY_EXISTS: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_WRITE_WALLET_V0:
      type: CC
      code: CC_WRITE_WALLET_V0
      inputs:
        wallet_id: $.results.CC_CLAIM_WALLET_IDENTITY_V1.wallet_id
        holder: $.results.CC_RESOLVE_ACTOR_IDENTITY_V0.actor_record.contact_address
      next:
        SUCCESS: CC_RECORD_WALLET_MOMENT_V0
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_RECORD_WALLET_MOMENT_V0:
      type: CC
      code: CC_RECORD_WALLET_MOMENT_V0
      inputs:
        occurrence: WALLET_CREATED
        holder: $.results.CC_RESOLVE_ACTOR_IDENTITY_V0.actor_record.contact_address
        wallet_id: $.results.CC_CLAIM_WALLET_IDENTITY_V1.wallet_id
      next:
        SUCCESS: EXIT_COMPLETED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    EXIT_COMPLETED:
      type: EXIT
      emit: blockchain::EV_WALLET_CREATED_V0
    EXIT_REJECTED:
      type: EXIT
```

---

## Intent

The governed sequence that performs: create wallet
