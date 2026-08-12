# Change Seed — blockchain / identity

**Stage:** 0 — Change Seed
**CR:** cr_02_identity
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`, including the clarifications its
author answered. Human input only — nothing here was added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The Identity subdomain governs who an actor is and whether the business trusts them. A person
supplies their own details and is admitted unverified; separately, an authority within the business
records a decision that accepts or rejects them. Both acts are performed by parties outside the
business — the person registering is unknown to the business by definition, and the authority
reviewing them is not required to have been admitted through the same door. Identity therefore has to
be reachable by those parties. Today it is not: the only way to reach either act is an internal tool
run by a member of staff, which means the business registers the person rather than the person
registering themselves, and the authority cannot record their own decision. This change gives each
act a simple web page. It adds no identity behaviour and revisits no decision already made.

## 1. CR Type

<!-- register:cr_type business_language -->
| Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|----------------|-----------|
| EXTEND_SUBDOMAIN | The identity function already exists and works. The change gives its two existing acts a way in from outside, and states what the business offers and what it turns away. No identity behaviour is introduced and no earlier decision is revisited. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Offered Act | An act the business has chosen to make reachable from outside, named by its business name. |
| Registering an Actor | The offered act by which a person supplies their own details and is admitted unverified. |
| Recording a Verification Decision | The offered act by which an authority accepts or rejects a registered actor. |
| Request | What a caller sends: the name of the act they want, and the details that act needs. |
| Caller | Whoever sends a request, whether a person registering themselves or an authority recording a decision. |
| Answer | What the business tells a caller in reply to a request. Always one of three kinds. |
| Turned Away | A request the business declines to begin, either because the act is not offered or because the details cannot be read. |
| Unreadable Details | Details that are missing, or not in the form the business asked for. The same test the previous change set for registration. |
| Web Page | The form a caller fills in and the answer they are shown. It holds no business rules. |
| Carried Detail | Something the person has just typed, held only to save them typing it again on the next page. Not a record, and never read by the business. |
| Front Page | The page listing the project's six functions, marking those that are not yet available. |
| Not Yet Available | How the front page shows a function the business has not built. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| A person can register themselves from a web page and be told what happened. |
| An authority can record a verification decision from a web page and be told what happened. |
| The business offers exactly the acts it has chosen to offer, by name, and turns away any other request. |
| A caller is always told which of three things happened: the act was done, it was turned away and why, or something went wrong inside the business. |
| The front page shows all six blockchain functions, with wallet, transaction, block and consensus marked as not yet available. |
| No business rule lives in the web page. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| The two acts a person and an authority perform are performed by parties outside the business. | HIGH |
| Today the only way to reach either act is an internal tool run by a member of staff. | HIGH |
| Two acts are offered from outside: registering an actor, and recording a verification decision. | HIGH |
| Those two are offered because they are the two acts identity has. | HIGH |
| A request for anything the business has not offered is turned away because the business does not offer it. | HIGH |
| An act is reachable because the business chose to offer it, not because it happens to exist. | HIGH |
| There is one way in, and the request names the act it wants. | HIGH |
| The business expects to add many more acts over time and does not want to give callers a new address for each one. | HIGH |
| An act is named by its business name, which is the business's public word for it. | HIGH |
| The name of an act should stay the same even if the way the business performs the act changes. | HIGH |
| A request for an offered act is checked in one way only: whether the business can read what was sent. | HIGH |
| Details are unreadable when they are missing, or not in the form the business asked for. | HIGH |
| The readability test is the one the previous change already defined for registration, reused rather than rewritten. | HIGH |
| Nothing else is judged before the act starts; if the details can be read, the act runs. | HIGH |
| Whatever the business then decides about the caller is decided where it was always decided. | HIGH |
| A turned-away request is not recorded as an identity event, because nothing happened to an actor. | HIGH |
| A caller who is turned away is told which of the two reasons it was, and which details were the problem. | HIGH |
| Every request gets an answer. | HIGH |
| An answer is one of three kinds: the act was done, the act was turned away and why, or something went wrong inside the business. | HIGH |
| A caller never has to guess which of the three happened. | HIGH |
| The answer appears on the page and that is the end of it; the business sends the person nothing afterwards. | HIGH |
| Confirming a registration by email made the person wait for the mail to be sent before being told anything, so confirmation was made optional and is now left out altogether. | HIGH |
| The caller is given nothing to quote back later, because nothing in this change requires them to come back. | HIGH |
| Being turned away is not the same as the business deciding against the request, and the caller is told which. | HIGH |
| Being turned away means the business did not start; the business saying no means it started and decided against it. | HIGH |
| The business promises that it answers, not how fast. | HIGH |
| The web page collects what the caller types, sends it, and shows the answer. | HIGH |
| The web page holds no business rules, decides nothing about the details, decides nothing about what happens next, and keeps no copy of what the business holds. | HIGH |
| The page may carry a detail the person has just typed from one page to the next, so they do not type it twice. | HIGH |
| Someone who registers and then goes to the decision page should find the address they just entered already filled in. | HIGH |
| A carried detail is a convenience for whoever fills in the form; it is not a record, the business never reads it, and nothing the business does depends on it being there. | HIGH |
| A page that lost a carried detail would still work, because the person would simply retype it. | HIGH |
| The web page does not check details before sending them; the platform checks them and says what is wrong, and the page shows that. | HIGH |
| A page that checked details itself would be a second opinion the business never approved. | HIGH |
| A rule must not live in two places, because the two will eventually disagree and nobody will know which is right. | HIGH |
| The page is a form and an answer, plain and quick to load, not an application. | HIGH |
| The pages being built are two — registering an actor, and recording a verification decision — plus a front page. | HIGH |
| The front page lists all six blockchain functions, and marks wallet, transaction, block and consensus as not yet available. | HIGH |
| The business would rather show a caller what is coming than offer something that fails when they click it. | HIGH |
| Listing the unbuilt functions promises nothing about whether or when the business will build them. | HIGH |
| No account or login is needed, because registration is done by someone the business does not know yet. | HIGH |
| The business does not check that a caller is who they claim to be. | HIGH |
| The business does not check that an authority recording a decision is allowed to; it records the authority's name, as it already did. | HIGH |
| Anyone can record a verification decision naming any authority, and the business states this openly. | HIGH |
| Being reachable from a web page does not weaken the authority claim, but does make it easier to make. | HIGH |
| The business does not tell a person apart from an authority at the web page; it tells them apart in the acts themselves and in what gets recorded. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| The business author believes the identity function already exists, with both acts working. | If either act is absent or differs from what the author describes, this change is not an extension of a working function and the pages have nothing to reach. | Establish whether the composition governs registering an actor and recording a verification decision, as the previous change defined them. |
| The business author believes the platform already offers a way to be reached from outside, and that identity does not have one yet. | If no such way exists, this change must ask for one; if identity already has one, the change is smaller than stated. | Establish whether the composition offers a way for an outside caller to reach a governed act, and whether identity uses it. |
| The business author believes the readability test defined by the previous change can be reused as it stands, rather than restated. | Restating it would create a second test for one question, which the author explicitly refuses. | Establish whether the readability check on registration details is declared in a form this change can reuse without redefining it. |
| The business author believes the platform can already distinguish a request it declines to begin from an act that ran and decided against the caller. | The two must reach the caller as different answers; if the platform cannot tell them apart, the answer collapses them. | Establish whether the composition distinguishes a request refused before an act from a refusal decided within one. |
| The business author believes the other five blockchain functions have nothing to offer from outside yet. | The front page marks them not yet available; if any is in fact governed, the page would be wrong. | Establish whether the composition governs any blockchain function other than identity. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| A caller has a web browser and can reach the business over the public network. | The business author asks for a web page and describes no other way in. |
| The volume of requests will be small enough that not settling how busy the site may get costs the business nothing yet. | The business author explicitly leaves volume, pace and speed of answer unsettled. |
| Callers acting as authorities will name authorities honestly while no check exists. | The business author accepts an unchecked authority claim for this change and defers the check, which only holds while the claim is usually honest. |
| A caller turned away will read the reason and correct their details rather than repeat the request unchanged. | The business author requires the reason to be given so the caller can fix it. |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| No business rule may live in the web page. | The business author's statement that the page holds no rules and that a rule must not live in two places. |
| The page may hold only what the person has just typed, and only to save them retyping it. | The business author's statement of what the page may hold on to. |
| The web page must not check details before sending them. | The business author's statement that a page checking details would be a second opinion the business never approved. |
| The page must be plain and quick to load — a form and an answer, not an application. | The business author's statement of what the page is. |
| There is one way in, and the request names the act. | The business author's statement that the business will add many acts and does not want to hand callers a new address for each. |
| The name of an act is the business's public word for it and must outlive changes to how the act is performed. | The business author's statement about what the acts are called. |
| The readability test must be the one the previous change defined, not a second one. | The business author's statement that this change reuses it rather than writing a second. |
| Only acts the business has chosen to offer may be reached. | The business author's statement that an act is reachable because the business chose to offer it. |
| The change introduces no identity behaviour and revisits no decision the previous change made. | The business author's statement of what this change is. |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| Only an act the business has chosen to offer can be reached from outside. |
| Every request receives an answer. |
| Every answer is exactly one of three kinds: the act was done, the act was turned away, or something went wrong inside the business. |
| An answer that turns a request away states which of the two reasons it was. |
| A request turned away creates no record of an actor. |
| A request whose details can be read is passed to the act, and nothing further is judged beforehand. |
| No business rule is held by the web page. |
| Nothing the business holds is copied into the web page. |
| No act of the business depends on a detail the page carried forward. |
| Being turned away and being decided against are never reported as the same answer. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| NONE IDENTIFIED |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| NONE IDENTIFIED |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| The set of acts offered from outside | The identity function of the blockchain project, for its own acts. |
| The name of an offered act | The business, as its public word for the act. |
| The decision to turn a request away | The business, before the act begins. |
| The web page | The business; it holds no rules and owns no decision. |
| The front page and what it marks as not yet available | The blockchain project, across all six functions. |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| Checking that a caller is who they claim to be | Named by the business author as not decided by this change. |
| Checking that a named authority is allowed to decide | Inseparable from deciding who may be an authority, which the previous change already left for later. |
| Any identity behaviour, and any decision the previous change made | This change gives the existing acts a way in and changes nothing about them. |
| Telling a person anything after they leave the page, by email or any other means | Making the person wait for it is what caused the trouble last time; it returns as a change of its own. |
| Looking up an actor from the web page | A separate need; the business would rather offer nothing than a reading surface whose shape it has not decided. |
| Web pages for wallet, transaction, mempool, block, chain and consensus | Each comes with the function it belongs to. |
| How many requests the business will accept, and how fast it answers | Named by the business author as not settled here. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| Identity | EXTENDED |
| Wallet | ADJACENT |
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
| A person can register from the web page, and is afterwards an unverified actor. |
| An authority can record a decision from the web page, and the actor is afterwards accepted or rejected as decided. |
| A registration made from the web page produces the same result as the same registration made from the internal tool. |
| A person who registers is told the outcome on the page, and the business sends them nothing afterwards. |
| A request naming an act the business does not offer is turned away, and the caller is told the act is not offered. |
| A request naming an offered act with a missing contact address is turned away, and the caller is told which detail was the problem. |
| A request turned away leaves no actor and no record behind. |
| A decision recorded against an actor already decided about is answered as the business deciding against the request, not as being turned away, and the caller can tell the two apart. |
| The front page lists all six blockchain functions, and wallet, transaction, block and consensus are marked as not yet available and cannot be used. |
| No caller needs an account or a login to use either page. |
| Removing every rule from the web page leaves the business's behaviour unchanged. |
| A person who registers and then opens the decision page finds the address they just entered already filled in. |
| Clearing what the page carried forward changes no outcome; the person retypes the detail and the result is the same. |
| Changing a rule in the platform changes what a caller is told without the web page being changed. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| Offered Act | Its business name. | Their names match; the name is the act, whatever the business does to perform it. |
| Request | The act it names and the details it carries. | Never — two requests are two requests even when identical, because each is answered separately. |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| NONE IDENTIFIED |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Any request from outside | The act it names is not one the business offers. | An act is reachable because the business chose to offer it, not because it happens to exist. |
| Any request from outside | The details it carries cannot be read — missing, or not in the form the business asked for. | The business checks readability and nothing else before an act starts. |
| Any request from outside | Never for the business's judgement of the caller or their details. | Anything beyond readability is the act's own decision, made where it was always made. |
| Registering an actor from the web page | The web page judges the details itself. | A page that checked details would be a second opinion the business never approved. |
| Any act the front page marks as not yet available | Always. | The business shows what is coming rather than offering something that fails. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| Establishing who a caller is | A follow-on governed change for checking callers | The business takes up who may be an authority, with which it belongs. |
| Establishing that a named authority is allowed to decide | A follow-on governed change for authority over verifiers | The business chooses to take it up; the previous change already deferred it. |
| Telling a person anything after they leave the page | A follow-on governed change for confirmation | The business wants it back, and can provide it without keeping the person waiting. |
| Looking up an actor from outside | A follow-on governed change for reading identity | The business decides the shape of a reading surface. |
| A way in for wallet, transaction, mempool, block, chain and consensus | The change that builds each function | Each function is taken up. |
| How busy the site may get, and how fast the business answers | A follow-on governed change | The business has reason to settle it. |

---

## gov_projection — Governed Handoff to Stage 1

| Direction | Fields |
|-----------|--------|
| **Consumes** ← human | business problem statement |
| **Emits** → Stage 1 | subdomain_purpose · cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
