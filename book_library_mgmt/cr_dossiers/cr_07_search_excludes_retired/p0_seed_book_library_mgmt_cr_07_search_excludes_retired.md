# Change Seed — book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p0
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_07_search_excludes_retired
  rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0
registers:
  subdomain_purpose: The catalog governs the library's single authoritative record for each work, each edition it holds and each physical copy it owns. It exists because a community library holding thousands of books maintains its catalog records manually, which produces inconsistent descriptions, duplicate entries and difficulty locating materials. It owns the description of what the library holds and the operations that maintain that description, and it governs none of the nine remaining functions of the library project.
  cr_type:
  - subdomain: catalog
    classification: MODIFY
    rationale: The catalog governs the library's single authoritative record for each work, each edition it holds and each physical copy it owns. It exists because a community library holding thousands of books maintains its catalog records manually, which produces inconsistent descriptions, duplicate entries and difficulty locating materials. It owns the description of what the library holds and the operations that maintain that description, and it governs none of the nine remaining functions of the library project.
  business_vocabulary:
  - term: Work
    definition: A published work, recognizable as one thing across the editions in which it is published, so staff find every edition of it together.
  - term: Book
    definition: 'An edition the library catalogs: the single authoritative description of one publication of a work, so the catalog describes what the library holds as it actually is.'
  - term: Physical copy
    definition: An individual copy the library owns, belonging to exactly one edition and told apart from every other copy by its barcode.
  requested_outcomes:
  - outcome: 'Register book: records a new book and physical copy.'
  - outcome: 'Register additional edition: records a new book.'
  - outcome: 'Register physical copy: records a new physical copy.'
  - outcome: 'Update bibliographic information: changes a book''s title, author, publication year and subject.'
  - outcome: 'Retire book record: moves a book from registered to retired.'
  - outcome: 'Reinstate book record: moves a book from retired to registered.'
  - outcome: 'Retire physical copy: moves a physical copy from registered to retired.'
  - outcome: 'Reinstate physical copy: moves a physical copy from retired to registered.'
  - outcome: 'Retrieve book details: returns one book, with its works and physical copies.'
  - outcome: 'Search catalog: returns the books that match.'
  known_facts:
  - fact: A work is identified by its title and author.
    certainty: HIGH
  - fact: A book is identified by its title, author and publication year.
    certainty: HIGH
  - fact: A physical copy is identified by its barcode.
    certainty: HIGH
  system_beliefs:
  - belief: The current catalog design names the records, entrances and requests its callers use today.
    why_it_matters: The derived design keeps those names, so a caller meets no change the ledger did not decide.
    verification_goal: Read the catalog baseline design and find there each name the derived design carries.
  assumptions: []
  constraints: []
  business_invariants:
  - invariant: No two works share their title and author.
  - invariant: No two books share their title, author and publication year.
  - invariant: Each book belongs to exactly one work.
  - invariant: No two physical copies share their barcode.
  - invariant: Each physical copy belongs to exactly one book.
  - invariant: Update bibliographic information never changes a book's state.
  - invariant: Every catalog operation records operation, staff id and subject on the catalog trail, and no entry is changed or removed.
  lifecycle_states:
  - object: book
    state: registered
    meaning: A book is registered after register book, register additional edition and reinstate book record.
  - object: book
    state: retired
    meaning: A book is retired after retire book record.
  - object: physical copy
    state: registered
    meaning: A physical copy is registered after register book, register physical copy and reinstate physical copy.
  - object: physical copy
    state: retired
    meaning: A physical copy is retired after retire physical copy.
  business_events:
  - event: Work registered
    when_it_occurs: When register book completes
    significance: Others learn that register book completed without reading the catalog records.
  - event: Book registered
    when_it_occurs: When register book completes
    significance: Others learn that register book completed without reading the catalog records.
  - event: Physical copy registered
    when_it_occurs: When register book completes
    significance: Others learn that register book completed without reading the catalog records.
  - event: Book registered
    when_it_occurs: When register additional edition completes
    significance: Others learn that register additional edition completed without reading the catalog records.
  - event: Physical copy registered
    when_it_occurs: When register physical copy completes
    significance: Others learn that register physical copy completed without reading the catalog records.
  - event: Bibliographic information updated
    when_it_occurs: When update bibliographic information completes
    significance: Others learn that update bibliographic information completed without reading the catalog records.
  - event: Book retired
    when_it_occurs: When retire book record completes
    significance: Others learn that retire book record completed without reading the catalog records.
  - event: Physical copy retired
    when_it_occurs: When retire physical copy completes
    significance: Others learn that retire physical copy completed without reading the catalog records.
  authority_boundaries:
  - business_object: work
    authoritative_owner: catalog
  - business_object: book
    authoritative_owner: catalog
  - business_object: physical copy
    authoritative_owner: catalog
  out_of_scope:
  - item: Circulation, patrons, staff, reservations, acquisitions, inventory, notifications, policy and reporting
    reason: The nine remaining functions of the library project; this domain is the catalog only.
  - item: Deciding which staff are authorized
    reason: That belongs to the staff function; the catalog reads authorization and never grants it.
  - item: Retirement of a work
    reason: A work is not retired; a work whose editions are all retired is simply that.
  - item: Import of the records staff maintain manually today
    reason: The catalog starts empty.
  governance_scope:
  - scope_item: catalog
    relationship: MODIFIED
  clarification_requests: []
  acceptance_criteria:
  - criterion: Register book is refused when a book that is the same is already recorded.
  - criterion: Register book is refused when a physical copy that is the same is already recorded.
  - criterion: Register additional edition is refused when a book that is the same is already recorded.
  - criterion: Register additional edition is refused when the work it belongs to is not recorded.
  - criterion: Register physical copy is refused when a physical copy that is the same is already recorded.
  - criterion: Register physical copy is refused when the book it belongs to is not recorded.
  - criterion: Update bibliographic information is refused when the book is not recorded.
  - criterion: Update bibliographic information is refused when the change would make the book the same as another.
  - criterion: Retire book record is refused when the book is not registered.
  - criterion: Reinstate book record is refused when the book is not retired.
  - criterion: Retire physical copy is refused when the physical copy is not registered.
  - criterion: Reinstate physical copy is refused when the physical copy is not retired.
  identity_and_sameness:
  - business_object: work
    identified_by: title and author
    two_are_the_same_when: they carry the same title and author, without regard to letter case or repeated spacing
  - business_object: book
    identified_by: title, author and publication year
    two_are_the_same_when: they carry the same title, author and publication year, without regard to letter case or repeated spacing
  - business_object: physical copy
    identified_by: barcode
    two_are_the_same_when: they carry the same barcode
  lifecycle_transitions:
  - object: book
    from_state: registered
    to_state: retired
    triggered_by: retire book record
    cascade: None
  - object: book
    from_state: retired
    to_state: registered
    triggered_by: reinstate book record
    cascade: None
  - object: physical copy
    from_state: registered
    to_state: retired
    triggered_by: retire physical copy
    cascade: None
  - object: physical copy
    from_state: retired
    to_state: registered
    triggered_by: reinstate physical copy
    cascade: None
  operation_refusals:
  - operation: register book
    refused_when: a book that is the same is already recorded
    business_reason: Two books that are the same would describe one book twice.
  - operation: register book
    refused_when: a physical copy that is the same is already recorded
    business_reason: Two physical copies that are the same would describe one physical copy twice.
  - operation: register additional edition
    refused_when: a book that is the same is already recorded
    business_reason: Two books that are the same would describe one book twice.
  - operation: register additional edition
    refused_when: the work it belongs to is not recorded
    business_reason: A book belongs to a recorded work.
  - operation: register physical copy
    refused_when: a physical copy that is the same is already recorded
    business_reason: Two physical copies that are the same would describe one physical copy twice.
  - operation: register physical copy
    refused_when: the book it belongs to is not recorded
    business_reason: A physical copy belongs to a recorded book.
  - operation: update bibliographic information
    refused_when: the book is not recorded
    business_reason: There is no book to act on.
  - operation: update bibliographic information
    refused_when: the change would make the book the same as another
    business_reason: Two books that are the same would describe one book twice.
  - operation: retire book record
    refused_when: the book is not registered
    business_reason: Only a registered book becomes retired.
  - operation: reinstate book record
    refused_when: the book is not retired
    business_reason: Only a retired book becomes registered.
  - operation: retire physical copy
    refused_when: the physical copy is not registered
    business_reason: Only a registered physical copy becomes retired.
  - operation: reinstate physical copy
    refused_when: the physical copy is not retired
    business_reason: Only a retired physical copy becomes registered.
  authority_deferrals: []
```

Projected from the decision ledger. Business prose (the purpose, each vocabulary definition, what is out of scope) is the ledger's own, word for word; every other row is said from the ledger's structure and claims nothing it does not state.

---

## 0. Subdomain Purpose

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

## gov_projection — Governed Handoff to Stage 1

| Direction | Fields |
|-----------|--------|
| **Consumes** ← the decision ledger | the owner's answers |
| **Emits** → Stage 1 | subdomain_purpose · cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
