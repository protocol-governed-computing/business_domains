# Delivery — cr_07_search_excludes_retired

**Decided by:** the domain owner, in this change's `ledger.yaml`. The ledger is the decision; every
other document here is derived from it.
**Designed against:** composition `32c325ad3ec9…` (`baseline.json`).
**Delivered:**
- A search never answers with a retired book, and a caller cannot ask it to. The exclusion is the
  catalog's rule, stated once in its ledger.

**Validated:**
- Phase documents 7/7 admissible. Construction 2141/2141 determined.
- Registration 23/23, works 27/27.

---

## What changed

One ledger answer: the search operation's `always_exclude: {state: retired}`, with
`caller_may_override: false`. The search contract, its entrance and its workflow take their next
versions (V2, V1 and V2). Nothing else changes meaning.
