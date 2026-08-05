# Change Seed — book_library_mgmt / catalog

**Stage:** 0 — Change Seed
**CR:** cr_01_catalog
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`. Human input only — nothing here was
added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The Catalog subdomain governs the authoritative description of what the library holds: each
bibliographic work the library has cataloged, and each physical copy the library owns. It exists
because catalog records are maintained by hand today, which produces inconsistent descriptions,
duplicate entries, and difficulty locating materials. It owns the description of the collection and
the operations that maintain that description; it does not govern who borrows the collection, what
is ordered, or what is owed.

## 1. CR Type

<!-- register:cr_type business_language -->
| Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|----------------|-----------|
| NEW_SUBDOMAIN | The library requires a governed catalog management capability it does not have; catalog records are maintained manually today. It extends nothing that exists. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Catalog | The library's authoritative description of the materials it holds. |
| Bibliographic Work | The subject of a single authoritative record describing a published title the library holds. |
| Book | One kind of bibliographic work: a published material the library registers in the catalog. |
| Physical Copy | An individual copy owned by the library, belonging to exactly one bibliographic work. |
| Catalog Record | The single authoritative record for one bibliographic work or one physical copy. |
| Bibliographic Information | The descriptive content of a bibliographic work's catalog record. |
| Book Details | The complete description of a registered book, as retrieved by staff. |
| Obsolete Record | A catalog record the library has determined is no longer to be used. |
| Authorized Staff | A library staff member permitted to perform catalog operations. |
| Business Operation | An action performed against the catalog that must be traceable and auditable. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| A single authoritative record exists for each bibliographic work the library has cataloged. |
| A single authoritative record exists for each physical copy the library owns. |
| Authorized staff can register new books, register physical copies, update bibliographic information, retire obsolete records, search the catalog, and retrieve complete book details. |
| Catalog descriptions are consistent, and duplicate entries no longer occur. |
| Materials can be located without the difficulty the manual catalog produces. |
| Every business operation performed against the catalog is traceable and auditable. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| The library maintains thousands of books and other published materials. | HIGH |
| Catalog records are maintained manually today. | HIGH |
| Manual maintenance produces inconsistent descriptions, duplicate entries, and difficulty locating materials. | HIGH |
| The library requires a single authoritative record for each bibliographic work and for each physical copy it owns. | HIGH |
| A book is one kind of bibliographic work. | HIGH |
| Each physical copy belongs to exactly one bibliographic work. | HIGH |
| Every business operation must be traceable and auditable. | HIGH |
| Only authorized staff may perform catalog operations. | HIGH |
| The operations required of the catalog are: register a book, register a physical copy, update bibliographic information, retire an obsolete record, search the catalog, retrieve complete book details. | HIGH |
| Borrowing, reservations, fines, patron management, acquisitions and inventory reconciliation are excluded from this release. | HIGH |
| The excluded capabilities are expected to be introduced through future governed change requests. | HIGH |
| The excluded capabilities must not be designed into the initial solution. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| No capability in the current composition manages a library catalog. | This change exists to fill that gap; if such a capability already exists, the scope of the change is different. | Confirm no existing capability registers, describes, searches or retires a catalog record. |
| The platform offers a governed form in which a business capability of this kind can be declared. | The library asks for a *governed* catalog capability; if no such form exists, the request cannot be met as stated. | Identify the governed forms available for declaring a business capability and its operations. |
| The platform already records business operations in a way that can be audited afterwards. | Traceability and auditability are required of every operation; whether they are reused or newly required depends on what already exists. | Identify what the composition already produces as a durable record of a performed operation. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| Nothing in this change depends on knowing who borrows a material. | Borrowing and patron management are declared out of scope. |
| "Thousands of books" describes the size of the collection and states no performance requirement. | The statement gives no performance target. |
| The library is treated as a single collection; no branch distinction is required. | The statement names no branch. |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| Capabilities deferred to future change requests must not be designed into this solution. | Business policy |
| Only authorized staff may perform catalog operations. | Business policy |
| Every business operation must leave a record that can be traced and audited. | Business policy |
| A physical copy may never be recorded against more than one bibliographic work. | Business policy |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| Each physical copy belongs to exactly one bibliographic work. |
| Each bibliographic work the library has cataloged has exactly one authoritative record. |
| Each physical copy the library owns has exactly one authoritative record. |
| Every business operation performed against the catalog is traceable and auditable. |
| Only authorized staff perform catalog operations. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Bibliographic Work | Registered | The work has been registered and the catalog holds its authoritative record. |
| Bibliographic Work | Retired | The record has been determined obsolete and retired from use. |
| Physical Copy | Registered | The copy has been registered against exactly one bibliographic work. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| Book Registered | When authorized staff register a new book. | A bibliographic work enters the catalog and acquires its authoritative record. |
| Physical Copy Registered | When authorized staff register a physical copy. | The library records a copy it owns against exactly one bibliographic work. |
| Bibliographic Information Updated | When authorized staff update the bibliographic information of a registered work. | The authoritative description of a work changes. |
| Record Retired | When authorized staff retire an obsolete record. | The record is no longer to be used. |
| Catalog Searched | When authorized staff search the catalog for materials. | A business operation occurred that must be traceable and auditable. |
| Book Details Retrieved | When authorized staff retrieve the complete details of a book. | A business operation occurred that must be traceable and auditable. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| Bibliographic work record | Catalog |
| Physical copy record | Catalog |
| Bibliographic information | Catalog |
| The decision that a record is obsolete | Authorized staff |
| The business problem statement | The person who wrote it |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| Borrowing | Declared excluded from this release; expected to arrive through a future governed change request. |
| Reservations | Declared excluded from this release; expected to arrive through a future governed change request. |
| Fines | Declared excluded from this release; expected to arrive through a future governed change request. |
| Patron management | Declared excluded from this release; expected to arrive through a future governed change request. |
| Acquisitions | Declared excluded from this release; expected to arrive through a future governed change request. |
| Inventory reconciliation | Declared excluded from this release; expected to arrive through a future governed change request. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| catalog | CREATED |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|
| Does retirement apply to physical copy records as well as to bibliographic work records? | The statement says "retire obsolete records" without saying which kind of record. | NO | HUMAN |
| Is a search or a retrieval a business operation that must be traceable and auditable? | Every business operation must be traceable; the statement does not say whether reads count. | NO | HUMAN |
| Who is authoritative for deciding which staff are authorized? | The statement requires authorized staff but names no authority that grants it, and patron management is out of scope. | NO | HUMAN |
| What is believed to already exist in the platform that this change should reuse? | The statement records no belief about the existing composition, so the later verification phase has few targets. | NO | HUMAN |

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| Authorized staff can register a new book, and the catalog then holds exactly one authoritative record for it. |
| Authorized staff can register a physical copy against exactly one bibliographic work. |
| Authorized staff can update the bibliographic information of a registered work. |
| Authorized staff can retire an obsolete record, and the retired record is no longer offered as current. |
| Authorized staff can search the catalog and locate a registered material. |
| Authorized staff can retrieve the complete details of a registered book. |
| A staff member who is not authorized cannot perform any catalog operation. |
| Registering the same book twice does not produce two authoritative records for it. |
| Every catalog operation performed can be traced and audited after the fact. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
