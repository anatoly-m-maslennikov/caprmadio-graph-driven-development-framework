---
subjects:
  governs: "feature-boundary"
  depends_on: []
version: 10
updated_at: "2026-10-05 00:12:58 +0000"
relations:
  method_for:
    - CA-R-857
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-M-104
content_role: Method
status: Active
current_scope_unit: START_BACKGROUND_SERVICES
claim_target_scope_unit: START_BACKGROUND_SERVICES
local_tier: Core
global_tier: 12
type: Implementation Method
---
# Summary

Control registered background services

## Scope

START_BACKGROUND_SERVICES contribution represented by this existing legacy Atom.

## Claim

Verify the selected runtime release, parse **and** validate its `background_services.toml`, expand **only** registered repository, runtime, temporary-state, Tool-root, **and** interpreter placeholders, **and** reject executable Framework Carriers outside `.caprmedio_runtime/tools`.

For status, report admission, queue count **and** bytes, active action **and** phase, process identity, selected release, leases, last success **and** failure, budget usage, circuit state, **and** dead letters **without** mutation. For pause, stop new dispatch **and** preserve intake **and** action state. For resume **or** start, verify health **and** declared budgets, restore admission, **and** drain accepted work **without** starting a duplicate process. For stop, stop admission, request cooperative bounded shutdown, **and** wait for a declared recoverable boundary. For reload, stop at that boundary, re-resolve the selected release, restart, **and** reconcile preserved work.

Use atomic PID **and** lifecycle-state records below each Runtime service directory, with their atomic-write intermediates below `.caprmedio_tmp`. Start processes **without** a shell, route technical and business log output to configured governed Journal sinks, which may be local or remote and need not use the runtime directory, route bytecode **and** disposable cache state **to** Project Temporary State, **and** verify the declared startup grace interval. Automatically restart **or** resume **only** a classified transient pre-mutation failure within its measured budget **and** **after** cooldown **and** health checks. Open the circuit **and** require explicit Operator recovery for exhausted budgets **or** governance, Journal, staging, ambiguous Git, **and** lease-integrity failures.

Stopping, reinstalling, reloading, or cleaning disposable service state must preserve accepted runtime Journal history and the Project Work Journal. A local sink is not disposable merely because a process wrote it; do not remove a runtime directory that contains retained Journal records.
