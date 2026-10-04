# Delivery — cr_06_routing_closure

**Authorized by:** Gate 1 and Gate 2, at P7 and P8, against composition `f8356d9c8938…` (v5)
**Delivered:** every identity and wallet act ends as rejected when a record it needs cannot be read or
written, at the step whose record failed. Five steps that carried on past a failed record now stop,
and thirteen act nodes route a failed record to the rejected ending they already had.
**Validated:** routing closure 6/6 (2 not exercised), identity 22/22 (3 not exercised), wallet 9/9
(1 not exercised); full regression 11/11; composition `74b822498da7…`

---

## What this change closed

When an authority accepted a person, identity first looked the person up. If the lookup failed,
identity carried on, read the person's record and recorded the acceptance. Three wallet steps did the
same with a failed claim, write or append. And thirteen act nodes ran a contract that could end with
a failed record, with no route for it, so the act stopped and nothing the business declared said how.

Now each of the five steps answers for the failed record its store declares, and ends its contract
with it. Each act routes a failed record to EXIT_REJECTED. Run against the new composition, an
acceptance whose lookup fails ends at EXIT_REJECTED, the person stays unverified, and nothing after
the lookup runs. Before this change the same run recorded the acceptance (SoSyM study, case O3).

Eight artifacts were redeclared whole; nothing was created and nothing was withdrawn.

---

## What it took

**The design was gathered, not retyped.** Each amended artifact is restated from the dossier that last
stated it: `CC_RESOLVE_ACTOR_V0` from `cr_01_identity`, the three wallet contracts and
`WF_CREATE_WALLET_V0` from `cr_04_wallet`, and the three identity acts from `cr_05_identity`. Only the
answers to BACKEND_ERROR were added. Construction measured 380 of 380 facts determined, and the
emitted diff is those answers plus the current renderer's body layout on the five artifacts last
rendered by an older design.

**Two rules had moved on since `cr_04_wallet`.** The design's success ending for `WF_CREATE_WALLET_V0`
is now typed EXIT_SUCCESS, as the current rule set requires of an ending that announces a moment. And
the inventory names `AC_PARTICIPANT_V0`, which is how construction learns the context the acts run
under.

**The change is the domain half of `v1` Changes 3 and 4 of the Open PGC Standard.** CP-13 requires a
composed step to answer for every outcome its store declares; GC-15 requires construction to refuse
an outcome no route answers. Blockchain now has no step gap and no unrouted outcome in any act it
dispatches.

---

## What is carried

- **The superseded act** `WF_RECORD_VERIFICATION_DECISION_V0` keeps three unrouted nodes. It is not
  dispatched, so no request reaches them, and GC-15 binds only what execution can reach.
- **A failure and a refusal end the same way.** The business keeps two endings; telling them apart is
  a later decision.
- **Records made before a failure stay.** A registration whose trail append fails has already
  recorded the person. The business adds to its record and does not rewrite it.
