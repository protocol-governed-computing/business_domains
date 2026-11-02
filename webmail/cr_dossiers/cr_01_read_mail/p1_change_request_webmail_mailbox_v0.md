# Stage 1 — Change Request: Clarification & Fact Capture: email / mailbox

## Machine

```yaml
document:
  phase: p1
  domain: webmail
  subdomain: mailbox
  cr: cr_01_read_mail
  rule_set: transformation.schemas.REGISTER_SCHEMA_P1_V0
registers:
  cr_type:
  - subdomain: mailbox
    classification: NEW_SUBDOMAIN
    rationale: The webmail domain does not exist. This change creates it with its first subdomain, which lists a folder, opens a message and marks a message as read or unread.
    source_finding: {phase: p0, register: cr_type, row: 1}
  business_vocabulary:
  - term: Person
    definition: The owner of a mailbox, who asks the business to show it or change it.
    source_finding: {phase: p0, register: business_vocabulary, row: 1}
  - term: Mail provider
    definition: The service that keeps a person's mail in a mailbox the person owns, such as Gmail. It is reached over IMAP.
    source_finding: {phase: p0, register: business_vocabulary, row: 2}
  - term: Mailbox
    definition: The mail a person owns, kept by their mail provider and divided into folders.
    source_finding: {phase: p0, register: business_vocabulary, row: 3}
  - term: Folder
    definition: A named part of a mailbox, such as the inbox, holding messages.
    source_finding: {phase: p0, register: business_vocabulary, row: 4}
  - term: Message
    definition: One mail in a folder, with a sender, recipients, a subject, a date and its content.
    source_finding: {phase: p0, register: business_vocabulary, row: 5}
  - term: Read state
    definition: Whether a message has been read. The mail provider holds it.
    source_finding: {phase: p0, register: business_vocabulary, row: 6}
  - term: Flag state
    definition: Whether a message has been flagged. The mail provider holds it.
    source_finding: {phase: p0, register: business_vocabulary, row: 7}
  - term: Plain text
    definition: The part of a message written as text, without formatting.
    source_finding: {phase: p0, register: business_vocabulary, row: 8}
  - term: Host
    definition: The program that connects to the mail provider over IMAP, signs in with the person's credentials, reports what the provider returned, and carries out the changes the business decides. It holds no authority.
    source_finding: {phase: p0, register: business_vocabulary, row: 9}
  - term: Credentials
    definition: What the person signs in to their mail provider with. The host reads them from a place the person controls.
    source_finding: {phase: p0, register: business_vocabulary, row: 10}
  - term: Page
    definition: The part of a folder's list shown at one time.
    source_finding: {phase: p0, register: business_vocabulary, row: 11}
  - term: Record
    definition: The business's account of every request, what was decided and what the provider answered.
    source_finding: {phase: p0, register: business_vocabulary, row: 12}
  requested_outcomes:
  - outcome: A person can list a folder of their mailbox, a page at a time, newest first.
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - outcome: A person can open a message and read its text, which marks it as read.
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - outcome: A person can mark a message as read or as unread.
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  - outcome: The host can report what the provider returned for a request.
    source_finding: {phase: p0, register: requested_outcomes, row: 4}
  - outcome: The host receives the business's decision about what to show and what to change.
    source_finding: {phase: p0, register: requested_outcomes, row: 5}
  - outcome: The host can report whether the provider accepted a change.
    source_finding: {phase: p0, register: requested_outcomes, row: 6}
  - outcome: Every request, answered or refused, is in the record, and no record holds the content of mail or a credential.
    source_finding: {phase: p0, register: requested_outcomes, row: 7}
  known_facts:
  - fact: A person's mail is kept by their mail provider, in a mailbox the person owns.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 1}
  - fact: The business does not keep the mail.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 2}
  - fact: The business changes the mailbox only in the ways the person asked for.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 3}
  - fact: The wanted behavior is that of established webmail, with Roundcube as the reference.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 4}
  - fact: This first part covers reading only; sending mail comes later.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 5}
  - fact: A webmail service holds a person's mail password and can do anything to the mailbox the person could do.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 6}
  - fact: The business decides every change made to a person's mailbox and keeps a record of it.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 7}
  - fact: The host may read the mailbox and report what the provider said; it may not decide what the person is shown or what is changed in the mailbox.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 8}
  - fact: The mailbox is reached over IMAP.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 9}
  - fact: The host connects to the provider, signs in with the person's credentials, and carries out one request at a time.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 10}
  - fact: The host reports to the business what the provider returned; the business decides what the person sees and which change, if any, is due.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 11}
  - fact: The host carries out the change the business decided and reports whether the provider accepted it; the business records the outcome.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 12}
  - fact: The business never holds the person's credentials; the host reads them from a place the person controls.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 13}
  - fact: A folder's list shows the newest messages first, a page of 50 at a time.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 14}
  - fact: Newest means most recently received by the provider; the date a message carries is not used to order a folder.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 15}
  - fact: A provider that does not answer within 30 seconds has not answered in time.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 16}
  - fact: For each listed message the business shows who sent it, its subject, its date, whether it has been read, whether it is flagged, and whether it has attachments.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 17}
  - fact: A folder with no messages is shown as empty, which is an answer and not a failure.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 18}
  - fact: An opened message shows its sender, recipients, subject, date and text.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 19}
  - fact: Opening a message marks it as read, as established webmail does.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 20}
  - fact: The business records that a message was opened and that it became read.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 21}
  - fact: Only the plain text of a message is shown.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 22}
  - fact: A message with no plain-text part is shown with a statement that its text cannot be displayed yet.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 23}
  - fact: Marking a message records the request and the provider's answer, and shows the state the message is now in.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 24}
  - fact: Marking a message with the state it already has is not an error; the business reports the state and records that nothing changed.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 25}
  - fact: A refusal tells the person which refusal happened and never shows a partial result as if it were complete.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 26}
  - fact: The record keeps who asked, what was asked, which folder and message it concerned, what was decided, and what the provider answered.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 27}
  - fact: The record identifies messages and does not copy their subjects, senders or text.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 28}
  system_beliefs:
  - belief: No domain in the composition reads or changes a mailbox.
    why_it_matters: If one does, this change reuses it instead of creating the webmail domain.
    verification_goal: Confirm that no artifact in the composition concerns mail, a mailbox or IMAP.
    source_finding: {phase: p0, register: system_beliefs, row: 1}
  - belief: The composition can keep a record that is only ever added to, with each entry kept as written.
    why_it_matters: Every request and its outcome is recorded, and no entry is changed afterwards.
    verification_goal: Confirm the composition offers append-only recording that a new domain can use.
    source_finding: {phase: p0, register: system_beliefs, row: 2}
  - belief: The composition already has a way for a program outside it to report a result and receive a decision, one act per call.
    why_it_matters: The host reports what the provider returned and receives what to show and what to change.
    verification_goal: Confirm an existing domain has acts called by an outside program that report a result and return a decision.
    source_finding: {phase: p0, register: system_beliefs, row: 3}
  assumptions: []
  constraints:
  - constraint: The mailbox is reached over IMAP with a password; other sign-in methods, such as OAuth, are out of this part.
    source: The problem statement's out-of-scope list.
    source_finding: {phase: p0, register: constraints, row: 1}
  - constraint: No connection to the provider is kept open between requests.
    source: The problem statement's out-of-scope list.
    source_finding: {phase: p0, register: constraints, row: 2}
  business_invariants:
  - invariant: The business changes a mailbox only in a way the person asked for.
    source_finding: {phase: p0, register: business_invariants, row: 1}
  - invariant: Every change made to a mailbox is one the business decided.
    source_finding: {phase: p0, register: business_invariants, row: 2}
  - invariant: Every request, answered or refused, is in the record.
    source_finding: {phase: p0, register: business_invariants, row: 3}
  - invariant: No record holds a subject, a sender, message text or a credential.
    source_finding: {phase: p0, register: business_invariants, row: 4}
  - invariant: A refusal never shows a partial result as if it were complete.
    source_finding: {phase: p0, register: business_invariants, row: 5}
  lifecycle_states:
  - object: message
    state: unread
    meaning: The provider holds the message as not read.
    source_finding: {phase: p0, register: lifecycle_states, row: 1}
  - object: message
    state: read
    meaning: The provider holds the message as read.
    source_finding: {phase: p0, register: lifecycle_states, row: 2}
  business_events:
  - event: Folder listed
    when_it_occurs: When a folder's page is shown to the person
    significance: The record shows which folder the person was shown, and when.
    source_finding: {phase: p0, register: business_events, row: 1}
  - event: Message opened
    when_it_occurs: When a message is shown to the person
    significance: The record shows which message was opened, and that it became read.
    source_finding: {phase: p0, register: business_events, row: 2}
  - event: Read state changed
    when_it_occurs: When the provider accepts a change to a message's read state
    significance: The record shows the change the business decided and that the provider accepted it.
    source_finding: {phase: p0, register: business_events, row: 3}
  - event: Request refused
    when_it_occurs: When a request is refused
    significance: The record shows which request was refused and why.
    source_finding: {phase: p0, register: business_events, row: 4}
  authority_boundaries:
  - business_object: mailbox
    authoritative_owner: the person's mail provider
    source_finding: {phase: p0, register: authority_boundaries, row: 1}
  - business_object: message
    authoritative_owner: the person's mail provider
    source_finding: {phase: p0, register: authority_boundaries, row: 2}
  - business_object: record
    authoritative_owner: mailbox
    source_finding: {phase: p0, register: authority_boundaries, row: 3}
  out_of_scope:
  - item: Sending, replying, forwarding and drafts
    reason: This first part covers reading only; sending comes later.
    source_finding: {phase: p0, register: out_of_scope, row: 1}
  - item: Displaying HTML mail, and opening or saving attachments
    reason: Only plain text is shown in this part.
    source_finding: {phase: p0, register: out_of_scope, row: 2}
  - item: Searching, sorting by other columns, and threads
    reason: Not part of reading in this first part.
    source_finding: {phase: p0, register: out_of_scope, row: 3}
  - item: Creating, renaming or deleting folders; moving, copying or deleting messages
    reason: Not part of reading in this first part.
    source_finding: {phase: p0, register: out_of_scope, row: 4}
  - item: Contacts, identities, signatures and settings
    reason: Not part of reading in this first part.
    source_finding: {phase: p0, register: out_of_scope, row: 5}
  - item: Sign-in methods other than a password for IMAP, such as OAuth
    reason: This part signs in with a password only.
    source_finding: {phase: p0, register: out_of_scope, row: 6}
  - item: Keeping a connection to the provider open between requests
    reason: The host carries out one request at a time.
    source_finding: {phase: p0, register: out_of_scope, row: 7}
  governance_scope:
  - scope_item: mailbox
    relationship: CREATED
    source_finding: {phase: p0, register: governance_scope, row: 1}
  clarification_requests: []
  acceptance_criteria:
  - criterion: Listing a folder shows its newest messages first, with sender, subject, date, read state, flag state and attachment indicator for each.
    source_finding: {phase: p0, register: acceptance_criteria, row: 1}
  - criterion: Listing a folder with more messages than a page shows one page, and says that more exist.
    source_finding: {phase: p0, register: acceptance_criteria, row: 2}
  - criterion: Listing an empty folder answers that it is empty.
    source_finding: {phase: p0, register: acceptance_criteria, row: 3}
  - criterion: Opening a message shows its sender, recipients, subject, date and plain text.
    source_finding: {phase: p0, register: acceptance_criteria, row: 4}
  - criterion: Opening an unread message makes it read at the provider, and the record says so.
    source_finding: {phase: p0, register: acceptance_criteria, row: 5}
  - criterion: Opening a message with no plain-text part says its text cannot be displayed yet.
    source_finding: {phase: p0, register: acceptance_criteria, row: 6}
  - criterion: Marking an unread message as read makes it read at the provider.
    source_finding: {phase: p0, register: acceptance_criteria, row: 7}
  - criterion: Marking a read message as unread makes it unread at the provider.
    source_finding: {phase: p0, register: acceptance_criteria, row: 8}
  - criterion: Marking a message with the state it already has reports that state and changes nothing.
    source_finding: {phase: p0, register: acceptance_criteria, row: 9}
  - criterion: Rejected credentials are refused, and the refusal says so.
    source_finding: {phase: p0, register: acceptance_criteria, row: 10}
  - criterion: An unreachable or silent provider is refused, and the refusal says so.
    source_finding: {phase: p0, register: acceptance_criteria, row: 11}
  - criterion: A folder that does not exist is refused, and the refusal says so.
    source_finding: {phase: p0, register: acceptance_criteria, row: 12}
  - criterion: A message that does not exist in the folder is refused, and the refusal says so.
    source_finding: {phase: p0, register: acceptance_criteria, row: 13}
  - criterion: Every request, answered or refused, is in the record.
    source_finding: {phase: p0, register: acceptance_criteria, row: 14}
  - criterion: No record holds a subject, a sender, message text or a credential.
    source_finding: {phase: p0, register: acceptance_criteria, row: 15}
  identity_and_sameness:
  - business_object: folder
    identified_by: its name in the mailbox
    two_are_the_same_when: they carry the same name in the same mailbox
    source_finding: {phase: p0, register: identity_and_sameness, row: 1}
  - business_object: message
    identified_by: the identifier the provider gives it within its folder
    two_are_the_same_when: they carry the same identifier in the same folder of the same mailbox
    source_finding: {phase: p0, register: identity_and_sameness, row: 2}
  lifecycle_transitions:
  - object: message
    from_state: unread
    to_state: read
    triggered_by: opening the message, or marking it as read
    cascade: None
    source_finding: {phase: p0, register: lifecycle_transitions, row: 1}
  - object: message
    from_state: read
    to_state: unread
    triggered_by: marking it as unread
    cascade: None
    source_finding: {phase: p0, register: lifecycle_transitions, row: 2}
  operation_refusals:
  - operation: list a folder, open a message, mark a message
    refused_when: the provider rejects the person's credentials
    business_reason: The mailbox cannot be read without the person's sign-in.
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: list a folder, open a message, mark a message
    refused_when: the provider cannot be reached, or does not answer in time
    business_reason: Nothing the provider has not said can be shown or changed.
    source_finding: {phase: p0, register: operation_refusals, row: 2}
  - operation: list a folder, open a message, mark a message
    refused_when: the folder does not exist
    business_reason: There is no folder to act on.
    source_finding: {phase: p0, register: operation_refusals, row: 3}
  - operation: open a message, mark a message
    refused_when: the message does not exist in the folder
    business_reason: There is no message to act on.
    source_finding: {phase: p0, register: operation_refusals, row: 4}
  authority_deferrals:
  - business_object: read state
    deferred_to: the person's mail provider
    until: always; the business decides a change and the provider holds the state
    source_finding: {phase: p0, register: authority_deferrals, row: 1}
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
