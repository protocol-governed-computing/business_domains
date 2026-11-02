# Change Seed — webmail / mailbox

## Machine

```yaml
document:
  phase: p0
  domain: webmail
  subdomain: mailbox
  cr: cr_01_read_mail
  rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0
registers:
  subdomain_purpose: The mailbox subdomain gives a person a web-based way to read the mail they already have, which their mail provider keeps in a mailbox the person owns. The business does not keep the mail. It reads the mailbox when the person asks, shows what they asked to see, changes the mailbox only in the ways the person asked for, and keeps a record of every request. The host that connects to the provider reports what the provider said and carries out the changes the business decides; it decides nothing. This first part covers reading only.
  cr_type:
  - subdomain: mailbox
    classification: NEW_SUBDOMAIN
    rationale: The webmail domain does not exist. This change creates it with its first subdomain, which lists a folder, opens a message and marks a message as read or unread.
  business_vocabulary:
  - term: Person
    definition: The owner of a mailbox, who asks the business to show it or change it.
  - term: Mail provider
    definition: The service that keeps a person's mail in a mailbox the person owns, such as Gmail. It is reached over IMAP.
  - term: Mailbox
    definition: The mail a person owns, kept by their mail provider and divided into folders.
  - term: Folder
    definition: A named part of a mailbox, such as the inbox, holding messages.
  - term: Message
    definition: One mail in a folder, with a sender, recipients, a subject, a date and its content.
  - term: Read state
    definition: Whether a message has been read. The mail provider holds it.
  - term: Flag state
    definition: Whether a message has been flagged. The mail provider holds it.
  - term: Plain text
    definition: The part of a message written as text, without formatting.
  - term: Host
    definition: The program that connects to the mail provider over IMAP, signs in with the person's credentials, reports what the provider returned, and carries out the changes the business decides. It holds no authority.
  - term: Credentials
    definition: What the person signs in to their mail provider with. The host reads them from a place the person controls.
  - term: Page
    definition: The part of a folder's list shown at one time.
  - term: Record
    definition: The business's account of every request, what was decided and what the provider answered.
  requested_outcomes:
  - outcome: A person can list a folder of their mailbox, a page at a time, newest first.
  - outcome: A person can open a message and read its text, which marks it as read.
  - outcome: A person can mark a message as read or as unread.
  - outcome: The host can report what the provider returned for a request.
  - outcome: The host receives the business's decision about what to show and what to change.
  - outcome: The host can report whether the provider accepted a change.
  - outcome: Every request, answered or refused, is in the record, and no record holds the content of mail or a credential.
  known_facts:
  - fact: A person's mail is kept by their mail provider, in a mailbox the person owns.
    certainty: HIGH
  - fact: The business does not keep the mail.
    certainty: HIGH
  - fact: The business changes the mailbox only in the ways the person asked for.
    certainty: HIGH
  - fact: The wanted behavior is that of established webmail, with Roundcube as the reference.
    certainty: HIGH
  - fact: This first part covers reading only; sending mail comes later.
    certainty: HIGH
  - fact: A webmail service holds a person's mail password and can do anything to the mailbox the person could do.
    certainty: HIGH
  - fact: The business decides every change made to a person's mailbox and keeps a record of it.
    certainty: HIGH
  - fact: The host may read the mailbox and report what the provider said; it may not decide what the person is shown or what is changed in the mailbox.
    certainty: HIGH
  - fact: The mailbox is reached over IMAP.
    certainty: HIGH
  - fact: The host connects to the provider, signs in with the person's credentials, and carries out one request at a time.
    certainty: HIGH
  - fact: The host reports to the business what the provider returned; the business decides what the person sees and which change, if any, is due.
    certainty: HIGH
  - fact: The host carries out the change the business decided and reports whether the provider accepted it; the business records the outcome.
    certainty: HIGH
  - fact: The business never holds the person's credentials; the host reads them from a place the person controls.
    certainty: HIGH
  - fact: A folder's list shows the newest messages first, a page of 50 at a time.
    certainty: HIGH
  - fact: Newest means most recently received by the provider; the date a message carries is not used to order a folder.
    certainty: HIGH
  - fact: A provider that does not answer within 30 seconds has not answered in time.
    certainty: HIGH
  - fact: For each listed message the business shows who sent it, its subject, its date, whether it has been read, whether it is flagged, and whether it has attachments.
    certainty: HIGH
  - fact: A folder with no messages is shown as empty, which is an answer and not a failure.
    certainty: HIGH
  - fact: An opened message shows its sender, recipients, subject, date and text.
    certainty: HIGH
  - fact: Opening a message marks it as read, as established webmail does.
    certainty: HIGH
  - fact: The business records that a message was opened and that it became read.
    certainty: HIGH
  - fact: Only the plain text of a message is shown.
    certainty: HIGH
  - fact: A message with no plain-text part is shown with a statement that its text cannot be displayed yet.
    certainty: HIGH
  - fact: Marking a message records the request and the provider's answer, and shows the state the message is now in.
    certainty: HIGH
  - fact: Marking a message with the state it already has is not an error; the business reports the state and records that nothing changed.
    certainty: HIGH
  - fact: A refusal tells the person which refusal happened and never shows a partial result as if it were complete.
    certainty: HIGH
  - fact: The record keeps who asked, what was asked, which folder and message it concerned, what was decided, and what the provider answered.
    certainty: HIGH
  - fact: The record identifies messages and does not copy their subjects, senders or text.
    certainty: HIGH
  system_beliefs:
  - belief: No domain in the composition reads or changes a mailbox.
    why_it_matters: If one does, this change reuses it instead of creating the webmail domain.
    verification_goal: Confirm that no artifact in the composition concerns mail, a mailbox or IMAP.
  - belief: The composition can keep a record that is only ever added to, with each entry kept as written.
    why_it_matters: Every request and its outcome is recorded, and no entry is changed afterwards.
    verification_goal: Confirm the composition offers append-only recording that a new domain can use.
  - belief: The composition already has a way for a program outside it to report a result and receive a decision, one act per call.
    why_it_matters: The host reports what the provider returned and receives what to show and what to change.
    verification_goal: Confirm an existing domain has acts called by an outside program that report a result and return a decision.
  assumptions: []
  constraints:
  - constraint: The mailbox is reached over IMAP with a password; other sign-in methods, such as OAuth, are out of this part.
    source: The problem statement's out-of-scope list.
  - constraint: No connection to the provider is kept open between requests.
    source: The problem statement's out-of-scope list.
  business_invariants:
  - invariant: The business changes a mailbox only in a way the person asked for.
  - invariant: Every change made to a mailbox is one the business decided.
  - invariant: Every request, answered or refused, is in the record.
  - invariant: No record holds a subject, a sender, message text or a credential.
  - invariant: A refusal never shows a partial result as if it were complete.
  lifecycle_states:
  - object: message
    state: unread
    meaning: The provider holds the message as not read.
  - object: message
    state: read
    meaning: The provider holds the message as read.
  business_events:
  - event: Folder listed
    when_it_occurs: When a folder's page is shown to the person
    significance: The record shows which folder the person was shown, and when.
  - event: Message opened
    when_it_occurs: When a message is shown to the person
    significance: The record shows which message was opened, and that it became read.
  - event: Read state changed
    when_it_occurs: When the provider accepts a change to a message's read state
    significance: The record shows the change the business decided and that the provider accepted it.
  - event: Request refused
    when_it_occurs: When a request is refused
    significance: The record shows which request was refused and why.
  authority_boundaries:
  - business_object: mailbox
    authoritative_owner: the person's mail provider
  - business_object: message
    authoritative_owner: the person's mail provider
  - business_object: record
    authoritative_owner: mailbox
  out_of_scope:
  - item: Sending, replying, forwarding and drafts
    reason: This first part covers reading only; sending comes later.
  - item: Displaying HTML mail, and opening or saving attachments
    reason: Only plain text is shown in this part.
  - item: Searching, sorting by other columns, and threads
    reason: Not part of reading in this first part.
  - item: Creating, renaming or deleting folders; moving, copying or deleting messages
    reason: Not part of reading in this first part.
  - item: Contacts, identities, signatures and settings
    reason: Not part of reading in this first part.
  - item: Sign-in methods other than a password for IMAP, such as OAuth
    reason: This part signs in with a password only.
  - item: Keeping a connection to the provider open between requests
    reason: The host carries out one request at a time.
  governance_scope:
  - scope_item: mailbox
    relationship: CREATED
  clarification_requests: []
  acceptance_criteria:
  - criterion: Listing a folder shows its newest messages first, with sender, subject, date, read state, flag state and attachment indicator for each.
  - criterion: Listing a folder with more messages than a page shows one page, and says that more exist.
  - criterion: Listing an empty folder answers that it is empty.
  - criterion: Opening a message shows its sender, recipients, subject, date and plain text.
  - criterion: Opening an unread message makes it read at the provider, and the record says so.
  - criterion: Opening a message with no plain-text part says its text cannot be displayed yet.
  - criterion: Marking an unread message as read makes it read at the provider.
  - criterion: Marking a read message as unread makes it unread at the provider.
  - criterion: Marking a message with the state it already has reports that state and changes nothing.
  - criterion: Rejected credentials are refused, and the refusal says so.
  - criterion: An unreachable or silent provider is refused, and the refusal says so.
  - criterion: A folder that does not exist is refused, and the refusal says so.
  - criterion: A message that does not exist in the folder is refused, and the refusal says so.
  - criterion: Every request, answered or refused, is in the record.
  - criterion: No record holds a subject, a sender, message text or a credential.
  identity_and_sameness:
  - business_object: folder
    identified_by: its name in the mailbox
    two_are_the_same_when: they carry the same name in the same mailbox
  - business_object: message
    identified_by: the identifier the provider gives it within its folder
    two_are_the_same_when: they carry the same identifier in the same folder of the same mailbox
  lifecycle_transitions:
  - object: message
    from_state: unread
    to_state: read
    triggered_by: opening the message, or marking it as read
    cascade: None
  - object: message
    from_state: read
    to_state: unread
    triggered_by: marking it as unread
    cascade: None
  operation_refusals:
  - operation: list a folder, open a message, mark a message
    refused_when: the provider rejects the person's credentials
    business_reason: The mailbox cannot be read without the person's sign-in.
  - operation: list a folder, open a message, mark a message
    refused_when: the provider cannot be reached, or does not answer in time
    business_reason: Nothing the provider has not said can be shown or changed.
  - operation: list a folder, open a message, mark a message
    refused_when: the folder does not exist
    business_reason: There is no folder to act on.
  - operation: open a message, mark a message
    refused_when: the message does not exist in the folder
    business_reason: There is no message to act on.
  authority_deferrals:
  - business_object: read state
    deferred_to: the person's mail provider
    until: always; the business decides a change and the provider holds the state
```

Reorganized faithfully from `p0_business_problem_statement.md`, including the three clarifications
its author answered: the page size, the order of a folder and the time a provider has to answer.
