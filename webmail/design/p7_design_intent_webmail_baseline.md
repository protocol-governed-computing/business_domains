# Design Intent — webmail, baseline

## Machine

```yaml
document:
  phase: p7
  domain: webmail
  subdomain:
  - mailbox
  cr: baseline
  rule_set: transformation.schemas.REGISTER_SCHEMA_P7_V0
registers:
  design_resolution: []
  existing_inventory: []
  new_artifacts:
  - family: AC
    code: webmail::AC_MAIL_HOST_V0
    summary: The program that reaches a person's mail provider; it reports and carries out, and holds
      no authority
    owner_subdomain: mailbox
    status: NEW
  - family: CC
    code: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    summary: Chooses a page of a folder's identifiers, newest received first
    owner_subdomain: mailbox
    status: NEW
  - family: CC
    code: webmail::CC_CHOOSE_MESSAGE_TEXT_V0
    summary: Chooses the plain-text part of a message to show, or says none can be displayed
    owner_subdomain: mailbox
    status: NEW
  - family: CC
    code: webmail::CC_CONFIRM_PROVIDER_ANSWERED_V0
    summary: Confirms the provider answered, refusing otherwise
    owner_subdomain: mailbox
    status: NEW
  - family: CC
    code: webmail::CC_DECIDE_READ_STATE_V0
    summary: Decides whether a message becomes read, becomes unread or stays as it is
    owner_subdomain: mailbox
    status: NEW
  - family: CC
    code: webmail::CC_RECORD_MAILBOX_REQUEST_V0
    summary: Adds an entry to the mailbox record
    owner_subdomain: mailbox
    status: NEW
  - family: CT
    code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    summary: Orders identifiers newest received first and cuts the page asked for
    owner_subdomain: mailbox
    status: NEW
  - family: CT
    code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    summary: Chooses a message's plain-text part from its parts, or says its text cannot be displayed
      yet
    owner_subdomain: mailbox
    status: NEW
  - family: CT
    code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    summary: Decides a change of read state from the state held and the state asked for
    owner_subdomain: mailbox
    status: NEW
  - family: EV
    code: webmail::EV_FOLDER_LISTED_V0
    summary: A folder's page was chosen for the person
    owner_subdomain: mailbox
    status: NEW
  - family: EV
    code: webmail::EV_MAILBOX_REQUEST_REFUSED_V0
    summary: A request was refused
    owner_subdomain: mailbox
    status: NEW
  - family: EV
    code: webmail::EV_MESSAGE_OPENED_V0
    summary: A message was opened for the person
    owner_subdomain: mailbox
    status: NEW
  - family: EV
    code: webmail::EV_READ_STATE_CHANGED_V0
    summary: The provider accepted a decided change of read state
    owner_subdomain: mailbox
    status: NEW
  - family: IN
    code: webmail::IN_LIST_FOLDER_V0
    summary: A host's report of a folder's message identifiers and the page asked for
    owner_subdomain: mailbox
    status: NEW
  - family: IN
    code: webmail::IN_MARK_MESSAGE_V0
    summary: A host's report of a message's read state and the state the person asked for
    owner_subdomain: mailbox
    status: NEW
  - family: IN
    code: webmail::IN_OPEN_MESSAGE_V0
    summary: A host's report of the read state and the parts of a message the person asked to open
    owner_subdomain: mailbox
    status: NEW
  - family: IN
    code: webmail::IN_REPORT_CHANGE_OUTCOME_V0
    summary: A host's report of whether the provider accepted a decided change
    owner_subdomain: mailbox
    status: NEW
  - family: STRUCTURE
    code: webmail::STRUCTURE_MAILBOX_STORAGE_V0
    summary: Declares the mailbox record and the path it occupies
    owner_subdomain: mailbox
    status: NEW
  - family: RB
    code: webmail::RB_MAILBOX_BINDINGS_V0
    summary: Binds every mailbox act to the record it appends to
    owner_subdomain: mailbox
    status: NEW
  - family: WF
    code: webmail::WF_LIST_FOLDER_V0
    summary: Chooses which messages make the page of a folder the person asked for, newest received first
    owner_subdomain: mailbox
    status: NEW
  - family: WF
    code: webmail::WF_MARK_MESSAGE_V0
    summary: Decides a change of a message's read state, or that nothing changes
    owner_subdomain: mailbox
    status: NEW
  - family: WF
    code: webmail::WF_OPEN_MESSAGE_V0
    summary: Chooses what of a message is shown and decides that it becomes read
    owner_subdomain: mailbox
    status: NEW
  - family: WF
    code: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    summary: Records whether the provider accepted a change the business decided
    owner_subdomain: mailbox
    status: NEW
  rb_declarations:
  - rb_code: webmail::RB_MAILBOX_BINDINGS_V0
    binds_wf: webmail::WF_LIST_FOLDER_V0
    cs_bindings:
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: webmail::STRUCTURE_MAILBOX_STORAGE_V0
  - rb_code: webmail::RB_MAILBOX_BINDINGS_V0
    binds_wf: webmail::WF_MARK_MESSAGE_V0
    cs_bindings:
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: webmail::STRUCTURE_MAILBOX_STORAGE_V0
  - rb_code: webmail::RB_MAILBOX_BINDINGS_V0
    binds_wf: webmail::WF_OPEN_MESSAGE_V0
    cs_bindings:
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: webmail::STRUCTURE_MAILBOX_STORAGE_V0
  - rb_code: webmail::RB_MAILBOX_BINDINGS_V0
    binds_wf: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    cs_bindings:
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: webmail::STRUCTURE_MAILBOX_STORAGE_V0
  execution_topology:
  - workflow: webmail::WF_LIST_FOLDER_V0
    node: IN_LIST_FOLDER_V0
    node_type: IN
    routing:
      ACK: CONFIRM_ANSWERED
      NACK: EXIT_REJECTED
  - workflow: webmail::WF_LIST_FOLDER_V0
    node: CONFIRM_ANSWERED
    node_type: CC
    routing:
      SUCCESS: CC_CHOOSE_FOLDER_PAGE_V0
      VIOLATION: RECORD_REFUSED
    runs: CC_CONFIRM_PROVIDER_ANSWERED_V0
  - workflow: webmail::WF_LIST_FOLDER_V0
    node: CC_CHOOSE_FOLDER_PAGE_V0
    node_type: CC
    routing:
      SUCCESS: RECORD_LISTED
      VIOLATION: RECORD_REPORT_REFUSED
  - workflow: webmail::WF_LIST_FOLDER_V0
    node: RECORD_LISTED
    node_type: CC
    routing:
      SUCCESS: EXIT_LISTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_MAILBOX_REQUEST_V0
  - workflow: webmail::WF_LIST_FOLDER_V0
    node: RECORD_REFUSED
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_MAILBOX_REQUEST_V0
  - workflow: webmail::WF_LIST_FOLDER_V0
    node: RECORD_REPORT_REFUSED
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_MAILBOX_REQUEST_V0
  - workflow: webmail::WF_LIST_FOLDER_V0
    node: EXIT_LISTED
    node_type: EXIT
    routing: null
  - workflow: webmail::WF_LIST_FOLDER_V0
    node: EXIT_REFUSED
    node_type: EXIT
    routing: null
  - workflow: webmail::WF_LIST_FOLDER_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: webmail::WF_MARK_MESSAGE_V0
    node: IN_MARK_MESSAGE_V0
    node_type: IN
    routing:
      ACK: CONFIRM_ANSWERED
      NACK: EXIT_REJECTED
  - workflow: webmail::WF_MARK_MESSAGE_V0
    node: CONFIRM_ANSWERED
    node_type: CC
    routing:
      SUCCESS: CC_DECIDE_READ_STATE_V0
      VIOLATION: RECORD_REFUSED
    runs: CC_CONFIRM_PROVIDER_ANSWERED_V0
  - workflow: webmail::WF_MARK_MESSAGE_V0
    node: CC_DECIDE_READ_STATE_V0
    node_type: CC
    routing:
      SUCCESS: RECORD_MARKED
      VIOLATION: RECORD_REPORT_REFUSED
  - workflow: webmail::WF_MARK_MESSAGE_V0
    node: RECORD_MARKED
    node_type: CC
    routing:
      SUCCESS: EXIT_MARKED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_MAILBOX_REQUEST_V0
  - workflow: webmail::WF_MARK_MESSAGE_V0
    node: RECORD_REFUSED
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_MAILBOX_REQUEST_V0
  - workflow: webmail::WF_MARK_MESSAGE_V0
    node: RECORD_REPORT_REFUSED
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_MAILBOX_REQUEST_V0
  - workflow: webmail::WF_MARK_MESSAGE_V0
    node: EXIT_MARKED
    node_type: EXIT
    routing: null
  - workflow: webmail::WF_MARK_MESSAGE_V0
    node: EXIT_REFUSED
    node_type: EXIT
    routing: null
  - workflow: webmail::WF_MARK_MESSAGE_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: webmail::WF_OPEN_MESSAGE_V0
    node: IN_OPEN_MESSAGE_V0
    node_type: IN
    routing:
      ACK: CONFIRM_ANSWERED
      NACK: EXIT_REJECTED
  - workflow: webmail::WF_OPEN_MESSAGE_V0
    node: CONFIRM_ANSWERED
    node_type: CC
    routing:
      SUCCESS: CC_CHOOSE_MESSAGE_TEXT_V0
      VIOLATION: RECORD_REFUSED
    runs: CC_CONFIRM_PROVIDER_ANSWERED_V0
  - workflow: webmail::WF_OPEN_MESSAGE_V0
    node: CC_CHOOSE_MESSAGE_TEXT_V0
    node_type: CC
    routing:
      SUCCESS: CC_DECIDE_READ_STATE_V0
      VIOLATION: RECORD_REPORT_REFUSED
  - workflow: webmail::WF_OPEN_MESSAGE_V0
    node: CC_DECIDE_READ_STATE_V0
    node_type: CC
    routing:
      SUCCESS: RECORD_OPENED
      VIOLATION: RECORD_REPORT_REFUSED
  - workflow: webmail::WF_OPEN_MESSAGE_V0
    node: RECORD_OPENED
    node_type: CC
    routing:
      SUCCESS: EXIT_OPENED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_MAILBOX_REQUEST_V0
  - workflow: webmail::WF_OPEN_MESSAGE_V0
    node: RECORD_REFUSED
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_MAILBOX_REQUEST_V0
  - workflow: webmail::WF_OPEN_MESSAGE_V0
    node: RECORD_REPORT_REFUSED
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_MAILBOX_REQUEST_V0
  - workflow: webmail::WF_OPEN_MESSAGE_V0
    node: EXIT_OPENED
    node_type: EXIT
    routing: null
  - workflow: webmail::WF_OPEN_MESSAGE_V0
    node: EXIT_REFUSED
    node_type: EXIT
    routing: null
  - workflow: webmail::WF_OPEN_MESSAGE_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    node: IN_REPORT_CHANGE_OUTCOME_V0
    node_type: IN
    routing:
      ACK: CONFIRM_ANSWERED
      NACK: EXIT_REJECTED
  - workflow: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    node: CONFIRM_ANSWERED
    node_type: CC
    routing:
      SUCCESS: RECORD_CHANGED
      VIOLATION: RECORD_REFUSED
    runs: CC_CONFIRM_PROVIDER_ANSWERED_V0
  - workflow: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    node: RECORD_CHANGED
    node_type: CC
    routing:
      SUCCESS: EXIT_CHANGED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_MAILBOX_REQUEST_V0
  - workflow: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    node: RECORD_REFUSED
    node_type: CC
    routing:
      SUCCESS: EXIT_REFUSED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_MAILBOX_REQUEST_V0
  - workflow: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    node: EXIT_CHANGED
    node_type: EXIT
    routing: null
  - workflow: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    node: EXIT_REFUSED
    node_type: EXIT
    routing: null
  - workflow: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  cc_composition:
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
    - answered
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
        answered: answered
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
    - entry
    routing:
      SUCCESS: continue
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: fields
      out:
        entry: entry
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
  - owner: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    step: choose_page
    direction: INPUT
    field: message_ids
    bound_to: inputs.message_ids
  - owner: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    step: choose_page
    direction: INPUT
    field: page
    bound_to: inputs.page
  - owner: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    step: choose_page
    direction: INPUT
    field: page_size
    bound_to:
      literal: 50
  - owner: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    step: choose_page
    direction: OUTPUT
    field: page_ids
    bound_to: capability_result.page_ids
  - owner: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    step: choose_page
    direction: OUTPUT
    field: more_exist
    bound_to: capability_result.more_exist
  - owner: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    step: choose_page
    direction: OUTPUT
    field: folder_empty
    bound_to: capability_result.folder_empty
  - owner: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    step: choose_page
    direction: OUTPUT
    field: message_count
    bound_to: capability_result.message_count
  - owner: webmail::CC_CHOOSE_MESSAGE_TEXT_V0
    step: choose_text
    direction: INPUT
    field: parts
    bound_to: inputs.parts
  - owner: webmail::CC_CHOOSE_MESSAGE_TEXT_V0
    step: choose_text
    direction: OUTPUT
    field: text_part
    bound_to: capability_result.text_part
  - owner: webmail::CC_CHOOSE_MESSAGE_TEXT_V0
    step: choose_text
    direction: OUTPUT
    field: text_displayable
    bound_to: capability_result.text_displayable
  - owner: webmail::CC_CHOOSE_MESSAGE_TEXT_V0
    step: choose_text
    direction: OUTPUT
    field: shown_headers
    bound_to: capability_result.shown_headers
  - owner: webmail::CC_CONFIRM_PROVIDER_ANSWERED_V0
    step: confirm_answered
    direction: INPUT
    field: value
    bound_to: inputs.provider_answer
  - owner: webmail::CC_CONFIRM_PROVIDER_ANSWERED_V0
    step: confirm_answered
    direction: INPUT
    field: allowed_set
    bound_to:
      literal:
      - ANSWERED
  - owner: webmail::CC_CONFIRM_PROVIDER_ANSWERED_V0
    step: confirm_answered
    direction: OUTPUT
    field: answered
    bound_to: capability_result.is_member
  - owner: webmail::CC_DECIDE_READ_STATE_V0
    step: decide_read_state
    direction: INPUT
    field: seen
    bound_to: inputs.seen
  - owner: webmail::CC_DECIDE_READ_STATE_V0
    step: decide_read_state
    direction: INPUT
    field: wanted_read
    bound_to: inputs.wanted_read
  - owner: webmail::CC_DECIDE_READ_STATE_V0
    step: decide_read_state
    direction: OUTPUT
    field: change
    bound_to: capability_result.change
  - owner: webmail::CC_DECIDE_READ_STATE_V0
    step: decide_read_state
    direction: OUTPUT
    field: read_now
    bound_to: capability_result.read_now
  - owner: webmail::CC_RECORD_MAILBOX_REQUEST_V0
    step: assemble_entry
    direction: INPUT
    field: fields
    bound_to: inputs.entry
  - owner: webmail::CC_RECORD_MAILBOX_REQUEST_V0
    step: assemble_entry
    direction: OUTPUT
    field: entry
    bound_to: capability_result.record
  - owner: webmail::CC_RECORD_MAILBOX_REQUEST_V0
    step: append_entry
    direction: INPUT
    field: record
    bound_to: results.assemble_entry.entry
  - owner: webmail::CC_RECORD_MAILBOX_REQUEST_V0
    step: append_entry
    direction: INPUT
    field: stream_id
    bound_to:
      literal: MAILBOX_RECORDS
  - owner: webmail::CC_RECORD_MAILBOX_REQUEST_V0
    step: append_entry
    direction: INPUT
    field: actor_id
    bound_to: inputs.host_id
  - owner: webmail::CC_RECORD_MAILBOX_REQUEST_V0
    step: append_entry
    direction: OUTPUT
    field: record_id
    bound_to: capability_result.record_id
  - owner: webmail::CC_RECORD_MAILBOX_REQUEST_V0
    step: append_entry
    direction: OUTPUT
    field: sequence_number
    bound_to: capability_result.sequence_number
  - owner: webmail::WF_LIST_FOLDER_V0
    step: CONFIRM_ANSWERED
    direction: INPUT
    field: provider_answer
    bound_to: payload.provider_answer
  - owner: webmail::WF_LIST_FOLDER_V0
    step: CC_CHOOSE_FOLDER_PAGE_V0
    direction: INPUT
    field: message_ids
    bound_to: payload.message_ids
  - owner: webmail::WF_LIST_FOLDER_V0
    step: CC_CHOOSE_FOLDER_PAGE_V0
    direction: INPUT
    field: page
    bound_to: payload.page
  - owner: webmail::WF_LIST_FOLDER_V0
    step: RECORD_LISTED
    direction: INPUT
    field: host_id
    bound_to: payload.host_id
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
  - owner: webmail::WF_LIST_FOLDER_V0
    step: RECORD_REFUSED
    direction: INPUT
    field: host_id
    bound_to: payload.host_id
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
  - owner: webmail::WF_LIST_FOLDER_V0
    step: RECORD_REPORT_REFUSED
    direction: INPUT
    field: host_id
    bound_to: payload.host_id
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
  - owner: webmail::WF_MARK_MESSAGE_V0
    step: CONFIRM_ANSWERED
    direction: INPUT
    field: provider_answer
    bound_to: payload.provider_answer
  - owner: webmail::WF_MARK_MESSAGE_V0
    step: CC_DECIDE_READ_STATE_V0
    direction: INPUT
    field: seen
    bound_to: payload.seen
  - owner: webmail::WF_MARK_MESSAGE_V0
    step: CC_DECIDE_READ_STATE_V0
    direction: INPUT
    field: wanted_read
    bound_to: payload.wanted_read
  - owner: webmail::WF_MARK_MESSAGE_V0
    step: RECORD_MARKED
    direction: INPUT
    field: host_id
    bound_to: payload.host_id
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
  - owner: webmail::WF_MARK_MESSAGE_V0
    step: RECORD_REFUSED
    direction: INPUT
    field: host_id
    bound_to: payload.host_id
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
  - owner: webmail::WF_MARK_MESSAGE_V0
    step: RECORD_REPORT_REFUSED
    direction: INPUT
    field: host_id
    bound_to: payload.host_id
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
  - owner: webmail::WF_OPEN_MESSAGE_V0
    step: CONFIRM_ANSWERED
    direction: INPUT
    field: provider_answer
    bound_to: payload.provider_answer
  - owner: webmail::WF_OPEN_MESSAGE_V0
    step: CC_CHOOSE_MESSAGE_TEXT_V0
    direction: INPUT
    field: parts
    bound_to: payload.parts
  - owner: webmail::WF_OPEN_MESSAGE_V0
    step: CC_DECIDE_READ_STATE_V0
    direction: INPUT
    field: seen
    bound_to: payload.seen
  - owner: webmail::WF_OPEN_MESSAGE_V0
    step: CC_DECIDE_READ_STATE_V0
    direction: INPUT
    field: wanted_read
    bound_to:
      literal: true
  - owner: webmail::WF_OPEN_MESSAGE_V0
    step: RECORD_OPENED
    direction: INPUT
    field: host_id
    bound_to: payload.host_id
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
  - owner: webmail::WF_OPEN_MESSAGE_V0
    step: RECORD_REFUSED
    direction: INPUT
    field: host_id
    bound_to: payload.host_id
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
  - owner: webmail::WF_OPEN_MESSAGE_V0
    step: RECORD_REPORT_REFUSED
    direction: INPUT
    field: host_id
    bound_to: payload.host_id
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
  - owner: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    step: CONFIRM_ANSWERED
    direction: INPUT
    field: provider_answer
    bound_to: payload.provider_answer
  - owner: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    step: RECORD_CHANGED
    direction: INPUT
    field: host_id
    bound_to: payload.host_id
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
  - owner: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    step: RECORD_REFUSED
    direction: INPUT
    field: host_id
    bound_to: payload.host_id
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
  interface_fields:
  - artifact: webmail::AC_MAIL_HOST_V0
    direction: ATTRIBUTE
    field: host_id
    type: string
    required: 'YES'
    default: null
    meaning: host id
  - artifact: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    direction: INPUT
    field: message_ids
    type: array
    required: 'YES'
    default: null
    meaning: message ids
  - artifact: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    direction: INPUT
    field: page
    type: integer
    required: 'YES'
    default: null
    meaning: page
  - artifact: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    direction: OUTPUT
    field: page_ids
    type: array
    required: 'YES'
    default: null
    meaning: page ids
  - artifact: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    direction: OUTPUT
    field: more_exist
    type: boolean
    required: 'YES'
    default: null
    meaning: more exist
  - artifact: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    direction: OUTPUT
    field: folder_empty
    type: boolean
    required: 'YES'
    default: null
    meaning: folder empty
  - artifact: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    direction: OUTPUT
    field: message_count
    type: integer
    required: 'YES'
    default: null
    meaning: message count
  - artifact: webmail::CC_CHOOSE_MESSAGE_TEXT_V0
    direction: INPUT
    field: parts
    type: array
    required: 'YES'
    default: null
    meaning: parts
  - artifact: webmail::CC_CHOOSE_MESSAGE_TEXT_V0
    direction: OUTPUT
    field: text_part
    type: string
    required: 'YES'
    default: null
    meaning: text part
  - artifact: webmail::CC_CHOOSE_MESSAGE_TEXT_V0
    direction: OUTPUT
    field: text_displayable
    type: boolean
    required: 'YES'
    default: null
    meaning: text displayable
  - artifact: webmail::CC_CHOOSE_MESSAGE_TEXT_V0
    direction: OUTPUT
    field: shown_headers
    type: array
    required: 'YES'
    default: null
    meaning: shown headers
  - artifact: webmail::CC_CONFIRM_PROVIDER_ANSWERED_V0
    direction: INPUT
    field: provider_answer
    type: string
    required: 'YES'
    default: null
    meaning: provider answer
  - artifact: webmail::CC_CONFIRM_PROVIDER_ANSWERED_V0
    direction: OUTPUT
    field: answered
    type: boolean
    required: 'YES'
    default: null
    meaning: answered
  - artifact: webmail::CC_DECIDE_READ_STATE_V0
    direction: INPUT
    field: seen
    type: boolean
    required: 'YES'
    default: null
    meaning: seen
  - artifact: webmail::CC_DECIDE_READ_STATE_V0
    direction: INPUT
    field: wanted_read
    type: boolean
    required: 'YES'
    default: null
    meaning: wanted read
  - artifact: webmail::CC_DECIDE_READ_STATE_V0
    direction: OUTPUT
    field: change
    type: string
    required: 'YES'
    default: null
    meaning: change
  - artifact: webmail::CC_DECIDE_READ_STATE_V0
    direction: OUTPUT
    field: read_now
    type: boolean
    required: 'YES'
    default: null
    meaning: read now
  - artifact: webmail::CC_RECORD_MAILBOX_REQUEST_V0
    direction: INPUT
    field: entry
    type: object
    required: 'YES'
    default: null
    meaning: entry
  - artifact: webmail::CC_RECORD_MAILBOX_REQUEST_V0
    direction: INPUT
    field: host_id
    type: string
    required: 'YES'
    default: null
    meaning: host id
  - artifact: webmail::CC_RECORD_MAILBOX_REQUEST_V0
    direction: OUTPUT
    field: entry
    type: object
    required: 'YES'
    default: null
    meaning: entry
  - artifact: webmail::CC_RECORD_MAILBOX_REQUEST_V0
    direction: OUTPUT
    field: record_id
    type: string
    required: 'YES'
    default: null
    meaning: record id
  - artifact: webmail::CC_RECORD_MAILBOX_REQUEST_V0
    direction: OUTPUT
    field: sequence_number
    type: integer
    required: 'YES'
    default: null
    meaning: sequence number
  - artifact: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    direction: INPUT
    field: message_ids
    type: array
    required: 'YES'
    default: null
    meaning: message ids
  - artifact: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    direction: INPUT
    field: page
    type: integer
    required: 'YES'
    default: null
    meaning: page
  - artifact: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    direction: INPUT
    field: page_size
    type: integer
    required: 'YES'
    default: null
    meaning: page size
  - artifact: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    direction: OUTPUT
    field: page_ids
    type: array
    required: 'YES'
    default: null
    meaning: page ids
  - artifact: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    direction: OUTPUT
    field: more_exist
    type: boolean
    required: 'YES'
    default: null
    meaning: more exist
  - artifact: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    direction: OUTPUT
    field: folder_empty
    type: boolean
    required: 'YES'
    default: null
    meaning: folder empty
  - artifact: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    direction: OUTPUT
    field: message_count
    type: integer
    required: 'YES'
    default: null
    meaning: message count
  - artifact: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    direction: INPUT
    field: parts
    type: array
    required: 'YES'
    default: null
    meaning: parts
  - artifact: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    direction: OUTPUT
    field: text_part
    type: string
    required: 'YES'
    default: null
    meaning: text part
  - artifact: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    direction: OUTPUT
    field: text_displayable
    type: boolean
    required: 'YES'
    default: null
    meaning: text displayable
  - artifact: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    direction: OUTPUT
    field: shown_headers
    type: array
    required: 'YES'
    default: null
    meaning: shown headers
  - artifact: webmail::CT_PURE_DECIDE_READ_STATE_V0
    direction: INPUT
    field: seen
    type: boolean
    required: 'YES'
    default: null
    meaning: seen
  - artifact: webmail::CT_PURE_DECIDE_READ_STATE_V0
    direction: INPUT
    field: wanted_read
    type: boolean
    required: 'YES'
    default: null
    meaning: wanted read
  - artifact: webmail::CT_PURE_DECIDE_READ_STATE_V0
    direction: OUTPUT
    field: change
    type: string
    required: 'YES'
    default: null
    meaning: change
  - artifact: webmail::CT_PURE_DECIDE_READ_STATE_V0
    direction: OUTPUT
    field: read_now
    type: boolean
    required: 'YES'
    default: null
    meaning: read now
  - artifact: webmail::EV_FOLDER_LISTED_V0
    direction: OUTPUT
    field: entry
    type: object
    required: 'YES'
    default: null
    meaning: entry
  - artifact: webmail::EV_FOLDER_LISTED_V0
    direction: OUTPUT
    field: sequence_number
    type: integer
    required: 'YES'
    default: null
    meaning: sequence number
  - artifact: webmail::EV_FOLDER_LISTED_V0
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: When the moment occurred
    format: date-time
  - artifact: webmail::EV_MAILBOX_REQUEST_REFUSED_V0
    direction: OUTPUT
    field: entry
    type: object
    required: 'YES'
    default: null
    meaning: entry
  - artifact: webmail::EV_MAILBOX_REQUEST_REFUSED_V0
    direction: OUTPUT
    field: sequence_number
    type: integer
    required: 'YES'
    default: null
    meaning: sequence number
  - artifact: webmail::EV_MAILBOX_REQUEST_REFUSED_V0
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: When the moment occurred
    format: date-time
  - artifact: webmail::EV_MESSAGE_OPENED_V0
    direction: OUTPUT
    field: entry
    type: object
    required: 'YES'
    default: null
    meaning: entry
  - artifact: webmail::EV_MESSAGE_OPENED_V0
    direction: OUTPUT
    field: sequence_number
    type: integer
    required: 'YES'
    default: null
    meaning: sequence number
  - artifact: webmail::EV_MESSAGE_OPENED_V0
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: When the moment occurred
    format: date-time
  - artifact: webmail::EV_READ_STATE_CHANGED_V0
    direction: OUTPUT
    field: entry
    type: object
    required: 'YES'
    default: null
    meaning: entry
  - artifact: webmail::EV_READ_STATE_CHANGED_V0
    direction: OUTPUT
    field: sequence_number
    type: integer
    required: 'YES'
    default: null
    meaning: sequence number
  - artifact: webmail::EV_READ_STATE_CHANGED_V0
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: When the moment occurred
    format: date-time
  - artifact: webmail::IN_LIST_FOLDER_V0
    direction: INPUT
    field: host_id
    type: string
    required: 'YES'
    default: null
    meaning: host id
  - artifact: webmail::IN_LIST_FOLDER_V0
    direction: INPUT
    field: mailbox
    type: string
    required: 'YES'
    default: null
    meaning: mailbox
  - artifact: webmail::IN_LIST_FOLDER_V0
    direction: INPUT
    field: folder
    type: string
    required: 'YES'
    default: null
    meaning: folder
  - artifact: webmail::IN_LIST_FOLDER_V0
    direction: INPUT
    field: provider_answer
    type: string
    required: 'YES'
    default: null
    meaning: provider answer
  - artifact: webmail::IN_LIST_FOLDER_V0
    direction: INPUT
    field: message_ids
    type: array
    required: 'YES'
    default: null
    meaning: message ids
  - artifact: webmail::IN_LIST_FOLDER_V0
    direction: INPUT
    field: page
    type: integer
    required: 'YES'
    default: null
    meaning: page
  - artifact: webmail::IN_MARK_MESSAGE_V0
    direction: INPUT
    field: host_id
    type: string
    required: 'YES'
    default: null
    meaning: host id
  - artifact: webmail::IN_MARK_MESSAGE_V0
    direction: INPUT
    field: mailbox
    type: string
    required: 'YES'
    default: null
    meaning: mailbox
  - artifact: webmail::IN_MARK_MESSAGE_V0
    direction: INPUT
    field: folder
    type: string
    required: 'YES'
    default: null
    meaning: folder
  - artifact: webmail::IN_MARK_MESSAGE_V0
    direction: INPUT
    field: provider_answer
    type: string
    required: 'YES'
    default: null
    meaning: provider answer
  - artifact: webmail::IN_MARK_MESSAGE_V0
    direction: INPUT
    field: message_id
    type: integer
    required: 'YES'
    default: null
    meaning: message id
  - artifact: webmail::IN_MARK_MESSAGE_V0
    direction: INPUT
    field: seen
    type: boolean
    required: 'YES'
    default: null
    meaning: seen
  - artifact: webmail::IN_MARK_MESSAGE_V0
    direction: INPUT
    field: wanted_read
    type: boolean
    required: 'YES'
    default: null
    meaning: wanted read
  - artifact: webmail::IN_OPEN_MESSAGE_V0
    direction: INPUT
    field: host_id
    type: string
    required: 'YES'
    default: null
    meaning: host id
  - artifact: webmail::IN_OPEN_MESSAGE_V0
    direction: INPUT
    field: mailbox
    type: string
    required: 'YES'
    default: null
    meaning: mailbox
  - artifact: webmail::IN_OPEN_MESSAGE_V0
    direction: INPUT
    field: folder
    type: string
    required: 'YES'
    default: null
    meaning: folder
  - artifact: webmail::IN_OPEN_MESSAGE_V0
    direction: INPUT
    field: provider_answer
    type: string
    required: 'YES'
    default: null
    meaning: provider answer
  - artifact: webmail::IN_OPEN_MESSAGE_V0
    direction: INPUT
    field: message_id
    type: integer
    required: 'YES'
    default: null
    meaning: message id
  - artifact: webmail::IN_OPEN_MESSAGE_V0
    direction: INPUT
    field: seen
    type: boolean
    required: 'YES'
    default: null
    meaning: seen
  - artifact: webmail::IN_OPEN_MESSAGE_V0
    direction: INPUT
    field: parts
    type: array
    required: 'YES'
    default: null
    meaning: parts
  - artifact: webmail::IN_REPORT_CHANGE_OUTCOME_V0
    direction: INPUT
    field: host_id
    type: string
    required: 'YES'
    default: null
    meaning: host id
  - artifact: webmail::IN_REPORT_CHANGE_OUTCOME_V0
    direction: INPUT
    field: mailbox
    type: string
    required: 'YES'
    default: null
    meaning: mailbox
  - artifact: webmail::IN_REPORT_CHANGE_OUTCOME_V0
    direction: INPUT
    field: folder
    type: string
    required: 'YES'
    default: null
    meaning: folder
  - artifact: webmail::IN_REPORT_CHANGE_OUTCOME_V0
    direction: INPUT
    field: provider_answer
    type: string
    required: 'YES'
    default: null
    meaning: provider answer
  - artifact: webmail::IN_REPORT_CHANGE_OUTCOME_V0
    direction: INPUT
    field: message_id
    type: integer
    required: 'YES'
    default: null
    meaning: message id
  - artifact: webmail::IN_REPORT_CHANGE_OUTCOME_V0
    direction: INPUT
    field: change
    type: string
    required: 'YES'
    default: null
    meaning: change
  implementation_bindings:
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    callable: execute
    operation: CHOOSE_FOLDER_PAGE
    kind: atom
    purity: ct_pure
    refusal: raises
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    callable: execute
    operation: CHOOSE_MESSAGE_TEXT
    kind: atom
    purity: ct_pure
    refusal: raises
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    callable: execute
    operation: DECIDE_READ_STATE
    kind: atom
    purity: ct_pure
    refusal: raises
  vocabulary_extensions: []
  runtime_policies:
  - rb_code: webmail::RB_MAILBOX_BINDINGS_V0
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    key: structure
    value: webmail::STRUCTURE_MAILBOX_STORAGE_V0
  artifact_properties:
  - artifact: webmail::AC_MAIL_HOST_V0
    property: type
    value: system
  - artifact: webmail::EV_MAILBOX_REQUEST_REFUSED_V0
    property: moment
    value: refusal
  - artifact: webmail::STRUCTURE_MAILBOX_STORAGE_V0
    property: layer
    value: DOMAINS
  - artifact: webmail::WF_LIST_FOLDER_V0
    property: actor_context
    value: webmail::AC_MAIL_HOST_V0
  - artifact: webmail::WF_LIST_FOLDER_V0
    property: emit.EXIT_LISTED
    value:
    - webmail::EV_FOLDER_LISTED_V0
  - artifact: webmail::WF_LIST_FOLDER_V0
    property: emit.EXIT_REFUSED
    value:
    - webmail::EV_MAILBOX_REQUEST_REFUSED_V0
  - artifact: webmail::WF_MARK_MESSAGE_V0
    property: actor_context
    value: webmail::AC_MAIL_HOST_V0
  - artifact: webmail::WF_MARK_MESSAGE_V0
    property: emit.EXIT_REFUSED
    value:
    - webmail::EV_MAILBOX_REQUEST_REFUSED_V0
  - artifact: webmail::WF_OPEN_MESSAGE_V0
    property: actor_context
    value: webmail::AC_MAIL_HOST_V0
  - artifact: webmail::WF_OPEN_MESSAGE_V0
    property: emit.EXIT_OPENED
    value:
    - webmail::EV_MESSAGE_OPENED_V0
  - artifact: webmail::WF_OPEN_MESSAGE_V0
    property: emit.EXIT_REFUSED
    value:
    - webmail::EV_MAILBOX_REQUEST_REFUSED_V0
  - artifact: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    property: actor_context
    value: webmail::AC_MAIL_HOST_V0
  - artifact: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    property: emit.EXIT_CHANGED
    value:
    - webmail::EV_READ_STATE_CHANGED_V0
  - artifact: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    property: emit.EXIT_REFUSED
    value:
    - webmail::EV_MAILBOX_REQUEST_REFUSED_V0
  structure_stores:
  - store_name: MAILBOX_RECORDS
    storage_type: CS_APPENDONLY_JSONL_V0
    proposed_path: webmail/mailbox/mailbox_records.jsonl
    used_by: webmail::CC_RECORD_MAILBOX_REQUEST_V0
    structure: webmail::STRUCTURE_MAILBOX_STORAGE_V0
  transport_bindings: []
  declared_reach: []
  molecule_steps: []
  molecule_step_bindings: []
  test_cases:
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: first_page_is_newest_received_first
    expected_outcome: SUCCESS
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: last_page_says_no_more_exist
    expected_outcome: SUCCESS
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: received_order_decides_not_the_identifier
    expected_outcome: SUCCESS
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: empty_folder_answers_empty
    expected_outcome: SUCCESS
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: a_page_before_the_first_is_refused
    expected_outcome: VIOLATION
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: an_identifier_that_is_not_a_number_is_refused
    expected_outcome: VIOLATION
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: plain_text_part_is_chosen
    expected_outcome: SUCCESS
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: first_plain_text_part_wins
    expected_outcome: SUCCESS
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: kind_is_read_without_regard_to_case
    expected_outcome: SUCCESS
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: html_only_cannot_be_displayed_yet
    expected_outcome: SUCCESS
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: a_part_without_a_kind_is_refused
    expected_outcome: VIOLATION
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: unread_asked_read_becomes_read
    expected_outcome: SUCCESS
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: read_asked_unread_becomes_unread
    expected_outcome: SUCCESS
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: read_asked_read_changes_nothing
    expected_outcome: SUCCESS
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: unread_asked_unread_changes_nothing
    expected_outcome: SUCCESS
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: a_state_that_is_not_true_or_false_is_refused
    expected_outcome: VIOLATION
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
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: first_page_is_newest_received_first
    role: INPUT
    field: page
    value: 1
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: first_page_is_newest_received_first
    role: INPUT
    field: page_size
    value: 2
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: first_page_is_newest_received_first
    role: EXPECTED
    field: page_ids
    value:
    - 12
    - 9
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: first_page_is_newest_received_first
    role: EXPECTED
    field: more_exist
    value: true
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: first_page_is_newest_received_first
    role: EXPECTED
    field: folder_empty
    value: false
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: first_page_is_newest_received_first
    role: EXPECTED
    field: message_count
    value: 4
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: last_page_says_no_more_exist
    role: INPUT
    field: message_ids
    value:
    - 3
    - 7
    - 9
    - 12
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: last_page_says_no_more_exist
    role: INPUT
    field: page
    value: 2
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: last_page_says_no_more_exist
    role: INPUT
    field: page_size
    value: 2
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: last_page_says_no_more_exist
    role: EXPECTED
    field: page_ids
    value:
    - 7
    - 3
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: last_page_says_no_more_exist
    role: EXPECTED
    field: more_exist
    value: false
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: last_page_says_no_more_exist
    role: EXPECTED
    field: folder_empty
    value: false
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: last_page_says_no_more_exist
    role: EXPECTED
    field: message_count
    value: 4
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: received_order_decides_not_the_identifier
    role: INPUT
    field: message_ids
    value:
    - 40
    - 5
    - 22
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: received_order_decides_not_the_identifier
    role: INPUT
    field: page
    value: 1
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: received_order_decides_not_the_identifier
    role: INPUT
    field: page_size
    value: 50
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: received_order_decides_not_the_identifier
    role: EXPECTED
    field: page_ids
    value:
    - 22
    - 5
    - 40
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: received_order_decides_not_the_identifier
    role: EXPECTED
    field: more_exist
    value: false
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: received_order_decides_not_the_identifier
    role: EXPECTED
    field: folder_empty
    value: false
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: received_order_decides_not_the_identifier
    role: EXPECTED
    field: message_count
    value: 3
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: empty_folder_answers_empty
    role: INPUT
    field: message_ids
    value: []
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: empty_folder_answers_empty
    role: INPUT
    field: page
    value: 1
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: empty_folder_answers_empty
    role: INPUT
    field: page_size
    value: 50
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: empty_folder_answers_empty
    role: EXPECTED
    field: page_ids
    value: []
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: empty_folder_answers_empty
    role: EXPECTED
    field: more_exist
    value: false
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: empty_folder_answers_empty
    role: EXPECTED
    field: folder_empty
    value: true
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: empty_folder_answers_empty
    role: EXPECTED
    field: message_count
    value: 0
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: a_page_before_the_first_is_refused
    role: INPUT
    field: message_ids
    value:
    - 1
    - 2
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: a_page_before_the_first_is_refused
    role: INPUT
    field: page
    value: 0
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: a_page_before_the_first_is_refused
    role: INPUT
    field: page_size
    value: 50
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: an_identifier_that_is_not_a_number_is_refused
    role: INPUT
    field: message_ids
    value:
    - 1
    - two
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: an_identifier_that_is_not_a_number_is_refused
    role: INPUT
    field: page
    value: 1
  - ct_code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    case: an_identifier_that_is_not_a_number_is_refused
    role: INPUT
    field: page_size
    value: 50
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: plain_text_part_is_chosen
    role: INPUT
    field: parts
    value:
    - part: '1'
      kind: text/plain
    - part: '2'
      kind: text/html
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: plain_text_part_is_chosen
    role: EXPECTED
    field: text_part
    value: '1'
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: plain_text_part_is_chosen
    role: EXPECTED
    field: text_displayable
    value: true
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
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: first_plain_text_part_wins
    role: INPUT
    field: parts
    value:
    - part: '1.1'
      kind: text/plain
    - part: '2'
      kind: text/plain
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: first_plain_text_part_wins
    role: EXPECTED
    field: text_part
    value: '1.1'
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: first_plain_text_part_wins
    role: EXPECTED
    field: text_displayable
    value: true
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
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: kind_is_read_without_regard_to_case
    role: INPUT
    field: parts
    value:
    - part: '1'
      kind: TEXT/PLAIN
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: kind_is_read_without_regard_to_case
    role: EXPECTED
    field: text_part
    value: '1'
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: kind_is_read_without_regard_to_case
    role: EXPECTED
    field: text_displayable
    value: true
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
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: html_only_cannot_be_displayed_yet
    role: INPUT
    field: parts
    value:
    - part: '1'
      kind: text/html
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: html_only_cannot_be_displayed_yet
    role: EXPECTED
    field: text_part
    value: ''
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: html_only_cannot_be_displayed_yet
    role: EXPECTED
    field: text_displayable
    value: false
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
  - ct_code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    case: a_part_without_a_kind_is_refused
    role: INPUT
    field: parts
    value:
    - part: '1'
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: unread_asked_read_becomes_read
    role: INPUT
    field: seen
    value: false
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: unread_asked_read_becomes_read
    role: INPUT
    field: wanted_read
    value: true
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: unread_asked_read_becomes_read
    role: EXPECTED
    field: change
    value: SET_READ
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: unread_asked_read_becomes_read
    role: EXPECTED
    field: read_now
    value: true
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: read_asked_unread_becomes_unread
    role: INPUT
    field: seen
    value: true
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: read_asked_unread_becomes_unread
    role: INPUT
    field: wanted_read
    value: false
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: read_asked_unread_becomes_unread
    role: EXPECTED
    field: change
    value: SET_UNREAD
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: read_asked_unread_becomes_unread
    role: EXPECTED
    field: read_now
    value: false
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: read_asked_read_changes_nothing
    role: INPUT
    field: seen
    value: true
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: read_asked_read_changes_nothing
    role: INPUT
    field: wanted_read
    value: true
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: read_asked_read_changes_nothing
    role: EXPECTED
    field: change
    value: NONE
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: read_asked_read_changes_nothing
    role: EXPECTED
    field: read_now
    value: true
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: unread_asked_unread_changes_nothing
    role: INPUT
    field: seen
    value: false
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: unread_asked_unread_changes_nothing
    role: INPUT
    field: wanted_read
    value: false
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: unread_asked_unread_changes_nothing
    role: EXPECTED
    field: change
    value: NONE
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: unread_asked_unread_changes_nothing
    role: EXPECTED
    field: read_now
    value: false
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: a_state_that_is_not_true_or_false_is_refused
    role: INPUT
    field: seen
    value: 'yes'
  - ct_code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    case: a_state_that_is_not_true_or_false_is_refused
    role: INPUT
    field: wanted_read
    value: true
  generation_provenance: []
  artifact_summary:
  - action: NEW
    subdomain: mailbox
    count: '23'
    artifacts: webmail::AC_MAIL_HOST_V0, webmail::CC_CHOOSE_FOLDER_PAGE_V0, webmail::CC_CHOOSE_MESSAGE_TEXT_V0,
      webmail::CC_CONFIRM_PROVIDER_ANSWERED_V0, webmail::CC_DECIDE_READ_STATE_V0, webmail::CC_RECORD_MAILBOX_REQUEST_V0,
      webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0, webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0, webmail::CT_PURE_DECIDE_READ_STATE_V0,
      webmail::EV_FOLDER_LISTED_V0, webmail::EV_MAILBOX_REQUEST_REFUSED_V0, webmail::EV_MESSAGE_OPENED_V0,
      webmail::EV_READ_STATE_CHANGED_V0, webmail::IN_LIST_FOLDER_V0, webmail::IN_MARK_MESSAGE_V0, webmail::IN_OPEN_MESSAGE_V0,
      webmail::IN_REPORT_CHANGE_OUTCOME_V0, webmail::STRUCTURE_MAILBOX_STORAGE_V0, webmail::RB_MAILBOX_BINDINGS_V0,
      webmail::WF_LIST_FOLDER_V0, webmail::WF_MARK_MESSAGE_V0, webmail::WF_OPEN_MESSAGE_V0, webmail::WF_REPORT_CHANGE_OUTCOME_V0
  refusal_discharge: []
  refusal_deferrals: []
  refusal_governance_discharge: []
  withdrawn_facts: null
```

The design of record of `webmail`: every artifact its registry holds, stated in the design language.
Written by `python -m transformation.record` from the registry. Construction of this design and its
mandate reproduces the registry, and `construction_acceptance` asks whether it does. A change to
`webmail` is a dossier designed against the composition.
