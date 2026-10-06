# Business Problem Statement

**Project Name:** blockchain — published identities

## 1. Context

The business published its identity and wallet acts in v5. A published act means what it meant on
the day it was published, and a citation of v5 relies on that.

After v5, `cr_06_routing_closure` decided what every identity and wallet act does when a record it
needs cannot be read or written. Four contracts came to report the failure, and four workflows came
to route it to an ending. That was the right change. It was made in place: each of the eight kept the
identity v5 published, so each now means something v5 did not say.

| Act | Kind | What changed |
|-----|------|--------------|
| Resolve an actor | contract | reports a failed record, and may end with it |
| Claim a wallet's identity | contract | the same |
| Create the wallet record | contract | reports a failed record |
| Record a wallet moment | contract | the same |
| Register an actor | workflow | routes a failed record to an ending |
| Accept an actor | workflow | the same |
| Reject an actor | workflow | the same |
| Create a wallet | workflow | the same |

---

## 2. Problem Statement

**Eight published acts do what v5 did not say they do, under the identities v5 published.**

This change shall:

- give each of the eight a new identity that does what it does today;
- return each published identity to what v5 published, and stand it down;
- have everything in force that names one of them name its successor;
- keep every identity and wallet act doing exactly what it does today.

### What the business already decided

These are settled and are not reopened by this change:

- **Identity is fixed at publication.** An unpublished identity may change before release; a
  published one may not.
- **A change of meaning is a new identity.** The old one stays in the record and out of reach.
- **What `cr_06` decided is right.** A failed record ends the act, and nothing it does is relaxed.

---

## 3. Clarifications answered by the business author

- **Does any request get a different answer?** No. Every act answers exactly as it does today.
- **Are the stored records touched?** No. Only the identities that state the acts change.
