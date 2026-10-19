# STRUCTURE_AI_LICENSING_STORAGE_V0

## 1. Intent

Storage topology for the `ai_licensing` subdomain. Declares every entity store the licensing
workflows touch, so the subdomain resolves its own paths and carries no reference into
`agent_governance`.

`LICENSE_FACTS` is **owned here** — licensing provisioning and reclamation are what write it.
`agent_governance` consumes the same feed read-only and declares it independently; neither
subdomain references the other's STRUCTURE.

---

## 2. Entity Stores

| Store | Mutability | Purpose |
|---|---|---|
| LICENSE_FACTS | read-write (owner) | License tier and status fact feed, keyed by user |
| LICENSE_REGISTRY | read-write | Employee → license assignment registry |
| LICENSE_AUDIT | append-only | Provision, denial, and reclaim decision trail |

---

## Machine

```yaml
fqdn: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0
artifact_kind: STRUCTURE
version: v0
governed_by: structure::CONSTITUTION_STRUCTURE_V0
authority: pgc.platform
concern: ai_licensing

core:
  summary: AI licensing subdomain storage topology
  description: Maps licensing entity stores to paths under the instance data root.

  layer: DOMAINS
  domain: ai_governance
  subdomain: ai_licensing

  storage_roots:
    base_path: "{{module_data_root}}"
    description: "Root path for all ai_licensing storage (resolved at runtime)"

  entity_stores:
    LICENSE_FACTS:
      description: "License tier and status fact feed (user_id → license record) — owned by ai_licensing"
      path: "ai_governance/ai_licensing/license_facts.json"
    LICENSE_REGISTRY:
      description: "Employee → license assignment registry"
      path: "ai_governance/ai_licensing/license_registry.json"
    LICENSE_AUDIT:
      description: "Append-only audit trail for license provisioning, denial, and reclaim decisions"
      path: "ai_governance/ai_licensing/audit_log.jsonl"

  resolution:
    description: "Runtime path resolution strategy"
    algorithm: "base_path / entity_stores[entity_type].path"
    example: "{{module_data_root}}/ai_governance/ai_licensing/audit_log.jsonl"

  isolation:
    description: "Entity storage isolation constraints"
    rules:
      - "Each entity type has dedicated storage"
      - "LICENSE_AUDIT is append-only — license audit records are immutable"
      - "All paths are scoped under ai_governance/ai_licensing — no cross-subdomain writes"
      - "Storage paths resolved via STRUCTURE only"
```

