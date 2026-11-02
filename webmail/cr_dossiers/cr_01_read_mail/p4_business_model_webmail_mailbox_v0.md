# Business Model — webmail / mailbox

## Machine

```yaml
document:
  phase: p4
  domain: webmail
  subdomain: mailbox
  cr: cr_01_read_mail
  rule_set: transformation.schemas.REGISTER_SCHEMA_P4_V0
registers:
  actors:
  - actor: Mail host
    role: Reports what the provider returned for a person's request, receives the business's decision, carries out the change decided and reports whether the provider accepted it
    authority_class: System
    source_finding: {phase: p2, register: business_processes, row: 1}
  bm_entities:
  - entity: Mailbox record
    description: The business's account of every request, what was decided and what the provider answered.
    store_model: One entry per request and per reported outcome, only ever added to, kept for each mailbox; no entry is changed or removed.
    source_finding: {phase: p2, register: entities, row: 1}
  - entity: Message
    description: One mail in a folder, with a sender, recipients, a subject, a date and its content.
    store_model: None. The provider keeps it; the business holds only what the host reports for one request, and keeps none of its content.
    source_finding: {phase: p2, register: entities, row: 2}
  - entity: Folder
    description: A named part of a mailbox, such as the inbox, holding messages.
    store_model: None. The provider keeps it; a request names it.
    source_finding: {phase: p2, register: entities, row: 3}
  resources:
  - resource: Mailbox record
    description: The business's account of every request, what was decided and what the provider answered.
    source_finding: {phase: p2, register: entities, row: 1}
  events:
  - event: Folder listed
    trigger: When a folder's page is shown to the person
    lifecycle_meaning: The record shows which folder the person was shown, and when.
    source_finding: {phase: p1, register: business_events, row: 1}
  - event: Message opened
    trigger: When a message is shown to the person
    lifecycle_meaning: The record shows which message was opened, and that it became read.
    source_finding: {phase: p1, register: business_events, row: 2}
  - event: Read state changed
    trigger: When the provider accepts a change to a message's read state
    lifecycle_meaning: The record shows the change the business decided and that the provider accepted it.
    source_finding: {phase: p1, register: business_events, row: 3}
  - event: Request refused
    trigger: When a request is refused
    lifecycle_meaning: The record shows which request was refused and why.
    source_finding: {phase: p1, register: business_events, row: 4}
  relationships:
  - subject: Folder
    verb: is identified by
    object: Name
    capability_need: Name the folder a request concerns
    source_finding: {phase: p1, register: identity_and_sameness, row: 1}
  - subject: Message
    verb: is identified by
    object: Identifier within its folder
    capability_need: Name the message a request concerns
    source_finding: {phase: p1, register: identity_and_sameness, row: 2}
  - subject: Mailbox record
    verb: identifies
    object: Message
    capability_need: Say which message a request concerned without copying its content
    source_finding: {phase: p1, register: business_invariants, row: 4}
  capability_graph:
  - capability: Appendonly jsonl side effect, as the platform declares it
    source_finding: {phase: p3, register: authoring_decisions, row: 1}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: Assemble record transform, as the platform declares it
    source_finding: {phase: p3, register: authoring_decisions, row: 2}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as the composition holds it.
  - capability: Choose a folder's page
    source_finding: {phase: p3, register: authoring_decisions, row: 3}
    status: CRITICAL
    gap_register_entry: GAP-01
    notes: No transform orders and pages a folder's identifiers.
  - capability: Choose a message's text
    source_finding: {phase: p3, register: authoring_decisions, row: 4}
    status: CRITICAL
    gap_register_entry: GAP-02
    notes: No transform chooses a message's plain-text part from its parts.
  - capability: Decide a change of read state
    source_finding: {phase: p3, register: authoring_decisions, row: 5}
    status: CRITICAL
    gap_register_entry: GAP-03
    notes: No transform decides a change of read state.
  - capability: The acts a mail host calls
    source_finding: {phase: p3, register: authoring_decisions, row: 6}
    status: CRITICAL
    gap_register_entry: GAP-04
    notes: No act lists a folder, opens a message, marks a message or records a change's outcome.
  - capability: The mail host
    source_finding: {phase: p3, register: authoring_decisions, row: 7}
    status: CRITICAL
    gap_register_entry: GAP-05
    notes: No actor stands for a program that reaches a mail provider.
  gap_register:
  - gap_code: GAP-01
    source_finding: {phase: p3, register: authoring_decisions, row: 3}
    capability: Choose a folder's page
    owner_subdomain: mailbox
    resolution: NEW
  - gap_code: GAP-02
    source_finding: {phase: p3, register: authoring_decisions, row: 4}
    capability: Choose a message's text
    owner_subdomain: mailbox
    resolution: NEW
  - gap_code: GAP-03
    source_finding: {phase: p3, register: authoring_decisions, row: 5}
    capability: Decide a change of read state
    owner_subdomain: mailbox
    resolution: NEW
  - gap_code: GAP-04
    source_finding: {phase: p3, register: authoring_decisions, row: 6}
    capability: The acts a mail host calls
    owner_subdomain: mailbox
    resolution: NEW
  - gap_code: GAP-05
    source_finding: {phase: p3, register: authoring_decisions, row: 7}
    capability: The mail host
    owner_subdomain: mailbox
    resolution: NEW
  authoring_scope:
  - capability: Choose a folder's page
    gap_register_ref: GAP-01
  - capability: Choose a message's text
    gap_register_ref: GAP-02
  - capability: Decide a change of read state
    gap_register_ref: GAP-03
  - capability: The acts a mail host calls
    gap_register_ref: GAP-04
  - capability: The mail host
    gap_register_ref: GAP-05
  dependency_graph:
  - from: webmail
    to: capability_side_effects::CS_APPENDONLY_JSONL_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 1}
  - from: webmail
    to: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 2}
  - from: webmail
    to: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 3}
  constraint_register:
  - number: '1'
    constraint: The business changes a mailbox only in a way the person asked for.
    source_finding: {phase: p1, register: business_invariants, row: 1}
    source: invariant
  - number: '2'
    constraint: Every change made to a mailbox is one the business decided.
    source_finding: {phase: p1, register: business_invariants, row: 2}
    source: invariant
  - number: '3'
    constraint: Every request, answered or refused, is in the record.
    source_finding: {phase: p1, register: business_invariants, row: 3}
    source: invariant
  - number: '4'
    constraint: No record holds a subject, a sender, message text or a credential.
    source_finding: {phase: p1, register: business_invariants, row: 4}
    source: invariant
  - number: '5'
    constraint: A refusal never shows a partial result as if it were complete.
    source_finding: {phase: p1, register: business_invariants, row: 5}
    source: invariant
  - number: '6'
    constraint: The mailbox is reached over IMAP with a password; other sign-in methods, such as OAuth, are out of this part.
    source_finding: {phase: p1, register: constraints, row: 1}
    source: constraint
  - number: '7'
    constraint: No connection to the provider is kept open between requests.
    source_finding: {phase: p1, register: constraints, row: 2}
    source: constraint
  design_decisions:
  - number: '1'
    decision: mailbox is a new subdomain of a new webmail domain, and owns the record.
    source_finding: {phase: p3, register: placement_decision, row: 1}
    rationale: The webmail domain does not exist.
    constraints_imposed: The record is the only thing the subdomain keeps.
  - number: '2'
    decision: The mail provider is reached by a host outside the composition; the host reports and carries out, and the business decides.
    source_finding: {phase: p2, register: architectural_observations, row: 1}
    rationale: A transform has no effects and a domain writes no side effect.
    constraints_imposed: Every act is called by the mail host, one act per call.
  - number: '3'
    decision: The host reads a message without marking it; the read state changes only through a change the business decided.
    source_finding: {phase: p3, register: analysis_findings, row: 1}
    rationale: Every change made to a mailbox is one the business decided.
    constraints_imposed: Opening a message answers with a decision the host must carry out and report.
  - number: '4'
    decision: No act is handed mail content. The host reports identifiers, read state and a message's structure; the business answers with identifiers and decisions; the host shows the content they name.
    source_finding: {phase: p3, register: analysis_findings, row: 2}
    rationale: No record holds a subject, a sender, message text or a credential.
    constraints_imposed: The record, every event and every answer carry identifiers, decisions and provider answers only.
  - number: '5'
    decision: Listing a folder is one call, in which the business chooses the page from the identifiers the host reports.
    source_finding: {phase: p3, register: analysis_findings, row: 3}
    rationale: The business, not the host, decides which messages make a page.
    constraints_imposed: The host shows the summaries of exactly the chosen identifiers, in the order chosen.
```

Consolidates P1 to P3; every row cites what it consolidates.
