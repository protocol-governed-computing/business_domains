# CT_PURE_EVALUATE_INACTIVITY_V0

## Header (Mandatory)

- **Artifact Code:** CT_PURE_EVALUATE_INACTIVITY_V0
- **Artifact Kind:** capability_transform
- **Governed By:** CONSTITUTION_CAPABILITY_TRANSFORMS_V0
- **Version:** v0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Decide whether a license has been dormant past its reclamation threshold.

`evaluation_date` is an **explicit declared input**, not a clock read. A pure CT may not consult
the system clock — doing so would make the transform non-deterministic and unreplayable. The
caller supplies the evaluation instant, so the same inputs always produce the same verdict.

---

## Machine

```yaml
fqdn: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: fb.capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0
core:
  summary: Evaluate license inactivity against a declared threshold
  refusal: raises
  description: |
    Signals VIOLATION by raising CTExecutionError; the runtime maps any CT exception to
    VIOLATION. A false predicate is never returned as a value — a plain return is SUCCESS
    and would let the consuming pipeline continue past a failed gate.
  inputs:
    last_active_date:
      type: string
      required: true
      description: ISO-8601 date or date-time of last recorded license activity
    evaluation_date:
      type: string
      required: true
      description: ISO-8601 date or date-time the evaluation is made as of — declared, never a clock read
    threshold_days:
      type: integer
      required: true
      description: Inactivity threshold in days
  outputs:
    is_inactive:
      type: boolean
      required: true
      description: True when days_inactive meets or exceeds threshold_days
    days_inactive:
      type: integer
      required: true
      description: Whole days elapsed between last_active_date and evaluation_date
machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: PURE_EVALUATE_INACTIVITY
  implementation:
    module: ai_governance.implementation.capability_transforms.atoms.ct_pure_evaluate_inactivity_v0
    callable: execute
```
