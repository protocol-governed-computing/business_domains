# TE_ACCEPT_ACTOR_V0

## 1. Intent

Classifies the endings of accepting an actor, including the actor that does not exist, and projects what was recorded.

---

## Machine

```yaml
fqdn: blockchain::TE_ACCEPT_ACTOR_V0
artifact_kind: TRANSPORT_EGRESS
version: v0
governed_by: transport::CONSTITUTION_TRANSPORT_EGRESS_V0
authority: pgc.platform
concern: identity
operation: blockchain.accept_actor
core:
  summary: Classifies the endings of accepting an actor, including the actor that does not exist, and
    projects what was recorded.
output_contract:
- field: contact_address
  from: surface.contact_address
- field: occurrence
  from: surface.record.occurrence
- field: verifying_authority
  from: surface.record.verifying_authority
- field: grounds
  from: surface.record.grounds
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
