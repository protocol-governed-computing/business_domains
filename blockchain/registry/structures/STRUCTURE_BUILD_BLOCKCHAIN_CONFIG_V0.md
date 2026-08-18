# STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0

## Header (Mandatory)

- **Artifact Code:** STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0
- **Artifact Kind:** structure
- **Governed By:** CONSTITUTION_STRUCTURE_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Build-time STRUCTURE manifest (blockchain business-domain scope)

---

## Machine

```yaml
fqdn: blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0
artifact_kind: STRUCTURE
version: V0
governed_by: fb.structure::CONSTITUTION_STRUCTURE_V0
structure_scope: blockchain
reuse_visibility: business
core:
  summary: Build-time STRUCTURE manifest (blockchain business-domain scope)
  description: 'Compiles the blockchain domain''s own artifacts, resolving governance and platform capability
    references against the imported compiled governance surface. Emits only blockchain artifacts. Self-describing:
    declares its own source layer and namespace rule additively. Subdomains: identity, wallet.'
layer_definitions:
  BLOCKCHAIN:
    domain_subpath: registry
    registry_module: blockchain.registry
    implementation_namespace: blockchain.implementation.capability_transforms.atoms
    layer_category: domain
identity_rules:
- match: blockchain.registry
  namespace: blockchain
artifact_discovery:
  search_layers:
  - BLOCKCHAIN
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
    BLOCKCHAIN:
      layer: BLOCKCHAIN
      subpath: compiled/canonical
  bootstrap_search_roots:
  - layer: GOVERNANCE
    subpath: structure/structures
build_phases:
- phase: discover
  description: Discover blockchain artifacts via STRUCTURE
- phase: parse
  description: Parse artifacts into canonical machine form
- phase: normalize
  description: Resolve references (blockchain + imported governance surface)
- phase: validate
  description: Validate artifacts using compiler schema rules
- phase: assert
  description: Evaluate cross-artifact invariants
- phase: materialize
  description: Emit deterministic compiled artifacts (blockchain scope only)
  target: compiled/artifacts/
```
