# Stage 1 — Change Request: Clarification & Fact Capture: blockchain / wallet
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** cr_04_wallet
**Status:** DRAFT
**Feeds:** Stage 2 — Domain Model Discovery

Projected from the change seed. Every row is the seed's own, cited to the section it was
said in. S1 interrogates and does not author: a question raised by restating the seed
amends the seed and is projected again, so no row here states business content the seed
does not.

---

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale | Source Finding |
|---------|-------------------------------------------------------------------|---------|--------------|
| wallet | EXTEND_SUBDOMAIN | Wallet was built by a first pass of this change and is in the business's hands. Two things it was asked for are missing: the act does not say it reads the records identity owns, and it gives a wallet to a person nobody accepted. | CR seed §1 CR Type #1 |
| identity | MODIFY | Identity is modified by this change: it declares an announcement of acceptance that it does not make, and wallet is the first function that needs to hear it. One unenforced rule of identity's is corrected at the same time. | CR seed §1 CR Type #2 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Wallet | Where an accepted person holds value. Belongs to exactly one person. | CR seed §2 Business Vocabulary #1 |
| Holder | The accepted person a wallet belongs to. | CR seed §2 Business Vocabulary #2 |
| Balance | What a wallet currently carries. Never negative. | CR seed §2 Business Vocabulary #3 |
| Denomination | The currency a wallet's balance is expressed in. | CR seed §2 Business Vocabulary #4 |
| Classification | What kind of wallet this is — the business distinguishes a default wallet from a private, business, savings, investment, mint, burn or pool wallet. | CR seed §2 Business Vocabulary #5 |
| Address | What others may pay to. Public; the business keeps no secret material behind it. | CR seed §2 Business Vocabulary #6 |
| Acceptance | The moment an authority records that the business accepts a person. | CR seed §2 Business Vocabulary #7 |
| Grounds | The reason an authority states when rejecting a person. | CR seed §2 Business Vocabulary #8 |
| Trail | The business's record of moments that occurred, added to and never rewritten. | CR seed §2 Business Vocabulary #9 |
| Reach | An act reading records another part of the business owns. | CR seed §2 Business Vocabulary #10 |
| Binding | What connects an act, when it runs, to the descriptions of the records it works against. | CR seed §2 Business Vocabulary #11 |
| Consulted | The records an act reads and never writes. | CR seed §2 Business Vocabulary #12 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| Each accepted person has a wallet, created once, when they are accepted. | CR seed §3 Requested Outcomes #1 |
| The moments identity already declares are announced, so that acceptance can be acted on. | CR seed §3 Requested Outcomes #2 |
| A rejection that states no grounds is refused. | CR seed §3 Requested Outcomes #3 |
| The creation of a wallet is recorded as a moment on the business's trail. | CR seed §3 Requested Outcomes #4 |
| The act that creates a wallet declares that it reads the records identity owns, and never writes them. | CR seed §3 Requested Outcomes #5 |
| A wallet is refused to a person the business has not accepted. | CR seed §3 Requested Outcomes #6 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| A wallet belongs to exactly one person. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| A wallet cannot exist for a person the business does not hold. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| A wallet's balance is never negative. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| A wallet is denominated in a currency, with a default the business supplies. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| A wallet carries a classification, drawn from a set the business fixes. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| A wallet is active when created, may become inactive, and may be closed. Closed is the end. | HIGH | CR seed §4 Known Facts — Business Truths #6 |
| A wallet has an address others may pay to, and the business keeps no secret material behind it. | HIGH | CR seed §4 Known Facts — Business Truths #7 |
| Two wallets never share an identity. | HIGH | CR seed §4 Known Facts — Business Truths #8 |
| Asking again for a wallet that already exists changes nothing. | HIGH | CR seed §4 Known Facts — Business Truths #9 |
| A wallet follows acceptance; it is not something a person asks for separately. | HIGH | CR seed §4 Known Facts — Business Truths #10 |
| The business decided a rejection must state why. | HIGH | CR seed §4 Known Facts — Business Truths #11 |
| Nothing after wallet can be built without it — transaction, block and consensus all depend on it. | HIGH | CR seed §4 Known Facts — Business Truths #12 |
| Notifying a person that their wallet was created is dropped from this change. | HIGH | CR seed §4 Known Facts — Business Truths #13 |
| A new wallet holds a balance of zero. | HIGH | CR seed §4 Known Facts — Business Truths #14 |
| A wallet created by this change always carries the default classification. | HIGH | CR seed §4 Known Facts — Business Truths #15 |
| Every wallet is denominated in one currency, the business's own, the same for all. | HIGH | CR seed §4 Known Facts — Business Truths #16 |
| One person holds one wallet. | HIGH | CR seed §4 Known Facts — Business Truths #17 |
| The key material behind a wallet's address is supplied to the business, not generated by it. | HIGH | CR seed §4 Known Facts — Business Truths #18 |
| The business must be able to show that a wallet was created, for whom, when, and with what denomination and classification. Nothing further. | HIGH | CR seed §4 Known Facts — Business Truths #19 |
| Acceptance stands on its own. Failing to give an accepted person a wallet does not un-accept them. | HIGH | CR seed §4 Known Facts — Business Truths #20 |
| A wallet is never created for a person who was rejected, or one still unverified. | HIGH | CR seed §4 Known Facts — Business Truths #21 |
| Whether a person exists and has been accepted is a fact identity owns and alone should state. | HIGH | CR seed §4 Known Facts — Business Truths #22 |
| The wallet keeps no copy of who exists; a second copy of one truth can disagree with the thing it describes. | HIGH | CR seed §4 Known Facts — Business Truths #23 |
| An act may read records another part of the business owns, provided it declares what it consults and never writes them. | HIGH | CR seed §4 Known Facts — Business Truths #24 |
| A reach added to a built artifact by hand works, passes every check, and is a reach no reviewer saw. | HIGH | CR seed §4 Known Facts — Business Truths #25 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| Identity is built and reachable: a person registers and is admitted unverified, and an authority then accepts or rejects them. | Wallet follows acceptance, so acceptance must already be a thing the business does. | Confirm the two identity operations exist and that acceptance is one of the recorded outcomes. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| A person keeps the details they registered with when a decision is recorded about them. | A wallet belongs to a person; if the person's record is thinned by a decision, the wallet's holder is thin too. | Confirm a decision leaves the registered details untouched. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| Identity declares that it announces an acceptance, and does not actually announce it. | Wallet is the first function that needs to hear it. If nothing is announced, nothing downstream can follow acceptance. | Confirm the acceptance moment is declared, and establish whether it is ever announced. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| A rejection stating no grounds is currently accepted and recorded rather than refused. | The identity a wallet depends on should be one whose own stated rules hold. | Confirm whether a rejection with no grounds is refused today. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |
| No wallet exists anywhere in the business today. | Determines whether this creates a function or extends one. | Confirm no wallet record, balance or address is held anywhere. | CR seed §5 Existing-System Beliefs — Requiring Verification #5 |
| A wallet design was worked out in an earlier system, including which of a wallet's details are the business's own and which were implementation detail. | The business need not re-derive decisions it already made. | Establish which of those decisions the current business still holds to. | CR seed §5 Existing-System Beliefs — Requiring Verification #6 |
| The act that creates a wallet reads records identity owns and declares nothing about them. | It is one of the two things missing from what was built. | Establish what the act declares today about the records it reads. | CR seed §5 Existing-System Beliefs — Requiring Verification #7 |
| The business permits an act to declare the bindings it consults, and refuses a write through one. | Says the capability exists and this change uses it rather than inventing it. | Confirm what is admitted, and what happens on a write through a consulted record. | CR seed §5 Existing-System Beliefs — Requiring Verification #8 |
| A person nobody accepted is given a wallet today. | The other missing thing, and the business's own rule going unenforced. | Establish what the act does with the person's state after it reads it. | CR seed §5 Existing-System Beliefs — Requiring Verification #9 |

