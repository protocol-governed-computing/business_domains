# RB_WALLET_BINDINGS_V0

## Header (Mandatory)

- **Artifact Code:** RB_WALLET_BINDINGS_V0
- **Artifact Kind:** runtime_binding
- **Governed By:** CONSTITUTION_RUNTIME_BINDING_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Binds the wallet workflow to the capabilities and stores it uses

---

## Machine

```yaml
fqdn: blockchain::RB_WALLET_BINDINGS_V0
artifact_kind: RUNTIME_BINDING
version: v0
governed_by: runtime_binding::CONSTITUTION_RUNTIME_BINDING_V0
authority: pgc.platform
concern: wallet
core:
  summary: Binds the wallet workflow to the capabilities and stores it uses
  storage_structure: blockchain::STRUCTURE_WALLET_STORAGE_V0
  bindings:
    capability_side_effects::CS_MUTABLE_JSON_V0:
      policy:
        store: WALLETS
    capability_side_effects::CS_APPENDONLY_JSONL_V0:
      policy:
        store: WALLET_OCCURRENCES
    capability_side_effects::CS_REGISTRY_V0:
      policy:
        store: WALLET_IDENTITIES
    capability_side_effects::CS_CLOCK_V0:
      policy:
        policy: utc
```
