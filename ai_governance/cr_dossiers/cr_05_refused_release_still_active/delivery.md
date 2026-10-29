# Delivery — cr_05_refused_release_still_active

**Decided by:** the domain owner, in cr_02. This change's `ledger.yaml` states the decision. Every
other document here is derived from it.
**Designed against:** composition `11a41c349dc9…` (`baseline.json`).
**Delivered:** a reclaim that the license registry refuses ends as still active. The license stays
assigned and nothing is announced. The reclaim releases the license before it moves it, so nothing
has changed when it ends there.

**Validated:**
- **Criteria, before the design:** 3/4 hold (`criteria_before.txt`). The one that fails is the
  decision: the reclaim ended at `EXIT_REJECTED`.
- **Criteria, after delivery:** 4/4 (`criteria_after.txt`).
- Phase documents 7/7 admissible. Construction 1929/1929 determined.
- Owner decisions 21/21 and routing closure 4/4.
- This ledger equals the derive route's test ledger for ai_governance, and re-deriving it keeps all
  59 artifacts.

---

## What changed

One ledger answer, `release_refused: otherwise`, on `reclaim license`. The answer is new to the
ledger. The route admits it from its seal `dossiers/release_refused_ends_otherwise`
(`transformation_compilers`).

The release step's `VIOLATION`, the registry's refusal, now routes to `EXIT_STILL_ACTIVE`. A
`BACKEND_ERROR` still ends the reclaim at `EXIT_REJECTED`. `WF_RECLAIM_LICENSE_V0` is superseded by
`WF_RECLAIM_LICENSE_V1`, and its entrance names the successor. The deletion is recorded in
`.github/process/retired_identities.yaml`.

**Callers.**
- Delivery repointed the domain's testbed.
- `protocol_runtime/testbed/pgc/test_step_outcome.py` was repointed by hand, because it uses the
  reclaim as a fixture.

**Route change found on the way.** Re-deriving this ledger refused `replaces: [auto reclaim]`. The
design of record names only `_V1`'s predecessor, `_V0`, so the replacement cr_04 made had left it.
The route now reads the replacements already made from the retirement ledger as well. That change is
sealed by `dossiers/replaces_spent_across_versions`.
