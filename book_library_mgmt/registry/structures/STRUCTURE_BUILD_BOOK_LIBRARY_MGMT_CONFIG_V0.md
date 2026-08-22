# STRUCTURE_BUILD_BOOK_LIBRARY_MGMT_CONFIG_V0

## 1. Intent

Build-time STRUCTURE manifest (book_library_mgmt business-domain scope)

---

## Machine

```yaml
fqdn: book_library_mgmt::STRUCTURE_BUILD_BOOK_LIBRARY_MGMT_CONFIG_V0
artifact_kind: STRUCTURE
version: V0
governed_by: structure::CONSTITUTION_STRUCTURE_V0
authority: pgc.platform
concern: book_library_mgmt
structure_scope: book_library_mgmt
reuse_visibility: business
core:
  summary: Build-time STRUCTURE manifest (book_library_mgmt business-domain scope)
  description: 'Compiles the book_library_mgmt domain''s own artifacts, resolving governance and platform
    capability references against the imported compiled governance surface. Emits only book_library_mgmt
    artifacts. Self-describing: declares its own source layer and namespace rule additively. Subdomains:
    catalog.'
layer_definitions:
  BOOK_LIBRARY_MGMT:
    domain_subpath: registry
    registry_module: book_library_mgmt.registry
    implementation_namespace: book_library_mgmt.implementation.capability_transforms.atoms
    layer_category: domain
identity_rules:
- match: book_library_mgmt.registry
  namespace: book_library_mgmt
artifact_discovery:
  search_layers:
  - BOOK_LIBRARY_MGMT
  import_surface:
    domain: platform
  artifact_types:
  - AC
  - IN
  - WF
  - CC
  - CT
  - RB
  - EV
  - VOCAB
  - STRUCTURE
  - TI
  - TE
output_configuration:
  artifacts:
    layer: PROTOCOL_BUILD_ROOT
    subpath: compiled/canonical
  vocabulary_projection_path:
    layer: GOVERNANCE
    subpath: compiled/vocabulary
  tokenized_projection_path:
    layer: GOVERNANCE
    subpath: compiled/tokenized
  evidence_projection_path:
    layer: GOVERNANCE
    subpath: compiled/evidence
  trust_attestation_path:
    layer: GOVERNANCE
    subpath: compiled/trust
  visualization_projection_path:
    layer: GOVERNANCE
    subpath: compiled/visualization
  layer_outputs:
    BOOK_LIBRARY_MGMT:
      layer: BOOK_LIBRARY_MGMT
      subpath: compiled/canonical
  bootstrap_search_roots:
  - layer: GOVERNANCE
    subpath: structure/structures
build_phases:
- phase: discover
  description: Discover book_library_mgmt artifacts via STRUCTURE
- phase: parse
  description: Parse artifacts into canonical machine form
- phase: normalize
  description: Resolve references (book_library_mgmt + imported governance surface)
- phase: validate
  description: Validate artifacts using compiler schema rules
- phase: assert
  description: Evaluate cross-artifact invariants
- phase: materialize
  description: Emit deterministic compiled artifacts (book_library_mgmt scope only)
  target: compiled/artifacts/
```
