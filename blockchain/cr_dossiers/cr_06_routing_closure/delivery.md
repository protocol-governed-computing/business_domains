# Delivery — cr_06_routing_closure

**Authorized by:** Gate 1 and Gate 2, at P7 and P8, against composition `35ea7c30f956…`
**Delivered:**
- Every identity and wallet act ends as rejected when a record it needs cannot be read or written,
  at the step whose record failed.
- The eight acts whose meaning changed are their next versions. The versions v5 published are stood
  down unchanged.

**Validated:**
- Routing closure 6/6 (2 not exercised); identity 22/22 (3 not exercised); wallet 9/9 (1 not
  exercised).
- Published identity: none of the 500 changed meaning.
- Construction acceptance 179/181, red by design for the two pinned book_library differences.
- Full regression 63/63 as expected.

---

## What this change closed

**What happened before.** When an authority accepted a person, identity first looked the person up.
If the lookup failed, identity carried on: it read the person's record and recorded the acceptance.
Three wallet steps did the same with a failed claim, write or append. And thirteen act nodes ran a
contract that could end with a failed record and had no route for it, so the act stopped and nothing
the business declared said how it ended.

**What happens now.** The next versions of four contracts answer for the failed record each store
declares, at five steps, and end the contract on it. The next versions of four acts route a failed
record to EXIT_REJECTED. An acceptance whose lookup fails now ends at EXIT_REJECTED, the person stays
unverified, and nothing after the lookup runs.

**Identity.** v5 published all eight acts, so the change is stated under new identities:
- `CC_RESOLVE_ACTOR_V1`, `CC_CLAIM_WALLET_IDENTITY_V1`, `CC_CREATE_WALLET_RECORD_V1`,
  `CC_APPEND_WALLET_OCCURRENCE_V1`;
- `WF_REGISTER_ACTOR_V1`, `WF_ACCEPT_ACTOR_V1`, `WF_REJECT_ACTOR_V1`, `WF_CREATE_WALLET_V1`.

Each V0 gains only `superseded_by`. The three entrances and four intents that start an act name its
V1, and nothing else in them changed. Callers see the same acts under the same entrances.

---

## What it took

**The design is cr_06's, as REPLACE.** dev/18 delivered the same behaviour as an in-place amendment
of the eight published acts. This design restates it under new identities. Each V1 equals that
amendment, apart from `version` and `supersedes`. Construction determined 394 of 394 facts.

**Places keep their labels.** A place whose contract is replaced keeps its label and runs the V1,
through the topology's `Runs` column. So bindings that read a place (`results.<label>`), traces and
test paths are unchanged.

**Acceptance learned REPOINT.** The acceptance harness reproduced each artifact from the last design
that rendered it, so it reported the seven re-points as differences. A later design's REPOINT is now
applied to the earlier rendering, by the same function construction uses.

**Callers outside the composition moved.** These now run the V1 acts:
- the identity and wallet execution validations;
- the routing-closure validation;
- the RUNBOOK's payload loops.

---

## What is carried

- **The stood-down act `WF_RECORD_VERIFICATION_DECISION_V0`** keeps its unrouted nodes and still
  names the published lookup. Nothing dispatches it.
- **A failure and a refusal end the same way.** The business keeps two endings.
- **Records made before a failure stay.** The business adds to its record and does not rewrite it.
