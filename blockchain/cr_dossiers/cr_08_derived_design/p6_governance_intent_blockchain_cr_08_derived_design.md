# Stage 6 — Governance Intent — blockchain / identity, wallet

## Machine

```yaml
document:
  phase: p6
  domain: blockchain
  subdomain:
  - identity
  - wallet
  cr: cr_08_derived_design
  rule_set: transformation.schemas.REGISTER_SCHEMA_P6_V0
registers:
  ownership:
  - capability: Register actor
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 1}
  - capability: Accept actor
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 2}
  - capability: Reject actor
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 3}
  - capability: Create wallet
    owner_subdomain: wallet
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 4}
  - capability: Authenticating callers
    owner_subdomain: identity
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 5}
  - capability: Wallets of any classification but default
    owner_subdomain: identity
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 6}
  - capability: Moving value between wallets
    owner_subdomain: identity
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 7}
  storage_governance:
  - storage_need: A durable actor record
    purpose: The business must know who registered, by their contact address, and whether it trusts them, keeping what they registered with.
    subdomain: identity
    source_finding: {phase: p5, register: business_objects, row: 1}
  - storage_need: A durable wallet record
    purpose: The business must know where a person it has accepted holds value, one wallet to each such person.
    subdomain: wallet
    source_finding: {phase: p5, register: business_objects, row: 2}
  - storage_need: A durable wallet identity registry
    purpose: Telling one wallet from another needs a claim on its identity at the moment it is recorded.
    subdomain: wallet
    source_finding: {phase: p5, register: business_objects, row: 3}
  - storage_need: A durable audit trail of identity
    purpose: Every operation must be traceable afterwards, and a trail that could be amended would not be evidence.
    subdomain: identity
    source_finding: {phase: p5, register: business_objects, row: 4}
  - storage_need: A durable audit trail of wallet
    purpose: Every operation must be traceable afterwards, and a trail that could be amended would not be evidence.
    subdomain: wallet
    source_finding: {phase: p5, register: business_objects, row: 5}
  cross_subdomain_deps:
  - dependency: Create wallet reads the actors identity keeps, and never writes them
    direction: wallet -> identity
    existing_artifact: blockchain::RB_IDENTITY_BINDINGS_V0
    status: SATISFIED
    source_finding: {phase: p5, register: actions, row: 4}
  pps_artifacts_requiring_action: []
  boundary_rules:
  - rule_name: IDENTITY_OWNS_ITS_RECORDS
    statement: Every record identity keeps is written only by identity's own operations.
    source_finding: {phase: p5, register: subdomain_purposes, row: 1}
  - rule_name: WALLET_OWNS_ITS_RECORDS
    statement: Every record wallet keeps is written only by wallet's own operations.
    source_finding: {phase: p5, register: subdomain_purposes, row: 2}
  - rule_name: WALLET_READS_IDENTITY_NEVER_WRITES
    statement: Create wallet reads what identity keeps and leaves it exactly as it was, including when it is refused.
    source_finding: {phase: p5, register: actions, row: 4}
  governance_outcome:
  - capability: Register actor
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: Register actor}
  - capability: Accept actor
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: Accept actor}
  - capability: Reject actor
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: Reject actor}
  - capability: Create wallet
    owner_subdomain: wallet
    source_finding: {phase: p6, register: ownership, key: Create wallet}
```

Projected from the business intent. Every row cites the business-intent row it places.

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

## gov_projection — Governed Handoff to Stage 7

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | boundary_rules · cross_subdomain_deps · governance_outcome · ownership · pps_artifacts_requiring_action · storage_governance |
| **Emits** → Stage 7 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
