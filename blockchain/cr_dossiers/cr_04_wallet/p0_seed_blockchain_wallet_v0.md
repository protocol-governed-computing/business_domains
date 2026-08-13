# Change Seed — blockchain / wallet

**Stage:** 0 — Change Seed
**CR:** cr_04_wallet
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`. Human input only — nothing here was
added, decided or designed by the pipeline. The clarifications its author has not yet answered are
carried forward as questions in §14, unanswered.

---

## 0. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The Wallet subdomain governs where a person the business has accepted holds value. It holds one
record for each wallet, the balance that wallet carries, the address others may pay to, and the
state that says whether the wallet is in use. A wallet belongs to exactly one accepted person and
follows from their acceptance rather than from a separate request. Wallet is the unit the rest of
the project operates on: a transaction moves value between wallets, a block records transactions,
and consensus finalises blocks. It does not govern whether a person is accepted, who may decide
that, or how value moves once a wallet holds it.

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|-----------|----------------|-----------|
| wallet | EXTEND_SUBDOMAIN | Wallet was built by a first pass of this change and is in the business's hands. Two things it was asked for are missing: the act does not say it reads the records identity owns, and it gives a wallet to a person nobody accepted. |
| identity | MODIFY | Identity is modified by this change: it declares an announcement of acceptance that it does not make, and wallet is the first function that needs to hear it. One unenforced rule of identity's is corrected at the same time. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Wallet | Where an accepted person holds value. Belongs to exactly one person. |
| Holder | The accepted person a wallet belongs to. |
| Balance | What a wallet currently carries. Never negative. |
| Denomination | The currency a wallet's balance is expressed in. |
| Classification | What kind of wallet this is — the business distinguishes a default wallet from a private, business, savings, investment, mint, burn or pool wallet. |
| Address | What others may pay to. Public; the business keeps no secret material behind it. |
| Acceptance | The moment an authority records that the business accepts a person. |
| Grounds | The reason an authority states when rejecting a person. |
| Trail | The business's record of moments that occurred, added to and never rewritten. |
| Reach | An act reading records another part of the business owns. |
| Binding | What connects an act, when it runs, to the descriptions of the records it works against. |
| Consulted | The records an act reads and never writes. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| Each accepted person has a wallet, created once, when they are accepted. |
| The moments identity already declares are announced, so that acceptance can be acted on. |
| A rejection that states no grounds is refused. |
| The creation of a wallet is recorded as a moment on the business's trail. |
| The act that creates a wallet declares that it reads the records identity owns, and never writes them. |
| A wallet is refused to a person the business has not accepted. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| A wallet belongs to exactly one person. | HIGH |
| A wallet cannot exist for a person the business does not hold. | HIGH |
| A wallet's balance is never negative. | HIGH |
| A wallet is denominated in a currency, with a default the business supplies. | HIGH |
| A wallet carries a classification, drawn from a set the business fixes. | HIGH |
| A wallet is active when created, may become inactive, and may be closed. Closed is the end. | HIGH |
| A wallet has an address others may pay to, and the business keeps no secret material behind it. | HIGH |
| Two wallets never share an identity. | HIGH |
| Asking again for a wallet that already exists changes nothing. | HIGH |
| A wallet follows acceptance; it is not something a person asks for separately. | HIGH |
| The business decided a rejection must state why. | HIGH |
| Nothing after wallet can be built without it — transaction, block and consensus all depend on it. | HIGH |
| Notifying a person that their wallet was created is dropped from this change. | HIGH |
| A new wallet holds a balance of zero. | HIGH |
| A wallet created by this change always carries the default classification. | HIGH |
| Every wallet is denominated in one currency, the business's own, the same for all. | HIGH |
| One person holds one wallet. | HIGH |
| The key material behind a wallet's address is supplied to the business, not generated by it. | HIGH |
| The business must be able to show that a wallet was created, for whom, when, and with what denomination and classification. Nothing further. | HIGH |
| Acceptance stands on its own. Failing to give an accepted person a wallet does not un-accept them. | HIGH |
| A wallet is never created for a person who was rejected, or one still unverified. | HIGH |
| Whether a person exists and has been accepted is a fact identity owns and alone should state. | HIGH |
| The wallet keeps no copy of who exists; a second copy of one truth can disagree with the thing it describes. | HIGH |
| An act may read records another part of the business owns, provided it declares what it consults and never writes them. | HIGH |
| A reach added to a built artifact by hand works, passes every check, and is a reach no reviewer saw. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| Identity is built and reachable: a person registers and is admitted unverified, and an authority then accepts or rejects them. | Wallet follows acceptance, so acceptance must already be a thing the business does. | Confirm the two identity operations exist and that acceptance is one of the recorded outcomes. |
| A person keeps the details they registered with when a decision is recorded about them. | A wallet belongs to a person; if the person's record is thinned by a decision, the wallet's holder is thin too. | Confirm a decision leaves the registered details untouched. |
| Identity declares that it announces an acceptance, and does not actually announce it. | Wallet is the first function that needs to hear it. If nothing is announced, nothing downstream can follow acceptance. | Confirm the acceptance moment is declared, and establish whether it is ever announced. |
| A rejection stating no grounds is currently accepted and recorded rather than refused. | The identity a wallet depends on should be one whose own stated rules hold. | Confirm whether a rejection with no grounds is refused today. |
| No wallet exists anywhere in the business today. | Determines whether this creates a function or extends one. | Confirm no wallet record, balance or address is held anywhere. |
| A wallet design was worked out in an earlier system, including which of a wallet's details are the business's own and which were implementation detail. | The business need not re-derive decisions it already made. | Establish which of those decisions the current business still holds to. |
| The act that creates a wallet reads records identity owns and declares nothing about them. | It is one of the two things missing from what was built. | Establish what the act declares today about the records it reads. |
| The business permits an act to declare the bindings it consults, and refuses a write through one. | Says the capability exists and this change uses it rather than inventing it. | Confirm what is admitted, and what happens on a write through a consulted record. |
| A person nobody accepted is given a wallet today. | The other missing thing, and the business's own rule going unenforced. | Establish what the act does with the person's state after it reads it. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| The classifications the business named are still the ones it wants. | They were fixed in an earlier design and have not been revisited. |
| An accepted person expects a wallet without asking for one. | Stated by the author: acceptance was supposed to give them one. |
| The one currency the business denominates in is the one the earlier design used. | The business stated one currency for all wallets and did not rename it. |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| No one is notified that a wallet was created. The moment is recorded; who is told is a later question. | Business author |
| No value moves. A wallet is created holding what the business says a new wallet holds, and nothing moves it. | Business author |
| The business does not go back for people already accepted. | Business author — the record is added to, never rewritten. |
| The same request must produce the same wallet. The business will not accept a system whose output it can neither reproduce nor check. | Business author |
| Only a default wallet is created. The other classifications remain named and unused until a second one is actually needed. | Business author |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| A wallet has exactly one holder. |
| A wallet's balance is never negative. |
| No two wallets share an identity. |
| No wallet exists for a person the business does not hold. |
| A person holds at most one wallet. |
| No wallet exists for a person who is not accepted. |
| A recorded moment is never changed or removed. |
| The act that creates a wallet declares every binding it consults. |
| Identity is the only writer of what identity owns. |
| No wallet exists for a person the business has not accepted. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Wallet | Active | In use. The state a wallet is in when created. |
| Wallet | Inactive | Not in use, but not ended. |
| Wallet | Closed | Ended. Nothing follows. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| A wallet was created | When an accepted person is given their wallet | The business can show when a person came to hold value, and for whom. |
| A person was accepted | When an authority records acceptance | Wallet follows from it; it is the moment wallet waits on. |
| A person was registered | When a person supplies their details and is admitted unverified | Declared by identity today and not announced. |
| A person was rejected | When an authority records a rejection | Declared by identity today and not announced. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| Wallet | Wallet |
| Balance | Wallet |
| Address | Wallet |
| Person, and whether the business accepts them | Identity |
| Grounds stated for a rejection | Identity |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| Notifying anyone that a wallet was created | Dropped by the business. The moment is recorded; who is told, and how, is a later question. |
| Moving value — transactions, transfers, any change of balance | A wallet is created and nothing moves it yet. |
| Closing or deactivating a wallet | The lifecycle is declared; only creation is built. |
| Who may be an authority, or whether the one named is entitled to decide | Not this change. |
| People already accepted, who have no wallet | The business does not go back for them. |
| Recovering a wallet whose holder has lost access | A later change. |
| Transaction ordering | Carried in an earlier design and deliberately left dormant, having no consumer. |
| The other five functions | Not this change. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| Wallet | CREATED |
| Identity | MODIFIED |
| Transaction | ADJACENT |
| Mempool | ADJACENT |
| Block | ADJACENT |
| Chain | ADJACENT |
| Consensus | ADJACENT |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|
| NONE IDENTIFIED |

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| A person who is accepted holds a wallet afterwards, and the business can show its identity, address, denomination and classification. |
| A person who is not accepted holds no wallet. |
| A wallet names exactly one holder, and that holder is a person the business holds. |
| Accepting the same person again does not produce a second wallet. |
| The business can show the moment a wallet was created, for whom, and when. |
| A rejection stating no grounds is refused, and no person is rejected by it. |
| The moments identity declares are announced when they occur. |
| No recorded moment is changed or removed by anything this change introduces. |
| The act declares the records it reads, and a reviewer reads that in the design rather than in the built act. |
| Identity's records are unchanged by every wallet act, including the refused ones. |
| A person the business has not accepted is refused a wallet, and none is recorded for them. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| Wallet | Its own wallet identity | They carry the same wallet identity. |
| Holder | The person identity held by Identity | They are the same person to Identity. |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Wallet | Does not exist | Active | A person being accepted | A moment is recorded on the trail. Nothing else follows. |
| Wallet | Active | Inactive | Out of scope for this change | NONE |
| Wallet | Active or Inactive | Closed | Out of scope for this change | NONE |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Creating a wallet | The person is not one the business holds | A wallet cannot exist for a person who does not exist. |
| Creating a wallet | The person has not been accepted, or was rejected | A wallet follows acceptance and nothing else. |
| Creating a wallet | The person already holds a wallet | One person holds one wallet; asking again changes nothing. |
| Recording a rejection | No grounds are stated | The business decided a rejection must say why. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| Transaction ordering | Transaction | Transaction exists and needs it. |
| Movement of value in and out of a wallet | Transaction | Transaction exists. |
| Notifying a person that their wallet was created | A later change | The business decides who is told and how. |
| Recovery of a wallet whose holder has lost access | A later change | The business decides what recovery means. |