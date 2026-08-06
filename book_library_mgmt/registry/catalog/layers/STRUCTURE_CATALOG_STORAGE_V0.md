# STRUCTURE_CATALOG_STORAGE_V0

## Header (Mandatory)

- **Artifact Code:** STRUCTURE_CATALOG_STORAGE_V0
- **Artifact Kind:** structure
- **Governed By:** CONSTITUTION_STRUCTURE_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Declares the stores the catalog owns and the paths they occupy

---

## Machine

```yaml
fqdn: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
artifact_kind: STRUCTURE
version: v0
governed_by: fb.structure::CONSTITUTION_STRUCTURE_V0
core:
  summary: Declares the stores the catalog owns and the paths they occupy
  layer: DOMAINS
  domain: book_library_mgmt
  subdomain: catalog
  entity_stores:
    WORKS:
      path: book_library_mgmt/catalog/works.json
    WORK_IDENTITY_REGISTRY:
      path: book_library_mgmt/catalog/work_identity_registry.jsonl
    BOOKS:
      path: book_library_mgmt/catalog/books.json
    PHYSICAL_COPIES:
      path: book_library_mgmt/catalog/physical_copies.json
    CATALOG_OPERATIONS:
      path: book_library_mgmt/catalog/catalog_operations.jsonl
    BOOK_IDENTITY_REGISTRY:
      path: book_library_mgmt/catalog/book_identity_registry.jsonl
    COPY_BARCODE_REGISTRY:
      path: book_library_mgmt/catalog/copy_barcode_registry.jsonl
```
