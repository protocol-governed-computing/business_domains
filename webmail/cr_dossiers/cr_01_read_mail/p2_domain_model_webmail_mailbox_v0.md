# Domain Model — webmail / mailbox

## Machine

```yaml
document:
  phase: p2
  domain: webmail
  subdomain: mailbox
  cr: cr_01_read_mail
  rule_set: transformation.schemas.REGISTER_SCHEMA_P2_V0
registers:
  entities:
  - entity: Mailbox record
    description: The business's account of every request, what was decided and what the provider answered.
    store_model: One entry per request and per reported outcome, only ever added to, kept for each mailbox; no entry is changed or removed.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_vocabulary, row: 12}
  - entity: Message
    description: One mail in a folder, with a sender, recipients, a subject, a date and its content.
    store_model: None. The provider keeps it; the business holds only what the host reports for one request, and keeps none of its content.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_vocabulary, row: 5}
  - entity: Folder
    description: A named part of a mailbox, such as the inbox, holding messages.
    store_model: None. The provider keeps it; a request names it.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_vocabulary, row: 4}
  entity_attributes:
  - entity: Mailbox record
    attribute: Mailbox
    meaning: Whose mailbox the request concerned; it also says who asked.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, row: 27}
  - entity: Mailbox record
    attribute: Request
    meaning: What was asked.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, row: 27}
  - entity: Mailbox record
    attribute: Folder
    meaning: Which folder the request concerned.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, row: 27}
  - entity: Mailbox record
    attribute: Message identifier
    meaning: Which message the request concerned, by the identifier the provider gives it.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, row: 27}
  - entity: Mailbox record
    attribute: Decision
    meaning: What the business decided.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, row: 27}
  - entity: Mailbox record
    attribute: Provider answer
    meaning: What the provider answered, as the host reported it.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, row: 27}
  - entity: Message
    attribute: Identifier
    meaning: What identifies a message within its folder.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: identity_and_sameness, row: 2}
  - entity: Message
    attribute: Read state
    meaning: Whether the message has been read; the provider holds it.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_vocabulary, row: 6}
  - entity: Message
    attribute: Flag state
    meaning: Whether the message has been flagged; the provider holds it.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_vocabulary, row: 7}
  - entity: Folder
    attribute: Name
    meaning: What identifies a folder in a mailbox.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: identity_and_sameness, row: 1}
  business_processes:
  - process: List a folder
    initiator: Person, through the host
    outcome: The newest messages of a folder are shown, a page of 50 at a time, with sender, subject, date, read state, flag state and attachment indicator.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  - process: Open a message
    initiator: Person, through the host
    outcome: A message's sender, recipients, subject, date and plain text are shown, and the message becomes read.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 2}
  - process: Mark a message
    initiator: Person, through the host
    outcome: A message becomes read or unread at the provider, and its state is shown.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 3}
  - process: Report a change's outcome
    initiator: Host
    outcome: The business records whether the provider accepted a change it decided.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 6}
  process_steps:
  - process: List a folder
    step: '1'
    action: Refuse when the provider rejected the credentials, could not be reached, or holds no such folder
    record_produced: A refusal in the record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 1}
  - process: List a folder
    step: '2'
    action: Decide which messages make the page asked for, newest received first
    record_produced: None
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, row: 14}
  - process: List a folder
    step: '3'
    action: Show the page, and say whether more messages exist or the folder is empty
    record_produced: A folder-listed entry in the record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_events, row: 1}
  - process: Open a message
    step: '1'
    action: Refuse when the provider rejected the credentials, could not be reached, or holds no such folder or message
    record_produced: A refusal in the record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 4}
  - process: Open a message
    step: '2'
    action: Show the message's sender, recipients, subject, date and plain text, or say its text cannot be displayed yet
    record_produced: None
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, row: 19}
  - process: Open a message
    step: '3'
    action: Decide that the message becomes read when it is unread
    record_produced: A message-opened entry in the record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, row: 20}
  - process: Mark a message
    step: '1'
    action: Refuse when the provider rejected the credentials, could not be reached, or holds no such folder or message
    record_produced: A refusal in the record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 4}
  - process: Mark a message
    step: '2'
    action: Decide the change, or that nothing changes when the message already has the state asked for
    record_produced: The request and the decision in the record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, row: 25}
  - process: Report a change's outcome
    step: '1'
    action: Record whether the provider accepted the change, and show the state the message is now in
    record_produced: A read-state-changed entry in the record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_events, row: 3}
  belief_verification:
  - belief: No domain in the composition reads or changes a mailbox.
    result: VERIFIED
    evidence: si.artifact.list over the pinned composition names no artifact concerning mail, a mailbox or IMAP; no domain is named webmail.
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - belief: The composition can keep a record that is only ever added to, with each entry kept as written.
    result: VERIFIED
    evidence: capability_side_effects::CS_APPENDONLY_JSONL_V0 declares APPEND and GET_ALL, with append_only and ordered among its guarantees and mutation among its non-guarantees.
    source_finding: {phase: p1, register: system_beliefs, row: 2}
  - belief: The composition already has a way for a program outside it to report a result and receive a decision, one act per call.
    result: VERIFIED
    evidence: causal_language_model::AC_MODEL_HOST_V0 calls causal_language_model::WF_OFFER_NEXT_TOKENS_V0, which takes the host's offer and returns the business's choice.
    source_finding: {phase: p1, register: system_beliefs, row: 3}
  pps_baseline_fqdns:
  - capability: Appendonly jsonl side effect, as the platform declares it
    fqdn: capability_side_effects::CS_APPENDONLY_JSONL_V0
    what_it_does: Provide an append-only JSONL persistence layer with ordered event history.
    fit: EXACT
    cannot_do: Nothing the record asks of it.
  - capability: Assemble record transform, as the platform declares it
    fqdn: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    what_it_does: Combines multiple input values into a single structured record object.
    fit: PARTIAL
    cannot_do: Decide a page, read a message's plain text, or decide a change of read state.
  - capability: A host's act, as the language model domain declares it
    fqdn: causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    what_it_does: Takes what an outside program reports, decides, records, and returns the decision.
    fit: MISMATCH
    cannot_do: Anything about mail; it is a pattern to follow, not a capability to reuse.
  gaps:
  - gap: No act lists a folder, opens a message, marks a message or records a change's outcome.
    severity: CRITICAL
    impact: This change authors them, in a new domain.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  - gap: No transform decides a folder's page, reads a message's plain text, or decides a change of read state.
    severity: CRITICAL
    impact: This change authors them, with test vectors.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 2}
  - gap: No actor stands for a mail host.
    severity: MAJOR
    impact: This change declares one.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 4}
  architectural_observations:
  - observation: A transform has no effects and a domain writes no side effect, so the mail provider is reached by a host outside the composition, as the language model domain reaches its model.
    evidence: causal_language_model::AC_MODEL_HOST_V0 · causal_language_model::WF_OFFER_NEXT_TOKENS_V0
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: system_beliefs, row: 3}
  - observation: The record can be kept with the platform's append-only side effect; nothing new is needed to keep it.
    evidence: capability_side_effects::CS_APPENDONLY_JSONL_V0
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: system_beliefs, row: 2}
  discovery_concerns:
  - concern: Reading a message over IMAP can mark it read at the provider by itself, before the business decides. The host must read without marking.
    evidence: The business decides every change to the mailbox; opening a message is decided to make it read.
    severity: MAJOR
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_invariants, row: 2}
  - concern: What an act is handed and what it answers can reach the trace; mail content must not.
    evidence: No record holds a subject, a sender, message text or a credential.
    severity: MAJOR
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_invariants, row: 4}
  open_questions: []
```

Written against the pinned composition. Every row cites the change-request row it models.
