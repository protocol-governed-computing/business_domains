# Delivery — cr_11_repeat_announces

**Decided by:** the domain owner, in this change's `ledger.yaml`. The ledger is the decision; every
other document here is derived from it.
**Designed against:** composition `d4396c629d04…` (`baseline.json`).
**Delivered:**
- A repeated registration announces that the actor registered again, with the details it
  submitted, apart from a first registration.

**Validated:**
- Phase documents 7/7 admissible. Construction 1313/1313 determined.
- Identity 26/26, routing closure 6/6, wallet 12/12, owner decisions 9/9: every criterion of cr_08
  to cr_11 (`testbed/identity/execution_validation_owner_decisions.py`).
- This ledger equals the derive route's test ledger for blockchain, answer for answer.

---

## What changed

One ledger answer, `on_repeat.announces`, and the event it names. `EV_ACTOR_REGISTERED_AGAIN_V0` is
new, and registration's workflow takes its next version.
