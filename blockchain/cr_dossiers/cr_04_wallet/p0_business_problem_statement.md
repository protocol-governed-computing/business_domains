# Business Problem Statement

**Project Name:** blockchain

## 1. Context

The blockchain project covers seven functions: identity, wallet, transaction, mempool, block, chain
and consensus.

Identity is built and reachable. A person registers themselves and is admitted unverified. An
authority then records a decision about them, accepting or rejecting them, and the person keeps the
details they registered with.

Wallet is the next function. It is where an accepted person holds value.

Nothing after identity can be built without it. A transaction moves value between wallets, a block
records transactions, and consensus finalises blocks — so the whole of the rest of the project waits
on this one.

**This statement has been re-authored.** A first pass built the wallet function and it is in the
business's hands today: a person can be accepted, the moments identity declares are announced, a
rejection stating no grounds is refused, and a wallet can be created. Two things that were asked for
in that pass are not in what was built, and both were found by running it rather than by reading it.
The statement below is the wallet change entire — what was asked for the first time, and what is
still missing — because a change that describes only the remainder describes an act nobody can read
whole.

---

## 2. Problem Statement

**A person the business has accepted has nowhere to hold anything, and where the business has begun
to give them one, it does not enforce its own rules about who may have it.**

Acceptance was the end of the story. The business admitted someone, recorded that it accepted them,
and stopped. The person held no balance, had no address anyone could pay, and owned nothing the
business could point to. There was no unit the rest of the project could operate on.

This change gives an accepted person a wallet, and it is not finished until three things are true
together.

**A wallet follows acceptance.** It is not something a person asks for separately. When an authority
accepts someone, that person gets a wallet — the business does not want an accepted person waiting
in a second queue for the thing acceptance was supposed to give them.

That has a consequence the business should see plainly. **Identity says it announces an acceptance
and does not.** The moment is declared and never actually announced, so nothing downstream can act on
it. Wallet is the first function that needs to hear it. Making that announcement real is therefore
part of this change, not a separate tidy-up.

**One rule of identity's is also unenforced and is fixed here.** The business decided a rejection must
say why. Today a rejection stating nothing is accepted and recorded, leaving refusals on the record
with no reason attached. This change refuses them, so that the identity a wallet depends on is one
whose own rules hold.

**The act that creates a wallet reads records identity owns, and must say so.** Whether a person
exists and has been accepted is a fact identity owns and alone should state, so the act establishes
it by reusing identity's own capability rather than keeping a second copy of who exists — a second
copy can disagree with the thing it describes, and the business would then hold two answers about who
may hold a wallet and could defend neither. Reading another part's records is something the business
permits and requires to be declared: the act names what it consults alongside what it owns, reads and
never writes it, and identity's description of its own records stays with identity.

**And an unverified person is currently given a wallet.** The business said plainly that a wallet
follows acceptance and nothing else. The act reads the person's record, takes their address from it,
and never looks at whether they were accepted. No authority ever decided about them and they hold
value anyway. Nothing reported a fault, because nothing checks.

This change shall:

- give each accepted person a wallet, once, when they are accepted;
- announce the moments identity already declares, so that acceptance can be acted on;
- refuse a rejection that states no grounds;
- record the creation of a wallet as a moment on the business's trail;
- have the act declare that it reads the records identity owns, and read them without ever writing
  them;
- refuse a wallet to a person the business has not accepted.

### What the business already decided about a wallet

These are settled and are not reopened by this change:

- **A wallet belongs to exactly one person**, and cannot exist for a person the business does not
  hold.
- **A wallet's balance is never negative.**
- **A wallet is denominated** in a currency, with a default the business supplies.
- **A wallet carries a classification** — the business distinguishes a default wallet from a private,
  business, savings, investment, mint, burn or pool wallet.
- **A wallet is active when created**, may become inactive, and may be closed. Closed is the end.
- **A wallet has an address** others can pay to, and the business keeps no secret material behind it.
- **Two wallets never share an identity.**
- **A person is not given a second wallet by accident** — asking again for one that exists changes
  nothing.

### What a caller sees

An accepted person is told they have a wallet, with its identity, its address, its denomination and
its classification. A rejection stating no grounds is refused rather than accepted — the only change
visible from outside that is not an addition.

### What this change does not decide

- **Notifying anyone.** The legacy design emailed a person when their wallet was created. The
  business is dropping that. The moment is recorded on the trail; who is told, and how, is a separate
  question and a later one.
- **Moving value.** No transaction, no transfer, no change of balance. A wallet is created holding
  what the business says a new wallet holds, and nothing moves it yet.
- **Closing or deactivating a wallet.** The lifecycle is declared; only creation is built.
- **Who may be an authority**, or whether the one named is entitled to decide.
- **Anything about the other five functions.**

### Left for later changes

- **People already accepted.** They have no wallet and this change does not go back for them. The
  business adds to its record and does not rewrite it.
- **Transaction ordering.** The legacy design carried a counter for it and deliberately left it
  dormant, having no consumer. It stays dormant until transaction exists.
- **Recovering a wallet** whose holder has lost access.

---

## 3. Clarifications answered by the business author

These questions were put to the business author and answered by them. The answer in every case was
the simplest one that does not contradict what the business already decided. The design process did
not assume them.

- **What does a new wallet hold when it is created?** Nothing. A new wallet holds a balance of zero.
- **Which classification does a wallet get when nobody chooses one?** The default one. The business
  keeps the full set of classifications it named, but this change only ever creates a default wallet.
- **What currency is a wallet denominated in?** One currency, the business's own, the same for every
  wallet. A person holding wallets in more than one denomination is not something the business does.
- **May a person hold more than one wallet?** No. One person, one wallet. The earlier design allowed
  one per classification; the business is not doing that yet, and will decide it when a second
  classification is actually needed.
- **Is the key material behind a wallet's address generated by the business, or supplied to it?**
  Supplied. The business does not want a system that produces a different wallet every time the same
  request is made, because it could then neither reproduce nor check what it did.
- **What must the business be able to prove about a wallet later?** That it was created, for whom,
  when, and with what denomination and classification. Nothing further.
- **When a person is accepted and their wallet cannot be created, what has happened?** They are
  accepted, and they have no wallet. Acceptance is a decision about a person and it stands on its
  own; failing to give them a wallet does not un-accept them.
- **Does the business announce a wallet's creation to anything beyond its own record?** No. The
  moment goes on the trail and nowhere else.
- **Is a wallet ever created for a person who was rejected, or one still unverified?** No. A wallet
  follows acceptance and nothing else.

The other five blockchain functions remain adjacent to this change: named, planned, and outside its
scope.
