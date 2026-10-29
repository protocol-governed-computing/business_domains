# STRUCTURE_AI_LICENSING_STORAGE_V1

## Machine

```yaml
fqdn: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V1
artifact_kind: STRUCTURE
version: v1
governed_by: structure::CONSTITUTION_STRUCTURE_V0
authority: pgc.platform
concern: ai_licensing
supersedes: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0
core:
  summary: Declares the stores the ai_licensing owns and the paths they occupy
  layer: DOMAINS
  domain: ai_governance
  subdomain: ai_licensing
  entity_stores:
    EMPLOYEE_EMPLOYEE_ID_REGISTRY:
      path: ai_governance/ai_licensing/employee_employee_id_registry.jsonl
    EMPLOYEES:
      path: ai_governance/ai_licensing/employees.json
    LICENSE_AUDIT:
      path: ai_governance/ai_licensing/audit_log.jsonl
    LICENSE_CAPS:
      path: ai_governance/ai_licensing/license_caps.json
    LICENSE_IDENTITY_REGISTRY:
      path: ai_governance/ai_licensing/license_identity_registry.jsonl
    LICENSES:
      path: ai_governance/ai_licensing/licenses.json
```

---

## Intent

Declares the stores the ai_licensing owns and the paths they occupy
