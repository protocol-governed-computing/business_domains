# CC_CHOOSE_FOLDER_PAGE_V0

## Machine

```yaml
fqdn: webmail::CC_CHOOSE_FOLDER_PAGE_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: mailbox
core:
  summary: Chooses a page of a folder's identifiers, newest received first
  inputs:
    message_ids:
      type: array
      required: true
    page:
      type: integer
      required: true
  outputs:
    page_ids:
      type: array
      required: true
    more_exist:
      type: boolean
      required: true
    folder_empty:
      type: boolean
      required: true
    message_count:
      type: integer
      required: true
  result_status_contract:
    allowed:
    - SUCCESS
    - VIOLATION
    on_input_failure: VIOLATION
  pipeline:
  - step: choose_page
    transform: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
    inputs:
      message_ids: $.inputs.message_ids
      page: $.inputs.page
      page_size: 50
    outputs:
      page_ids: $.capability_result.page_ids
      more_exist: $.capability_result.more_exist
      folder_empty: $.capability_result.folder_empty
      message_count: $.capability_result.message_count
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: exit
      VIOLATION: exit
```

---

## Intent

Chooses a page of a folder's identifiers, newest received first
