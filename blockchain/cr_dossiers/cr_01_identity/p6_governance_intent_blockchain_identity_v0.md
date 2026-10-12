# Stage 6 — Governance Intent: blockchain / identity

## Machine

```yaml
document:
  phase: p6
  domain: blockchain
  subdomain: identity
  cr: cr_01_identity
  rule_set: transformation.schemas.REGISTER_SCHEMA_P6_V0
registers:
  ownership:
  - capability: Declare the actors of this business
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Declare the actors of this business}
  - capability: Declare the stores identity owns
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Declare the stores identity owns}
  - capability: Bind identity's workflows to the stores they use
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Bind identity's workflows to the stores they use}
  - capability: Recognise the moments an actor is registered, accepted and rejected
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: 'Recognise the moments an actor is registered, accepted and rejected'}
  - capability: Record an acceptance and a rejection
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Record an acceptance and a rejection}
  - capability: Admit a person's registration and record them unverified
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Admit a person's registration and record them unverified}
  - capability: Record an authority's decision against a registered actor
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Record an authority's decision against a registered actor}
  - capability: Admit a request to register a person
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Admit a request to register a person}
  - capability: Admit a request to record a verification decision
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Admit a request to record a verification decision}
  - capability: Hold the trail of occurrences
    owner_subdomain: identity
    disposition: SATISFIED
    existing_artifact: capability_side_effects::CS_APPENDONLY_JSONL_V0
    source_finding: {phase: p4, register: capability_graph, key: Hold the trail of occurrences}
  - capability: Hold an actor's current state
    owner_subdomain: identity
    disposition: SATISFIED
    existing_artifact: capability_side_effects::CS_MUTABLE_JSON_V0
    source_finding: {phase: p4, register: capability_graph, key: Hold an actor's current state}
  - capability: Claim and resolve the contact address
    owner_subdomain: identity
    disposition: SATISFIED
    existing_artifact: capability_side_effects::CS_REGISTRY_V0
    source_finding: {phase: p4, register: capability_graph, key: Claim and resolve the contact address}
  - capability: Read a registration for absent or malformed details
    owner_subdomain: identity
    disposition: SATISFIED
    existing_artifact: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    source_finding: {phase: p4, register: capability_graph, key: Read a registration for absent or malformed details}
  - capability: Determine the time an occurrence happened
    owner_subdomain: capability_side_effects
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Determine the time an occurrence happened}
  - capability: Re-application by a rejected actor
    owner_subdomain: identity
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Re-application by a rejected actor}
  - capability: Revocation of an accepted actor
    owner_subdomain: identity
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Revocation of an accepted actor}
  - capability: Governing which persons may be an authority
    owner_subdomain: identity
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Governing which persons may be an authority}
  - capability: Holding the material an authority examined
    owner_subdomain: identity
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Holding the material an authority examined}
  - capability: Correcting an actor's own details after registration
    owner_subdomain: identity
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Correcting an actor's own details after registration}
  storage_governance:
  - storage_need: A durable record of every person the business knows, carrying whether it has accepted them
    purpose: The business requires one authoritative record per actor, whose state changes once and in place when a decision is recorded, so that the state can be read at the moment of deciding
    subdomain: identity
    source_finding: {phase: p5, register: business_objects, key: Actor record}
  - storage_need: An atomic claim on each contact address
    purpose: Two registrations carrying the same address must resolve to one actor, and only a claim taken at the moment of registration can guarantee it
    subdomain: identity
    source_finding: {phase: p5, register: business_objects, key: Contact address registry}
  - storage_need: An unamendable trail of every occurrence recorded against an actor
    purpose: An occurrence that has happened cannot be un-happened, so its record is never amended and never removed, and the business can afterwards show who registered, who decided, what was decided and when
    subdomain: identity
    source_finding: {phase: p5, register: business_objects, key: Actor occurrence trail}
  cross_subdomain_deps:
  - dependency: Holding the trail of occurrences unamendably
    direction: identity -> capability_side_effects
    existing_artifact: capability_side_effects::CS_APPENDONLY_JSONL_V0
    status: SATISFIED
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_side_effects::CS_APPENDONLY_JSONL_V0'}
  - dependency: Holding an actor's current state addressably
    direction: identity -> capability_side_effects
    existing_artifact: capability_side_effects::CS_MUTABLE_JSON_V0
    status: SATISFIED
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_side_effects::CS_MUTABLE_JSON_V0'}
  - dependency: Claiming and resolving the contact address
    direction: identity -> capability_side_effects
    existing_artifact: capability_side_effects::CS_REGISTRY_V0
    status: SATISFIED
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_side_effects::CS_REGISTRY_V0'}
  - dependency: Reading a registration for absent or malformed details
    direction: identity -> capability_transforms
    existing_artifact: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    status: SATISFIED
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0'}
  - dependency: Reading a value against a declared admitted set
    direction: identity -> capability_transforms
    existing_artifact: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    status: SATISFIED
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0'}
  - dependency: Comparing the authority named on a decision against the actor it names
    direction: identity -> capability_transforms
    existing_artifact: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
    status: SATISFIED
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_transforms::CT_PURE_COMPARE_EQUAL_V0'}
  - dependency: Assembling the record each occurrence appends
    direction: identity -> capability_transforms
    existing_artifact: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    status: SATISFIED
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0'}
  - dependency: Extracting named values from a registration or a decision
    direction: identity -> capability_transforms
    existing_artifact: capability_transforms::CT_PURE_EXTRACT_V0
    status: SATISFIED
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_transforms::CT_PURE_EXTRACT_V0'}
  - dependency: Determining the time an occurrence happened
    direction: identity -> capability_side_effects
    existing_artifact: ''
    status: GAP
    source_finding: {phase: p4, register: dependency_graph, key: the substrate capability supplying the current time}
  pps_artifacts_requiring_action:
  - fqdn: capability_side_effects::CS_APPENDONLY_JSONL_V0
    current_status: Present and reused unchanged; impacted by 58 artifacts
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_side_effects::CS_APPENDONLY_JSONL_V0'}
  - fqdn: capability_side_effects::CS_MUTABLE_JSON_V0
    current_status: Present and reused unchanged; impacted by 51 artifacts
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_side_effects::CS_MUTABLE_JSON_V0'}
  - fqdn: capability_side_effects::CS_REGISTRY_V0
    current_status: Present and reused unchanged; impacted by 47 artifacts
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_side_effects::CS_REGISTRY_V0'}
  - fqdn: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    current_status: Present and reused unchanged
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0'}
  - fqdn: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    current_status: Present and reused unchanged
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0'}
  - fqdn: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
    current_status: Present and reused unchanged
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_transforms::CT_PURE_COMPARE_EQUAL_V0'}
  - fqdn: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    current_status: Present and reused unchanged
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0'}
  - fqdn: capability_transforms::CT_PURE_EXTRACT_V0
    current_status: Present and reused unchanged
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_transforms::CT_PURE_EXTRACT_V0'}
  boundary_rules:
  - rule_name: IDENTITY_OWNS_ITS_STORES
    statement: Every store identity reads or writes is declared by identity, and no identity operation writes into a store another subdomain owns.
    source_finding: {phase: p4, register: design_decisions, row: 1}
  - rule_name: THE_TRAIL_IS_NEVER_READ_TO_DECIDE
    statement: No operation reads the occurrence trail to decide anything; an actor's state is read from the state store, and the trail is evidence only.
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - rule_name: EVERY_CLAIM_PRECEDES_EVERY_WRITE
    statement: A registration claims the contact address before it writes the actor record, so a refused registration leaves nothing behind.
    source_finding: {phase: p4, register: design_decisions, row: 3}
  - rule_name: AUTHORITY_IS_RECORDED_NEVER_RESOLVED
    statement: Identity records the authority named on a decision and resolves it against nothing. No store holds authorities, and the self-verification refusal compares two names.
    source_finding: {phase: p4, register: design_decisions, row: 6}
  - rule_name: ACCEPTANCE_AND_REJECTION_ARE_DISTINCT
    statement: No operation writes one decision record and distinguishes the outcome by a field; the two outcomes are recorded as two occurrences.
    source_finding: {phase: p4, register: design_decisions, row: 4}
  - rule_name: NO_TIME_IS_INVENTED
    statement: No identity operation supplies a time it did not receive from the capability that determines one. Until the substrate offers that capability this change cannot be built.
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - rule_name: IDENTITY_GRANTS_NO_PERMISSION
    statement: Identity says who an actor is and whether it is trusted; it declares nothing about what a trusted actor may do, which belongs to the functions that name the actor.
    source_finding: {phase: p4, register: constraint_register, row: 5}
  governance_outcome:
  - capability: Declare the actors of this business
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: Declare the actors of this business}
  - capability: Declare the stores identity owns
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: Declare the stores identity owns}
  - capability: Bind identity's workflows to the stores they use
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: Bind identity's workflows to the stores they use}
  - capability: Recognise the moments an actor is registered, accepted and rejected
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: 'Recognise the moments an actor is registered, accepted and rejected'}
  - capability: Record an acceptance and a rejection
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: Record an acceptance and a rejection}
  - capability: Admit a person's registration and record them unverified
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: Admit a person's registration and record them unverified}
  - capability: Record an authority's decision against a registered actor
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: Record an authority's decision against a registered actor}
  - capability: Admit a request to register a person
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: Admit a request to register a person}
  - capability: Admit a request to record a verification decision
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: Admit a request to record a verification decision}
```

Placement only. Every capability declared in scope is given an owner, every store is placed with the
subdomain that holds it, and the one capability this change needs and does not own is declared as a
crossing rather than quietly placed here.

---

## 1. Subdomain Boundary — Ownership

---

## 2. Storage Governance Requirements

---

## 3. Cross-Subdomain Dependency Declaration

---

## 4. PPS Artifacts Requiring Action

---

## 5. Governance Boundary Rules

---

## 6. Governance Outcome

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 4 — Business Model | p4_business_model_blockchain_identity_v0.md | COMPLETE |
| Stage 5 — Business Intent | p5_business_intent_blockchain_identity_v0.md | COMPLETE |
| Stage 6 — Governance Intent | This document | COMPLETE |

---

## gov_projection — Governed Handoff to Stage 7

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
| **Emits** → Stage 7 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
