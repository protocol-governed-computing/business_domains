# TE_REGISTER_ACTOR_V0

## 1. Intent

Classifies the endings of registering an actor and projects the contact address, the occurrence, its time and its position.

---

## Machine

```yaml
fqdn: blockchain::TE_REGISTER_ACTOR_V0
artifact_kind: TRANSPORT_EGRESS
version: v0
governed_by: transport::CONSTITUTION_TRANSPORT_EGRESS_V0
authority: pgc.platform
concern: identity
operation: blockchain.register_actor
core:
  summary: Classifies the endings of registering an actor and projects the contact address, the occurrence,
    its time and its position.
output_contract:
- field: contact_address
  from: surface.contact_address
- field: occurrence
  from: surface.record.occurrence
- field: occurred_at
  from: surface.record.occurred_at
- field: sequence_number
  from: surface.sequence_number
result_classification:
  SUCCESS: SUCCESS
  VIOLATION: VIOLATION
  NOT_FOUND: NOT_FOUND
default_result_class: EXECUTION_FAILURE
evidence_policy: reference_only
```