---

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis | Source Finding |
|----------|-----|--------------|
| The classifications the business named are still the ones it wants. | They were fixed in an earlier design and have not been revisited. | CR seed §6 Assumptions #1 |
| An accepted person expects a wallet without asking for one. | Stated by the author: acceptance was supposed to give them one. | CR seed §6 Assumptions #2 |
| The one currency the business denominates in is the one the earlier design used. | The business stated one currency for all wallets and did not rename it. | CR seed §6 Assumptions #3 |

---

## 7. Constraints

<!-- register:constraints business_language -->
| Constraint | Source | Source Finding |
|----------|------|--------------|
| No one is notified that a wallet was created. The moment is recorded; who is told is a later question. | Business author | CR seed §7 Constraints #1 |
| No value moves. A wallet is created holding what the business says a new wallet holds, and nothing moves it. | Business author | CR seed §7 Constraints #2 |
| The business does not go back for people already accepted. | Business author — the record is added to, never rewritten. | CR seed §7 Constraints #3 |
| The same request must produce the same wallet. The business will not accept a system whose output it can neither reproduce nor check. | Business author | CR seed §7 Constraints #4 |
| Only a default wallet is created. The other classifications remain named and unused until a second one is actually needed. | Business author | CR seed §7 Constraints #5 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| A wallet has exactly one holder. | CR seed §8 Business Invariants #1 |
| A wallet's balance is never negative. | CR seed §8 Business Invariants #2 |
| No two wallets share an identity. | CR seed §8 Business Invariants #3 |
| No wallet exists for a person the business does not hold. | CR seed §8 Business Invariants #4 |
| A person holds at most one wallet. | CR seed §8 Business Invariants #5 |
| No wallet exists for a person who is not accepted. | CR seed §8 Business Invariants #6 |
| A recorded moment is never changed or removed. | CR seed §8 Business Invariants #7 |
| The act that creates a wallet declares every binding it consults. | CR seed §8 Business Invariants #8 |
| Identity is the only writer of what identity owns. | CR seed §8 Business Invariants #9 |
| No wallet exists for a person the business has not accepted. | CR seed §8 Business Invariants #10 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Wallet | Active | In use. The state a wallet is in when created. | CR seed §9 Lifecycle States #1 |
| Wallet | Inactive | Not in use, but not ended. | CR seed §9 Lifecycle States #2 |
| Wallet | Closed | Ended. Nothing follows. | CR seed §9 Lifecycle States #3 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| A wallet was created | When an accepted person is given their wallet | The business can show when a person came to hold value, and for whom. | CR seed §10 Business Events #1 |
| A person was accepted | When an authority records acceptance | Wallet follows from it; it is the moment wallet waits on. | CR seed §10 Business Events #2 |
| A person was registered | When a person supplies their details and is admitted unverified | Declared by identity today and not announced. | CR seed §10 Business Events #3 |
| A person was rejected | When an authority records a rejection | Declared by identity today and not announced. | CR seed §10 Business Events #4 |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| Wallet | Wallet | CR seed §11 Authority Boundaries #1 |
| Balance | Wallet | CR seed §11 Authority Boundaries #2 |
| Address | Wallet | CR seed §11 Authority Boundaries #3 |
| Person, and whether the business accepts them | Identity | CR seed §11 Authority Boundaries #4 |
| Grounds stated for a rejection | Identity | CR seed §11 Authority Boundaries #5 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| Notifying anyone that a wallet was created | Dropped by the business. The moment is recorded; who is told, and how, is a later question. | CR seed §12 Out of Scope #1 |
| Moving value — transactions, transfers, any change of balance | A wallet is created and nothing moves it yet. | CR seed §12 Out of Scope #2 |
| Closing or deactivating a wallet | The lifecycle is declared; only creation is built. | CR seed §12 Out of Scope #3 |
| Who may be an authority, or whether the one named is entitled to decide | Not this change. | CR seed §12 Out of Scope #4 |
| People already accepted, who have no wallet | The business does not go back for them. | CR seed §12 Out of Scope #5 |
| Recovering a wallet whose holder has lost access | A later change. | CR seed §12 Out of Scope #6 |
| Transaction ordering | Carried in an earlier design and deliberately left dormant, having no consumer. | CR seed §12 Out of Scope #7 |
| The other five functions | Not this change. | CR seed §12 Out of Scope #8 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| Wallet | CREATED | CR seed §13 Governance Scope #1 |
| Identity | MODIFIED | CR seed §13 Governance Scope #2 |
| Transaction | ADJACENT | CR seed §13 Governance Scope #3 |
| Mempool | ADJACENT | CR seed §13 Governance Scope #4 |
| Block | ADJACENT | CR seed §13 Governance Scope #5 |
| Chain | ADJACENT | CR seed §13 Governance Scope #6 |
| Consensus | ADJACENT | CR seed §13 Governance Scope #7 |

