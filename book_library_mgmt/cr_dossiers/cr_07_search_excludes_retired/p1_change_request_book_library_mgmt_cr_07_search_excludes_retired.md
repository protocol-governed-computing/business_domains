# Stage 1 — Change Request: Clarification & Fact Capture: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p1
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_07_search_excludes_retired
  rule_set: transformation.schemas.REGISTER_SCHEMA_P1_V0
registers:
  cr_type:
  - subdomain: catalog
    classification: MODIFY
    rationale: The catalog governs the library's single authoritative record for each work, each edition it holds and each physical copy it owns. It exists because a community library holding thousands of books maintains its catalog records manually, which produces inconsistent descriptions, duplicate entries and difficulty locating materials. It owns the description of what the library holds and the operations that maintain that description, and it governs none of the nine remaining functions of the library project.
    source_finding: {phase: p0, register: cr_type, row: 1}
  business_vocabulary:
  - term: Work
    definition: A published work, recognizable as one thing across the editions in which it is published, so staff find every edition of it together.
    source_finding: {phase: p0, register: business_vocabulary, row: 1}
  - term: Book
    definition: 'An edition the library catalogs: the single authoritative description of one publication of a work, so the catalog describes what the library holds as it actually is.'
    source_finding: {phase: p0, register: business_vocabulary, row: 2}
  - term: Physical copy
    definition: An individual copy the library owns, belonging to exactly one edition and told apart from every other copy by its barcode.
    source_finding: {phase: p0, register: business_vocabulary, row: 3}
  requested_outcomes:
  - outcome: 'Register book: records a new book and physical copy.'
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - outcome: 'Register additional edition: records a new book.'
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - outcome: 'Register physical copy: records a new physical copy.'
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  - outcome: 'Update bibliographic information: changes a book''s title, author, publication year and subject.'
    source_finding: {phase: p0, register: requested_outcomes, row: 4}
  - outcome: 'Retire book record: moves a book from registered to retired.'
    source_finding: {phase: p0, register: requested_outcomes, row: 5}
  - outcome: 'Reinstate book record: moves a book from retired to registered.'
    source_finding: {phase: p0, register: requested_outcomes, row: 6}
  - outcome: 'Retire physical copy: moves a physical copy from registered to retired.'
    source_finding: {phase: p0, register: requested_outcomes, row: 7}
  - outcome: 'Reinstate physical copy: moves a physical copy from retired to registered.'
    source_finding: {phase: p0, register: requested_outcomes, row: 8}
  - outcome: 'Retrieve book details: returns one book, with its works and physical copies.'
    source_finding: {phase: p0, register: requested_outcomes, row: 9}
  - outcome: 'Search catalog: returns the books that match.'
    source_finding: {phase: p0, register: requested_outcomes, row: 10}
  known_facts:
  - fact: A work is identified by its title and author.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 1}
  - fact: A book is identified by its title, author and publication year.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 2}
  - fact: A physical copy is identified by its barcode.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 3}
  system_beliefs:
  - belief: The current catalog design names the records, entrances and requests its callers use today.
    why_it_matters: The derived design keeps those names, so a caller meets no change the ledger did not decide.
    verification_goal: Read the catalog baseline design and find there each name the derived design carries.
    source_finding: {phase: p0, register: system_beliefs, row: 1}
  assumptions: []
  constraints: []
  business_invariants:
  - invariant: No two works share their title and author.
    source_finding: {phase: p0, register: business_invariants, row: 1}
  - invariant: No two books share their title, author and publication year.
    source_finding: {phase: p0, register: business_invariants, row: 2}
  - invariant: Each book belongs to exactly one work.
    source_finding: {phase: p0, register: business_invariants, row: 3}
  - invariant: No two physical copies share their barcode.
    source_finding: {phase: p0, register: business_invariants, row: 4}
  - invariant: Each physical copy belongs to exactly one book.
    source_finding: {phase: p0, register: business_invariants, row: 5}
  - invariant: Update bibliographic information never changes a book's state.
    source_finding: {phase: p0, register: business_invariants, row: 6}
  - invariant: Every catalog operation records operation, staff id and subject on the catalog trail, and no entry is changed or removed.
    source_finding: {phase: p0, register: business_invariants, row: 7}
  lifecycle_states:
  - object: book
    state: registered
    meaning: A book is registered after register book, register additional edition and reinstate book record.
    source_finding: {phase: p0, register: lifecycle_states, row: 1}
  - object: book
    state: retired
    meaning: A book is retired after retire book record.
    source_finding: {phase: p0, register: lifecycle_states, row: 2}
  - object: physical copy
    state: registered
    meaning: A physical copy is registered after register book, register physical copy and reinstate physical copy.
    source_finding: {phase: p0, register: lifecycle_states, row: 3}
  - object: physical copy
    state: retired
    meaning: A physical copy is retired after retire physical copy.
    source_finding: {phase: p0, register: lifecycle_states, row: 4}
  business_events:
  - event: Work registered
    when_it_occurs: When register book completes
    significance: Others learn that register book completed without reading the catalog records.
    source_finding: {phase: p0, register: business_events, row: 1}
  - event: Book registered
    when_it_occurs: When register book completes
    significance: Others learn that register book completed without reading the catalog records.
    source_finding: {phase: p0, register: business_events, row: 2}
  - event: Physical copy registered
    when_it_occurs: When register book completes
    significance: Others learn that register book completed without reading the catalog records.
    source_finding: {phase: p0, register: business_events, row: 3}
  - event: Book registered
    when_it_occurs: When register additional edition completes
    significance: Others learn that register additional edition completed without reading the catalog records.
    source_finding: {phase: p0, register: business_events, row: 4}
  - event: Physical copy registered
    when_it_occurs: When register physical copy completes
    significance: Others learn that register physical copy completed without reading the catalog records.
    source_finding: {phase: p0, register: business_events, row: 5}
  - event: Bibliographic information updated
    when_it_occurs: When update bibliographic information completes
    significance: Others learn that update bibliographic information completed without reading the catalog records.
    source_finding: {phase: p0, register: business_events, row: 6}
  - event: Book retired
    when_it_occurs: When retire book record completes
    significance: Others learn that retire book record completed without reading the catalog records.
    source_finding: {phase: p0, register: business_events, row: 7}
  - event: Physical copy retired
    when_it_occurs: When retire physical copy completes
    significance: Others learn that retire physical copy completed without reading the catalog records.
    source_finding: {phase: p0, register: business_events, row: 8}
  authority_boundaries:
  - business_object: work
    authoritative_owner: catalog
    source_finding: {phase: p0, register: authority_boundaries, row: 1}
  - business_object: book
    authoritative_owner: catalog
    source_finding: {phase: p0, register: authority_boundaries, row: 2}
  - business_object: physical copy
    authoritative_owner: catalog
    source_finding: {phase: p0, register: authority_boundaries, row: 3}
  out_of_scope:
  - item: Circulation, patrons, staff, reservations, acquisitions, inventory, notifications, policy and reporting
    reason: The nine remaining functions of the library project; this domain is the catalog only.
    source_finding: {phase: p0, register: out_of_scope, row: 1}
  - item: Deciding which staff are authorized
    reason: That belongs to the staff function; the catalog reads authorization and never grants it.
    source_finding: {phase: p0, register: out_of_scope, row: 2}
  - item: Retirement of a work
    reason: A work is not retired; a work whose editions are all retired is simply that.
    source_finding: {phase: p0, register: out_of_scope, row: 3}
  - item: Import of the records staff maintain manually today
    reason: The catalog starts empty.
    source_finding: {phase: p0, register: out_of_scope, row: 4}
  governance_scope:
  - scope_item: catalog
    relationship: MODIFIED
    source_finding: {phase: p0, register: governance_scope, row: 1}
  clarification_requests: []
  acceptance_criteria:
  - criterion: Register book is refused when a book that is the same is already recorded.
    source_finding: {phase: p0, register: acceptance_criteria, row: 1}
  - criterion: Register book is refused when a physical copy that is the same is already recorded.
    source_finding: {phase: p0, register: acceptance_criteria, row: 2}
  - criterion: Register additional edition is refused when a book that is the same is already recorded.
    source_finding: {phase: p0, register: acceptance_criteria, row: 3}
  - criterion: Register additional edition is refused when the work it belongs to is not recorded.
    source_finding: {phase: p0, register: acceptance_criteria, row: 4}
  - criterion: Register physical copy is refused when a physical copy that is the same is already recorded.
    source_finding: {phase: p0, register: acceptance_criteria, row: 5}
  - criterion: Register physical copy is refused when the book it belongs to is not recorded.
    source_finding: {phase: p0, register: acceptance_criteria, row: 6}
  - criterion: Update bibliographic information is refused when the book is not recorded.
    source_finding: {phase: p0, register: acceptance_criteria, row: 7}
  - criterion: Update bibliographic information is refused when the change would make the book the same as another.
    source_finding: {phase: p0, register: acceptance_criteria, row: 8}
  - criterion: Retire book record is refused when the book is not registered.
    source_finding: {phase: p0, register: acceptance_criteria, row: 9}
  - criterion: Reinstate book record is refused when the book is not retired.
    source_finding: {phase: p0, register: acceptance_criteria, row: 10}
  - criterion: Retire physical copy is refused when the physical copy is not registered.
    source_finding: {phase: p0, register: acceptance_criteria, row: 11}
  - criterion: Reinstate physical copy is refused when the physical copy is not retired.
    source_finding: {phase: p0, register: acceptance_criteria, row: 12}
  identity_and_sameness:
  - business_object: work
    identified_by: title and author
    two_are_the_same_when: they carry the same title and author, without regard to letter case or repeated spacing
    source_finding: {phase: p0, register: identity_and_sameness, row: 1}
  - business_object: book
    identified_by: title, author and publication year
    two_are_the_same_when: they carry the same title, author and publication year, without regard to letter case or repeated spacing
    source_finding: {phase: p0, register: identity_and_sameness, row: 2}
  - business_object: physical copy
    identified_by: barcode
    two_are_the_same_when: they carry the same barcode
    source_finding: {phase: p0, register: identity_and_sameness, row: 3}
  lifecycle_transitions:
  - object: book
    from_state: registered
    to_state: retired
    triggered_by: retire book record
    cascade: None
    source_finding: {phase: p0, register: lifecycle_transitions, row: 1}
  - object: book
    from_state: retired
    to_state: registered
    triggered_by: reinstate book record
    cascade: None
    source_finding: {phase: p0, register: lifecycle_transitions, row: 2}
  - object: physical copy
    from_state: registered
    to_state: retired
    triggered_by: retire physical copy
    cascade: None
    source_finding: {phase: p0, register: lifecycle_transitions, row: 3}
  - object: physical copy
    from_state: retired
    to_state: registered
    triggered_by: reinstate physical copy
    cascade: None
    source_finding: {phase: p0, register: lifecycle_transitions, row: 4}
  operation_refusals:
  - operation: register book
    refused_when: a book that is the same is already recorded
    business_reason: Two books that are the same would describe one book twice.
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: register book
    refused_when: a physical copy that is the same is already recorded
    business_reason: Two physical copies that are the same would describe one physical copy twice.
    source_finding: {phase: p0, register: operation_refusals, row: 2}
  - operation: register additional edition
    refused_when: a book that is the same is already recorded
    business_reason: Two books that are the same would describe one book twice.
    source_finding: {phase: p0, register: operation_refusals, row: 3}
  - operation: register additional edition
    refused_when: the work it belongs to is not recorded
    business_reason: A book belongs to a recorded work.
    source_finding: {phase: p0, register: operation_refusals, row: 4}
  - operation: register physical copy
    refused_when: a physical copy that is the same is already recorded
    business_reason: Two physical copies that are the same would describe one physical copy twice.
    source_finding: {phase: p0, register: operation_refusals, row: 5}
  - operation: register physical copy
    refused_when: the book it belongs to is not recorded
    business_reason: A physical copy belongs to a recorded book.
    source_finding: {phase: p0, register: operation_refusals, row: 6}
  - operation: update bibliographic information
    refused_when: the book is not recorded
    business_reason: There is no book to act on.
    source_finding: {phase: p0, register: operation_refusals, row: 7}
  - operation: update bibliographic information
    refused_when: the change would make the book the same as another
    business_reason: Two books that are the same would describe one book twice.
    source_finding: {phase: p0, register: operation_refusals, row: 8}
  - operation: retire book record
    refused_when: the book is not registered
    business_reason: Only a registered book becomes retired.
    source_finding: {phase: p0, register: operation_refusals, row: 9}
  - operation: reinstate book record
    refused_when: the book is not retired
    business_reason: Only a retired book becomes registered.
    source_finding: {phase: p0, register: operation_refusals, row: 10}
  - operation: retire physical copy
    refused_when: the physical copy is not registered
    business_reason: Only a registered physical copy becomes retired.
    source_finding: {phase: p0, register: operation_refusals, row: 11}
  - operation: reinstate physical copy
    refused_when: the physical copy is not retired
    business_reason: Only a retired physical copy becomes registered.
    source_finding: {phase: p0, register: operation_refusals, row: 12}
  authority_deferrals: []
```

Projected from the change seed. Every row is the seed's own, cited to the section it was
said in. S1 interrogates and does not author: a question raised by restating the seed
amends the seed and is projected again, so no row here states business content the seed
does not.

---

## 1. CR Type

---

## 2. Business Vocabulary

---

## 3. Requested Outcomes

---

## 4. Known Facts — Business Truths

---

## 5. Existing-System Beliefs — Requiring Verification

---

## 6. Assumptions

---

## 7. Constraints

---

## 8. Business Invariants

---

## 9. Lifecycle States

---

## 10. Business Events

---

## 11. Authority Boundaries

---

## 12. Out of Scope

---

## 13. Governance Scope

---

## 14. Clarification Requests

---

## 15. Acceptance Criteria

---

## 16. Identity and Sameness

---

## 17. Lifecycle Transitions

---

## 18. Operation Refusals

---

## 19. Authority Deferrals

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
