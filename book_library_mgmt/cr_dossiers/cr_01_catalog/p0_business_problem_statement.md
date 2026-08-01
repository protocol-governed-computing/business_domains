# Business Problem Statement — book_library_mgmt / catalog

A community library maintains thousands of books and other published materials. Library staff
currently maintain catalog records manually, leading to inconsistent descriptions, duplicate
entries, and difficulty locating materials.

The library requires a governed catalog management capability that provides a single authoritative
record for each bibliographic work and each physical copy owned by the library.

The system shall allow authorized staff to: register new books; register physical copies; update
bibliographic information; retire obsolete records; search the catalog; retrieve complete book
details.

Each physical copy shall belong to exactly one bibliographic work. Every business operation shall
be traceable and auditable.

This release intentionally excludes borrowing, reservations, fines, patron management,
acquisitions, and inventory reconciliation. Those capabilities are expected to be introduced
through future governed change requests rather than being designed into the initial solution.

## Clarification answered by the business author

Asked: are "book" and "bibliographic work" the same business object, or is a book one kind of
bibliographic work?

Answered: a book is one kind of bibliographic work.