# RB_IDENTITY_BINDINGS_V0

## Header (Mandatory)

- **Artifact Code:** RB_IDENTITY_BINDINGS_V0
- **Artifact Kind:** runtime_binding
- **Governed By:** CONSTITUTION_RUNTIME_BINDING_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Binds identity's workflows to the side effects and storage they use

---

## Machine

```yaml
fqdn: blockchain::RB_IDENTITY_BINDINGS_V0
artifact_kind: RUNTIME_BINDING
version: v0
governed_by: fb.runtime_binding::CONSTITUTION_RUNTIME_BINDING_V0
core:
  summary: Binds identity's workflows to the side effects and storage they use
  storage_structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
  bindings:
    capability_side_effects::CS_MUTABLE_JSON_V0:
      policy:
        structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    capability_side_effects::CS_REGISTRY_V0:
      policy:
        structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    capability_side_effects::CS_APPENDONLY_JSONL_V0:
      policy:
        structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    capability_side_effects::CS_CLOCK_V0:
      policy:
        precision: seconds
```
