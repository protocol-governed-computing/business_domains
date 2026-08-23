# STRUCTURE_WALLET_STORAGE_V0

## 1. Intent

Declares the three stores wallet owns

---

## Machine

```yaml
fqdn: blockchain::STRUCTURE_WALLET_STORAGE_V0
artifact_kind: STRUCTURE
version: v0
governed_by: structure::CONSTITUTION_STRUCTURE_V0
authority: pgc.platform
concern: wallet
core:
  summary: Declares the three stores wallet owns
  layer: DOMAINS
  domain: blockchain
  subdomain: wallet
  entity_stores:
    WALLETS:
      path: blockchain/wallet/wallets.json
    WALLET_OCCURRENCES:
      path: blockchain/wallet/wallet_occurrences.jsonl
    WALLET_IDENTITIES:
      path: blockchain/wallet/wallet_identity_registry.jsonl
```
