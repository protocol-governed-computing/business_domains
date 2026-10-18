# TI_REGISTER_ACTOR_V0

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
  summary: Admits a request to register an actor, and sends the act only what the caller supplies and
    the person's preferences
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
      currency_preference: BACHI
      language: en
```

---

## Intent

Admits a request to register an actor, and sends the act only what the caller supplies and the person's preferences
