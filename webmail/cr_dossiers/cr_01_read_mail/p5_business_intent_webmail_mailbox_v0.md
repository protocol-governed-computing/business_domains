# Business Intent — webmail / mailbox

## Machine

```yaml
document:
  phase: p5
  domain: webmail
  subdomain: mailbox
  cr: cr_01_read_mail
  rule_set: transformation.schemas.REGISTER_SCHEMA_P5_V0
registers:
  subdomain_purpose: The mailbox subdomain gives a person a web-based way to read the mail they already have, which their mail provider keeps in a mailbox the person owns. The business does not keep the mail. It reads the mailbox when the person asks, shows what they asked to see, changes the mailbox only in the ways the person asked for, and keeps a record of every request. The host that connects to the provider reports what the provider said and carries out the changes the business decides; it decides nothing. This first part covers reading only.
  purpose_provenance:
  - source: Change seed §0 Subdomain Purpose
    disposition: INHERITED
    refinement: null
  subdomain_purposes:
  - subdomain: mailbox
    purpose: Mailbox lists a folder a page at a time, opens a message and marks a message as read or unread, deciding what the person sees and what changes in the mailbox, and recording every request.
    source_finding: {phase: p0, register: cr_type, row: 1}
  scope_boundary:
  - capability: List a folder
    status: IN_SCOPE
    notes: Newest received first, a page of 50, saying whether more exist or the folder is empty
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - capability: Open a message
    status: IN_SCOPE
    notes: Shows sender, recipients, subject, date and plain text, and makes the message read
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - capability: Mark a message as read or unread
    status: IN_SCOPE
    notes: Changes nothing when the message already has the state asked for
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  - capability: Report a change's outcome
    status: IN_SCOPE
    notes: The host reports whether the provider accepted a change the business decided
    source_finding: {phase: p0, register: requested_outcomes, row: 6}
  - capability: Sending, replying, forwarding and drafts
    status: DEFERRED
    notes: This first part covers reading only.
    source_finding: {phase: p0, register: out_of_scope, row: 1}
  - capability: Displaying HTML mail, and opening or saving attachments
    status: DEFERRED
    notes: Only plain text is shown in this part.
    source_finding: {phase: p0, register: out_of_scope, row: 2}
  - capability: Searching, sorting by other columns, and threads
    status: DEFERRED
    notes: Not part of reading in this first part.
    source_finding: {phase: p0, register: out_of_scope, row: 3}
  - capability: Managing folders and moving, copying or deleting messages
    status: DEFERRED
    notes: Not part of reading in this first part.
    source_finding: {phase: p0, register: out_of_scope, row: 4}
  business_objects:
  - store_name: Mailbox record
    record_model: APPEND_ONLY_JOURNAL
    business_rationale: Every request, answered or refused, must be in the record, and a record that could be amended would not be evidence.
    source_finding: {phase: p0, register: business_invariants, row: 3}
  identity_semantics:
  - store_name: Mailbox record
    identity_field: Sequence number
    source: Formed when the entry is added
    uniqueness_rule: Each entry is its own; no entry replaces another.
    cross_subdomain_relationship: None
    source_finding: {phase: p0, register: business_invariants, row: 3}
  invariants:
  - invariant: The business changes a mailbox only in a way the person asked for.
    business_reason: The person owns the mailbox.
    source_finding: {phase: p0, register: business_invariants, row: 1}
  - invariant: Every change made to a mailbox is one the business decided.
    business_reason: The host holds the person's password and could do anything; the business's decision is what limits it.
    source_finding: {phase: p0, register: business_invariants, row: 2}
  - invariant: Every request, answered or refused, is in the record.
    business_reason: The record is how the business shows it did only what was asked.
    source_finding: {phase: p0, register: business_invariants, row: 3}
  - invariant: No record holds a subject, a sender, message text or a credential.
    business_reason: A person's mail stays with their provider.
    source_finding: {phase: p0, register: business_invariants, row: 4}
  - invariant: A refusal never shows a partial result as if it were complete.
    business_reason: A person must be able to tell an answer from a failure.
    source_finding: {phase: p0, register: business_invariants, row: 5}
  actions:
  - action: List a folder
    object: folder
    trigger: The host reports a folder's message identifiers and the page the person asked for
    status: IN_SCOPE
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - action: Open a message
    object: message
    trigger: The host reports the read state and the parts of a message the person asked to open
    status: IN_SCOPE
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - action: Mark a message
    object: message
    trigger: The host reports a message's read state and the state the person asked for
    status: IN_SCOPE
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  - action: Report a change's outcome
    object: message
    trigger: The host reports whether the provider accepted a change the business decided
    status: IN_SCOPE
    source_finding: {phase: p0, register: requested_outcomes, row: 6}
  provisional_codes:
  - subdomain: mailbox
    provisional_code: AC_MAIL_HOST_V0
    family: AC
    summary: The program that reaches a person's mail provider; it reports and carries out, and holds no authority
    source_finding: {phase: p0, register: business_vocabulary, row: 9}
  - subdomain: mailbox
    provisional_code: WF_LIST_FOLDER_V0
    family: WF
    summary: Chooses which messages make the page of a folder the person asked for, newest received first
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - subdomain: mailbox
    provisional_code: WF_OPEN_MESSAGE_V0
    family: WF
    summary: Chooses what of a message is shown and decides that it becomes read
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - subdomain: mailbox
    provisional_code: WF_MARK_MESSAGE_V0
    family: WF
    summary: Decides a change of a message's read state, or that nothing changes
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  - subdomain: mailbox
    provisional_code: WF_REPORT_CHANGE_OUTCOME_V0
    family: WF
    summary: Records whether the provider accepted a change the business decided
    source_finding: {phase: p0, register: requested_outcomes, row: 6}
  - subdomain: mailbox
    provisional_code: IN_LIST_FOLDER_V0
    family: IN
    summary: A host's report of a folder's message identifiers and the page asked for
    source_finding: {phase: p0, register: requested_outcomes, row: 4}
  - subdomain: mailbox
    provisional_code: IN_OPEN_MESSAGE_V0
    family: IN
    summary: A host's report of the read state and the parts of a message the person asked to open
    source_finding: {phase: p0, register: requested_outcomes, row: 4}
  - subdomain: mailbox
    provisional_code: IN_MARK_MESSAGE_V0
    family: IN
    summary: A host's report of a message's read state and the state the person asked for
    source_finding: {phase: p0, register: requested_outcomes, row: 4}
  - subdomain: mailbox
    provisional_code: IN_REPORT_CHANGE_OUTCOME_V0
    family: IN
    summary: A host's report of whether the provider accepted a decided change
    source_finding: {phase: p0, register: requested_outcomes, row: 6}
  - subdomain: mailbox
    provisional_code: CC_CONFIRM_PROVIDER_ANSWERED_V0
    family: CC
    summary: Confirms the provider answered, refusing otherwise
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - subdomain: mailbox
    provisional_code: CC_CHOOSE_FOLDER_PAGE_V0
    family: CC
    summary: Chooses a page of a folder's identifiers, newest received first
    source_finding: {phase: p0, register: known_facts, row: 14}
  - subdomain: mailbox
    provisional_code: CC_CHOOSE_MESSAGE_TEXT_V0
    family: CC
    summary: Chooses the plain-text part of a message to show, or says none can be displayed
    source_finding: {phase: p0, register: known_facts, row: 22}
  - subdomain: mailbox
    provisional_code: CC_DECIDE_READ_STATE_V0
    family: CC
    summary: Decides whether a message becomes read, becomes unread or stays as it is
    source_finding: {phase: p0, register: known_facts, row: 25}
  - subdomain: mailbox
    provisional_code: CC_RECORD_MAILBOX_REQUEST_V0
    family: CC
    summary: Adds an entry to the mailbox record
    source_finding: {phase: p0, register: known_facts, row: 27}
  - subdomain: mailbox
    provisional_code: CT_PURE_CHOOSE_FOLDER_PAGE_V0
    family: CT
    summary: Orders identifiers newest received first and cuts the page asked for
    source_finding: {phase: p0, register: known_facts, row: 15}
  - subdomain: mailbox
    provisional_code: CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    family: CT
    summary: Chooses a message's plain-text part from its parts, or says its text cannot be displayed yet
    source_finding: {phase: p0, register: known_facts, row: 23}
  - subdomain: mailbox
    provisional_code: CT_PURE_DECIDE_READ_STATE_V0
    family: CT
    summary: Decides a change of read state from the state held and the state asked for
    source_finding: {phase: p0, register: known_facts, row: 25}
  - subdomain: mailbox
    provisional_code: EV_FOLDER_LISTED_V0
    family: EV
    summary: A folder's page was chosen for the person
    source_finding: {phase: p0, register: business_events, row: 1}
  - subdomain: mailbox
    provisional_code: EV_MESSAGE_OPENED_V0
    family: EV
    summary: A message was opened for the person
    source_finding: {phase: p0, register: business_events, row: 2}
  - subdomain: mailbox
    provisional_code: EV_READ_STATE_CHANGED_V0
    family: EV
    summary: The provider accepted a decided change of read state
    source_finding: {phase: p0, register: business_events, row: 3}
  - subdomain: mailbox
    provisional_code: EV_MAILBOX_REQUEST_REFUSED_V0
    family: EV
    summary: A request was refused
    source_finding: {phase: p0, register: business_events, row: 4}
  - subdomain: mailbox
    provisional_code: STRUCTURE_MAILBOX_STORAGE_V0
    family: STRUCTURE
    summary: Declares the mailbox record and the path it occupies
    source_finding: {phase: p0, register: business_invariants, row: 3}
  - subdomain: mailbox
    provisional_code: RB_MAILBOX_BINDINGS_V0
    family: RB
    summary: Binds every mailbox act to the record it appends to
    source_finding: {phase: p0, register: business_invariants, row: 3}
  cross_subdomain_refs: []
```

States what the subdomain does; P6 places it and P7 designs it.
