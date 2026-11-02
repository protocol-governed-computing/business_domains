# Governance Intent — webmail / mailbox

## Machine

```yaml
document:
  phase: p6
  domain: webmail
  subdomain: mailbox
  cr: cr_01_read_mail
  rule_set: transformation.schemas.REGISTER_SCHEMA_P6_V0
registers:
  ownership:
  - capability: List a folder
    owner_subdomain: mailbox
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 1}
  - capability: Open a message
    owner_subdomain: mailbox
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 2}
  - capability: Mark a message as read or unread
    owner_subdomain: mailbox
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 3}
  - capability: Report a change's outcome
    owner_subdomain: mailbox
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 4}
  - capability: Sending, replying, forwarding and drafts
    owner_subdomain: mailbox
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 5}
  - capability: Displaying HTML mail, and opening or saving attachments
    owner_subdomain: mailbox
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 6}
  - capability: Searching, sorting by other columns, and threads
    owner_subdomain: mailbox
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 7}
  - capability: Managing folders and moving, copying or deleting messages
    owner_subdomain: mailbox
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 8}
  storage_governance:
  - storage_need: A durable mailbox record, only ever added to
    purpose: Every request, answered or refused, must be in the record, and a record that could be amended would not be evidence.
    subdomain: mailbox
    source_finding: {phase: p5, register: business_objects, row: 1}
  cross_subdomain_deps: []
  pps_artifacts_requiring_action: []
  boundary_rules:
  - rule_name: MAILBOX_OWNS_ITS_RECORD
    statement: The mailbox record is written only by mailbox's own acts, and only by adding entries.
    source_finding: {phase: p5, register: subdomain_purposes, row: 1}
  - rule_name: HOST_HOLDS_NO_AUTHORITY
    statement: Every mailbox act is called by the mail host; the host reports and carries out, and every decision is the act's.
    source_finding: {phase: p5, register: invariants, row: 2}
  - rule_name: NO_MAIL_CONTENT_KEPT
    statement: No record entry and no event carries a subject, a sender, message text or a credential.
    source_finding: {phase: p5, register: invariants, row: 4}
  governance_outcome:
  - capability: List a folder
    owner_subdomain: mailbox
    source_finding: {phase: p6, register: ownership, key: List a folder}
  - capability: Open a message
    owner_subdomain: mailbox
    source_finding: {phase: p6, register: ownership, key: Open a message}
  - capability: Mark a message as read or unread
    owner_subdomain: mailbox
    source_finding: {phase: p6, register: ownership, key: Mark a message as read or unread}
  - capability: Report a change's outcome
    owner_subdomain: mailbox
    source_finding: {phase: p6, register: ownership, key: Report a change's outcome}
```

Places every capability in mailbox. The domain is new, so no existing artifact needs action.
