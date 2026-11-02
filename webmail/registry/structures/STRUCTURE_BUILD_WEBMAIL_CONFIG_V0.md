# STRUCTURE_BUILD_WEBMAIL_CONFIG_V0

## Machine

```yaml
fqdn: webmail::STRUCTURE_BUILD_WEBMAIL_CONFIG_V0
artifact_kind: STRUCTURE
version: V0
governed_by: structure::CONSTITUTION_STRUCTURE_V0
authority: pgc.platform
concern: webmail
structure_scope: webmail
reuse_visibility: business
core:
  summary: Build-time STRUCTURE manifest (webmail business-domain scope)
  description: 'Compiles the webmail domain''s own artifacts, resolving governance and platform capability
    references against the imported compiled governance surface. Emits only webmail artifacts. Self-describing:
    declares its own source layer and namespace rule additively. Subdomains: mailbox.'
layer_definitions:
  WEBMAIL:
    domain_subpath: registry
    registry_module: webmail.registry
    implementation_namespace: webmail.implementation.capability_transforms.atoms
    layer_category: domain
identity_rules:
- match: webmail.registry
  namespace: webmail
artifact_discovery:
  search_layers:
  - WEBMAIL
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
  - TEST_DATA
output_configuration:
  root: snapshot
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
  layer_outputs:
    WEBMAIL:
      layer: WEBMAIL
      subpath: compiled/canonical
  bootstrap_search_roots:
  - layer: GOVERNANCE
    subpath: structure/structures
  conformance:
    layer: GOVERNANCE
    subpath: compiled/transform_conformance
build_phases:
- phase: discover
  description: Discover webmail artifacts via STRUCTURE
- phase: parse
  description: Parse artifacts into canonical machine form
- phase: normalize
  description: Resolve references (webmail + imported governance surface)
- phase: validate
  description: Validate artifacts using compiler schema rules
- phase: assert
  description: Evaluate cross-artifact invariants
- phase: materialize
  description: Emit deterministic compiled artifacts (webmail scope only)
  target: compiled/artifacts/
```

---

## Intent

Build-time STRUCTURE manifest (webmail business-domain scope)
