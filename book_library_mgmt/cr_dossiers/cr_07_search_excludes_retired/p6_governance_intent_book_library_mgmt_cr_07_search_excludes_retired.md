# Stage 6 — Governance Intent — book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p6
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_07_search_excludes_retired
  rule_set: transformation.schemas.REGISTER_SCHEMA_P6_V0
registers:
  ownership:
  - capability: Register book
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 1}
  - capability: Register additional edition
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 2}
  - capability: Register physical copy
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 3}
  - capability: Update bibliographic information
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 4}
  - capability: Retire book record
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 5}
  - capability: Reinstate book record
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 6}
  - capability: Retire physical copy
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 7}
  - capability: Reinstate physical copy
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 8}
  - capability: Retrieve book details
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 9}
  - capability: Search catalog
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 10}
  - capability: Circulation, patrons, staff, reservations, acquisitions, inventory, notifications, policy and reporting
    owner_subdomain: catalog
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 11}
  - capability: Deciding which staff are authorized
    owner_subdomain: catalog
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 12}
  - capability: Retirement of a work
    owner_subdomain: catalog
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 13}
  - capability: Import of the records staff maintain manually today
    owner_subdomain: catalog
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 14}
  storage_governance:
  - storage_need: A durable work record
    purpose: A published work, recognizable as one thing across the editions in which it is published, so staff find every edition of it together.
    subdomain: catalog
    source_finding: {phase: p5, register: business_objects, row: 1}
  - storage_need: A durable work identity registry
    purpose: Telling one work from another needs a claim on its identity at the moment it is recorded.
    subdomain: catalog
    source_finding: {phase: p5, register: business_objects, row: 2}
  - storage_need: A durable book record
    purpose: 'An edition the library catalogs: the single authoritative description of one publication of a work, so the catalog describes what the library holds as it actually is.'
    subdomain: catalog
    source_finding: {phase: p5, register: business_objects, row: 3}
  - storage_need: A durable book identity registry
    purpose: Telling one book from another needs a claim on its identity at the moment it is recorded.
    subdomain: catalog
    source_finding: {phase: p5, register: business_objects, row: 4}
  - storage_need: A durable physical copy record
    purpose: An individual copy the library owns, belonging to exactly one edition and told apart from every other copy by its barcode.
    subdomain: catalog
    source_finding: {phase: p5, register: business_objects, row: 5}
  - storage_need: A durable physical copy identity registry
    purpose: Telling one physical copy from another needs a claim on its identity at the moment it is recorded.
    subdomain: catalog
    source_finding: {phase: p5, register: business_objects, row: 6}
  - storage_need: A durable audit trail of catalog
    purpose: Every operation must be traceable afterwards, and a trail that could be amended would not be evidence.
    subdomain: catalog
    source_finding: {phase: p5, register: business_objects, row: 7}
  cross_subdomain_deps: []
  pps_artifacts_requiring_action: []
  boundary_rules:
  - rule_name: CATALOG_OWNS_ITS_RECORDS
    statement: Every record catalog keeps is written only by catalog's own operations.
    source_finding: {phase: p5, register: subdomain_purposes, row: 1}
  governance_outcome:
  - capability: Register book
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Register book}
  - capability: Register additional edition
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Register additional edition}
  - capability: Register physical copy
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Register physical copy}
  - capability: Update bibliographic information
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Update bibliographic information}
  - capability: Retire book record
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Retire book record}
  - capability: Reinstate book record
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Reinstate book record}
  - capability: Retire physical copy
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Retire physical copy}
  - capability: Reinstate physical copy
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Reinstate physical copy}
  - capability: Retrieve book details
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Retrieve book details}
  - capability: Search catalog
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Search catalog}
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
