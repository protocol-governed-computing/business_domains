# Stage 1 — Change Request: Clarification & Fact Capture: blockchain / identity
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** cr_02_identity
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
|-----------|-------------------------------------------------------------------|---------|--------------|
| identity | EXTEND_SUBDOMAIN | The identity function already exists and works. The change gives its two existing acts a way in from outside, and states what the business offers and what it turns away. No identity behaviour is introduced and no earlier decision is revisited. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Offered Act | An act the business has chosen to make reachable from outside, named by its business name. | CR seed §2 Business Vocabulary #1 |
| Registering an Actor | The offered act by which a person supplies their own details and is admitted unverified. | CR seed §2 Business Vocabulary #2 |
| Recording a Verification Decision | The offered act by which an authority accepts or rejects a registered actor. | CR seed §2 Business Vocabulary #3 |
| Request | What a caller sends: the name of the act they want, and the details that act needs. | CR seed §2 Business Vocabulary #4 |
| Caller | Whoever sends a request, whether a person registering themselves or an authority recording a decision. | CR seed §2 Business Vocabulary #5 |
| Answer | What the business tells a caller in reply to a request. Always one of three kinds. | CR seed §2 Business Vocabulary #6 |
| Turned Away | A request the business declines to begin, either because the act is not offered or because the details cannot be read. | CR seed §2 Business Vocabulary #7 |
| Unreadable Details | Details that are missing, or not in the form the business asked for. The same test the previous change set for registration. | CR seed §2 Business Vocabulary #8 |
| Web Page | The form a caller fills in and the answer they are shown. It holds no business rules. | CR seed §2 Business Vocabulary #9 |
| Carried Detail | Something the person has just typed, held only to save them typing it again on the next page. Not a record, and never read by the business. | CR seed §2 Business Vocabulary #10 |
| Front Page | The page listing the project's six functions, marking those that are not yet available. | CR seed §2 Business Vocabulary #11 |
| Not Yet Available | How the front page shows a function the business has not built. | CR seed §2 Business Vocabulary #12 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| A person can register themselves from a web page and be told what happened. | CR seed §3 Requested Outcomes #1 |
| An authority can record a verification decision from a web page and be told what happened. | CR seed §3 Requested Outcomes #2 |
| The business offers exactly the acts it has chosen to offer, by name, and turns away any other request. | CR seed §3 Requested Outcomes #3 |
| A caller is always told which of three things happened: the act was done, it was turned away and why, or something went wrong inside the business. | CR seed §3 Requested Outcomes #4 |
| The front page shows all six blockchain functions, with wallet, transaction, block and consensus marked as not yet available. | CR seed §3 Requested Outcomes #5 |
| No business rule lives in the web page. | CR seed §3 Requested Outcomes #6 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| The two acts a person and an authority perform are performed by parties outside the business. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| Today the only way to reach either act is an internal tool run by a member of staff. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| Two acts are offered from outside: registering an actor, and recording a verification decision. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| Those two are offered because they are the two acts identity has. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| A request for anything the business has not offered is turned away because the business does not offer it. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| An act is reachable because the business chose to offer it, not because it happens to exist. | HIGH | CR seed §4 Known Facts — Business Truths #6 |
| There is one way in, and the request names the act it wants. | HIGH | CR seed §4 Known Facts — Business Truths #7 |
| The business expects to add many more acts over time and does not want to give callers a new address for each one. | HIGH | CR seed §4 Known Facts — Business Truths #8 |
| An act is named by its business name, which is the business's public word for it. | HIGH | CR seed §4 Known Facts — Business Truths #9 |
| The name of an act should stay the same even if the way the business performs the act changes. | HIGH | CR seed §4 Known Facts — Business Truths #10 |
| A request for an offered act is checked in one way only: whether the business can read what was sent. | HIGH | CR seed §4 Known Facts — Business Truths #11 |
| Details are unreadable when they are missing, or not in the form the business asked for. | HIGH | CR seed §4 Known Facts — Business Truths #12 |
| The readability test is the one the previous change already defined for registration, reused rather than rewritten. | HIGH | CR seed §4 Known Facts — Business Truths #13 |
| Nothing else is judged before the act starts; if the details can be read, the act runs. | HIGH | CR seed §4 Known Facts — Business Truths #14 |
| Whatever the business then decides about the caller is decided where it was always decided. | HIGH | CR seed §4 Known Facts — Business Truths #15 |
| A turned-away request is not recorded as an identity event, because nothing happened to an actor. | HIGH | CR seed §4 Known Facts — Business Truths #16 |
| A caller who is turned away is told which of the two reasons it was, and which details were the problem. | HIGH | CR seed §4 Known Facts — Business Truths #17 |
| Every request gets an answer. | HIGH | CR seed §4 Known Facts — Business Truths #18 |
| An answer is one of three kinds: the act was done, the act was turned away and why, or something went wrong inside the business. | HIGH | CR seed §4 Known Facts — Business Truths #19 |
| A caller never has to guess which of the three happened. | HIGH | CR seed §4 Known Facts — Business Truths #20 |
| The answer appears on the page and that is the end of it; the business sends the person nothing afterwards. | HIGH | CR seed §4 Known Facts — Business Truths #21 |
| Confirming a registration by email made the person wait for the mail to be sent before being told anything, so confirmation was made optional and is now left out altogether. | HIGH | CR seed §4 Known Facts — Business Truths #22 |
| The caller is given nothing to quote back later, because nothing in this change requires them to come back. | HIGH | CR seed §4 Known Facts — Business Truths #23 |
| Being turned away is not the same as the business deciding against the request, and the caller is told which. | HIGH | CR seed §4 Known Facts — Business Truths #24 |
| Being turned away means the business did not start; the business saying no means it started and decided against it. | HIGH | CR seed §4 Known Facts — Business Truths #25 |
| The business promises that it answers, not how fast. | HIGH | CR seed §4 Known Facts — Business Truths #26 |
| The web page collects what the caller types, sends it, and shows the answer. | HIGH | CR seed §4 Known Facts — Business Truths #27 |
| The web page holds no business rules, decides nothing about the details, decides nothing about what happens next, and keeps no copy of what the business holds. | HIGH | CR seed §4 Known Facts — Business Truths #28 |
| The page may carry a detail the person has just typed from one page to the next, so they do not type it twice. | HIGH | CR seed §4 Known Facts — Business Truths #29 |
| Someone who registers and then goes to the decision page should find the address they just entered already filled in. | HIGH | CR seed §4 Known Facts — Business Truths #30 |
| A carried detail is a convenience for whoever fills in the form; it is not a record, the business never reads it, and nothing the business does depends on it being there. | HIGH | CR seed §4 Known Facts — Business Truths #31 |
| A page that lost a carried detail would still work, because the person would simply retype it. | HIGH | CR seed §4 Known Facts — Business Truths #32 |
| The web page does not check details before sending them; the platform checks them and says what is wrong, and the page shows that. | HIGH | CR seed §4 Known Facts — Business Truths #33 |
| A page that checked details itself would be a second opinion the business never approved. | HIGH | CR seed §4 Known Facts — Business Truths #34 |
| A rule must not live in two places, because the two will eventually disagree and nobody will know which is right. | HIGH | CR seed §4 Known Facts — Business Truths #35 |
| The page is a form and an answer, plain and quick to load, not an application. | HIGH | CR seed §4 Known Facts — Business Truths #36 |
| The pages being built are two — registering an actor, and recording a verification decision — plus a front page. | HIGH | CR seed §4 Known Facts — Business Truths #37 |
| The front page lists all six blockchain functions, and marks wallet, transaction, block and consensus as not yet available. | HIGH | CR seed §4 Known Facts — Business Truths #38 |
| The business would rather show a caller what is coming than offer something that fails when they click it. | HIGH | CR seed §4 Known Facts — Business Truths #39 |
| Listing the unbuilt functions promises nothing about whether or when the business will build them. | HIGH | CR seed §4 Known Facts — Business Truths #40 |
| No account or login is needed, because registration is done by someone the business does not know yet. | HIGH | CR seed §4 Known Facts — Business Truths #41 |
| The business does not check that a caller is who they claim to be. | HIGH | CR seed §4 Known Facts — Business Truths #42 |
| The business does not check that an authority recording a decision is allowed to; it records the authority's name, as it already did. | HIGH | CR seed §4 Known Facts — Business Truths #43 |
| Anyone can record a verification decision naming any authority, and the business states this openly. | HIGH | CR seed §4 Known Facts — Business Truths #44 |
| Being reachable from a web page does not weaken the authority claim, but does make it easier to make. | HIGH | CR seed §4 Known Facts — Business Truths #45 |
| The business does not tell a person apart from an authority at the web page; it tells them apart in the acts themselves and in what gets recorded. | HIGH | CR seed §4 Known Facts — Business Truths #46 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| The business author believes the identity function already exists, with both acts working. | If either act is absent or differs from what the author describes, this change is not an extension of a working function and the pages have nothing to reach. | Establish whether the composition governs registering an actor and recording a verification decision, as the previous change defined them. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| The business author believes the platform already offers a way to be reached from outside, and that identity does not have one yet. | If no such way exists, this change must ask for one; if identity already has one, the change is smaller than stated. | Establish whether the composition offers a way for an outside caller to reach a governed act, and whether identity uses it. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| The business author believes the readability test defined by the previous change can be reused as it stands, rather than restated. | Restating it would create a second test for one question, which the author explicitly refuses. | Establish whether the readability check on registration details is declared in a form this change can reuse without redefining it. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| The business author believes the platform can already distinguish a request it declines to begin from an act that ran and decided against the caller. | The two must reach the caller as different answers; if the platform cannot tell them apart, the answer collapses them. | Establish whether the composition distinguishes a request refused before an act from a refusal decided within one. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |
| The business author believes the other five blockchain functions have nothing to offer from outside yet. | The front page marks them not yet available; if any is in fact governed, the page would be wrong. | Establish whether the composition governs any blockchain function other than identity. | CR seed §5 Existing-System Beliefs — Requiring Verification #5 |

