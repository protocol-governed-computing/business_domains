# Delivery — cr_06_catalog_derived

**Decided by:** the domain owner, in this change's `ledger.yaml`. The ledger is the decision; every
other document here is derived from it.
**Designed against:** composition `1605993494b6…` (`baseline.json`).
**Delivered:**
- The catalog's design is derived from its ledger by the Design Compiler's derive route. Every phase
  document, P0 to P6, is projected from the ledger, and P7 and P8 are the derived design.
- Behavior stays as the design of record had it. The caller states the search filter, an empty
  search is refused, and reinstatement announces nothing.
- Three corrections come with it, because the ledger has no shape for the earlier form:
  - a transition checks the state it moves from, so retiring a retired book is refused;
  - the trail names every operation's subject by its identity, including a registration, which
    recorded the title before;
  - an update may change a book's identity, as P0 stated. The edition moves to the work its new
    title and author name, its copies follow, and the old identity is freed. The design of record
    refused any identity change, a narrowing no phase before P7 stated.

**Validated:**
- Phase documents 7/7 admissible. Construction 2154/2154 determined.
- Registration 23/23, works 27/27. The corrections are criteria of `execution_validation_owner_decisions.py`, first run after cr_09.

---

## What changed

Kept 23, superseded 18, new 14, retired 10. Each workflow takes its next version, because the
doctrine composes it differently: one validation step, claims in a fixed order, and a from-state
check on every transition. Each successor names its predecessor in `supersedes`. The predecessors
are deleted and recorded in `retired_identities.yaml`.

The registration, retirement and reinstatement contracts the design of record held are retired.
The derived design composes those acts from shared components (`CC_MOVE_*`, `CC_RECORD_CATALOG_MOMENT_V0`,
`CC_CHECK_*_SUBMISSION_V0`). The testbed's suites are repointed to the successor workflows.
