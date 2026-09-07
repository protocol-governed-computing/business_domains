# WF_CREATE_WALLET_V0

## 1. Intent

The governed sequence that gives an accepted person a wallet and records that it did

---

## Machine

```yaml
fqdn: blockchain::WF_CREATE_WALLET_V0
artifact_kind: WORKFLOW
version: v0
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: wallet
runtime_binding: blockchain::RB_WALLET_BINDINGS_V0
consults:
- blockchain::RB_IDENTITY_BINDINGS_V0
subdomain: wallet
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: The governed sequence that gives an accepted person a wallet and records that it did
  actor_context: blockchain::AC_PARTICIPANT_V0
  start_node: IN_WALLET_CREATION_V0
  nodes:
    IN_WALLET_CREATION_V0:
      type: IN
      code: IN_WALLET_CREATION_V0
      next:
        ACK: CC_RESOLVE_ACTOR_V0
        NACK: EXIT_REJECTED
    CC_RESOLVE_ACTOR_V0:
      type: CC
      code: CC_RESOLVE_ACTOR_V0
      inputs:
        contact_address: $.payload.contact_address
      next:
        SUCCESS: CC_REQUIRE_ACCEPTED_HOLDER_V0
        NOT_FOUND: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
    CC_REQUIRE_ACCEPTED_HOLDER_V0:
      type: CC
      code: CC_REQUIRE_ACCEPTED_HOLDER_V0
      inputs:
        holder_state: $.results.CC_RESOLVE_ACTOR_V0.value.state
        states_admitting_a_wallet:
        - ACCEPTED
      next:
        SUCCESS: CC_DETERMINE_WALLET_IDENTITY_V0
        VIOLATION: EXIT_REJECTED
    CC_DETERMINE_WALLET_IDENTITY_V0:
      type: CC
      code: CC_DETERMINE_WALLET_IDENTITY_V0
      inputs:
        holder: $.results.CC_RESOLVE_ACTOR_V0.value.contact_address
        wallet_id_prefix: $.payload.wallet_id_prefix
      next:
        SUCCESS: CC_CLAIM_WALLET_IDENTITY_V0
        VIOLATION: EXIT_REJECTED
    CC_CLAIM_WALLET_IDENTITY_V0:
      type: CC
      code: CC_CLAIM_WALLET_IDENTITY_V0
      inputs:
        wallet_id: $.results.CC_DETERMINE_WALLET_IDENTITY_V0.id
      next:
        SUCCESS: CC_ESTABLISH_WALLET_ADDRESS_V0
        ALREADY_EXISTS: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
    CC_ESTABLISH_WALLET_ADDRESS_V0:
      type: CC
      code: CC_ESTABLISH_WALLET_ADDRESS_V0
      inputs:
        key_material: $.payload.key_material
      next:
        SUCCESS: CC_CREATE_WALLET_RECORD_V0
        VIOLATION: EXIT_REJECTED
    CC_CREATE_WALLET_RECORD_V0:
      type: CC
      code: CC_CREATE_WALLET_RECORD_V0
      inputs:
        wallet_id: $.results.CC_DETERMINE_WALLET_IDENTITY_V0.id
        wallet_fields: $.payload.wallet_fields
      next:
        SUCCESS: CC_APPEND_WALLET_OCCURRENCE_V0
        VIOLATION: EXIT_REJECTED
    CC_APPEND_WALLET_OCCURRENCE_V0:
      type: CC
      code: CC_APPEND_WALLET_OCCURRENCE_V0
      inputs:
        stream_id: $.results.CC_DETERMINE_WALLET_IDENTITY_V0.id
        occurrence_fields: $.payload.occurrence_fields
      next:
        SUCCESS: EXIT_SUCCESS
        VIOLATION: EXIT_REJECTED
    EXIT_SUCCESS:
      type: EXIT
      emit: blockchain::EV_WALLET_CREATED_V0
    EXIT_REJECTED:
      type: EXIT
```
