# Delivery — cr_03_parameter_result

**Authorized by:** Gate 1 and Gate 2, at P7 and P8, against composition `6ddb2b553379…`
**Delivered:** `ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1`, which reports whether every declared
rule passed, stands in for V0. The governed action runs it.
**Validated:** construction 53/53; construction acceptance 177/177 with 0 field differences, now
including ai_governance; full regression `--all` 65/65 as expected

---

## What this change closed

The parameter check mapped `validation_result` from the check's `value`, which
`capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0` never returns. It returns `valid`,
true whenever it returns, and denies when a rule fails. V1 maps `validation_result` from `valid`, as a
boolean, and keeps the same two steps, rules and routes. Its second step no longer passes the rules
through again: its first step already places them on the surface.

A change of what a check reports is a change of its meaning, so V1 is a new identity. V0 is stood
down and kept. `ai_governance::WF_GOVERN_AGENT_ACTION_V0` is re-pointed: the place that runs the check
names V1 in `code`, and its label and the routes to it are unchanged. A valid action is authorized
and recorded, and an action breaking a rule is audited and denied, as before.

---

## What it took

This is the first change built with `REPLACE` and `REPOINT`. It found three defects in how they
worked, each fixed before this change was built:

- **A route read as a reference.** Inspection reports the contract a workflow routes from as a
  referrer, by `NODE_NEXT`. Construction's reach check now counts only edges a declaration makes.
- **A re-point renamed the place.** The workflow labels the place, and routes to it, by the code it
  runs. Construction now rewrites only values in declared reference parts, and `code` was declared
  one, in `artifact::VOCAB_DECLARATION_REPRESENTATION_V1`, as a recorded exception.
- **A label read as a reach.** The compiler's check that nothing reaches a stood-down artifact read
  the kept label as a reference to V0. In a workflow, a value naming one of its own places is now a
  label, unless it sits in a declared reference part.

The rule map in the first step is a step-binding literal. Written YAML-style, construction kept it as
a string without a word; written as a quoted literal, it renders as a map.

ai_governance is now compared by construction acceptance. Its registry predates the lifecycle, so 39
of its artifacts are determined by no dossier; the 8 that are reproduce exactly.

---

## What is carried

- **A step-binding literal that does not parse is kept as a string.** It should be refused.
- **The place keeps its old label.** It reads `CC_VALIDATE_TOOL_PARAMETERS_V0` and runs V1. A label is
  local, and renaming it would be a change to the workflow.
