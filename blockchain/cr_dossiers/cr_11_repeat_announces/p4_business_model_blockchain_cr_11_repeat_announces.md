# Stage 4 — Business Model — blockchain / identity, wallet

## Machine

```yaml
document:
  phase: p4
  domain: blockchain
  subdomain:
  - identity
  - wallet
  cr: cr_11_repeat_announces
  rule_set: transformation.schemas.REGISTER_SCHEMA_P4_V0
registers:
  actors:
  - actor: Participant
    role: Requests register actor, accept actor, reject actor, list actors and create wallet
    authority_class: Operator
    source_finding: {phase: p2, register: business_processes, row: 1}
  bm_entities:
  - entity: Actor
    description: The business must know who registered, by their contact address, and whether it trusts them, keeping what they registered with.
    store_model: One durable record per actor, addressed by its contact address, updated in place, carrying its own state (unverified, accepted and rejected).
    source_finding: {phase: p2, register: entities, row: 1}
  - entity: Wallet
    description: The business must know where a person it has accepted holds value, one wallet to each such person.
    store_model: One durable record per wallet, addressed by its holder, carrying its own state (active).
    source_finding: {phase: p2, register: entities, row: 2}
  resources:
  - resource: Actors records
    description: The business must know who registered, by their contact address, and whether it trusts them, keeping what they registered with.
    source_finding: {phase: p2, register: entities, row: 1}
  - resource: Wallets records
    description: The business must know where a person it has accepted holds value, one wallet to each such person.
    source_finding: {phase: p2, register: entities, row: 2}
  events:
  - event: Actor registered unverified
    trigger: When register actor completes
    lifecycle_meaning: Others learn that register actor completed without reading the identity records.
    source_finding: {phase: p1, register: business_events, row: 1}
  - event: Actor accepted
    trigger: When accept actor completes
    lifecycle_meaning: Others learn that accept actor completed without reading the identity records.
    source_finding: {phase: p1, register: business_events, row: 2}
  - event: Actor rejected
    trigger: When reject actor completes
    lifecycle_meaning: Others learn that reject actor completed without reading the identity records.
    source_finding: {phase: p1, register: business_events, row: 3}
  - event: Wallet created
    trigger: When create wallet completes
    lifecycle_meaning: Others learn that create wallet completed without reading the wallet records.
    source_finding: {phase: p1, register: business_events, row: 4}
  relationships:
  - subject: Actor
    verb: is identified by
    object: Contact address
    capability_need: Tell one actor from another when it is recorded
    source_finding: {phase: p1, register: identity_and_sameness, row: 1}
  - subject: Wallet
    verb: is identified by
    object: Holder
    capability_need: Tell one wallet from another when it is recorded
    source_finding: {phase: p1, register: identity_and_sameness, row: 2}
  - subject: Wallet
    verb: is held by
    object: Actor
    capability_need: Read the actor who holds it
    source_finding: {phase: p1, register: identity_and_sameness, row: 2}
  capability_graph:
  - capability: Appendonly jsonl side effect, as the platform declares it
    source_finding: {phase: p3, register: authoring_decisions, row: 1}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: Clock side effect, as the platform declares it
    source_finding: {phase: p3, register: authoring_decisions, row: 2}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: Mutable json side effect, as the platform declares it
    source_finding: {phase: p3, register: authoring_decisions, row: 3}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: Registry side effect, as the platform declares it
    source_finding: {phase: p3, register: authoring_decisions, row: 4}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: Assemble record transform, as the platform declares it
    source_finding: {phase: p3, register: authoring_decisions, row: 5}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: Compare equal transform, as the platform declares it
    source_finding: {phase: p3, register: authoring_decisions, row: 6}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: Generate id transform, as the platform declares it
    source_finding: {phase: p3, register: authoring_decisions, row: 7}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: Select records transform, as the platform declares it
    source_finding: {phase: p3, register: authoring_decisions, row: 8}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: Validate parameter rules transform, as the platform declares it
    source_finding: {phase: p3, register: authoring_decisions, row: 9}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: Validate record structure transform, as the platform declares it
    source_finding: {phase: p3, register: authoring_decisions, row: 10}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: Validate set membership transform, as the platform declares it
    source_finding: {phase: p3, register: authoring_decisions, row: 11}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: The register actor workflow
    source_finding: {phase: p3, register: authoring_decisions, row: 12}
    status: CRITICAL
    gap_register_entry: GAP-01
    notes: The workflow the composition holds for register actor means something other than the ledger decides, so its successor takes the next unused version.
  - capability: The accept actor workflow
    source_finding: {phase: p3, register: authoring_decisions, row: 13}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: The reject actor workflow
    source_finding: {phase: p3, register: authoring_decisions, row: 14}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: The list actors workflow
    source_finding: {phase: p3, register: authoring_decisions, row: 15}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: The create wallet workflow
    source_finding: {phase: p3, register: authoring_decisions, row: 16}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  gap_register:
  - gap_code: GAP-01
    source_finding: {phase: p3, register: authoring_decisions, row: 12}
    capability: The register actor workflow
    owner_subdomain: identity
    resolution: EXTEND
  authoring_scope:
  - capability: The register actor workflow
    gap_register_ref: GAP-01
  dependency_graph:
  - from: blockchain
    to: capability_side_effects::CS_APPENDONLY_JSONL_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 1}
  - from: blockchain
    to: capability_side_effects::CS_CLOCK_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 2}
  - from: blockchain
    to: capability_side_effects::CS_MUTABLE_JSON_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 3}
  - from: blockchain
    to: capability_side_effects::CS_REGISTRY_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 4}
  - from: blockchain
    to: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 5}
  - from: blockchain
    to: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 6}
  - from: blockchain
    to: capability_transforms::CT_PURE_GENERATE_ID_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 7}
  - from: blockchain
    to: capability_transforms::CT_PURE_SELECT_RECORDS_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 8}
  - from: blockchain
    to: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 9}
  - from: blockchain
    to: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 10}
  - from: blockchain
    to: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 11}
  constraint_register:
  - number: '1'
    constraint: Recording an actor again with the same contact address records the repeat, and the actor already recorded is unchanged by it.
    source_finding: {phase: p1, register: business_invariants, row: 1}
    source: invariant
  - number: '2'
    constraint: No two wallets share their holder.
    source_finding: {phase: p1, register: business_invariants, row: 2}
    source: invariant
  - number: '3'
    constraint: Each wallet is held by one actor who is accepted.
    source_finding: {phase: p1, register: business_invariants, row: 3}
    source: invariant
  - number: '4'
    constraint: Every identity operation records contact address, verifying authority and grounds on the identity trail, and no entry is changed or removed.
    source_finding: {phase: p1, register: business_invariants, row: 4}
    source: invariant
  - number: '5'
    constraint: Every wallet operation records holder on the wallet trail, and no entry is changed or removed.
    source_finding: {phase: p1, register: business_invariants, row: 5}
    source: invariant
  design_decisions:
  - number: '1'
    decision: identity stays the subdomain it is; the derived design extends it.
    source_finding: {phase: p3, register: placement_decision, row: 1}
    rationale: The composition already holds identity; the derived design keeps its binding and its entrances.
    constraints_imposed: The binding and entrances callers meet keep their names.
  - number: '2'
    decision: wallet stays the subdomain it is; the derived design extends it.
    source_finding: {phase: p3, register: placement_decision, row: 2}
    rationale: The composition already holds wallet; the derived design keeps its binding and its entrances.
    constraints_imposed: The binding and entrances callers meet keep their names.
  - number: '3'
    decision: Each artifact keeps its identity when its meaning is unchanged, and takes the next unused version when it changes.
    source_finding: {phase: p3, register: analysis_findings, row: 1}
    rationale: A caller relying on an identity relies on what it means.
    constraints_imposed: A caller dispatching by identity follows supersedes.
```

Projected from the analysis loop. Every row cites what it consolidates.

---

## 1. Discovery Summary

---

## 2. Capability Graph (capability_graph)

---

## 3. Dependency Graph (dependency_graph)

---

## 4. Constraint Register (constraint_register)

---

## 5. Gap Register (gap_register)

---

## 6. Design Decisions (design_decisions)

---

## 7. Authoring Scope (authoring_scope)

---

## gov_projection — Governed Handoff to Stage 5

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 3 | actors · authoring_scope · bm_entities · capability_graph · constraint_register · dependency_graph · design_decisions · events · gap_register · relationships · resources |
| **Emits** → Stage 5 | actors · bm_entities · resources · events · relationships · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
