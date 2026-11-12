# Delivery — cr_08_derived_design

**Decided by:** the domain owner, in this change's `ledger.yaml`. The ledger is the decision; every
other document here is derived from it.
**Designed against:** composition `50aeec1b85ea…` (`baseline.json`).
**Delivered:**
- Identity's and wallet's designs are derived from their ledger by the Design Compiler's derive
  route. Every phase document, P0 to P6, is projected from the ledger, and P7 and P8 are the derived
  design.
- Behavior stays as the design of record had it: no listing of actors, and a repeated registration
  records its moment and announces nothing of its own.
- One correction comes with it, because the ledger has no shape for the earlier form: a wallet's
  address is unique, claimed in its own registry, so a key already used for one wallet is refused
  for another. The ledger cannot state an address that is neither claimed nor written on the wallet.

**Validated:**
- Phase documents 7/7 admissible. Construction 1163/1163 determined.
- Identity 26/26, routing closure 6/6, wallet 12/12.

---

## What changed

Kept 17, superseded 9, new 13, retired 12. The workflows take their next versions, because the
doctrine composes them from shared components (`CC_RESOLVE_ACTOR_IDENTITY_V0`,
`CC_MOVE_ACTOR_FROM_UNVERIFIED_V0`, `CC_RECORD_*_MOMENT_V0`). The client's screens and the testbed's
suites are repointed to the successor workflows. The public names, the transport entrances and the
HTTP binding are unchanged.
