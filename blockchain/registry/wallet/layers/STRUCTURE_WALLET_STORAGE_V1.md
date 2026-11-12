# STRUCTURE_WALLET_STORAGE_V1

## Machine

```yaml
fqdn: blockchain::STRUCTURE_WALLET_STORAGE_V1
artifact_kind: STRUCTURE
version: v1
governed_by: structure::CONSTITUTION_STRUCTURE_V0
authority: pgc.platform
concern: wallet
supersedes: blockchain::STRUCTURE_WALLET_STORAGE_V0
core:
  summary: Declares the stores the wallet owns and the paths they occupy
  layer: DOMAINS
  domain: blockchain
  subdomain: wallet
  entity_stores:
    WALLET_ADDRESS_REGISTRY:
      path: blockchain/wallet/wallet_address_registry.jsonl
    WALLET_IDENTITIES:
      path: blockchain/wallet/wallet_identity_registry.jsonl
    WALLETS:
      path: blockchain/wallet/wallets.json
    WALLET_OCCURRENCES:
      path: blockchain/wallet/wallet_occurrences.jsonl
```

---

## Intent

Declares the stores the wallet owns and the paths they occupy
