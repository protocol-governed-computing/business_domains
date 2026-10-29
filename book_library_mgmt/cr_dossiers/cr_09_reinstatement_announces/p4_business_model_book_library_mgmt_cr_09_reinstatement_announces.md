# Stage 4 — Business Model — book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p4
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_09_reinstatement_announces
  rule_set: transformation.schemas.REGISTER_SCHEMA_P4_V0
registers:
  actors:
  - actor: Library staff
    role: Requests register book, register additional edition, register physical copy, update bibliographic information, retire book record, reinstate book record, retire physical copy, reinstate physical copy, retrieve book details and search catalog
    authority_class: Operator
    source_finding: {phase: p2, register: business_processes, row: 1}
  bm_entities:
  - entity: Work
    description: A published work, recognizable as one thing across the editions in which it is published, so staff find every edition of it together.
    store_model: One durable record per work, addressed by its title and author.
    source_finding: {phase: p2, register: entities, row: 1}
  - entity: Book
    description: 'An edition the library catalogs: the single authoritative description of one publication of a work, so the catalog describes what the library holds as it actually is.'
    store_model: One durable record per book, addressed by its title, author and publication year, updated in place, carrying its own state (registered and retired).
    source_finding: {phase: p2, register: entities, row: 2}
  - entity: Physical copy
    description: An individual copy the library owns, belonging to exactly one edition and told apart from every other copy by its barcode.
    store_model: One durable record per physical copy, addressed by its barcode, updated in place, carrying its own state (registered and retired).
    source_finding: {phase: p2, register: entities, row: 3}
  resources:
  - resource: Works records
    description: A published work, recognizable as one thing across the editions in which it is published, so staff find every edition of it together.
    source_finding: {phase: p2, register: entities, row: 1}
  - resource: Books records
    description: 'An edition the library catalogs: the single authoritative description of one publication of a work, so the catalog describes what the library holds as it actually is.'
    source_finding: {phase: p2, register: entities, row: 2}
  - resource: Physical copies records
    description: An individual copy the library owns, belonging to exactly one edition and told apart from every other copy by its barcode.
    source_finding: {phase: p2, register: entities, row: 3}
  events:
  - event: Work registered
    trigger: When register book completes
    lifecycle_meaning: Others learn that register book completed without reading the catalog records.
    source_finding: {phase: p1, register: business_events, row: 1}
  - event: Book registered
    trigger: When register book completes
    lifecycle_meaning: Others learn that register book completed without reading the catalog records.
    source_finding: {phase: p1, register: business_events, row: 2}
  - event: Physical copy registered
    trigger: When register book completes
    lifecycle_meaning: Others learn that register book completed without reading the catalog records.
    source_finding: {phase: p1, register: business_events, row: 3}
  - event: Book registered
    trigger: When register additional edition completes
    lifecycle_meaning: Others learn that register additional edition completed without reading the catalog records.
    source_finding: {phase: p1, register: business_events, row: 4}
  - event: Physical copy registered
    trigger: When register physical copy completes
    lifecycle_meaning: Others learn that register physical copy completed without reading the catalog records.
    source_finding: {phase: p1, register: business_events, row: 5}
  - event: Bibliographic information updated
    trigger: When update bibliographic information completes
    lifecycle_meaning: Others learn that update bibliographic information completed without reading the catalog records.
    source_finding: {phase: p1, register: business_events, row: 6}
  - event: Book retired
    trigger: When retire book record completes
    lifecycle_meaning: Others learn that retire book record completed without reading the catalog records.
    source_finding: {phase: p1, register: business_events, row: 7}
  - event: Book reinstated
    trigger: When reinstate book record completes
    lifecycle_meaning: Others learn that reinstate book record completed without reading the catalog records.
    source_finding: {phase: p1, register: business_events, row: 8}
  - event: Physical copy retired
    trigger: When retire physical copy completes
    lifecycle_meaning: Others learn that retire physical copy completed without reading the catalog records.
    source_finding: {phase: p1, register: business_events, row: 9}
  - event: Physical copy reinstated
    trigger: When reinstate physical copy completes
    lifecycle_meaning: Others learn that reinstate physical copy completed without reading the catalog records.
    source_finding: {phase: p1, register: business_events, row: 10}
  relationships:
  - subject: Work
    verb: is identified by
    object: Title and author
    capability_need: Tell one work from another when it is recorded
    source_finding: {phase: p1, register: identity_and_sameness, row: 1}
  - subject: Book
    verb: is identified by
    object: Title, author and publication year
    capability_need: Tell one book from another when it is recorded
    source_finding: {phase: p1, register: identity_and_sameness, row: 2}
  - subject: Book
    verb: belongs to
    object: Work
    capability_need: Record a book against exactly one work
    source_finding: {phase: p1, register: identity_and_sameness, row: 2}
  - subject: Physical copy
    verb: is identified by
    object: Barcode
    capability_need: Tell one physical copy from another when it is recorded
    source_finding: {phase: p1, register: identity_and_sameness, row: 3}
  - subject: Physical copy
    verb: belongs to
    object: Book
    capability_need: Record a physical copy against exactly one book
    source_finding: {phase: p1, register: identity_and_sameness, row: 3}
  capability_graph:
  - capability: Appendonly jsonl side effect, as the platform declares it
    source_finding: {phase: p3, register: authoring_decisions, row: 1}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: Mutable json side effect, as the platform declares it
    source_finding: {phase: p3, register: authoring_decisions, row: 2}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: Registry side effect, as the platform declares it
    source_finding: {phase: p3, register: authoring_decisions, row: 3}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: Assemble record transform, as the platform declares it
    source_finding: {phase: p3, register: authoring_decisions, row: 4}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: Compare equal transform, as the platform declares it
    source_finding: {phase: p3, register: authoring_decisions, row: 5}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: Select records transform, as the platform declares it
    source_finding: {phase: p3, register: authoring_decisions, row: 6}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: Validate parameter rules transform, as the platform declares it
    source_finding: {phase: p3, register: authoring_decisions, row: 7}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: Validate record structure transform, as the platform declares it
    source_finding: {phase: p3, register: authoring_decisions, row: 8}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: Validate set membership transform, as the platform declares it
    source_finding: {phase: p3, register: authoring_decisions, row: 9}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: The register book workflow
    source_finding: {phase: p3, register: authoring_decisions, row: 10}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: The register additional edition workflow
    source_finding: {phase: p3, register: authoring_decisions, row: 11}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: The register physical copy workflow
    source_finding: {phase: p3, register: authoring_decisions, row: 12}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: The update bibliographic information workflow
    source_finding: {phase: p3, register: authoring_decisions, row: 13}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: The retire book record workflow
    source_finding: {phase: p3, register: authoring_decisions, row: 14}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: The reinstate book record workflow
    source_finding: {phase: p3, register: authoring_decisions, row: 15}
    status: CRITICAL
    gap_register_entry: GAP-01
    notes: The workflow the composition holds for reinstate book record means something other than the ledger decides, so its successor takes the next unused version.
  - capability: The retire physical copy workflow
    source_finding: {phase: p3, register: authoring_decisions, row: 16}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: The reinstate physical copy workflow
    source_finding: {phase: p3, register: authoring_decisions, row: 17}
    status: CRITICAL
    gap_register_entry: GAP-02
    notes: The workflow the composition holds for reinstate physical copy means something other than the ledger decides, so its successor takes the next unused version.
  - capability: The retrieve book details workflow
    source_finding: {phase: p3, register: authoring_decisions, row: 18}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: The search catalog workflow
    source_finding: {phase: p3, register: authoring_decisions, row: 19}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  gap_register:
  - gap_code: GAP-01
    source_finding: {phase: p3, register: authoring_decisions, row: 15}
    capability: The reinstate book record workflow
    owner_subdomain: catalog
    resolution: EXTEND
  - gap_code: GAP-02
    source_finding: {phase: p3, register: authoring_decisions, row: 17}
    capability: The reinstate physical copy workflow
    owner_subdomain: catalog
    resolution: EXTEND
  authoring_scope:
  - capability: The reinstate book record workflow
    gap_register_ref: GAP-01
  - capability: The reinstate physical copy workflow
    gap_register_ref: GAP-02
  dependency_graph:
  - from: book_library_mgmt
    to: capability_side_effects::CS_APPENDONLY_JSONL_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 1}
  - from: book_library_mgmt
    to: capability_side_effects::CS_MUTABLE_JSON_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 2}
  - from: book_library_mgmt
    to: capability_side_effects::CS_REGISTRY_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 3}
  - from: book_library_mgmt
    to: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 4}
  - from: book_library_mgmt
    to: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 5}
  - from: book_library_mgmt
    to: capability_transforms::CT_PURE_SELECT_RECORDS_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 6}
  - from: book_library_mgmt
    to: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 7}
  - from: book_library_mgmt
    to: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 8}
  - from: book_library_mgmt
    to: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 9}
  constraint_register:
  - number: '1'
    constraint: No two works share their title and author.
    source_finding: {phase: p1, register: business_invariants, row: 1}
    source: invariant
  - number: '2'
    constraint: No two books share their title, author and publication year.
    source_finding: {phase: p1, register: business_invariants, row: 2}
    source: invariant
  - number: '3'
    constraint: Each book belongs to exactly one work.
    source_finding: {phase: p1, register: business_invariants, row: 3}
    source: invariant
  - number: '4'
    constraint: No two physical copies share their barcode.
    source_finding: {phase: p1, register: business_invariants, row: 4}
    source: invariant
  - number: '5'
    constraint: Each physical copy belongs to exactly one book.
    source_finding: {phase: p1, register: business_invariants, row: 5}
    source: invariant
  - number: '6'
    constraint: Update bibliographic information never changes a book's state.
    source_finding: {phase: p1, register: business_invariants, row: 6}
    source: invariant
  - number: '7'
    constraint: Every catalog operation records operation, staff id and subject on the catalog trail, and no entry is changed or removed.
    source_finding: {phase: p1, register: business_invariants, row: 7}
    source: invariant
  design_decisions:
  - number: '1'
    decision: catalog stays the subdomain it is; the derived design extends it.
    source_finding: {phase: p3, register: placement_decision, row: 1}
    rationale: The composition already holds catalog; the derived design keeps its binding and its entrances.
    constraints_imposed: The binding and entrances callers meet keep their names.
  - number: '2'
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
