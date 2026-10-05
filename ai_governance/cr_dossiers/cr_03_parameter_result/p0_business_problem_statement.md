# Business Problem Statement

**Project Name:** ai_governance — parameter result

## 1. Context

Before an agent's action is recorded as governed, the business checks the action's parameters
against the rules it has declared for the tool the agent wants to use. A parameter that breaks a rule
denies the action, and the denial is audited.

The check says it reports a validation result. It never has. The result it reports is always empty,
because it reads the result from a place the check underneath it does not write. Nothing reads the
result today, so nothing has gone wrong. But the platform is about to refuse a check that reports
something it never received, and from then on every governed action would be refused.

---

## 2. Problem Statement

**The parameter check reports a result it never receives.**

This change shall:

- have the parameter check report the result the check underneath it actually gives;
- do so as a new version of the parameter check, which stands in for the old one;
- have the agent's governed action run the new version.

### What the business already decided

These are settled and are not reopened by this change:

- **A parameter that breaks a declared rule denies the action.** Unchanged.
- **A change of what a check reports is a new version of it.** The old version stays in the record
  and out of reach.
- **The governed action's steps, routes and audits are unchanged.** Only the check it runs at the
  parameter step changes.

---

## 3. Clarifications answered by the business author

- **What result does the new version report?** Whether every declared rule passed. The check
  underneath answers only that, because a broken rule denies the action rather than returning.
- **Does anything else read the old result?** No.
