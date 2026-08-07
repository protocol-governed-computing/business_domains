# Stage 5 — Business Intent: blockchain / identity

**Stage:** 5 — Business Intent
**CR:** cr_01_identity
**Status:** DRAFT
**Feeds:** Stage 6 — Governance Intent

---

## 1. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The Identity subdomain governs who an actor is and whether the business trusts them. It holds one
record for each person known to the system, the state that says whether the business has accepted
them, and the record of every moment in their history. It establishes the authority to say that a
person exists and that they are trusted — a person is an actor because identity says so, and is
trusted because identity records an authority's decision to that effect. It manages the actor's
lifecycle from admission through the single decision made about them, and it records every
occurrence so that the business can afterwards show who registered, who decided, what was decided
and on what grounds. It exists because the business must admit people before it knows anything about
them and decide afterwards whether to trust them, and those are two acts by two parties at two
times. It does not govern what a trusted actor may then do, which persons may be an authority, or
anything an actor's conduct might later change.

<!-- register:purpose_provenance business_language=refinement -->
| Source | Disposition (INHERITED, REFINED) | Refinement |
|--------|----------------------------------|------------|
| CR seed §0 Subdomain Purpose | REFINED | The seed states why the subdomain exists — that admission and trust are separate acts by separate parties. This states the subdomain that results: the records it holds, the authority it establishes over who exists and who is trusted, the lifecycle it manages, and the three things it does not govern. Nothing here contradicts the seed; what it adds is the standing description rather than the reason for the change. |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| Declare the actors of this business | IN_SCOPE | One actor for the ordinary participant; the authority is not one. | S4 authoring_scope GAP-02 |
| Declare the stores identity owns | IN_SCOPE | Three: the actor and its state, the address registry, the trail. | S4 authoring_scope GAP-03 |
| Bind identity's workflows to the stores they use | IN_SCOPE | Without it the workflows cannot reach the stores they declare. | S4 authoring_scope GAP-04 |
| Recognise the moments an actor is registered, accepted and rejected | IN_SCOPE | Three distinct occurrences. | S4 authoring_scope GAP-05 |
| Record an acceptance and a rejection | IN_SCOPE | Two records, not one carrying an outcome field. | S4 authoring_scope GAP-06 |
| Admit a person's registration and record them unverified | IN_SCOPE | The first business operation. | S4 authoring_scope GAP-07 |
| Record an authority's decision against a registered actor | IN_SCOPE | The second business operation, carrying every declared refusal. | S4 authoring_scope GAP-08 |
| Admit a request to register a person | IN_SCOPE | The boundary registration is reached through. | S4 authoring_scope GAP-09 |
| Admit a request to record a verification decision | IN_SCOPE | A distinct admission surface from registration's. | S4 authoring_scope GAP-10 |
| Determine the time an occurrence happened | DEFERRED | Owned by the substrate. A prerequisite of this change and not a part of it — a business subdomain may not author a neutral capability. | S4 authoring_scope Determine the time an occurrence happened |
| Re-application by a rejected actor | DEFERRED | Deferred by the business until this change states what a rejection means. | S4 authoring_scope Re-application by a rejected actor |
| Revocation of an accepted actor | DEFERRED | Deferred by the business to a governed change of its own. | S4 authoring_scope Revocation of an accepted actor |
| Governing which persons may be an authority | DEFERRED | Identity records the name and does not resolve it. | S4 authoring_scope Governing which persons may be an authority |
| Holding the material an authority examined | DEFERRED | Deferred with its retention and privacy consequences. | S4 authoring_scope Holding the material an authority examined |
| Correcting an actor's own details after registration | DEFERRED | Deferred until a verification decision is defined. | S4 authoring_scope Correcting an actor's own details after registration |

---

## 3. Business Objects

