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

The stores the catalog subdomain owns. A subdomain owns its stores exclusively: no peer writes
these, and the catalog writes no peer's.

---

## Machine

```yaml
fqdn: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
artifact_kind: STRUCTURE
version: v0
governed_by: fb.structure::CONSTITUTION_STRUCTURE_V0

core:
  summary: Catalog subdomain storage topology
  description: Maps catalog record stores to paths under the instance data root.

  layer: DOMAINS
  domain: book_library_mgmt
  subdomain: catalog

  storage_roots:
    base_path: "{{module_data_root}}"
    description: "Root path for all catalog storage (resolved at runtime)"

  entity_stores:
    BIBLIOGRAPHIC_WORKS:
      description: "The authoritative record of each cataloged work — owned by catalog"
      path: "book_library_mgmt/catalog/bibliographic_works.json"
    PHYSICAL_COPIES:
      description: "The authoritative record of each copy the library owns, each naming one work"
      path: "book_library_mgmt/catalog/physical_copies.json"
    CATALOG_OPERATIONS:
      description: "Append-only account of every catalog operation performed"
      path: "book_library_mgmt/catalog/catalog_operations.jsonl"
    CATALOG_STAFF:
      description: "Which staff members are authorized — read here, granted by patron in a future change"
      path: "book_library_mgmt/catalog/catalog_staff.json"

  resolution:
    description: "Runtime path resolution strategy"
    algorithm: "base_path / entity_stores[entity_type].path"
    example: "{{module_data_root}}/book_library_mgmt/catalog/bibliographic_works.json"

  isolation:
    description: "Entity storage isolation constraints"
    rules:
      - "Each entity type has dedicated storage"
      - "CATALOG_OPERATIONS is append-only — a performed operation is never rewritten"
      - "All paths are scoped under book_library_mgmt/catalog — no cross-subdomain writes"
      - "Storage paths resolved via STRUCTURE only"
```
