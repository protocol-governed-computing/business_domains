# RB_IDENTITY_BINDINGS_V0

## Machine

```yaml
fqdn: blockchain::RB_IDENTITY_BINDINGS_V0
artifact_kind: RUNTIME_BINDING
version: v0
governed_by: runtime_binding::CONSTITUTION_RUNTIME_BINDING_V0
authority: pgc.platform
concern: identity
core:
  summary: Binds the identity's workflows to the stores and mechanisms they use
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

---

## Intent

Binds the identity's workflows to the stores and mechanisms they use
