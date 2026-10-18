# Design Intent — book_library_mgmt, baseline

## Machine

```yaml
document:
  phase: p7
  domain: book_library_mgmt
  subdomain:
  - catalog
  cr: baseline
  rule_set: transformation.schemas.REGISTER_SCHEMA_P7_V0
registers:
  design_resolution: []
  existing_inventory: []
  new_artifacts:
  - family: AC
    code: book_library_mgmt::AC_LIBRARY_STAFF_V0
    summary: The actor whose authorization every catalog operation binds
    owner_subdomain: catalog
    status: NEW
  - family: CC
    code: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    summary: Append a durable account of a performed operation to the catalog's own trail
    owner_subdomain: catalog
    status: NEW
  - family: CC
    code: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    summary: Assembles an edition, the physical copies of it, and the record of the work it belongs to
    owner_subdomain: catalog
    status: NEW
  - family: CC
    code: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    summary: Claim a book's identity so a second registration of the same book is refused
    owner_subdomain: catalog
    status: NEW
  - family: CC
    code: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    summary: Claim a copy's barcode so a second copy carrying it is refused
    owner_subdomain: catalog
    status: NEW
  - family: CC
    code: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    summary: Forms the work key, claims it, and writes the work record when the claim is new
    owner_subdomain: catalog
    status: NEW
  - family: CC
    code: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    summary: Confirm the staff member may perform catalog operations
    owner_subdomain: catalog
    status: NEW
  - family: CC
    code: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    summary: Assembles the edition record against a resolved work and writes it
    owner_subdomain: catalog
    status: NEW
  - family: CC
    code: book_library_mgmt::CC_REGISTER_BOOK_V0
    summary: Validates, assembles and writes an edition record against the work it belongs to
    owner_subdomain: catalog
    status: NEW
  - family: CC
    code: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    summary: Record a copy against exactly one book
    owner_subdomain: catalog
    status: NEW
  - family: CC
    code: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
    summary: Mark a retired book record registered again
    owner_subdomain: catalog
    status: NEW
  - family: CC
    code: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
    summary: Mark a retired copy registered again
    owner_subdomain: catalog
    status: NEW
  - family: CC
    code: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
    summary: Resolve a registered book's identity key
    owner_subdomain: catalog
    status: NEW
  - family: CC
    code: book_library_mgmt::CC_RESOLVE_WORK_V0
    summary: Forms the work key, resolves it against the registry, and reads the work record it names
    owner_subdomain: catalog
    status: NEW
  - family: CC
    code: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    summary: Mark a book record retired so it is no longer offered as current
    owner_subdomain: catalog
    status: NEW
  - family: CC
    code: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    summary: Mark a copy retired so the library no longer holds it
    owner_subdomain: catalog
    status: NEW
  - family: CC
    code: book_library_mgmt::CC_SEARCH_CATALOG_V0
    summary: Selects the registered editions matching a subject or title and groups them under their work
    owner_subdomain: catalog
    status: NEW
  - family: CC
    code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    summary: Changes a registered edition's descriptive content and refuses a change that would duplicate
      another edition
    owner_subdomain: catalog
    status: NEW
  - family: CC
    code: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    summary: Confirms a registration carries what a work and an edition require, before any identity is
      claimed
    owner_subdomain: catalog
    status: NEW
  - family: CT
    code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    summary: Forms the single key the registry claims from the three identifying attributes
    owner_subdomain: catalog
    status: NEW
  - family: CT
    code: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    summary: Forms the single key claimed for a work from its title and author
    owner_subdomain: catalog
    status: NEW
  - family: CT
    code: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
    summary: Groups records by the value of a named attribute, returning one group per distinct value
    owner_subdomain: catalog
    status: NEW
  - family: CT
    code: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
    summary: Selects the records matching stated criteria and returns none when none match
    owner_subdomain: catalog
    status: NEW
  - family: EV
    code: book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
    summary: The authoritative description of a book changed
    owner_subdomain: catalog
    status: NEW
  - family: EV
    code: book_library_mgmt::EV_BOOK_REGISTERED_V0
    summary: A book entered the catalog and acquired its authoritative record
    owner_subdomain: catalog
    status: NEW
  - family: EV
    code: book_library_mgmt::EV_BOOK_RETIRED_V0
    summary: A book record is no longer to be used
    owner_subdomain: catalog
    status: NEW
  - family: EV
    code: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
    summary: The library recorded another copy it owns
    owner_subdomain: catalog
    status: NEW
  - family: EV
    code: book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
    summary: The library no longer holds that copy
    owner_subdomain: catalog
    status: NEW
  - family: EV
    code: book_library_mgmt::EV_WORK_REGISTERED_V0
    summary: The moment a work enters the catalog, created by the edition that evidences it
    owner_subdomain: catalog
    status: NEW
  - family: IN
    code: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    summary: The boundary that admits a request to register a further edition of a work the catalog already
      holds
    owner_subdomain: catalog
    status: NEW
  - family: IN
    code: book_library_mgmt::IN_REGISTER_BOOK_V0
    summary: A request to register a book together with its first physical copy
    owner_subdomain: catalog
    status: NEW
  - family: IN
    code: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    summary: A request to register a further copy against a registered book
    owner_subdomain: catalog
    status: NEW
  - family: IN
    code: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
    summary: A request to return a retired book record to the registered state
    owner_subdomain: catalog
    status: NEW
  - family: IN
    code: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
    summary: A request to return a retired copy to the registered state
    owner_subdomain: catalog
    status: NEW
  - family: IN
    code: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
    summary: A request to retire a book record judged obsolete
    owner_subdomain: catalog
    status: NEW
  - family: IN
    code: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
    summary: A request to retire a lost or damaged copy
    owner_subdomain: catalog
    status: NEW
  - family: IN
    code: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    summary: A request for a book's complete details with the copies held
    owner_subdomain: catalog
    status: NEW
  - family: IN
    code: book_library_mgmt::IN_SEARCH_CATALOG_V0
    summary: A request to locate material by subject or by title
    owner_subdomain: catalog
    status: NEW
  - family: IN
    code: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    summary: A request to change a registered book's description
    owner_subdomain: catalog
    status: NEW
  - family: STRUCTURE
    code: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    summary: Declares the stores the catalog owns and the paths they occupy
    owner_subdomain: catalog
    status: NEW
  - family: RB
    code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    summary: Binds the catalog's workflows to the stores and mechanisms they use
    owner_subdomain: catalog
    status: NEW
  - family: WF
    code: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    summary: The governed sequence that registers a further edition of a work the library already holds
    owner_subdomain: catalog
    status: NEW
  - family: WF
    code: book_library_mgmt::WF_REGISTER_BOOK_V0
    summary: The governed sequence that registers a work, its first edition and that edition's first physical
      copy
    owner_subdomain: catalog
    status: NEW
  - family: WF
    code: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    summary: The governed sequence that registers a further physical copy of an edition
    owner_subdomain: catalog
    status: NEW
  - family: WF
    code: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    summary: Returning a retired book record to the registered state
    owner_subdomain: catalog
    status: NEW
  - family: WF
    code: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    summary: Returning a retired copy to the registered state
    owner_subdomain: catalog
    status: NEW
  - family: WF
    code: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    summary: The governed sequence that takes a book out of service
    owner_subdomain: catalog
    status: NEW
  - family: WF
    code: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    summary: The governed sequence that takes a physical copy out of service
    owner_subdomain: catalog
    status: NEW
  - family: WF
    code: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    summary: Assembling a book with the copies the library holds of it
    owner_subdomain: catalog
    status: NEW
  - family: WF
    code: book_library_mgmt::WF_SEARCH_CATALOG_V0
    summary: Searching by subject or title, excluding retired books
    owner_subdomain: catalog
    status: NEW
  - family: WF
    code: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    summary: Corrects what the library publishes about a registered book
    owner_subdomain: catalog
    status: NEW
  rb_declarations:
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    binds_wf: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    binds_wf: book_library_mgmt::WF_REGISTER_BOOK_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    binds_wf: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    binds_wf: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    binds_wf: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    binds_wf: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    binds_wf: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    binds_wf: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    binds_wf: book_library_mgmt::WF_SEARCH_CATALOG_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    binds_wf: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  execution_topology:
  - workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    node: IN_REGISTER_ADDITIONAL_EDITION_V0
    node_type: IN
    routing:
      ACK: CC_CONFIRM_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    node: CC_CONFIRM_STAFF_AUTHORIZED_V0
    node_type: CC
    routing:
      SUCCESS: CC_VALIDATE_BOOK_SUBMISSION_V0
      VIOLATION: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    node: CC_VALIDATE_BOOK_SUBMISSION_V0
    node_type: CC
    routing:
      SUCCESS: CC_RESOLVE_WORK_V0
      VIOLATION: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    node: CC_RESOLVE_WORK_V0
    node_type: CC
    routing:
      SUCCESS: CC_CLAIM_BOOK_IDENTITY_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    node: CC_CLAIM_BOOK_IDENTITY_V0
    node_type: CC
    routing:
      SUCCESS: CC_REGISTER_ADDITIONAL_EDITION_V0
      ALREADY_EXISTS: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    node: CC_REGISTER_ADDITIONAL_EDITION_V0
    node_type: CC
    routing:
      SUCCESS: CC_APPEND_CATALOG_OPERATION_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    node: CC_APPEND_CATALOG_OPERATION_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    node: EXIT_COMPLETED
    node_type: EXIT
    routing: null
  - workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: IN_REGISTER_BOOK_V0
    node_type: IN
    routing:
      ACK: CC_CONFIRM_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: CC_CONFIRM_STAFF_AUTHORIZED_V0
    node_type: CC
    routing:
      SUCCESS: CC_VALIDATE_BOOK_SUBMISSION_V0
      VIOLATION: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: CC_VALIDATE_BOOK_SUBMISSION_V0
    node_type: CC
    routing:
      SUCCESS: CC_CLAIM_WORK_IDENTITY_V0
      VIOLATION: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: CC_CLAIM_WORK_IDENTITY_V0
    node_type: CC
    routing:
      SUCCESS: CC_CLAIM_BOOK_IDENTITY_V0
      ALREADY_EXISTS: CC_CLAIM_BOOK_IDENTITY_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: CC_CLAIM_BOOK_IDENTITY_V0
    node_type: CC
    routing:
      SUCCESS: CC_CLAIM_COPY_BARCODE_V0
      ALREADY_EXISTS: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: CC_CLAIM_COPY_BARCODE_V0
    node_type: CC
    routing:
      SUCCESS: CC_REGISTER_BOOK_V0
      ALREADY_EXISTS: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: CC_REGISTER_BOOK_V0
    node_type: CC
    routing:
      SUCCESS: CC_REGISTER_PHYSICAL_COPY_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: CC_REGISTER_PHYSICAL_COPY_V0
    node_type: CC
    routing:
      SUCCESS: CC_APPEND_CATALOG_OPERATION_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: CC_APPEND_CATALOG_OPERATION_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: EXIT_COMPLETED
    node_type: EXIT
    routing: null
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    node: IN_REGISTER_PHYSICAL_COPY_V0
    node_type: IN
    routing:
      ACK: CC_CONFIRM_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    node: CC_CONFIRM_STAFF_AUTHORIZED_V0
    node_type: CC
    routing:
      SUCCESS: CC_CLAIM_COPY_BARCODE_V0
      VIOLATION: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    node: CC_CLAIM_COPY_BARCODE_V0
    node_type: CC
    routing:
      SUCCESS: CC_REGISTER_PHYSICAL_COPY_V0
      ALREADY_EXISTS: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    node: CC_REGISTER_PHYSICAL_COPY_V0
    node_type: CC
    routing:
      SUCCESS: CC_APPEND_CATALOG_OPERATION_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    node: CC_APPEND_CATALOG_OPERATION_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    node: EXIT_COMPLETED
    node_type: EXIT
    routing: null
  - workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    node: IN_REINSTATE_BOOK_RECORD_V0
    node_type: IN
    routing:
      ACK: CC_CONFIRM_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    node: CC_CONFIRM_STAFF_AUTHORIZED_V0
    node_type: CC
    routing:
      SUCCESS: CC_REINSTATE_BOOK_RECORD_V0
      VIOLATION: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    node: CC_REINSTATE_BOOK_RECORD_V0
    node_type: CC
    routing:
      SUCCESS: CC_APPEND_CATALOG_OPERATION_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    node: CC_APPEND_CATALOG_OPERATION_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    node: EXIT_COMPLETED
    node_type: EXIT
    routing: null
  - workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    node: IN_REINSTATE_PHYSICAL_COPY_V0
    node_type: IN
    routing:
      ACK: CC_CONFIRM_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    node: CC_CONFIRM_STAFF_AUTHORIZED_V0
    node_type: CC
    routing:
      SUCCESS: CC_REINSTATE_PHYSICAL_COPY_V0
      VIOLATION: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    node: CC_REINSTATE_PHYSICAL_COPY_V0
    node_type: CC
    routing:
      SUCCESS: CC_APPEND_CATALOG_OPERATION_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    node: CC_APPEND_CATALOG_OPERATION_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    node: EXIT_COMPLETED
    node_type: EXIT
    routing: null
  - workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    node: IN_RETIRE_BOOK_RECORD_V0
    node_type: IN
    routing:
      ACK: CC_CONFIRM_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    node: CC_CONFIRM_STAFF_AUTHORIZED_V0
    node_type: CC
    routing:
      SUCCESS: CC_RETIRE_BOOK_RECORD_V0
      VIOLATION: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    node: CC_RETIRE_BOOK_RECORD_V0
    node_type: CC
    routing:
      SUCCESS: CC_APPEND_CATALOG_OPERATION_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    node: CC_APPEND_CATALOG_OPERATION_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    node: EXIT_COMPLETED
    node_type: EXIT
    routing: null
  - workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    node: IN_RETIRE_PHYSICAL_COPY_V0
    node_type: IN
    routing:
      ACK: CC_CONFIRM_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    node: CC_CONFIRM_STAFF_AUTHORIZED_V0
    node_type: CC
    routing:
      SUCCESS: CC_RETIRE_PHYSICAL_COPY_V0
      VIOLATION: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    node: CC_RETIRE_PHYSICAL_COPY_V0
    node_type: CC
    routing:
      SUCCESS: CC_APPEND_CATALOG_OPERATION_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    node: CC_APPEND_CATALOG_OPERATION_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    node: EXIT_COMPLETED
    node_type: EXIT
    routing: null
  - workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    node: IN_RETRIEVE_BOOK_DETAILS_V0
    node_type: IN
    routing:
      ACK: CC_CONFIRM_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    node: CC_CONFIRM_STAFF_AUTHORIZED_V0
    node_type: CC
    routing:
      SUCCESS: CC_APPEND_CATALOG_OPERATION_V0
      VIOLATION: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    node: CC_ASSEMBLE_BOOK_DETAILS_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    node: CC_APPEND_CATALOG_OPERATION_V0
    node_type: CC
    routing:
      SUCCESS: CC_ASSEMBLE_BOOK_DETAILS_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    node: EXIT_COMPLETED
    node_type: EXIT
    routing: null
  - workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
    node: IN_SEARCH_CATALOG_V0
    node_type: IN
    routing:
      ACK: CC_CONFIRM_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
    node: CC_CONFIRM_STAFF_AUTHORIZED_V0
    node_type: CC
    routing:
      SUCCESS: CC_APPEND_CATALOG_OPERATION_V0
      VIOLATION: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
    node: CC_SEARCH_CATALOG_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
    node: CC_APPEND_CATALOG_OPERATION_V0
    node_type: CC
    routing:
      SUCCESS: CC_SEARCH_CATALOG_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
    node: EXIT_COMPLETED
    node_type: EXIT
    routing: null
  - workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    node: IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    node_type: IN
    routing:
      ACK: CC_CONFIRM_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    node: CC_CONFIRM_STAFF_AUTHORIZED_V0
    node_type: CC
    routing:
      SUCCESS: CC_RESOLVE_BOOK_IDENTITY_V0
      VIOLATION: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    node: CC_RESOLVE_BOOK_IDENTITY_V0
    node_type: CC
    routing:
      SUCCESS: CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    node: CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    node_type: CC
    routing:
      SUCCESS: CC_APPEND_CATALOG_OPERATION_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    node: CC_APPEND_CATALOG_OPERATION_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    node: EXIT_COMPLETED
    node_type: EXIT
    routing: null
  - workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  cc_composition:
  - cc_code: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    step: '1'
    step_name: append_operation
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    kind: CS
    operation: APPEND
    store: CATALOG_OPERATIONS
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
  - cc_code: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: '1'
    step_name: read_book_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: READ
    store: BOOKS
    consumes:
    - key
    produces:
    - value
    - result_status
    - book_record
    routing:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
      out:
        value: value
        result_status: result_status
        book_record: book_record
  - cc_code: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: '2'
    step_name: form_work_key
    capability: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - title
    - author
    produces:
    - work_key
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        title: title
        author: author
      out:
        work_key: work_key
  - cc_code: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: '3'
    step_name: read_work_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: READ
    store: WORKS
    consumes:
    - key
    produces:
    - work_record
    routing:
      SUCCESS: continue
      NOT_FOUND: continue
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
      out:
        work_record: work_record
  - cc_code: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: '4'
    step_name: select_copy_records
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: SELECT
    store: PHYSICAL_COPIES
    consumes: null
    produces:
    - records
    - result_status
    routing:
      SUCCESS: continue
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in: {}
      out:
        records: records
        result_status: result_status
  - cc_code: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: '5'
    step_name: select_copies_of_book
    capability: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - source
    - filter
    produces:
    - copies_held
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        source: source
        filter: filter
      out:
        copies_held: copies_held
  - cc_code: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    step: '1'
    step_name: form_identity_key
    capability: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - title
    - author
    - publication_year
    produces:
    - identity_key
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        title: title
        author: author
        publication_year: publication_year
      out:
        identity_key: identity_key
  - cc_code: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    step: '2'
    step_name: claim_identity
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: REGISTER
    store: BOOK_IDENTITY_REGISTRY
    consumes:
    - key
    - target_cs
    - target_ref
    produces:
    - address
    - result_status
    routing:
      SUCCESS: exit
      ALREADY_EXISTS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
        target_cs: target_cs
        target_ref: target_ref
      out:
        address: address
        result_status: result_status
  - cc_code: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    step: '1'
    step_name: claim_barcode
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: REGISTER
    store: COPY_BARCODE_REGISTRY
    consumes:
    - key
    - target_cs
    - target_ref
    produces:
    - address
    - result_status
    routing:
      SUCCESS: exit
      ALREADY_EXISTS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
        target_cs: target_cs
        target_ref: target_ref
      out:
        address: address
        result_status: result_status
  - cc_code: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: '1'
    step_name: form_work_key
    capability: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - title
    - author
    produces:
    - work_key
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        title: title
        author: author
      out:
        work_key: work_key
  - cc_code: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: '2'
    step_name: claim_work
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: REGISTER
    store: WORK_IDENTITY_REGISTRY
    consumes:
    - key
    - target_cs
    - target_ref
    produces:
    - address
    - result_status
    routing:
      SUCCESS: continue
      ALREADY_EXISTS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
        target_cs: target_cs
        target_ref: target_ref
      out:
        address: address
        result_status: result_status
  - cc_code: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: '3'
    step_name: assemble_work_record
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - fields
    produces:
    - work_record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: fields
      out:
        work_record: work_record
  - cc_code: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: '4'
    step_name: write_work_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: WRITE
    store: WORKS
    consumes:
    - key
    - value
    produces:
    - result_status
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
        value: value
      out:
        result_status: result_status
  - cc_code: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    step: '1'
    step_name: confirm_authorization
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - parameters
    - rules
    produces:
    - is_authorized
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: parameters
        rules: rules
      out:
        is_authorized: is_authorized
  - cc_code: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: '1'
    step_name: validate_edition_fields
    capability: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - record
    - schema
    produces:
    - violations
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        record: record
        schema: schema
      out:
        violations: violations
  - cc_code: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: '2'
    step_name: refuse_incomplete_record
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - parameters
    - rules
    produces:
    - valid
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: parameters
        rules: rules
      out:
        valid: valid
  - cc_code: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: '3'
    step_name: assemble_edition_record
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - fields
    produces:
    - edition_record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: fields
      out:
        edition_record: edition_record
  - cc_code: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: '4'
    step_name: write_edition_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: WRITE
    store: BOOKS
    consumes:
    - key
    - value
    produces:
    - result_status
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
        value: value
      out:
        result_status: result_status
  - cc_code: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: '1'
    step_name: form_work_key
    capability: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - title
    - author
    produces:
    - work_key
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        title: title
        author: author
      out:
        work_key: work_key
  - cc_code: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: '2'
    step_name: validate_book_fields
    capability: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - record
    - schema
    produces:
    - violations
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        record: record
        schema: schema
      out:
        violations: violations
  - cc_code: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: '3'
    step_name: refuse_incomplete_record
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - parameters
    - rules
    produces:
    - valid
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: parameters
        rules: rules
      out:
        valid: valid
  - cc_code: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: '4'
    step_name: assemble_book_record
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - fields
    produces:
    - book_record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: fields
      out:
        book_record: book_record
  - cc_code: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: '5'
    step_name: write_book_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: WRITE
    store: BOOKS
    consumes:
    - key
    - value
    produces:
    - result_status
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
        value: value
      out:
        result_status: result_status
  - cc_code: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    step: '1'
    step_name: read_book_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: READ
    store: BOOKS
    consumes:
    - key
    produces:
    - book_record
    - result_status
    routing:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
      out:
        book_record: book_record
        result_status: result_status
  - cc_code: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    step: '2'
    step_name: assemble_copy_record
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - fields
    produces:
    - copy_record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: fields
      out:
        copy_record: copy_record
  - cc_code: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    step: '3'
    step_name: write_copy_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: WRITE
    store: PHYSICAL_COPIES
    consumes:
    - key
    - value
    produces:
    - result_status
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
        value: value
      out:
        result_status: result_status
  - cc_code: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
    step: '1'
    step_name: set_record_state
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: UPDATE_WHERE
    store: BOOKS
    consumes:
    - filter
    - updates
    produces:
    - matched_keys
    - updated_count
    - result_status
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        filter: filter
        updates: updates
      out:
        matched_keys: matched_keys
        updated_count: updated_count
        result_status: result_status
  - cc_code: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
    step: '1'
    step_name: set_record_state
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: UPDATE_WHERE
    store: PHYSICAL_COPIES
    consumes:
    - filter
    - updates
    produces:
    - matched_keys
    - updated_count
    - result_status
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        filter: filter
        updates: updates
      out:
        matched_keys: matched_keys
        updated_count: updated_count
        result_status: result_status
  - cc_code: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
    step: '1'
    step_name: resolve_identity
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: RESOLVE
    store: BOOK_IDENTITY_REGISTRY
    consumes:
    - key_or_address
    produces:
    - target_ref
    - result_status
    routing:
      SUCCESS: exit
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key_or_address: key_or_address
      out:
        target_ref: target_ref
        result_status: result_status
  - cc_code: book_library_mgmt::CC_RESOLVE_WORK_V0
    step: '1'
    step_name: form_work_key
    capability: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - title
    - author
    produces:
    - work_key
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        title: title
        author: author
      out:
        work_key: work_key
  - cc_code: book_library_mgmt::CC_RESOLVE_WORK_V0
    step: '2'
    step_name: resolve_work_claim
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: RESOLVE
    store: WORK_IDENTITY_REGISTRY
    consumes:
    - key_or_address
    produces:
    - target_ref
    - result_status
    routing:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key_or_address: key_or_address
      out:
        target_ref: target_ref
        result_status: result_status
  - cc_code: book_library_mgmt::CC_RESOLVE_WORK_V0
    step: '3'
    step_name: read_work_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: READ
    store: WORKS
    consumes:
    - key
    produces:
    - work_record
    - result_status
    routing:
      SUCCESS: exit
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
      out:
        work_record: work_record
        result_status: result_status
  - cc_code: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    step: '1'
    step_name: set_record_state
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: UPDATE_WHERE
    store: BOOKS
    consumes:
    - filter
    - updates
    produces:
    - matched_keys
    - updated_count
    - result_status
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        filter: filter
        updates: updates
      out:
        matched_keys: matched_keys
        updated_count: updated_count
        result_status: result_status
  - cc_code: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    step: '1'
    step_name: set_record_state
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: UPDATE_WHERE
    store: PHYSICAL_COPIES
    consumes:
    - filter
    - updates
    produces:
    - matched_keys
    - updated_count
    - result_status
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        filter: filter
        updates: updates
      out:
        matched_keys: matched_keys
        updated_count: updated_count
        result_status: result_status
  - cc_code: book_library_mgmt::CC_SEARCH_CATALOG_V0
    step: '1'
    step_name: select_book_records
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: SELECT
    store: BOOKS
    consumes: null
    produces:
    - records
    - result_status
    routing:
      SUCCESS: continue
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in: {}
      out:
        records: records
        result_status: result_status
  - cc_code: book_library_mgmt::CC_SEARCH_CATALOG_V0
    step: '2'
    step_name: select_matching_books
    capability: capability_transforms::CT_PURE_FILTER_RECORDS_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - source
    - filter
    produces:
    - matching_books
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        source: source
        filter: filter
      out:
        matching_books: matching_books
  - cc_code: book_library_mgmt::CC_SEARCH_CATALOG_V0
    step: '3'
    step_name: group_editions_by_work
    capability: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - source
    - attribute
    produces:
    - matching_works
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        source: source
        attribute: attribute
      out:
        matching_works: matching_works
  - cc_code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: '1'
    step_name: read_book_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: READ
    store: BOOKS
    consumes:
    - key
    produces:
    - book_record
    - result_status
    routing:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
      out:
        book_record: book_record
        result_status: result_status
  - cc_code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: '2'
    step_name: form_updated_identity_key
    capability: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - title
    - author
    - publication_year
    produces:
    - updated_identity_key
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        title: title
        author: author
        publication_year: publication_year
      out:
        updated_identity_key: updated_identity_key
  - cc_code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: '3'
    step_name: compare_identity
    capability: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - left
    - right
    produces:
    - identity_unchanged
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        left: left
        right: right
      out:
        identity_unchanged: identity_unchanged
  - cc_code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: '4'
    step_name: require_identity_unchanged
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - parameters
    - rules
    produces:
    - valid
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: parameters
        rules: rules
      out:
        valid: valid
  - cc_code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: '5'
    step_name: assemble_updated_record
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - fields
    produces:
    - updated_record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: fields
      out:
        updated_record: updated_record
  - cc_code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: '6'
    step_name: check_corrected_record
    capability: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - record
    - schema
    produces:
    - violations
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        record: record
        schema: schema
      out:
        violations: violations
  - cc_code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: '7'
    step_name: refuse_incomplete_correction
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - parameters
    - rules
    produces:
    - valid
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: parameters
        rules: rules
      out:
        valid: valid
  - cc_code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: '8'
    step_name: write_updated_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: WRITE
    store: BOOKS
    consumes:
    - key
    - value
    produces:
    - result_status
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
        value: value
      out:
        result_status: result_status
  - cc_code: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    step: '1'
    step_name: validate_book_fields
    capability: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - record
    - schema
    produces:
    - violations
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        record: record
        schema: schema
      out:
        violations: violations
  - cc_code: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    step: '2'
    step_name: validate_work_fields
    capability: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - record
    - schema
    produces:
    - violations
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        record: record
        schema: schema
      out:
        violations: violations
  - cc_code: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    step: '3'
    step_name: require_submission_complete
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - parameters
    - rules
    produces:
    - valid
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: parameters
        rules: rules
      out:
        valid: valid
  step_bindings:
  - owner: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    step: append_operation
    direction: INPUT
    field: record
    bound_to: inputs.record
  - owner: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    step: append_operation
    direction: INPUT
    field: stream_id
    bound_to:
      literal: CATALOG_OPERATIONS
  - owner: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    step: append_operation
    direction: INPUT
    field: actor_id
    bound_to: inputs.staff_id
  - owner: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    step: append_operation
    direction: OUTPUT
    field: record_id
    bound_to: capability_result.record_id
  - owner: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    step: append_operation
    direction: OUTPUT
    field: sequence_number
    bound_to: capability_result.sequence_number
  - owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: read_book_record
    direction: INPUT
    field: key
    bound_to: inputs.identity_key
  - owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: read_book_record
    direction: OUTPUT
    field: value
    bound_to: capability_result.value
  - owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: read_book_record
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: read_book_record
    direction: OUTPUT
    field: book_record
    bound_to: capability_result.value
  - owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: form_work_key
    direction: INPUT
    field: title
    bound_to: results.read_book_record.value.title
  - owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: form_work_key
    direction: INPUT
    field: author
    bound_to: results.read_book_record.value.author
  - owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: form_work_key
    direction: OUTPUT
    field: work_key
    bound_to: capability_result.work_key
  - owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: read_work_record
    direction: INPUT
    field: key
    bound_to: results.form_work_key.work_key
  - owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: read_work_record
    direction: OUTPUT
    field: work_record
    bound_to: capability_result.value
  - owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: select_copy_records
    direction: OUTPUT
    field: records
    bound_to: capability_result.records
  - owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: select_copy_records
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: select_copies_of_book
    direction: INPUT
    field: source
    bound_to: results.select_copy_records.records
  - owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: select_copies_of_book
    direction: INPUT
    field: filter
    bound_to: inputs.copy_criteria
  - owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: select_copies_of_book
    direction: OUTPUT
    field: copies_held
    bound_to: capability_result.extracted
  - owner: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    step: form_identity_key
    direction: INPUT
    field: title
    bound_to: inputs.title
  - owner: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    step: form_identity_key
    direction: INPUT
    field: author
    bound_to: inputs.author
  - owner: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    step: form_identity_key
    direction: INPUT
    field: publication_year
    bound_to: inputs.publication_year
  - owner: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    step: form_identity_key
    direction: OUTPUT
    field: identity_key
    bound_to: capability_result.identity_key
  - owner: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    step: claim_identity
    direction: INPUT
    field: key
    bound_to: results.form_identity_key.identity_key
  - owner: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    step: claim_identity
    direction: INPUT
    field: target_cs
    bound_to:
      literal: CS_MUTABLE_JSON_V0
  - owner: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    step: claim_identity
    direction: INPUT
    field: target_ref
    bound_to:
      literal: BOOKS
  - owner: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    step: claim_identity
    direction: OUTPUT
    field: address
    bound_to: capability_result.address
  - owner: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    step: claim_identity
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    step: claim_barcode
    direction: INPUT
    field: key
    bound_to: inputs.barcode
  - owner: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    step: claim_barcode
    direction: INPUT
    field: target_cs
    bound_to:
      literal: CS_MUTABLE_JSON_V0
  - owner: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    step: claim_barcode
    direction: INPUT
    field: target_ref
    bound_to:
      literal: PHYSICAL_COPIES
  - owner: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    step: claim_barcode
    direction: OUTPUT
    field: address
    bound_to: capability_result.address
  - owner: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    step: claim_barcode
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: form_work_key
    direction: INPUT
    field: title
    bound_to: inputs.title
  - owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: form_work_key
    direction: INPUT
    field: author
    bound_to: inputs.author
  - owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: form_work_key
    direction: OUTPUT
    field: work_key
    bound_to: capability_result.work_key
  - owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: claim_work
    direction: INPUT
    field: key
    bound_to: results.form_work_key.work_key
  - owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: claim_work
    direction: INPUT
    field: target_cs
    bound_to:
      literal: CS_MUTABLE_JSON_V0
  - owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: claim_work
    direction: INPUT
    field: target_ref
    bound_to:
      literal: WORKS
  - owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: claim_work
    direction: OUTPUT
    field: address
    bound_to: capability_result.address
  - owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: claim_work
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: assemble_work_record
    direction: INPUT
    field: fields
    bound_to: inputs.work_fields
  - owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: assemble_work_record
    direction: OUTPUT
    field: work_record
    bound_to: capability_result.record
  - owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: write_work_record
    direction: INPUT
    field: key
    bound_to: results.form_work_key.work_key
  - owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: write_work_record
    direction: INPUT
    field: value
    bound_to: results.assemble_work_record.work_record
  - owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: write_work_record
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    step: confirm_authorization
    direction: INPUT
    field: parameters
    bound_to: inputs.staff_credentials
  - owner: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    step: confirm_authorization
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: staff_id
        op: not_null
      - field: authorized
        op: eq
        value: true
  - owner: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    step: confirm_authorization
    direction: OUTPUT
    field: is_authorized
    bound_to: capability_result.valid
  - owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: validate_edition_fields
    direction: INPUT
    field: record
    bound_to: inputs.edition_fields
  - owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: validate_edition_fields
    direction: INPUT
    field: schema
    bound_to:
      literal:
        title:
          required: true
          type: string
        author:
          required: true
          type: string
        publication_year:
          required: true
          type: integer
        subject:
          required: true
          type: array
  - owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: validate_edition_fields
    direction: OUTPUT
    field: violations
    bound_to: capability_result.violations
  - owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: refuse_incomplete_record
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        violations: $.results.validate_edition_fields.violations
  - owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: refuse_incomplete_record
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: violations
        op: eq
        value: []
  - owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: refuse_incomplete_record
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
  - owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: assemble_edition_record
    direction: INPUT
    field: fields
    bound_to: inputs.edition_fields
  - owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: assemble_edition_record
    direction: OUTPUT
    field: edition_record
    bound_to: capability_result.record
  - owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: write_edition_record
    direction: INPUT
    field: key
    bound_to: inputs.identity_key
  - owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: write_edition_record
    direction: INPUT
    field: value
    bound_to: results.assemble_edition_record.edition_record
  - owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: write_edition_record
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: form_work_key
    direction: INPUT
    field: title
    bound_to: inputs.book_fields.title
  - owner: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: form_work_key
    direction: INPUT
    field: author
    bound_to: inputs.book_fields.author
  - owner: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: form_work_key
    direction: OUTPUT
    field: work_key
    bound_to: capability_result.work_key
  - owner: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: validate_book_fields
    direction: INPUT
    field: record
    bound_to: inputs.book_fields
  - owner: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: validate_book_fields
    direction: INPUT
    field: schema
    bound_to:
      literal:
        title:
          required: true
          type: string
        author:
          required: true
          type: string
        publication_year:
          required: true
          type: integer
        subject:
          required: true
          type: array
  - owner: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: validate_book_fields
    direction: OUTPUT
    field: violations
    bound_to: capability_result.violations
  - owner: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: refuse_incomplete_record
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        violations: $.results.validate_book_fields.violations
  - owner: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: refuse_incomplete_record
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: violations
        op: eq
        value: []
  - owner: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: refuse_incomplete_record
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
  - owner: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: assemble_book_record
    direction: INPUT
    field: fields
    bound_to:
      literal:
        identity_key: $.inputs.identity_key
        title: $.inputs.book_fields.title
        author: $.inputs.book_fields.author
        publication_year: $.inputs.book_fields.publication_year
        subject: $.inputs.book_fields.subject
        state: $.inputs.book_fields.state
        work_key: $.results.form_work_key.work_key
  - owner: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: assemble_book_record
    direction: OUTPUT
    field: book_record
    bound_to: capability_result.record
  - owner: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: write_book_record
    direction: INPUT
    field: key
    bound_to: inputs.identity_key
  - owner: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: write_book_record
    direction: INPUT
    field: value
    bound_to: results.assemble_book_record.book_record
  - owner: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: write_book_record
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    step: read_book_record
    direction: INPUT
    field: key
    bound_to: inputs.identity_key
  - owner: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    step: read_book_record
    direction: OUTPUT
    field: book_record
    bound_to: capability_result.value
  - owner: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    step: read_book_record
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    step: assemble_copy_record
    direction: INPUT
    field: fields
    bound_to:
      literal:
        identity_key: $.inputs.identity_key
        barcode: $.inputs.barcode
        state: REGISTERED
  - owner: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    step: assemble_copy_record
    direction: OUTPUT
    field: copy_record
    bound_to: capability_result.record
  - owner: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    step: write_copy_record
    direction: INPUT
    field: key
    bound_to: inputs.barcode
  - owner: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    step: write_copy_record
    direction: INPUT
    field: value
    bound_to: results.assemble_copy_record.copy_record
  - owner: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    step: write_copy_record
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
    step: set_record_state
    direction: INPUT
    field: filter
    bound_to:
      literal:
        identity_key: $.inputs.identity_key
  - owner: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
    step: set_record_state
    direction: INPUT
    field: updates
    bound_to:
      literal:
        state: REGISTERED
  - owner: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
    step: set_record_state
    direction: OUTPUT
    field: matched_keys
    bound_to: capability_result.matched_keys
  - owner: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
    step: set_record_state
    direction: OUTPUT
    field: updated_count
    bound_to: capability_result.updated_count
  - owner: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
    step: set_record_state
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
    step: set_record_state
    direction: INPUT
    field: filter
    bound_to:
      literal:
        barcode: $.inputs.barcode
  - owner: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
    step: set_record_state
    direction: INPUT
    field: updates
    bound_to:
      literal:
        state: REGISTERED
  - owner: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
    step: set_record_state
    direction: OUTPUT
    field: matched_keys
    bound_to: capability_result.matched_keys
  - owner: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
    step: set_record_state
    direction: OUTPUT
    field: updated_count
    bound_to: capability_result.updated_count
  - owner: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
    step: set_record_state
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
    step: resolve_identity
    direction: INPUT
    field: key_or_address
    bound_to: inputs.identity_key
  - owner: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
    step: resolve_identity
    direction: OUTPUT
    field: target_ref
    bound_to: capability_result.target_ref
  - owner: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
    step: resolve_identity
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: book_library_mgmt::CC_RESOLVE_WORK_V0
    step: form_work_key
    direction: INPUT
    field: title
    bound_to: inputs.title
  - owner: book_library_mgmt::CC_RESOLVE_WORK_V0
    step: form_work_key
    direction: INPUT
    field: author
    bound_to: inputs.author
  - owner: book_library_mgmt::CC_RESOLVE_WORK_V0
    step: form_work_key
    direction: OUTPUT
    field: work_key
    bound_to: capability_result.work_key
  - owner: book_library_mgmt::CC_RESOLVE_WORK_V0
    step: resolve_work_claim
    direction: INPUT
    field: key_or_address
    bound_to: results.form_work_key.work_key
  - owner: book_library_mgmt::CC_RESOLVE_WORK_V0
    step: resolve_work_claim
    direction: OUTPUT
    field: target_ref
    bound_to: capability_result.target_ref
  - owner: book_library_mgmt::CC_RESOLVE_WORK_V0
    step: resolve_work_claim
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: book_library_mgmt::CC_RESOLVE_WORK_V0
    step: read_work_record
    direction: INPUT
    field: key
    bound_to: results.form_work_key.work_key
  - owner: book_library_mgmt::CC_RESOLVE_WORK_V0
    step: read_work_record
    direction: OUTPUT
    field: work_record
    bound_to: capability_result.value
  - owner: book_library_mgmt::CC_RESOLVE_WORK_V0
    step: read_work_record
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    step: set_record_state
    direction: INPUT
    field: filter
    bound_to:
      literal:
        identity_key: $.inputs.identity_key
  - owner: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    step: set_record_state
    direction: INPUT
    field: updates
    bound_to:
      literal:
        state: RETIRED
  - owner: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    step: set_record_state
    direction: OUTPUT
    field: matched_keys
    bound_to: capability_result.matched_keys
  - owner: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    step: set_record_state
    direction: OUTPUT
    field: updated_count
    bound_to: capability_result.updated_count
  - owner: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    step: set_record_state
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    step: set_record_state
    direction: INPUT
    field: filter
    bound_to:
      literal:
        barcode: $.inputs.barcode
  - owner: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    step: set_record_state
    direction: INPUT
    field: updates
    bound_to:
      literal:
        state: RETIRED
  - owner: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    step: set_record_state
    direction: OUTPUT
    field: matched_keys
    bound_to: capability_result.matched_keys
  - owner: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    step: set_record_state
    direction: OUTPUT
    field: updated_count
    bound_to: capability_result.updated_count
  - owner: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    step: set_record_state
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: book_library_mgmt::CC_SEARCH_CATALOG_V0
    step: select_book_records
    direction: OUTPUT
    field: records
    bound_to: capability_result.records
  - owner: book_library_mgmt::CC_SEARCH_CATALOG_V0
    step: select_book_records
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: book_library_mgmt::CC_SEARCH_CATALOG_V0
    step: select_matching_books
    direction: INPUT
    field: source
    bound_to: results.select_book_records.records
  - owner: book_library_mgmt::CC_SEARCH_CATALOG_V0
    step: select_matching_books
    direction: INPUT
    field: filter
    bound_to: inputs.search_criteria
  - owner: book_library_mgmt::CC_SEARCH_CATALOG_V0
    step: select_matching_books
    direction: OUTPUT
    field: matching_books
    bound_to: capability_result.extracted
  - owner: book_library_mgmt::CC_SEARCH_CATALOG_V0
    step: group_editions_by_work
    direction: INPUT
    field: source
    bound_to: results.select_matching_books.matching_books
  - owner: book_library_mgmt::CC_SEARCH_CATALOG_V0
    step: group_editions_by_work
    direction: INPUT
    field: attribute
    bound_to:
      literal: work_key
  - owner: book_library_mgmt::CC_SEARCH_CATALOG_V0
    step: group_editions_by_work
    direction: OUTPUT
    field: matching_works
    bound_to: capability_result.grouped
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: read_book_record
    direction: INPUT
    field: key
    bound_to: inputs.identity_key
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: read_book_record
    direction: OUTPUT
    field: book_record
    bound_to: capability_result.value
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: read_book_record
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: form_updated_identity_key
    direction: INPUT
    field: title
    bound_to: inputs.updated_fields.title
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: form_updated_identity_key
    direction: INPUT
    field: author
    bound_to: inputs.updated_fields.author
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: form_updated_identity_key
    direction: INPUT
    field: publication_year
    bound_to: inputs.updated_fields.publication_year
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: form_updated_identity_key
    direction: OUTPUT
    field: updated_identity_key
    bound_to: capability_result.identity_key
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: compare_identity
    direction: INPUT
    field: left
    bound_to: inputs.identity_key
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: compare_identity
    direction: INPUT
    field: right
    bound_to: results.form_updated_identity_key.updated_identity_key
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: compare_identity
    direction: OUTPUT
    field: identity_unchanged
    bound_to: capability_result.is_equal
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: require_identity_unchanged
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        identity_unchanged: $.results.compare_identity.identity_unchanged
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: require_identity_unchanged
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: identity_unchanged
        op: eq
        value: true
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: require_identity_unchanged
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: assemble_updated_record
    direction: INPUT
    field: fields
    bound_to:
      literal:
        identity_key: $.inputs.identity_key
        title: $.inputs.updated_fields.title
        author: $.inputs.updated_fields.author
        publication_year: $.inputs.updated_fields.publication_year
        subject: $.inputs.updated_fields.subject
        state: $.results.read_book_record.book_record.state
        work_key: $.results.read_book_record.book_record.work_key
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: assemble_updated_record
    direction: OUTPUT
    field: updated_record
    bound_to: capability_result.record
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: check_corrected_record
    direction: INPUT
    field: record
    bound_to: results.assemble_updated_record.updated_record
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: check_corrected_record
    direction: INPUT
    field: schema
    bound_to:
      literal:
        title:
          required: true
          type: string
        author:
          required: true
          type: string
        publication_year:
          required: true
          type: integer
        subject:
          required: true
          type: array
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: check_corrected_record
    direction: OUTPUT
    field: violations
    bound_to: capability_result.violations
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: refuse_incomplete_correction
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        violations: $.results.check_corrected_record.violations
        subject: $.results.assemble_updated_record.updated_record.subject
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: refuse_incomplete_correction
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: violations
        op: eq
        value: []
      - field: subject
        op: neq
        value: []
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: refuse_incomplete_correction
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: write_updated_record
    direction: INPUT
    field: key
    bound_to: inputs.identity_key
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: write_updated_record
    direction: INPUT
    field: value
    bound_to: results.assemble_updated_record.updated_record
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: write_updated_record
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    step: validate_book_fields
    direction: INPUT
    field: record
    bound_to: inputs.book_fields
  - owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    step: validate_book_fields
    direction: INPUT
    field: schema
    bound_to:
      literal:
        title:
          required: true
          type: string
        author:
          required: true
          type: string
        publication_year:
          required: true
          type: integer
        subject:
          required: true
          type: array
  - owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    step: validate_book_fields
    direction: OUTPUT
    field: violations
    bound_to: capability_result.violations
  - owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    step: validate_work_fields
    direction: INPUT
    field: record
    bound_to: inputs.work_fields
  - owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    step: validate_work_fields
    direction: INPUT
    field: schema
    bound_to:
      literal:
        title:
          required: true
          type: string
        author:
          required: true
          type: string
  - owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    step: validate_work_fields
    direction: OUTPUT
    field: violations
    bound_to: capability_result.violations
  - owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    step: require_submission_complete
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        barcode: $.inputs.barcode
        subject: $.inputs.book_fields.subject
        book_violations: $.results.validate_book_fields.violations
        work_violations: $.results.validate_work_fields.violations
  - owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    step: require_submission_complete
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: barcode
        op: neq
        value: ''
      - field: subject
        op: neq
        value: []
      - field: book_violations
        op: eq
        value: []
      - field: work_violations
        op: eq
        value: []
  - owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    step: require_submission_complete
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: INPUT
    field: book_fields
    bound_to:
      literal:
        title: $.payload.title
        author: $.payload.author
        publication_year: $.payload.publication_year
        subject: $.payload.subject
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: INPUT
    field: work_fields
    bound_to:
      literal:
        title: $.payload.title
        author: $.payload.author
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: CC_RESOLVE_WORK_V0
    direction: INPUT
    field: title
    bound_to: payload.title
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: CC_RESOLVE_WORK_V0
    direction: INPUT
    field: author
    bound_to: payload.author
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: CC_CLAIM_BOOK_IDENTITY_V0
    direction: INPUT
    field: title
    bound_to: payload.title
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: CC_CLAIM_BOOK_IDENTITY_V0
    direction: INPUT
    field: author
    bound_to: payload.author
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: CC_CLAIM_BOOK_IDENTITY_V0
    direction: INPUT
    field: publication_year
    bound_to: payload.publication_year
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: CC_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: identity_key
    bound_to: results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: CC_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: edition_fields
    bound_to:
      literal:
        identity_key: $.results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key
        title: $.payload.title
        author: $.payload.author
        publication_year: $.payload.publication_year
        subject: $.payload.subject
        state: REGISTERED
        work_key: $.results.CC_RESOLVE_WORK_V0.work_key
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: REGISTER_ADDITIONAL_EDITION
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: REGISTER_ADDITIONAL_EDITION
        staff_id: $.payload.staff_id
        subject: $.results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: INPUT
    field: work_fields
    bound_to:
      literal:
        title: $.payload.title
        author: $.payload.author
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: INPUT
    field: book_fields
    bound_to:
      literal:
        title: $.payload.title
        author: $.payload.author
        publication_year: $.payload.publication_year
        subject: $.payload.book_fields.subject
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: INPUT
    field: barcode
    bound_to: payload.barcode
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: CC_CLAIM_WORK_IDENTITY_V0
    direction: INPUT
    field: title
    bound_to: payload.title
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: CC_CLAIM_WORK_IDENTITY_V0
    direction: INPUT
    field: author
    bound_to: payload.author
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: CC_CLAIM_WORK_IDENTITY_V0
    direction: INPUT
    field: work_fields
    bound_to:
      literal:
        title: $.payload.title
        author: $.payload.author
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: CC_CLAIM_BOOK_IDENTITY_V0
    direction: INPUT
    field: title
    bound_to: payload.title
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: CC_CLAIM_BOOK_IDENTITY_V0
    direction: INPUT
    field: author
    bound_to: payload.author
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: CC_CLAIM_BOOK_IDENTITY_V0
    direction: INPUT
    field: publication_year
    bound_to: payload.publication_year
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: CC_CLAIM_COPY_BARCODE_V0
    direction: INPUT
    field: barcode
    bound_to: payload.barcode
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: CC_REGISTER_BOOK_V0
    direction: INPUT
    field: book_fields
    bound_to:
      literal:
        title: $.payload.title
        author: $.payload.author
        publication_year: $.payload.publication_year
        subject: $.payload.book_fields.subject
        state: REGISTERED
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: CC_REGISTER_BOOK_V0
    direction: INPUT
    field: identity_key
    bound_to: results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: CC_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: identity_key
    bound_to: results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: CC_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: barcode
    bound_to: payload.barcode
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: CC_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: copy_fields
    bound_to: payload.copy_fields
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: REGISTER_BOOK
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: REGISTER_BOOK
        staff_id: $.payload.staff_id
        subject: $.payload.title
  - owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    step: CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
  - owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    step: CC_CLAIM_COPY_BARCODE_V0
    direction: INPUT
    field: barcode
    bound_to: payload.barcode
  - owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    step: CC_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
  - owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    step: CC_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: barcode
    bound_to: payload.barcode
  - owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    step: CC_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: copy_fields
    bound_to: payload.copy_fields
  - owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    step: CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
  - owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    step: CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: REGISTER_PHYSICAL_COPY
  - owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    step: CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: REGISTER_PHYSICAL_COPY
        staff_id: $.payload.staff_id
        subject: $.payload.barcode
  - owner: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    step: CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
  - owner: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    step: CC_REINSTATE_BOOK_RECORD_V0
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
  - owner: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    step: CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
  - owner: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    step: CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: REINSTATE_BOOK_RECORD
  - owner: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    step: CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: REINSTATE_BOOK_RECORD
        staff_id: $.payload.staff_id
        subject: $.payload.identity_key
  - owner: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    step: CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
  - owner: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    step: CC_REINSTATE_PHYSICAL_COPY_V0
    direction: INPUT
    field: barcode
    bound_to: payload.barcode
  - owner: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    step: CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
  - owner: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    step: CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: REINSTATE_PHYSICAL_COPY
  - owner: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    step: CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: REINSTATE_PHYSICAL_COPY
        staff_id: $.payload.staff_id
        subject: $.payload.barcode
  - owner: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    step: CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
  - owner: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    step: CC_RETIRE_BOOK_RECORD_V0
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
  - owner: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    step: CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
  - owner: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    step: CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: RETIRE_BOOK_RECORD
  - owner: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    step: CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: RETIRE_BOOK_RECORD
        staff_id: $.payload.staff_id
        subject: $.payload.identity_key
  - owner: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    step: CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
  - owner: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    step: CC_RETIRE_PHYSICAL_COPY_V0
    direction: INPUT
    field: barcode
    bound_to: payload.barcode
  - owner: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    step: CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
  - owner: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    step: CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: RETIRE_PHYSICAL_COPY
  - owner: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    step: CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: RETIRE_PHYSICAL_COPY
        staff_id: $.payload.staff_id
        subject: $.payload.barcode
  - owner: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    step: CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
  - owner: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    step: CC_ASSEMBLE_BOOK_DETAILS_V0
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
  - owner: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    step: CC_ASSEMBLE_BOOK_DETAILS_V0
    direction: INPUT
    field: copy_criteria
    bound_to:
      literal:
        identity_key: $.payload.identity_key
  - owner: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    step: CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
  - owner: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    step: CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: RETRIEVE_BOOK_DETAILS
  - owner: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    step: CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: RETRIEVE_BOOK_DETAILS
        staff_id: $.payload.staff_id
        subject: $.payload.identity_key
  - owner: book_library_mgmt::WF_SEARCH_CATALOG_V0
    step: CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
  - owner: book_library_mgmt::WF_SEARCH_CATALOG_V0
    step: CC_SEARCH_CATALOG_V0
    direction: INPUT
    field: search_criteria
    bound_to: payload.search_criteria
  - owner: book_library_mgmt::WF_SEARCH_CATALOG_V0
    step: CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
  - owner: book_library_mgmt::WF_SEARCH_CATALOG_V0
    step: CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: SEARCH_CATALOG
  - owner: book_library_mgmt::WF_SEARCH_CATALOG_V0
    step: CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: SEARCH_CATALOG
        staff_id: $.payload.staff_id
        subject: $.payload.search_criteria
  - owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
  - owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: CC_RESOLVE_BOOK_IDENTITY_V0
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
  - owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
  - owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    direction: INPUT
    field: updated_fields
    bound_to: payload.updated_fields
  - owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: UPDATE_BIBLIOGRAPHIC_INFORMATION
  - owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: UPDATE_BIBLIOGRAPHIC_INFORMATION
        staff_id: $.payload.staff_id
        subject: $.payload.identity_key
  - owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
  interface_fields:
  - artifact: book_library_mgmt::AC_LIBRARY_STAFF_V0
    direction: ATTRIBUTE
    field: staff_id
    type: string
    required: 'YES'
    default: null
    meaning: staff id
  - artifact: book_library_mgmt::AC_LIBRARY_STAFF_V0
    direction: ATTRIBUTE
    field: authorized
    type: boolean
    required: 'NO'
    default: false
    meaning: authorized
  - artifact: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: record
    type: object
    required: 'YES'
    default: null
    meaning: record
  - artifact: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: null
    meaning: staff id
  - artifact: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: operation
    type: string
    required: 'YES'
    default: null
    meaning: operation
  - artifact: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: OUTPUT
    field: record_id
    type: string
    required: 'YES'
    default: null
    meaning: record id
  - artifact: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: OUTPUT
    field: sequence_number
    type: integer
    required: 'YES'
    default: null
    meaning: sequence number
  - artifact: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    direction: INPUT
    field: copy_criteria
    type: object
    required: 'YES'
    default: null
    meaning: copy criteria
  - artifact: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    direction: OUTPUT
    field: work_record
    type: object
    required: 'YES'
    default: null
    meaning: work record
  - artifact: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    direction: OUTPUT
    field: book_record
    type: object
    required: 'YES'
    default: null
    meaning: book record
  - artifact: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    direction: OUTPUT
    field: copies_held
    type: array
    required: 'YES'
    default: null
    meaning: copies held
  - artifact: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    direction: INPUT
    field: title
    type: string
    required: 'YES'
    default: null
    meaning: title
  - artifact: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    direction: INPUT
    field: author
    type: string
    required: 'YES'
    default: null
    meaning: author
  - artifact: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    direction: INPUT
    field: publication_year
    type: integer
    required: 'YES'
    default: null
    meaning: publication year
  - artifact: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    direction: OUTPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    direction: OUTPUT
    field: address
    type: string
    required: 'YES'
    default: null
    meaning: address
  - artifact: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    direction: INPUT
    field: barcode
    type: string
    required: 'YES'
    default: null
    meaning: barcode
  - artifact: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    direction: OUTPUT
    field: address
    type: string
    required: 'YES'
    default: null
    meaning: address
  - artifact: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    direction: INPUT
    field: title
    type: string
    required: 'YES'
    default: null
    meaning: title
  - artifact: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    direction: INPUT
    field: author
    type: string
    required: 'YES'
    default: null
    meaning: author
  - artifact: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    direction: INPUT
    field: work_fields
    type: object
    required: 'YES'
    default: null
    meaning: work fields
  - artifact: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    direction: OUTPUT
    field: work_key
    type: string
    required: 'YES'
    default: null
    meaning: work key
  - artifact: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: null
    meaning: staff credentials
  - artifact: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: OUTPUT
    field: is_authorized
    type: boolean
    required: 'YES'
    default: null
    meaning: is authorized
  - artifact: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: edition_fields
    type: object
    required: 'YES'
    default: null
    meaning: edition fields
  - artifact: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    direction: OUTPUT
    field: edition_record
    type: object
    required: 'YES'
    default: null
    meaning: edition record
  - artifact: book_library_mgmt::CC_REGISTER_BOOK_V0
    direction: INPUT
    field: book_fields
    type: object
    required: 'YES'
    default: null
    meaning: book fields
  - artifact: book_library_mgmt::CC_REGISTER_BOOK_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: book_library_mgmt::CC_REGISTER_BOOK_V0
    direction: OUTPUT
    field: book_record
    type: object
    required: 'YES'
    default: null
    meaning: book record
  - artifact: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: barcode
    type: string
    required: 'YES'
    default: null
    meaning: barcode
  - artifact: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: copy_fields
    type: object
    required: 'YES'
    default: null
    meaning: copy fields
  - artifact: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    direction: OUTPUT
    field: book_record
    type: object
    required: 'YES'
    default: null
    meaning: book record
  - artifact: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
    direction: OUTPUT
    field: updated_count
    type: integer
    required: 'YES'
    default: null
    meaning: updated count
  - artifact: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
    direction: INPUT
    field: barcode
    type: string
    required: 'YES'
    default: null
    meaning: barcode
  - artifact: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
    direction: OUTPUT
    field: updated_count
    type: integer
    required: 'YES'
    default: null
    meaning: updated count
  - artifact: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
    direction: OUTPUT
    field: target_ref
    type: string
    required: 'YES'
    default: null
    meaning: target ref
  - artifact: book_library_mgmt::CC_RESOLVE_WORK_V0
    direction: INPUT
    field: title
    type: string
    required: 'YES'
    default: null
    meaning: title
  - artifact: book_library_mgmt::CC_RESOLVE_WORK_V0
    direction: INPUT
    field: author
    type: string
    required: 'YES'
    default: null
    meaning: author
  - artifact: book_library_mgmt::CC_RESOLVE_WORK_V0
    direction: OUTPUT
    field: work_key
    type: string
    required: 'YES'
    default: null
    meaning: work key
  - artifact: book_library_mgmt::CC_RESOLVE_WORK_V0
    direction: OUTPUT
    field: work_record
    type: object
    required: 'NO'
    default: null
    meaning: work record
  - artifact: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    direction: OUTPUT
    field: updated_count
    type: integer
    required: 'YES'
    default: null
    meaning: updated count
  - artifact: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    direction: INPUT
    field: barcode
    type: string
    required: 'YES'
    default: null
    meaning: barcode
  - artifact: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    direction: OUTPUT
    field: updated_count
    type: integer
    required: 'YES'
    default: null
    meaning: updated count
  - artifact: book_library_mgmt::CC_SEARCH_CATALOG_V0
    direction: INPUT
    field: search_criteria
    type: object
    required: 'YES'
    default: null
    meaning: search criteria
  - artifact: book_library_mgmt::CC_SEARCH_CATALOG_V0
    direction: OUTPUT
    field: matching_works
    type: array
    required: 'YES'
    default: null
    meaning: matching works
  - artifact: book_library_mgmt::CC_SEARCH_CATALOG_V0
    direction: OUTPUT
    field: matching_books
    type: array
    required: 'YES'
    default: null
    meaning: matching books
  - artifact: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    direction: INPUT
    field: updated_fields
    type: object
    required: 'YES'
    default: null
    meaning: updated fields
  - artifact: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    direction: OUTPUT
    field: book_record
    type: object
    required: 'YES'
    default: null
    meaning: book record
  - artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: INPUT
    field: work_fields
    type: object
    required: 'YES'
    default: null
    meaning: work fields
  - artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: INPUT
    field: book_fields
    type: object
    required: 'YES'
    default: null
    meaning: book fields
  - artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: INPUT
    field: barcode
    type: string
    required: 'NO'
    default: null
    meaning: barcode
  - artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: OUTPUT
    field: valid
    type: boolean
    required: 'YES'
    default: null
    meaning: valid
  - artifact: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    direction: INPUT
    field: title
    type: string
    required: 'YES'
    default: null
    meaning: title
  - artifact: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    direction: INPUT
    field: author
    type: string
    required: 'YES'
    default: null
    meaning: author
  - artifact: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    direction: INPUT
    field: publication_year
    type: integer
    required: 'YES'
    default: null
    meaning: publication year
  - artifact: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    direction: OUTPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    direction: INPUT
    field: title
    type: string
    required: 'YES'
    default: null
    meaning: title
  - artifact: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    direction: INPUT
    field: author
    type: string
    required: 'YES'
    default: null
    meaning: author
  - artifact: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    direction: OUTPUT
    field: work_key
    type: string
    required: 'YES'
    default: null
    meaning: work key
  - artifact: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
    direction: INPUT
    field: source
    type: array
    required: 'YES'
    default: null
    meaning: source
  - artifact: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
    direction: INPUT
    field: attribute
    type: string
    required: 'YES'
    default: null
    meaning: attribute
  - artifact: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
    direction: OUTPUT
    field: grouped
    type: array
    required: 'YES'
    default: null
    meaning: grouped
  - artifact: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
    direction: INPUT
    field: source
    type: array
    required: 'YES'
    default: null
    meaning: source
  - artifact: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
    direction: INPUT
    field: filter
    type: object
    required: 'YES'
    default: null
    meaning: filter
  - artifact: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
    direction: OUTPUT
    field: extracted
    type: array
    required: 'YES'
    default: null
    meaning: extracted
  - artifact: book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
    direction: OUTPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
    direction: OUTPUT
    field: staff_id
    type: string
    required: 'YES'
    default: null
    meaning: staff id
  - artifact: book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: When the moment occurred
    format: date-time
  - artifact: book_library_mgmt::EV_BOOK_REGISTERED_V0
    direction: OUTPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: book_library_mgmt::EV_BOOK_REGISTERED_V0
    direction: OUTPUT
    field: title
    type: string
    required: 'YES'
    default: null
    meaning: title
  - artifact: book_library_mgmt::EV_BOOK_REGISTERED_V0
    direction: OUTPUT
    field: author
    type: string
    required: 'YES'
    default: null
    meaning: author
  - artifact: book_library_mgmt::EV_BOOK_REGISTERED_V0
    direction: OUTPUT
    field: publication_year
    type: integer
    required: 'YES'
    default: null
    meaning: publication year
  - artifact: book_library_mgmt::EV_BOOK_REGISTERED_V0
    direction: OUTPUT
    field: barcode
    type: string
    required: 'YES'
    default: null
    meaning: barcode
  - artifact: book_library_mgmt::EV_BOOK_REGISTERED_V0
    direction: OUTPUT
    field: staff_id
    type: string
    required: 'YES'
    default: null
    meaning: staff id
  - artifact: book_library_mgmt::EV_BOOK_REGISTERED_V0
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: When the moment occurred
    format: date-time
  - artifact: book_library_mgmt::EV_BOOK_RETIRED_V0
    direction: OUTPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: book_library_mgmt::EV_BOOK_RETIRED_V0
    direction: OUTPUT
    field: staff_id
    type: string
    required: 'YES'
    default: null
    meaning: staff id
  - artifact: book_library_mgmt::EV_BOOK_RETIRED_V0
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: When the moment occurred
    format: date-time
  - artifact: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
    direction: OUTPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
    direction: OUTPUT
    field: barcode
    type: string
    required: 'YES'
    default: null
    meaning: barcode
  - artifact: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
    direction: OUTPUT
    field: staff_id
    type: string
    required: 'YES'
    default: null
    meaning: staff id
  - artifact: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: When the moment occurred
    format: date-time
  - artifact: book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
    direction: OUTPUT
    field: barcode
    type: string
    required: 'YES'
    default: null
    meaning: barcode
  - artifact: book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
    direction: OUTPUT
    field: staff_id
    type: string
    required: 'YES'
    default: null
    meaning: staff id
  - artifact: book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: When the moment occurred
    format: date-time
  - artifact: book_library_mgmt::EV_WORK_REGISTERED_V0
    direction: OUTPUT
    field: work_key
    type: string
    required: 'YES'
    default: null
    meaning: work key
  - artifact: book_library_mgmt::EV_WORK_REGISTERED_V0
    direction: OUTPUT
    field: title
    type: string
    required: 'YES'
    default: null
    meaning: title
  - artifact: book_library_mgmt::EV_WORK_REGISTERED_V0
    direction: OUTPUT
    field: author
    type: string
    required: 'YES'
    default: null
    meaning: author
  - artifact: book_library_mgmt::EV_WORK_REGISTERED_V0
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: When the moment occurred
    format: date-time
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: null
    meaning: staff credentials
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: null
    meaning: staff id
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: title
    type: string
    required: 'YES'
    default: null
    meaning: title
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: author
    type: string
    required: 'YES'
    default: null
    meaning: author
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: publication_year
    type: integer
    required: 'YES'
    default: null
    meaning: publication year
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: subject
    type: array
    required: 'YES'
    default: null
    meaning: subject
  - artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: null
    meaning: staff credentials
  - artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
    direction: INPUT
    field: title
    type: string
    required: 'YES'
    default: null
    meaning: title
  - artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
    direction: INPUT
    field: author
    type: string
    required: 'YES'
    default: null
    meaning: author
  - artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
    direction: INPUT
    field: publication_year
    type: integer
    required: 'YES'
    default: null
    meaning: publication year
  - artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
    direction: INPUT
    field: book_fields
    type: object
    required: 'YES'
    default: null
    meaning: book fields
  - artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
    direction: INPUT
    field: barcode
    type: string
    required: 'YES'
    default: null
    meaning: barcode
  - artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
    direction: INPUT
    field: copy_fields
    type: object
    required: 'YES'
    default: null
    meaning: copy fields
  - artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: null
    meaning: staff id
  - artifact: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: null
    meaning: staff credentials
  - artifact: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: barcode
    type: string
    required: 'YES'
    default: null
    meaning: barcode
  - artifact: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: copy_fields
    type: object
    required: 'YES'
    default: null
    meaning: copy fields
  - artifact: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: null
    meaning: staff id
  - artifact: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: null
    meaning: staff credentials
  - artifact: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: null
    meaning: staff id
  - artifact: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: null
    meaning: staff credentials
  - artifact: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
    direction: INPUT
    field: barcode
    type: string
    required: 'YES'
    default: null
    meaning: barcode
  - artifact: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: null
    meaning: staff id
  - artifact: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: null
    meaning: staff credentials
  - artifact: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: null
    meaning: staff id
  - artifact: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: null
    meaning: staff credentials
  - artifact: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
    direction: INPUT
    field: barcode
    type: string
    required: 'YES'
    default: null
    meaning: barcode
  - artifact: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: null
    meaning: staff id
  - artifact: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: null
    meaning: staff credentials
  - artifact: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: null
    meaning: staff id
  - artifact: book_library_mgmt::IN_SEARCH_CATALOG_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: null
    meaning: staff credentials
  - artifact: book_library_mgmt::IN_SEARCH_CATALOG_V0
    direction: INPUT
    field: search_criteria
    type: object
    required: 'YES'
    default: null
    meaning: search criteria
  - artifact: book_library_mgmt::IN_SEARCH_CATALOG_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: null
    meaning: staff id
  - artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: null
    meaning: staff credentials
  - artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: null
    meaning: staff id
  - artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: identity key
  - artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    direction: INPUT
    field: updated_fields
    type: object
    required: 'YES'
    default: null
    meaning: updated fields
  implementation_bindings:
  - ct_code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    callable: execute
    operation: PURE_FORM_BOOK_IDENTITY_KEY
    kind: atom
    purity: ct_pure
    refusal: never
  - ct_code: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    callable: execute
    operation: PURE_FORM_WORK_IDENTITY_KEY
    kind: atom
    purity: ct_pure
    refusal: never
  - ct_code: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
    callable: execute
    operation: PURE_GROUP_RECORDS
    kind: atom
    purity: ct_pure
    refusal: never
  - ct_code: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
    callable: execute
    operation: PURE_SELECT_RECORDS
    kind: atom
    purity: ct_pure
    refusal: never
  vocabulary_extensions: []
  runtime_policies:
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    key: structure
    value: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    capability: capability_side_effects::CS_REGISTRY_V0
    key: structure
    value: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    key: structure
    value: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  artifact_properties:
  - artifact: book_library_mgmt::AC_LIBRARY_STAFF_V0
    property: type
    value: ENDUSER
  - artifact: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    property: layer
    value: DOMAINS
  - artifact: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    property: actor_context
    value: book_library_mgmt::AC_LIBRARY_STAFF_V0
  - artifact: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    property: emit.EXIT_COMPLETED
    value:
    - book_library_mgmt::EV_BOOK_REGISTERED_V0
  - artifact: book_library_mgmt::WF_REGISTER_BOOK_V0
    property: actor_context
    value: book_library_mgmt::AC_LIBRARY_STAFF_V0
  - artifact: book_library_mgmt::WF_REGISTER_BOOK_V0
    property: emit.EXIT_COMPLETED
    value:
    - book_library_mgmt::EV_WORK_REGISTERED_V0
    - book_library_mgmt::EV_BOOK_REGISTERED_V0
    - book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
  - artifact: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    property: actor_context
    value: book_library_mgmt::AC_LIBRARY_STAFF_V0
  - artifact: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    property: emit.EXIT_COMPLETED
    value:
    - book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
  - artifact: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    property: actor_context
    value: book_library_mgmt::AC_LIBRARY_STAFF_V0
  - artifact: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    property: actor_context
    value: book_library_mgmt::AC_LIBRARY_STAFF_V0
  - artifact: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    property: actor_context
    value: book_library_mgmt::AC_LIBRARY_STAFF_V0
  - artifact: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    property: emit.EXIT_COMPLETED
    value:
    - book_library_mgmt::EV_BOOK_RETIRED_V0
  - artifact: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    property: actor_context
    value: book_library_mgmt::AC_LIBRARY_STAFF_V0
  - artifact: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    property: emit.EXIT_COMPLETED
    value:
    - book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
  - artifact: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    property: actor_context
    value: book_library_mgmt::AC_LIBRARY_STAFF_V0
  - artifact: book_library_mgmt::WF_SEARCH_CATALOG_V0
    property: actor_context
    value: book_library_mgmt::AC_LIBRARY_STAFF_V0
  - artifact: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    property: actor_context
    value: book_library_mgmt::AC_LIBRARY_STAFF_V0
  - artifact: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    property: emit.EXIT_COMPLETED
    value:
    - book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
  structure_stores:
  - store_name: WORKS
    storage_type: CS_MUTABLE_JSON_V0
    proposed_path: book_library_mgmt/catalog/works.json
    used_by: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0, book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0,
      book_library_mgmt::CC_RESOLVE_WORK_V0
    structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  - store_name: WORK_IDENTITY_REGISTRY
    storage_type: CS_REGISTRY_V0
    proposed_path: book_library_mgmt/catalog/work_identity_registry.jsonl
    used_by: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0, book_library_mgmt::CC_RESOLVE_WORK_V0
    structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  - store_name: BOOKS
    storage_type: CS_MUTABLE_JSON_V0
    proposed_path: book_library_mgmt/catalog/books.json
    used_by: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0, book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0,
      book_library_mgmt::CC_REGISTER_BOOK_V0, book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0, book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0,
      book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0, book_library_mgmt::CC_SEARCH_CATALOG_V0, book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  - store_name: PHYSICAL_COPIES
    storage_type: CS_MUTABLE_JSON_V0
    proposed_path: book_library_mgmt/catalog/physical_copies.json
    used_by: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0, book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0,
      book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0, book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  - store_name: CATALOG_OPERATIONS
    storage_type: CS_APPENDONLY_JSONL_V0
    proposed_path: book_library_mgmt/catalog/catalog_operations.jsonl
    used_by: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  - store_name: BOOK_IDENTITY_REGISTRY
    storage_type: CS_REGISTRY_V0
    proposed_path: book_library_mgmt/catalog/book_identity_registry.jsonl
    used_by: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0, book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
    structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  - store_name: COPY_BARCODE_REGISTRY
    storage_type: CS_REGISTRY_V0
    proposed_path: book_library_mgmt/catalog/copy_barcode_registry.jsonl
    used_by: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  transport_bindings: []
  declared_reach: []
  molecule_steps: []
  molecule_step_bindings: []
  test_cases:
  - ct_code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    case: forms_normalized_key
    expected_outcome: SUCCESS
  - ct_code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    case: refuses_blank_title
    expected_outcome: VIOLATION
  - ct_code: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    case: forms_normalized_key
    expected_outcome: SUCCESS
  - ct_code: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
    case: groups_by_attribute
    expected_outcome: SUCCESS
  - ct_code: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
    case: selects_matching_records
    expected_outcome: SUCCESS
  test_case_values:
  - ct_code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    case: forms_normalized_key
    role: INPUT
    field: title
    value: THE ODYSSEY
  - ct_code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    case: forms_normalized_key
    role: INPUT
    field: author
    value: Homer
  - ct_code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    case: forms_normalized_key
    role: INPUT
    field: publication_year
    value: 1614
  - ct_code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    case: forms_normalized_key
    role: EXPECTED
    field: identity_key
    value: the odyssey|homer|1614
  - ct_code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    case: refuses_blank_title
    role: INPUT
    field: title
    value: ' '
  - ct_code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    case: refuses_blank_title
    role: INPUT
    field: author
    value: Homer
  - ct_code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    case: refuses_blank_title
    role: INPUT
    field: publication_year
    value: 1614
  - ct_code: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    case: forms_normalized_key
    role: INPUT
    field: title
    value: The Odyssey
  - ct_code: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    case: forms_normalized_key
    role: INPUT
    field: author
    value: Homer
  - ct_code: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    case: forms_normalized_key
    role: EXPECTED
    field: work_key
    value: the odyssey|homer
  - ct_code: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
    case: groups_by_attribute
    role: INPUT
    field: source
    value:
    - work: w1
      edition: 1
    - work: w2
      edition: 1
    - work: w1
      edition: 2
  - ct_code: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
    case: groups_by_attribute
    role: INPUT
    field: attribute
    value: work
  - ct_code: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
    case: groups_by_attribute
    role: EXPECTED
    field: grouped
    value:
    - key: w1
      records:
      - work: w1
        edition: 1
      - work: w1
        edition: 2
    - key: w2
      records:
      - work: w2
        edition: 1
  - ct_code: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
    case: selects_matching_records
    role: INPUT
    field: source
    value:
    - author: Homer
      title: Iliad
    - author: Virgil
      title: Aeneid
  - ct_code: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
    case: selects_matching_records
    role: INPUT
    field: filter
    value:
      author: Homer
  - ct_code: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
    case: selects_matching_records
    role: EXPECTED
    field: extracted
    value:
    - author: Homer
      title: Iliad
  generation_provenance: []
  artifact_summary:
  - action: NEW
    subdomain: catalog
    count: '51'
    artifacts: book_library_mgmt::AC_LIBRARY_STAFF_V0, book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0,
      book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0, book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0, book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0,
      book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0, book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0,
      book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0, book_library_mgmt::CC_REGISTER_BOOK_V0, book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0,
      book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0, book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0,
      book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0, book_library_mgmt::CC_RESOLVE_WORK_V0, book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0,
      book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0, book_library_mgmt::CC_SEARCH_CATALOG_V0, book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0,
      book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0, book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0,
      book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0, book_library_mgmt::CT_PURE_GROUP_RECORDS_V0,
      book_library_mgmt::CT_PURE_SELECT_RECORDS_V0, book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0,
      book_library_mgmt::EV_BOOK_REGISTERED_V0, book_library_mgmt::EV_BOOK_RETIRED_V0, book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0,
      book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0, book_library_mgmt::EV_WORK_REGISTERED_V0, book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0,
      book_library_mgmt::IN_REGISTER_BOOK_V0, book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0, book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0,
      book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0, book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0, book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0,
      book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0, book_library_mgmt::IN_SEARCH_CATALOG_V0, book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0,
      book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0, book_library_mgmt::RB_CATALOG_BINDINGS_V0, book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0,
      book_library_mgmt::WF_REGISTER_BOOK_V0, book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0, book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0,
      book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0, book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0, book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0,
      book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0, book_library_mgmt::WF_SEARCH_CATALOG_V0, book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
  refusal_discharge: []
  refusal_deferrals: []
  refusal_governance_discharge: []
  withdrawn_facts: null
```

The design of record of `book_library_mgmt`: every artifact its registry holds, stated in the design language.
Written by `python -m transformation.record` from the registry. Construction of this design and its
mandate reproduces the registry, and `construction_acceptance` asks whether it does. A change to
`book_library_mgmt` is a dossier designed against the composition.
