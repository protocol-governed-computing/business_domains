# RB_CATALOG_BINDINGS_V0

## Header (Mandatory)

- **Artifact Code:** RB_CATALOG_BINDINGS_V0
- **Artifact Kind:** runtime_binding
- **Governed By:** CONSTITUTION_RUNTIME_BINDING_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Binds every catalog workflow to the mechanisms and stores it uses

---

## Machine

```yaml
fqdn: book_library_mgmt::RB_CATALOG_BINDINGS_V0
artifact_kind: RUNTIME_BINDING
version: v0
governed_by: fb.runtime_binding::CONSTITUTION_RUNTIME_BINDING_V0
core:
  summary: Binds every catalog workflow to the mechanisms and stores it uses
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
