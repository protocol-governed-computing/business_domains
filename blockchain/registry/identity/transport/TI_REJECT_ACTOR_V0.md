# TI_REJECT_ACTOR_V0

## Header (Mandatory)

- **Artifact Code:** TI_REJECT_ACTOR_V0
- **Artifact Kind:** transport_ingress
- **Governed By:** CONSTITUTION_TRANSPORT_INGRESS_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Admits a request to reject a registered actor, declaring the contact address, authority and required grounds a caller sends and holding the decision, admitted states and outcomes, and the rejection occurrence label

---

## Machine

```yaml
fqdn: blockchain::TI_REJECT_ACTOR_V0
artifact_kind: TRANSPORT_INGRESS
version: v0
governed_by: transport::CONSTITUTION_TRANSPORT_INGRESS_V0
authority: pgc.platform
concern: identity
operation: blockchain.reject_actor
core:
  summary: Admits a request to reject a registered actor, declaring the contact address, authority and
    required grounds a caller sends and holding the decision, admitted states and outcomes, and the rejection
    occurrence label
input_contract:
  contact_address:
    type: string
    required: true
  verifying_authority:
    type: string
    required: true
  grounds:
    type: string
    required: true
context_requirements: []
handler:
  kind: WF_INVOCATION
  workflow: blockchain::WF_REJECT_ACTOR_V0
  payload_template:
    contact_address: ${input.contact_address}
    verifying_authority: ${input.verifying_authority}
    decision: REJECTED
    grounds: ${input.grounds}
    states_admitting_a_decision:
    - UNVERIFIED
    admitted_outcomes:
    - ACCEPTED
    - REJECTED
    decided_actor_fields:
      contact_address: ${input.contact_address}
      state: REJECTED
      verifying_authority: ${input.verifying_authority}
      grounds: ${input.grounds}
    self_check_parameters:
      verifying_authority: ${input.verifying_authority}
      contact_address: ${input.contact_address}
    self_check_rules:
    - field: verifying_authority
      op: neq
      value: ${input.contact_address}
    stream_id: ACTOR_OCCURRENCES
    occurrence_fields:
      occurrence: ACTOR_REJECTED
      contact_address: ${input.contact_address}
      verifying_authority: ${input.verifying_authority}
      grounds: ${input.grounds}
    grounds_parameters:
      grounds: ${input.grounds}
    grounds_rules:
    - field: grounds
      op: not_null
    - field: grounds
      op: neq
      value: ''
```
