# TI_REGISTER_ACTOR_V0

## Header (Mandatory)

- **Artifact Code:** TI_REGISTER_ACTOR_V0
- **Artifact Kind:** transport_ingress
- **Governed By:** CONSTITUTION_TRANSPORT_INGRESS_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Admits a request to register an actor, declaring the name and contact address a caller sends and holding the schema, address path, stream, preferences and occurrence label the act requires.

---

## Machine

```yaml
fqdn: blockchain::TI_REGISTER_ACTOR_V0
artifact_kind: TRANSPORT_INGRESS
version: v0
governed_by: transport::CONSTITUTION_TRANSPORT_INGRESS_V0
authority: pgc.platform
concern: identity
operation: blockchain.register_actor
core:
  summary: Admits a request to register an actor, declaring the name and contact address a caller sends
    and holding the schema, address path, stream, preferences and occurrence label the act requires.
input_contract:
  name:
    type: string
    required: true
  contact_address:
    type: string
    required: true
context_requirements: []
handler:
  kind: WF_INVOCATION
  workflow: blockchain::WF_REGISTER_ACTOR_V0
  payload_template:
    actor_record:
      name: ${input.name}
      contact_address: ${input.contact_address}
      state: UNVERIFIED
      currency_preference: BACHI
      language: en
    registration_schema:
      name:
        required: true
        type: string
      contact_address:
        required: true
        type: string
    address_path: contact_address
    address_type: string
    stream_id: ACTOR_OCCURRENCES
    occurrence_fields:
      occurrence: ACTOR_REGISTERED_UNVERIFIED
      contact_address: ${input.contact_address}
```
