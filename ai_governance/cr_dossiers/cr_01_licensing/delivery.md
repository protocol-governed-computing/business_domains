# Delivery — cr_01_licensing

**Authorized by:** Gate 1 and Gate 2, at P7 and P8, against composition `25009fed290d…`
**Delivered:** the three checks that decide licensing are proven. The license check, the training
check and the inactivity check each carry the cases that prove them, which run against them on every
build.
**Validated:** transform conformance for ai_governance is 3 proven, 0 unproven, 7 cases; full
regression 57/57 on a clean rebuild, composition `b8dd7145232e…`

---

## What this change closed

Each check was declared, built and run by the business's own acts, and none was proven. The cases the
business had were written for the system this one replaced. They expected each check to answer no and
succeed, where this system's checks refuse, and they named the inactivity check's evaluation date and
the training check's answer by names this system does not use.

Now each check is redeclared whole, as it stands, with its cases. Each no case expects a refusal, and
each yes case keeps its answer. The earlier values stay under this system's names. One case was added:
a license unused for exactly the threshold is inactive. The domain's build manifest is regenerated so
that the domain compiles the cases. Nothing any check decides, and no act that uses one, has changed.

---

## What it took

**The refusals were the checks' own.** The seed first listed the three refusals as refusals of
operations. A refusal of an operation is carried out by an act, so P7 had to restate both acts whole
to show where. That exposed one more thing: provisioning records a denial and completes, so the
design check found no refusing ending to reach. The author ruled the refusals the checks' own, proven
by their refusal cases, and dropped them from the seed. P1 was re-projected, and P7 names only the
checks and the manifest.

**Construction was fixed twice on the way.** A change that only amends produced no build manifest,
so the domain could not have compiled the cases, and the manifest named only the subdomains the
change declared. And `emit` wrote the checks without the descriptions that `check` had measured them
with. Both are recorded in `.github/process/rulings.md`.

---

## What is carried

- **Provisioning records a denial as a completion.** A denied request ends at `EXIT_DENIED`, which
  completes and announces the denial. Nothing is provisioned. Whether that ending should be a refusal
  is a question about the act, not the checks, and is left open.
- **The checks' prose.** Each check's hand-written Intent section is replaced by its summary; its
  description and every field's description are carried unchanged.
