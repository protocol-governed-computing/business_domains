# CR-1 "model_response" — requirements mapped to existing kinds

Every requirement in `cr_dossiers/cr_01_model_response/p0_business_problem_statement.md`, mapped to the
existing artifact kind that would carry it, with the closest precedent in the repo.

## Requirements that map cleanly

| Requirement | Kind | Precedent |
|---|---|---|
| Register a model. Same description and fingerprint mean the same model. | CS registry (`CS_REGISTRY_V0`) + pure CT identity key | book `CT_PURE_FORM_BOOK_IDENTITY_KEY_V0`, `CC_CLAIM_BOOK_IDENTITY_V0` |
| Refuse a model that cannot be built (width not divisible by heads) | pure CT validation with a declared refusal | `CC_VALIDATE_BOOK_SUBMISSION_V0` |
| Fingerprint recorded as the provider's claim | a field of the registration record | — |
| Place in service with sensitivity ceiling, response rules, system prompt. Withdraw. | CS mutable store (`CS_MUTABLE_JSON_V0`) + WF + CC | book retire/reinstate |
| Sensitivity classes public … restricted | VOCAB | — |
| Model staff, requester | AC, plus an authorization-check CC | `AC_LIBRARY_STAFF_V0`, `CC_CONFIRM_STAFF_AUTHORIZED_V0` |
| Acting for a customer is decided elsewhere | the same deferral the catalog made for staff authority | book P0 §3 |
| Four refusals before the model sees the request | TI admission + WF `admission.requires/forbids` + CC refusal routing to EXIT | every existing WF |
| The record: exactly what was read, rules in force, model response or reason | CS append-only (`CS_APPENDONLY_JSONL_V0`) + EV | `CC_APPEND_CATALOG_OPERATION_V0` |
| Record integrity, requester bound to the evidence | platform trace and signing | `INVARIANT_TRACE_AUTHORITY_BINDING_REQUIRED_V0`, `INVARIANT_CS_TRACEABLE_V0` |
| Test model, later a real one | CT `machine.implementation` sealed in the snapshot; stand-in module in `conformance_workloads` | the implementation-closure check |

Most of CR-1 is the catalog pattern with different nouns. That is expected and costs little.

## Where the concept lives: writing word by word

The model writes one word at a time. At each word:

1. **propose:** the model offers candidate next words. This part is not deterministic.
2. **select:** the response rules remove forbidden candidates, and one word is chosen under the declared
   freedom and seed. Given the same candidates, rules, and seed, this part is deterministic.

This repeats until the response ends, a rule leaves no permitted word, or the longest response is reached.

| Need | What exists | Fit |
|---|---|---|
| Repetition | Workflows must be acyclic (`CONSTITUTION_WORKFLOW_V0`: "Cycles are constitutional violations") | **Not at workflow level, and correctly so** |
| Bounded repetition | Molecule `loop` step: iterates over a collection with an accumulator (`SCHEMA_MOLECULE_V0`, `ct_executor._execute_loop`) | **Fits.** Iterate over the positions 1…longest response. The accumulator carries the text so far, the words blocked, and a done flag. The longest-response rule *is* the loop bound. |
| propose and select as two declared steps in each pass | A loop body is **one atom**: one `handler_ref` per iteration | **Gap** |
| Declaring where determinism ends | `ct_purity: ct_pure / ct_impure / ct_exec` exists in the CT schema | **Named but unexercised.** No CT in the repo is `ct_impure`. `INVARIANT_ATOM_OUTPUT_PURITY_V0` describes atoms as pure functions. |
| Refusal by rule or by length | CT `core.refusal`, CC `on_ct_result`, WF `next` → EXIT | Fits |
| Evidence that a forbidden word was offered and not written | accumulator → CT output → record | Fits |

## The go/no-go answer

**Without the gap closed**, one atom does both propose and select. The rules then live inside that
atom's code. Governance sees settings passed to a component and cannot tell selection from the model.
That is governed orchestration around a model, the modest outcome.

**With the gap closed**, each pass runs two declared atoms: a `ct_impure` proposer (the model) and a
`ct_pure` selector (the rules). The snapshot then shows exactly where determinism ends and where the
rules act. The stand-in and the real model swap only the proposer. That is the concept.

The gap is small, and it is generic: a loop body that is a sequence of steps instead of a single
atom. A second, smaller point needs settling alongside it: what `ct_impure` means to the compiler,
the runtime, and the purity invariant.

## Molecules and loops end to end

| Layer | Behavior |
|---|---|
| Repo | No molecule CT exists. All 13 CTs are atoms. Molecules and loops have never been exercised. |
| Schema | `SCHEMA_MOLECULE_V0` step kinds: `atom`, `molecule`, `loop` |
| Compiler (`s5_construct.py`) | A `loop` step names a **molecule** as its body and emits no `handler_ref`. A nested `molecule` step also emits none. |
| Runtime (`ct_executor.py`) | Every step, including each loop pass, runs through `_execute_handler_ref`, which requires a `handler_ref` |
| Result | Compile → run fails. Executing the compiler's loop shape raises `CTExecutionError: CT-IR step missing handler_ref`. Nested molecules fail the same way. |

The compiler already intends the loop body to be a molecule, which is a sequence of steps and exactly
what the concept needs. The runtime disagrees, and nothing exercised the path to notice. The gap is
therefore not a new construct. It is a declared construct whose realization is incomplete: the
runtime must execute a molecule, as a loop body or as a nested step, by running its own atom stream.

## Consequence for the sequence

- **One governance-surface dossier before CR-1's design:** `software_governance/dossiers/molecule_execution/`,
  P0–P6. It covers running a molecule as a loop body and as a nested step, and the meaning of
  `ct_impure`. Implementation: `ct_executor` (molecule execution), plus a compiler check that a loop
  body resolves to something the runtime can run. The schema already has the construct.
- **No new artifact kind, so no construction builder** (Stage C in the old plan does not arise).
  CR-1 uses only the existing families.
- CR-1 then proceeds P0–P8 on the existing kinds.
