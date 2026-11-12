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
    code: book_library_mgmt::EV_BOOK_REINSTATED_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '6'
    code: book_library_mgmt::EV_BOOK_RETIRED_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '7'
    code: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V1
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '8'
    code: book_library_mgmt::EV_PHYSICAL_COPY_REINSTATED_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '9'
    code: book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '10'
    code: book_library_mgmt::EV_WORK_REGISTERED_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '11'
    code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '12'
    code: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '13'
    code: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '14'
    code: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '15'
    code: book_library_mgmt::CC_CHECK_REGISTER_ADDITIONAL_EDITION_SUBMISSION_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '16'
    code: book_library_mgmt::CC_CHECK_REGISTER_BOOK_SUBMISSION_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '17'
    code: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V1
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '18'
    code: book_library_mgmt::CC_CONFIRM_BOOK_IDENTITY_UNCHANGED_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '19'
    code: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '20'
    code: book_library_mgmt::CC_MOVE_BOOK_FROM_REGISTERED_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '21'
    code: book_library_mgmt::CC_MOVE_BOOK_FROM_RETIRED_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '22'
    code: book_library_mgmt::CC_MOVE_PHYSICAL_COPY_FROM_REGISTERED_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '23'
    code: book_library_mgmt::CC_MOVE_PHYSICAL_COPY_FROM_RETIRED_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '24'
    code: book_library_mgmt::CC_RECORD_CATALOG_MOMENT_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '25'
    code: book_library_mgmt::CC_REKEY_BOOK_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '26'
    code: book_library_mgmt::CC_REQUIRE_COPY_BARCODE_FREE_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '27'
    code: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V1
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '28'
    code: book_library_mgmt::CC_WRITE_CORRECTED_BOOK_RECORD_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '29'
    code: book_library_mgmt::CC_WRITE_PHYSICAL_COPY_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '30'
    code: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '31'
    code: book_library_mgmt::IN_REGISTER_BOOK_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '32'
    code: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '33'
    code: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V1
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '34'
    code: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V1
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '35'
    code: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '36'
    code: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '37'
    code: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '38'
    code: book_library_mgmt::IN_SEARCH_CATALOG_V2
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '39'
    code: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '2'
    step: '40'
    code: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V1
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
  - wave: '2'
    step: '41'
    code: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V1
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
  - wave: '2'
    step: '42'
    code: book_library_mgmt::CC_RESOLVE_WORK_V1
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
  - wave: '2'
    step: '43'
    code: book_library_mgmt::CC_RETRIEVE_BOOK_DETAILS_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    - book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
  - wave: '2'
    step: '44'
    code: book_library_mgmt::CC_SEARCH_CATALOG_V3
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
    - book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
  - wave: '2'
    step: '45'
    code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    - book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
  - wave: '2'
    step: '46'
    code: book_library_mgmt::CC_WRITE_BOOK_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
  - wave: '2'
    step: '47'
    code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  - wave: '3'
    step: '48'
    code: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V1
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::RB_CATALOG_BINDINGS_V0
    - book_library_mgmt::AC_LIBRARY_STAFF_V0
    - book_library_mgmt::EV_BOOK_REGISTERED_V0
    - book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    - book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - book_library_mgmt::CC_CHECK_REGISTER_ADDITIONAL_EDITION_SUBMISSION_V0
    - book_library_mgmt::CC_RESOLVE_WORK_V1
    - book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V1
    - book_library_mgmt::CC_WRITE_BOOK_V0
    - book_library_mgmt::CC_RECORD_CATALOG_MOMENT_V0
  - wave: '3'
    step: '49'
    code: book_library_mgmt::WF_REGISTER_BOOK_V1
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::RB_CATALOG_BINDINGS_V0
    - book_library_mgmt::AC_LIBRARY_STAFF_V0
    - book_library_mgmt::EV_WORK_REGISTERED_V0
    - book_library_mgmt::EV_BOOK_REGISTERED_V0
    - book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V1
    - book_library_mgmt::IN_REGISTER_BOOK_V0
    - book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - book_library_mgmt::CC_CHECK_REGISTER_BOOK_SUBMISSION_V0
    - book_library_mgmt::CC_REQUIRE_COPY_BARCODE_FREE_V0
    - book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V1
    - book_library_mgmt::CC_CLAIM_COPY_BARCODE_V1
    - book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V1
    - book_library_mgmt::CC_WRITE_BOOK_V0
    - book_library_mgmt::CC_WRITE_PHYSICAL_COPY_V0
    - book_library_mgmt::CC_RECORD_CATALOG_MOMENT_V0
  - wave: '3'
    step: '50'
    code: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V1
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::RB_CATALOG_BINDINGS_V0
    - book_library_mgmt::AC_LIBRARY_STAFF_V0
    - book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V1
    - book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    - book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V1
    - book_library_mgmt::CC_CLAIM_COPY_BARCODE_V1
    - book_library_mgmt::CC_WRITE_PHYSICAL_COPY_V0
    - book_library_mgmt::CC_RECORD_CATALOG_MOMENT_V0
  - wave: '3'
    step: '51'
    code: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V2
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::RB_CATALOG_BINDINGS_V0
    - book_library_mgmt::AC_LIBRARY_STAFF_V0
    - book_library_mgmt::EV_BOOK_REINSTATED_V0
    - book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V1
    - book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - book_library_mgmt::CC_MOVE_BOOK_FROM_RETIRED_V0
    - book_library_mgmt::CC_RECORD_CATALOG_MOMENT_V0
  - wave: '3'
    step: '52'
    code: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V2
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::RB_CATALOG_BINDINGS_V0
    - book_library_mgmt::AC_LIBRARY_STAFF_V0
    - book_library_mgmt::EV_PHYSICAL_COPY_REINSTATED_V0
    - book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V1
    - book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - book_library_mgmt::CC_MOVE_PHYSICAL_COPY_FROM_RETIRED_V0
    - book_library_mgmt::CC_RECORD_CATALOG_MOMENT_V0
  - wave: '3'
    step: '53'
    code: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V1
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::RB_CATALOG_BINDINGS_V0
    - book_library_mgmt::AC_LIBRARY_STAFF_V0
    - book_library_mgmt::EV_BOOK_RETIRED_V0
    - book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
    - book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - book_library_mgmt::CC_MOVE_BOOK_FROM_REGISTERED_V0
    - book_library_mgmt::CC_RECORD_CATALOG_MOMENT_V0
  - wave: '3'
    step: '54'
    code: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V1
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::RB_CATALOG_BINDINGS_V0
    - book_library_mgmt::AC_LIBRARY_STAFF_V0
    - book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
    - book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
    - book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - book_library_mgmt::CC_MOVE_PHYSICAL_COPY_FROM_REGISTERED_V0
    - book_library_mgmt::CC_RECORD_CATALOG_MOMENT_V0
  - wave: '3'
    step: '55'
    code: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V1
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::RB_CATALOG_BINDINGS_V0
    - book_library_mgmt::AC_LIBRARY_STAFF_V0
    - book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    - book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - book_library_mgmt::CC_RECORD_CATALOG_MOMENT_V0
    - book_library_mgmt::CC_RETRIEVE_BOOK_DETAILS_V0
  - wave: '3'
    step: '56'
    code: book_library_mgmt::WF_SEARCH_CATALOG_V3
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::RB_CATALOG_BINDINGS_V0
    - book_library_mgmt::AC_LIBRARY_STAFF_V0
    - book_library_mgmt::IN_SEARCH_CATALOG_V2
    - book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - book_library_mgmt::CC_RECORD_CATALOG_MOMENT_V0
    - book_library_mgmt::CC_SEARCH_CATALOG_V3
  - wave: '3'
    step: '57'
    code: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::RB_CATALOG_BINDINGS_V0
    - book_library_mgmt::AC_LIBRARY_STAFF_V0
    - book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
    - book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    - book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V1
    - book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    - book_library_mgmt::CC_CONFIRM_BOOK_IDENTITY_UNCHANGED_V0
    - book_library_mgmt::CC_WRITE_CORRECTED_BOOK_RECORD_V0
    - book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V1
    - book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V1
    - book_library_mgmt::CC_REKEY_BOOK_V0
    - book_library_mgmt::CC_RECORD_CATALOG_MOMENT_V0
  critical_path:
  - position: '1'
    code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
  - position: '2'
    code: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V1
  - position: '3'
    code: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V1
  mandate_artifact_summary:
  - action: NEW
    count: '57'
    description: 1 STRUCTURE, 1 AC, 8 EV, 4 CT, 22 CC, 10 IN, 10 WF, 1 RB
  field_declarations:
  - code: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    subdomain_field: catalog
  - code: book_library_mgmt::AC_LIBRARY_STAFF_V0
    subdomain_field: catalog
  - code: book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
    subdomain_field: catalog
  - code: book_library_mgmt::EV_BOOK_REGISTERED_V0
    subdomain_field: catalog
  - code: book_library_mgmt::EV_BOOK_REINSTATED_V0
    subdomain_field: catalog
  - code: book_library_mgmt::EV_BOOK_RETIRED_V0
    subdomain_field: catalog
  - code: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V1
    subdomain_field: catalog
  - code: book_library_mgmt::EV_PHYSICAL_COPY_REINSTATED_V0
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
  - code: book_library_mgmt::CC_CHECK_REGISTER_ADDITIONAL_EDITION_SUBMISSION_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_CHECK_REGISTER_BOOK_SUBMISSION_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V1
    subdomain_field: catalog
  - code: book_library_mgmt::CC_CONFIRM_BOOK_IDENTITY_UNCHANGED_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_MOVE_BOOK_FROM_REGISTERED_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_MOVE_BOOK_FROM_RETIRED_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_MOVE_PHYSICAL_COPY_FROM_REGISTERED_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_MOVE_PHYSICAL_COPY_FROM_RETIRED_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_RECORD_CATALOG_MOMENT_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_REKEY_BOOK_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_REQUIRE_COPY_BARCODE_FREE_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V1
    subdomain_field: catalog
  - code: book_library_mgmt::CC_WRITE_CORRECTED_BOOK_RECORD_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_WRITE_PHYSICAL_COPY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_REGISTER_BOOK_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V1
    subdomain_field: catalog
  - code: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V1
    subdomain_field: catalog
  - code: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_SEARCH_CATALOG_V2
    subdomain_field: catalog
  - code: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V1
    subdomain_field: catalog
  - code: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V1
    subdomain_field: catalog
  - code: book_library_mgmt::CC_RESOLVE_WORK_V1
    subdomain_field: catalog
  - code: book_library_mgmt::CC_RETRIEVE_BOOK_DETAILS_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_SEARCH_CATALOG_V3
    subdomain_field: catalog
  - code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    subdomain_field: catalog
  - code: book_library_mgmt::CC_WRITE_BOOK_V0
    subdomain_field: catalog
  - code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V1
    subdomain_field: catalog
  - code: book_library_mgmt::WF_REGISTER_BOOK_V1
    subdomain_field: catalog
  - code: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V1
    subdomain_field: catalog
  - code: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V2
    subdomain_field: catalog
  - code: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V2
    subdomain_field: catalog
  - code: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V1
    subdomain_field: catalog
  - code: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V1
    subdomain_field: catalog
  - code: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V1
    subdomain_field: catalog
  - code: book_library_mgmt::WF_SEARCH_CATALOG_V3
    subdomain_field: catalog
  - code: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
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
    purpose: A request to register additional edition
    workflow: WF_REGISTER_ADDITIONAL_EDITION_V1
    inputs: staff_credentials:object, staff_id:string, title:string, author:string, publication_year:integer,
      subject:array
  - code: book_library_mgmt::IN_REGISTER_BOOK_V0
    purpose: A request to register book
    workflow: WF_REGISTER_BOOK_V1
    inputs: staff_credentials:object, title:string, author:string, publication_year:integer, book_fields:object,
      barcode:string, copy_fields:object, staff_id:string
  - code: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    purpose: A request to register physical copy
    workflow: WF_REGISTER_PHYSICAL_COPY_V1
    inputs: staff_credentials:object, identity_key:string, barcode:string, copy_fields:object, staff_id:string
  - code: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V1
    purpose: A request to reinstate book record
    workflow: WF_REINSTATE_BOOK_RECORD_V2
    inputs: staff_credentials:object, identity_key:string, staff_id:string
  - code: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V1
    purpose: A request to reinstate physical copy
    workflow: WF_REINSTATE_PHYSICAL_COPY_V2
    inputs: staff_credentials:object, barcode:string, staff_id:string
  - code: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
    purpose: A request to retire book record
    workflow: WF_RETIRE_BOOK_RECORD_V1
    inputs: staff_credentials:object, identity_key:string, staff_id:string
  - code: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
    purpose: A request to retire physical copy
    workflow: WF_RETIRE_PHYSICAL_COPY_V1
    inputs: staff_credentials:object, barcode:string, staff_id:string
  - code: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    purpose: A request to retrieve book details
    workflow: WF_RETRIEVE_BOOK_DETAILS_V1
    inputs: staff_credentials:object, identity_key:string, staff_id:string
  - code: book_library_mgmt::IN_SEARCH_CATALOG_V2
    purpose: A request to search catalog
    workflow: WF_SEARCH_CATALOG_V3
    inputs: staff_credentials:object, search_criteria:object, staff_id:string
  - code: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    purpose: A request to update bibliographic information
    workflow: WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    inputs: staff_credentials:object, staff_id:string, identity_key:string, updated_fields:object
  cross_subdomain_notes: []
```

The 57 artifacts of `book_library_mgmt`'s design of record, scheduled in dependency order. Written by
`python -m transformation.record` from the P7 beside it. The mandate orders the build; it decides
nothing.
