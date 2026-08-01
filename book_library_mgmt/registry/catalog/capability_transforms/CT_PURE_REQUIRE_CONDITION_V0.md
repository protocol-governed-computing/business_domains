# CT_PURE_REQUIRE_CONDITION_V0

## Header (Mandatory)

- **Artifact Code:** CT_PURE_REQUIRE_CONDITION_V0
- **Artifact Kind:** capability_transform
- **Governed By:** CONSTITUTION_CAPABILITY_TRANSFORMS_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Interpret an observation as a required condition.

A capability that reads external state reports whether the *read* succeeded, not what it *found*.
`exists`, `matched`, `authorized` are observations; routing a workflow on them directly routes on
"the store answered", which is always true. This transform is the governed step that turns one such
observation into a decision.

It is deliberately generic. It knows nothing about authorization, or duplicates, or catalogs — it
asserts that a named observation matches the value the design requires, and refuses when it does not — the same transform serves "must exist" and "must not exist". If other domains repeatedly need
a richer interpretation (`exists=false → NOT_FOUND` as a distinct outcome), that pattern will have
earned a reusable platform transform; until then, enriching the platform on one example would be
premature.

## 2. How a transform expresses a decision

The execution contract gives a transform exactly two outcomes: `SUCCESS` when it returns, and
`VIOLATION` when it raises. A transform that returns a boolean for both answers has interpreted
nothing, however it is named. So this one raises — that is the whole mechanism by which an
observation becomes a branch the workflow can route on.

---

## Machine

```yaml
fqdn: book_library_mgmt::CT_PURE_REQUIRE_CONDITION_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: fb.capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0

core:
  summary: Assert that an observed condition holds, refusing when it does not.

  inputs:
    condition:
      type: boolean
      required: true
      description: The observation being interpreted
    expected:
      type: boolean
      required: true
      description: The value the condition must hold, so one transform serves both directions

  outputs:
    result_status:
      type: string
      description: SUCCESS when the condition held; the runtime maps a raise to VIOLATION
    condition_held:
      type: boolean
      required: true
      description: True whenever this transform returns at all

machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: PURE_REQUIRE_CONDITION
  implementation:
    module: book_library_mgmt.implementation.capability_transforms.atoms.ct_pure_require_condition_v0
    callable: execute
```
