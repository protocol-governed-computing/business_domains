# Stage 1 — Change Request: Clarification & Fact Capture: blockchain / identity

## Machine

```yaml
document:
  phase: p1
  domain: blockchain
  subdomain: identity
  cr: cr_02_identity
  rule_set: transformation.schemas.REGISTER_SCHEMA_P1_V0
registers:
  cr_type:
  - classification: EXTEND_SUBDOMAIN
    rationale: The identity function already exists and works. The change gives its two existing acts a way in from outside, and states what the business offers and what it turns away. No identity behaviour is introduced and no earlier decision is revisited.
    source_finding: {phase: p0, register: cr_type, row: 1}
  business_vocabulary:
  - term: Offered Act
    definition: An act the business has chosen to make reachable from outside, named by its business name.
    source_finding: {phase: p0, register: business_vocabulary, row: 1}
  - term: Registering an Actor
    definition: The offered act by which a person supplies their own details and is admitted unverified.
    source_finding: {phase: p0, register: business_vocabulary, row: 2}
  - term: Recording a Verification Decision
    definition: The offered act by which an authority accepts or rejects a registered actor.
    source_finding: {phase: p0, register: business_vocabulary, row: 3}
  - term: Request
    definition: 'What a caller sends: the name of the act they want, and the details that act needs.'
    source_finding: {phase: p0, register: business_vocabulary, row: 4}
  - term: Caller
    definition: Whoever sends a request, whether a person registering themselves or an authority recording a decision.
    source_finding: {phase: p0, register: business_vocabulary, row: 5}
  - term: Answer
    definition: What the business tells a caller in reply to a request. Always one of three kinds.
    source_finding: {phase: p0, register: business_vocabulary, row: 6}
  - term: Turned Away
    definition: A request the business declines to begin, either because the act is not offered or because the details cannot be read.
    source_finding: {phase: p0, register: business_vocabulary, row: 7}
  - term: Unreadable Details
    definition: Details that are missing, or not in the form the business asked for. The same test the previous change set for registration.
    source_finding: {phase: p0, register: business_vocabulary, row: 8}
  - term: Web Page
    definition: The form a caller fills in and the answer they are shown. It holds no business rules.
    source_finding: {phase: p0, register: business_vocabulary, row: 9}
  - term: Carried Detail
    definition: Something the person has just typed, held only to save them typing it again on the next page. Not a record, and never read by the business.
    source_finding: {phase: p0, register: business_vocabulary, row: 10}
  - term: Front Page
    definition: The page listing the project's six functions, marking those that are not yet available.
    source_finding: {phase: p0, register: business_vocabulary, row: 11}
  - term: Not Yet Available
    definition: How the front page shows a function the business has not built.
    source_finding: {phase: p0, register: business_vocabulary, row: 12}
  requested_outcomes:
  - outcome: A person can register themselves from a web page and be told what happened.
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - outcome: An authority can record a verification decision from a web page and be told what happened.
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - outcome: The business offers exactly the acts it has chosen to offer, by name, and turns away any other request.
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  - outcome: 'A caller is always told which of three things happened: the act was done, it was turned away and why, or something went wrong inside the business.'
    source_finding: {phase: p0, register: requested_outcomes, row: 4}
  - outcome: The front page shows all six blockchain functions, with wallet, transaction, block and consensus marked as not yet available.
    source_finding: {phase: p0, register: requested_outcomes, row: 5}
  - outcome: No business rule lives in the web page.
    source_finding: {phase: p0, register: requested_outcomes, row: 6}
  known_facts:
  - fact: The two acts a person and an authority perform are performed by parties outside the business.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 1}
  - fact: Today the only way to reach either act is an internal tool run by a member of staff.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 2}
  - fact: 'Two acts are offered from outside: registering an actor, and recording a verification decision.'
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 3}
  - fact: Those two are offered because they are the two acts identity has.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 4}
  - fact: A request for anything the business has not offered is turned away because the business does not offer it.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 5}
  - fact: An act is reachable because the business chose to offer it, not because it happens to exist.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 6}
  - fact: There is one way in, and the request names the act it wants.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 7}
  - fact: The business expects to add many more acts over time and does not want to give callers a new address for each one.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 8}
  - fact: An act is named by its business name, which is the business's public word for it.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 9}
  - fact: The name of an act should stay the same even if the way the business performs the act changes.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 10}
  - fact: 'A request for an offered act is checked in one way only: whether the business can read what was sent.'
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 11}
  - fact: Details are unreadable when they are missing, or not in the form the business asked for.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 12}
  - fact: The readability test is the one the previous change already defined for registration, reused rather than rewritten.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 13}
  - fact: Nothing else is judged before the act starts; if the details can be read, the act runs.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 14}
  - fact: Whatever the business then decides about the caller is decided where it was always decided.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 15}
  - fact: A turned-away request is not recorded as an identity event, because nothing happened to an actor.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 16}
  - fact: A caller who is turned away is told which of the two reasons it was, and which details were the problem.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 17}
  - fact: Every request gets an answer.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 18}
  - fact: 'An answer is one of three kinds: the act was done, the act was turned away and why, or something went wrong inside the business.'
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 19}
  - fact: A caller never has to guess which of the three happened.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 20}
  - fact: The answer appears on the page and that is the end of it; the business sends the person nothing afterwards.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 21}
  - fact: Confirming a registration by email made the person wait for the mail to be sent before being told anything, so confirmation was made optional and is now left out altogether.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 22}
  - fact: The caller is given nothing to quote back later, because nothing in this change requires them to come back.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 23}
  - fact: Being turned away is not the same as the business deciding against the request, and the caller is told which.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 24}
  - fact: Being turned away means the business did not start; the business saying no means it started and decided against it.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 25}
  - fact: The business promises that it answers, not how fast.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 26}
  - fact: The web page collects what the caller types, sends it, and shows the answer.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 27}
  - fact: The web page holds no business rules, decides nothing about the details, decides nothing about what happens next, and keeps no copy of what the business holds.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 28}
  - fact: The page may carry a detail the person has just typed from one page to the next, so they do not type it twice.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 29}
  - fact: Someone who registers and then goes to the decision page should find the address they just entered already filled in.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 30}
  - fact: A carried detail is a convenience for whoever fills in the form; it is not a record, the business never reads it, and nothing the business does depends on it being there.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 31}
  - fact: A page that lost a carried detail would still work, because the person would simply retype it.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 32}
  - fact: The web page does not check details before sending them; the platform checks them and says what is wrong, and the page shows that.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 33}
  - fact: A page that checked details itself would be a second opinion the business never approved.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 34}
  - fact: A rule must not live in two places, because the two will eventually disagree and nobody will know which is right.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 35}
  - fact: The page is a form and an answer, plain and quick to load, not an application.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 36}
  - fact: The pages being built are two — registering an actor, and recording a verification decision — plus a front page.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 37}
  - fact: The front page lists all six blockchain functions, and marks wallet, transaction, block and consensus as not yet available.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 38}
  - fact: The business would rather show a caller what is coming than offer something that fails when they click it.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 39}
  - fact: Listing the unbuilt functions promises nothing about whether or when the business will build them.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 40}
  - fact: No account or login is needed, because registration is done by someone the business does not know yet.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 41}
  - fact: The business does not check that a caller is who they claim to be.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 42}
  - fact: The business does not check that an authority recording a decision is allowed to; it records the authority's name, as it already did.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 43}
  - fact: Anyone can record a verification decision naming any authority, and the business states this openly.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 44}
  - fact: Being reachable from a web page does not weaken the authority claim, but does make it easier to make.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 45}
  - fact: The business does not tell a person apart from an authority at the web page; it tells them apart in the acts themselves and in what gets recorded.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 46}
  system_beliefs:
  - belief: The business author believes the identity function already exists, with both acts working.
    why_it_matters: If either act is absent or differs from what the author describes, this change is not an extension of a working function and the pages have nothing to reach.
    verification_goal: Establish whether the composition governs registering an actor and recording a verification decision, as the previous change defined them.
    source_finding: {phase: p0, register: system_beliefs, row: 1}
  - belief: The business author believes the platform already offers a way to be reached from outside, and that identity does not have one yet.
    why_it_matters: If no such way exists, this change must ask for one; if identity already has one, the change is smaller than stated.
    verification_goal: Establish whether the composition offers a way for an outside caller to reach a governed act, and whether identity uses it.
    source_finding: {phase: p0, register: system_beliefs, row: 2}
  - belief: The business author believes the readability test defined by the previous change can be reused as it stands, rather than restated.
    why_it_matters: Restating it would create a second test for one question, which the author explicitly refuses.
    verification_goal: Establish whether the readability check on registration details is declared in a form this change can reuse without redefining it.
    source_finding: {phase: p0, register: system_beliefs, row: 3}
  - belief: The business author believes the platform can already distinguish a request it declines to begin from an act that ran and decided against the caller.
    why_it_matters: The two must reach the caller as different answers; if the platform cannot tell them apart, the answer collapses them.
    verification_goal: Establish whether the composition distinguishes a request refused before an act from a refusal decided within one.
    source_finding: {phase: p0, register: system_beliefs, row: 4}
  - belief: The business author believes the other five blockchain functions have nothing to offer from outside yet.
    why_it_matters: The front page marks them not yet available; if any is in fact governed, the page would be wrong.
    verification_goal: Establish whether the composition governs any blockchain function other than identity.
    source_finding: {phase: p0, register: system_beliefs, row: 5}
  assumptions:
  - assumption: A caller has a web browser and can reach the business over the public network.
    basis: The business author asks for a web page and describes no other way in.
    source_finding: {phase: p0, register: assumptions, row: 1}
  - assumption: The volume of requests will be small enough that not settling how busy the site may get costs the business nothing yet.
    basis: The business author explicitly leaves volume, pace and speed of answer unsettled.
    source_finding: {phase: p0, register: assumptions, row: 2}
  - assumption: Callers acting as authorities will name authorities honestly while no check exists.
    basis: The business author accepts an unchecked authority claim for this change and defers the check, which only holds while the claim is usually honest.
    source_finding: {phase: p0, register: assumptions, row: 3}
  - assumption: A caller turned away will read the reason and correct their details rather than repeat the request unchanged.
    basis: The business author requires the reason to be given so the caller can fix it.
    source_finding: {phase: p0, register: assumptions, row: 4}
  constraints:
  - constraint: No business rule may live in the web page.
    source: The business author's statement that the page holds no rules and that a rule must not live in two places.
    source_finding: {phase: p0, register: constraints, row: 1}
  - constraint: The page may hold only what the person has just typed, and only to save them retyping it.
    source: The business author's statement of what the page may hold on to.
    source_finding: {phase: p0, register: constraints, row: 2}
  - constraint: The web page must not check details before sending them.
    source: The business author's statement that a page checking details would be a second opinion the business never approved.
    source_finding: {phase: p0, register: constraints, row: 3}
  - constraint: The page must be plain and quick to load — a form and an answer, not an application.
    source: The business author's statement of what the page is.
    source_finding: {phase: p0, register: constraints, row: 4}
  - constraint: There is one way in, and the request names the act.
    source: The business author's statement that the business will add many acts and does not want to hand callers a new address for each.
    source_finding: {phase: p0, register: constraints, row: 5}
  - constraint: The name of an act is the business's public word for it and must outlive changes to how the act is performed.
    source: The business author's statement about what the acts are called.
    source_finding: {phase: p0, register: constraints, row: 6}
  - constraint: The readability test must be the one the previous change defined, not a second one.
    source: The business author's statement that this change reuses it rather than writing a second.
    source_finding: {phase: p0, register: constraints, row: 7}
  - constraint: Only acts the business has chosen to offer may be reached.
    source: The business author's statement that an act is reachable because the business chose to offer it.
    source_finding: {phase: p0, register: constraints, row: 8}
  - constraint: The change introduces no identity behaviour and revisits no decision the previous change made.
    source: The business author's statement of what this change is.
    source_finding: {phase: p0, register: constraints, row: 9}
  business_invariants:
  - invariant: Only an act the business has chosen to offer can be reached from outside.
    source_finding: {phase: p0, register: business_invariants, row: 1}
  - invariant: Every request receives an answer.
    source_finding: {phase: p0, register: business_invariants, row: 2}
  - invariant: 'Every answer is exactly one of three kinds: the act was done, the act was turned away, or something went wrong inside the business.'
    source_finding: {phase: p0, register: business_invariants, row: 3}
  - invariant: An answer that turns a request away states which of the two reasons it was.
    source_finding: {phase: p0, register: business_invariants, row: 4}
  - invariant: A request turned away creates no record of an actor.
    source_finding: {phase: p0, register: business_invariants, row: 5}
  - invariant: A request whose details can be read is passed to the act, and nothing further is judged beforehand.
    source_finding: {phase: p0, register: business_invariants, row: 6}
  - invariant: No business rule is held by the web page.
    source_finding: {phase: p0, register: business_invariants, row: 7}
  - invariant: Nothing the business holds is copied into the web page.
    source_finding: {phase: p0, register: business_invariants, row: 8}
  - invariant: No act of the business depends on a detail the page carried forward.
    source_finding: {phase: p0, register: business_invariants, row: 9}
  - invariant: Being turned away and being decided against are never reported as the same answer.
    source_finding: {phase: p0, register: business_invariants, row: 10}
  lifecycle_states: []
  business_events: []
  authority_boundaries:
  - business_object: The set of acts offered from outside
    authoritative_owner: The identity function of the blockchain project, for its own acts.
    source_finding: {phase: p0, register: authority_boundaries, row: 1}
  - business_object: The name of an offered act
    authoritative_owner: The business, as its public word for the act.
    source_finding: {phase: p0, register: authority_boundaries, row: 2}
  - business_object: The decision to turn a request away
    authoritative_owner: The business, before the act begins.
    source_finding: {phase: p0, register: authority_boundaries, row: 3}
  - business_object: The web page
    authoritative_owner: The business; it holds no rules and owns no decision.
    source_finding: {phase: p0, register: authority_boundaries, row: 4}
  - business_object: The front page and what it marks as not yet available
    authoritative_owner: The blockchain project, across all six functions.
    source_finding: {phase: p0, register: authority_boundaries, row: 5}
  out_of_scope:
  - item: Checking that a caller is who they claim to be
    reason: Named by the business author as not decided by this change.
    source_finding: {phase: p0, register: out_of_scope, row: 1}
  - item: Checking that a named authority is allowed to decide
    reason: Inseparable from deciding who may be an authority, which the previous change already left for later.
    source_finding: {phase: p0, register: out_of_scope, row: 2}
  - item: Any identity behaviour, and any decision the previous change made
    reason: This change gives the existing acts a way in and changes nothing about them.
    source_finding: {phase: p0, register: out_of_scope, row: 3}
  - item: Telling a person anything after they leave the page, by email or any other means
    reason: Making the person wait for it is what caused the trouble last time; it returns as a change of its own.
    source_finding: {phase: p0, register: out_of_scope, row: 4}
  - item: Looking up an actor from the web page
    reason: A separate need; the business would rather offer nothing than a reading surface whose shape it has not decided.
    source_finding: {phase: p0, register: out_of_scope, row: 5}
  - item: Web pages for wallet, transaction, mempool, block, chain and consensus
    reason: Each comes with the function it belongs to.
    source_finding: {phase: p0, register: out_of_scope, row: 6}
  - item: How many requests the business will accept, and how fast it answers
    reason: Named by the business author as not settled here.
    source_finding: {phase: p0, register: out_of_scope, row: 7}
  governance_scope:
  - scope_item: Identity
    relationship: EXTENDED
    source_finding: {phase: p0, register: governance_scope, row: 1}
  - scope_item: Wallet
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 2}
  - scope_item: Transaction
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 3}
  - scope_item: Mempool
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 4}
  - scope_item: Block
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 5}
  - scope_item: Chain
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 6}
  - scope_item: Consensus
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 7}
  clarification_requests: []
  acceptance_criteria:
  - criterion: A person can register from the web page, and is afterwards an unverified actor.
    source_finding: {phase: p0, register: acceptance_criteria, row: 1}
  - criterion: An authority can record a decision from the web page, and the actor is afterwards accepted or rejected as decided.
    source_finding: {phase: p0, register: acceptance_criteria, row: 2}
  - criterion: A registration made from the web page produces the same result as the same registration made from the internal tool.
    source_finding: {phase: p0, register: acceptance_criteria, row: 3}
  - criterion: A person who registers is told the outcome on the page, and the business sends them nothing afterwards.
    source_finding: {phase: p0, register: acceptance_criteria, row: 4}
  - criterion: A request naming an act the business does not offer is turned away, and the caller is told the act is not offered.
    source_finding: {phase: p0, register: acceptance_criteria, row: 5}
  - criterion: A request naming an offered act with a missing contact address is turned away, and the caller is told which detail was the problem.
    source_finding: {phase: p0, register: acceptance_criteria, row: 6}
  - criterion: A request turned away leaves no actor and no record behind.
    source_finding: {phase: p0, register: acceptance_criteria, row: 7}
  - criterion: A decision recorded against an actor already decided about is answered as the business deciding against the request, not as being turned away, and the caller can tell the two apart.
    source_finding: {phase: p0, register: acceptance_criteria, row: 8}
  - criterion: The front page lists all six blockchain functions, and wallet, transaction, block and consensus are marked as not yet available and cannot be used.
    source_finding: {phase: p0, register: acceptance_criteria, row: 9}
  - criterion: No caller needs an account or a login to use either page.
    source_finding: {phase: p0, register: acceptance_criteria, row: 10}
  - criterion: Removing every rule from the web page leaves the business's behaviour unchanged.
    source_finding: {phase: p0, register: acceptance_criteria, row: 11}
  - criterion: A person who registers and then opens the decision page finds the address they just entered already filled in.
    source_finding: {phase: p0, register: acceptance_criteria, row: 12}
  - criterion: Clearing what the page carried forward changes no outcome; the person retypes the detail and the result is the same.
    source_finding: {phase: p0, register: acceptance_criteria, row: 13}
  - criterion: Changing a rule in the platform changes what a caller is told without the web page being changed.
    source_finding: {phase: p0, register: acceptance_criteria, row: 14}
  identity_and_sameness:
  - business_object: Offered Act
    identified_by: Its business name.
    two_are_the_same_when: Their names match; the name is the act, whatever the business does to perform it.
    source_finding: {phase: p0, register: identity_and_sameness, row: 1}
  - business_object: Request
    identified_by: The act it names and the details it carries.
    two_are_the_same_when: Never — two requests are two requests even when identical, because each is answered separately.
    source_finding: {phase: p0, register: identity_and_sameness, row: 2}
  lifecycle_transitions: []
  operation_refusals:
  - operation: Any request from outside
    refused_when: The act it names is not one the business offers.
    business_reason: An act is reachable because the business chose to offer it, not because it happens to exist.
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: Any request from outside
    refused_when: The details it carries cannot be read — missing, or not in the form the business asked for.
    business_reason: The business checks readability and nothing else before an act starts.
    source_finding: {phase: p0, register: operation_refusals, row: 2}
  - operation: Any request from outside
    refused_when: Never for the business's judgement of the caller or their details.
    business_reason: Anything beyond readability is the act's own decision, made where it was always made.
    source_finding: {phase: p0, register: operation_refusals, row: 3}
  - operation: Registering an actor from the web page
    refused_when: The web page judges the details itself.
    business_reason: A page that checked details would be a second opinion the business never approved.
    source_finding: {phase: p0, register: operation_refusals, row: 4}
  - operation: Any act the front page marks as not yet available
    refused_when: Always.
    business_reason: The business shows what is coming rather than offering something that fails.
    source_finding: {phase: p0, register: operation_refusals, row: 5}
  authority_deferrals:
  - business_object: Establishing who a caller is
    deferred_to: A follow-on governed change for checking callers
    until: The business takes up who may be an authority, with which it belongs.
    source_finding: {phase: p0, register: authority_deferrals, row: 1}
  - business_object: Establishing that a named authority is allowed to decide
    deferred_to: A follow-on governed change for authority over verifiers
    until: The business chooses to take it up; the previous change already deferred it.
    source_finding: {phase: p0, register: authority_deferrals, row: 2}
  - business_object: Telling a person anything after they leave the page
    deferred_to: A follow-on governed change for confirmation
    until: The business wants it back, and can provide it without keeping the person waiting.
    source_finding: {phase: p0, register: authority_deferrals, row: 3}
  - business_object: Looking up an actor from outside
    deferred_to: A follow-on governed change for reading identity
    until: The business decides the shape of a reading surface.
    source_finding: {phase: p0, register: authority_deferrals, row: 4}
  - business_object: A way in for wallet, transaction, mempool, block, chain and consensus
    deferred_to: The change that builds each function
    until: Each function is taken up.
    source_finding: {phase: p0, register: authority_deferrals, row: 5}
  - business_object: How busy the site may get, and how fast the business answers
    deferred_to: A follow-on governed change
    until: The business has reason to settle it.
    source_finding: {phase: p0, register: authority_deferrals, row: 6}
```

Projected from the change seed. Every row is the seed's own, cited to the section it was
said in. S1 interrogates and does not author: a question raised by restating the seed
amends the seed and is projected again, so no row here states business content the seed
does not.

---

## 1. CR Type

---

## 2. Business Vocabulary

---

## 3. Requested Outcomes

---

## 4. Known Facts — Business Truths

---

## 5. Existing-System Beliefs — Requiring Verification

---

## 6. Assumptions

---

## 7. Constraints

---

## 8. Business Invariants

---

## 9. Lifecycle States

---

## 10. Business Events

---

## 11. Authority Boundaries

---

## 12. Out of Scope

---

## 13. Governance Scope

---

## 14. Clarification Requests

---

## 15. Acceptance Criteria

---

## 16. Identity and Sameness

---

## 17. Lifecycle Transitions

---

## 18. Operation Refusals

---

## 19. Authority Deferrals

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
