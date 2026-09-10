# Business Problem Statement

**Project Name:** blockchain

## 1. Context

The blockchain project covers seven functions: identity, wallet, transaction, mempool, block, chain
and consensus.

Identity is built and reachable. A person registers themselves and is admitted unverified. An
authority then records a decision about them, accepting or rejecting them.

The business decided at the outset that a person keeps the details they were admitted with. Nothing
an authority does should change who a person said they were.

That is not what happens.

---

## 2. Problem Statement

**Recording a decision erases what the business already knows about the person.**

When someone registers, the business holds their name, their contact address, and the two preferences
they were admitted with. When an authority then accepts or rejects them, the business is left holding
only their address, their state, and the name of the authority who decided. The person's own name is
gone. So are their preferences.

Nobody asked for that. The business stated the opposite rule and has been breaking it since the
function was built.

This is a defect, not a new requirement. The business is not deciding anything here that it has not
already decided — it is making the system do what it already said it would do.

This change shall:

- leave everything the business knows about a person untouched when a decision is recorded, except
  the three things a decision is entitled to change: the person's state, the authority who decided,
  and the grounds they stated

### What a caller sees

Nothing. What a caller sends and what they are told back are unchanged. A person using the web page
cannot tell that anything is different, and neither can anyone recording a decision another way.

### What this change does not decide

- **Anything about how a decision is performed**, beyond not destroying what it should not touch.
- **Anything about grounds.** A rejection must state them and an acceptance need not, exactly as
  before.
- **Anything about who may be an authority**, or whether the one named is entitled to decide.
- **Anything about the other six functions.**

### Left for later changes

- **Records already thinned.** People decided about before this change have already lost their
  details. The business is not going back for them — the record is added to and never rewritten, and
  that rule holds even when what was written is thin.
- **Correcting a person's own details.** Still a separate change and still deferred.

---

## 3. Clarifications answered by the business author

These questions were put to the business author and answered by them. The design process did not
assume them.

- **What should a decision change about a person?** Three things: whether they are accepted or
  rejected, who decided, and the grounds stated. Nothing else.
- **What should it leave alone?** Everything else the business holds about them, starting with the
  name and the preferences they registered with.
- **Is this a rule the business is adding?** No. The business already decided that a person keeps
  what they were admitted with. This is the system catching up to it.
- **How did anyone notice?** A person was registered from the web page and then accepted, and the
  record afterwards no longer carried their name.
- **Does a decision ever have a reason to change a person's own details?** No. A decision records a
  decision. Changing a person's details is a different act, and a deferred one.
- **What about people already decided about, whose details are gone?** They stay as they are. The
  business does not rewrite what it has recorded, and it would rather carry a thin old record than
  start editing history.
- **Does anything a caller sends or sees change?** No. This is invisible from outside, and it should
  be.
- **Is the trail affected?** No. The same moments are recorded, saying the same things.

The other six blockchain functions remain adjacent to this change: named, planned, and outside its
scope.
