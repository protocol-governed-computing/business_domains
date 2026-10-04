# Business Problem Statement

**Project Name:** ai_governance — ai_licensing

## 1. Context

The business reclaims an AI tool license that has gone unused for its threshold of days. The reclaim
checks whether the license is inactive and, if it is, takes the license back from the employee by
removing their assignment from the license registry.

Removing an assignment can be refused by the registry itself, when the request to it is malformed.
The business has never said what a reclaim does when that happens.

---

## 2. Problem Statement

**When the license registry refuses to remove an assignment, the reclaim does not say what happens
next.**

The step that removes the assignment answers when the registry removes it, when it finds no
assignment, and when it cannot be reached. It does not answer when the registry refuses the request,
so the reclaim would carry on as if the assignment had been removed.

This change shall:

- end a reclaim the registry refuses, with the license left assigned;
- leave every other reclaim unchanged.

### What the business already decided

These are settled and are not reopened by this change:

- **A reclaim ends as reclaimed, still active, or in error.** No ending is added.
- **A license the registry did not release stays with the employee.**

---

## 3. Clarifications answered by the business author

- **Where does a reclaim the registry refused end?** As still active. The license is not reclaimed
  and stays with the employee, so the ending says what is true of it. The record of why stays in
  the trace.
