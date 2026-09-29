# Business Problem Statement

**Project Name:** ai_governance — ai_licensing

## 1. Context

The business provisions licenses for AI tools to its employees and takes back licenses nobody uses.
Three checks decide it. An employee is provisioned only while licenses remain under the business's
cap, and only once they have completed the required training. A license is reclaimed once it has gone
unused for the business's threshold of days.

Each check refuses when its answer is no. A request past the cap, from an employee without the
training, or to reclaim a license still in use, is refused, and nothing is provisioned or reclaimed.

---

## 2. Problem Statement

**Nothing proves the three checks decide what the business decided.**

Each check is declared, built and run by the business's own acts, and none of them is proven. A
check is proven by cases stated beside it — what it is given, and what it must answer — that are run
against it on every build. These three have none.

The cases the business had for them were written for the system this one replaced, and they disagree
with this one. They expect each check to answer no and succeed; this system's checks refuse instead,
as the business decided they should. They also name two things by names this system does not use:
the date an inactivity check is made as of, and what a training check answers.

This change shall:

- state, beside each of the three checks, the cases that prove it: a case it admits, with what it
  answers, and a case it refuses;
- take those cases from the ones the business already had, restated so they expect a refusal where
  the answer is no, and use this system's names;
- leave what each check decides, and every act that uses them, unchanged.

### What the business already decided about these checks

These are settled and are not reopened by this change:

- **A check whose answer is no refuses.** It does not answer no and let the act continue.
- **A license is available while fewer are assigned than the cap.** At the cap, none is.
- **An employee is eligible once their required training is complete.**
- **A license is inactive once it has gone unused for the threshold of days or more.**

### What this change does not decide

- **The cap, the training required, or the threshold.** Each is stated by the act that uses the
  check, and none changes.
- **Anything about the agent_governance subdomain.**

---

## 3. Clarifications answered by the business author

These questions were put to the business author and answered by them. The design process did not
assume them.

- **The earlier cases are two per check: one answered yes, one answered no. Should the no case become
  a refusal case, and the yes case stay with its answer?** Yes. The no case expects a refusal.
- **The earlier inactivity cases state a date the check is made as of under a name this system does
  not use. Should they keep their dates under this system's name?** Yes. The values stay; the names
  are this system's.
- **Should each check also be proven at its boundary?** The cap exactly reached is already an earlier
  case. Add one more: a license unused for exactly the threshold is inactive.
