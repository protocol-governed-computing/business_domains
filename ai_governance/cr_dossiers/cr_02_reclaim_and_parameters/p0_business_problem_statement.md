# Business Problem Statement

**Project Name:** ai_governance — reclaim and parameter result

## 1. Context

The business governs two things with AI tools. AI Licensing provisions an employee a license, and
reclaims a license that has gone unused for the business's threshold of days. Agent Governance judges
an agent's proposed action: among other checks, it checks the action's parameters against the rules
declared for the tool.

Both were published in v5. Two of their acts do not do what the business needs.

---

## 2. Problem Statement

**A reclaim does not say what happens when the registry refuses to remove an assignment, and the
parameter check reports a result it never receives.**

**The reclaim.** Removing an assignment can be refused by the license registry, when the request to
it is malformed. The step that removes the assignment answers when the registry removes it, when it
finds no assignment, and when it cannot be reached. It does not answer a refusal, so the reclaim would
carry on as if the assignment had been removed.

**The parameter check.** It says it reports a validation result. It never has: it reads the result
from a place the check underneath it does not write, so the result is always empty. Nothing reads it
today. But the platform is about to refuse a check that reports something it never received, and
from then on every governed action would be refused.

This change shall:

- end a reclaim the registry refuses, with the license left assigned;
- have the parameter check report whether every declared rule passed;
- state each act whose meaning this changes under a new identity, leave the identity v5 published as
  it was published, and have whatever runs it run the new one;
- leave every other reclaim and every governed action deciding as it does today.

### What the business already decided

These are settled and are not reopened by this change:

- **A reclaim ends as reclaimed, still active, or in error.** No ending is added.
- **A license the registry did not release stays with the employee.**
- **A parameter that breaks a declared rule denies the action.**
- **Identity is fixed at publication.** An act that comes to mean something else is a new identity;
  the published one stays in the record, stood down, and whatever names it names its successor.

---

## 3. Clarifications answered by the business author

- **Where does a reclaim the registry refused end?** As still active. The license is not reclaimed and
  stays with the employee. The record of why stays in the trace.
- **What result does the new parameter check report?** Whether every declared rule passed. The check
  underneath answers only that, because a broken rule denies the action rather than returning.
- **Does anything else read the old parameter result?** No.
- **What about the licence-cap check nothing runs?** Out of scope. It stays as v5 published it.
