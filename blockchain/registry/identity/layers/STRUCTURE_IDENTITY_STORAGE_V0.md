# STRUCTURE_IDENTITY_STORAGE_V0

## 1. Intent

Declares the three stores identity owns and the paths they occupy

---

## Machine

```yaml
fqdn: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
artifact_kind: STRUCTURE
version: v0
governed_by: structure::CONSTITUTION_STRUCTURE_V0
authority: pgc.platform
concern: identity
core:
  summary: Declares the three stores identity owns and the paths they occupy
  layer: DOMAINS
  domain: blockchain
  subdomain: identity
  entity_stores:
    ACTORS:
      path: blockchain/identity/actors.json
    CONTACT_ADDRESS_REGISTRY:
      path: blockchain/identity/contact_address_registry.jsonl
    ACTOR_OCCURRENCES:
      path: blockchain/identity/actor_occurrences.jsonl
```
