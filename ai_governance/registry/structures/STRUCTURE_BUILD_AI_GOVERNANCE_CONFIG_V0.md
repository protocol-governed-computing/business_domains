# STRUCTURE_BUILD_AI_GOVERNANCE_CONFIG_V0

## Machine

```yaml
fqdn: ai_governance::STRUCTURE_BUILD_AI_GOVERNANCE_CONFIG_V0
artifact_kind: STRUCTURE
version: V0
governed_by: structure::CONSTITUTION_STRUCTURE_V0
authority: pgc.platform
concern: ai_governance
structure_scope: ai_governance
reuse_visibility: business
core:
  summary: Build-time STRUCTURE manifest (ai_governance business-domain scope)
  description: 'Compiles the ai_governance domain''s own artifacts, resolving governance and platform
    capability references against the imported compiled governance surface. Emits only ai_governance artifacts.
    Self-describing: declares its own source layer and namespace rule additively. Subdomains: agent_governance,
    ai_licensing.'
layer_definitions:
  AI_GOVERNANCE:
    domain_subpath: registry
    registry_module: ai_governance.registry
    implementation_namespace: ai_governance.implementation.capability_transforms.atoms
    layer_category: domain
identity_rules:
- match: ai_governance.registry
  namespace: ai_governance
artifact_discovery:
  search_layers:
  - AI_GOVERNANCE
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
  visualization_projection_path:
    layer: GOVERNANCE
    subpath: compiled/visualization
  layer_outputs:
    AI_GOVERNANCE:
      layer: AI_GOVERNANCE
      subpath: compiled/canonical
  bootstrap_search_roots:
  - layer: GOVERNANCE
    subpath: structure/structures
  conformance:
    layer: GOVERNANCE
    subpath: compiled/transform_conformance
build_phases:
- phase: discover
  description: Discover ai_governance artifacts via STRUCTURE
- phase: parse
  description: Parse artifacts into canonical machine form
- phase: normalize
  description: Resolve references (ai_governance + imported governance surface)
- phase: validate
  description: Validate artifacts using compiler schema rules
- phase: assert
  description: Evaluate cross-artifact invariants
- phase: materialize
  description: Emit deterministic compiled artifacts (ai_governance scope only)
  target: compiled/artifacts/
```

---

## Intent

Build-time STRUCTURE manifest (ai_governance business-domain scope)
