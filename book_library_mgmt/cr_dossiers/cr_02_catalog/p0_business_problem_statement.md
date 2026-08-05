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

The purpose of this change is to improve the quality and usefulness of the catalog by supporting richer bibliographic description while preserving all behavior established by the previous governed change.

---

## 2. Problem Statement

The current catalog adequately manages books, physical copies, and basic bibliographic information. As the library collection grows, staff increasingly encounter situations that cannot be represented accurately within the existing model.

Many published works exist in multiple editions that differ in publication date, publisher, format, or content revision while remaining recognizably the same work. The current catalog cannot distinguish these editions without creating separate book records or compromising bibliographic accuracy.

Books may also be identified by multiple identifiers. Different publishers, distributors, or historical editions may assign different ISBN values to the same publication. The catalog currently assumes a single identifying value and therefore cannot represent these relationships.

The library also wishes to organize its collection using a governed subject taxonomy rather than relying solely on unrestricted subject text. A controlled taxonomy improves consistency of cataloging and enables more accurate searching and reporting while allowing future expansion of subject hierarchies.

Increasingly, library collections include digital resources associated with physical books, including electronic editions, supplementary downloadable material, publisher resources, and external reference links. Staff require the ability to associate these digital resources with catalog records without changing the circulation model.

Library staff also require the ability to associate one or more images with catalog records, such as cover images or scanned illustrations, to improve catalog usability for both staff and future patron-facing services.

The library therefore requires the existing catalog capability to be extended while preserving all existing governed behavior introduced by the previous catalog change request.

The extended catalog shall allow authorized staff to:

- register additional editions of an existing work
- associate multiple ISBN values with catalog records where appropriate
- classify catalog records using a governed subject taxonomy
- associate digital resources with catalog records
- associate one or more images with catalog records
- search and retrieve catalog records using the extended bibliographic information

Existing capabilities, including:

- registering books
- registering physical copies
- updating bibliographic information
- retiring records
- searching the catalog
- retrieving complete book details

shall continue to operate without behavioral regression.

Every business operation shall remain traceable and auditable.

This change extends an existing governed catalog. Existing catalog records remain valid and shall continue to function without requiring recreation.

This release intentionally excludes circulation, patron management, reservations, acquisitions, inventory management, notifications, reporting, and staff authorization, except where existing catalog behavior depends upon those functions.

---

## 3. Clarifications to be answered by the business author

The following business questions intentionally remain unanswered. They are expected to be resolved through clarification during this change request rather than being assumed by the design process.

### Editions

- What distinguishes one edition from another?
- Is an edition part of an existing Book, or is it a new catalog entity?
- Can multiple editions share physical copies?
- Can an edition be retired independently of other editions?

### ISBN Management

- May an edition have multiple ISBN values?
- Can the same ISBN ever refer to more than one catalog record?
- Should historical or withdrawn ISBN values be retained?

### Subject Taxonomy

- Is the taxonomy centrally governed or maintained locally by the library?
- May a catalog record belong to multiple taxonomy categories?
- Is free-text subject entry still permitted alongside taxonomy classification?

### Digital Resources

- What kinds of digital resources are permitted?
- Are digital resources owned by the library or merely referenced?
- Can multiple digital resources be attached to the same catalog record?
- May a digital resource be shared between multiple catalog records?

### Images

- Are images stored within the library system or referenced externally?
- Can multiple images be associated with a catalog record?
- Is one image considered the primary image?

### Search

- Should searches operate across editions individually or at the work level?
- Should searches include digital-resource metadata?
- Should taxonomy searches include descendant categories?

### Compatibility

- How should existing catalog records be interpreted after these extensions?
- Is migration required, or are existing records automatically considered valid?
- Must all previous catalog operations continue unchanged?

The remaining project functions continue to be adjacent to this change: named, planned, and outside the scope of this governed extension.