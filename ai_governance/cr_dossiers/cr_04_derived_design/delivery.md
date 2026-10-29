# Delivery — cr_04_derived_design

**Decided by:** the domain owner, in this change's `ledger.yaml`. The ledger is the decision; every
other document here is derived from it.
**Designed against:** composition `ccee6f3adba8…` (`baseline.json`).
**Delivered:**
- AI licensing's and agent governance's designs are derived from their ledger by the Design
  Compiler's derive route. Every phase document, P0 to P6, is projected from the ledger, and P7 and
  P8 are the derived design.
- The business holds its own facts and rules, and takes none of them from a request. This is the
  owner's ruling, and the ledger has no shape for anything else. Every difference from the earlier
  design follows from it, so this change request is the only one. No owner decision is left to
  deliver as its own delta.

**Validated:**
- Phase documents 7/7 admissible. Construction 1965/1965 determined.
- Owner decisions 21/21 (`testbed/owner_decisions/execution_validation_owner_decisions.py`).
- Routing closure 4/4 (`testbed/routing_closure/execution_validation.py`, rewritten for the
  derived reclaim).
- The seven agent-governance scenarios in `testbed/agent_governance/README.md` give their stated
  decisions, against licenses that AI licensing's own acts provisioned.
- This ledger equals the derive route's test ledger for ai_governance, answer for answer.
  Re-deriving it keeps all 59 artifacts.

---

## What changed, and why each change follows from the ruling

| Earlier design | Delivered | Why |
|---|---|---|
| Provisioning reads training, the assigned count and the cap from the request | `register employee`, `record training completed` and `set license cap` record them. Provisioning checks the records, refuses an untrained employee, and refuses a license at the cap. | A fact the request states is not one the business holds. |
| The request supplies the license id | The business forms the license's identity from the employee, so an employee holds one active license. | Agent governance finds a user's license by the user. |
| Provisioning assigns no tier | The request names `standard` or `enterprise`; any other tier is refused; one cap covers both. | Agent governance reads the tier from licensing's license. |
| A separate act, `WF_DENY_PROVISION_V0`, announces a denial | Provisioning announces its own denial, with the reason the failed check gives. | The ledger has no act that only announces. |
| Reclaim reads the threshold and both dates from the request | Reclaim holds 30 days. It reads the last use that `record license usage` keeps, and today from the clock. A license never used counts from provisioning. | As above. |
| Agent governance reads `license_facts.json`, a store no act writes | It reads AI licensing's license and writes nothing there. | The ledger cannot name a store no act writes. |
| The actors `AC_ENTERPRISE_RUNTIME_V0` and `AC_SYSTEM_GOVERNOR_V0` | Retired. | No act names them. |

**Replaced:**
- `WF_PROVISION_AI_LICENSING_V0` by `WF_PROVISION_LICENSE_V0`;
- `WF_AUTO_RECLAIM_V0` by `WF_RECLAIM_LICENSE_V0`;
- their entrances likewise.

**Superseded:** 16 artifacts, including `WF_GOVERN_AGENT_ACTION_V0` by `_V1`, both bindings,
both storage structures and every event.

**Retired:** 18 artifacts, among them `WF_DENY_PROVISION_V0` and the earlier contracts. Each deletion
is recorded in `.github/process/retired_identities.yaml`.

**One ending is named differently.** cr_02 decided that a reclaim the registry refuses keeps the
license assigned and announces nothing. The derived reclaim releases the license's identity before
it moves the license. A refused release therefore ends the reclaim at `EXIT_REJECTED`, before
anything changes, where the earlier design ended at `EXIT_ACTIVE`. The behavior cr_02 decided holds;
only the name of the ending differs. The ledger has no shape to route a refused release to
`otherwise`.

**Callers.** These were repointed:
- `testbed/routing_closure/execution_validation.py`;
- the agent-governance testbed and its README, which now licenses the seed users through
  `testbed/ai_licensing/test_payloads/`;
- `protocol_runtime/testbed/pgc/test_step_outcome.py`;
- `transformation_compilers/scripts/testbed/semantic_change_design_test.py`;
- the regression's execution steps and the runbook.

`license_facts.json` and the earlier provisioning payload are deleted.
