# Design Intent — webmail / mailbox

## Machine

```yaml
document:
  phase: p7
  domain: webmail
  subdomain: mailbox
  cr: cr_01_read_mail
  rule_set: transformation.schemas.REGISTER_SCHEMA_P7_V0
registers:
  design_resolution: []
  existing_inventory:
  - fqdn: capability_side_effects::CS_APPENDONLY_JSONL_V0
    action: REUSE
    summary: Append-only persistence with ordered history
    reason: The record is only ever added to.
    source_finding:
      phase: p3
      register: dependency_discoveries
      row: 1
  - fqdn: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    action: REUSE
    summary: Combines input values into a single record
    reason: Each entry is assembled before it is added.
    source_finding:
      phase: p3
      register: dependency_discoveries
      row: 2
  - fqdn: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    action: REUSE
    summary: Validates that a value is a member of a declared set
    reason: Each act confirms with it that the provider answered.
    source_finding:
      phase: p3
      register: dependency_discoveries
      row: 3
  new_artifacts:
  - capability: Every mailbox act
    family: AC
    code: webmail::AC_MAIL_HOST_V0
    summary: The program that reaches a person's mail provider; it reports and carries out, and holds no authority
    owner_subdomain: mailbox
    status: NEW
    source_finding:
      phase: p5
      register: provisional_codes
      row: 1
  - capability: List a folder
    family: IN
    code: webmail::IN_LIST_FOLDER_V0
    summary: A host's report of a folder's message identifiers and the page asked for
    owner_subdomain: mailbox
    status: NEW
    source_finding:
      phase: p5
      register: provisional_codes
      row: 6
  - capability: Open a message
    family: IN
    code: webmail::IN_OPEN_MESSAGE_V0
    summary: A host's report of the read state and the parts of a message the person asked to open
    owner_subdomain: mailbox
    status: NEW
    source_finding:
      phase: p5
      register: provisional_codes
      row: 7
  - capability: Mark a message as read or unread
    family: IN
    code: webmail::IN_MARK_MESSAGE_V0
    summary: A host's report of a message's read state and the state the person asked for
    owner_subdomain: mailbox
    status: NEW
    source_finding:
      phase: p5
      register: provisional_codes
      row: 8
  - capability: Report a change's outcome
    family: IN
    code: webmail::IN_REPORT_CHANGE_OUTCOME_V0
    summary: A host's report of whether the provider accepted a decided change
    owner_subdomain: mailbox
    status: NEW
    source_finding:
      phase: p5
      register: provisional_codes
      row: 9
  - capability: List a folder
    family: CT
    code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    summary: Orders identifiers newest received first and cuts the page asked for
    owner_subdomain: mailbox
    status: NEW
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - capability: Open a message
    family: CT
    code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    summary: Chooses a message's plain-text part from its parts, or says its text cannot be displayed yet
    owner_subdomain: mailbox
    status: NEW
    source_finding:
      phase: p5
      register: provisional_codes
      row: 16
  - capability: Mark a message as read or unread
    family: CT
    code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    summary: Decides a change of read state from the state held and the state asked for
    owner_subdomain: mailbox
    status: NEW
    source_finding:
      phase: p5
      register: provisional_codes
      row: 17
  - capability: Every mailbox act
    family: CC
    code: webmail::CC_CONFIRM_PROVIDER_ANSWERED_V0
    summary: Confirms the provider answered, refusing otherwise
    owner_subdomain: mailbox
    status: NEW
    source_finding:
      phase: p5
      register: provisional_codes
      row: 10
  - capability: List a folder
    family: CC
    code: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    summary: Chooses a page of a folder's identifiers, newest received first
    owner_subdomain: mailbox
    status: NEW
    source_finding:
      phase: p5
      register: provisional_codes
      row: 11
  - capability: Open a message
    family: CC
    code: webmail::CC_CHOOSE_MESSAGE_TEXT_V0
    summary: Chooses the plain-text part of a message to show, or says none can be displayed
    owner_subdomain: mailbox
    status: NEW
    source_finding:
      phase: p5
      register: provisional_codes
      row: 12
  - capability: Mark a message as read or unread
    family: CC
    code: webmail::CC_DECIDE_READ_STATE_V0
    summary: Decides whether a message becomes read, becomes unread or stays as it is
    owner_subdomain: mailbox
    status: NEW
    source_finding:
      phase: p5
      register: provisional_codes
      row: 13
  - capability: Every mailbox act
    family: CC
    code: webmail::CC_RECORD_MAILBOX_REQUEST_V0
    summary: Adds an entry to the mailbox record
    owner_subdomain: mailbox
    status: NEW
    source_finding:
      phase: p5
      register: provisional_codes
      row: 14
  - capability: List a folder
    family: EV
    code: webmail::EV_FOLDER_LISTED_V0
    summary: A folder's page was chosen for the person
    owner_subdomain: mailbox
    status: NEW
    source_finding:
      phase: p5
      register: provisional_codes
      row: 18
  - capability: Open a message
    family: EV
    code: webmail::EV_MESSAGE_OPENED_V0
    summary: A message was opened for the person
    owner_subdomain: mailbox
    status: NEW
    source_finding:
      phase: p5
      register: provisional_codes
      row: 19
  - capability: Report a change's outcome
    family: EV
    code: webmail::EV_READ_STATE_CHANGED_V0
    summary: The provider accepted a decided change of read state
    owner_subdomain: mailbox
    status: NEW
    source_finding:
      phase: p5
      register: provisional_codes
      row: 20
  - capability: Every mailbox act
    family: EV
    code: webmail::EV_MAILBOX_REQUEST_REFUSED_V0
    summary: A request was refused
    owner_subdomain: mailbox
    status: NEW
    source_finding:
      phase: p5
      register: provisional_codes
      row: 21
  - capability: List a folder
    family: WF
    code: webmail::WF_LIST_FOLDER_V0
    summary: Chooses which messages make the page of a folder the person asked for, newest received first
    owner_subdomain: mailbox
    status: NEW
    source_finding:
      phase: p5
      register: provisional_codes
      row: 2
  - capability: Open a message
    family: WF
    code: webmail::WF_OPEN_MESSAGE_V0
    summary: Chooses what of a message is shown and decides that it becomes read
    owner_subdomain: mailbox
    status: NEW
    source_finding:
      phase: p5
      register: provisional_codes
      row: 3
  - capability: Mark a message as read or unread
    family: WF
    code: webmail::WF_MARK_MESSAGE_V0
    summary: Decides a change of a message's read state, or that nothing changes
    owner_subdomain: mailbox
    status: NEW
    source_finding:
      phase: p5
      register: provisional_codes
      row: 4
  - capability: Report a change's outcome
    family: WF
    code: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    summary: Records whether the provider accepted a change the business decided
    owner_subdomain: mailbox
    status: NEW
    source_finding:
      phase: p5
      register: provisional_codes
      row: 5
  - capability: Every mailbox act
    family: STRUCTURE
    code: webmail::STRUCTURE_MAILBOX_STORAGE_V0
    summary: Declares the mailbox record and the path it occupies
    owner_subdomain: mailbox
    status: NEW
    source_finding:
      phase: p5
      register: provisional_codes
      row: 22
  - capability: Every mailbox act
    family: RB
    code: webmail::RB_MAILBOX_BINDINGS_V0
    summary: Binds every mailbox act to the record it appends to
    owner_subdomain: mailbox
    status: NEW
    source_finding:
      phase: p5
      register: provisional_codes
      row: 23
  rb_declarations:
  - rb_code: webmail::RB_MAILBOX_BINDINGS_V0
    binds_wf: webmail::WF_LIST_FOLDER_V0
    cs_bindings:
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: webmail::STRUCTURE_MAILBOX_STORAGE_V0
    source_finding:
      phase: p5
      register: provisional_codes
      row: 23
  - rb_code: webmail::RB_MAILBOX_BINDINGS_V0
    binds_wf: webmail::WF_OPEN_MESSAGE_V0
    cs_bindings:
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: webmail::STRUCTURE_MAILBOX_STORAGE_V0
    source_finding:
      phase: p5
      register: provisional_codes
      row: 23
  - rb_code: webmail::RB_MAILBOX_BINDINGS_V0
    binds_wf: webmail::WF_MARK_MESSAGE_V0
    cs_bindings:
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: webmail::STRUCTURE_MAILBOX_STORAGE_V0
    source_finding:
      phase: p5
      register: provisional_codes
      row: 23
  - rb_code: webmail::RB_MAILBOX_BINDINGS_V0
    binds_wf: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    cs_bindings:
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: webmail::STRUCTURE_MAILBOX_STORAGE_V0
    source_finding:
      phase: p5
      register: provisional_codes
      row: 23
  execution_topology:
  - workflow: webmail::WF_LIST_FOLDER_V0
    node: webmail::IN_LIST_FOLDER_V0
    node_type: IN
    routing:
      ACK: CONFIRM_ANSWERED
      NACK: EXIT_REJECTED
    source_finding: &id001
      phase: p5
      register: actions
      row: 1
  - workflow: webmail::WF_LIST_FOLDER_V0
    node: CONFIRM_ANSWERED
    node_type: CC
    routing:
      SUCCESS: webmail::CC_CHOOSE_FOLDER_PAGE_V0
      VIOLATION: RECORD_REFUSED
    source_finding: *id001
    runs: webmail::CC_CONFIRM_PROVIDER_ANSWERED_V0
  - workflow: webmail::WF_LIST_FOLDER_V0
    node: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    node_type: CC
    routing:
      SUCCESS: RECORD_LISTED
      VIOLATION: RECORD_REPORT_REFUSED
    source_finding: *id001
  - workflow: webmail::WF_LIST_FOLDER_V0
    node: RECORD_LISTED
    node_type: CC
    routing:
      SUCCESS: EXIT_LISTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: *id001
    runs: webmail::CC_RECORD_MAILBOX_REQUEST_V0
  - workflow: webmail::WF_LIST_FOLDER_V0
    node: RECORD_REFUSED
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: *id001
    runs: webmail::CC_RECORD_MAILBOX_REQUEST_V0
  - workflow: webmail::WF_LIST_FOLDER_V0
    node: RECORD_REPORT_REFUSED
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: *id001
    runs: webmail::CC_RECORD_MAILBOX_REQUEST_V0
  - workflow: webmail::WF_LIST_FOLDER_V0
    node: EXIT_LISTED
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: *id001
  - workflow: webmail::WF_LIST_FOLDER_V0
    node: EXIT_REFUSED
    node_type: EXIT
    routing: null
    source_finding: *id001
  - workflow: webmail::WF_LIST_FOLDER_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
    source_finding: *id001
  - workflow: webmail::WF_OPEN_MESSAGE_V0
    node: webmail::IN_OPEN_MESSAGE_V0
    node_type: IN
    routing:
      ACK: CONFIRM_ANSWERED
      NACK: EXIT_REJECTED
    source_finding: &id002
      phase: p5
      register: actions
      row: 2
  - workflow: webmail::WF_OPEN_MESSAGE_V0
    node: CONFIRM_ANSWERED
    node_type: CC
    routing:
      SUCCESS: webmail::CC_CHOOSE_MESSAGE_TEXT_V0
      VIOLATION: RECORD_REFUSED
    source_finding: *id002
    runs: webmail::CC_CONFIRM_PROVIDER_ANSWERED_V0
  - workflow: webmail::WF_OPEN_MESSAGE_V0
    node: webmail::CC_CHOOSE_MESSAGE_TEXT_V0
    node_type: CC
    routing:
      SUCCESS: webmail::CC_DECIDE_READ_STATE_V0
      VIOLATION: RECORD_REPORT_REFUSED
    source_finding: *id002
  - workflow: webmail::WF_OPEN_MESSAGE_V0
    node: webmail::CC_DECIDE_READ_STATE_V0
    node_type: CC
    routing:
      SUCCESS: RECORD_OPENED
      VIOLATION: RECORD_REPORT_REFUSED
    source_finding: *id002
  - workflow: webmail::WF_OPEN_MESSAGE_V0
    node: RECORD_OPENED
    node_type: CC
    routing:
      SUCCESS: EXIT_OPENED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: *id002
    runs: webmail::CC_RECORD_MAILBOX_REQUEST_V0
  - workflow: webmail::WF_OPEN_MESSAGE_V0
    node: RECORD_REFUSED
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: *id002
    runs: webmail::CC_RECORD_MAILBOX_REQUEST_V0
  - workflow: webmail::WF_OPEN_MESSAGE_V0
    node: RECORD_REPORT_REFUSED
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: *id002
    runs: webmail::CC_RECORD_MAILBOX_REQUEST_V0
  - workflow: webmail::WF_OPEN_MESSAGE_V0
    node: EXIT_OPENED
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: *id002
  - workflow: webmail::WF_OPEN_MESSAGE_V0
    node: EXIT_REFUSED
    node_type: EXIT
    routing: null
    source_finding: *id002
  - workflow: webmail::WF_OPEN_MESSAGE_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
    source_finding: *id002
  - workflow: webmail::WF_MARK_MESSAGE_V0
    node: webmail::IN_MARK_MESSAGE_V0
    node_type: IN
    routing:
      ACK: CONFIRM_ANSWERED
      NACK: EXIT_REJECTED
    source_finding: &id003
      phase: p5
      register: actions
      row: 3
  - workflow: webmail::WF_MARK_MESSAGE_V0
    node: CONFIRM_ANSWERED
    node_type: CC
    routing:
      SUCCESS: webmail::CC_DECIDE_READ_STATE_V0
      VIOLATION: RECORD_REFUSED
    source_finding: *id003
    runs: webmail::CC_CONFIRM_PROVIDER_ANSWERED_V0
  - workflow: webmail::WF_MARK_MESSAGE_V0
    node: webmail::CC_DECIDE_READ_STATE_V0
    node_type: CC
    routing:
      SUCCESS: RECORD_MARKED
      VIOLATION: RECORD_REPORT_REFUSED
    source_finding: *id003
  - workflow: webmail::WF_MARK_MESSAGE_V0
    node: RECORD_MARKED
    node_type: CC
    routing:
      SUCCESS: EXIT_MARKED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: *id003
    runs: webmail::CC_RECORD_MAILBOX_REQUEST_V0
  - workflow: webmail::WF_MARK_MESSAGE_V0
    node: RECORD_REFUSED
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: *id003
    runs: webmail::CC_RECORD_MAILBOX_REQUEST_V0
  - workflow: webmail::WF_MARK_MESSAGE_V0
    node: RECORD_REPORT_REFUSED
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: *id003
    runs: webmail::CC_RECORD_MAILBOX_REQUEST_V0
  - workflow: webmail::WF_MARK_MESSAGE_V0
    node: EXIT_MARKED
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: *id003
  - workflow: webmail::WF_MARK_MESSAGE_V0
    node: EXIT_REFUSED
    node_type: EXIT
    routing: null
    source_finding: *id003
  - workflow: webmail::WF_MARK_MESSAGE_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
    source_finding: *id003
  - workflow: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    node: webmail::IN_REPORT_CHANGE_OUTCOME_V0
    node_type: IN
    routing:
      ACK: CONFIRM_ANSWERED
      NACK: EXIT_REJECTED
    source_finding: &id004
      phase: p5
      register: actions
      row: 4
  - workflow: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    node: CONFIRM_ANSWERED
    node_type: CC
    routing:
      SUCCESS: RECORD_CHANGED
      VIOLATION: RECORD_REFUSED
    source_finding: *id004
    runs: webmail::CC_CONFIRM_PROVIDER_ANSWERED_V0
  - workflow: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    node: RECORD_CHANGED
    node_type: CC
    routing:
      SUCCESS: EXIT_CHANGED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: *id004
    runs: webmail::CC_RECORD_MAILBOX_REQUEST_V0
  - workflow: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    node: RECORD_REFUSED
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: *id004
    runs: webmail::CC_RECORD_MAILBOX_REQUEST_V0
  - workflow: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    node: EXIT_CHANGED
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: *id004
  - workflow: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    node: EXIT_REFUSED
    node_type: EXIT
    routing: null
    source_finding: *id004
  - workflow: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
    source_finding: *id004
  cc_composition:
  - cc_code: webmail::CC_CONFIRM_PROVIDER_ANSWERED_V0
    step: '1'
    step_name: confirm_answered
    capability: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - value
    - allowed_set
    produces:
    - is_member
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        value: value
        allowed_set: allowed_set
      out:
        is_member: answered
  - cc_code: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    step: '1'
    step_name: choose_page
    capability: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - message_ids
    - page
    - page_size
    produces:
    - page_ids
    - more_exist
    - folder_empty
    - message_count
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        message_ids: message_ids
        page: page
        page_size: page_size
      out:
        page_ids: page_ids
        more_exist: more_exist
        folder_empty: folder_empty
        message_count: message_count
  - cc_code: webmail::CC_CHOOSE_MESSAGE_TEXT_V0
    step: '1'
    step_name: choose_text
    capability: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - parts
    produces:
    - text_part
    - text_displayable
    - shown_headers
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parts: parts
      out:
        text_part: text_part
        text_displayable: text_displayable
        shown_headers: shown_headers
  - cc_code: webmail::CC_DECIDE_READ_STATE_V0
    step: '1'
    step_name: decide_read_state
    capability: webmail::CT_PURE_DECIDE_READ_STATE_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - seen
    - wanted_read
    produces:
    - change
    - read_now
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        seen: seen
        wanted_read: wanted_read
      out:
        change: change
        read_now: read_now
  - cc_code: webmail::CC_RECORD_MAILBOX_REQUEST_V0
    step: '1'
    step_name: assemble_entry
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - fields
    produces:
    - record
    routing:
      SUCCESS: continue
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: fields
      out:
        record: entry
  - cc_code: webmail::CC_RECORD_MAILBOX_REQUEST_V0
    step: '2'
    step_name: append_entry
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    kind: CS
    operation: APPEND
    store: MAILBOX_RECORDS
    consumes:
    - record
    - stream_id
    - actor_id
    produces:
    - record_id
    - sequence_number
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        record: record
        stream_id: stream_id
        actor_id: actor_id
      out:
        record_id: record_id
        sequence_number: sequence_number
  step_bindings:
  - owner: webmail::CC_CONFIRM_PROVIDER_ANSWERED_V0
    step: confirm_answered
    direction: INPUT
    field: value
    bound_to: inputs.provider_answer
    source_finding:
      phase: p5
      register: provisional_codes
      row: 10
  - owner: webmail::CC_CONFIRM_PROVIDER_ANSWERED_V0
    step: confirm_answered
    direction: INPUT
    field: allowed_set
    bound_to:
      literal:
      - ANSWERED
    source_finding:
      phase: p5
      register: provisional_codes
      row: 10
  - owner: webmail::CC_CONFIRM_PROVIDER_ANSWERED_V0
    step: confirm_answered
    direction: OUTPUT
    field: answered
    bound_to: capability_result.is_member
    source_finding:
      phase: p5
      register: provisional_codes
      row: 10
  - owner: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    step: choose_page
    direction: INPUT
    field: message_ids
    bound_to: inputs.message_ids
    source_finding:
      phase: p5
      register: provisional_codes
      row: 11
  - owner: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    step: choose_page
    direction: INPUT
    field: page
    bound_to: inputs.page
    source_finding:
      phase: p5
      register: provisional_codes
      row: 11
  - owner: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    step: choose_page
    direction: INPUT
    field: page_size
    bound_to:
      literal: 50
    source_finding:
      phase: p5
      register: provisional_codes
      row: 11
  - owner: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    step: choose_page
    direction: OUTPUT
    field: page_ids
    bound_to: capability_result.page_ids
    source_finding:
      phase: p5
      register: provisional_codes
      row: 11
  - owner: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    step: choose_page
    direction: OUTPUT
    field: more_exist
    bound_to: capability_result.more_exist
    source_finding:
      phase: p5
      register: provisional_codes
      row: 11
  - owner: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    step: choose_page
    direction: OUTPUT
    field: folder_empty
    bound_to: capability_result.folder_empty
    source_finding:
      phase: p5
      register: provisional_codes
      row: 11
  - owner: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    step: choose_page
    direction: OUTPUT
    field: message_count
    bound_to: capability_result.message_count
    source_finding:
      phase: p5
      register: provisional_codes
      row: 11
  - owner: webmail::CC_CHOOSE_MESSAGE_TEXT_V0
    step: choose_text
    direction: INPUT
    field: parts
    bound_to: inputs.parts
    source_finding:
      phase: p5
      register: provisional_codes
      row: 12
  - owner: webmail::CC_CHOOSE_MESSAGE_TEXT_V0
    step: choose_text
    direction: OUTPUT
    field: text_part
    bound_to: capability_result.text_part
    source_finding:
      phase: p5
      register: provisional_codes
      row: 12
  - owner: webmail::CC_CHOOSE_MESSAGE_TEXT_V0
    step: choose_text
    direction: OUTPUT
    field: text_displayable
    bound_to: capability_result.text_displayable
    source_finding:
      phase: p5
      register: provisional_codes
      row: 12
  - owner: webmail::CC_CHOOSE_MESSAGE_TEXT_V0
    step: choose_text
    direction: OUTPUT
    field: shown_headers
    bound_to: capability_result.shown_headers
    source_finding:
      phase: p5
      register: provisional_codes
      row: 12
  - owner: webmail::CC_DECIDE_READ_STATE_V0
    step: decide_read_state
    direction: INPUT
    field: seen
    bound_to: inputs.seen
    source_finding:
      phase: p5
      register: provisional_codes
      row: 13
  - owner: webmail::CC_DECIDE_READ_STATE_V0
    step: decide_read_state
    direction: INPUT
    field: wanted_read
    bound_to: inputs.wanted_read
    source_finding:
      phase: p5
      register: provisional_codes
      row: 13
  - owner: webmail::CC_DECIDE_READ_STATE_V0
    step: decide_read_state
    direction: OUTPUT
    field: change
    bound_to: capability_result.change
    source_finding:
      phase: p5
      register: provisional_codes
      row: 13
  - owner: webmail::CC_DECIDE_READ_STATE_V0
    step: decide_read_state
    direction: OUTPUT
    field: read_now
    bound_to: capability_result.read_now
    source_finding:
      phase: p5
      register: provisional_codes
      row: 13
  - owner: webmail::CC_RECORD_MAILBOX_REQUEST_V0
    step: assemble_entry
    direction: INPUT
    field: fields
    bound_to: inputs.entry
    source_finding:
      phase: p5
      register: provisional_codes
      row: 14
  - owner: webmail::CC_RECORD_MAILBOX_REQUEST_V0
    step: assemble_entry
    direction: OUTPUT
    field: entry
    bound_to: capability_result.record
    source_finding:
      phase: p5
      register: provisional_codes
      row: 14
  - owner: webmail::CC_RECORD_MAILBOX_REQUEST_V0
    step: append_entry
    direction: INPUT
    field: record
    bound_to: results.assemble_entry.entry
    source_finding:
      phase: p5
      register: provisional_codes
      row: 14
  - owner: webmail::CC_RECORD_MAILBOX_REQUEST_V0
    step: append_entry
    direction: INPUT
    field: stream_id
    bound_to:
      literal: MAILBOX_RECORDS
    source_finding:
      phase: p5
      register: provisional_codes
      row: 14
  - owner: webmail::CC_RECORD_MAILBOX_REQUEST_V0
    step: append_entry
    direction: INPUT
    field: actor_id
    bound_to: inputs.host_id
    source_finding:
      phase: p5
      register: provisional_codes
      row: 14
  - owner: webmail::CC_RECORD_MAILBOX_REQUEST_V0
    step: append_entry
    direction: OUTPUT
    field: record_id
    bound_to: capability_result.record_id
    source_finding:
      phase: p5
      register: provisional_codes
      row: 14
  - owner: webmail::CC_RECORD_MAILBOX_REQUEST_V0
    step: append_entry
    direction: OUTPUT
    field: sequence_number
    bound_to: capability_result.sequence_number
    source_finding:
      phase: p5
      register: provisional_codes
      row: 14
  - owner: webmail::WF_LIST_FOLDER_V0
    step: CONFIRM_ANSWERED
    direction: INPUT
    field: provider_answer
    bound_to: payload.provider_answer
    source_finding: *id001
  - owner: webmail::WF_LIST_FOLDER_V0
    step: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    direction: INPUT
    field: message_ids
    bound_to: payload.message_ids
    source_finding: *id001
  - owner: webmail::WF_LIST_FOLDER_V0
    step: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    direction: INPUT
    field: page
    bound_to: payload.page
    source_finding: *id001
  - owner: webmail::WF_LIST_FOLDER_V0
    step: RECORD_LISTED
    direction: INPUT
    field: host_id
    bound_to: payload.host_id
    source_finding: *id001
  - owner: webmail::WF_LIST_FOLDER_V0
    step: RECORD_LISTED
    direction: INPUT
    field: entry
    bound_to:
      literal:
        request: LIST_FOLDER
        mailbox: $.payload.mailbox
        folder: $.payload.folder
        outcome: ANSWERED
        provider_answer: $.payload.provider_answer
        page: $.payload.page
        page_ids: $.results.CC_CHOOSE_FOLDER_PAGE_V0.page_ids
        more_exist: $.results.CC_CHOOSE_FOLDER_PAGE_V0.more_exist
        folder_empty: $.results.CC_CHOOSE_FOLDER_PAGE_V0.folder_empty
        message_count: $.results.CC_CHOOSE_FOLDER_PAGE_V0.message_count
    source_finding: *id001
  - owner: webmail::WF_LIST_FOLDER_V0
    step: RECORD_REFUSED
    direction: INPUT
    field: host_id
    bound_to: payload.host_id
    source_finding: *id001
  - owner: webmail::WF_LIST_FOLDER_V0
    step: RECORD_REFUSED
    direction: INPUT
    field: entry
    bound_to:
      literal:
        request: LIST_FOLDER
        mailbox: $.payload.mailbox
        folder: $.payload.folder
        outcome: REFUSED
        provider_answer: $.payload.provider_answer
        reason: $.payload.provider_answer
    source_finding: *id001
  - owner: webmail::WF_LIST_FOLDER_V0
    step: RECORD_REPORT_REFUSED
    direction: INPUT
    field: host_id
    bound_to: payload.host_id
    source_finding: *id001
  - owner: webmail::WF_LIST_FOLDER_V0
    step: RECORD_REPORT_REFUSED
    direction: INPUT
    field: entry
    bound_to:
      literal:
        request: LIST_FOLDER
        mailbox: $.payload.mailbox
        folder: $.payload.folder
        outcome: REFUSED
        provider_answer: $.payload.provider_answer
        reason: REPORT_NOT_VALID
    source_finding: *id001
  - owner: webmail::WF_OPEN_MESSAGE_V0
    step: CONFIRM_ANSWERED
    direction: INPUT
    field: provider_answer
    bound_to: payload.provider_answer
    source_finding: *id002
  - owner: webmail::WF_OPEN_MESSAGE_V0
    step: webmail::CC_CHOOSE_MESSAGE_TEXT_V0
    direction: INPUT
    field: parts
    bound_to: payload.parts
    source_finding: *id002
  - owner: webmail::WF_OPEN_MESSAGE_V0
    step: webmail::CC_DECIDE_READ_STATE_V0
    direction: INPUT
    field: seen
    bound_to: payload.seen
    source_finding: *id002
  - owner: webmail::WF_OPEN_MESSAGE_V0
    step: webmail::CC_DECIDE_READ_STATE_V0
    direction: INPUT
    field: wanted_read
    bound_to:
      literal: true
    source_finding: *id002
  - owner: webmail::WF_OPEN_MESSAGE_V0
    step: RECORD_OPENED
    direction: INPUT
    field: host_id
    bound_to: payload.host_id
    source_finding: *id002
  - owner: webmail::WF_OPEN_MESSAGE_V0
    step: RECORD_OPENED
    direction: INPUT
    field: entry
    bound_to:
      literal:
        request: OPEN_MESSAGE
        mailbox: $.payload.mailbox
        folder: $.payload.folder
        outcome: ANSWERED
        provider_answer: $.payload.provider_answer
        message_id: $.payload.message_id
        text_part: $.results.CC_CHOOSE_MESSAGE_TEXT_V0.text_part
        text_displayable: $.results.CC_CHOOSE_MESSAGE_TEXT_V0.text_displayable
        shown_headers: $.results.CC_CHOOSE_MESSAGE_TEXT_V0.shown_headers
        change: $.results.CC_DECIDE_READ_STATE_V0.change
        read_now: $.results.CC_DECIDE_READ_STATE_V0.read_now
    source_finding: *id002
  - owner: webmail::WF_OPEN_MESSAGE_V0
    step: RECORD_REFUSED
    direction: INPUT
    field: host_id
    bound_to: payload.host_id
    source_finding: *id002
  - owner: webmail::WF_OPEN_MESSAGE_V0
    step: RECORD_REFUSED
    direction: INPUT
    field: entry
    bound_to:
      literal:
        request: OPEN_MESSAGE
        mailbox: $.payload.mailbox
        folder: $.payload.folder
        outcome: REFUSED
        provider_answer: $.payload.provider_answer
        reason: $.payload.provider_answer
        message_id: $.payload.message_id
    source_finding: *id002
  - owner: webmail::WF_OPEN_MESSAGE_V0
    step: RECORD_REPORT_REFUSED
    direction: INPUT
    field: host_id
    bound_to: payload.host_id
    source_finding: *id002
  - owner: webmail::WF_OPEN_MESSAGE_V0
    step: RECORD_REPORT_REFUSED
    direction: INPUT
    field: entry
    bound_to:
      literal:
        request: OPEN_MESSAGE
        mailbox: $.payload.mailbox
        folder: $.payload.folder
        outcome: REFUSED
        provider_answer: $.payload.provider_answer
        reason: REPORT_NOT_VALID
        message_id: $.payload.message_id
    source_finding: *id002
  - owner: webmail::WF_MARK_MESSAGE_V0
    step: CONFIRM_ANSWERED
    direction: INPUT
    field: provider_answer
    bound_to: payload.provider_answer
    source_finding: *id003
  - owner: webmail::WF_MARK_MESSAGE_V0
    step: webmail::CC_DECIDE_READ_STATE_V0
    direction: INPUT
    field: seen
    bound_to: payload.seen
    source_finding: *id003
  - owner: webmail::WF_MARK_MESSAGE_V0
    step: webmail::CC_DECIDE_READ_STATE_V0
    direction: INPUT
    field: wanted_read
    bound_to: payload.wanted_read
    source_finding: *id003
  - owner: webmail::WF_MARK_MESSAGE_V0
    step: RECORD_MARKED
    direction: INPUT
    field: host_id
    bound_to: payload.host_id
    source_finding: *id003
  - owner: webmail::WF_MARK_MESSAGE_V0
    step: RECORD_MARKED
    direction: INPUT
    field: entry
    bound_to:
      literal:
        request: MARK_MESSAGE
        mailbox: $.payload.mailbox
        folder: $.payload.folder
        outcome: ANSWERED
        provider_answer: $.payload.provider_answer
        message_id: $.payload.message_id
        wanted_read: $.payload.wanted_read
        change: $.results.CC_DECIDE_READ_STATE_V0.change
        read_now: $.results.CC_DECIDE_READ_STATE_V0.read_now
    source_finding: *id003
  - owner: webmail::WF_MARK_MESSAGE_V0
    step: RECORD_REFUSED
    direction: INPUT
    field: host_id
    bound_to: payload.host_id
    source_finding: *id003
  - owner: webmail::WF_MARK_MESSAGE_V0
    step: RECORD_REFUSED
    direction: INPUT
    field: entry
    bound_to:
      literal:
        request: MARK_MESSAGE
        mailbox: $.payload.mailbox
        folder: $.payload.folder
        outcome: REFUSED
        provider_answer: $.payload.provider_answer
        reason: $.payload.provider_answer
        message_id: $.payload.message_id
    source_finding: *id003
  - owner: webmail::WF_MARK_MESSAGE_V0
    step: RECORD_REPORT_REFUSED
    direction: INPUT
    field: host_id
    bound_to: payload.host_id
    source_finding: *id003
  - owner: webmail::WF_MARK_MESSAGE_V0
    step: RECORD_REPORT_REFUSED
    direction: INPUT
    field: entry
    bound_to:
      literal:
        request: MARK_MESSAGE
        mailbox: $.payload.mailbox
        folder: $.payload.folder
        outcome: REFUSED
        provider_answer: $.payload.provider_answer
        reason: REPORT_NOT_VALID
        message_id: $.payload.message_id
    source_finding: *id003
  - owner: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    step: CONFIRM_ANSWERED
    direction: INPUT
    field: provider_answer
    bound_to: payload.provider_answer
    source_finding: *id004
  - owner: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    step: RECORD_CHANGED
    direction: INPUT
    field: host_id
    bound_to: payload.host_id
    source_finding: *id004
  - owner: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    step: RECORD_CHANGED
    direction: INPUT
    field: entry
    bound_to:
      literal:
        request: REPORT_CHANGE_OUTCOME
        mailbox: $.payload.mailbox
        folder: $.payload.folder
        outcome: ANSWERED
        provider_answer: $.payload.provider_answer
        message_id: $.payload.message_id
        change: $.payload.change
    source_finding: *id004
  - owner: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    step: RECORD_REFUSED
    direction: INPUT
    field: host_id
    bound_to: payload.host_id
    source_finding: *id004
  - owner: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    step: RECORD_REFUSED
    direction: INPUT
    field: entry
    bound_to:
      literal:
        request: REPORT_CHANGE_OUTCOME
        mailbox: $.payload.mailbox
        folder: $.payload.folder
        outcome: REFUSED
        provider_answer: $.payload.provider_answer
        reason: $.payload.provider_answer
        message_id: $.payload.message_id
    source_finding: *id004
  interface_fields:
  - artifact: webmail::AC_MAIL_HOST_V0
    direction: ATTRIBUTE
    field: host_id
    type: string
    required: 'YES'
    default: null
    meaning: Which host is calling
  - artifact: webmail::IN_LIST_FOLDER_V0
    direction: INPUT
    field: host_id
    type: string
    required: 'YES'
    default: null
    meaning: Which host reports
  - artifact: webmail::IN_LIST_FOLDER_V0
    direction: INPUT
    field: mailbox
    type: string
    required: 'YES'
    default: null
    meaning: The mailbox the request concerns, which also says who asked
  - artifact: webmail::IN_LIST_FOLDER_V0
    direction: INPUT
    field: folder
    type: string
    required: 'YES'
    default: null
    meaning: The folder the request concerns
  - artifact: webmail::IN_LIST_FOLDER_V0
    direction: INPUT
    field: provider_answer
    type: string
    required: 'YES'
    default: null
    meaning: 'What the provider answered: ANSWERED, CREDENTIALS_REJECTED, UNREACHABLE, NO_SUCH_FOLDER or NO_SUCH_MESSAGE'
  - artifact: webmail::IN_LIST_FOLDER_V0
    direction: INPUT
    field: message_ids
    type: array
    required: 'YES'
    default: null
    meaning: The folder's message identifiers, in the order the provider received them
  - artifact: webmail::IN_LIST_FOLDER_V0
    direction: INPUT
    field: page
    type: integer
    required: 'YES'
    default: null
    meaning: The page asked for, counting from 1
  - artifact: webmail::IN_OPEN_MESSAGE_V0
    direction: INPUT
    field: host_id
    type: string
    required: 'YES'
    default: null
    meaning: Which host reports
  - artifact: webmail::IN_OPEN_MESSAGE_V0
    direction: INPUT
    field: mailbox
    type: string
    required: 'YES'
    default: null
    meaning: The mailbox the request concerns, which also says who asked
  - artifact: webmail::IN_OPEN_MESSAGE_V0
    direction: INPUT
    field: folder
    type: string
    required: 'YES'
    default: null
    meaning: The folder the request concerns
  - artifact: webmail::IN_OPEN_MESSAGE_V0
    direction: INPUT
    field: provider_answer
    type: string
    required: 'YES'
    default: null
    meaning: 'What the provider answered: ANSWERED, CREDENTIALS_REJECTED, UNREACHABLE, NO_SUCH_FOLDER or NO_SUCH_MESSAGE'
  - artifact: webmail::IN_OPEN_MESSAGE_V0
    direction: INPUT
    field: message_id
    type: integer
    required: 'YES'
    default: null
    meaning: The message asked for
  - artifact: webmail::IN_OPEN_MESSAGE_V0
    direction: INPUT
    field: seen
    type: boolean
    required: 'YES'
    default: null
    meaning: Whether the provider holds the message as read
  - artifact: webmail::IN_OPEN_MESSAGE_V0
    direction: INPUT
    field: parts
    type: array
    required: 'YES'
    default: null
    meaning: The message's parts, each with its part number and kind, and none of its content
  - artifact: webmail::IN_MARK_MESSAGE_V0
    direction: INPUT
    field: host_id
    type: string
    required: 'YES'
    default: null
    meaning: Which host reports
  - artifact: webmail::IN_MARK_MESSAGE_V0
    direction: INPUT
    field: mailbox
    type: string
    required: 'YES'
    default: null
    meaning: The mailbox the request concerns, which also says who asked
  - artifact: webmail::IN_MARK_MESSAGE_V0
    direction: INPUT
    field: folder
    type: string
    required: 'YES'
    default: null
    meaning: The folder the request concerns
  - artifact: webmail::IN_MARK_MESSAGE_V0
    direction: INPUT
    field: provider_answer
    type: string
    required: 'YES'
    default: null
    meaning: 'What the provider answered: ANSWERED, CREDENTIALS_REJECTED, UNREACHABLE, NO_SUCH_FOLDER or NO_SUCH_MESSAGE'
  - artifact: webmail::IN_MARK_MESSAGE_V0
    direction: INPUT
    field: message_id
    type: integer
    required: 'YES'
    default: null
    meaning: The message asked for
  - artifact: webmail::IN_MARK_MESSAGE_V0
    direction: INPUT
    field: seen
    type: boolean
    required: 'YES'
    default: null
    meaning: Whether the provider holds the message as read
  - artifact: webmail::IN_MARK_MESSAGE_V0
    direction: INPUT
    field: wanted_read
    type: boolean
    required: 'YES'
    default: null
    meaning: Whether the person asked for the message to be read
  - artifact: webmail::IN_REPORT_CHANGE_OUTCOME_V0
    direction: INPUT
    field: host_id
    type: string
    required: 'YES'
    default: null
    meaning: Which host reports
  - artifact: webmail::IN_REPORT_CHANGE_OUTCOME_V0
    direction: INPUT
    field: mailbox
    type: string
    required: 'YES'
    default: null
    meaning: The mailbox the request concerns, which also says who asked
  - artifact: webmail::IN_REPORT_CHANGE_OUTCOME_V0
    direction: INPUT
    field: folder
    type: string
    required: 'YES'
    default: null
    meaning: The folder the request concerns
  - artifact: webmail::IN_REPORT_CHANGE_OUTCOME_V0
    direction: INPUT
    field: provider_answer
    type: string
    required: 'YES'
    default: null
    meaning: 'What the provider answered: ANSWERED, CREDENTIALS_REJECTED, UNREACHABLE, NO_SUCH_FOLDER or NO_SUCH_MESSAGE'
  - artifact: webmail::IN_REPORT_CHANGE_OUTCOME_V0
    direction: INPUT
    field: message_id
    type: integer
    required: 'YES'
    default: null
    meaning: The message the change concerned
  - artifact: webmail::IN_REPORT_CHANGE_OUTCOME_V0
    direction: INPUT
    field: change
    type: string
    required: 'YES'
    default: null
    meaning: 'The change the business decided: SET_READ or SET_UNREAD'
  - artifact: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    direction: INPUT
    field: message_ids
    type: array
    required: 'YES'
    default: null
    meaning: The folder's message identifiers, in the order the provider received them
  - artifact: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    direction: INPUT
    field: page
    type: integer
    required: 'YES'
    default: null
    meaning: The page asked for, counting from 1
  - artifact: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    direction: INPUT
    field: page_size
    type: integer
    required: 'YES'
    default: null
    meaning: How many messages make one page
  - artifact: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    direction: OUTPUT
    field: page_ids
    type: array
    required: 'YES'
    default: null
    meaning: The identifiers of the page, newest received first
  - artifact: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    direction: OUTPUT
    field: more_exist
    type: boolean
    required: 'YES'
    default: null
    meaning: Whether messages exist beyond this page
  - artifact: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    direction: OUTPUT
    field: folder_empty
    type: boolean
    required: 'YES'
    default: null
    meaning: Whether the folder holds no messages
  - artifact: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    direction: OUTPUT
    field: message_count
    type: integer
    required: 'YES'
    default: null
    meaning: How many messages the folder holds
  - artifact: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    direction: INPUT
    field: parts
    type: array
    required: 'YES'
    default: null
    meaning: The message's parts, each with its part number and kind
  - artifact: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    direction: OUTPUT
    field: text_part
    type: string
    required: 'YES'
    default: null
    meaning: The part number of the plain text shown, or empty when there is none
  - artifact: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    direction: OUTPUT
    field: text_displayable
    type: boolean
    required: 'YES'
    default: null
    meaning: Whether the message has plain text to show
  - artifact: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    direction: OUTPUT
    field: shown_headers
    type: array
    required: 'YES'
    default: null
    meaning: The headers shown with the message
  - artifact: webmail::CT_PURE_DECIDE_READ_STATE_V0
    direction: INPUT
    field: seen
    type: boolean
    required: 'YES'
    default: null
    meaning: Whether the provider holds the message as read
  - artifact: webmail::CT_PURE_DECIDE_READ_STATE_V0
    direction: INPUT
    field: wanted_read
    type: boolean
    required: 'YES'
    default: null
    meaning: Whether the message is to be read
  - artifact: webmail::CT_PURE_DECIDE_READ_STATE_V0
    direction: OUTPUT
    field: change
    type: string
    required: 'YES'
    default: null
    meaning: SET_READ, SET_UNREAD or NONE
  - artifact: webmail::CT_PURE_DECIDE_READ_STATE_V0
    direction: OUTPUT
    field: read_now
    type: boolean
    required: 'YES'
    default: null
    meaning: Whether the message is read once the decision is carried out
  - artifact: webmail::CC_CONFIRM_PROVIDER_ANSWERED_V0
    direction: INPUT
    field: provider_answer
    type: string
    required: 'YES'
    default: null
    meaning: What the provider answered
  - artifact: webmail::CC_CONFIRM_PROVIDER_ANSWERED_V0
    direction: OUTPUT
    field: answered
    type: boolean
    required: 'YES'
    default: null
    meaning: Whether the provider answered
  - artifact: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    direction: INPUT
    field: message_ids
    type: array
    required: 'YES'
    default: null
    meaning: The folder's message identifiers, in received order
  - artifact: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    direction: INPUT
    field: page
    type: integer
    required: 'YES'
    default: null
    meaning: The page asked for
  - artifact: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    direction: OUTPUT
    field: page_ids
    type: array
    required: 'YES'
    default: null
    meaning: The identifiers of the page
  - artifact: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    direction: OUTPUT
    field: more_exist
    type: boolean
    required: 'YES'
    default: null
    meaning: Whether more exist
  - artifact: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    direction: OUTPUT
    field: folder_empty
    type: boolean
    required: 'YES'
    default: null
    meaning: Whether the folder is empty
  - artifact: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    direction: OUTPUT
    field: message_count
    type: integer
    required: 'YES'
    default: null
    meaning: How many the folder holds
  - artifact: webmail::CC_CHOOSE_MESSAGE_TEXT_V0
    direction: INPUT
    field: parts
    type: array
    required: 'YES'
    default: null
    meaning: The message's parts
  - artifact: webmail::CC_CHOOSE_MESSAGE_TEXT_V0
    direction: OUTPUT
    field: text_part
    type: string
    required: 'YES'
    default: null
    meaning: The plain-text part shown
  - artifact: webmail::CC_CHOOSE_MESSAGE_TEXT_V0
    direction: OUTPUT
    field: text_displayable
    type: boolean
    required: 'YES'
    default: null
    meaning: Whether there is plain text
  - artifact: webmail::CC_CHOOSE_MESSAGE_TEXT_V0
    direction: OUTPUT
    field: shown_headers
    type: array
    required: 'YES'
    default: null
    meaning: The headers shown
  - artifact: webmail::CC_DECIDE_READ_STATE_V0
    direction: INPUT
    field: seen
    type: boolean
    required: 'YES'
    default: null
    meaning: Whether the message is read
  - artifact: webmail::CC_DECIDE_READ_STATE_V0
    direction: INPUT
    field: wanted_read
    type: boolean
    required: 'YES'
    default: null
    meaning: Whether it is to be read
  - artifact: webmail::CC_DECIDE_READ_STATE_V0
    direction: OUTPUT
    field: change
    type: string
    required: 'YES'
    default: null
    meaning: The change decided
  - artifact: webmail::CC_DECIDE_READ_STATE_V0
    direction: OUTPUT
    field: read_now
    type: boolean
    required: 'YES'
    default: null
    meaning: Whether it is read once carried out
  - artifact: webmail::CC_RECORD_MAILBOX_REQUEST_V0
    direction: INPUT
    field: entry
    type: object
    required: 'YES'
    default: null
    meaning: What was asked, decided and answered, by identifier only
  - artifact: webmail::CC_RECORD_MAILBOX_REQUEST_V0
    direction: INPUT
    field: host_id
    type: string
    required: 'YES'
    default: null
    meaning: Which host reported
  - artifact: webmail::CC_RECORD_MAILBOX_REQUEST_V0
    direction: OUTPUT
    field: entry
    type: object
    required: 'YES'
    default: null
    meaning: The entry added
  - artifact: webmail::CC_RECORD_MAILBOX_REQUEST_V0
    direction: OUTPUT
    field: record_id
    type: string
    required: 'YES'
    default: null
    meaning: The entry's record identifier
  - artifact: webmail::CC_RECORD_MAILBOX_REQUEST_V0
    direction: OUTPUT
    field: sequence_number
    type: integer
    required: 'YES'
    default: null
    meaning: The entry's place in the record
  - artifact: webmail::EV_FOLDER_LISTED_V0
    direction: OUTPUT
    field: entry
    type: object
    required: 'YES'
    default: null
    meaning: The record entry, by identifier only
  - artifact: webmail::EV_FOLDER_LISTED_V0
    direction: OUTPUT
    field: sequence_number
    type: integer
    required: 'YES'
    default: null
    meaning: The entry's place in the record
  - artifact: webmail::EV_MESSAGE_OPENED_V0
    direction: OUTPUT
    field: entry
    type: object
    required: 'YES'
    default: null
    meaning: The record entry, by identifier only
  - artifact: webmail::EV_MESSAGE_OPENED_V0
    direction: OUTPUT
    field: sequence_number
    type: integer
    required: 'YES'
    default: null
    meaning: The entry's place in the record
  - artifact: webmail::EV_READ_STATE_CHANGED_V0
    direction: OUTPUT
    field: entry
    type: object
    required: 'YES'
    default: null
    meaning: The record entry, by identifier only
  - artifact: webmail::EV_READ_STATE_CHANGED_V0
    direction: OUTPUT
    field: sequence_number
    type: integer
    required: 'YES'
    default: null
    meaning: The entry's place in the record
  - artifact: webmail::EV_MAILBOX_REQUEST_REFUSED_V0
    direction: OUTPUT
    field: entry
    type: object
    required: 'YES'
    default: null
    meaning: The record entry, by identifier only
  - artifact: webmail::EV_MAILBOX_REQUEST_REFUSED_V0
    direction: OUTPUT
    field: sequence_number
    type: integer
    required: 'YES'
    default: null
    meaning: The entry's place in the record
  implementation_bindings:
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    callable: execute
    operation: CHOOSE_FOLDER_PAGE
    kind: atom
    purity: ct_pure
    refusal: raises
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    callable: execute
    operation: CHOOSE_MESSAGE_TEXT
    kind: atom
    purity: ct_pure
    refusal: raises
    source_finding:
      phase: p5
      register: provisional_codes
      row: 16
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    callable: execute
    operation: DECIDE_READ_STATE
    kind: atom
    purity: ct_pure
    refusal: raises
    source_finding:
      phase: p5
      register: provisional_codes
      row: 17
  vocabulary_extensions: []
  runtime_policies:
  - rb_code: webmail::RB_MAILBOX_BINDINGS_V0
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    key: structure
    value: webmail::STRUCTURE_MAILBOX_STORAGE_V0
    source_finding:
      phase: p5
      register: provisional_codes
      row: 23
  artifact_properties:
  - artifact: webmail::AC_MAIL_HOST_V0
    property: type
    value: system
    source_finding:
      phase: p5
      register: provisional_codes
      row: 1
  - artifact: webmail::EV_MAILBOX_REQUEST_REFUSED_V0
    property: moment
    value: refusal
    source_finding:
      phase: p5
      register: provisional_codes
      row: 21
  - artifact: webmail::WF_LIST_FOLDER_V0
    property: emit.EXIT_LISTED
    value:
    - webmail::EV_FOLDER_LISTED_V0
    source_finding: *id001
  - artifact: webmail::WF_LIST_FOLDER_V0
    property: emit.EXIT_REFUSED
    value:
    - webmail::EV_MAILBOX_REQUEST_REFUSED_V0
    source_finding: *id001
  - artifact: webmail::WF_LIST_FOLDER_V0
    property: actor_context
    value: webmail::AC_MAIL_HOST_V0
    source_finding: *id001
  - artifact: webmail::WF_OPEN_MESSAGE_V0
    property: emit.EXIT_OPENED
    value:
    - webmail::EV_MESSAGE_OPENED_V0
    source_finding: *id002
  - artifact: webmail::WF_OPEN_MESSAGE_V0
    property: emit.EXIT_REFUSED
    value:
    - webmail::EV_MAILBOX_REQUEST_REFUSED_V0
    source_finding: *id002
  - artifact: webmail::WF_OPEN_MESSAGE_V0
    property: actor_context
    value: webmail::AC_MAIL_HOST_V0
    source_finding: *id002
  - artifact: webmail::WF_MARK_MESSAGE_V0
    property: emit.EXIT_REFUSED
    value:
    - webmail::EV_MAILBOX_REQUEST_REFUSED_V0
    source_finding: *id003
  - artifact: webmail::WF_MARK_MESSAGE_V0
    property: actor_context
    value: webmail::AC_MAIL_HOST_V0
    source_finding: *id003
  - artifact: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    property: emit.EXIT_CHANGED
    value:
    - webmail::EV_READ_STATE_CHANGED_V0
    source_finding: *id004
  - artifact: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    property: emit.EXIT_REFUSED
    value:
    - webmail::EV_MAILBOX_REQUEST_REFUSED_V0
    source_finding: *id004
  - artifact: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    property: actor_context
    value: webmail::AC_MAIL_HOST_V0
    source_finding: *id004
  - artifact: webmail::STRUCTURE_MAILBOX_STORAGE_V0
    property: layer
    value: DOMAINS
    source_finding:
      phase: p5
      register: provisional_codes
      row: 22
  structure_stores:
  - store_name: MAILBOX_RECORDS
    storage_type: CS_APPENDONLY_JSONL_V0
    proposed_path: webmail/mailbox/mailbox_records.jsonl
    used_by: webmail::CC_RECORD_MAILBOX_REQUEST_V0
    structure: webmail::STRUCTURE_MAILBOX_STORAGE_V0
    source_finding:
      phase: p6
      register: storage_governance
      row: 1
  transport_bindings: []
  artifact_summary:
  - action: NEW
    subdomain: mailbox
    count: '23'
    artifacts: webmail::AC_MAIL_HOST_V0, webmail::CC_CHOOSE_FOLDER_PAGE_V0, webmail::CC_CHOOSE_MESSAGE_TEXT_V0, webmail::CC_CONFIRM_PROVIDER_ANSWERED_V0,
      webmail::CC_DECIDE_READ_STATE_V0, webmail::CC_RECORD_MAILBOX_REQUEST_V0, webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0, webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0,
      webmail::CT_PURE_DECIDE_READ_STATE_V0, webmail::EV_FOLDER_LISTED_V0, webmail::EV_MAILBOX_REQUEST_REFUSED_V0, webmail::EV_MESSAGE_OPENED_V0,
      webmail::EV_READ_STATE_CHANGED_V0, webmail::IN_LIST_FOLDER_V0, webmail::IN_MARK_MESSAGE_V0, webmail::IN_OPEN_MESSAGE_V0,
      webmail::IN_REPORT_CHANGE_OUTCOME_V0, webmail::RB_MAILBOX_BINDINGS_V0, webmail::STRUCTURE_MAILBOX_STORAGE_V0, webmail::WF_LIST_FOLDER_V0,
      webmail::WF_MARK_MESSAGE_V0, webmail::WF_OPEN_MESSAGE_V0, webmail::WF_REPORT_CHANGE_OUTCOME_V0
  generation_provenance: []
  declared_reach: []
  refusal_discharge:
  - operation: list a folder, open a message, mark a message
    refused_when: the provider rejects the person's credentials
    act: webmail::WF_LIST_FOLDER_V0
    step: RECORD_REFUSED
    outcome: SUCCESS
    source_finding:
      phase: p0
      register: operation_refusals
      row: 1
  - operation: list a folder, open a message, mark a message
    refused_when: the provider rejects the person's credentials
    act: webmail::WF_OPEN_MESSAGE_V0
    step: RECORD_REFUSED
    outcome: SUCCESS
    source_finding:
      phase: p0
      register: operation_refusals
      row: 1
  - operation: list a folder, open a message, mark a message
    refused_when: the provider rejects the person's credentials
    act: webmail::WF_MARK_MESSAGE_V0
    step: RECORD_REFUSED
    outcome: SUCCESS
    source_finding:
      phase: p0
      register: operation_refusals
      row: 1
  - operation: list a folder, open a message, mark a message
    refused_when: the provider cannot be reached, or does not answer in time
    act: webmail::WF_LIST_FOLDER_V0
    step: RECORD_REFUSED
    outcome: SUCCESS
    source_finding:
      phase: p0
      register: operation_refusals
      row: 2
  - operation: list a folder, open a message, mark a message
    refused_when: the provider cannot be reached, or does not answer in time
    act: webmail::WF_OPEN_MESSAGE_V0
    step: RECORD_REFUSED
    outcome: SUCCESS
    source_finding:
      phase: p0
      register: operation_refusals
      row: 2
  - operation: list a folder, open a message, mark a message
    refused_when: the provider cannot be reached, or does not answer in time
    act: webmail::WF_MARK_MESSAGE_V0
    step: RECORD_REFUSED
    outcome: SUCCESS
    source_finding:
      phase: p0
      register: operation_refusals
      row: 2
  - operation: list a folder, open a message, mark a message
    refused_when: the folder does not exist
    act: webmail::WF_LIST_FOLDER_V0
    step: RECORD_REFUSED
    outcome: SUCCESS
    source_finding:
      phase: p0
      register: operation_refusals
      row: 3
  - operation: list a folder, open a message, mark a message
    refused_when: the folder does not exist
    act: webmail::WF_OPEN_MESSAGE_V0
    step: RECORD_REFUSED
    outcome: SUCCESS
    source_finding:
      phase: p0
      register: operation_refusals
      row: 3
  - operation: list a folder, open a message, mark a message
    refused_when: the folder does not exist
    act: webmail::WF_MARK_MESSAGE_V0
    step: RECORD_REFUSED
    outcome: SUCCESS
    source_finding:
      phase: p0
      register: operation_refusals
      row: 3
  - operation: open a message, mark a message
    refused_when: the message does not exist in the folder
    act: webmail::WF_OPEN_MESSAGE_V0
    step: RECORD_REFUSED
    outcome: SUCCESS
    source_finding:
      phase: p0
      register: operation_refusals
      row: 4
  - operation: open a message, mark a message
    refused_when: the message does not exist in the folder
    act: webmail::WF_MARK_MESSAGE_V0
    step: RECORD_REFUSED
    outcome: SUCCESS
    source_finding:
      phase: p0
      register: operation_refusals
      row: 4
  refusal_deferrals: []
  refusal_governance_discharge: []
  molecule_steps: []
  molecule_step_bindings: []
  test_cases:
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: first_page_is_newest_received_first
    expected_outcome: SUCCESS
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: last_page_says_no_more_exist
    expected_outcome: SUCCESS
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: received_order_decides_not_the_identifier
    expected_outcome: SUCCESS
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: empty_folder_answers_empty
    expected_outcome: SUCCESS
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: a_page_before_the_first_is_refused
    expected_outcome: VIOLATION
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: an_identifier_that_is_not_a_number_is_refused
    expected_outcome: VIOLATION
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: plain_text_part_is_chosen
    expected_outcome: SUCCESS
    source_finding:
      phase: p5
      register: provisional_codes
      row: 16
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: first_plain_text_part_wins
    expected_outcome: SUCCESS
    source_finding:
      phase: p5
      register: provisional_codes
      row: 16
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: kind_is_read_without_regard_to_case
    expected_outcome: SUCCESS
    source_finding:
      phase: p5
      register: provisional_codes
      row: 16
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: html_only_cannot_be_displayed_yet
    expected_outcome: SUCCESS
    source_finding:
      phase: p5
      register: provisional_codes
      row: 16
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: a_part_without_a_kind_is_refused
    expected_outcome: VIOLATION
    source_finding:
      phase: p5
      register: provisional_codes
      row: 16
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: unread_asked_read_becomes_read
    expected_outcome: SUCCESS
    source_finding:
      phase: p5
      register: provisional_codes
      row: 17
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: read_asked_unread_becomes_unread
    expected_outcome: SUCCESS
    source_finding:
      phase: p5
      register: provisional_codes
      row: 17
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: read_asked_read_changes_nothing
    expected_outcome: SUCCESS
    source_finding:
      phase: p5
      register: provisional_codes
      row: 17
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: unread_asked_unread_changes_nothing
    expected_outcome: SUCCESS
    source_finding:
      phase: p5
      register: provisional_codes
      row: 17
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: a_state_that_is_not_true_or_false_is_refused
    expected_outcome: VIOLATION
    source_finding:
      phase: p5
      register: provisional_codes
      row: 17
  test_case_values:
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: first_page_is_newest_received_first
    role: INPUT
    field: message_ids
    value:
    - 3
    - 7
    - 9
    - 12
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: first_page_is_newest_received_first
    role: INPUT
    field: page
    value: 1
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: first_page_is_newest_received_first
    role: INPUT
    field: page_size
    value: 2
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: first_page_is_newest_received_first
    role: EXPECTED
    field: page_ids
    value:
    - 12
    - 9
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: first_page_is_newest_received_first
    role: EXPECTED
    field: more_exist
    value: true
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: first_page_is_newest_received_first
    role: EXPECTED
    field: folder_empty
    value: false
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: first_page_is_newest_received_first
    role: EXPECTED
    field: message_count
    value: 4
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: last_page_says_no_more_exist
    role: INPUT
    field: message_ids
    value:
    - 3
    - 7
    - 9
    - 12
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: last_page_says_no_more_exist
    role: INPUT
    field: page
    value: 2
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: last_page_says_no_more_exist
    role: INPUT
    field: page_size
    value: 2
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: last_page_says_no_more_exist
    role: EXPECTED
    field: page_ids
    value:
    - 7
    - 3
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: last_page_says_no_more_exist
    role: EXPECTED
    field: more_exist
    value: false
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: last_page_says_no_more_exist
    role: EXPECTED
    field: folder_empty
    value: false
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: last_page_says_no_more_exist
    role: EXPECTED
    field: message_count
    value: 4
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: received_order_decides_not_the_identifier
    role: INPUT
    field: message_ids
    value:
    - 40
    - 5
    - 22
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: received_order_decides_not_the_identifier
    role: INPUT
    field: page
    value: 1
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: received_order_decides_not_the_identifier
    role: INPUT
    field: page_size
    value: 50
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: received_order_decides_not_the_identifier
    role: EXPECTED
    field: page_ids
    value:
    - 22
    - 5
    - 40
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: received_order_decides_not_the_identifier
    role: EXPECTED
    field: more_exist
    value: false
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: received_order_decides_not_the_identifier
    role: EXPECTED
    field: folder_empty
    value: false
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: received_order_decides_not_the_identifier
    role: EXPECTED
    field: message_count
    value: 3
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: empty_folder_answers_empty
    role: INPUT
    field: message_ids
    value: []
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: empty_folder_answers_empty
    role: INPUT
    field: page
    value: 1
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: empty_folder_answers_empty
    role: INPUT
    field: page_size
    value: 50
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: empty_folder_answers_empty
    role: EXPECTED
    field: page_ids
    value: []
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: empty_folder_answers_empty
    role: EXPECTED
    field: more_exist
    value: false
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: empty_folder_answers_empty
    role: EXPECTED
    field: folder_empty
    value: true
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: empty_folder_answers_empty
    role: EXPECTED
    field: message_count
    value: 0
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: a_page_before_the_first_is_refused
    role: INPUT
    field: message_ids
    value:
    - 1
    - 2
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: a_page_before_the_first_is_refused
    role: INPUT
    field: page
    value: 0
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: a_page_before_the_first_is_refused
    role: INPUT
    field: page_size
    value: 50
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: an_identifier_that_is_not_a_number_is_refused
    role: INPUT
    field: message_ids
    value:
    - 1
    - two
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: an_identifier_that_is_not_a_number_is_refused
    role: INPUT
    field: page
    value: 1
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: an_identifier_that_is_not_a_number_is_refused
    role: INPUT
    field: page_size
    value: 50
    source_finding:
      phase: p5
      register: provisional_codes
      row: 15
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: plain_text_part_is_chosen
    role: INPUT
    field: parts
    value:
    - part: '1'
      kind: text/plain
    - part: '2'
      kind: text/html
    source_finding:
      phase: p5
      register: provisional_codes
      row: 16
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: plain_text_part_is_chosen
    role: EXPECTED
    field: text_part
    value: '1'
    source_finding:
      phase: p5
      register: provisional_codes
      row: 16
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: plain_text_part_is_chosen
    role: EXPECTED
    field: text_displayable
    value: true
    source_finding:
      phase: p5
      register: provisional_codes
      row: 16
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: plain_text_part_is_chosen
    role: EXPECTED
    field: shown_headers
    value:
    - from
    - to
    - cc
    - subject
    - date
    source_finding:
      phase: p5
      register: provisional_codes
      row: 16
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: first_plain_text_part_wins
    role: INPUT
    field: parts
    value:
    - part: '1.1'
      kind: text/plain
    - part: '2'
      kind: text/plain
    source_finding:
      phase: p5
      register: provisional_codes
      row: 16
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: first_plain_text_part_wins
    role: EXPECTED
    field: text_part
    value: '1.1'
    source_finding:
      phase: p5
      register: provisional_codes
      row: 16
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: first_plain_text_part_wins
    role: EXPECTED
    field: text_displayable
    value: true
    source_finding:
      phase: p5
      register: provisional_codes
      row: 16
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: first_plain_text_part_wins
    role: EXPECTED
    field: shown_headers
    value:
    - from
    - to
    - cc
    - subject
    - date
    source_finding:
      phase: p5
      register: provisional_codes
      row: 16
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: kind_is_read_without_regard_to_case
    role: INPUT
    field: parts
    value:
    - part: '1'
      kind: TEXT/PLAIN
    source_finding:
      phase: p5
      register: provisional_codes
      row: 16
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: kind_is_read_without_regard_to_case
    role: EXPECTED
    field: text_part
    value: '1'
    source_finding:
      phase: p5
      register: provisional_codes
      row: 16
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: kind_is_read_without_regard_to_case
    role: EXPECTED
    field: text_displayable
    value: true
    source_finding:
      phase: p5
      register: provisional_codes
      row: 16
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: kind_is_read_without_regard_to_case
    role: EXPECTED
    field: shown_headers
    value:
    - from
    - to
    - cc
    - subject
    - date
    source_finding:
      phase: p5
      register: provisional_codes
      row: 16
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: html_only_cannot_be_displayed_yet
    role: INPUT
    field: parts
    value:
    - part: '1'
      kind: text/html
    source_finding:
      phase: p5
      register: provisional_codes
      row: 16
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: html_only_cannot_be_displayed_yet
    role: EXPECTED
    field: text_part
    value: ''
    source_finding:
      phase: p5
      register: provisional_codes
      row: 16
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: html_only_cannot_be_displayed_yet
    role: EXPECTED
    field: text_displayable
    value: false
    source_finding:
      phase: p5
      register: provisional_codes
      row: 16
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: html_only_cannot_be_displayed_yet
    role: EXPECTED
    field: shown_headers
    value:
    - from
    - to
    - cc
    - subject
    - date
    source_finding:
      phase: p5
      register: provisional_codes
      row: 16
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: a_part_without_a_kind_is_refused
    role: INPUT
    field: parts
    value:
    - part: '1'
    source_finding:
      phase: p5
      register: provisional_codes
      row: 16
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: unread_asked_read_becomes_read
    role: INPUT
    field: seen
    value: false
    source_finding:
      phase: p5
      register: provisional_codes
      row: 17
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: unread_asked_read_becomes_read
    role: INPUT
    field: wanted_read
    value: true
    source_finding:
      phase: p5
      register: provisional_codes
      row: 17
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: unread_asked_read_becomes_read
    role: EXPECTED
    field: change
    value: SET_READ
    source_finding:
      phase: p5
      register: provisional_codes
      row: 17
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: unread_asked_read_becomes_read
    role: EXPECTED
    field: read_now
    value: true
    source_finding:
      phase: p5
      register: provisional_codes
      row: 17
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: read_asked_unread_becomes_unread
    role: INPUT
    field: seen
    value: true
    source_finding:
      phase: p5
      register: provisional_codes
      row: 17
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: read_asked_unread_becomes_unread
    role: INPUT
    field: wanted_read
    value: false
    source_finding:
      phase: p5
      register: provisional_codes
      row: 17
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: read_asked_unread_becomes_unread
    role: EXPECTED
    field: change
    value: SET_UNREAD
    source_finding:
      phase: p5
      register: provisional_codes
      row: 17
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: read_asked_unread_becomes_unread
    role: EXPECTED
    field: read_now
    value: false
    source_finding:
      phase: p5
      register: provisional_codes
      row: 17
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: read_asked_read_changes_nothing
    role: INPUT
    field: seen
    value: true
    source_finding:
      phase: p5
      register: provisional_codes
      row: 17
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: read_asked_read_changes_nothing
    role: INPUT
    field: wanted_read
    value: true
    source_finding:
      phase: p5
      register: provisional_codes
      row: 17
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: read_asked_read_changes_nothing
    role: EXPECTED
    field: change
    value: NONE
    source_finding:
      phase: p5
      register: provisional_codes
      row: 17
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: read_asked_read_changes_nothing
    role: EXPECTED
    field: read_now
    value: true
    source_finding:
      phase: p5
      register: provisional_codes
      row: 17
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: unread_asked_unread_changes_nothing
    role: INPUT
    field: seen
    value: false
    source_finding:
      phase: p5
      register: provisional_codes
      row: 17
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: unread_asked_unread_changes_nothing
    role: INPUT
    field: wanted_read
    value: false
    source_finding:
      phase: p5
      register: provisional_codes
      row: 17
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: unread_asked_unread_changes_nothing
    role: EXPECTED
    field: change
    value: NONE
    source_finding:
      phase: p5
      register: provisional_codes
      row: 17
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: unread_asked_unread_changes_nothing
    role: EXPECTED
    field: read_now
    value: false
    source_finding:
      phase: p5
      register: provisional_codes
      row: 17
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: a_state_that_is_not_true_or_false_is_refused
    role: INPUT
    field: seen
    value: 'yes'
    source_finding:
      phase: p5
      register: provisional_codes
      row: 17
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: a_state_that_is_not_true_or_false_is_refused
    role: INPUT
    field: wanted_read
    value: true
    source_finding:
      phase: p5
      register: provisional_codes
      row: 17
  withdrawn_facts: null
```

Generated by `generate_p7.py` in this dossier from the design tables it states. Every row cites the P5, P6 or P0 row it realises.
