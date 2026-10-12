# Stage 3 — Analysis Loop: blockchain / identity

## Machine

```yaml
document:
  phase: p3
  domain: blockchain
  subdomain: identity
  cr: cr_02_identity
  rule_set: transformation.schemas.REGISTER_SCHEMA_P3_V0
registers:
  analysis_findings:
  - question_id: Q1
    finding: The business asked for one way in with the act named in the request, and that shape is already proven in the composition at seventeen acts. The inspection namespace binds seventeen acts to a single place, the act being named in what the caller sends; the reference workload binds its one act to a place of its own. Both are supported by the same boundary, and which is used is a property of how names are bound, not of any artifact this change authors.
    impact: The two identity acts share one way in. Adding the remaining five functions later adds names, not places, which is what the business asked for when it declined to hand callers a new address for every act.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: The composition declares eighteen transport ingress and eighteen transport egress artifacts; seventeen ingress artifacts of the inspection namespace share one way in, and workload::TI_COLLATZ_COMPUTE_V0 does not
  - question_id: Q2
    finding: A public name and the act it reaches are separate declarations, which is what allows the name to outlive the act. workload::TI_COLLATZ_COMPUTE_V0 carries the public name, and separately the workflow that name is bound to, stating in terms that the bound workflow is an implementation detail that may be re-pointed.
    impact: The two names this change introduces are the business's own words for its acts, and neither is a workflow's name. Re-pointing either act later changes no caller.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: workload::TI_COLLATZ_COMPUTE_V0 declares an operation identity and a separately declared handler naming workload::WF_COLLATZ_CONJECTURE_V0
  - question_id: Q3
    finding: Both identity acts are handed their own configuration through the same door as the caller's data. Admitting a person requires the declaration the registration is read against, where the address sits, what kind it is, the stream the occurrence belongs to and the occurrence's own fields; recording a decision additionally requires the states that admit a decision and the outcomes permitted. Only the person's details and the authority's decision belong to a caller.
    impact: A caller cannot be asked for any of it, because supplying the declaration a registration is read against is supplying the test. Something between the caller and the act must hold it.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: blockchain::WF_REGISTER_ACTOR_V0 draws actor_record, registration_schema, address_path, address_type, stream_id and occurrence_fields from its payload; blockchain::WF_RECORD_VERIFICATION_DECISION_V0 additionally draws states_admitting_a_decision, admitted_outcomes and decided_actor_fields
  - question_id: Q4
    finding: The ingress declaration holds that configuration. Its template maps what a caller sends onto what the act needs, substituting only the caller's own values and passing every other value through as written, including whole nested structures the caller never sends. The reference workload already relies on this, wrapping a caller's single number in a list the caller does not supply.
    impact: The rules an act needs but a caller must not send are declared in a compiled artifact sealed into the snapshot. They are held once, where a change to them is a governed change, and never in the web page.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: workload::TI_COLLATZ_COMPUTE_V0 declares a payload template substituting the caller's value into a literal list structure; the boundary substitutes only declared input keys and fails rather than forwarding an undeclared one
  - question_id: Q5
    finding: Holding the configuration at the boundary is the right decision for this change and the wrong place for it in the long run. The alternative — the workflows drawing their configuration from a declared structure of their own — is better placement, because the rules would sit with the function that owns them rather than with the door it is reached through. It reopens two sealed workflows, which this change states it does not do.
    impact: The configuration is held in the ingress declarations now, and moving it into the domain is recorded as a change of its own. Both acts keep working unchanged in the meantime.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'S1 out_of_scope #3 states this change revisits no decision the previous change made; blockchain::WF_REGISTER_ACTOR_V0 and blockchain::WF_RECORD_VERIFICATION_DECISION_V0 would both require amendment under the alternative'
  - question_id: Q6
    finding: The readability test the business requires is already the reusable form, and reaching it from outside requires a second statement of it rather than a second test. The act's own contract takes both the record and the declaration it is read against as inputs, so the declaration held at the boundary is the same declaration the act applies. What the boundary states about a caller's request must agree with it.
    impact: One test, stated at the boundary as what a caller may send and applied by the act as the declaration it validates against. The business's refusal to have two tests is honoured by both statements naming the same fields.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: blockchain::CC_VALIDATE_REGISTRATION_V0 runs capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 over a record and a schema, both supplied as inputs
  - question_id: Q7
    finding: Three of the four refusals the business names are already distinguishable at the boundary. An act the business does not offer is refused by the boundary before any act is reached and carries its own class. An actor that does not exist is answered by the act and carries the class for a subject that is absent. A request whose details cannot be read is refused at the door. The classes are a closed governed set of six.
    impact: Only one pair collides, and the other refusals need nothing authored to keep them apart.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: transport::CONSTITUTION_TRANSPORT_EGRESS_V0 declares the closed set SUCCESS, VIOLATION, UNAUTHORIZED, NOT_FOUND, OPERATION_NOT_FOUND and EXECUTION_FAILURE, and requires that a subject absent and an act not offered are never conflated; executing blockchain::WF_RECORD_VERIFICATION_DECISION_V0 against an unregistered actor returns NOT_FOUND
  - question_id: Q8
    finding: 'The remaining pair collides in the kind of the answer and differs in its detail. A request whose details cannot be read and an act that ran and refused both carry the class for a violation. What the caller receives is not identical: the first names the fields at fault, the second reports the act''s own status. The business requires that the two are never reported as the same answer, which two answers differing in what they state satisfy; it does not require a distinct kind, and the governed set has no kind to give.'
    impact: The requirement is met by what the answer states. That the two share a kind is recorded as a concern, and a class for an act that ran and refused is named as a change to the platform's governed set, which this change does not make.
    evidence_status: OBSERVED
    confidence: MEDIUM
    resolution_status: CLOSED
    evidence: The boundary refuses an unreadable request with the offending fields named, and reports an act's refusal as its terminal status; executing blockchain::WF_RECORD_VERIFICATION_DECISION_V0 against an actor already decided about returns VIOLATION, as does a registration missing its address
  - question_id: Q9
    finding: An act that refuses says that it refused and not what it refused for. Every refusal in both acts — a registration that cannot be read, an address that could not be claimed, an actor that does not exist, an actor already decided about, an authority deciding about itself — reaches a single ending. A caller told the business refused cannot be told which refusal it was.
    impact: Within this change the caller is told that the act refused. Telling them which refusal requires the acts to distinguish their endings, which is an amendment to sealed workflows and belongs with the placement change recorded in Q5.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: Both workflows route every refusing outcome to one ending; executing the deciding act against a self-verifying authority returns NOT_FOUND rather than a refusal naming self-verification
  - question_id: Q10
    finding: 'The events this business named are declared and cannot fire. Three event artifacts exist for the moments an actor is registered, accepted and rejected, and neither act reaches them: the ending that would announce a moment carries a field the platform does not read, and does not carry the field it does. Every domain authored through the pipeline shows this and every hand-authored domain does not.'
    impact: Nothing in this change depends on an event firing — the caller is answered from the act's own result, and the trail of occurrences is written by the acts themselves. The defect is in construction rather than in either domain, and is named as a change against the pipeline.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: blockchain declares three event artifacts and book_library_mgmt six, and no workflow of either domain announces one; ai_governance and workload announce theirs from the ending reached; a trace of blockchain::WF_REGISTER_ACTOR_V0 records the act's steps and no event
  - question_id: Q11
    finding: The front page and the two forms are not artifacts of the composition and are not governed by it. What the business offers is declared in the composition; what a page shows about it is not. Marking four functions as not yet available is a statement the pages make, which nothing in the composition confirms or contradicts.
    impact: The pages are built and are held to the business's constraints — no rule, no check before sending, carrying only what the person typed — by the acceptance criteria rather than by a compiled artifact.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'No artifact of the composition declares a web page; S1 acceptance_criteria #11 and #14 state the tests that hold the page thin'
  verification_results:
  - item: The business author believes the identity function already exists, with both acts working.
    origin: {phase: p2, register: belief_verification, row: 1}
    result: CONFIRMED
    evidence: Seventeen artifacts in the blockchain namespace, all owned by identity; executing blockchain::WF_REGISTER_ACTOR_V0 against the pinned snapshot returns SUCCESS and writes an occurrence
  - item: The business author believes the platform already offers a way to be reached from outside, and that identity does not have one yet.
    origin: {phase: p2, register: belief_verification, row: 2}
    result: CONFIRMED
    evidence: Eighteen ingress and eighteen egress artifacts, none in the blockchain namespace
  - item: The business author believes the readability test defined by the previous change can be reused as it stands, rather than restated.
    origin: {phase: p2, register: belief_verification, row: 3}
    result: CONFIRMED
    evidence: blockchain::CC_VALIDATE_REGISTRATION_V0 takes the record and the declaration as inputs and applies capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
  - item: The business author believes the platform can already distinguish a request it declines to begin from an act that ran and decided against the caller.
    origin: {phase: p2, register: belief_verification, row: 4}
    result: CONFIRMED
    evidence: 'Resolved in Q7 and Q8: three of the four refusals carry distinct governed classes, and the remaining pair differs in what the answer states while sharing its kind'
  - item: The business author believes the other five blockchain functions have nothing to offer from outside yet.
    origin: {phase: p2, register: belief_verification, row: 5}
    result: CONFIRMED
    evidence: Every blockchain artifact declares identity as its owning subdomain
  - item: Both acts declare their successful ending to be a refusal
    origin: {phase: p2, register: discovery_concerns, row: 1}
    result: CONFIRMED
    evidence: 'Resolved in Q10 and shown to be inert: the field is read by nothing, and the same ending fails to carry the field that is read'
  - item: The declaration a registration is read against is supplied by its caller
    origin: {phase: p2, register: discovery_concerns, row: 2}
    result: CONFIRMED
    evidence: 'Resolved in Q3 and Q4: the declaration is held in the ingress artifact, so one caller supplies it and it is sealed'
  - item: An act that refuses does not say what it refused for
    origin: {phase: p2, register: discovery_concerns, row: 3}
    result: CONFIRMED
    evidence: Resolved in Q9 and carried forward with the placement change in Q5
  - item: The five unbuilt functions are absent rather than declared absent
    origin: {phase: p2, register: discovery_concerns, row: 4}
    result: CONFIRMED
    evidence: 'Resolved in Q11: what a page shows is not governed by the composition'
  dependency_discoveries:
  - dependency: The boundary's ingress and egress kinds
    type: Governed artifact kind
    disposition: EXISTING
    evidence: transport::CONSTITUTION_TRANSPORT_INGRESS_V0 and transport::CONSTITUTION_TRANSPORT_EGRESS_V0 govern them, and thirty-six compiled artifacts of those kinds are sealed in the composition
  - dependency: The act that admits a person
    type: Workflow
    disposition: REUSE
    evidence: blockchain::WF_REGISTER_ACTOR_V0, unchanged; impacted by nothing in the composition
  - dependency: The act that records a decision
    type: Workflow
    disposition: REUSE
    evidence: blockchain::WF_RECORD_VERIFICATION_DECISION_V0, unchanged; impacted by nothing in the composition
  - dependency: Reading a record for absence and form
    type: Capability transform
    disposition: REUSE
    evidence: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0, impacted by 31 artifacts, reached through blockchain::CC_VALIDATE_REGISTRATION_V0
  - dependency: The name a caller uses for an act
    type: Governed declaration
    disposition: AUTHOR_NEW
    evidence: No artifact of the blockchain namespace declares a public name for either act
  - dependency: What a caller may send, and what the act is handed
    type: Governed declaration
    disposition: AUTHOR_NEW
    evidence: The same; the configuration held here is drawn from the acts' own declared payloads
  - dependency: The kinds of answer a caller is told
    type: Governed declaration
    disposition: AUTHOR_NEW
    evidence: The same; the closed set of classes is governed and is not extended by this change
  - dependency: A source layer for the boundary declarations
    type: Build manifest
    disposition: AUTHOR_NEW
    evidence: blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 already admits both kinds among its artifact types and declares one source layer; the workload manifest declares a separate transport layer and a second identity rule alongside its registry layer
  - dependency: The table binding a place to a name
    type: Adapter configuration
    disposition: REUSE
    evidence: The binding table is data the adapter is pointed at, not an artifact of the composition; the inspection surface and the reference workload each carry one
  - dependency: The web pages
    type: Client
    disposition: AUTHOR_NEW
    evidence: No artifact of the composition declares one; the legacy pages of the prior implementation are lifted one way and depend on nothing in it
  - dependency: Announcing the moments an actor is registered, accepted and rejected
    type: Domain event
    disposition: INVESTIGATE
    evidence: Three event artifacts exist and cannot fire; the cause is in construction and is carried as a change of its own, on which nothing in this one depends
  - dependency: Establishing who a caller is
    type: Governed declaration
    disposition: INVESTIGATE
    evidence: Deferred by the business with the question of who may be an authority; nothing in the composition establishes a caller's identity
  impact_analysis:
  - artifact: blockchain::WF_REGISTER_ACTOR_V0
    impact_scope: Named by a new boundary declaration; not amended
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    impact_scope: Named by a new boundary declaration; not amended
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: blockchain::CC_VALIDATE_REGISTRATION_V0
    impact_scope: Reached unchanged through the act; the declaration it validates against is now held at the boundary
    consumer_count: '2'
    evidence: si.topology.impact impacted_count 2
  - artifact: blockchain::AC_PARTICIPANT_V0
    impact_scope: Reused unchanged; a caller from outside is not established as this or any actor
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    impact_scope: Reused unchanged
    consumer_count: '31'
    evidence: si.topology.impact impacted_count 31
  - artifact: workload::TI_COLLATZ_COMPUTE_V0
    impact_scope: Not changed; read as the precedent for a public name, a caller's declared input and a template holding what a caller does not send
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: workload::TE_COLLATZ_COMPUTE_V0
    impact_scope: Not changed; read as the precedent for classifying an act's outcome and exposing evidence by reference
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: transport::CONSTITUTION_TRANSPORT_INGRESS_V0
    impact_scope: Governs the new declarations; not amended
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: transport::CONSTITUTION_TRANSPORT_EGRESS_V0
    impact_scope: Governs the new declarations; not amended, and its closed set of classes is not extended
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0
    impact_scope: Amended to declare where the boundary declarations are found
    consumer_count: '0'
    evidence: It already admits both kinds among its artifact types while declaring no layer they could be found in
  authoring_decisions:
  - capability: Admit a person's registration
    decision: REUSE
    rationale: The act exists, runs and is unchanged by this change. Only the way in is new.
    alternatives_checked: 'Amending it to take its configuration from a declared structure of its own was checked and deferred in Q5: it is better placement and it reopens a sealed act.'
    source_finding: {phase: p3, register: analysis_findings, key: Q5}
  - capability: Record an authority's decision
    decision: REUSE
    rationale: The same.
    alternatives_checked: The same.
    source_finding: {phase: p3, register: analysis_findings, key: Q5}
  - capability: Read a registration for absent or malformed details
    decision: REUSE
    rationale: The business refuses to have two tests, and the one it has takes the declaration it applies as an input, so it is already the reusable form.
    alternatives_checked: 'Restating the test at the boundary as a second test was checked and rejected: two tests for one question is how they come to disagree.'
    source_finding: {phase: p3, register: analysis_findings, key: Q6}
  - capability: Offer registering an actor to a caller outside the business
    decision: AUTHOR_NEW
    rationale: The act has no public name, so nothing a caller could ask for reaches it. The name is the business's own word for the act and is declared apart from the act it reaches.
    alternatives_checked: 'Naming the act by the workflow that performs it was checked and rejected: it would bind every caller to an implementation the business intends to be free to change.'
    source_finding: {phase: p3, register: analysis_findings, key: Q2}
  - capability: Offer recording a verification decision to a caller outside the business
    decision: AUTHOR_NEW
    rationale: The second act, needing its own name because what a caller may send differs entirely from registration.
    alternatives_checked: 'Sharing one name with registration was checked and rejected: the two carry different required values and would need the caller to say which they meant.'
    source_finding: {phase: p3, register: analysis_findings, key: Q2}
  - capability: Hold what an act requires and a caller must not send
    decision: AUTHOR_NEW
    rationale: The acts are handed their own rules through the same door as the caller's data. Held in the declaration that admits the request, they are sealed in the snapshot and stated once.
    alternatives_checked: Asking the caller for them was checked and rejected — it is supplying the rules that judge you. Holding them in the web page was checked and rejected by the business outright.
    source_finding: {phase: p3, register: analysis_findings, key: Q4}
  - capability: Tell a caller how their registration ended
    decision: AUTHOR_NEW
    rationale: The kinds of answer are governed and closed, and which of them each ending takes is declared per act.
    alternatives_checked: 'Leaving the act''s result to be shown as it stands was checked and rejected: it exposes what the act holds rather than what the business exposes.'
    source_finding: {phase: p3, register: analysis_findings, key: Q7}
  - capability: Tell a caller how their decision ended
    decision: AUTHOR_NEW
    rationale: The same, over the endings that act reaches, including the absent actor which is already a distinct kind.
    alternatives_checked: 'Sharing one statement of answers with registration was checked and rejected: the two acts end differently.'
    source_finding: {phase: p3, register: analysis_findings, key: Q7}
  - capability: Offer both acts through one way in
    decision: REUSE
    rationale: The business asked for one way in with the act named in the request, and seventeen acts already share one. What binds a place to a name is configuration the boundary is pointed at, not an artifact.
    alternatives_checked: A place for each act was checked and rejected against the business's statement that it will add many acts and will not hand callers a new address for each.
    source_finding: {phase: p3, register: analysis_findings, key: Q1}
  - capability: Declare where the boundary declarations are found
    decision: EXTEND
    rationale: The domain's build manifest already admits both kinds while declaring no place they could be found. The worked precedent declares a second source layer beside the registry one.
    alternatives_checked: Placing them among the domain's existing artifacts was checked; the precedent keeps them apart, and keeping them apart makes what is reachable from outside legible at a glance.
    source_finding: {phase: p3, register: dependency_discoveries, row: 8}
  - capability: Show a person a form and its answer
    decision: AUTHOR_NEW
    rationale: Two forms and a front page. The pages are lifted from the prior implementation, which harvests what is typed and renders what comes back without knowing any schema.
    alternatives_checked: 'Building them new was checked and rejected: the existing pages already hold no rules, which is the constraint the business cares about. What they say to the platform is replaced, because they name an act''s implementation and read an envelope this platform does not produce.'
    source_finding: {phase: p3, register: analysis_findings, key: Q11}
  - capability: Carry a detail from one page to the next
    decision: AUTHOR_NEW
    rationale: A convenience the business asked for, holding only what the person just typed.
    alternatives_checked: Holding nothing was checked; the business chose the convenience and bounded it so that nothing the business does depends on it.
    source_finding: {phase: p3, register: analysis_findings, key: Q11}
  - capability: Show the functions the business has not built
    decision: AUTHOR_NEW
    rationale: Four of six functions are named and marked not yet available, so a caller sees what is coming instead of something that fails.
    alternatives_checked: Omitting them was checked and rejected against the business's statement of what the front page shows.
    source_finding: {phase: p3, register: analysis_findings, key: Q11}
  - capability: Announce the moments an actor is registered, accepted and rejected
    decision: REUSE
    rationale: The three moments are already declared. That they cannot presently be announced is a defect in how artifacts are constructed, not in this domain, and nothing in this change depends on one being announced.
    alternatives_checked: 'Redeclaring them here was checked and rejected: they exist and are correct. Repairing construction was checked and placed outside this change, which authors no pipeline.'
    source_finding: {phase: p3, register: analysis_findings, key: Q10}
  placement_decision:
  - decision: EXTEND
    subdomain: identity
    rationale: The acts being offered are identity's own, and what is added says only how they are reached. A subdomain of its own would separate the name of an act from the act it names, leaving each half owned by a different part of the business. Every artifact of this domain already declares identity as its owner.
    source_finding: {phase: p3, register: analysis_findings, key: Q2}
  saturation:
  - criterion: No unresolved CRITICAL gaps
    status: SATISFIED
    evidence: 'The four CRITICAL gaps carried from Stage 2 each resolve to a committed decision: the missing public names and the missing statement of what a caller may send to AUTHOR_NEW in Q2, the configuration travelling as payload to the boundary declarations in Q4, and the colliding refusals to the reading settled in Q8 with the residual concern named'
  - criterion: No open analyst questions
    status: SATISFIED
    evidence: 'All eleven findings in this stage are CLOSED. The one business question this stage raised was put to the business author and answered before it ran: the configuration is held at the boundary rather than moved into the domain'
  - criterion: No dependency expansion in the last pass
    status: SATISFIED
    evidence: The twelve dependencies were established in one pass against the composition's transport surface, the domain's own artifacts and its build manifest; re-reading them surfaced only the manifest's missing source layer, which was already among them
  - criterion: Verification pass complete, no OVERTURNED item unresolved
    status: SATISFIED
    evidence: All nine items re-grounded and CONFIRMED, including the belief returned from Stage 2 as INSUFFICIENT_EVIDENCE, which Q7 and Q8 resolve, and all four Stage 2 discovery concerns
  - criterion: Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried forward with a reason
    status: SATISFIED
    evidence: Stage 2 carried no INFERRED row. Every finding in this stage is OBSERVED; Q8 alone is held at MEDIUM confidence, because it rests on a reading of what the business requires rather than on a governed class that expresses it
```

Each gap and concern carried from Stage 2 is driven to a committed decision against the pinned
composition. This change adds a way in to a function that already runs, so every question here is
about the boundary and none is about identity's behaviour, which is unchanged.

---

## 1. Analysis Findings

## 2. Verification Results

## 3. Dependency Discoveries

## 4. Impact Analysis

## 5. Authoring Decisions

## 6. Placement Decision

## 7. Saturation Assessment

---

## gov_projection — Governed Handoff to Stage 4

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 1 | cr_type · assumptions · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · constraints |
| **Consumes** ← Stage 2 | belief_verification · pps_baseline_fqdns · gaps · architectural_observations · discovery_concerns · open_questions |
| **Emits** → Stage 4 | authoring_decisions · dependency_discoveries · placement_decision · saturation |
