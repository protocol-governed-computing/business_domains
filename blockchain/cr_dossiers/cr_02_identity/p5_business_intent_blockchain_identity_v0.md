# Stage 5 — Business Intent: blockchain / identity

**Stage:** 5 — Business Intent
**CR:** cr_02_identity
**Status:** DRAFT
**Feeds:** Stage 6 — Governance Intent

---

## 1. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The Identity subdomain governs who an actor is and whether the business trusts them. It holds one
record for each person known to the system, the state that says whether the business has accepted
them, and the record of every moment in their history. It establishes the authority to say that a
person exists and that they are trusted. It also decides what of itself the business offers to
callers outside it, and what it turns away at the door: three acts are offered by name — a person
registering themselves, an authority accepting a registered actor, and an authority rejecting one —
and anything else is refused as an act the business does not offer. Accepting and rejecting are
offered separately because the business already holds them to be distinct in kind, not one act
carrying an outcome. It exists because the business must admit people before it knows
anything about them and decide afterwards whether to trust them, and because both of those acts are
performed by parties who are not inside the business and must be able to reach it. It does not
govern what a trusted actor may then do, which persons may be an authority, or who a caller is.

<!-- register:purpose_provenance business_language=refinement -->
| Source | Disposition (INHERITED, REFINED) | Refinement |
|--------|----------------------------------|------------|
| CR seed §0 Subdomain Purpose | REFINED | The seed states that identity's two acts are performed by parties outside the business and that today neither can reach it. This states the subdomain that results: alongside the records it holds and the authority it establishes, it now owns what it offers to the outside and what it turns away. Nothing here contradicts the seed or the previous change; what it adds is the standing description of a function that is reachable, rather than the reason for making it so. The seed speaks of two acts offered; three names are offered, because the seed and the previous change both hold acceptance and rejection to be distinct in kind, and naming them together would be the door presenting as one act what the business records as two. |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| Offer registering an actor to a caller outside the business | IN_SCOPE | The public name of the act and what a caller may send. | S4 authoring_scope GAP-01 |
| Offer recording a verification decision to a caller outside the business | IN_SCOPE | A name of its own; what a caller sends differs entirely from registration. | S4 authoring_scope GAP-02 |
| Hold what an act requires and a caller must not send | IN_SCOPE | Held within the two admissions, sealed and stated once. | S4 authoring_scope GAP-03 |
| Tell a caller how their registration ended | IN_SCOPE | Which kind of answer each ending takes, and what of the result is exposed. | S4 authoring_scope GAP-04 |
| Tell a caller how their decision ended | IN_SCOPE | The same over that act's endings, including the actor that does not exist. | S4 authoring_scope GAP-05 |
| Declare where the boundary declarations are found | IN_SCOPE | The domain's build manifest admits both kinds and declares no place for them. | S4 authoring_scope GAP-06 |
| Show a person a form and its answer | IN_SCOPE | Two forms, holding no rules. | S4 authoring_scope GAP-07 |
| Carry a detail from one page to the next | IN_SCOPE | A convenience; nothing the business does depends on it. | S4 authoring_scope GAP-08 |
| Show the functions the business has not built | IN_SCOPE | Four of six named and marked not yet available. | S4 authoring_scope GAP-09 |
| Announce the moments an actor is registered, accepted and rejected | DEFERRED | Owned by construction rather than by identity; the moments are already declared and correct. | S4 authoring_scope Announce the moments an actor is registered, accepted and rejected |
| Hold what an act requires with the act that requires it | DEFERRED | Better placement, and it reopens two sealed acts. | S4 authoring_scope Hold what an act requires with the act that requires it |
| Establishing who a caller is, and what they are allowed to do | DEFERRED | Deferred by the business with the question of who may be an authority. | S4 authoring_scope Establishing who a caller is, and what they are allowed to do |
| Looking up an actor from outside | DEFERRED | The business would rather offer nothing than a reading surface it has not decided the shape of. | S4 authoring_scope Looking up an actor from outside |
| Telling a person anything after they leave the page | DEFERRED | Making the person wait for it is what caused the trouble before. | S4 authoring_scope Telling a person anything after they leave the page |
| A way in for wallet, transaction, mempool, block, chain and consensus | DEFERRED | Each comes with the function it belongs to. | S4 authoring_scope A way in for wallet, transaction, mempool, block, chain and consensus |
| A kind of answer for an act that ran and refused | DEFERRED | A change to the platform's closed governed set, not to this domain. | S4 authoring_scope A kind of answer for an act that ran and refused |

---

## 3. Business Objects

<!-- register:business_objects optional business_language=store_name,business_rationale -->
| Store Name | Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID) | Business Rationale | Source Finding |
|------------|------------------------------------------------------------------------------|--------------------|----------------|

---

## 4. Identity Semantics

<!-- register:identity_semantics business_language=identity_field,source,uniqueness_rule,cross_subdomain_relationship -->
| Store Name | Identity Field | Source | Uniqueness Rule | Cross-Subdomain Relationship | Source Finding |
|------------|----------------|--------|-----------------|------------------------------|----------------|
| NONE IDENTIFIED | The public name of an offered act | Chosen by the business as its word for the act | One name denotes one act; two acts never share a name, and a name outlives the act it currently reaches | Names an act of this subdomain and of no other; a later function's acts take names of their own under the same shared way in | S4 design_decisions #2 |

---

## 5. Invariants

