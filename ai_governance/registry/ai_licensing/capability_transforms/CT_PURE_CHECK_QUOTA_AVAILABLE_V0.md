# CT_PURE_CHECK_QUOTA_AVAILABLE_V0

## Machine

```yaml
fqdn: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: capability_transforms::CONSTITUTION_DETERMINISTIC_ATOMS_V0
authority: pgc.platform
concern: ai_licensing
core:
  summary: Evaluate whether license quota remains available under the declared cap
  refusal: raises
  inputs:
    assigned_count:
      type: integer
      required: true
      description: Number of licenses currently assigned
    quota:
      type: integer
      required: true
      description: Declared license cap
  outputs:
    quota_available:
      type: boolean
      required: true
      description: True when at least one license remains under the cap
    remaining:
      type: integer
      required: true
      description: Licenses remaining under the cap, floored at zero
  description: 'Signals VIOLATION by raising CTExecutionError; the runtime maps any CT exception to

    VIOLATION. A false predicate is never returned as a value — a plain return is SUCCESS

    and would let the consuming pipeline continue past a failed gate.

    '
machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: PURE_CHECK_QUOTA_AVAILABLE
  implementation:
    module: ai_governance.implementation.capability_transforms.atoms.ct_pure_check_quota_available_v0
    callable: execute
```

---

## Intent

Evaluate whether license quota remains available under the declared cap
