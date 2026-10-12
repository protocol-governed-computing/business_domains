# Stage 2 — Domain Model Verification: blockchain / identity

## Machine

```yaml
document:
  phase: p2
  domain: blockchain
  subdomain: identity
  cr: cr_02_identity
  rule_set: transformation.schemas.REGISTER_SCHEMA_P2_V0
registers:
  entities:
  - entity: Offered Act
    description: An act the business has chosen to make reachable from outside, named by its business name.
    store_model: None — an offered act is declared, not stored. The composition declares eighteen such acts for reading a snapshot and one for a workload, and none for this business.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 2}
  - entity: Request
    description: 'What a caller sends: the name of the act they want, and the details that act needs.'
    store_model: None — a request is answered and not kept. Nothing in the composition retains one.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 2}
  - entity: Answer
    description: What the business tells a caller in reply to a request. Always one of three kinds.
    store_model: None — an answer is composed for one caller and not kept; the record of what happened is the occurrence the act itself writes.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 4}
  - entity: Carried Detail
    description: Something the person has just typed, held only to save them typing it again on the next page.
    store_model: None the business holds. It lives with whoever is filling in the form, and the business never reads it.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 31}
  - entity: Actor
    description: A person known to the system, whether or not the business has accepted them. Named here because the acts being reached are acts upon one; unchanged by this change.
    store_model: Already held. The composition declares a store for this business's actors and the occurrences recorded against them.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  entity_attributes:
  - entity: Offered Act
    attribute: Name
    meaning: The business's public word for the act, which outlives changes to how the act is performed.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 9}
  - entity: Request
    attribute: Act Named
    meaning: Which offered act the caller is asking for.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 7}
  - entity: Request
    attribute: Details Carried
    meaning: What the named act needs in order to run.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: business_vocabulary, row: 4}
  - entity: Answer
    attribute: Kind
    meaning: 'Which of the three the answer is: the act was done, it was turned away, or something went wrong inside the business.'
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 19}
  - entity: Answer
    attribute: Reason
    meaning: Why a request was turned away, and which details were the problem.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 17}
  - entity: Carried Detail
    attribute: Value
    meaning: The detail itself, as the person typed it.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 29}
  business_processes:
  - process: Reach an offered act from outside
    initiator: A caller — a person registering themselves, or an authority recording a decision
    outcome: The named act runs and the caller is told what happened, or the request is turned away and the caller is told which of the two reasons it was.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 3}
  - process: Show what the business offers
    initiator: A caller opening the front page
    outcome: All six blockchain functions are listed, with the four that are not built marked as not yet available.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 5}
  process_steps:
  - process: Reach an offered act from outside
    step: '1'
    action: Read which act the request names, and turn it away if the business does not offer it.
    record_produced: None — a turned-away request records nothing.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 5}
  - process: Reach an offered act from outside
    step: '2'
    action: Read the details the request carries against what the named act asks for, and turn it away if they cannot be read, saying which were the problem.
    record_produced: None.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 11}
  - process: Reach an offered act from outside
    step: '3'
    action: Pass the details to the act, judging nothing further.
    record_produced: None at this step; whatever the act records, it records.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: business_invariants, row: 6}
  - process: Reach an offered act from outside
    step: '4'
    action: Tell the caller which of the three kinds of answer it is, distinguishing a request that was turned away from one the business decided against.
    record_produced: None.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: business_invariants, row: 10}
  - process: Show what the business offers
    step: '1'
    action: List the six functions, marking wallet, transaction, block and consensus as not yet available.
    record_produced: None.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 38}
  belief_verification:
  - belief: The business author believes the identity function already exists, with both acts working.
    result: VERIFIED
    evidence: The pinned composition holds seventeen artifacts in the blockchain namespace, every one of them owned by the identity subdomain. Both acts are declared as workflows — blockchain::WF_REGISTER_ACTOR_V0 and blockchain::WF_RECORD_VERIFICATION_DECISION_V0 — over six capability contracts, three events, two intents, an actor declaration, a runtime binding and a storage structure. Executing blockchain::WF_REGISTER_ACTOR_V0 against the pinned snapshot with the domain's own registration payload returns a terminal status of SUCCESS and writes an occurrence at sequence number 1. The function exists and runs.
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - belief: The business author believes the platform already offers a way to be reached from outside, and that identity does not have one yet.
    result: VERIFIED
    evidence: The composition declares eighteen transport ingress artifacts and eighteen transport egress artifacts — seventeen pairs in the inspection namespace and one pair, workload::TI_COLLATZ_COMPUTE_V0 and workload::TE_COLLATZ_COMPUTE_V0, for the reference workload. Every one is a governed compiled artifact, so being reached from outside is an established shape and not a new one. None is in the blockchain namespace, and no artifact of that namespace is of either kind. Both halves of the belief hold.
    source_finding: {phase: p1, register: system_beliefs, row: 2}
  - belief: The business author believes the readability test defined by the previous change can be reused as it stands, rather than restated.
    result: VERIFIED
    evidence: blockchain::CC_VALIDATE_REGISTRATION_V0 confirms a registration carries a name and an address of the form asked for, over capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0. Both the record and the declaration it is read against are inputs to the contract rather than fixed within it, and it admits exactly two outcomes, SUCCESS and VIOLATION. The test is already the reusable form the business asked for; nothing about reaching it from outside requires a second one.
    source_finding: {phase: p1, register: system_beliefs, row: 3}
  - belief: The business author believes the platform can already distinguish a request it declines to begin from an act that ran and decided against the caller.
    result: INSUFFICIENT_EVIDENCE
    evidence: The mechanism to distinguish them exists and is not currently arranged to. The boundary answers a request naming an unoffered act with its own distinct class, separate from any the act could produce. But a request whose details cannot be read is answered with the same class as an act that ran and refused — the transport egress artifact of the reference workload maps the workflow's own refusal onto that same class. The two are distinguishable in the detail carried alongside the answer, where one names the fields at fault and the other names the act's status; they are not distinguishable in the kind of the answer itself. What the business requires is therefore achievable and is not achieved by the arrangement the composition currently exhibits.
    source_finding: {phase: p1, register: system_beliefs, row: 4}
  - belief: The business author believes the other five blockchain functions have nothing to offer from outside yet.
    result: VERIFIED
    evidence: Every one of the seventeen blockchain artifacts declares identity as its owning subdomain. No artifact of the composition belongs to a wallet, transaction, mempool, block, chain or consensus subdomain, in this namespace or any other. The front page marking the four as not yet available states what is true of the composition.
    source_finding: {phase: p1, register: system_beliefs, row: 5}
  pps_baseline_fqdns:
  - capability: Admitting a person
    fqdn: blockchain::WF_REGISTER_ACTOR_V0
    what_it_does: The governed sequence that admits a person as an unverified actor, reading the registration, claiming the contact address, registering the actor and appending the occurrence.
    fit: EXACT
    cannot_do: It is reachable only by a caller already inside the composition. It declares no public name of its own, and nothing about it says how a caller outside would name it.
  - capability: Recording a decision
    fqdn: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    what_it_does: The governed sequence that resolves the actor, records the authority's decision against it and appends the occurrence.
    fit: EXACT
    cannot_do: 'The same: no public name and no way in.'
  - capability: Reading a registration
    fqdn: blockchain::CC_VALIDATE_REGISTRATION_V0
    what_it_does: Confirms a registration carries a name and an address of the form asked for, taking both the record and the declaration it is read against as inputs.
    fit: EXACT
    cannot_do: It reads what it is given against what it is told to expect. It does not decide what to expect, so whatever supplies that declaration decides the test.
  - capability: Reading a record for absence and form
    fqdn: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    what_it_does: Reads a supplied record for fields the declaration requires and for the form they must take.
    fit: EXACT
    cannot_do: Nothing for this purpose. It is the mechanical test the business drew and judges nothing about belief.
  - capability: Admitting a request from outside
    fqdn: workload::TI_COLLATZ_COMPUTE_V0
    what_it_does: Declares a public name for an act, the details a caller may send, and the act that name is bound to, with a template mapping what the caller sent onto what the act needs.
    fit: EXACT
    cannot_do: It admits one act under one name. A family of acts sharing one way in is a matter of how names are bound to routes, not of this artifact.
  - capability: Answering a caller
    fqdn: workload::TE_COLLATZ_COMPUTE_V0
    what_it_does: Maps the act's terminal status onto the kind of answer the caller is told, projects the act's result into what is exposed, and exposes evidence by reference only.
    fit: PARTIAL
    cannot_do: It maps the act's own refusal onto the same kind of answer the boundary gives a request it could not read, so those two arrive alike.
  - capability: Admitting a family of acts under one name
    fqdn: inspection::TI_SI_CATALOG_V0
    what_it_does: One of seventeen ingress artifacts whose acts share a single way in, each act named in what the caller sends rather than by where they send it.
    fit: EXACT
    cannot_do: It is the shape the business asked for, proven at seventeen acts. Nothing about it is specific to reading a snapshot.
  - capability: Declaring this business's participant
    fqdn: blockchain::AC_PARTICIPANT_V0
    what_it_does: Declares the kind of party that performs identity's acts.
    fit: EXACT
    cannot_do: It declares who acts, not who may be reached from outside; nothing in the composition establishes that a caller is the party it claims to be.
  gaps:
  - gap: Neither identity act has a public name, so nothing a caller could ask for resolves to either of them.
    severity: CRITICAL
    impact: Both requested outcomes rest on a caller naming an act. Without a name there is nothing to offer and nothing to turn away.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 2}
  - gap: Nothing declares what a caller may send for either act, so there is no statement of what can and cannot be read.
    severity: CRITICAL
    impact: Turning a request away for details that cannot be read requires a declaration of what readable means at the boundary; the business has one for a registration and none for a request.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - gap: Both acts are declared to be given the rules that judge them, not only the details being judged.
    severity: CRITICAL
    impact: Admitting a person requires the declaration the registration is read against, where the address sits, what kind it is, which stream the occurrence belongs to and the occurrence's own fields; recording a decision likewise requires the states that admit a decision and the outcomes that are permitted. A caller outside the business cannot be asked for any of these, because supplying them is supplying the rules. Something between the caller and the act must hold them, or a business rule ends up in the web page.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: architectural_observations, row: 2}
  - gap: A request the business could not read and an act that ran and refused arrive as the same kind of answer.
    severity: CRITICAL
    impact: The business requires that being turned away and being decided against are never reported as the same answer. Nothing in the composition currently keeps them apart at the level of the answer's kind.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 4}
  - gap: Nothing lists the six functions or marks four of them as not yet available.
    severity: MAJOR
    impact: The front page is a requested outcome in its own right.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 5}
  - gap: Nothing carries a detail from one page to the next.
    severity: MINOR
    impact: A convenience the business asked for, on which nothing it does depends.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 29}
  - gap: Nothing establishes who a caller is.
    severity: MINOR
    impact: Deliberately so — the business states plainly that it does not check, and defers the check with the question of who may be an authority. Recorded because reaching the act from outside makes an unchecked claim easier to make.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: out_of_scope, row: 1}
  architectural_observations:
  - observation: The shape the business asked for — one way in, with the act named in what the caller sends — is already proven at seventeen acts.
    evidence: The inspection namespace declares seventeen ingress and seventeen egress artifacts whose acts share a single way in, the act being named in the request rather than by where it is sent. The reference workload's single act uses the other shape, one act to one place. Both are available; the business asked for the first.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 7}
  - observation: A public name and the act it reaches are separate things in the composition, which is what lets the name outlive the act.
    evidence: The reference workload's ingress artifact carries a public name and, separately, the workflow that name is bound to, with a template mapping what the caller sent onto what the act needs. Rebinding the name changes no caller.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 5}
  - observation: Both identity acts take their configuration through the same door as their data.
    evidence: blockchain::WF_REGISTER_ACTOR_V0 draws the registration record, the declaration it is validated against, the address path, the address type, the stream identifier and the occurrence fields all from the payload it is handed. blockchain::WF_RECORD_VERIFICATION_DECISION_V0 likewise draws the admitted outcomes and the states admitting a decision from its payload. In process this is invisible, because the caller is the business. From outside it is the whole difficulty.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: gaps, row: 3}
  - observation: The mapping between what a caller sends and what an act needs is declared, not written.
    evidence: The reference workload's ingress artifact carries a template that substitutes the caller's value into the act's payload, including literal structure the caller never sends. Configuration an act requires but a caller must not supply has a declared place to be held.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 5}
  - observation: The kind of answer a caller is told is declared by the business surface, and its projection onto any particular way of reaching it is not.
    evidence: The reference workload's egress artifact maps terminal statuses onto kinds of answer and states which kind an unlisted status takes. Where that kind is then rendered for one manner of access is settled outside the business's artifacts entirely.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 6}
  - observation: Identity already writes the evidence a caller would be told about, so being reached from outside adds no recording requirement.
    evidence: Executing the admitting act against the pinned snapshot writes an occurrence carrying the time it happened and returns the position at which it was written, without anything of this change present.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  discovery_concerns:
  - concern: Both identity acts declare their successful ending to be a refusal.
    evidence: blockchain::WF_REGISTER_ACTOR_V0 and blockchain::WF_RECORD_VERIFICATION_DECISION_V0 each declare two endings, one reached when the act succeeds and one when it refuses, and both are declared to carry the outcome VIOLATION. The successful ending of the only comparable workflow elsewhere in the composition, transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0, carries SUCCESS. Nothing currently reads the declared outcome — the terminal status is taken from the last step that ran, which is why executing the act returns SUCCESS and why this was never visible. It is a false statement sealed into two artifacts, and it becomes a wrong answer to a caller the moment anything classifies on what is declared rather than on what happened.
    severity: MAJOR
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - concern: The declaration a registration is read against is supplied by whoever calls the act, so the readability test is only as fixed as its caller.
    evidence: blockchain::CC_VALIDATE_REGISTRATION_V0 takes both the record and the declaration as inputs, and blockchain::WF_REGISTER_ACTOR_V0 draws that declaration from its payload. Two callers may hand the same act two different tests. The business requires one test, defined once.
    severity: MAJOR
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: gaps, row: 3}
  - concern: An act that refuses says only that it refused, not what it refused for.
    evidence: Both acts route every refusal — a registration that cannot be read, an address that could not be claimed, an actor that does not exist, an actor already decided about, an authority deciding about itself — to a single ending carrying a single outcome. A caller told that the business decided against them cannot be told which of those it was without something further being declared.
    severity: MAJOR
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 4}
  - concern: The other five functions are absent from the composition rather than declared as absent.
    evidence: No artifact declares that wallet, transaction, mempool, block, chain or consensus is planned and unbuilt. The front page's claim that four are not yet available is a statement the business makes on the page, which nothing in the composition confirms or contradicts.
    severity: MINOR
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  open_questions: null
```

Every belief the change request declared is resolved against the pinned composition, and every other
register projects from those resolutions. This change request is against a domain the composition
already holds: identity exists and both its acts execute, so the baseline here is prior behaviour
rather than mechanism alone, and what is missing is a way to reach it.

---

## 1. Business Entities

## 2. Business Processes

## 3. Belief Verification — THE SPINE

## 4. PPS Baseline — What Already Exists

## 5. Gap Analysis — What Is Missing

## 6. Architectural Observations

## 7. Discovery Concerns

## 8. Open Questions
