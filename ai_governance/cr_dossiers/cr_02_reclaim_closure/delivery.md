# Delivery — cr_02_reclaim_closure

**Authorized by:** Gate 1 and Gate 2, at P7 and P8, against composition `6783308c59ca…`
**Delivered:** the reclaim's removal step now answers a refused removal. It ends the contract, and
the reclaim act routes the refusal to EXIT_ACTIVE. The license stays assigned, and no revocation is
announced.
**Validated:** reclaim closure 4/4 (0 not exercised); full regression 13/13; construction acceptance
167/167; composition `00576332ef3c…`

---

## What this change closed

The registry declares four answers to a removal: removed, not found, refused, and unreachable. The
reclaim's removal step answered three. A refused removal had no route of its own.

Now the step answers all four, and ends the contract on each. The reclaim act already routed the
contract's VIOLATION to EXIT_ACTIVE, so the act is unchanged. One artifact was redeclared whole;
nothing was created and nothing was withdrawn.

---

## What it took

**The contract was stated whole for the first time.** The first licensing change reused it, so no
earlier design held it. Construction measured 53 of 53 facts determined. The emitted diff is the
added answer, the store the removal step writes (`LICENSE_REGISTRY`, which the registry previously
inferred), and the current renderer's layout.

**The design language was widened in two places to keep the contract whole.** Before that, an
amendment would have dropped three facts no register could state:

- `transformation/build/render.py`: an interface field's Type may carry a format, written
  `string (date-time)`, as the artifacts' own prose tables write it. The two date inputs keep
  `format: date-time`.
- `transformation/build/completeness.py`: carry-forward keeps a description that sits under a
  top-level block the design renders nothing else into. The contract keeps `extensions.description`.

Construction acceptance still reproduces 167 of 167 artifacts with no field difference.

**The refusal is deferred, not discharged.** A discharge must name a place in an act's topology, and
this act cannot be restated: no register carries its admission rules, its renamed audit node, or
its nested literal inputs. So `refusal_deferrals` names the act and the route it already has. This
is the second case of the gap queued as the `generated_discharge` design CR. That CR should also
accept a discharge through an act reused unchanged, read from the snapshot.

---

## What is carried

- **The defect was latent.** The removal is the contract's last step, so the runtime's default
  `continue` already ended the contract with VIOLATION, and the act already routed it to still
  active. Criterion 1 holds against the v5 composition too. The change closes the declaration
  (CP-13). The behaviour difference shows only once EX-18 makes the runtime refuse an unlisted
  outcome.
- **The refusal is staged.** The registry refuses a removal only when it is handed no key, and the
  contract refuses that earlier, at its own inputs. Criterion 1 stands in for the registry's removal
  for that one run.
- **A refused removal and a license still in use end the same way.** Both leave the license
  assigned. The business keeps one ending for both, and telling them apart is a later decision.
- **ai_governance is not in construction acceptance.** Its delivered dossiers are not yet compared
  against the built registry.
