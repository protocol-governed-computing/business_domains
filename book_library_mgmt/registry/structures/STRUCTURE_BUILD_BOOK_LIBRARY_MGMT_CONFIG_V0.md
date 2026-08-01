# STRUCTURE_BUILD_BOOK_LIBRARY_MGMT_CONFIG_V0

**Artifact Type**: STRUCTURE
**Version**: V0
**Governed By**: fb.structure::CONSTITUTION_STRUCTURE_V0

---

## Purpose

Self-describing build manifest for the **AI governance business domain** (`book_library_mgmt::`) — an
independently-authored domain compiled **against** the already-compiled governance surface, then
composed into the assembled universe.

This artifact lives in the domain's own repo (`business_domains`), so the governance surface is
never edited to admit the domain — its identity and hash are unchanged. The compiler merges this
manifest's `layer_definitions` and `identity_rules` **additively**, for this build only, on top of
the immutable `STRUCTURE_DISCOVERY_V0` / `STRUCTURE_IDENTITY_V0`.

## Subdomains

The domain is one namespace (`book_library_mgmt`) partitioned into two subdomains, each carried by the
`subdomain:` declaration on its workflows and resolved by recursive discovery under `registry/`:

| Subdomain | Concern |
|---|---|
| `agent_governance` | Constitutional mediation of agent-proposed actions against license-tier authority |
| `ai_licensing` | License provisioning, cap enforcement, and reclamation of dormant licenses |

Neither subdomain references the other's artifacts. `agent_governance` consumes the license fact
feed read-only through its own STRUCTURE declaration, so either subdomain can be removed by
deleting its folder — no other artifact is touched.

---

## Machine

```yaml
fqdn: book_library_mgmt::STRUCTURE_BUILD_BOOK_LIBRARY_MGMT_CONFIG_V0
artifact_kind: STRUCTURE
version: V0
governed_by: fb.structure::CONSTITUTION_STRUCTURE_V0
structure_scope: book_library_mgmt
reuse_visibility: business
core:
  summary: Build-time STRUCTURE manifest (book library management business-domain scope)
  description: 'Compiles the book_library_mgmt domain''s own artifacts (WF/IN/CC/CT/EV/AC/RB/STRUCTURE),
    resolving governance and platform capability references against the imported compiled governance
    surface. Emits only book_library_mgmt artifacts. Self-describing: declares its own source layer and
    namespace rule additively.

    '
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
  - WF
  - IN
  - CC
  - CT
  - EV
  - AC
  - RB
  - STRUCTURE
  - VOCAB
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

## Version History

- **V0**: First AI governance business-domain build manifest. Self-describing; compiles
  `book_library_mgmt::` against the imported compiled governance surface; emits only `book_library_mgmt`
  artifacts. Governance surface unchanged.
