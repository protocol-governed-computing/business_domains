# STRUCTURE_AGENT_GOVERNANCE_STORAGE_V1

## Machine

```yaml
fqdn: ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V1
artifact_kind: STRUCTURE
version: v1
governed_by: structure::CONSTITUTION_STRUCTURE_V0
authority: pgc.platform
concern: agent_governance
supersedes: ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V0
core:
  summary: Declares the stores the agent_governance owns and the paths they occupy
  layer: DOMAINS
  domain: ai_governance
  subdomain: agent_governance
  entity_stores:
    ACTION_IDENTITY_REGISTRY:
      path: ai_governance/agent_governance/action_identity_registry.jsonl
    ACTIONS:
      path: ai_governance/agent_governance/actions.json
    GOVERNANCE_AUDIT:
      path: ai_governance/agent_governance/governance_audit.jsonl
```

---

## Intent

Declares the stores the agent_governance owns and the paths they occupy