---

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis | Source Finding |
|----------|-----|--------------|
| A caller has a web browser and can reach the business over the public network. | The business author asks for a web page and describes no other way in. | CR seed §6 Assumptions #1 |
| The volume of requests will be small enough that not settling how busy the site may get costs the business nothing yet. | The business author explicitly leaves volume, pace and speed of answer unsettled. | CR seed §6 Assumptions #2 |
| Callers acting as authorities will name authorities honestly while no check exists. | The business author accepts an unchecked authority claim for this change and defers the check, which only holds while the claim is usually honest. | CR seed §6 Assumptions #3 |
| A caller turned away will read the reason and correct their details rather than repeat the request unchanged. | The business author requires the reason to be given so the caller can fix it. | CR seed §6 Assumptions #4 |

---

## 7. Constraints

<!-- register:constraints business_language -->
| Constraint | Source | Source Finding |
|----------|------|--------------|
| No business rule may live in the web page. | The business author's statement that the page holds no rules and that a rule must not live in two places. | CR seed §7 Constraints #1 |
| The page may hold only what the person has just typed, and only to save them retyping it. | The business author's statement of what the page may hold on to. | CR seed §7 Constraints #2 |
| The web page must not check details before sending them. | The business author's statement that a page checking details would be a second opinion the business never approved. | CR seed §7 Constraints #3 |
| The page must be plain and quick to load — a form and an answer, not an application. | The business author's statement of what the page is. | CR seed §7 Constraints #4 |
| There is one way in, and the request names the act. | The business author's statement that the business will add many acts and does not want to hand callers a new address for each. | CR seed §7 Constraints #5 |
| The name of an act is the business's public word for it and must outlive changes to how the act is performed. | The business author's statement about what the acts are called. | CR seed §7 Constraints #6 |
| The readability test must be the one the previous change defined, not a second one. | The business author's statement that this change reuses it rather than writing a second. | CR seed §7 Constraints #7 |
| Only acts the business has chosen to offer may be reached. | The business author's statement that an act is reachable because the business chose to offer it. | CR seed §7 Constraints #8 |
| The change introduces no identity behaviour and revisits no decision the previous change made. | The business author's statement of what this change is. | CR seed §7 Constraints #9 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| Only an act the business has chosen to offer can be reached from outside. | CR seed §8 Business Invariants #1 |
| Every request receives an answer. | CR seed §8 Business Invariants #2 |
| Every answer is exactly one of three kinds: the act was done, the act was turned away, or something went wrong inside the business. | CR seed §8 Business Invariants #3 |
| An answer that turns a request away states which of the two reasons it was. | CR seed §8 Business Invariants #4 |
| A request turned away creates no record of an actor. | CR seed §8 Business Invariants #5 |
| A request whose details can be read is passed to the act, and nothing further is judged beforehand. | CR seed §8 Business Invariants #6 |
| No business rule is held by the web page. | CR seed §8 Business Invariants #7 |
| Nothing the business holds is copied into the web page. | CR seed §8 Business Invariants #8 |
| No act of the business depends on a detail the page carried forward. | CR seed §8 Business Invariants #9 |
| Being turned away and being decided against are never reported as the same answer. | CR seed §8 Business Invariants #10 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| NONE IDENTIFIED |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| NONE IDENTIFIED |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| The set of acts offered from outside | The identity function of the blockchain project, for its own acts. | CR seed §11 Authority Boundaries #1 |
| The name of an offered act | The business, as its public word for the act. | CR seed §11 Authority Boundaries #2 |
| The decision to turn a request away | The business, before the act begins. | CR seed §11 Authority Boundaries #3 |
| The web page | The business; it holds no rules and owns no decision. | CR seed §11 Authority Boundaries #4 |
| The front page and what it marks as not yet available | The blockchain project, across all six functions. | CR seed §11 Authority Boundaries #5 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| Checking that a caller is who they claim to be | Named by the business author as not decided by this change. | CR seed §12 Out of Scope #1 |
| Checking that a named authority is allowed to decide | Inseparable from deciding who may be an authority, which the previous change already left for later. | CR seed §12 Out of Scope #2 |
| Any identity behaviour, and any decision the previous change made | This change gives the existing acts a way in and changes nothing about them. | CR seed §12 Out of Scope #3 |
| Telling a person anything after they leave the page, by email or any other means | Making the person wait for it is what caused the trouble last time; it returns as a change of its own. | CR seed §12 Out of Scope #4 |
| Looking up an actor from the web page | A separate need; the business would rather offer nothing than a reading surface whose shape it has not decided. | CR seed §12 Out of Scope #5 |
| Web pages for wallet, transaction, mempool, block, chain and consensus | Each comes with the function it belongs to. | CR seed §12 Out of Scope #6 |
| How many requests the business will accept, and how fast it answers | Named by the business author as not settled here. | CR seed §12 Out of Scope #7 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| Identity | EXTENDED | CR seed §13 Governance Scope #1 |
| Wallet | ADJACENT | CR seed §13 Governance Scope #2 |
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
| A person can register from the web page, and is afterwards an unverified actor. | CR seed §15 Acceptance Criteria #1 |
| An authority can record a decision from the web page, and the actor is afterwards accepted or rejected as decided. | CR seed §15 Acceptance Criteria #2 |
| A registration made from the web page produces the same result as the same registration made from the internal tool. | CR seed §15 Acceptance Criteria #3 |
| A person who registers is told the outcome on the page, and the business sends them nothing afterwards. | CR seed §15 Acceptance Criteria #4 |
| A request naming an act the business does not offer is turned away, and the caller is told the act is not offered. | CR seed §15 Acceptance Criteria #5 |
| A request naming an offered act with a missing contact address is turned away, and the caller is told which detail was the problem. | CR seed §15 Acceptance Criteria #6 |
| A request turned away leaves no actor and no record behind. | CR seed §15 Acceptance Criteria #7 |
| A decision recorded against an actor already decided about is answered as the business deciding against the request, not as being turned away, and the caller can tell the two apart. | CR seed §15 Acceptance Criteria #8 |
| The front page lists all six blockchain functions, and wallet, transaction, block and consensus are marked as not yet available and cannot be used. | CR seed §15 Acceptance Criteria #9 |
| No caller needs an account or a login to use either page. | CR seed §15 Acceptance Criteria #10 |
| Removing every rule from the web page leaves the business's behaviour unchanged. | CR seed §15 Acceptance Criteria #11 |
| A person who registers and then opens the decision page finds the address they just entered already filled in. | CR seed §15 Acceptance Criteria #12 |
| Clearing what the page carried forward changes no outcome; the person retypes the detail and the result is the same. | CR seed §15 Acceptance Criteria #13 |
| Changing a rule in the platform changes what a caller is told without the web page being changed. | CR seed §15 Acceptance Criteria #14 |

