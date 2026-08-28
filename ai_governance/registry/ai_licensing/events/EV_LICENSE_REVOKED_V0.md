# EV_LICENSE_REVOKED_V0

## 1. Fact

A license has been revoked and returned to the pool.

---

## 2. Rationale

License revocation is autonomous reclamation:
- Triggered by inactivity threshold
- No human intervention required
- Returns license for pending employees

---

## 3. Emitted By

| Workflow | Capability Contract |
|----------|---------------------|
| WF_AUTO_RECLAIM_V0 | CC_RECLAIM_UNUSED_LICENSE_V0 |

---

## 4. Schema

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| license_id | string | true | License that was revoked |
| reason | string | true | Revocation reason: INACTIVITY |
| timestamp | string (date-time) | true | When revocation occurred |

---

## Machine

```yaml
fqdn: ai_governance::EV_LICENSE_REVOKED_V0
artifact_kind: EVENT
version: v0
governed_by: event::CONSTITUTION_EVENT_V0
authority: pgc.platform
concern: ai_licensing

core:
  summary: License Revoked
  description: Emitted when a license is revoked and returned to pool

  schema:
    license_id:
      type: string
      required: true
    reason:
      type: string
      enum:
        - INACTIVITY
      required: true
    timestamp:
      type: string
      format: date-time
      required: true
```
