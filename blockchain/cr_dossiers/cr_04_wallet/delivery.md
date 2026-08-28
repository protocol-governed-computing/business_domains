# Delivery — cr_04_wallet

**Authorized by:** Gate 1 and Gate 2, at P7 and P8, against composition `381ba055108b…`
**Delivered:** the wallet function entire — an accepted person is given a wallet, the moments identity
declares are announced, a rejection stating no grounds is refused, the act declares the records it
reads, and a person the business has not accepted is refused
**Validated:** wallet 9/9, identity 15/15, both against a composition built from this design alone

---

## What this dossier is

It was authored once, delivered, and then **re-authored from P0 against the composition it had
produced**. That is unusual enough to state plainly, because a reader meeting it will find a change
whose artifacts mostly already exist.

The first pass built the wallet function. Two things it had been asked for were not in what it built,
and both were found by running the act rather than by reading the design:

- **the act read records identity owns and said nothing about it**, so it halted on its second step
  asking for a record it never declared it would read;
- **a person nobody accepted was given a wallet**, though the business had enumerated that refusal
  at P0 in `operation_refusals`.

The first was raised as a separate change request. That was the wrong shape: an EXTEND is a whole
redeclaration, so two in-flight dossiers each declared themselves the whole of one artifact and
neither was complete. Emitting either silently reverted the other, and **nothing refuses that** —
the narrowing check compares an amendment against its own pinned baseline, where the other change's
additions do not yet exist. The two were consolidated here, and the rule that prevents a repeat is in
`transformation/CLAUDE.md`: a subject touching an artifact a dossier in flight declares is not a new
change request.

---

## What it took

**The refusal was declared and never discharged.** P0's `operation_refusals` carried four rows.
Three became branches — `NOT_FOUND`, `ALREADY_EXISTS`, and the grounds check. The fourth, *"the
person has not been accepted, or was rejected"*, travelled through all nine phases as prose: it is in
P1 verbatim, in P5 as a business invariant, and in P7's design resolution as a promise of *"declared
outcomes routing to a terminal node"*. The topology routed `SUCCESS / NOT_FOUND / VIOLATION`. There
was no branch for *held, but not accepted*, and every phase passed with 100% construction
completeness while an unverified person held value.

Nothing could have caught it. `operation_refusals` is read by exactly one rule, in P1, checking the
rows arrive from P0 unchanged; no phase reads it afterwards. No rule grounds a workflow node's
routing in what the contract it invokes can answer. The only rule touching P5's invariants asks
whether the Business Reason cell is empty. **The pipeline traces artifacts, not obligations** — and
that gap is now the next change on the board.

**A business rule the caller supplies is a business rule the caller can widen.** The refusal was
first designed to take its admitted states from the payload, copying identity's precedent for
`states_admitting_a_decision`. It refused everyone, because nothing sent the field — and the fix was
not to send it. A caller passing `["UNVERIFIED","ACCEPTED"]` reopens exactly the hole being closed,
so the design fixes the set as a literal. **Identity still takes its own admitted states from the
caller**, and that is recorded as an open issue rather than quietly changed here.

**Two dead branches, removed, and the cost of removing them.** `OBSERVATION_WITHOUT_INTERPRETATION`
found two clock steps routing on `VIOLATION`, which `NOW` cannot answer — a branch nothing can reach.
They route on `BACKEND_ERROR` now. Removing them tripped the known limitation that a design can add
and cannot deliberately remove: `AMENDMENT NARROWS — 2 fact(s) lost`, and `tc construction check`
exits 1. True in fact, false in intent.

**Re-pinning turns a change's own additions into amendments.** Seventeen artifacts this dossier
authored already existed in the composition it was re-pinned against, so they moved from `NEW` to
`EXTEND`. That is honest against the current pin and it costs something: the dossier no longer records
that it authored them. Git does.

---

## What the composition holds

```
WF_CREATE_WALLET_V0
  consults: [blockchain::RB_IDENTITY_BINDINGS_V0]

  IN_WALLET_CREATION_V0          ACK     -> CC_RESOLVE_ACTOR_V0
  CC_RESOLVE_ACTOR_V0            SUCCESS -> CC_REQUIRE_ACCEPTED_HOLDER_V0
  CC_REQUIRE_ACCEPTED_HOLDER_V0  SUCCESS -> CC_DETERMINE_WALLET_IDENTITY_V0 ; VIOLATION -> EXIT_REJECTED
  …
  CC_APPEND_WALLET_OCCURRENCE_V0 SUCCESS -> EXIT_SUCCESS
```

`CC_REQUIRE_ACCEPTED_HOLDER_V0` is the one artifact this pass authored: a single step naming
`CT_PURE_VALIDATE_SET_MEMBERSHIP_V0`, which **raises**. That matters — a transform that returned its
judgement would leave the step succeeding whatever it found, and the refusal the business declared
would be a branch nothing reaches.

---

## What it proved, by running

The reach is read-only and it is checked rather than asserted: every store identity owns is hashed
before the wallet act and after it, refused acts included, and the hashes are identical. The wallet's
own three stores are written. No identity artifact changed — one file moved in the whole repository.

```
OK  an accepted person is given a wallet, and the act runs to completion
OK  identity's records are consulted and never written — byte for byte what they were
OK  an unverified person is refused a wallet, and none is recorded for them
OK  a person the business already gave a wallet is not given a second
OK  no refused wallet act left a mark on identity's records
```

And identity's own criterion — *an unverified or rejected actor holds no wallet* — declared by
`cr_01_identity` and skipped ever since for want of a wallet, is exercised at last and holds.

---

## What this change did not do

It does not decide what happens to a wallet if its holder is later rejected. That is a question about
a wallet that already exists.

It does not give the other wallet acts a reach. One act needs it; another that needs it declares it
in the change that needs it.

It leaves one criterion unexercised: a wallet act attempting to write through the reach. No act is
authored to try, so there is nothing to dispatch — the platform refuses it at run time and proving
that needs an act written to attempt it.
