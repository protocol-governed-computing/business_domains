# Business Problem Statement

**Project Name:** blockchain

## 1. Context

The blockchain project covers seven functions: identity, wallet, transaction, mempool, block, chain
and consensus.

The previous change built the **identity** function. It lets a person register and be admitted as
unverified. It lets an authority record a decision that accepts or rejects that person. Both work
today, but only from inside the business's own tools. A person outside the business cannot reach
either one.

This change gives them a way in: a simple web page.

---

## 2. Problem Statement

The business needs people to register themselves. Right now they cannot. The only way to register
someone is for a member of staff to run an internal tool, which means the business is registering
the person rather than the person registering themselves. That is not what identity was built for.
The same is true of the verification decision: the authority who reviews a person cannot record
their own decision.

This change provides a simple web page for each of those two acts:

- **Register.** A person fills in their details and is registered. They are told what happened.
- **Record a decision.** An authority fills in their decision about a registered person. They are
  told what happened.

### The web page stays thin

The web page collects what the person types, sends it to the platform, and shows the answer. That is
all it does.

The page holds no business rules. It does not decide whether details are acceptable. It does not
decide what happens next. It keeps no copy of what the business holds. Every rule stays in the
platform where it already lives, so a change to a rule never means changing the web page, and no rule
can be worked around by reaching the platform another way.

The page may carry a detail the person has already typed from one page to the next, so they do not
type it twice. Someone who registers and then goes to the decision page should find the address they
just entered already filled in. That is a convenience for whoever is filling in the form. It is not a
record, the business never reads it, and nothing the business does depends on it being there.

The business wants the page to be plain and quick to load. It is a form and an answer, not an
application.

### What the business offers, and what it turns away

The business offers two acts by name: registering an actor, and recording a verification decision. A
request for anything else is turned away because the business does not offer it.

A request for an act the business does offer is checked in one way only: can the business read what
was sent? Details are unreadable if they are missing, or if they are not in the form the business
asked for. That is the same check the previous change already defined for registration, and this
change reuses it rather than writing a second one.

Nothing else is judged at this point. If the details can be read, the act runs, and whatever the
business then decides is decided where it was always decided.

### What the caller is told

Every request gets an answer. The answer is one of three things:

1. The act was done, and here is what was recorded.
2. The act was turned away, and here is why.
3. Something went wrong inside the business.

The person should never have to guess which of the three happened.

The answer appears on the page, and that is the end of it. The business does not send the person
anything afterwards. Earlier attempts at confirming a registration by email made the person wait for
mail to be sent before they were told anything, so confirmation was made optional and is now left out
altogether.

### The functions that are not built yet

The web site will also show wallet, transaction, block and consensus. Each of these is shown by name
and marked as not yet available. The business would rather show a person what is coming than offer
something that fails when they click it.

### What this change does not decide

- **Who the caller is.** The business does not check that a caller is who they claim to be. It does
  not check that an authority recording a decision is allowed to. It records the authority's name,
  which is what it already did.
- **The other functions.** Wallet, transaction, block and consensus are named on the site and nothing
  more.
- **How busy the site may get.** How many requests the business will accept, and how fast it answers,
  are not settled here.

### Left for later changes

- **Checking who a caller is, and what they are allowed to do.** This depends on deciding who is
  allowed to be an authority, which the previous change already left for later. The two belong
  together.
- **Telling a person anything after they leave the page.** Confirming a registration by email, or by
  any other means, is a separate need. It is left out here because making the person wait for it is
  what caused the trouble last time.
- **Looking up an actor from the web page.** This change lets a person register and an authority
  decide. Asking the business what it already knows about an actor is a separate need.
- **Web pages for the other six functions.** Each one comes with the function it belongs to.

---

## 3. Clarifications answered by the business author

These questions were put to the business author and answered by them. The design process did not
assume them.

### The web pages

- **Which pages are being built?** Two: register an actor, and record a verification decision. Plus a
  front page listing all six functions, where the other four are marked as not yet available.
