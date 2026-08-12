# Halt — cr_03_catalog

**Phases reached:** P0 – P2, every one admissible
**Status:** HALTED, blocked by a platform capability gap
**Blocked by:** `transformation/dossiers/multi_emission`
**Do not:** patch this locally, narrow the scope to five moments, or split the registration act.

---

## Why it stops

The design is sound and the business requirement is settled. Six declared moments must be announced,
and five of them map cleanly onto an act that completes them:

| act | moment |
|---|---|
| register an additional edition | a book was registered |
| register a physical copy | a physical copy was registered |
| update bibliographic information | bibliographic information was updated |
| retire a book | a book was retired |
| retire a physical copy | a physical copy was retired |

The sixth does not, and cannot be made to. `WF_REGISTER_BOOK_V0` registers a work, its first edition
and that edition's first physical copy — three declared moments completed by one act. An act
announces one moment; the running system resolves one moment per act and outcome.

## What was rejected, and why it stays rejected

- **Announcing only one and leaving two silent** — the defect this change exists to fix.
- **Splitting the registration act into three** — changing the business to suit the platform.
- **Patching the design language alone** — a design would declare three announcements and the
  running system would fire one, silently.

## What the business ruled

`WF_REGISTER_BOOK_V0` completes three distinct business moments and must announce all three. This is
a missing platform capability, not an authoring problem. Reinstatement is silent, and the six are the
complete set.

## Resuming

When `multi_emission` is delivered, this dossier resumes at P3 with no design decision reopened. The
open question P2 recorded is already closed by evidence: `WF_REGISTER_BOOK_V0` *claims* a work
identity and `WF_REGISTER_ADDITIONAL_EDITION_V0` *resolves* an existing one, so a work is registered
by the first and never by the second.
