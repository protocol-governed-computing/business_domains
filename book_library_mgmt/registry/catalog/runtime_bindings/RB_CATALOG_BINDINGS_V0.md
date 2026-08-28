# RB_CATALOG_BINDINGS_V0

## 1. Intent

Binds the catalog's workflows to the stores and mechanisms they use

---

## Machine

```yaml
fqdn: book_library_mgmt::RB_CATALOG_BINDINGS_V0
artifact_kind: RUNTIME_BINDING
version: v0
governed_by: runtime_binding::CONSTITUTION_RUNTIME_BINDING_V0
authority: pgc.platform
concern: catalog
core:
  summary: Binds the catalog's workflows to the stores and mechanisms they use
  storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  bindings:
    capability_side_effects::CS_MUTABLE_JSON_V0:
      policy:
        structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    capability_side_effects::CS_REGISTRY_V0:
      policy:
        structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    capability_side_effects::CS_APPENDONLY_JSONL_V0:
      policy:
        structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
```
