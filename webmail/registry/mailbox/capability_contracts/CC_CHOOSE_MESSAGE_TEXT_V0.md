# CC_CHOOSE_MESSAGE_TEXT_V0

## Machine

```yaml
fqdn: webmail::CC_CHOOSE_MESSAGE_TEXT_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: mailbox
core:
  summary: Chooses the plain-text part of a message to show, or says none can be displayed
  inputs:
    parts:
      type: array
      required: true
  outputs:
    text_part:
      type: string
      required: true
    text_displayable:
      type: boolean
      required: true
    shown_headers:
      type: array
      required: true
  result_status_contract:
    allowed:
    - SUCCESS
    - VIOLATION
    on_input_failure: VIOLATION
  pipeline:
  - step: choose_text
    transform: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
    inputs:
      parts: $.inputs.parts
    outputs:
      text_part: $.capability_result.text_part
      text_displayable: $.capability_result.text_displayable
      shown_headers: $.capability_result.shown_headers
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: exit
      VIOLATION: exit
```

---

## Intent

Chooses the plain-text part of a message to show, or says none can be displayed