<!-- register:business_objects optional business_language=store_name,business_rationale -->
| Store Name | Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID) | Business Rationale | Source Finding |
|------------|------------------------------------------------------------------------------|--------------------|----------------|
| Actor record | MUTABLE_STATE | The business needs one place that says which people it knows and whether each is trusted; the state changes once, in place, when a decision is recorded | S4 bm_entities Actor |
| Contact address registry | IDENTITY_REGISTRY | Two registrations carrying the same address must not produce two actors, and only an atomic claim can guarantee that | S4 bm_entities Contact Address |
| Actor occurrence trail | APPEND_ONLY_JOURNAL | An occurrence that has happened cannot be un-happened, so its record is never amended and never removed | S4 bm_entities Occurrence |

---

## 4. Identity Semantics

<!-- register:identity_semantics business_language=identity_field,source,uniqueness_rule,cross_subdomain_relationship -->
| Store Name | Identity Field | Source | Uniqueness Rule | Cross-Subdomain Relationship | Source Finding |
|------------|----------------|--------|-----------------|------------------------------|----------------|
| Actor record | Contact address | Supplied by the person registering themselves | Two registrations carrying the same address describe the same person, and the second neither creates another actor nor is refused | None — the actor is named by later subdomains and names none | S1 identity_and_sameness #1 |
| Contact address registry | The contact address as supplied | Supplied by the person registering themselves | The address is claimed once; a second claim on it resolves to the actor already admitted rather than refusing | None | S4 design_decisions #3 |
| Actor occurrence trail | Append position | Assigned when the occurrence is appended | Each occurrence appends exactly one entry, and no entry is amended or removed | Names the actor the occurrence was recorded against, and the authority when there is one | S4 bm_entities Occurrence |

---

## 5. Business Invariants

<!-- register:invariants business_language=invariant,business_reason -->
| Invariant | Business Reason | Source Finding |
|-----------|-----------------|----------------|
| An actor is identified by exactly one contact address, and two actors never share one | The address is what makes two registrations the same person; if two actors could share one, the business could not say who it had admitted | S1 business_invariants Two actors never share a contact address |
| An actor is unverified, accepted or rejected, and never more than one at a time | The business would rather say it has not decided than imply a decision it has not made | S1 business_invariants An actor is either unverified, accepted or rejected |
| An actor that has not been decided about is unverified | There is no fourth state and no absence of state; an actor with no decision is one the business has recorded and not accepted | S1 business_invariants An actor that has not been decided about is unverified |
| A decision exists only against a registration that exists | Without a registration it is not an incomplete decision but a meaningless one | S1 business_invariants A verification decision exists only against a registration that exists |
| An actor is decided about once, and is never accepted and rejected both | Trust is given or withheld once; revisiting it is a governed change the business deferred | S1 business_invariants An actor is decided about once |
| Every decision names the authority that made it | A decision whose author is unknown is not evidence | S1 business_invariants A verification decision names the authority that made it |
| A rejection states grounds | The grounds are the substance of a rejection, and a rejection without them cannot be reviewed | S1 business_invariants A rejection states grounds |
| A person never makes the decision about themselves | Trust the subject grants itself is not trust the business has extended | S1 business_invariants A person never makes the verification decision about themselves |
| Neither an unverified nor a rejected actor is trusted with anything | The whole change turns on an unverified actor being a distinct thing rather than a label on an ordinary one | S1 business_invariants Neither an unverified nor a rejected actor is trusted |
| Every recorded occurrence carries the time it occurred | A record whose times do not advance is regarded by the business as no record at all | S1 business_invariants Every recorded occurrence carries the time it occurred |
| No recorded occurrence is altered or removed once written | A correction is a further occurrence stating the correction, never an edit of what was written | S1 business_invariants No recorded occurrence is altered or removed |

---

