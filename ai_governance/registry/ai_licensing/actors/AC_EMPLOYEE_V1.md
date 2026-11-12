# AC_EMPLOYEE_V1

## Machine

```yaml
fqdn: ai_governance::AC_EMPLOYEE_V1
artifact_kind: ACTOR
version: v1
governed_by: actor::CONSTITUTION_ACTOR_IDENTITY_V0
authority: pgc.platform
concern: ai_licensing
supersedes: ai_governance::AC_EMPLOYEE_V0
core:
  summary: A person the business may license for AI tools
  type: human
  attributes:
    employee_id:
      type: string
      required: true
```

---

## Intent

A person the business may license for AI tools
