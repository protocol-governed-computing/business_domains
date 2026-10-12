# TI_REJECT_ACTOR_V1

## Machine

```yaml
fqdn: blockchain::TI_REJECT_ACTOR_V1
artifact_kind: TRANSPORT_INGRESS
version: v1
governed_by: transport::CONSTITUTION_TRANSPORT_INGRESS_V0
authority: pgc.platform
concern: identity
supersedes: blockchain::TI_REJECT_ACTOR_V0
operation: blockchain.reject_actor
core:
  summary: Admits a request to reject a registered actor, and sends the act only what the caller supplies
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
  workflow: blockchain::WF_REJECT_ACTOR_V2
  payload_template:
    contact_address: ${input.contact_address}
    verifying_authority: ${input.verifying_authority}
    grounds: ${input.grounds}
```

---

## Intent

Admits a request to reject a registered actor, and sends the act only what the caller supplies
