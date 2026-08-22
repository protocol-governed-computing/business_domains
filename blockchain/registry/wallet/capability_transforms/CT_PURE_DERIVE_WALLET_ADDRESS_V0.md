# CT_PURE_DERIVE_WALLET_ADDRESS_V0

## Header (Mandatory)

- **Artifact Code:** CT_PURE_DERIVE_WALLET_ADDRESS_V0
- **Artifact Kind:** capability_transform
- **Governed By:** CONSTITUTION_CAPABILITY_TRANSFORMS_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Derives an address from supplied key material; the same material always yields the same address

---

## Machine

```yaml
fqdn: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0
authority: pgc.platform
concern: wallet
core:
  summary: Derives an address from supplied key material; the same material always yields the same address
  refusal: never
  inputs:
    key_material:
      type: string
      required: true
  outputs:
    address:
      type: string
      required: true
machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: DERIVE_WALLET_ADDRESS
  implementation:
    module: blockchain.implementation.capability_transforms.atoms.ct_pure_derive_wallet_address_v0
    callable: execute
```
