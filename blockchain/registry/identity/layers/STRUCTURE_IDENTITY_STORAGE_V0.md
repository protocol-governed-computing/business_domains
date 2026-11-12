# STRUCTURE_IDENTITY_STORAGE_V0

## Machine

```yaml
fqdn: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
artifact_kind: STRUCTURE
version: v0
governed_by: structure::CONSTITUTION_STRUCTURE_V0
authority: pgc.platform
concern: identity
core:
  summary: Declares the stores the identity owns and the paths they occupy
  layer: DOMAINS
  domain: blockchain
  subdomain: identity
  entity_stores:
    CONTACT_ADDRESS_REGISTRY:
      path: blockchain/identity/contact_address_registry.jsonl
    ACTORS:
      path: blockchain/identity/actors.json
    ACTOR_OCCURRENCES:
      path: blockchain/identity/actor_occurrences.jsonl
```

---

## Intent

Declares the stores the identity owns and the paths they occupy
