# Business Problem Statement

**Project Name:** blockchain

## 1. Context

This project establishes the **blockchain** system.

The overall project scope includes the following blockchain functions:

- identity
- wallet
- transaction
- mempool
- block
- chain
- consensus

This change request establishes the **identity** function, which is the first of them. Nothing in
this domain exists yet, so this change introduces a function rather than extending one.

Identity is first because every other function names an actor. A wallet belongs to someone, a
transaction is submitted by someone, a validator is someone the chain has agreed to trust. None of
those can be said accurately until the business can say who an actor is and whether it has accepted
them. The purpose of this change is to let the business admit a person to the system and then decide,
as a separate act, whether that person is trusted.

---

## 2. Problem Statement

The business needs to let people join the system before it knows anything about them, and to decide
afterwards whether to trust them. Those are two different decisions made by two different parties at
two different times, and treating them as one is what this change exists to prevent.

Someone who wants to use the system supplies their own details and is admitted immediately, but
admitted as *unverified* — known to the system, not yet trusted by it. Separately, an authority
inside the business reviews that person and records a decision. Until that decision is recorded the
person is in the system and can do nothing that requires trust.

**The question this change exists to answer is what an unverified actor is permitted to be.** Every
other question follows from it: whether admission can fail, what a second admission of the same
person means, whether a decision can be revisited, and what the business is able to prove afterwards
about who decided what. If being unverified were merely a label on an otherwise ordinary actor, the
two-step design would be ceremony. The business author has settled it in §3: an unverified actor is a
claim the business has recorded and not yet accepted, it may hold no wallet and submit no
transaction, and it is not a lesser actor but a different thing.

The identity function shall allow:

- a person to register themselves, supplying their own identifying details, and be admitted in an
  unverified state
- an authority to record a verification decision against a registered person, accepting or rejecting
  them

Every business operation shall be traceable and auditable. The business must be able to show, for any
actor, who admitted them, who decided about them, what was decided, when, and on what stated grounds.
That record is evidence, and it is written as the decision is made rather than reconstructed later.

### What identity does not decide

Identity says who an actor is and whether the business trusts them. It does not say what a trusted
actor may then do. Permissions, roles beyond the distinction between an ordinary participant and an
authority, and any notion of an actor's standing changing through their conduct are outside this
change.

### Deferred to follow-on changes

The business has further identity needs which are **named here and deliberately excluded from this
change**, because each rests on the unverified-actor question above and cannot be settled before it
is:

- **Re-application after rejection.** A person the business has rejected may later have grounds to
  ask again. Whether that is a new registration, a reopening of the original decision, or something
  the business refuses outright depends on what a rejection is taken to mean, which this change is
  the first to state.
- **Revocation of a verified actor.** Trust once given may need to be withdrawn — for conduct, for
  expiry, or because the original decision was wrong. What that leaves behind, and what happens to
  what the actor did while trusted, is a governed change of its own.
- **Authority over verifiers.** This change records which authority made a decision. It does not
  govern who is permitted to be an authority, nor how that permission is granted or removed.
- **Identity documents and evidence.** The business currently records that a decision was made and
  the grounds stated for it. Attaching the material an authority actually examined is a separate
  need with its own retention and privacy consequences.
- **Correcting an actor's own details.** A person's name, contact address or preferences may change.
  What that means for a decision already made against the earlier details is not answerable until a
  decision is defined.

This release intentionally excludes wallets, transactions, mempool, blocks, chain and consensus,
except where identity behaviour is depended upon by those functions.

---

## 3. Clarifications answered by the business author

The following business questions were put to the business author and answered by them. They were not
assumed by the design process.

### The unverified actor

- **What is an unverified actor?** A claim the business has recorded and not yet accepted. The person
  exists in the system, is addressable, and is trusted with nothing. It is not a lesser actor; it is
  a different thing, and the business would rather say "we have not decided" than imply a decision it
  has not made.
- **What may an unverified actor do?** Nothing that requires trust. It may hold no wallet and submit
  no transaction. It may be looked at, decided about, and nothing else.
- **May registration be refused at the moment it is made?** Only for details the business cannot
  read — a missing name, a missing contact address. Refusing on judgement at this point would be
  making the verification decision early, under a different name and by the wrong party.
- **What counts as a detail the business cannot read, as against one it does not believe?** A detail
  is unreadable when it is absent or is not of the form the business asked for — no name at all, no
  contact address at all, or something offered as a contact address that is not shaped like one.
  Everything else is a matter of belief: whether the person controls that address, whether the name
  is theirs, whether they are who they say. Belief is the verification decision's business and never
  registration's. The test is deliberately mechanical, because any test requiring judgement would be
  the verification decision made early by the wrong party.