---

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) | Source Finding |
|--------|----------|------------------|-----------------------------------|--------------|
| NONE IDENTIFIED |

---

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion | Source Finding |
|---------|--------------|
| A person who is accepted holds a wallet afterwards, and the business can show its identity, address, denomination and classification. | CR seed §15 Acceptance Criteria #1 |
| A person who is not accepted holds no wallet. | CR seed §15 Acceptance Criteria #2 |
| A wallet names exactly one holder, and that holder is a person the business holds. | CR seed §15 Acceptance Criteria #3 |
| Accepting the same person again does not produce a second wallet. | CR seed §15 Acceptance Criteria #4 |
| The business can show the moment a wallet was created, for whom, and when. | CR seed §15 Acceptance Criteria #5 |
| A rejection stating no grounds is refused, and no person is rejected by it. | CR seed §15 Acceptance Criteria #6 |
| The moments identity declares are announced when they occur. | CR seed §15 Acceptance Criteria #7 |
| No recorded moment is changed or removed by anything this change introduces. | CR seed §15 Acceptance Criteria #8 |
| The act declares the records it reads, and a reviewer reads that in the design rather than in the built act. | CR seed §15 Acceptance Criteria #9 |
| Identity's records are unchanged by every wallet act, including the refused ones. | CR seed §15 Acceptance Criteria #10 |
| A person the business has not accepted is refused a wallet, and none is recorded for them. | CR seed §15 Acceptance Criteria #11 |

