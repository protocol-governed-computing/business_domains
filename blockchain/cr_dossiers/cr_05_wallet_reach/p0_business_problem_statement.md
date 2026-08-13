# Business Problem Statement

**Project Name:** blockchain — wallet

> **This dossier is at P0 and its phase run has not begun.** It records a confirmed requirement and
> the change it needs. It is not a design.

## 1. Context

A wallet belongs to a person. Before the business creates one it must establish that the person
exists and has been accepted — a fact the identity part of this domain owns and alone should state.
The wallet keeps no copy of who exists: a second copy of one truth can disagree with the thing it
describes, and then the business holds two answers about who may hold a wallet and can defend
neither.

So the act that creates a wallet reuses identity's capability for resolving a person, rather than
restating what a person is. That is the arrangement the composition encourages, and it is the one
this change completes.

---

## 2. Problem Statement

**The act that creates a wallet reads records identity owns, and does not say so.**

The act reuses identity's contract for establishing that a person exists and has been accepted. That
contract reads the records identity holds. The act names where its own records live and says nothing
about identity's, so when it runs it asks for a record it never declared it would read:

```
PROTOCOL VIOLATION: Entity 'ACTORS' not found in STRUCTURE entity_stores.
Available entities: ['WALLETS', 'WALLET_IDENTITIES', 'WALLET_OCCURRENCES']
```

Every phase of design passed. Every fact construction requires was determined. It compiles, verifies
and attests, and stops on its second step.

**What changed, and why this is now a small change.** The platform did not admit an act reading
another subdomain's records at all; that is why this stopped rather than being declared. It admits
one now: an act states the bindings it consults alongside the one it owns, the composition resolves
both, and a write to anything it merely consults is refused when it runs. The capability exists and
is proven; what remains is for this domain to use it.

This change shall:

- have the wallet act declare that it reads the records identity owns;
- keep the wallet the only writer of what the wallet owns, and identity the only writer of what
  identity owns;
- leave identity's description of its own records exactly where it is, maintained by identity.

### What this change does not decide

- **How an act reaches another subdomain's records.** The platform decided that; this domain uses it.
- **Which records identity owns.** Identity's business, settled, and untouched here.
- **Whether other wallet acts need the same reach.** One act needs it today. Another that needs it
  says so in its own change.

---

## 3. What this change amends

Two artifacts, both owned by this domain, both families the design language authors and construction
renders:

| Artifact | What changes |
|---|---|
| `blockchain::WF_CREATE_WALLET_V0` | Declares the binding it consults alongside the one it owns. |
| `blockchain::RB_WALLET_BINDINGS_V0` | Unchanged in what it describes; it keeps naming the wallet's storage and only the wallet's. |

**Nothing in identity changes.** The reach is declared by the act that reaches, in an artifact this
subdomain owns — which is what the platform's model requires, and what keeps identity's description
maintained by the people answerable for identity's records.

---

## 3a. What this change is waiting on

**The design language cannot yet state a reach.** P7 declares where an act's records live and has no
register for the bindings an act consults; P8 schedules what construction renders, and construction
renders what P7 states. So this change can be designed as far as P6 and cannot be *expressed* at P7
— the same shape the platform half met, one layer up.

**This dossier is not to be hand-delivered.** Adding the declaration to the workflow artifact
directly would work, would pass every check, and would be an ungoverned change to a domain artifact
— which is what was reverted to raise this change request in the first place. The whole point of the
platform capability is that a reach is *declared where a reviewer reads it*, and a reach delivered
by hand is a reach no reviewer saw.

It waits on a focused change to the lifecycle language: a P7 declaration for a workflow's consulted
bindings, and the rendering surface at P8 that emits them.

---

## 4. Clarifications — answered

### Answered

- **Should the wallet keep its own copy of who exists, instead?**
  **No.** A second copy of one truth can disagree with the thing it describes, and the business would
  then hold two answers about who may hold a wallet. This is the option the platform change was made
  to remove, and taking it here would waste the change.

- **Should the wallet act write anything identity owns — an occurrence, say, recording that a wallet
  was created for a person?**
  **No.** Identity owns what identity holds, and a second writer means two subdomains decide what is
  true about a person and neither is answerable. The wallet records its own occurrence in its own
  store, which it already does.

- **Do the other wallet acts need this?**
  **Not today.** One act establishes that a person exists; the rest work on wallets the business
  already holds. An act that later needs the reach declares it in the change that needs it.
