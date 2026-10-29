# Delivery — cr_08_empty_search_answers_empty

**Decided by:** the domain owner, in this change's `ledger.yaml`. The ledger is the decision; every
other document here is derived from it.
**Designed against:** composition `0c5b578bc4fe…` (`baseline.json`).
**Delivered:**
- A search that matches nothing answers with no books. It was refused before.

**Validated:**
- Phase documents 7/7 admissible. Construction 2139/2139 determined.
- Registration 23/23, works 27/27.

---

## What changed

One ledger answer: the search's `nothing_found: empty`. The search selects with
`capability_transforms::CT_PURE_SELECT_RECORDS_V0`, which answers an empty list. The search
contract, its entrance and its workflow take their next versions (V3, V2 and V3).
