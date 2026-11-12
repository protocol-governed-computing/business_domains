# Stage 2 — Domain Model — book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p2
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_09_reinstatement_announces
  rule_set: transformation.schemas.REGISTER_SCHEMA_P2_V0
registers:
  entities:
  - entity: Work
    description: A published work, recognizable as one thing across the editions in which it is published, so staff find every edition of it together.
    store_model: One durable record per work, addressed by its title and author.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_vocabulary, row: 1}
  - entity: Book
    description: 'An edition the library catalogs: the single authoritative description of one publication of a work, so the catalog describes what the library holds as it actually is.'
    store_model: One durable record per book, addressed by its title, author and publication year, updated in place, carrying its own state (registered and retired).
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_vocabulary, row: 2}
  - entity: Physical copy
    description: An individual copy the library owns, belonging to exactly one edition and told apart from every other copy by its barcode.
    store_model: One durable record per physical copy, addressed by its barcode, updated in place, carrying its own state (registered and retired).
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_vocabulary, row: 3}
  entity_attributes:
  - entity: Work
    attribute: Title
    meaning: What identifies a work.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: identity_and_sameness, row: 1}
  - entity: Work
    attribute: Author
    meaning: What identifies a work.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: identity_and_sameness, row: 1}
  - entity: Book
    attribute: Title
    meaning: What identifies a book.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: identity_and_sameness, row: 2}
  - entity: Book
    attribute: Author
    meaning: What identifies a book.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: identity_and_sameness, row: 2}
  - entity: Book
    attribute: Publication year
    meaning: What identifies a book.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: identity_and_sameness, row: 2}
  - entity: Book
    attribute: Subject
    meaning: Required when a book is recorded, as a list.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_vocabulary, row: 2}
  - entity: Physical copy
    attribute: Barcode
    meaning: What identifies a physical copy.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: identity_and_sameness, row: 3}
  business_processes:
  - process: Register book
    initiator: Library staff
    outcome: Records a new book and physical copy.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  - process: Register additional edition
    initiator: Library staff
    outcome: Records a new book.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 2}
  - process: Register physical copy
    initiator: Library staff
    outcome: Records a new physical copy.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 3}
  - process: Update bibliographic information
    initiator: Library staff
    outcome: Changes a book's title, author, publication year and subject.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 4}
  - process: Retire book record
    initiator: Library staff
    outcome: Moves a book from registered to retired.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 5}
  - process: Reinstate book record
    initiator: Library staff
    outcome: Moves a book from retired to registered.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 6}
  - process: Retire physical copy
    initiator: Library staff
    outcome: Moves a physical copy from registered to retired.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 7}
  - process: Reinstate physical copy
    initiator: Library staff
    outcome: Moves a physical copy from retired to registered.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 8}
  - process: Retrieve book details
    initiator: Library staff
    outcome: Returns one book, with its works and physical copies.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 9}
  - process: Search catalog
    initiator: Library staff
    outcome: Returns the books that match.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 10}
  process_steps:
  - process: Register book
    step: '1'
    action: Refuse when a book that is the same is already recorded
    record_produced: A refusal, and nothing recorded
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 1}
  - process: Register book
    step: '2'
    action: Refuse when a physical copy that is the same is already recorded
    record_produced: A refusal, and nothing recorded
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 2}
  - process: Register book
    step: '3'
    action: Records a new book and physical copy
    record_produced: The book and physical copy record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  - process: Register book
    step: '4'
    action: Record the operation on the catalog trail
    record_produced: A trail entry
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  - process: Register additional edition
    step: '1'
    action: Refuse when a book that is the same is already recorded
    record_produced: A refusal, and nothing recorded
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 3}
  - process: Register additional edition
    step: '2'
    action: Refuse when the work it belongs to is not recorded
    record_produced: A refusal, and nothing recorded
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 4}
  - process: Register additional edition
    step: '3'
    action: Records a new book
    record_produced: The book record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 2}
  - process: Register additional edition
    step: '4'
    action: Record the operation on the catalog trail
    record_produced: A trail entry
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 2}
  - process: Register physical copy
    step: '1'
    action: Refuse when a physical copy that is the same is already recorded
    record_produced: A refusal, and nothing recorded
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 5}
  - process: Register physical copy
    step: '2'
    action: Refuse when the book it belongs to is not recorded
    record_produced: A refusal, and nothing recorded
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 6}
  - process: Register physical copy
    step: '3'
    action: Records a new physical copy
    record_produced: The physical copy record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 3}
  - process: Register physical copy
    step: '4'
    action: Record the operation on the catalog trail
    record_produced: A trail entry
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 3}
  - process: Update bibliographic information
    step: '1'
    action: Refuse when the book is not recorded
    record_produced: A refusal, and nothing recorded
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 7}
  - process: Update bibliographic information
    step: '2'
    action: Refuse when the change would make the book the same as another
    record_produced: A refusal, and nothing recorded
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 8}
  - process: Update bibliographic information
    step: '3'
    action: Changes a book's title, author, publication year and subject
    record_produced: The book record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 4}
  - process: Update bibliographic information
    step: '4'
    action: Record the operation on the catalog trail
    record_produced: A trail entry
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 4}
  - process: Retire book record
    step: '1'
    action: Refuse when the book is not registered
    record_produced: A refusal, and nothing recorded
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 9}
  - process: Retire book record
    step: '2'
    action: Moves a book from registered to retired
    record_produced: The book record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 5}
  - process: Retire book record
    step: '3'
    action: Record the operation on the catalog trail
    record_produced: A trail entry
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 5}
  - process: Reinstate book record
    step: '1'
    action: Refuse when the book is not retired
    record_produced: A refusal, and nothing recorded
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 10}
  - process: Reinstate book record
    step: '2'
    action: Moves a book from retired to registered
    record_produced: The book record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 6}
  - process: Reinstate book record
    step: '3'
    action: Record the operation on the catalog trail
    record_produced: A trail entry
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 6}
  - process: Retire physical copy
    step: '1'
    action: Refuse when the physical copy is not registered
    record_produced: A refusal, and nothing recorded
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 11}
  - process: Retire physical copy
    step: '2'
    action: Moves a physical copy from registered to retired
    record_produced: The physical copy record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 7}
  - process: Retire physical copy
    step: '3'
    action: Record the operation on the catalog trail
    record_produced: A trail entry
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 7}
  - process: Reinstate physical copy
    step: '1'
    action: Refuse when the physical copy is not retired
    record_produced: A refusal, and nothing recorded
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 12}
  - process: Reinstate physical copy
    step: '2'
    action: Moves a physical copy from retired to registered
    record_produced: The physical copy record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 8}
  - process: Reinstate physical copy
    step: '3'
    action: Record the operation on the catalog trail
    record_produced: A trail entry
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 8}
  - process: Retrieve book details
    step: '1'
    action: Returns one book, with its works and physical copies
    record_produced: The book record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 9}
  - process: Retrieve book details
    step: '2'
    action: Record the operation on the catalog trail
    record_produced: A trail entry
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 9}
  - process: Search catalog
    step: '1'
    action: Returns the books that match
    record_produced: The book record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 10}
  - process: Search catalog
    step: '2'
    action: Record the operation on the catalog trail
    record_produced: A trail entry
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 10}
  belief_verification:
  - belief: The current catalog design names the records, entrances and requests its callers use today.
    result: VERIFIED
    evidence: The baseline design names book_library_mgmt::RB_CATALOG_BINDINGS_V0, book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 and book_library_mgmt::IN_REGISTER_BOOK_V0, and the derived design carries them.
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  pps_baseline_fqdns:
  - capability: Appendonly jsonl side effect, as the platform declares it
    fqdn: capability_side_effects::CS_APPENDONLY_JSONL_V0
    what_it_does: Provide an append-only JSONL persistence layer with ordered event history.
    fit: EXACT
    cannot_do: 'Nothing this design asks of it: every step the derived design binds to it uses an operation it declares.'
  - capability: Mutable json side effect, as the platform declares it
    fqdn: capability_side_effects::CS_MUTABLE_JSON_V0
    what_it_does: Provide a mutable key-addressable JSON state store with last-write-wins semantics.
    fit: EXACT
    cannot_do: 'Nothing this design asks of it: every step the derived design binds to it uses an operation it declares.'
  - capability: Registry side effect, as the platform declares it
    fqdn: capability_side_effects::CS_REGISTRY_V0
    what_it_does: Provide a registry capability for stable indirection by binding symbolic keys to opaque addresses and underlying storage references.
    fit: EXACT
    cannot_do: 'Nothing this design asks of it: every step the derived design binds to it uses an operation it declares.'
  - capability: Assemble record transform, as the platform declares it
    fqdn: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    what_it_does: Combines multiple input values into a single structured record object.
    fit: EXACT
    cannot_do: 'Nothing this design asks of it: every step the derived design binds to it uses an operation it declares.'
  - capability: Compare equal transform, as the platform declares it
    fqdn: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
    what_it_does: Compare two values for equality.
    fit: EXACT
    cannot_do: 'Nothing this design asks of it: every step the derived design binds to it uses an operation it declares.'
  - capability: Select records transform, as the platform declares it
    fqdn: capability_transforms::CT_PURE_SELECT_RECORDS_V0
    what_it_does: Select the records of an array that satisfy declared field criteria, and answer none when none do.
    fit: EXACT
    cannot_do: 'Nothing this design asks of it: every step the derived design binds to it uses an operation it declares.'
  - capability: Validate parameter rules transform, as the platform declares it
    fqdn: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    what_it_does: Evaluate declarative parameter constraint rules against a parameter map.
    fit: EXACT
    cannot_do: 'Nothing this design asks of it: every step the derived design binds to it uses an operation it declares.'
  - capability: Validate record structure transform, as the platform declares it
    fqdn: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    what_it_does: Validate a record against a provided schema of field validation rules.
    fit: EXACT
    cannot_do: 'Nothing this design asks of it: every step the derived design binds to it uses an operation it declares.'
  - capability: Validate set membership transform, as the platform declares it
    fqdn: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    what_it_does: Validate that a value is a member of a declared set.
    fit: EXACT
    cannot_do: 'Nothing this design asks of it: every step the derived design binds to it uses an operation it declares.'
  gaps:
  - gap: The composition holds none of 2 artifacts the ledger's decisions need.
    severity: CRITICAL
    impact: They are authored by this change.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  - gap: 4 artifacts the composition holds mean something other than the ledger decides.
    severity: MAJOR
    impact: Each takes the next unused version and names its predecessor as superseded.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  architectural_observations:
  - observation: The catalog design keeps its records through one binding, and the derived design carries its name.
    evidence: book_library_mgmt::RB_CATALOG_BINDINGS_V0 · book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - observation: 51 artifacts the composition holds mean what the ledger decides, and keep their identity.
    evidence: book_library_mgmt::AC_LIBRARY_STAFF_V0 · book_library_mgmt::CC_CHECK_REGISTER_ADDITIONAL_EDITION_SUBMISSION_V0 · book_library_mgmt::CC_CHECK_REGISTER_BOOK_SUBMISSION_V0
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  discovery_concerns:
  - concern: 4 artifacts change meaning, so a caller that dispatches by identity must follow supersedes.
    evidence: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0 · book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V1 · book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0 · book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V1
    severity: MAJOR
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  open_questions: []
```

Projected from what the derivation observed: the baseline design, the derived design and the composition the inspector reads. Every row cites the change-request row it models.

---

## 1. Business Entities

---

## 2. Business Processes

---

## 3. Belief Verification — THE SPINE (fill this register FIRST)

---

## 4. PPS Baseline — What Already Exists

---

## 5. Gap Analysis — What Is Missing

---

## 6. Architectural Observations

---

## 7. Discovery Concerns

---

## 8. Open Questions for Stage 3

---

## gov_projection — Governed Handoff to Stage 3

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 1 | architectural_observations · belief_verification · business_processes · discovery_concerns · entities · entity_attributes · gaps · open_questions · pps_baseline_fqdns · process_steps |
| **Emits** → Stage 3 | entities · entity_attributes · business_processes · process_steps · belief_verification · pps_baseline_fqdns · gaps · architectural_observations · discovery_concerns · open_questions |
