# Authoring Mandate — webmail, baseline

## Machine

```yaml
document:
  phase: p8
  domain: webmail
  subdomain:
  - mailbox
  cr: baseline
  rule_set: transformation.schemas.REGISTER_SCHEMA_P8_V0
registers:
  build_order:
  - wave: '1'
    step: '1'
    code: webmail::STRUCTURE_MAILBOX_STORAGE_V0
    action: NEW
    subdomain: mailbox
    depends_on: null
  - wave: '1'
    step: '2'
    code: webmail::AC_MAIL_HOST_V0
    action: NEW
    subdomain: mailbox
    depends_on: null
  - wave: '1'
    step: '3'
    code: webmail::EV_FOLDER_LISTED_V0
    action: NEW
    subdomain: mailbox
    depends_on: null
  - wave: '1'
    step: '4'
    code: webmail::EV_MAILBOX_REQUEST_REFUSED_V0
    action: NEW
    subdomain: mailbox
    depends_on: null
  - wave: '1'
    step: '5'
    code: webmail::EV_MESSAGE_OPENED_V0
    action: NEW
    subdomain: mailbox
    depends_on: null
  - wave: '1'
    step: '6'
    code: webmail::EV_READ_STATE_CHANGED_V0
    action: NEW
    subdomain: mailbox
    depends_on: null
  - wave: '1'
    step: '7'
    code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    action: NEW
    subdomain: mailbox
    depends_on: null
  - wave: '1'
    step: '8'
    code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    action: NEW
    subdomain: mailbox
    depends_on: null
  - wave: '1'
    step: '9'
    code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    action: NEW
    subdomain: mailbox
    depends_on: null
  - wave: '1'
    step: '10'
    code: webmail::CC_CONFIRM_PROVIDER_ANSWERED_V0
    action: NEW
    subdomain: mailbox
    depends_on: null
  - wave: '1'
    step: '11'
    code: webmail::CC_RECORD_MAILBOX_REQUEST_V0
    action: NEW
    subdomain: mailbox
    depends_on: null
  - wave: '1'
    step: '12'
    code: webmail::IN_LIST_FOLDER_V0
    action: NEW
    subdomain: mailbox
    depends_on: null
  - wave: '1'
    step: '13'
    code: webmail::IN_MARK_MESSAGE_V0
    action: NEW
    subdomain: mailbox
    depends_on: null
  - wave: '1'
    step: '14'
    code: webmail::IN_OPEN_MESSAGE_V0
    action: NEW
    subdomain: mailbox
    depends_on: null
  - wave: '1'
    step: '15'
    code: webmail::IN_REPORT_CHANGE_OUTCOME_V0
    action: NEW
    subdomain: mailbox
    depends_on: null
  - wave: '2'
    step: '16'
    code: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    action: NEW
    subdomain: mailbox
    depends_on:
    - webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
  - wave: '2'
    step: '17'
    code: webmail::CC_CHOOSE_MESSAGE_TEXT_V0
    action: NEW
    subdomain: mailbox
    depends_on:
    - webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
  - wave: '2'
    step: '18'
    code: webmail::CC_DECIDE_READ_STATE_V0
    action: NEW
    subdomain: mailbox
    depends_on:
    - webmail::CT_PURE_DECIDE_READ_STATE_V0
  - wave: '2'
    step: '19'
    code: webmail::RB_MAILBOX_BINDINGS_V0
    action: NEW
    subdomain: mailbox
    depends_on:
    - webmail::STRUCTURE_MAILBOX_STORAGE_V0
  - wave: '3'
    step: '20'
    code: webmail::WF_LIST_FOLDER_V0
    action: NEW
    subdomain: mailbox
    depends_on:
    - webmail::RB_MAILBOX_BINDINGS_V0
    - webmail::AC_MAIL_HOST_V0
    - webmail::EV_FOLDER_LISTED_V0
    - webmail::EV_MAILBOX_REQUEST_REFUSED_V0
    - webmail::IN_LIST_FOLDER_V0
    - webmail::CC_CHOOSE_FOLDER_PAGE_V0
  - wave: '3'
    step: '21'
    code: webmail::WF_MARK_MESSAGE_V0
    action: NEW
    subdomain: mailbox
    depends_on:
    - webmail::RB_MAILBOX_BINDINGS_V0
    - webmail::AC_MAIL_HOST_V0
    - webmail::EV_MAILBOX_REQUEST_REFUSED_V0
    - webmail::IN_MARK_MESSAGE_V0
    - webmail::CC_DECIDE_READ_STATE_V0
  - wave: '3'
    step: '22'
    code: webmail::WF_OPEN_MESSAGE_V0
    action: NEW
    subdomain: mailbox
    depends_on:
    - webmail::RB_MAILBOX_BINDINGS_V0
    - webmail::AC_MAIL_HOST_V0
    - webmail::EV_MESSAGE_OPENED_V0
    - webmail::EV_MAILBOX_REQUEST_REFUSED_V0
    - webmail::IN_OPEN_MESSAGE_V0
    - webmail::CC_CHOOSE_MESSAGE_TEXT_V0
    - webmail::CC_DECIDE_READ_STATE_V0
  - wave: '3'
    step: '23'
    code: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    action: NEW
    subdomain: mailbox
    depends_on:
    - webmail::RB_MAILBOX_BINDINGS_V0
    - webmail::AC_MAIL_HOST_V0
    - webmail::EV_READ_STATE_CHANGED_V0
    - webmail::EV_MAILBOX_REQUEST_REFUSED_V0
    - webmail::IN_REPORT_CHANGE_OUTCOME_V0
  critical_path:
  - position: '1'
    code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
  - position: '2'
    code: webmail::CC_CHOOSE_FOLDER_PAGE_V0
  - position: '3'
    code: webmail::WF_LIST_FOLDER_V0
  mandate_artifact_summary:
  - action: NEW
    count: '23'
    description: 1 STRUCTURE, 1 AC, 4 EV, 3 CT, 5 CC, 4 IN, 4 WF, 1 RB
  field_declarations:
  - code: webmail::STRUCTURE_MAILBOX_STORAGE_V0
    subdomain_field: mailbox
  - code: webmail::AC_MAIL_HOST_V0
    subdomain_field: mailbox
  - code: webmail::EV_FOLDER_LISTED_V0
    subdomain_field: mailbox
  - code: webmail::EV_MAILBOX_REQUEST_REFUSED_V0
    subdomain_field: mailbox
  - code: webmail::EV_MESSAGE_OPENED_V0
    subdomain_field: mailbox
  - code: webmail::EV_READ_STATE_CHANGED_V0
    subdomain_field: mailbox
  - code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    subdomain_field: mailbox
  - code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    subdomain_field: mailbox
  - code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    subdomain_field: mailbox
  - code: webmail::CC_CONFIRM_PROVIDER_ANSWERED_V0
    subdomain_field: mailbox
  - code: webmail::CC_RECORD_MAILBOX_REQUEST_V0
    subdomain_field: mailbox
  - code: webmail::IN_LIST_FOLDER_V0
    subdomain_field: mailbox
  - code: webmail::IN_MARK_MESSAGE_V0
    subdomain_field: mailbox
  - code: webmail::IN_OPEN_MESSAGE_V0
    subdomain_field: mailbox
  - code: webmail::IN_REPORT_CHANGE_OUTCOME_V0
    subdomain_field: mailbox
  - code: webmail::CC_CHOOSE_FOLDER_PAGE_V0
    subdomain_field: mailbox
  - code: webmail::CC_CHOOSE_MESSAGE_TEXT_V0
    subdomain_field: mailbox
  - code: webmail::CC_DECIDE_READ_STATE_V0
    subdomain_field: mailbox
  - code: webmail::RB_MAILBOX_BINDINGS_V0
    subdomain_field: mailbox
  - code: webmail::WF_LIST_FOLDER_V0
    subdomain_field: mailbox
  - code: webmail::WF_MARK_MESSAGE_V0
    subdomain_field: mailbox
  - code: webmail::WF_OPEN_MESSAGE_V0
    subdomain_field: mailbox
  - code: webmail::WF_REPORT_CHANGE_OUTCOME_V0
    subdomain_field: mailbox
  new_capabilities:
  - code: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    purpose: Orders identifiers newest received first and cuts the page asked for
    inputs: message_ids:array, page:integer, page_size:integer
    outputs: page_ids:array, more_exist:boolean, folder_empty:boolean, message_count:integer
  - code: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    purpose: Chooses a message's plain-text part from its parts, or says its text cannot be displayed
      yet
    inputs: parts:array
    outputs: text_part:string, text_displayable:boolean, shown_headers:array
  - code: webmail::CT_PURE_DECIDE_READ_STATE_V0
    purpose: Decides a change of read state from the state held and the state asked for
    inputs: seen:boolean, wanted_read:boolean
    outputs: change:string, read_now:boolean
  new_intents:
  - code: webmail::IN_LIST_FOLDER_V0
    purpose: A host's report of a folder's message identifiers and the page asked for
    workflow: WF_LIST_FOLDER_V0
    inputs: host_id:string, mailbox:string, folder:string, provider_answer:string, message_ids:array,
      page:integer
  - code: webmail::IN_MARK_MESSAGE_V0
    purpose: A host's report of a message's read state and the state the person asked for
    workflow: WF_MARK_MESSAGE_V0
    inputs: host_id:string, mailbox:string, folder:string, provider_answer:string, message_id:integer,
      seen:boolean, wanted_read:boolean
  - code: webmail::IN_OPEN_MESSAGE_V0
    purpose: A host's report of the read state and the parts of a message the person asked to open
    workflow: WF_OPEN_MESSAGE_V0
    inputs: host_id:string, mailbox:string, folder:string, provider_answer:string, message_id:integer,
      seen:boolean, parts:array
  - code: webmail::IN_REPORT_CHANGE_OUTCOME_V0
    purpose: A host's report of whether the provider accepted a decided change
    workflow: WF_REPORT_CHANGE_OUTCOME_V0
    inputs: host_id:string, mailbox:string, folder:string, provider_answer:string, message_id:integer,
      change:string
  cross_subdomain_notes: []
```

The 23 artifacts of `webmail`'s design of record, scheduled in dependency order. Written by
`python -m transformation.record` from the P7 beside it. The mandate orders the build; it decides
nothing.
