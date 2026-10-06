# Business Problem Statement

**Project Name:** blockchain

## 1. Context

The blockchain project covers seven functions: identity, wallet, transaction, mempool, block, chain
and consensus. Identity and wallet are built and reachable.

A person registers and is held unverified. An authority accepts or rejects them, and an accepted
person is given a wallet. Every one of these acts reads or writes a record the business keeps: the
person's record, the address they claimed, the trail of moments in their history, and their wallet.

Reading or writing a record can fail. The store may be unreachable, or it may answer with an error.
The business has never said what an act does when that happens.

---

## 2. Problem Statement

**When a record cannot be read or written, identity and wallet do not say what happens next, and in
one case the act carries on as if nothing went wrong.**

Most acts end without an answer when a record fails. The act stops, and nothing the business decided
says how it ended. The caller cannot tell a refusal the business intended from a failure nobody
planned for.

**And one failure is ignored.** When an authority accepts a person, identity first looks the person
up. If that lookup fails, identity does not stop. It goes on to read the person's record and records
the acceptance. A person was accepted whose lookup had failed. The same gap sits in three of wallet's
steps: claiming a wallet's identity, writing the wallet's record, and recording the wallet's moment.

This change shall:

- end every identity and wallet act as rejected when a record it needs cannot be read or written;
- stop every act at the step whose record failed, so nothing after it runs;
- leave everything else identity and wallet do unchanged;
- state each act whose meaning this changes under a new identity, and leave the identity v5 published
  as it was published.

### What the business already decided

These are settled and are not reopened by this change:

- **An act either succeeds or is rejected.** Identity and wallet have no third ending.
- **A rejection changes no record.** Where an act already recorded something before the failure, that
  record stays as it was. The business adds to its record and does not rewrite it.
- **Identity is fixed at publication.** Identity and wallet were published in v5. An act that comes
  to mean something else is a new identity; the published one stays in the record, stood down, and
  whatever names it names its successor.

---

## 3. Clarifications answered by the business author

- **Should a failed record end as rejected, or as a separate failure?** As rejected. The business
  keeps two endings. Telling a refusal apart from a failure is a later decision, not this change.
- **Should identity or wallet try again?** No. A failed record ends the act. Nothing retries.
- **Does a caller see a different act?** No. The entrances and intents that start an act keep their
  identities and start its successor.