## 6. Business Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| Register | A person, admitted as an unverified actor | A person supplies their own identifying details | IN_SCOPE | S4 capability_graph Admit a person's registration and record them unverified |
| Register | A person already known, recorded as a further occurrence | A person who has registered before supplies their details again | IN_SCOPE | S4 capability_graph Admit a person's registration and record them unverified |
| Decide | A registered actor, accepted or rejected | An authority records a decision against a registered actor | IN_SCOPE | S4 capability_graph Record an authority's decision against a registered actor |
| Reapply | A rejected actor seeking a further decision | A rejected person asks the business to consider them again | DEFERRED | S4 authoring_scope Re-application by a rejected actor |
| Revoke | An accepted actor whose trust is withdrawn | The business withdraws trust it has given | DEFERRED | S4 authoring_scope Revocation of an accepted actor |
| Correct | An actor's own registered details | A person's name or address changes after admission | DEFERRED | S4 authoring_scope Correcting an actor's own details after registration |

---

## 7. Provisional Artifact Codes

<!-- register:provisional_codes business_language=summary -->
| Provisional Code | Family (AC, IN, WF, CC, CT, EV, RB, STRUCTURE) | Summary | Source Finding |
|------------------|-------------------------|---------|----------------|
| AC_PARTICIPANT_V0 | AC | The ordinary participant who registers themselves and is decided about | S4 gap_register GAP-02 |
| STRUCTURE_IDENTITY_STORAGE_V0 | STRUCTURE | Declares the three stores identity owns and what each holds | S4 gap_register GAP-03 |
| RB_IDENTITY_BINDINGS_V0 | RB | Binds identity's workflows to the stores they use | S4 gap_register GAP-04 |
| EV_ACTOR_REGISTERED_UNVERIFIED_V0 | EV | The moment a person is admitted and trusted with nothing | S4 gap_register GAP-05 |
| EV_ACTOR_ACCEPTED_V0 | EV | The moment an authority records a decision to trust an actor | S4 gap_register GAP-05 |
| EV_ACTOR_REJECTED_V0 | EV | The moment an authority records a decision not to trust an actor, distinct in kind from an acceptance | S4 gap_register GAP-05 |
| CC_CLAIM_CONTACT_ADDRESS_V0 | CC | Claims a contact address so that two registrations of one person do not produce two actors | S4 gap_register GAP-07 |
| CC_RESOLVE_ACTOR_V0 | CC | Answers which actor a contact address denotes, and reports when none does | S4 gap_register GAP-08 |
| CC_VALIDATE_REGISTRATION_V0 | CC | Confirms a registration carries a name and an address, and that the address is of the form asked for | S4 gap_register GAP-07 |
| CC_REGISTER_ACTOR_V0 | CC | Claims the address, writes the actor unverified, and records the occurrence | S4 gap_register GAP-07 |
| CC_RECORD_VERIFICATION_DECISION_V0 | CC | Resolves the actor, refuses every declared refusal, moves the state and records the occurrence | S4 gap_register GAP-08 |
| CC_APPEND_ACTOR_OCCURRENCE_V0 | CC | Appends one occurrence to the trail, carrying the time it happened | S4 gap_register GAP-06 |
| WF_REGISTER_ACTOR_V0 | WF | The governed sequence that admits a person as an unverified actor | S5 actions Register |
| WF_RECORD_VERIFICATION_DECISION_V0 | WF | The governed sequence that records an authority's decision against a registered actor | S5 actions Decide |
| IN_REGISTER_ACTOR_V0 | IN | A request to admit a person as an actor | S4 gap_register GAP-09 |
| IN_RECORD_VERIFICATION_DECISION_V0 | IN | A request to record a decision, carrying the authority, the outcome and the grounds | S4 gap_register GAP-10 |

---

## 8. Cross-Subdomain References

<!-- register:cross_subdomain_refs optional business_language=role -->
| CC Code | Defined In | Role | Source Finding |
|---------|------------|------|----------------|
| NONE IDENTIFIED |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 4 — Business Model | p4_business_model_blockchain_identity_v0.md | COMPLETE |
| Stage 5 — Business Intent | This document | COMPLETE |
| Stage 6 — Governance Intent | Pending | — |

---

## gov_projection — Governed Handoff to Stage 6

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 4 | actors · bm_entities · events · capability_graph · gap_register · design_decisions · authoring_scope |
| **Emits** → Stage 6 | subdomain_purpose · purpose_provenance · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
