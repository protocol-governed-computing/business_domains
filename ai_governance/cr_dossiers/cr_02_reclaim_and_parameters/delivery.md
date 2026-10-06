# Delivery — cr_02_reclaim_and_parameters

**Authorized by:** Gate 1 and Gate 2, at P7 and P8, against composition `6f931dffd412…`
**Delivered:**
- A reclaim the license registry refuses ends as still active. The license stays assigned, and no
  revocation is announced.
- The parameter check reports whether every declared rule passed.
- Both contracts are their next versions. The versions v5 published are stood down unchanged.

**Validated:**
- Reclaim closure 4/4 (0 not exercised).
- Published identity: none of the 500 changed meaning.
- Construction acceptance 181/183, red by design for the two pinned book_library differences.
- Full regression 64/64 as expected.

---

## What this change closed

**The reclaim.** The registry declares four answers to a removal: removed, not found, refused, and
unreachable. The reclaim's removal step answered three, so a refused removal had no route of its own.
`CC_RECLAIM_UNUSED_LICENSE_V1` answers all four, and ends the contract on each. `WF_AUTO_RECLAIM_V0`
already routed the contract's VIOLATION to EXIT_ACTIVE, so the act decides as it did.

**The parameter check.** `CC_VALIDATE_TOOL_PARAMETERS_V0` mapped `validation_result` from a field the
check underneath never writes, so the result was always empty.
`CC_VALIDATE_TOOL_PARAMETERS_V1` maps it from `valid`: whether every declared rule passed.

**Identity.** v5 published both contracts, so each change is a new identity. Each V0 gains only
`superseded_by`. `WF_AUTO_RECLAIM_V0` and `WF_GOVERN_AGENT_ACTION_V0` are re-pointed: each changes
one line, the `code` of the place that runs the contract. Labels and routes are unchanged.

---

## What it took

**One dossier, two designs.** This dossier carries dev/18's `cr_02_reclaim_closure` and
`cr_03_parameter_result` together. dev/18 amended the reclaim in place; here it is replaced. The
parameter check's V1 equals dev/18's exactly. Construction determined 108 of 108 facts.

**One explanation is not carried.** dev/18's in-place reclaim kept `extensions.description` through
amendment carry-forward. A next version is not an amendment, and no register states that
description, so `CC_RECLAIM_UNUSED_LICENSE_V1` has none. It is explanation only and carries no
meaning. Its declaration otherwise equals dev/18's, apart from `version` and `supersedes`.

**The reclaim-closure validation** is carried from dev/18 and added to the regression.

---

## What is carried

- **The reclaim act is re-pointed, not restated.** It states admission rules no register carries.
  The refusal it routes is deferred until the act is next restated.
- **A refused removal and a license still in use end the same way.** Both leave the license assigned.
- **`CC_ENFORCE_LICENSE_CAP_V0`** stays as v5 published it. Nothing runs it.
