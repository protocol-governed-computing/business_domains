# Business Problem Statement

**Project Name:** blockchain

## 1. Context

The blockchain project covers seven functions: identity, wallet, transaction, mempool, block, chain
and consensus. Identity and wallet are built and reachable.

A person registers and is held unverified. An authority accepts or rejects them, and an accepted
person is given a wallet. Each act records a moment on a trail: that the person registered, was
accepted, was rejected, or was given a wallet. Registration claims the person's contact address, so
that one person is one actor. Creating a wallet writes the wallet's record and gives it an identity.

---

## 2. Problem Statement

**Identity and wallet take values from the request that only the business may decide.**

Each act records its own moment, but the request names it. A register request says which moment
happened and which trail it goes on. So does an acceptance and a rejection. A direct caller can name
a moment other than the one that happened, or a trail other than the person's.

**Registration takes from the request where the contact address sits and what kind of value it is.**
A caller can point the claim at another field of the person's record.

**Wallet's record is whatever the request supplies.** The request states the wallet's holder, its
balance, its denomination, its classification and its state. A caller can create a wallet for a
holder other than the accepted person, with any balance. The request also chooses the prefix of the
wallet's identity, and the moment the wallet's trail records.

The entrances send these values on every request, so callers through an entrance see nothing wrong.
The acts themselves do not declare them as anything a caller may send. The business's own check of its
entry points reports the gap ten times.

This change shall:

- have every identity and wallet act state the moment it records and the trail it records it on;
- have registration state where the contact address sits and what kind of value it is;
- have wallet state the record it creates: the accepted person as holder, a balance of zero, the
  business's denomination and classification, and an active state;
- have wallet state the prefix of a wallet's identity;
- stop the entrances sending any of these values;
- leave everything else identity and wallet do unchanged;
- state each act, entrance and entry point whose meaning this changes under a new identity.

### What the business already decided

These are settled and are not reopened by this change:

- **An act either succeeds or is rejected.** Identity and wallet have no third ending.
- **The business adds to its record and does not rewrite it.** Records made before this change stay
  as they were made.
- **Identity is fixed at publication.** An act that comes to mean something else is a new identity.
  The predecessor is retired by record, and whatever names it names its successor.
- **An acceptance may state its grounds or not.** A rejection must state them.

---

## 3. Clarifications answered by the business author

- **Which values of a new wallet does wallet state?** All five. The holder is the accepted person
  identity holds. The balance is zero, the denomination BACHI, the classification DEFAULT and the
  state ACTIVE. A caller sends none of them.
- **Does wallet state the prefix of a wallet's identity?** Yes. The entry point stops declaring it.
- **Do the entrances become new identities?** Yes. Each entrance stops sending the values its act now
  states, and callers send the same inputs as before.
- **Is the acceptance an entrance cannot answer without grounds part of this change?** No. It waits on
  the transport standard letting an entrance's answer leave a field out.
