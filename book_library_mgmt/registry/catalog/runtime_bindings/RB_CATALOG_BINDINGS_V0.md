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

Which concrete host implementations satisfy the catalog's capability pipelines, and which structure
resolves its store paths. One binding serves every catalog workflow, because they share one set of
stores.

---

## Machine

```yaml
fqdn: book_library_mgmt::RB_CATALOG_BINDINGS_V0
artifact_kind: RUNTIME_BINDING
version: v0
governed_by: fb.runtime_binding::CONSTITUTION_RUNTIME_BINDING_V0

parameters:
  - module_data_root

core:
  summary: Runtime binding of catalog capability side effects
  description: Declares which concrete host implementations satisfy catalog capability pipelines during execution.
  storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0

  bindings:
    capability_side_effects::CS_MUTABLE_JSON_V0:
      policy:
        path: "{{module_data_root}}/book_library_mgmt/catalog/bibliographic_works.json"

    capability_side_effects::CS_APPENDONLY_JSONL_V0:
      policy: {}

extensions:
  notes:
    - This artifact performs no discovery and no inference.
    - All capability runtimes must be explicitly bound.
    - Storage paths are resolved via template parameters.
```
