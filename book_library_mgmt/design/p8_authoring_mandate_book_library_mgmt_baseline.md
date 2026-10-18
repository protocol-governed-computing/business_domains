# Authoring Mandate — book_library_mgmt, baseline

## Machine

```yaml
document:
  phase: p8
  domain: book_library_mgmt
  subdomain:
  - catalog
  cr: baseline
  rule_set: transformation.schemas.REGISTER_SCHEMA_P8_V0
registers:
  build_order:
  - wave: '1'
    step: '1'
    code: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '2'
    code: book_library_mgmt::AC_LIBRARY_STAFF_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '3'
    code: book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '4'
    code: book_library_mgmt::EV_BOOK_REGISTERED_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '5'
    code: book_library_mgmt::EV_BOOK_RETIRED_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '6'
    code: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '7'
    code: book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '8'
    code: book_library_mgmt::EV_WORK_REGISTERED_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '9'
    code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '10'
    code: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '11'
    code: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '12'
    code: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '13'
    code: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '14'
    code: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '15'
    code: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '16'
    code: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '17'
    code: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '18'
    code: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '19'
    code: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '20'
    code: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '21'
    code: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '22'
    code: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '23'
    code: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '24'
    code: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '25'
    code: book_library_mgmt::IN_REGISTER_BOOK_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '26'
    code: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '27'
    code: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '28'
    code: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '29'
    code: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '30'
    code: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '31'
    code: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '32'
    code: book_library_mgmt::IN_SEARCH_CATALOG_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '33'
    code: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '2'
    step: '34'
    code: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    - book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
  - wave: '2'
    step: '35'
    code: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
  - wave: '2'
    step: '36'
    code: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
  - wave: '2'
    step: '37'
    code: book_library_mgmt::CC_REGISTER_BOOK_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
  - wave: '2'
    step: '38'
    code: book_library_mgmt::CC_RESOLVE_WORK_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
  - wave: '2'
    step: '39'
    code: book_library_mgmt::CC_SEARCH_CATALOG_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
  - wave: '2'
    step: '40'
    code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
  - wave: '2'
    step: '41'
    code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  - wave: '3'
    step: '42'
    code: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::RB_CATALOG_BINDINGS_V0
    - book_library_mgmt::AC_LIBRARY_STAFF_V0
    - book_library_mgmt::EV_BOOK_REGISTERED_V0
    - book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    - book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    - book_library_mgmt::CC_RESOLVE_WORK_V0
    - book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    - book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    - book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
  - wave: '3'
    step: '43'
    code: book_library_mgmt::WF_REGISTER_BOOK_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::RB_CATALOG_BINDINGS_V0
    - book_library_mgmt::AC_LIBRARY_STAFF_V0
    - book_library_mgmt::EV_WORK_REGISTERED_V0
    - book_library_mgmt::EV_BOOK_REGISTERED_V0
    - book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
    - book_library_mgmt::IN_REGISTER_BOOK_V0
    - book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    - book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    - book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    - book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    - book_library_mgmt::CC_REGISTER_BOOK_V0
    - book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    - book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
  - wave: '3'
    step: '44'
    code: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::RB_CATALOG_BINDINGS_V0
    - book_library_mgmt::AC_LIBRARY_STAFF_V0
    - book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
    - book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    - book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    - book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    - book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
  - wave: '3'
    step: '45'
    code: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::RB_CATALOG_BINDINGS_V0
    - book_library_mgmt::AC_LIBRARY_STAFF_V0
    - book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
    - book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
    - book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
  - wave: '3'
    step: '46'
    code: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::RB_CATALOG_BINDINGS_V0
    - book_library_mgmt::AC_LIBRARY_STAFF_V0
    - book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
    - book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
    - book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
  - wave: '3'
    step: '47'
    code: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::RB_CATALOG_BINDINGS_V0
    - book_library_mgmt::AC_LIBRARY_STAFF_V0
    - book_library_mgmt::EV_BOOK_RETIRED_V0
    - book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
    - book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    - book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
  - wave: '3'
    step: '48'
    code: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::RB_CATALOG_BINDINGS_V0
    - book_library_mgmt::AC_LIBRARY_STAFF_V0
    - book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
    - book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
    - book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    - book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
  - wave: '3'
    step: '49'
    code: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::RB_CATALOG_BINDINGS_V0
    - book_library_mgmt::AC_LIBRARY_STAFF_V0
    - book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    - book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    - book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
  - wave: '3'
    step: '50'
    code: book_library_mgmt::WF_SEARCH_CATALOG_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::RB_CATALOG_BINDINGS_V0
    - book_library_mgmt::AC_LIBRARY_STAFF_V0
    - book_library_mgmt::IN_SEARCH_CATALOG_V0
    - book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - book_library_mgmt::CC_SEARCH_CATALOG_V0
    - book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
  - wave: '3'
    step: '51'
    code: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::RB_CATALOG_BINDINGS_V0
    - book_library_mgmt::AC_LIBRARY_STAFF_V0
    - book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
    - book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    - book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
    - book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    - book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
  critical_path:
  - position: '1'
    code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
  - position: '2'
    code: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
  - position: '3'
    code: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
  mandate_artifact_summary:
  - action: NEW
    count: '51'
    description: 1 STRUCTURE, 1 AC, 6 EV, 4 CT, 18 CC, 10 IN, 10 WF, 1 RB
  field_declarations:
  - code: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    subdomain_field: catalog
  - code: book_library_mgmt::AC_LIBRARY_STAFF_V0
    subdomain_field: catalog
  - code: book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
    subdomain_field: catalog
  - code: book_library_mgmt::EV_BOOK_REGISTERED_V0
    subdomain_field: catalog
  - code: book_library_mgmt::EV_BOOK_RETIRED_V0
    subdomain_field: catalog
  - code: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
    subdomain_field: catalog
  - code: book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
    subdomain_field: catalog
  - code: book_library_mgmt::EV_WORK_REGISTERED_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_REGISTER_BOOK_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_SEARCH_CATALOG_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_REGISTER_BOOK_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_RESOLVE_WORK_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_SEARCH_CATALOG_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    subdomain_field: catalog
  - code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_REGISTER_BOOK_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_SEARCH_CATALOG_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    subdomain_field: catalog
  new_capabilities:
  - code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    purpose: Forms the single key the registry claims from the three identifying attributes
    inputs: title:string, author:string, publication_year:integer
    outputs: identity_key:string
  - code: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    purpose: Forms the single key claimed for a work from its title and author
    inputs: title:string, author:string
    outputs: work_key:string
  - code: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
    purpose: Groups records by the value of a named attribute, returning one group per distinct value
    inputs: source:array, attribute:string
    outputs: grouped:array
  - code: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
    purpose: Selects the records matching stated criteria and returns none when none match
    inputs: source:array, filter:object
    outputs: extracted:array
  new_intents:
  - code: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    purpose: The boundary that admits a request to register a further edition of a work the catalog already
      holds
    workflow: WF_REGISTER_ADDITIONAL_EDITION_V0
    inputs: staff_credentials:object, staff_id:string, title:string, author:string, publication_year:integer,
      subject:array
  - code: book_library_mgmt::IN_REGISTER_BOOK_V0
    purpose: A request to register a book together with its first physical copy
    workflow: WF_REGISTER_BOOK_V0
    inputs: staff_credentials:object, title:string, author:string, publication_year:integer, book_fields:object,
      barcode:string, copy_fields:object, staff_id:string
  - code: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    purpose: A request to register a further copy against a registered book
    workflow: WF_REGISTER_PHYSICAL_COPY_V0
    inputs: staff_credentials:object, identity_key:string, barcode:string, copy_fields:object, staff_id:string
  - code: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
    purpose: A request to return a retired book record to the registered state
    workflow: WF_REINSTATE_BOOK_RECORD_V0
    inputs: staff_credentials:object, identity_key:string, staff_id:string
  - code: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
    purpose: A request to return a retired copy to the registered state
    workflow: WF_REINSTATE_PHYSICAL_COPY_V0
    inputs: staff_credentials:object, barcode:string, staff_id:string
  - code: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
    purpose: A request to retire a book record judged obsolete
    workflow: WF_RETIRE_BOOK_RECORD_V0
    inputs: staff_credentials:object, identity_key:string, staff_id:string
  - code: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
    purpose: A request to retire a lost or damaged copy
    workflow: WF_RETIRE_PHYSICAL_COPY_V0
    inputs: staff_credentials:object, barcode:string, staff_id:string
  - code: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    purpose: A request for a book's complete details with the copies held
    workflow: WF_RETRIEVE_BOOK_DETAILS_V0
    inputs: staff_credentials:object, identity_key:string, staff_id:string
  - code: book_library_mgmt::IN_SEARCH_CATALOG_V0
    purpose: A request to locate material by subject or by title
    workflow: WF_SEARCH_CATALOG_V0
    inputs: staff_credentials:object, search_criteria:object, staff_id:string
  - code: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    purpose: A request to change a registered book's description
    workflow: WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    inputs: staff_credentials:object, staff_id:string, identity_key:string, updated_fields:object
  cross_subdomain_notes: []
```

The 51 artifacts of `book_library_mgmt`'s design of record, scheduled in dependency order. Written by
`python -m transformation.record` from the P7 beside it. The mandate orders the build; it decides
nothing.
