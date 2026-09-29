# causal_language_model — change request sequence

Each change request is designed, constructed, compiled, assembled, and executed before the next one
begins. Each one pins the composition its predecessor produced. No change request reworks a
completed one. Each one adds a function that the earlier ones left adjacent.

The motivation lives in `causal_language_model.md`. It explains why the sequence exists. It does
not steer the sequence.

> **Where the sequence stands.** CR-1 is delivered and validated (27/27). The real model came next,
> as this sequence's note foresaw, and took the dossier name `cr_02_hosted_model`: Qwen3 8B, hosted
> outside PGC and governed token by token, capacity in tokens, numbers optionally grounded in what
> the model read. The CR-2 through CR-6 below are still parked, not cancelled, and would take the
> next dossier numbers if taken up.

## The sequence

| CR | Function | Adds | Axis |
|---|---|---|---|
| 1 | model_response | Register a model, place it in service with a system prompt and response rules, and submit a user prompt through the test model. Rules apply while the model writes. Refusals are recorded. | both, thin |
| 2 | registry | The full registry: describe, list, retire, reinstate | flexibility |
| 3 | disclosure | Review a finished model response before release | behavior |
| 4 | action | A model proposes an action. Only an authorized actor's authority lets it proceed. | behavior |
| 5 | substitution | Replace the model in service under unchanged behavior declarations. The identity change is evidenced. | flexibility |
| 6 | reporting | Evidence for an independent auditor | both |

CR-1 is a vertical slice: it carries the concept (rules applied during writing, refused at a
governed boundary) through the whole path first. Later change requests broaden it.

A real model binding follows CR-6 as an implementation change. The behavior declarations stay
byte-identical, and the snapshot diff shows only the binding change.

## Implementation is deferred, never absent

- From CR-1, the model capability is realized by a scripted stand-in. It produces the cases
  each change request must refuse.
- The stand-in is permanent. It is a conformance workload, not scaffolding. The real model later
  joins it as a second realization; it does not replace it.
- Every other capability transform is a real implementation from the change request that introduces
  it.

## Where each change request's analysis happens

- **P3** maps each function's components to existing kinds. A gap is recorded there, in the change
  request that meets it, not in an up-front survey.
- **P6** maps the change request's conditions (authority closure, enforcement, evidence, worker
  neutrality) to existing invariants. A new invariant needs a demonstrated gap.
- A needed governance-surface change becomes its own dossier, complete at P6, per
  `THE_SHAPE_OF_A_CHANGE_V0.md` §7.