---

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|---------------|-------------|---------------------|--------------|
| Wallet | Its own wallet identity | They carry the same wallet identity. | CR seed §16 Identity and Sameness #1 |
| Holder | The person identity held by Identity | They are the same person to Identity. | CR seed §16 Identity and Sameness #2 |

---

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|------|----------|--------|------------|-------|--------------|
| Wallet | Does not exist | Active | A person being accepted | A moment is recorded on the trail. Nothing else follows. | CR seed §17 Lifecycle Transitions #1 |
| Wallet | Active | Inactive | Out of scope for this change | NONE | CR seed §17 Lifecycle Transitions #2 |
| Wallet | Active or Inactive | Closed | Out of scope for this change | NONE | CR seed §17 Lifecycle Transitions #3 |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| Creating a wallet | The person is not one the business holds | A wallet cannot exist for a person who does not exist. | CR seed §18 Operation Refusals #1 |
| Creating a wallet | The person has not been accepted, or was rejected | A wallet follows acceptance and nothing else. | CR seed §18 Operation Refusals #2 |
| Creating a wallet | The person already holds a wallet | One person holds one wallet; asking again changes nothing. | CR seed §18 Operation Refusals #3 |
| Recording a rejection | No grounds are stated | The business decided a rejection must say why. | CR seed §18 Operation Refusals #4 |

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|---------------|-----------|-----|--------------|
| Transaction ordering | Transaction | Transaction exists and needs it. | CR seed §19 Authority Deferrals #1 |
| Movement of value in and out of a wallet | Transaction | Transaction exists. | CR seed §19 Authority Deferrals #2 |
| Notifying a person that their wallet was created | A later change | The business decides who is told and how. | CR seed §19 Authority Deferrals #3 |
| Recovery of a wallet whose holder has lost access | A later change | The business decides what recovery means. | CR seed §19 Authority Deferrals #4 |

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
