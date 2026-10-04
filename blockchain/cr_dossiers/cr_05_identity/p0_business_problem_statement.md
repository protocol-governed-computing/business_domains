# Business Problem Statement

**Project Name:** blockchain

## 1. Context

The blockchain project covers seven functions: identity, wallet, transaction, mempool, block, chain
and consensus. Identity and wallet are built and reachable.

A person registers themselves and is admitted unverified. An authority then records a decision about
them — accepting or rejecting them — and an accepted person is given a wallet. The business has said
what a registration must contain, which people an authority may decide about, and which decisions it
may record.

Those rules are the business's. Today they are not held by identity. They travel with each request,
and identity applies whatever the request carries.

---

## 2. Problem Statement

**Identity applies its rules as the request states them, so a request can change the rules it is
judged by — and one of them, when it is broken, is noticed and then ignored.**

The public entrance to identity supplies the business's rules itself: what a registration must
contain, that only an unverified person may be decided about, and that the decision is to accept or
to reject. A person reaching identity through that entrance is held to them. But identity does not
hold them. It takes each one from the request, so anything that reaches identity another way states
its own rules and is judged by those.

A request that says an accepted person may be decided about again gets a second decision recorded. A
request that names a decision the business never allowed gets it recorded. The wallet function met
exactly this and closed it for itself: *a business rule the caller supplies is a business rule the
caller can widen.* Identity still has the hole.

**And a registration that breaks the business's own description of one is admitted anyway.**
Identity checks a registration against what it must contain and finds what is missing — and then
registers the person regardless. The check reports; nothing acts on the report. Through the public
entrance this cannot show, because the entrance refuses an incomplete request first. Any other way
in, it can.

This change shall:

- hold what a registration must contain in identity itself, and refuse a registration that does not
  meet it;
- hold in identity which people an authority may decide about, and refuse a decision about anyone
  else, whatever the request says;
- hold in identity which decisions may be recorded, and refuse any other, whatever the request says;
- hold in identity that an authority does not decide about themselves, and that a rejection states
  its grounds, whatever the request says;
- leave everything a caller sees through the public entrance unchanged.

### What the business already decided about identity

These are settled and are not reopened by this change:

- **A registration names the person and the address they are reached at.** Both are required.
- **A person is decided about once.** Only an unverified person may be accepted or rejected.
- **A decision is an acceptance or a rejection.** There is no third.
- **A rejection states its grounds.** An acceptance may.
- **An authority does not decide about themselves.**

### What a caller sees

Nothing changes for a caller using the public entrance: the same requests are admitted and the same
are refused, with the same answers. What changes is that identity, reached any way at all, holds a
request to the business's rules rather than to the rules the request brought.

### What this change does not decide

- **Who may be an authority**, or whether the one named is entitled to decide.
- **What a registration may contain beyond its two required parts.**
- **Anything about the wallet function**, which already holds its own rules.
- **Anything about the other five functions.**

### Left for later changes

- **People already registered or decided about.** The business adds to its record and does not
  rewrite it; a record made under a request's own rules stays as it was made.

---

## 3. Clarifications answered by the business author

These questions were put to the business author and answered by them. The answer in every case was
the simplest one that does not contradict what the business already decided. The design process did
not assume them.

- **Should a registration missing its name or address be refused, or registered and flagged?**
  Refused. The business said both are required.
- **Should identity refuse a request that states rules at all, or ignore the rules it states?**
  Ignore them. The business's rules are identity's; what a request says about them is not part of
  the request, and refusing it would turn a caller's extra words into a failure.
- **Is anything recorded when a decision is refused because the person was already decided about?**
  Nothing. A refusal changes no record, as today.
- **Discovery found two more of identity's rules travelling with the request: that an authority
  does not decide about themselves, and that a rejection states its grounds. Does identity hold
  those too?** Yes, all five. Every business rule of identity's is held by identity.

The other five blockchain functions remain adjacent to this change: named, planned, and outside its
scope.
