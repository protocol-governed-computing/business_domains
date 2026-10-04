# CT_PURE_CHECK_TRAINING_STATUS_V0

## Machine

```yaml
fqdn: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: capability_transforms::CONSTITUTION_DETERMINISTIC_ATOMS_V0
authority: pgc.platform
concern: ai_licensing
core:
  summary: Evaluate whether required training has been completed
  refusal: raises
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
  description: 'Signals VIOLATION by raising CTExecutionError; the runtime maps any CT exception to

    VIOLATION. A false predicate is never returned as a value — a plain return is SUCCESS

    and would let the consuming pipeline continue past a failed gate.

    '
machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: PURE_CHECK_TRAINING_STATUS
  implementation:
    module: ai_governance.implementation.capability_transforms.atoms.ct_pure_check_training_status_v0
    callable: execute
```

---

## Intent

Evaluate whether required training has been completed