- **Who registers a person — the person themselves, or the business?** The person themselves. The
  details are their claim about who they are, which is exactly why the business does not treat them
  as established.

### Identity of an actor

- **What identifies an actor?** The contact address they register with. Two registrations carrying
  the same contact address are the same person.
- **What happens when the same person registers twice?** They remain one actor. The second
  registration does not create a second person and does not fail — the person is simply already
  known. The business would rather absorb a repeated registration than reject a person who is unsure
  whether their first attempt succeeded.
- **Is the second registration recorded?** Yes, as a distinct occurrence against the same actor. That
  a person registered twice is a fact about them the business wants to keep, and an audit trail that
  silently dropped it would be an audit trail that could not be trusted about anything else.
- **Does a repeated registration reset a decision already made?** No. A decision, once recorded,
  stands until a governed change withdraws it, and no act of the person themselves may disturb it.
- **May the second registration carry details differing from the first, and if so which prevail?**
  It may, and the first prevails. The actor keeps the name and preferences it was admitted with; the
  differing details are recorded as part of the occurrence and change nothing. The business would
  rather hold what it admitted and keep a record of what was later claimed than let an actor be
  quietly rewritten by anyone able to name its address. Correcting details is deliberately a separate
  change, deferred in §2.

### The verification decision

- **Who decides?** An authority within the business, acting as a distinct kind of actor from the
  person being decided about. A person may never verify themselves.
- **What may be decided?** Accepted or rejected. There is no third outcome and no deferral: an
  authority that is not ready to decide has not decided, and the actor stays unverified.
- **May an actor be decided about before being registered?** No. There is nothing to decide about.
  The decision is a decision on a registration, and without one it is not an incomplete decision but
  a meaningless one.
- **Is a rejection recorded differently from an acceptance?** Yes, and this matters more than it may
  appear. A rejection is its own occurrence, distinct in kind from an acceptance. The business must
  be able to ask "who has been rejected" and receive an answer, and it must never be possible to read
  a rejected actor as a verified one.
- **Does a rejected actor become trusted in any respect?** No. A rejected actor is trusted with
  nothing, exactly as an unverified one is, and is recorded among the actors the business has
  accepted in no sense whatever.
- **May a decision be made twice about the same actor?** No. An actor is decided about once. What
  happens after that — re-application, revocation — is deferred in §2 and deliberately not answered
  here.
- **Must the authority state grounds?** Yes for a rejection, where the grounds are the substance of
  the decision. For an acceptance the grounds may be omitted, because the decision itself is the
  statement.
- **Is the deciding authority recorded?** Yes, on every decision, acceptance and rejection alike. A
  decision whose author is unknown is not evidence.
- **Must an authority be a registered actor of this system, or may it be identified outside it?**
  Identified outside it. An authority is part of the business, not a participant that registered and
  was verified, and requiring it to have been admitted through the same door would make the first
  decision impossible to make. Identity records which authority decided; it does not hold authorities
  and does not resolve one. Which persons may be an authority is deferred in §2, and this is why: a
  name recorded and not resolved is exactly what that later change will have to take up.

### The record

- **When is the time of an event determined?** At the moment the event occurs. Every recorded
  occurrence carries the time it actually happened, and the business regards a record whose times do
  not advance as no record at all.
- **May a recorded occurrence be altered or removed afterwards?** No. The record is added to and
  never rewritten. A correction is a further occurrence stating the correction, not an edit of what
  was written before.
- **What must the business be able to show about any actor?** That they registered and when, every
  time they registered, whether a decision was made, by which authority, what it was, when, and the
  grounds stated for it.

### Preferences

- **Does the business need anything beyond identity to admit a person?** Two preferences are
  collected at registration: the currency the person prefers to be quoted in, and the language they
  prefer to be addressed in. Both are conveniences, both have a default, and neither bears on
  identity or on the verification decision.
- **What are the defaults?** BACHI for currency and English for language. A person who states no
  preference is recorded as preferring those, rather than as having stated nothing — the business
  wants every actor to carry an answer, so that nothing downstream has to decide what an absent
  preference means.
- **Do preferences distinguish one actor from another?** No. Two registrations differing only in
  preference are the same person.

The remaining project functions continue to be adjacent to this change: named, planned, and outside
the scope of this governed change. The identity needs deferred in §2 — re-application, revocation,
authority over verifiers, identity evidence and correction of details — carry their own
clarifications, which belong to the changes that take them up.
