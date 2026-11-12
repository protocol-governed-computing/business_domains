# Delivery — cr_09_reinstatement_announces

**Decided by:** the domain owner, in this change's `ledger.yaml`. The ledger is the decision; every
other document here is derived from it.
**Designed against:** composition `d72ae85963f9…` (`baseline.json`).
**Delivered:**
- Reinstating a book announces that the book was reinstated. Reinstating a physical copy announces
  that the copy was reinstated. Retirement already announced; reinstatement now does as well.

**Validated:**
- Phase documents 7/7 admissible. Construction 2176/2176 determined.
- Registration 23/23, works 27/27, owner decisions 8/8: every criterion of cr_06 to cr_09.
- This ledger equals the derive route's test ledger for the catalog, answer for answer: the domain
  now stands where its owner decided.

---

## What changed

Two ledger answers, under `announces`. Two events are new: `EV_BOOK_REINSTATED_V0` and
`EV_PHYSICAL_COPY_REINSTATED_V0`. The two reinstatement workflows and their entrances take their
next versions.
