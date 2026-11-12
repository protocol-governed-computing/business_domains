# Agent Governance Testbed

## Business Process

An AI agent acts on behalf of a human user. Before the agent may invoke any tool,
the business answers these questions in order:

1. **Is the request complete?** — A request missing what the act needs is rejected.
2. **Does the tool exist?** — Only tools declared in the closed registry may be
   referenced. Anything else is structurally absent.
3. **Is the user licensed?** — Read the license AI licensing holds for the user. No active
   license means no authority, regardless of which tool was requested.
4. **Does the license cover this tool?** — Each tier grants a specific, closed set of
   tools. Standard cannot invoke premium tools; enterprise can.
5. **Are the parameters valid?** — Tool-specific parameter rules (max quantity, allowed
   values, etc.) are enforced declaratively before the action is recorded.

Every judgment — authorized or denied — is recorded in the audit trail
(`governance_audit.jsonl`). An authorized action is registered once in `actions.json`, however
often it is proposed.

### License Tiers and Tool Surface

| Tier       | Allowed Tools                                                   |
|------------|-----------------------------------------------------------------|
| `standard` | `READ_RECORD`, `PROVISION_STANDARD_LICENSE`                     |
| `enterprise` | `READ_RECORD`, `PROVISION_STANDARD_LICENSE`, `PROVISION_PREMIUM_LICENSE` |

### Workflow: `WF_GOVERN_AGENT_ACTION_V1`

```
Request
  → Check the submission       — incomplete → EXIT_REJECTED
  → Require tool declared      — VIOLATION → Audit: UNDECLARED_TOOL
  → Resolve the license        — NOT_FOUND / VIOLATION → Audit: UNAUTHORIZED_ACTOR
  → Require license active     — VIOLATION → Audit: UNAUTHORIZED_ACTOR
  → Require tier grants tool   — VIOLATION → Audit: UNAUTHORIZED_TOOL
  → Require parameters satisfy rules — VIOLATION → Audit: PARAMETER_VIOLATION
  → Form, claim and write the action, audit the judgment → EXIT_COMPLETED
```

---

## Setup

### One-time: license the seed users

Agent governance reads the license AI licensing holds for the requesting user, and writes nothing
there. License the seed users through AI licensing's own acts, in this order:

```bash
P=../ai_licensing/test_payloads
for step in SET_LICENSE_CAP:01_set_license_cap \
            REGISTER_EMPLOYEE:02_register_employee_std RECORD_TRAINING_COMPLETED:03_record_training_std \
            PROVISION_LICENSE:04_provision_license_std \
            REGISTER_EMPLOYEE:05_register_employee_ent RECORD_TRAINING_COMPLETED:06_record_training_ent \
            PROVISION_LICENSE:07_provision_license_ent; do
  protocol_runtime run --wf "ai_governance::WF_${step%%:*}_V0" --payload "$P/${step#*:}.json" \
    --data-root "$PGC_DATA_ROOT" --snapshot "$PGC_SNAPSHOT_ROOT"
done
```

### Seed users

| User ID        | License Status | Tier         |
|----------------|----------------|--------------|
| `EMP_STD_001`  | active         | standard     |
| `EMP_ENT_001`  | active         | enterprise   |
| `EMP_NONE_001` | *(never licensed)* | none     |

---

## Running a Scenario

```bash
protocol_runtime run \
  --wf ai_governance::WF_GOVERN_AGENT_ACTION_V1 \
  --payload <path-to-payload.json> \
  --data-root "$PGC_DATA_ROOT" \
  --snapshot "$PGC_SNAPSHOT_ROOT"
```

To inspect the audit trail after running:

```bash
cat "$PGC_DATA_ROOT/ai_governance/agent_governance/governance_audit.jsonl" | python3 -c "
import sys, json
for i, line in enumerate(sys.stdin, 1):
    r = json.loads(line)['record']
    print(f'{i:02d}. {r[\"decision\"]:10} | {r[\"event_code\"]} | tool={r[\"tool_name\"]} | denial={r.get(\"denial_reason\",\"-\")}')
"
```

---

## Scenarios

### 01 — Authorized: standard user, standard tool, valid parameters

**Payload:** `test_payloads/01_valid_standard_action.json`

```json
{ "tool_name": "PROVISION_STANDARD_LICENSE", "parameters": { "tier": "standard", "quantity": 50 },
  "requesting_user_id": "EMP_STD_001", "domain_context": "ai_licensing" }
```

**Expected decision:** `AUTHORIZED`
**Audit event:** `EV_AGENT_ACTION_AUTHORIZED_V1`
**Path:** full happy path — all five gates pass, action recorded.

---

### 02 — Denied: no license record

**Payload:** `test_payloads/02_no_license.json`

```json
{ "tool_name": "PROVISION_STANDARD_LICENSE", "parameters": { "tier": "standard", "quantity": 10 },
  "requesting_user_id": "EMP_NONE_001", "domain_context": "ai_licensing" }
```

**Expected decision:** `DENIED` — `UNAUTHORIZED_ACTOR`
**Path:** tool declared (pass) → resolve the license **NOT_FOUND** → audit denial.
`EMP_NONE_001` was never licensed.

---

### 03 — Denied: standard user requests premium tool

**Payload:** `test_payloads/03_standard_requests_premium.json`

```json
{ "tool_name": "PROVISION_PREMIUM_LICENSE", "parameters": { "tier": "premium", "quantity": 10 },
  "requesting_user_id": "EMP_STD_001", "domain_context": "ai_licensing" }
```

