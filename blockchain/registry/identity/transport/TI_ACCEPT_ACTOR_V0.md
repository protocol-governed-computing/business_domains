# TI_ACCEPT_ACTOR_V0

## Header (Mandatory)

- **Artifact Code:** TI_ACCEPT_ACTOR_V0
- **Artifact Kind:** transport_ingress
- **Governed By:** CONSTITUTION_TRANSPORT_INGRESS_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Admits a request to accept a registered actor, declaring the contact address, authority and optional grounds a caller sends and holding the decision, admitted states and outcomes, and the acceptance occurrence label.

---

## Machine

```yaml
fqdn: blockchain::TI_ACCEPT_ACTOR_V0
artifact_kind: TRANSPORT_INGRESS
version: v0
governed_by: fb.transport::CONSTITUTION_TRANSPORT_INGRESS_V0
operation: blockchain.accept_actor
core:
  summary: Admits a request to accept a registered actor, declaring the contact address, authority and
    optional grounds a caller sends and holding the decision, admitted states and outcomes, and the acceptance
    occurrence label.
input_contract:
  contact_address:
    type: string
    required: true
  verifying_authority:
    type: string
    required: true
  grounds:
    type: string
context_requirements: []
handler:
  kind: WF_INVOCATION
  workflow: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
  payload_template:
    contact_address: ${input.contact_address}
    verifying_authority: ${input.verifying_authority}
    decision: ACCEPTED
    grounds: ${input.grounds}
    states_admitting_a_decision:
    - UNVERIFIED
    admitted_outcomes:
    - ACCEPTED
    - REJECTED
    decided_actor_fields:
      contact_address: ${input.contact_address}
      state: ACCEPTED
      verifying_authority: ${input.verifying_authority}
      grounds: ${input.grounds}
    stream_id: ACTOR_OCCURRENCES
    occurrence_fields:
      occurrence: ACTOR_ACCEPTED
      contact_address: ${input.contact_address}
      verifying_authority: ${input.verifying_authority}
      grounds: ${input.grounds}
```
