# Stage 5 — Business Intent — book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p5
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_06_catalog_derived
  rule_set: transformation.schemas.REGISTER_SCHEMA_P5_V0
registers:
  subdomain_purpose: The catalog governs the library's single authoritative record for each work, each edition it holds and each physical copy it owns. It exists because a community library holding thousands of books maintains its catalog records manually, which produces inconsistent descriptions, duplicate entries and difficulty locating materials. It owns the description of what the library holds and the operations that maintain that description, and it governs none of the nine remaining functions of the library project.
  purpose_provenance:
  - source: Change seed §0 Subdomain Purpose
    disposition: INHERITED
    refinement: null
  subdomain_purposes:
  - subdomain: catalog
    purpose: The catalog governs the library's single authoritative record for each work, each edition it holds and each physical copy it owns. It exists because a community library holding thousands of books maintains its catalog records manually, which produces inconsistent descriptions, duplicate entries and difficulty locating materials. It owns the description of what the library holds and the operations that maintain that description, and it governs none of the nine remaining functions of the library project.
    source_finding: {phase: p0, register: cr_type, row: 1}
  scope_boundary:
  - capability: Register book
    status: IN_SCOPE
    notes: Records a new book and physical copy
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - capability: Register additional edition
    status: IN_SCOPE
    notes: Records a new book
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - capability: Register physical copy
    status: IN_SCOPE
    notes: Records a new physical copy
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  - capability: Update bibliographic information
    status: IN_SCOPE
    notes: Changes a book's title, author, publication year and subject
    source_finding: {phase: p0, register: requested_outcomes, row: 4}
  - capability: Retire book record
    status: IN_SCOPE
    notes: Moves a book from registered to retired
    source_finding: {phase: p0, register: requested_outcomes, row: 5}
  - capability: Reinstate book record
    status: IN_SCOPE
    notes: Moves a book from retired to registered
    source_finding: {phase: p0, register: requested_outcomes, row: 6}
  - capability: Retire physical copy
    status: IN_SCOPE
    notes: Moves a physical copy from registered to retired
    source_finding: {phase: p0, register: requested_outcomes, row: 7}
  - capability: Reinstate physical copy
    status: IN_SCOPE
    notes: Moves a physical copy from retired to registered
    source_finding: {phase: p0, register: requested_outcomes, row: 8}
  - capability: Retrieve book details
    status: IN_SCOPE
    notes: Returns one book, with its works and physical copies
    source_finding: {phase: p0, register: requested_outcomes, row: 9}
  - capability: Search catalog
    status: IN_SCOPE
    notes: Returns the books that match
    source_finding: {phase: p0, register: requested_outcomes, row: 10}
  - capability: Circulation, patrons, staff, reservations, acquisitions, inventory, notifications, policy and reporting
    status: DEFERRED
    notes: The nine remaining functions of the library project; this domain is the catalog only.
    source_finding: {phase: p0, register: out_of_scope, row: 1}
  - capability: Deciding which staff are authorized
    status: DEFERRED
    notes: That belongs to the staff function; the catalog reads authorization and never grants it.
    source_finding: {phase: p0, register: out_of_scope, row: 2}
  - capability: Retirement of a work
    status: DEFERRED
    notes: A work is not retired; a work whose editions are all retired is simply that.
    source_finding: {phase: p0, register: out_of_scope, row: 3}
  - capability: Import of the records staff maintain manually today
    status: DEFERRED
    notes: The catalog starts empty.
    source_finding: {phase: p0, register: out_of_scope, row: 4}
  business_objects:
  - store_name: Work record
    record_model: MUTABLE_STATE
    business_rationale: A published work, recognizable as one thing across the editions in which it is published, so staff find every edition of it together.
    source_finding: {phase: p0, register: business_vocabulary, row: 1}
  - store_name: Work identity registry
    record_model: IDENTITY_REGISTRY
    business_rationale: Telling one work from another needs a claim on its identity at the moment it is recorded.
    source_finding: {phase: p0, register: identity_and_sameness, row: 1}
  - store_name: Book record
    record_model: MUTABLE_STATE
    business_rationale: 'An edition the library catalogs: the single authoritative description of one publication of a work, so the catalog describes what the library holds as it actually is.'
    source_finding: {phase: p0, register: business_vocabulary, row: 2}
  - store_name: Book identity registry
    record_model: IDENTITY_REGISTRY
    business_rationale: Telling one book from another needs a claim on its identity at the moment it is recorded.
    source_finding: {phase: p0, register: identity_and_sameness, row: 2}
  - store_name: Physical copy record
    record_model: MUTABLE_STATE
    business_rationale: An individual copy the library owns, belonging to exactly one edition and told apart from every other copy by its barcode.
    source_finding: {phase: p0, register: business_vocabulary, row: 3}
  - store_name: Physical copy identity registry
    record_model: IDENTITY_REGISTRY
    business_rationale: Telling one physical copy from another needs a claim on its identity at the moment it is recorded.
    source_finding: {phase: p0, register: identity_and_sameness, row: 3}
  - store_name: Audit trail of catalog
    record_model: APPEND_ONLY_JOURNAL
    business_rationale: Every operation must be traceable afterwards, and a trail that could be amended would not be evidence.
    source_finding: {phase: p0, register: business_invariants, row: 7}
  identity_semantics:
  - store_name: Work record
    identity_field: Title and author
    source: Supplied with the request
    uniqueness_rule: Two works are the same when they carry the same title and author, without regard to letter case or repeated spacing.
    cross_subdomain_relationship: None
    source_finding: {phase: p0, register: identity_and_sameness, row: 1}
  - store_name: Book record
    identity_field: Title, author and publication year
    source: Supplied with the request
    uniqueness_rule: Two books are the same when they carry the same title, author and publication year, without regard to letter case or repeated spacing.
    cross_subdomain_relationship: Names exactly one work
    source_finding: {phase: p0, register: identity_and_sameness, row: 2}
  - store_name: Physical copy record
    identity_field: Barcode
    source: Supplied with the request
    uniqueness_rule: Two physical copies are the same when they carry the same barcode.
    cross_subdomain_relationship: Names exactly one book
    source_finding: {phase: p0, register: identity_and_sameness, row: 3}
  invariants:
  - invariant: No two works share their title and author.
    business_reason: Two works that are the same would describe one work twice.
    source_finding: {phase: p0, register: business_invariants, row: 1}
  - invariant: No two books share their title, author and publication year.
    business_reason: Two books that are the same would describe one book twice.
    source_finding: {phase: p0, register: business_invariants, row: 2}
  - invariant: Each book belongs to exactly one work.
    business_reason: A book recorded against two works would make the record untrue.
    source_finding: {phase: p0, register: business_invariants, row: 3}
  - invariant: No two physical copies share their barcode.
    business_reason: Two physical copies that are the same would describe one physical copy twice.
    source_finding: {phase: p0, register: business_invariants, row: 4}
  - invariant: Each physical copy belongs to exactly one book.
    business_reason: A physical copy recorded against two books would make the record untrue.
    source_finding: {phase: p0, register: business_invariants, row: 5}
  - invariant: Update bibliographic information never changes a book's state.
    business_reason: Update bibliographic information changes only what it is for.
    source_finding: {phase: p0, register: business_invariants, row: 6}
  - invariant: Every catalog operation records operation, staff id and subject on the catalog trail, and no entry is changed or removed.
    business_reason: Every operation must be traceable afterwards, and a trail that could be amended would not be evidence.
    source_finding: {phase: p0, register: business_invariants, row: 7}
  actions:
  - action: Register book
    object: book and physical copy
    trigger: Requested by the library staff
    status: IN_SCOPE
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - action: Register additional edition
    object: book
    trigger: Requested by the library staff
    status: IN_SCOPE
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - action: Register physical copy
    object: physical copy
    trigger: Requested by the library staff
    status: IN_SCOPE
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  - action: Update bibliographic information
    object: book
    trigger: Requested by the library staff
    status: IN_SCOPE
    source_finding: {phase: p0, register: requested_outcomes, row: 4}
  - action: Retire book record
    object: book
    trigger: Requested by the library staff
    status: IN_SCOPE
    source_finding: {phase: p0, register: requested_outcomes, row: 5}
  - action: Reinstate book record
    object: book
    trigger: Requested by the library staff
    status: IN_SCOPE
    source_finding: {phase: p0, register: requested_outcomes, row: 6}
  - action: Retire physical copy
    object: physical copy
    trigger: Requested by the library staff
    status: IN_SCOPE
    source_finding: {phase: p0, register: requested_outcomes, row: 7}
  - action: Reinstate physical copy
    object: physical copy
    trigger: Requested by the library staff
    status: IN_SCOPE
    source_finding: {phase: p0, register: requested_outcomes, row: 8}
  - action: Retrieve book details
    object: book
    trigger: Requested by the library staff
    status: IN_SCOPE
    source_finding: {phase: p0, register: requested_outcomes, row: 9}
  - action: Search catalog
    object: book
    trigger: Requested by the library staff
    status: IN_SCOPE
    source_finding: {phase: p0, register: requested_outcomes, row: 10}
  provisional_codes:
  - subdomain: catalog
    provisional_code: WF_REGISTER_BOOK_V0
    family: WF
    summary: Records a new book and physical copy
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - subdomain: catalog
    provisional_code: WF_REGISTER_ADDITIONAL_EDITION_V0
    family: WF
    summary: Records a new book
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - subdomain: catalog
    provisional_code: WF_REGISTER_PHYSICAL_COPY_V0
    family: WF
    summary: Records a new physical copy
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  - subdomain: catalog
    provisional_code: WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    family: WF
    summary: Changes a book's title, author, publication year and subject
    source_finding: {phase: p0, register: requested_outcomes, row: 4}
  - subdomain: catalog
    provisional_code: WF_RETIRE_BOOK_RECORD_V0
    family: WF
    summary: Moves a book from registered to retired
    source_finding: {phase: p0, register: requested_outcomes, row: 5}
  - subdomain: catalog
    provisional_code: WF_REINSTATE_BOOK_RECORD_V0
    family: WF
    summary: Moves a book from retired to registered
    source_finding: {phase: p0, register: requested_outcomes, row: 6}
  - subdomain: catalog
    provisional_code: WF_RETIRE_PHYSICAL_COPY_V0
    family: WF
    summary: Moves a physical copy from registered to retired
    source_finding: {phase: p0, register: requested_outcomes, row: 7}
  - subdomain: catalog
    provisional_code: WF_REINSTATE_PHYSICAL_COPY_V0
    family: WF
    summary: Moves a physical copy from retired to registered
    source_finding: {phase: p0, register: requested_outcomes, row: 8}
  - subdomain: catalog
    provisional_code: WF_RETRIEVE_BOOK_DETAILS_V0
    family: WF
    summary: Returns one book, with its works and physical copies
    source_finding: {phase: p0, register: requested_outcomes, row: 9}
  - subdomain: catalog
    provisional_code: WF_SEARCH_CATALOG_V0
    family: WF
    summary: Returns the books that match
    source_finding: {phase: p0, register: requested_outcomes, row: 10}
  cross_subdomain_refs: []
```

Projected from the change seed, which is projected from the decision ledger. Every row cites the seed row it restates.

---

## 1. Subdomain Purpose

---

## 2. Scope Boundary

---

## 3. Business Objects

---

## 4. Identity Semantics

---

## 5. Business Invariants

---

## 6. Business Actions

---

## 7. Provisional Artifact Codes

---

## 8. Cross-Subdomain References

---

## gov_projection — Governed Handoff to Stage 6

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Change seed | actions · business_objects · cross_subdomain_refs · identity_semantics · invariants · provisional_codes · purpose_provenance · scope_boundary · subdomain_purpose · subdomain_purposes |
| **Emits** → Stage 6 | subdomain_purpose · purpose_provenance · subdomain_purposes · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
