# Delivery — cr_03_catalog

**Authorized by:** Gate 1 and Gate 2, both closed against composition `9c2c693d882e…`
**Delivered:** six catalog acts announce the eight moments they complete, where they announced
nothing
**Produced:** composition `6e1e571dbbb8…`, 390 artifacts, conformance PASSED

---

## What was delivered

**Eight announcements across six acts.** `WF_REGISTER_BOOK_V0` announces three at one ending, in the
order the business completes them — the work, then the book, then the physical copy. The other five
acts announce one each: an additional edition registered, a physical copy registered, bibliographic
information updated, a book retired, a physical copy retired. All six moments were declared long ago
and referenced by nothing; what changed is that the acts completing them now say so.

No artifact was authored. The mandate scheduled no build step, and the six acts were re-rendered
whole from the design, which is what an EXTEND means.

**The two reinstatement acts are untouched, deliberately.** The business declares no moment for
either, so announcing one would be inventing a moment nobody asked for. They stay silent and the
dossier says why.

## The halt, and what closed it

This dossier halted at P2 for a platform capability it could not work around: an act announcing
several moments at one ending. Announcing only one and leaving two silent was the defect the change
exists to fix; splitting the registration act into three was changing the business to suit the
platform. `multi_emission` delivered the capability — the clause, the invariant, the sealed
sequence, the runtime and the renderer — and this dossier resumed at P3 with no design decision
reopened.

## The design was refused before it was gated, and the refusal was right

Construction Completeness read **98.2%** and named one missing fact six times: `core.actor_context`,
once per act. The design inventoried the six acts and the six moments, and not the actor those acts
run as.

Every catalog act carries `book_library_mgmt::AC_LIBRARY_STAFF_V0` in the composition, and an EXTEND
re-renders an act **whole** from the design — so a design silent about the actor re-renders six acts
with none, dropping the authorization binding from every catalog operation while every phase read
ADMISSIBLE. `cr_02` had named the actor as a `REUSE` row; this dossier had not.

One row was added to P6's `pps_artifacts_requiring_action` and one to P7's `existing_inventory`,
both before Gate 1. They state what was always true and change no decision this dossier took.

**This is the value of measuring construction separately from admissibility.** A design failure is
an incomplete or contradictory mandate and a phase's rule set catches it. This was the other kind: a
mandate that was valid and did not uniquely determine the artifact. Nothing in P0–P8 was wrong.

## What the acceptance corpus needed

`construction_acceptance` renders a **sequence** of designs and compares the last renderer of each
artifact against what is built. cr_03 re-renders six workflows that cr_01 and cr_02 had rendered, so
until it joined the sequence the harness rendered them from a design that is no longer their design
of record — 46/52 with 12 field differences, six summaries and six announcements. A fixture copy of
this dossier was added and appended to `DOSSIERS`, and the corpus reads **52/52, 0 field
differences**.

## Verification

```
p0–p8                       ADMISSIBLE · 0 findings · pinned 9c2c693d…
construction check          100.0%   340/340 determined
construction_acceptance     52/52 artifacts · 0 field differences
emit_rule_sets --check      agrees
meta_test                   793 rules · 9 phases · 53 check kinds
differential                37 documents · both paths agree
e2e_phases_test             37 cases
projection_test             PASSED
implementation_closure      27 transforms
pgc_env_check               PASSED
inspector                   108/108
snapshot                    6e1e571d… · 7 domains · 390 artifacts · conformance PASSED
catalog                     23/23        collatz          SUCCESS
identity                    15/15 (2 not exercised)       ai_governance  SUCCESS (both workflows)
wallet                      9/9 (1 not exercised)
```

**The catalog validation was expected to be unaffected and is.** Its occurrence counts read store
records written by capability steps, not announced moments. Nothing in the composition counts
announcements — that is `multi_emission`'s own open question, not this dossier's to answer.
