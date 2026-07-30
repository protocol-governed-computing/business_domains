# CT_PURE_CHECK_TRAINING_STATUS_V0

## Header (Mandatory)

- **Artifact Code:** CT_PURE_CHECK_TRAINING_STATUS_V0
- **Artifact Kind:** capability_transform
- **Governed By:** CONSTITUTION_CAPABILITY_TRANSFORMS_V0
- **Version:** v0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Decide whether an employee's training record satisfies the licensing precondition. Pure predicate —
the eligibility *policy* lives in `CC_VALIDATE_ELIGIBILITY_V0`; this transform only evaluates it.

---

## Machine

```yaml
fqdn: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: fb.capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0
core:
  summary: Evaluate whether required training has been completed
  description: |
    Signals VIOLATION by raising CTExecutionError; the runtime maps any CT exception to
    VIOLATION. A false predicate is never returned as a value — a plain return is SUCCESS
    and would let the consuming pipeline continue past a failed gate.
  inputs:
    training_completed:
      type: boolean
      required: true
      description: Whether the employee has completed required AI-use training
  outputs:
    training_eligible:
      type: boolean
      required: true
      description: True when training is complete and the employee clears this gate
machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: PURE_CHECK_TRAINING_STATUS
  implementation:
    module: ai_governance.implementation.capability_transforms.atoms.ct_pure_check_training_status_v0
    callable: execute
```
