# causal_language_model — parked changes

The domain registers a model, places it in service with a system prompt and response rules, and
answers a user prompt under those rules, with every refusal recorded. It does so two ways: through a
scripted test model, and through Qwen3 8B hosted outside PGC and governed token by token. The
domain's [`README.md`](../README.md) and [`ARCHITECTURE.md`](../ARCHITECTURE.md) describe both.

The changes below are parked. None is scheduled, and none is cancelled. Each would take the next
dossier number in `cr_dossiers/` if taken up.

## The changes

| Function | Adds | Axis |
|---|---|---|
| registry | The full registry: describe, list, retire, reinstate | flexibility |
| disclosure | Review a finished model response before release | behavior |
| action | A model proposes an action. Only an authorized actor's authority lets it proceed. | behavior |
| substitution | Replace the model in service under unchanged behavior declarations. The identity change is evidenced. | flexibility |
| reporting | Evidence for an independent auditor | both |

## How each change runs

- Each change is designed, constructed, compiled, assembled and executed before the next begins.
  Each pins the composition the one before it produced. No change reworks a completed one.
- The scripted test model is permanent. It is a conformance workload, not scaffolding, and it
  produces the cases each change must refuse. Every other capability transform is a real
  implementation from the change that introduces it.
- **P3** maps each function's components to existing kinds. A gap is recorded there, in the change
  that meets it, not in an up-front survey.
- **P6** maps the change's conditions (authority closure, enforcement, evidence, worker neutrality)
  to existing invariants. A new invariant needs a demonstrated gap.
- A needed governance-surface change becomes its own dossier, complete at P6, per
  `THE_SHAPE_OF_A_CHANGE_V0.md` §5.
