---
atom_id: CA-R-1847
content_role: Requirement
current_scope_unit: MCP
claim_target_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-04 19:03:32 +0000"
subjects:
  governs: "MCP/selected Workflow capability routes"
  depends_on: [MCP, Tool, Workflow, Action, Operator, Run, Journal]
relations:
  relates_to: [CA-R-1720, CA-R-1525, CA-R-1728, CA-P-1484]
---
# Summary

Expose selected Workflow capability routes

## Scope

The Project-local MCP adapter surface for the thirteen Operator-selected P1117 capabilities and their standalone/nested Action and Run observations.

## Claim

MCP **must** expose exactly the selected capability adapters below through the existing reloadable Project-local server, while delegating execution and every-Run recording to the shared `WORKFLOW_OPERATIONS/RUN_SUPPORT` service.

## Details

The public route names are `create_atom`, `update_atom`, `replace_atom`, `change_atom_status`, `create_scope_unit`, `rename_scope_unit`, `move_scope_unit`, `remove_scope_unit`, `run_implementation_workflow`, `revert_changes`, `build_entities_graph`, `build_terms_graph`, and `build_applicable_methodology`. Their only selected-definition binding is the closed thirteen-route projection `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/selected_workflow_bindings.json`, derived from CA-A-1142 v2. It carries every route's full current source Workflow, ordered Steps, ordered Action bindings, and any source-closed native Action call with exact source path, Version, and SHA-256 digest. It is an immutable derived projection, not another Workflow graph or source authority. Missing, malformed, incomplete, duplicate, digest-mismatched, or stale bindings reject the route before shared support, worker start, Run creation, Action Run creation, effect, or Journal event.

Every route delegates one normalized request to shared `run_selected_operation(request)`: route/operation identity, the manifest digest and exact expected current definition bindings, input/parameters, source-frontier/currentness refs, caller-chosen idempotency/retry key, optional real parent lineage, and explicit current sealed Initiative authorization for mutations. It returns only the shared `RunResult`: real Run/definition IDs, outcome, safe result/effect/report/output refs, canonical Journal recording state/event refs, source currentness, and diagnostics. `mode` defaults to `preview`; only explicit `execute` may start work. `execute` is permitted only for a mutation-capable admitted route with explicit Operator authorization bound to the exact preview, target/frontier and manifest digests, effects, and request id; it never starts a worker automatically. No `apply` mode exists.

`get_selected_workflow_run` and `get_selected_action_run` read only one exact Run/Action Run and return its status, safe output/result/effect references, lineage, source currentness, and canonical event/receipt references. `recover_selected_run_recording` accepts only a pending shared-recording event reference and retries persistence with the same event identity and payload; it never replays an Action or Workflow. MCP must not implement a parallel request schema or execution path.

The adapters reuse the server's existing Project-root/stdin binding, discovery helpers, `workflow_orchestrator`, and hot-reload gateway. CA-D-521 v3's existing DBOS `enqueue_selected` variant remains the general selected-dispatch variant; MCP supplies the admitted request to that existing APP and does not create another executor. The adapters add no alternate root, shell, arbitrary path, generic mutation, implicit dispatch, Journal writer, or duplicate business behavior. The existing eight helper names and their contracts remain available. Route annotations truthfully describe preview/execute behavior and do not override client permission policy.

### Sources

- CA-A-1142 v2, exact current selected source registry and source-stage admission; CA-P-1117 v3 shared Run obligation.
- CA-D-527 v1; CA-D-521 v3; CA-D-548 v1; CA-R-1720 v17; CA-R-1525 v6; CA-R-1728 v16; CA-D-523 v2.