---

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|---------------|-------------|---------------------|--------------|
| Offered Act | Its business name. | Their names match; the name is the act, whatever the business does to perform it. | CR seed §16 Identity and Sameness #1 |
| Request | The act it names and the details it carries. | Never — two requests are two requests even when identical, because each is answered separately. | CR seed §16 Identity and Sameness #2 |

---

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|------|----------|--------|------------|-------|--------------|
| NONE IDENTIFIED |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| Any request from outside | The act it names is not one the business offers. | An act is reachable because the business chose to offer it, not because it happens to exist. | CR seed §18 Operation Refusals #1 |
| Any request from outside | The details it carries cannot be read — missing, or not in the form the business asked for. | The business checks readability and nothing else before an act starts. | CR seed §18 Operation Refusals #2 |
| Any request from outside | Never for the business's judgement of the caller or their details. | Anything beyond readability is the act's own decision, made where it was always made. | CR seed §18 Operation Refusals #3 |
| Registering an actor from the web page | The web page judges the details itself. | A page that checked details would be a second opinion the business never approved. | CR seed §18 Operation Refusals #4 |
| Any act the front page marks as not yet available | Always. | The business shows what is coming rather than offering something that fails. | CR seed §18 Operation Refusals #5 |

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|---------------|-----------|-----|--------------|
| Establishing who a caller is | A follow-on governed change for checking callers | The business takes up who may be an authority, with which it belongs. | CR seed §19 Authority Deferrals #1 |
| Establishing that a named authority is allowed to decide | A follow-on governed change for authority over verifiers | The business chooses to take it up; the previous change already deferred it. | CR seed §19 Authority Deferrals #2 |
| Telling a person anything after they leave the page | A follow-on governed change for confirmation | The business wants it back, and can provide it without keeping the person waiting. | CR seed §19 Authority Deferrals #3 |
| Looking up an actor from outside | A follow-on governed change for reading identity | The business decides the shape of a reading surface. | CR seed §19 Authority Deferrals #4 |
| A way in for wallet, transaction, mempool, block, chain and consensus | The change that builds each function | Each function is taken up. | CR seed §19 Authority Deferrals #5 |
| How busy the site may get, and how fast the business answers | A follow-on governed change | The business has reason to settle it. | CR seed §19 Authority Deferrals #6 |

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
