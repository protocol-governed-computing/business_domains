# Analysis Loop — webmail / mailbox

## Machine

```yaml
document:
  phase: p3
  domain: webmail
  subdomain: mailbox
  cr: cr_01_read_mail
  rule_set: transformation.schemas.REGISTER_SCHEMA_P3_V0
registers:
  analysis_findings:
  - question_id: 'S2 discovery_concerns #1'
    finding: The host reads a message without marking it, using the IMAP read that leaves the read state as it is. The provider changes the read state only when the host carries out a change the business decided.
    impact: Opening a message changes the mailbox only through the business's decision, which keeps every change one the business decided.
    evidence_status: INFERRED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: IMAP distinguishes a read that marks a message as seen from one that does not (BODY.PEEK); the host uses the second.
  - question_id: 'S2 discovery_concerns #2'
    finding: Mail content never enters an act. The host reports identifiers, read state and a message's structure, the parts it has and their kinds, and never a subject, a sender or text. The business answers with identifiers and decisions, and the host shows the person the content those decisions name.
    impact: No record entry, no event and no trace can hold mail content, because no act is ever handed any.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: protocol_runtime/runtime/scheduler.py returns the last contract's outputs as the act's answer and announces the same outputs as the event's payload, so an answer carrying content would carry it into the trace.
  - question_id: 'S2 architectural_observations #1'
    finding: Listing a folder is one call. The host reports the identifiers of a folder's messages in the order the provider received them, and the business chooses the page, newest received first; the host then shows the summaries of exactly those messages, in that order.
    impact: The business, not the host, decides which messages make a page, and the host never fetches a whole folder's summaries.
    evidence_status: INFERRED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: A folder's identifiers are cheap to ask a provider for; its summaries are not, and a large inbox holds thousands.
  verification_results:
  - item: No domain in the composition reads or changes a mailbox.
    origin: {phase: p2, register: belief_verification, row: 1}
    result: CONFIRMED
    evidence: si.artifact.list names no artifact concerning mail, a mailbox or IMAP.
  - item: The composition can keep a record that is only ever added to, with each entry kept as written.
    origin: {phase: p2, register: belief_verification, row: 2}
    result: CONFIRMED
    evidence: si.capability.surface shows capability_side_effects::CS_APPENDONLY_JSONL_V0 with APPEND, a write, and GET_ALL, a read.
  - item: The composition already has a way for a program outside it to report a result and receive a decision, one act per call.
    origin: {phase: p2, register: belief_verification, row: 3}
    result: CONFIRMED
    evidence: causal_language_model::WF_OFFER_NEXT_TOKENS_V0 starts at an intent its host calls and answers with the business's choice.
  dependency_discoveries:
  - dependency: capability_side_effects::CS_APPENDONLY_JSONL_V0
    type: Capability side effect
    disposition: REUSE
    evidence: Declared in the composition; the record appends to it.
  - dependency: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    type: Capability transform
    disposition: REUSE
    evidence: Declared in the composition; each record entry is assembled with it before it is appended.
  - dependency: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    type: Capability transform
    disposition: REUSE
    evidence: Declared in the composition; each act confirms with it that the provider answered.
  impact_analysis:
  - artifact: capability_side_effects::CS_APPENDONLY_JSONL_V0
    impact_scope: ai_governance, blockchain, book_library_mgmt, capability_side_effects, causal_language_model, surface_contract, transformation, workload
    consumer_count: '206'
    evidence: si.topology.impact impacted_count 206; reused as declared, so no consumer is affected
  - artifact: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    impact_scope: ai_governance, blockchain, book_library_mgmt, capability_transforms, causal_language_model, transformation
    consumer_count: '147'
    evidence: si.topology.impact impacted_count 147; reused as declared, so no consumer is affected
  - artifact: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    impact_scope: ai_governance, blockchain, book_library_mgmt, capability_transforms, causal_language_model
    consumer_count: '86'
    evidence: si.topology.impact impacted_count 86; reused as declared, so no consumer is affected
  authoring_decisions:
  - capability: Appendonly jsonl side effect, as the platform declares it
    decision: REUSE
    rationale: The record is only ever added to, which is what the side effect guarantees.
    alternatives_checked: capability_side_effects::CS_APPENDONLY_JSONL_V0 satisfies it as-is.
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 1}
  - capability: Assemble record transform, as the platform declares it
    decision: REUSE
    rationale: A record entry is a set of named values, which the transform assembles.
    alternatives_checked: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 satisfies it as-is.
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 2}
  - capability: Choose a folder's page
    decision: AUTHOR_NEW
    rationale: No transform orders identifiers newest first and cuts a page of 50 from them, saying whether more exist and whether the folder is empty.
    alternatives_checked: capability_transforms::CT_PURE_SELECT_RECORDS_V0 selects by field and neither orders nor pages.
    source_finding: {phase: p2, register: gaps, row: 2}
  - capability: Choose a message's text
    decision: AUTHOR_NEW
    rationale: No transform chooses, from a message's parts, the plain-text part to show, or says its text cannot be displayed.
    alternatives_checked: capability_transforms::CT_PURE_SELECT_RECORDS_V0 selects records by field and does not choose one part by kind.
    source_finding: {phase: p2, register: gaps, row: 2}
  - capability: Decide a change of read state
    decision: AUTHOR_NEW
    rationale: No transform decides whether a message becomes read, becomes unread or stays as it is.
    alternatives_checked: capability_transforms::CT_PURE_COMPARE_EQUAL_V0 answers equality and decides no change.
    source_finding: {phase: p2, register: gaps, row: 2}
  - capability: The acts a mail host calls
    decision: AUTHOR_NEW
    rationale: No act lists a folder, opens a message, marks a message or records a change's outcome.
    alternatives_checked: causal_language_model::WF_OFFER_NEXT_TOKENS_V0 is the pattern followed, and is about a model, not mail.
    source_finding: {phase: p2, register: gaps, row: 1}
  - capability: The mail host
    decision: AUTHOR_NEW
    rationale: No actor stands for a program that reaches a mail provider.
    alternatives_checked: causal_language_model::AC_MODEL_HOST_V0 stands for a model's host in another domain.
    source_finding: {phase: p2, register: gaps, row: 3}
  placement_decision:
  - decision: NEW_SUBDOMAIN
    subdomain: mailbox
    rationale: The webmail domain does not exist; mailbox is its first subdomain and owns the record.
    source_finding: {phase: p2, register: architectural_observations, row: 1}
  saturation:
  - criterion: No unresolved CRITICAL gaps
    status: SATISFIED
    evidence: Both CRITICAL gaps have authoring decisions; the acts and the transforms are authored by this change.
  - criterion: No open analyst questions
    status: SATISFIED
    evidence: P2 holds no open question, and both discovery concerns are closed above.
  - criterion: No dependency expansion in the last pass
    status: SATISFIED
    evidence: The design reuses 3 platform artifacts, each declared in the composition.
  - criterion: Verification pass complete, no OVERTURNED item unresolved
    status: SATISFIED
    evidence: 3 beliefs re-verified, none overturned.
  - criterion: Every INFERRED finding promoted, accepted or carried forward with a reason
    status: SATISFIED
    evidence: The two INFERRED findings rest on how IMAP reads a message and what a provider answers cheaply; they are carried forward to P5, which declares the acts on them.
```

Every finding cites the P2 row it resolves.
