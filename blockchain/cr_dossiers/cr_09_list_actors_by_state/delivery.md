# Delivery — cr_09_list_actors_by_state

**Decided by:** the domain owner, in this change's `ledger.yaml`. The ledger is the decision; every
other document here is derived from it.
**Designed against:** composition `0808e8c4064b…` (`baseline.json`).
**Delivered:**
- The business lists the actors in a given state, from inside only. A listing of a state no actor
  is in answers with none.

**Validated:**
- Phase documents 7/7 admissible. Construction 1219/1219 determined.
- Identity 26/26, routing closure 6/6, wallet 12/12.

---

## What changed

One operation in the ledger. Three artifacts are new: `WF_LIST_ACTORS_V0`, `IN_LIST_ACTORS_V0` and
`CC_LIST_ACTORS_V0`. Nothing changes meaning.

## What it took

The first delivery of this change superseded wallet's moment recorder: its trail became one stream
instead of one per wallet, and the wallet suite caught it (11/12). The derive route read a trail's
form from the hand-authored design, and did not recognize the form it writes itself. The route was
corrected, the first delivery undone by re-emitting cr_08 against the composition it was designed
against, and this change delivered again.
