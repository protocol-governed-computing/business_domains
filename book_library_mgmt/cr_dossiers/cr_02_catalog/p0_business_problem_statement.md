# Business Problem Statement

**Project Name:** book_library_mgmt

## 1. Context

This project extends the existing **book_library_mgmt** system.

The overall project scope continues to include the following library functions:

- catalog
- circulation
- patron
- staff
- reservations
- acquisitions
- inventory
- notifications
- policy
- reporting

The initial catalog capability established a governed catalog containing bibliographic records and physical copies of library materials.

This change request extends the existing catalog function. It does not introduce a new library function.

The purpose of this change is to allow the catalog to represent a published work that exists in more than one edition, while preserving all behavior established by the previous governed change.

---

## 2. Problem Statement

The current catalog adequately manages books, physical copies, and basic bibliographic information. As the library collection grows, staff increasingly encounter situations that cannot be represented accurately within the existing model.

Many published works exist in multiple editions that differ in publication date, publisher, format, or content revision while remaining recognizably the same work. The current catalog cannot distinguish these editions without creating separate book records or compromising bibliographic accuracy.

**The question this change exists to answer is whether an edition is part of an existing Book or is a catalog entity in its own right.** Every other question in this change follows from it: what a physical copy is a copy *of*, what a search returns and at which level, what retirement applies to, and what an identifier identifies. The previous catalog change established that a book is identified by title, author and publication year. If an edition differs by publication date, that identity either distinguishes editions already or was never an identity for the work at all. The business author must settle this; the design process must not assume it.

The extended catalog shall allow authorized staff to:

- register additional editions of an existing work
- search and retrieve catalog records where a work has more than one edition

Existing capabilities, including:

- registering books
- registering physical copies
- updating bibliographic information
- retiring records
- searching the catalog
- retrieving complete book details

shall continue to operate without behavioral regression.

Every business operation shall remain traceable and auditable.

### Existing records

This change extends a governed catalog that already holds records. Existing catalog records remain valid and shall continue to function without requiring recreation.

That statement is a promise about records written under the previous change and read under this one, and it is not satisfied by the catalog merely continuing to compile. It must be demonstrated against records created by the previous catalog capability: whatever a work with a single edition means after this change, a record written before it must still be found by search, retrieved in full, updated, retired and reinstated. Whether that requires the existing records to be altered is a business question stated in §3 and not assumed here.

### Deferred to follow-on changes

The library has further needs in the catalog which are **named here and deliberately excluded from this change**, because each of them rests on the edition question above and cannot be settled before it is:

- **Multiple identifiers.** Different publishers, distributors, or historical editions may assign different ISBN values to the same publication. The catalog currently assumes a single identifying value and cannot represent these relationships. What an ISBN identifies — a work, an edition, or a printing — is not answerable until an edition is defined.
- **Governed subject taxonomy.** The library wishes to organize its collection using a governed taxonomy rather than relying solely on unrestricted subject text, improving consistency of cataloging and enabling more accurate searching and reporting.
- **Digital resources.** Library collections increasingly include electronic editions, supplementary downloadable material, publisher resources, and external reference links which staff require the ability to associate with catalog records without changing the circulation model.
- **Images.** Staff require the ability to associate one or more images with catalog records, such as cover images or scanned illustrations, to improve catalog usability for both staff and future patron-facing services.

Each is a governed change of its own, in the order the business chooses.

This release intentionally excludes circulation, patron management, reservations, acquisitions, inventory management, notifications, reporting, and staff authorization, except where existing catalog behavior depends upon those functions.

---

## 3. Clarifications to be answered by the business author

The following business questions intentionally remain unanswered. They are expected to be resolved through clarification during this change request rather than being assumed by the design process.

### Editions

- Is an edition part of an existing Book, or is it a new catalog entity?
- What distinguishes one edition from another?
- If a work is identified by title, author and publication year, and editions differ by publication date, does the existing identity already distinguish editions?
- Can multiple editions share physical copies?
- Is a physical copy a copy of a work, or of a particular edition?
- Can an edition be retired independently of other editions?
- May a work exist with no editions, or is the first edition created with the work?

### Search and retrieval

- Should searches operate across editions individually or at the work level?
- When a work has several editions, what does retrieving its complete details return?

### Existing records

- How should existing catalog records be interpreted after this extension?
- Is migration required, or are existing records automatically considered valid?
- If a record written before this change has no edition, what is it?
- Must all previous catalog operations continue unchanged?

The remaining project functions continue to be adjacent to this change: named, planned, and outside the scope of this governed extension. The catalog needs deferred in §2 — identifiers, taxonomy, digital resources and images — carry their own clarifications, which belong to the changes that take them up.