**Expected decision:** `DENIED` — `UNAUTHORIZED_TOOL`
**Path:** resolve the license (standard tier) → tier grants tool: `PROVISION_PREMIUM_LICENSE` not in
`["READ_RECORD", "PROVISION_STANDARD_LICENSE"]` → **VIOLATION** → Audit denial.

---

### 04 — Authorized: enterprise user, premium tool, valid parameters

**Payload:** `test_payloads/04_enterprise_premium_allowed.json`

```json
{ "tool_name": "PROVISION_PREMIUM_LICENSE", "parameters": { "tier": "premium", "quantity": 25 },
  "requesting_user_id": "EMP_ENT_001", "domain_context": "ai_licensing" }
```

**Expected decision:** `AUTHORIZED`
**Path:** Enterprise tier includes `PROVISION_PREMIUM_LICENSE` — all gates pass.

---

### 05 — Denied: tool not in registry

**Payload:** `test_payloads/05_undeclared_tool.json`

```json
{ "tool_name": "DELETE_DATABASE", "parameters": {},
  "requesting_user_id": "EMP_STD_001", "domain_context": "ai_licensing" }
```

**Expected decision:** `DENIED` — `UNDECLARED_TOOL`
**Path:** tool declared: `DELETE_DATABASE` absent from the closed set
→ **VIOLATION** → Audit denial. The workflow exits at the second gate;
license is never consulted.

---

### 06 — Denied: parameter rule violation (quantity exceeds limit)

**Payload:** `test_payloads/06_parameter_violation.json`

```json
{ "tool_name": "PROVISION_STANDARD_LICENSE", "parameters": { "tier": "standard", "quantity": 200 },
  "requesting_user_id": "EMP_STD_001", "domain_context": "ai_licensing" }
```

**Expected decision:** `DENIED` — `PARAMETER_VIOLATION`
**Path:** All four earlier gates pass (declared, licensed, authorized tier), then
parameters satisfy rules: `quantity=200` exceeds the declared max → **VIOLATION** → Audit denial.

---

### 07 — Denied: shell command not in registry (enterprise user, doesn't matter)

**Payload:** `test_payloads/07_shell_command_absent.json`

```json
{ "tool_name": "EXECUTE_SHELL_COMMAND", "parameters": { "command": "rm -rf /" },
  "requesting_user_id": "EMP_ENT_001", "domain_context": "system" }
```

**Expected decision:** `DENIED` — `UNDECLARED_TOOL`
**Path:** tool declared: `EXECUTE_SHELL_COMMAND` not in the closed set → **VIOLATION** → Audit denial.
Enterprise tier is irrelevant — the tool surface is closed before license is checked.

---

## Summary Table

| # | User           | Tool                       | Params          | Decision   | Denial Reason       |
|---|----------------|----------------------------|-----------------|------------|---------------------|
| 01 | EMP_STD_001   | PROVISION_STANDARD_LICENSE | qty=50          | AUTHORIZED | —                   |
| 02 | EMP_NONE_001  | PROVISION_STANDARD_LICENSE | qty=10          | DENIED     | UNAUTHORIZED_ACTOR  |
| 03 | EMP_STD_001   | PROVISION_PREMIUM_LICENSE  | qty=10          | DENIED     | UNAUTHORIZED_TOOL   |
| 04 | EMP_ENT_001   | PROVISION_PREMIUM_LICENSE  | qty=25          | AUTHORIZED | —                   |
| 05 | EMP_STD_001   | DELETE_DATABASE            | {}              | DENIED     | UNDECLARED_TOOL     |
| 06 | EMP_STD_001   | PROVISION_STANDARD_LICENSE | qty=200         | DENIED     | PARAMETER_VIOLATION |
| 07 | EMP_ENT_001   | EXECUTE_SHELL_COMMAND      | rm -rf /        | DENIED     | UNDECLARED_TOOL     |

---

## Debugging Notes

### Artifacts to inspect

| Question | Artifact |
|---|---|
| What tools are declared? | `CC_REQUIRE_TOOL_DECLARED_V0` |
| What tools does a tier get? | `CC_REQUIRE_TIER_GRANTS_TOOL_V0` |
| What parameter rules apply? | `CC_REQUIRE_PARAMETERS_SATISFY_RULES_V0` |
| What happened at runtime? | `$PGC_DATA_ROOT/ai_governance/agent_governance/governance_audit.jsonl` |
| Full execution trace? | `$PGC_DATA_ROOT/traces/` |

### Two classes of protocol bug

**Routing bugs** (visible in graph topology): wrong `next` condition on a WF node, or
wrong `on_result` key in a CC step. The compiled graph (`WF_GOVERN_AGENT_ACTION_V1.graph.json`)
shows these — every edge is an `on_result` condition.

**Binding bugs** (invisible in graph topology): wrong `$.path` expression in a CC step's
`inputs` or `outputs` block. These cause the runtime to silently resolve `None` and either
misroute or crash. To debug: open the full CC artifact in
`protocol_snapshot/artifacts/capability_contracts/` and trace each `$.` path manually.
The graph `projection.steps[].bindings` shows *which* inputs are bound but not the full
JSONPath expression. The new `input_bindings` field on each graph node shows the WF-level
data flow into each CC.

### CT atoms signal VIOLATION by raising

`CT_PURE_VALIDATE_SET_MEMBERSHIP_V0` and `CT_PURE_VALIDATE_PARAMETER_RULES_V0` raise
`CTExecutionError` on constraint failure. If you add a new validation CT, it must raise
(not return a falsy field) for `on_result: VIOLATION` routing to trigger.
