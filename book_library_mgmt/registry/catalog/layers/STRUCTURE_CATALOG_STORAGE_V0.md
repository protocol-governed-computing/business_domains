# STRUCTURE_CATALOG_STORAGE_V0

## Machine

```yaml
fqdn: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
artifact_kind: STRUCTURE
version: v0
governed_by: structure::CONSTITUTION_STRUCTURE_V0
authority: pgc.platform
concern: catalog
core:
  summary: Declares the stores the catalog owns and the paths they occupy
  layer: DOMAINS
  domain: book_library_mgmt
  subdomain: catalog
  entity_stores:
    COPY_BARCODE_REGISTRY:
      path: book_library_mgmt/catalog/copy_barcode_registry.jsonl
    BOOK_IDENTITY_REGISTRY:
      path: book_library_mgmt/catalog/book_identity_registry.jsonl
    BOOKS:
      path: book_library_mgmt/catalog/books.json
    PHYSICAL_COPIES:
      path: book_library_mgmt/catalog/physical_copies.json
    WORK_IDENTITY_REGISTRY:
      path: book_library_mgmt/catalog/work_identity_registry.jsonl
    WORKS:
      path: book_library_mgmt/catalog/works.json
    CATALOG_OPERATIONS:
      path: book_library_mgmt/catalog/catalog_operations.jsonl
```

---

## Intent

Declares the stores the catalog owns and the paths they occupy
