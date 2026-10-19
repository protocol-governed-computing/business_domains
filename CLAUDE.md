## Response Style

Keep responses under ~400 output tokens. Prefer terse bullet summaries over prose narration. When a full document is needed, Write it to a file instead of printing it in chat.

## Document Authoring Rules

- Never include internal review notes, meta-scaffolding, work-order framing, cross-reference stubs, or 'Status:' metadata in deliverable docs or figures.
- Do not add dates to papers or appendices.
- An 'outline' means a clean reader-facing outline of the paper, not an execution plan.

# Business Domains (PGC) — Repository Rules

## What this repo is

The business domains a composition executes: `ai_governance`, `blockchain`, `book_library_mgmt` and
`causal_language_model`. Each domain is a compiled namespace (`<domain>::…`) with its own build
manifest. It is compiled **against** the already-compiled governance surface in
`software_governance`, and it changes nothing there.

A domain **declares**. It does not implement admission, routing, persistence or auditing: the
runtime does those, from the sealed snapshot. What a domain implements is its capability transforms,
and nothing else.

- **Org:** `protocol-governed-computing`. **Repo:** `business_domains`. **Package:** `pgc-domains`.
- **All development happens on the current `dev/N` branch** (the workspace's development cycle). The user
  runs every git command.

## Layout

```
<domain>/
  registry/<subdomain>/      the declared artifacts: workflows, intents, capability contracts,
                             transforms, events, actors, layers, runtime bindings, transport
  registry/structures/       STRUCTURE_BUILD_<DOMAIN>_CONFIG_V0 — the build manifest
  implementation/capability_transforms/atoms/   the transform implementations, one module each
  design/                    the design of record: P7 and P8, generated from the registry
  cr_dossiers/cr_NN_<subject>/   a change, P0 to P8, designed against the composition
  testbed/                   payloads and the domain's execution validation
  snapshot/                  compiled output — never edit it; recompile
```

`blockchain/client/` is a browser surface and its HTTP binding table. `causal_language_model/host/`
drives a hosted model from outside PGC. Neither is part of the composition.

## Capability transforms — the only code a domain owns

A transform is an artifact *and* a module. The artifact's `machine.implementation` names the module
by its full path, `<domain>.implementation.capability_transforms.atoms.<code_lower>`. A sealed
snapshot binds that path, so it never moves.

- **Signature:** `execute(inputs: dict, context=None) -> dict`, returning exactly the declared outputs.
- **Refusal:** raise `CTExecutionError` with a message naming the transform. The runtime turns it into
  the contract's declared refusal outcome. Raising is how a transform refuses, never how it controls
  flow.
- **No effects.** No I/O, no filesystem, no network, no global state. Every effect is a capability
  side effect the platform declares, bound by a runtime binding.
- **Deterministic** unless the artifact declares `ct_purity: ct_impure`. An impure atom is governed by
  `capability_transforms::CONSTITUTION_NONDETERMINISTIC_ATOMS_V0`: the runtime records every result,
  a replay substitutes the recorded one, and nothing routes on it before a deterministic step uses it.
- **A molecule declares no implementation.** Its steps are its specification, under
  `capability_transforms::CONSTITUTION_MOLECULES_V0`.
- **A new transform carries test vectors:** a `TEST_DATA_<CT>` artifact whose `target` names it and
  whose `cases` state what it is handed and must return. P7 refuses a new transform without cases,
  and the compile proves them. Transforms delivered before vectors existed report as unproven until
  their own change adds vectors.

## Imports

- Absolute imports only, no relative imports.
- An implementation may import the standard library, `runtime.ct_executor` (for `CTExecutionError`)
  and a declared optional dependency (`pycryptodome`, for blockchain's Keccak-256 only).
- No import of the compiler, the assembler, another domain, or a `pgs_*` package. Domains reach one
  another only through compiled identity.
- No `sys.path` manipulation, dynamic imports or filesystem discovery.

## Identity

- Every reference is a full name: `<domain>::<CODE>_V<n>`. No short names in declarations.
- Meaning decides identity. A change of meaning is the next unused version, which names its
  predecessor in `supersedes`. The predecessor is deleted and recorded in
  `.github/process/retired_identities.yaml`. One version of each artifact is live.
- An artifact published in a release is never edited in place.

## Changing a domain

Every change runs through the transformation lifecycle, P0 to P8, as a dossier in this domain's
`cr_dossiers/`, built on the domain's design of record in `design/`. The next change takes the next
number. Its pin, `baseline.json`, is the composition it was designed against. A completed dossier is
never re-pinned and never edited. Once it is built, the design of record is regenerated from the
registry (`write_baseline_designs.py`).

- **Design first:** problem statement, then the phases, each admissible before the next is written.
- **Validation criteria come from P0**, in the seed's own words, and are written while P7 is drafted.
- **Every domain whose dossiers change its acts has an execution validation** under `testbed/`. It
  dispatches the workflows against a fresh data root, with one criterion per acceptance criterion.
  The workspace regression runs every one.
- **Diagnose, then plan, then get approval** before a multi-file change.

## Build and run

```
protocol_compiler/compile_domain.sh business_domains/<domain>   # compile against the platform
snapshot_assembler/assemble.sh                                   # assemble the composition
.github/process/regression.sh --all                              # the full workspace check
```

The snapshot is sealed at build time, and the runtime executes exactly what it declares. Editing
`snapshot/` changes nothing: change the declaration and recompile.

Build in the workspace venv (`.venv`, Python 3.12). Do not install packages; a dependency needs a
declared need in `pyproject.toml`.