<!-- register:invariants business_language -->
| Invariant | Business Reason | Source Finding |
|-----------|-----------------|----------------|
| Only an act the business has chosen to offer can be reached from outside. | An act is reachable because the business decided to offer it, never because it happens to exist. Without this there is no door, only a wall with holes in it. | S1 business_invariants #1 |
| Every request receives an answer. | A caller who is told nothing cannot know whether they registered, and would try again. | S1 business_invariants #2 |
| Every answer is exactly one of three kinds: the act was done, the act was turned away, or something went wrong inside the business. | The caller must never have to work out which happened, because each calls for something different from them. | S1 business_invariants #3 |
| An answer that turns a request away states which of the two reasons it was. | Told only "no", a caller can correct nothing, and the business gains nothing by withholding it. | S1 business_invariants #4 |
| A request turned away creates no record of an actor. | Nothing happened to an actor. The record of who registered must not fill with people who did not. | S1 business_invariants #5 |
| A request whose details can be read is passed to the act, and nothing further is judged beforehand. | Anything judged before the act is the act's decision made early and by the wrong party. | S1 business_invariants #6 |
| No business rule is held by the web page. | A rule in two places is two rules that will disagree, and nobody will know which is right. | S1 business_invariants #7 |
| Nothing the business holds is copied into the web page. | What the business holds is the business's, and a copy outside it is neither governed nor current. | S1 business_invariants #8 |
| No act of the business depends on a detail the page carried forward. | The convenience must stay a convenience; the moment something depends on it, it is hidden state. | S1 business_invariants #9 |
| Being turned away and being decided against are never reported as the same answer. | One means the business did not start, the other that it started and refused. Telling someone to fix their details when the business has decided about them misleads them. | S1 business_invariants #10 |

---

## 6. Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| Offer | The act of registering an actor, under the business's own name for it | The business decides to make the act reachable from outside | IN_SCOPE | S4 capability_graph Offer registering an actor to a caller outside the business |
| Offer | The act of accepting a registered actor, under the business's own name for it | The business decides to make the act reachable from outside | IN_SCOPE | S4 capability_graph Offer recording a verification decision to a caller outside the business |
| Offer | The act of rejecting a registered actor, under the business's own name for it | The business decides to make the act reachable from outside | IN_SCOPE | S4 capability_graph Offer recording a verification decision to a caller outside the business |
| Turn away | A request naming an act the business does not offer | A caller asks for something the business has not offered | IN_SCOPE | S4 capability_graph Offer both acts through one way in |
| Turn away | A request whose details the business cannot read | A caller sends details that are missing or not of the form asked for | IN_SCOPE | S4 capability_graph Hold what an act requires and a caller must not send |
| Answer | A caller whose registration ran, whichever way it ended | The act of registering reaches an ending | IN_SCOPE | S4 capability_graph Tell a caller how their registration ended |
| Answer | A caller whose decision ran, whichever way it ended | The act of recording a decision reaches an ending | IN_SCOPE | S4 capability_graph Tell a caller how their decision ended |
| Show | The six functions of the project, four of them not yet available | A caller opens the front page | IN_SCOPE | S4 capability_graph Show the functions the business has not built |
| Carry | A detail the person has just typed, to the next page | A person moves from one form to another | IN_SCOPE | S4 capability_graph Carry a detail from one page to the next |
| Establish | Who a caller is, and what they are permitted to ask for | A caller reaches the business | DEFERRED | S4 authoring_scope Establishing who a caller is, and what they are allowed to do |
| Look up | What the business already knows about an actor | A caller asks about an actor rather than acting on one | DEFERRED | S4 authoring_scope Looking up an actor from outside |
| Notify | A person, after they have left the page | A registration or a decision completes | DEFERRED | S4 authoring_scope Telling a person anything after they leave the page |

---

## 7. Provisional Codes

<!-- register:provisional_codes business_language=summary -->
| Provisional Code | Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE) | Summary | Source Finding |
|------------------|-------------------------|---------|----------------|
| TI_REGISTER_ACTOR_V0 | TI | Offers registering an actor under the business's public name for it, states what a caller may send, and holds what the act requires and a caller must not | S4 gap_register GAP-01 |
| TE_REGISTER_ACTOR_V0 | TE | States which kind of answer each ending of registering an actor takes, and what of the result the caller is told | S4 gap_register GAP-04 |
| TI_ACCEPT_ACTOR_V0 | TI | Offers accepting a registered actor under the business's public name for it, states what a caller may send, and holds what the act requires and a caller must not | S4 gap_register GAP-02 |
| TE_ACCEPT_ACTOR_V0 | TE | States which kind of answer each ending of accepting an actor takes, including the actor that does not exist, and what of the result the caller is told | S4 gap_register GAP-05 |
| TI_REJECT_ACTOR_V0 | TI | Offers rejecting a registered actor under the business's public name for it, states what a caller may send, and holds what the act requires and a caller must not | S4 gap_register GAP-02 |
| TE_REJECT_ACTOR_V0 | TE | States which kind of answer each ending of rejecting an actor takes, including the actor that does not exist, and what of the result the caller is told | S4 gap_register GAP-05 |

---

## 8. Cross-Subdomain References

<!-- register:cross_subdomain_refs optional business_language=role -->
| CC Code | Defined In | Role | Source Finding |
|---------|-----------|------|----------------|
| NONE IDENTIFIED | | | |

---

## gov_projection — Governed Handoff to Stage 6

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 4 | actors · bm_entities · events · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
| **Emits** → Stage 6 | subdomain_purpose · purpose_provenance · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
