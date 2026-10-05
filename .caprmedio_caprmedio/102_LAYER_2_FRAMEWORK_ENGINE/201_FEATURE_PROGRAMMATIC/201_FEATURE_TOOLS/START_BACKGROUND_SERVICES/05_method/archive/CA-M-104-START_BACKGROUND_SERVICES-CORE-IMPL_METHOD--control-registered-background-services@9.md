---
subjects:
  governs: "feature-boundary"
  depends_on: []
version: 9
updated_at: 2026-09-15 03:15:32 +0400
relations:
  method_for:
    - CA-R-857
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Control registered background services

Verify the selected runtime release, parse **and** validate its `background_services.toml`, expand **only** registered repository, runtime, temporary-state, Tool-root, **and** interpreter placeholders, **and** reject executable Framework Carriers outside `.caprmedio_runtime/tools`.

For status, report admission, queue count **and** bytes, active action **and** phase, process identity, selected release, leases, last success **and** failure, budget usage, circuit state, **and** dead letters **without** mutation. For pause, stop new dispatch **and** preserve intake **and** action state. For resume **or** start, verify health **and** declared budgets, restore admission, **and** drain accepted work **without** starting a duplicate process. For stop, stop admission, request cooperative bounded shutdown, **and** wait for a declared recoverable boundary. For reload, stop at that boundary, re-resolve the selected release, restart, **and** reconcile preserved work.

Use atomic PID **and** lifecycle-state records below each Runtime service directory, with their atomic-write intermediates below `.caprmedio_tmp`. Start processes **without** a shell, route output **to** Runtime logs, route bytecode **and** disposable cache state **to** Project Temporary State, **and** verify the declared startup grace interval. Automatically restart **or** resume **only** a classified transient pre-mutation failure within its measured budget **and** **after** cooldown **and** health checks. Open the circuit **and** require explicit Operator recovery for exhausted budgets **or** governance, Journal, staging, ambiguous Git, **and** lease-integrity failures.
