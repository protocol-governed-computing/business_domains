# TI_REJECT_ACTOR_V0

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
    required grounds a caller sends and holding the stream and the rejection occurrence label
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
  workflow: blockchain::WF_REJECT_ACTOR_V1
  payload_template:
    contact_address: ${input.contact_address}
    verifying_authority: ${input.verifying_authority}
    grounds: ${input.grounds}
    stream_id: ACTOR_OCCURRENCES
    occurrence_fields:
      occurrence: ACTOR_REJECTED
      contact_address: ${input.contact_address}
      verifying_authority: ${input.verifying_authority}
      grounds: ${input.grounds}
```

---

## Intent

Admits a request to reject a registered actor, declaring the contact address, authority and required grounds a caller sends and holding the stream and the rejection occurrence label
