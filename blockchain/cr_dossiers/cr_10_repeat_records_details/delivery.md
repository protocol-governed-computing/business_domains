# Delivery — cr_10_repeat_records_details

**Decided by:** the domain owner, in this change's `ledger.yaml`. The ledger is the decision; every
other document here is derived from it.
**Designed against:** composition `d76b1c207cd0…` (`baseline.json`).
**Delivered:**
- A repeated registration records the details it submitted. The actor already registered is
  unchanged by them.

**Validated:**
- Phase documents 7/7 admissible. Construction 1290/1290 determined.
- Identity 26/26, routing closure 6/6, wallet 12/12.

---

## What changed

One ledger answer: `on_repeat.records`. Registration's workflow takes its next version, and the
recorder of a repeat is new.
