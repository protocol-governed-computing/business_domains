# RB_WALLET_BINDINGS_V1

## Machine

```yaml
fqdn: blockchain::RB_WALLET_BINDINGS_V1
artifact_kind: RUNTIME_BINDING
version: v1
governed_by: runtime_binding::CONSTITUTION_RUNTIME_BINDING_V0
authority: pgc.platform
concern: wallet
supersedes: blockchain::RB_WALLET_BINDINGS_V0
core:
  summary: Binds the wallet's workflows to the stores and mechanisms they use
  storage_structure: blockchain::STRUCTURE_WALLET_STORAGE_V1
  bindings:
    capability_side_effects::CS_MUTABLE_JSON_V0:
      policy:
        structure: blockchain::STRUCTURE_WALLET_STORAGE_V1
    capability_side_effects::CS_REGISTRY_V0:
      policy:
        structure: blockchain::STRUCTURE_WALLET_STORAGE_V1
    capability_side_effects::CS_APPENDONLY_JSONL_V0:
      policy:
        structure: blockchain::STRUCTURE_WALLET_STORAGE_V1
```

---

## Intent

Binds the wallet's workflows to the stores and mechanisms they use