- **Why only two?** Because identity is the only function that exists. The others have nothing to
  offer yet.
- **How much should the page do on its own?** As little as possible. It collects what the person
  types and shows what the platform says back. The business does not want a rule living in two
  places, because the two will eventually disagree and nobody will know which one is right.
- **Should the page check the details before sending them?** No. The platform checks them and says
  what is wrong, and the page shows that. A page that checked details itself would be a second
  opinion the business never approved.
- **May the page hold on to anything at all?** Only what the person has just typed, and only to save
  them typing it again on the next page. Nothing the business holds is copied there, the business
  never reads it back, and a page that lost it would still work — the person would simply retype.
- **Does the page need an account or a login?** No. Registration is done by someone the business does
  not know yet, so requiring them to be known first makes no sense.

### What the business offers

- **Which acts can be reached from the web page?** Registering an actor, and recording a verification
  decision. Those two, because those are the two identity has.
- **Can a caller reach anything the business has not listed?** No. An act can be reached because the
  business chose to offer it, not because it happens to exist.
- **Is there one way in, or a separate one for each act?** One way in, and the request says which act
  it wants. The business expects to add many more acts over time, and it does not want to hand
  callers a new address every time it adds one.
- **What are the acts called?** By their business names: registering an actor, and recording a
  verification decision. That name is the business's public word for the act. It should stay the same
  even if the way the business performs the act changes.

### Turning a request away

- **What does the business turn away before the act starts?** An act it does not offer, and an act it
  does offer where the details cannot be read. Nothing else.
- **What counts as details that cannot be read?** Missing, or not in the form the business asked for.
  This is exactly the test the previous change already set.
- **Is a turned-away request recorded as an identity event?** No. Nothing happened to an actor. The
  business does not want its record of who registered to fill up with people who did not.
- **Is the caller told why they were turned away?** Yes, and which of the two it was, including which
  details were the problem. Telling someone only "no" gives them no way to fix it.

### The answer

- **What can the caller be told?** That the act was done, that it was turned away and why, or that
  something went wrong inside the business.
- **Does the business tell the person anything after they close the page?** No. The answer on the
  page is the whole of it.
- **Not even a confirmation email?** No. That was tried, and making the person wait for the mail to
  go out before telling them anything was the problem. It was made optional and is now left out. When
  the business wants it back it will be a change of its own, and the person will not be kept waiting
  for it.
- **Does the caller get anything they can quote back later?** Not in this change. Nothing in it
  requires them to come back, because there is nothing yet to come back to — asking the business what
  it knows about an actor is itself left for later.
- **Is being turned away at the door the same as the business saying no?** No, and the caller is told
  which. Being turned away means the business did not start. The business saying no means it started
  and decided against it. Someone told to fix their details when the business has actually decided
  about them would be misled.
- **Does the business promise how fast it answers?** No. It promises that it answers.

### The functions that are not built yet

- **How does the site show a function that does not exist?** By name, marked as not yet available.
- **Does listing them promise the business will build them?** No. The list is the project's stated
  scope, which was already public. It says nothing about when.

### Who can use the pages

- **Does a caller have to prove who they are?** Not in this change.
- **So anyone can record a verification decision and name any authority?** Yes, and the business
  states this openly rather than leaving it to be found out. The record shows which authority was
  named, exactly as it did before. Being reachable from a web page does not make that claim any
  weaker, but it does make it easier to make. Checking that a named authority is allowed to decide is
  left for later, together with deciding who can be an authority at all.
- **Does the business tell a person apart from an authority at the web page?** No. It tells them
  apart where it always did: in the acts themselves and in what gets recorded.

The other six blockchain functions remain adjacent to this change: named, planned, and outside its
scope. The identity needs the previous change left for later — re-application, revocation, authority
over verifiers, identity evidence, and correcting an actor's details — are still left for later and
are untouched here.
