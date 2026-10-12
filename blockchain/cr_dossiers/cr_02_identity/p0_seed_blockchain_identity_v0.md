# Change Seed — blockchain / identity

## Machine

```yaml
document:
  phase: p0
  domain: blockchain
  subdomain: identity
  cr: cr_02_identity
  rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0
registers:
  subdomain_purpose: |2

    The Identity subdomain governs who an actor is and whether the business trusts them. A person
    supplies their own details and is admitted unverified; separately, an authority within the business
    records a decision that accepts or rejects them. Both acts are performed by parties outside the
    business — the person registering is unknown to the business by definition, and the authority
    reviewing them is not required to have been admitted through the same door. Identity therefore has to
    be reachable by those parties. Today it is not: the only way to reach either act is an internal tool
    run by a member of staff, which means the business registers the person rather than the person
    registering themselves, and the authority cannot record their own decision. This change gives each
    act a simple web page. It adds no identity behaviour and revisits no decision already made.
  cr_type:
  - classification: EXTEND_SUBDOMAIN
    rationale: The identity function already exists and works. The change gives its two existing acts a way in from outside, and states what the business offers and what it turns away. No identity behaviour is introduced and no earlier decision is revisited.
  business_vocabulary:
  - term: Offered Act
    definition: An act the business has chosen to make reachable from outside, named by its business name.
  - term: Registering an Actor
    definition: The offered act by which a person supplies their own details and is admitted unverified.
  - term: Recording a Verification Decision
    definition: The offered act by which an authority accepts or rejects a registered actor.
  - term: Request
    definition: 'What a caller sends: the name of the act they want, and the details that act needs.'
  - term: Caller
    definition: Whoever sends a request, whether a person registering themselves or an authority recording a decision.
  - term: Answer
    definition: What the business tells a caller in reply to a request. Always one of three kinds.
  - term: Turned Away
    definition: A request the business declines to begin, either because the act is not offered or because the details cannot be read.
  - term: Unreadable Details
    definition: Details that are missing, or not in the form the business asked for. The same test the previous change set for registration.
  - term: Web Page
    definition: The form a caller fills in and the answer they are shown. It holds no business rules.
  - term: Carried Detail
    definition: Something the person has just typed, held only to save them typing it again on the next page. Not a record, and never read by the business.
  - term: Front Page
    definition: The page listing the project's six functions, marking those that are not yet available.
  - term: Not Yet Available
    definition: How the front page shows a function the business has not built.
  requested_outcomes:
  - outcome: A person can register themselves from a web page and be told what happened.
  - outcome: An authority can record a verification decision from a web page and be told what happened.
  - outcome: The business offers exactly the acts it has chosen to offer, by name, and turns away any other request.
  - outcome: 'A caller is always told which of three things happened: the act was done, it was turned away and why, or something went wrong inside the business.'
  - outcome: The front page shows all six blockchain functions, with wallet, transaction, block and consensus marked as not yet available.
  - outcome: No business rule lives in the web page.
  known_facts:
  - fact: The two acts a person and an authority perform are performed by parties outside the business.
    certainty: HIGH
  - fact: Today the only way to reach either act is an internal tool run by a member of staff.
    certainty: HIGH
  - fact: 'Two acts are offered from outside: registering an actor, and recording a verification decision.'
    certainty: HIGH
  - fact: Those two are offered because they are the two acts identity has.
    certainty: HIGH
  - fact: A request for anything the business has not offered is turned away because the business does not offer it.
    certainty: HIGH
  - fact: An act is reachable because the business chose to offer it, not because it happens to exist.
    certainty: HIGH
  - fact: There is one way in, and the request names the act it wants.
    certainty: HIGH
  - fact: The business expects to add many more acts over time and does not want to give callers a new address for each one.
    certainty: HIGH
  - fact: An act is named by its business name, which is the business's public word for it.
    certainty: HIGH
  - fact: The name of an act should stay the same even if the way the business performs the act changes.
    certainty: HIGH
  - fact: 'A request for an offered act is checked in one way only: whether the business can read what was sent.'
    certainty: HIGH
  - fact: Details are unreadable when they are missing, or not in the form the business asked for.
    certainty: HIGH
  - fact: The readability test is the one the previous change already defined for registration, reused rather than rewritten.
    certainty: HIGH
  - fact: Nothing else is judged before the act starts; if the details can be read, the act runs.
    certainty: HIGH
  - fact: Whatever the business then decides about the caller is decided where it was always decided.
    certainty: HIGH
  - fact: A turned-away request is not recorded as an identity event, because nothing happened to an actor.
    certainty: HIGH
  - fact: A caller who is turned away is told which of the two reasons it was, and which details were the problem.
    certainty: HIGH
  - fact: Every request gets an answer.
    certainty: HIGH
  - fact: 'An answer is one of three kinds: the act was done, the act was turned away and why, or something went wrong inside the business.'
    certainty: HIGH
  - fact: A caller never has to guess which of the three happened.
    certainty: HIGH
  - fact: The answer appears on the page and that is the end of it; the business sends the person nothing afterwards.
    certainty: HIGH
  - fact: Confirming a registration by email made the person wait for the mail to be sent before being told anything, so confirmation was made optional and is now left out altogether.
    certainty: HIGH
  - fact: The caller is given nothing to quote back later, because nothing in this change requires them to come back.
    certainty: HIGH
  - fact: Being turned away is not the same as the business deciding against the request, and the caller is told which.
    certainty: HIGH
  - fact: Being turned away means the business did not start; the business saying no means it started and decided against it.
    certainty: HIGH
  - fact: The business promises that it answers, not how fast.
    certainty: HIGH
  - fact: The web page collects what the caller types, sends it, and shows the answer.
    certainty: HIGH
  - fact: The web page holds no business rules, decides nothing about the details, decides nothing about what happens next, and keeps no copy of what the business holds.
    certainty: HIGH
  - fact: The page may carry a detail the person has just typed from one page to the next, so they do not type it twice.
    certainty: HIGH
  - fact: Someone who registers and then goes to the decision page should find the address they just entered already filled in.
    certainty: HIGH
  - fact: A carried detail is a convenience for whoever fills in the form; it is not a record, the business never reads it, and nothing the business does depends on it being there.
    certainty: HIGH
  - fact: A page that lost a carried detail would still work, because the person would simply retype it.
    certainty: HIGH
  - fact: The web page does not check details before sending them; the platform checks them and says what is wrong, and the page shows that.
    certainty: HIGH
  - fact: A page that checked details itself would be a second opinion the business never approved.
    certainty: HIGH
  - fact: A rule must not live in two places, because the two will eventually disagree and nobody will know which is right.
    certainty: HIGH
  - fact: The page is a form and an answer, plain and quick to load, not an application.
    certainty: HIGH
  - fact: The pages being built are two — registering an actor, and recording a verification decision — plus a front page.
    certainty: HIGH
  - fact: The front page lists all six blockchain functions, and marks wallet, transaction, block and consensus as not yet available.
    certainty: HIGH
  - fact: The business would rather show a caller what is coming than offer something that fails when they click it.
    certainty: HIGH
  - fact: Listing the unbuilt functions promises nothing about whether or when the business will build them.
    certainty: HIGH
  - fact: No account or login is needed, because registration is done by someone the business does not know yet.
    certainty: HIGH
  - fact: The business does not check that a caller is who they claim to be.
    certainty: HIGH
  - fact: The business does not check that an authority recording a decision is allowed to; it records the authority's name, as it already did.
    certainty: HIGH
  - fact: Anyone can record a verification decision naming any authority, and the business states this openly.
    certainty: HIGH
  - fact: Being reachable from a web page does not weaken the authority claim, but does make it easier to make.
    certainty: HIGH
  - fact: The business does not tell a person apart from an authority at the web page; it tells them apart in the acts themselves and in what gets recorded.
    certainty: HIGH
  system_beliefs:
  - belief: The business author believes the identity function already exists, with both acts working.
    why_it_matters: If either act is absent or differs from what the author describes, this change is not an extension of a working function and the pages have nothing to reach.
    verification_goal: Establish whether the composition governs registering an actor and recording a verification decision, as the previous change defined them.
  - belief: The business author believes the platform already offers a way to be reached from outside, and that identity does not have one yet.
    why_it_matters: If no such way exists, this change must ask for one; if identity already has one, the change is smaller than stated.
    verification_goal: Establish whether the composition offers a way for an outside caller to reach a governed act, and whether identity uses it.
  - belief: The business author believes the readability test defined by the previous change can be reused as it stands, rather than restated.
    why_it_matters: Restating it would create a second test for one question, which the author explicitly refuses.
    verification_goal: Establish whether the readability check on registration details is declared in a form this change can reuse without redefining it.
  - belief: The business author believes the platform can already distinguish a request it declines to begin from an act that ran and decided against the caller.
    why_it_matters: The two must reach the caller as different answers; if the platform cannot tell them apart, the answer collapses them.
    verification_goal: Establish whether the composition distinguishes a request refused before an act from a refusal decided within one.
  - belief: The business author believes the other five blockchain functions have nothing to offer from outside yet.
    why_it_matters: The front page marks them not yet available; if any is in fact governed, the page would be wrong.
    verification_goal: Establish whether the composition governs any blockchain function other than identity.
  assumptions:
  - assumption: A caller has a web browser and can reach the business over the public network.
    basis: The business author asks for a web page and describes no other way in.
  - assumption: The volume of requests will be small enough that not settling how busy the site may get costs the business nothing yet.
    basis: The business author explicitly leaves volume, pace and speed of answer unsettled.
  - assumption: Callers acting as authorities will name authorities honestly while no check exists.
    basis: The business author accepts an unchecked authority claim for this change and defers the check, which only holds while the claim is usually honest.
  - assumption: A caller turned away will read the reason and correct their details rather than repeat the request unchanged.
    basis: The business author requires the reason to be given so the caller can fix it.
  constraints:
  - constraint: No business rule may live in the web page.
    source: The business author's statement that the page holds no rules and that a rule must not live in two places.
  - constraint: The page may hold only what the person has just typed, and only to save them retyping it.
    source: The business author's statement of what the page may hold on to.
  - constraint: The web page must not check details before sending them.
    source: The business author's statement that a page checking details would be a second opinion the business never approved.
  - constraint: The page must be plain and quick to load — a form and an answer, not an application.
    source: The business author's statement of what the page is.
  - constraint: There is one way in, and the request names the act.
    source: The business author's statement that the business will add many acts and does not want to hand callers a new address for each.
  - constraint: The name of an act is the business's public word for it and must outlive changes to how the act is performed.
    source: The business author's statement about what the acts are called.
  - constraint: The readability test must be the one the previous change defined, not a second one.
    source: The business author's statement that this change reuses it rather than writing a second.
  - constraint: Only acts the business has chosen to offer may be reached.
    source: The business author's statement that an act is reachable because the business chose to offer it.
  - constraint: The change introduces no identity behaviour and revisits no decision the previous change made.
    source: The business author's statement of what this change is.
  business_invariants:
  - invariant: Only an act the business has chosen to offer can be reached from outside.
  - invariant: Every request receives an answer.
  - invariant: 'Every answer is exactly one of three kinds: the act was done, the act was turned away, or something went wrong inside the business.'
  - invariant: An answer that turns a request away states which of the two reasons it was.
  - invariant: A request turned away creates no record of an actor.
  - invariant: A request whose details can be read is passed to the act, and nothing further is judged beforehand.
  - invariant: No business rule is held by the web page.
  - invariant: Nothing the business holds is copied into the web page.
  - invariant: No act of the business depends on a detail the page carried forward.
  - invariant: Being turned away and being decided against are never reported as the same answer.
  lifecycle_states: []
  business_events: []
  authority_boundaries:
  - business_object: The set of acts offered from outside
    authoritative_owner: The identity function of the blockchain project, for its own acts.
  - business_object: The name of an offered act
    authoritative_owner: The business, as its public word for the act.
  - business_object: The decision to turn a request away
    authoritative_owner: The business, before the act begins.
  - business_object: The web page
    authoritative_owner: The business; it holds no rules and owns no decision.
  - business_object: The front page and what it marks as not yet available
    authoritative_owner: The blockchain project, across all six functions.
  out_of_scope:
  - item: Checking that a caller is who they claim to be
    reason: Named by the business author as not decided by this change.
  - item: Checking that a named authority is allowed to decide
    reason: Inseparable from deciding who may be an authority, which the previous change already left for later.
  - item: Any identity behaviour, and any decision the previous change made
    reason: This change gives the existing acts a way in and changes nothing about them.
  - item: Telling a person anything after they leave the page, by email or any other means
    reason: Making the person wait for it is what caused the trouble last time; it returns as a change of its own.
  - item: Looking up an actor from the web page
    reason: A separate need; the business would rather offer nothing than a reading surface whose shape it has not decided.
  - item: Web pages for wallet, transaction, mempool, block, chain and consensus
    reason: Each comes with the function it belongs to.
  - item: How many requests the business will accept, and how fast it answers
    reason: Named by the business author as not settled here.
  governance_scope:
  - scope_item: Identity
    relationship: EXTENDED
  - scope_item: Wallet
    relationship: ADJACENT
  - scope_item: Transaction
    relationship: ADJACENT
  - scope_item: Mempool
    relationship: ADJACENT
  - scope_item: Block
    relationship: ADJACENT
  - scope_item: Chain
    relationship: ADJACENT
  - scope_item: Consensus
    relationship: ADJACENT
  clarification_requests: []
  acceptance_criteria:
  - criterion: A person can register from the web page, and is afterwards an unverified actor.
  - criterion: An authority can record a decision from the web page, and the actor is afterwards accepted or rejected as decided.
  - criterion: A registration made from the web page produces the same result as the same registration made from the internal tool.
  - criterion: A person who registers is told the outcome on the page, and the business sends them nothing afterwards.
  - criterion: A request naming an act the business does not offer is turned away, and the caller is told the act is not offered.
  - criterion: A request naming an offered act with a missing contact address is turned away, and the caller is told which detail was the problem.
  - criterion: A request turned away leaves no actor and no record behind.
  - criterion: A decision recorded against an actor already decided about is answered as the business deciding against the request, not as being turned away, and the caller can tell the two apart.
  - criterion: The front page lists all six blockchain functions, and wallet, transaction, block and consensus are marked as not yet available and cannot be used.
  - criterion: No caller needs an account or a login to use either page.
  - criterion: Removing every rule from the web page leaves the business's behaviour unchanged.
  - criterion: A person who registers and then opens the decision page finds the address they just entered already filled in.
  - criterion: Clearing what the page carried forward changes no outcome; the person retypes the detail and the result is the same.
  - criterion: Changing a rule in the platform changes what a caller is told without the web page being changed.
  identity_and_sameness:
  - business_object: Offered Act
    identified_by: Its business name.
    two_are_the_same_when: Their names match; the name is the act, whatever the business does to perform it.
  - business_object: Request
    identified_by: The act it names and the details it carries.
    two_are_the_same_when: Never — two requests are two requests even when identical, because each is answered separately.
  lifecycle_transitions: []
  operation_refusals:
  - operation: Any request from outside
    refused_when: The act it names is not one the business offers.
    business_reason: An act is reachable because the business chose to offer it, not because it happens to exist.
  - operation: Any request from outside
    refused_when: The details it carries cannot be read — missing, or not in the form the business asked for.
    business_reason: The business checks readability and nothing else before an act starts.
  - operation: Any request from outside
    refused_when: Never for the business's judgement of the caller or their details.
    business_reason: Anything beyond readability is the act's own decision, made where it was always made.
  - operation: Registering an actor from the web page
    refused_when: The web page judges the details itself.
    business_reason: A page that checked details would be a second opinion the business never approved.
  - operation: Any act the front page marks as not yet available
    refused_when: Always.
    business_reason: The business shows what is coming rather than offering something that fails.
  authority_deferrals:
  - business_object: Establishing who a caller is
    deferred_to: A follow-on governed change for checking callers
    until: The business takes up who may be an authority, with which it belongs.
  - business_object: Establishing that a named authority is allowed to decide
    deferred_to: A follow-on governed change for authority over verifiers
    until: The business chooses to take it up; the previous change already deferred it.
  - business_object: Telling a person anything after they leave the page
    deferred_to: A follow-on governed change for confirmation
    until: The business wants it back, and can provide it without keeping the person waiting.
  - business_object: Looking up an actor from outside
    deferred_to: A follow-on governed change for reading identity
    until: The business decides the shape of a reading surface.
  - business_object: A way in for wallet, transaction, mempool, block, chain and consensus
    deferred_to: The change that builds each function
    until: Each function is taken up.
  - business_object: How busy the site may get, and how fast the business answers
    deferred_to: A follow-on governed change
    until: The business has reason to settle it.
```

Reorganized faithfully from `p0_business_problem_statement.md`, including the clarifications its
author answered. Human input only — nothing here was added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

## 1. CR Type

## 2. Business Vocabulary

## 3. Requested Outcomes

## 4. Known Facts — Business Truths

## 5. Existing-System Beliefs — Requiring Verification

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

## 6. Assumptions

## 7. Constraints

## 8. Business Invariants

## 9. Lifecycle States

## 10. Business Events

## 11. Authority Boundaries

## 12. Out of Scope

## 13. Governance Scope

## 14. Clarification Requests

## 15. Acceptance Criteria

## 16. Identity and Sameness

## 17. Lifecycle Transitions

## 18. Operation Refusals

## 19. Authority Deferrals

---

## gov_projection — Governed Handoff to Stage 1

| Direction | Fields |
|-----------|--------|
| **Consumes** ← human | business problem statement |
| **Emits** → Stage 1 | subdomain_purpose · cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
