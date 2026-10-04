---
atom_id: CA-R-1847
content_role: Requirement
current_scope_unit: MCP
claim_target_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 18:30:00 +0000"
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

The public route names are `create_atom`, `update_atom`, `replace_atom`, `change_atom_status`, `create_scope_unit`, `rename_scope_unit`, `move_scope_unit`, `remove_scope_unit`, `run_implementation_workflow`, `revert_changes`, `build_entities_graph`, `build_terms_graph`, and `build_applicable_methodology`. They bind respectively to the accepted source definitions: O032 v4, O030 v4, O051 v6/O031 v3, R1521 v4/O029 v3, O015 v6/O012–O014 v5, O015 v6/O012–O014 v5, O015 v6/O012–O014 v5, O015 v6/O012–O014 v5, O016 v11/O017 v6/O024 v11, O130 v1/O131 v2/O132 v1, R1438 v8/R1387 v8, R1335 v13/R1387 v8, and O011 v10/O010 v7/R1317 v11. A route does not claim a missing source implementation is present.

Every route delegates one normalized request to shared `run_selected_operation(request)`: route/operation identity, exact expected current definition revision, input/parameters, source-frontier/currentness refs, caller-chosen idempotency/retry key, optional real parent lineage, and explicit current sealed Initiative authorization for mutations. It returns only the shared `RunResult`: real Run/definition IDs, outcome, safe result/effect/report/output refs, canonical Journal recording state/event refs, source currentness, and diagnostics. A preview is the default. `apply` is accepted only for a mutation-capable route with explicit Operator authorization bound to the exact preview, target/frontier digests, effects, and request id; it never starts a worker automatically.

`get_selected_workflow_run` and `get_selected_action_run` read only one exact Run/Action Run and return its status, safe output/result/effect references, lineage, source currentness, and canonical event/receipt references. `recover_selected_run_recording` accepts only a pending shared-recording event reference and retries persistence with the same event identity and payload; it never replays an Action or Workflow. MCP must not implement a parallel request schema or execution path.

The adapters reuse the server's existing Project-root/stdin binding, discovery helpers, `workflow_orchestrator`, and hot-reload gateway. They add no alternate root, shell, arbitrary path, generic mutation, implicit dispatch, Journal writer, or duplicate business behavior. The existing eight helper names and their contracts remain available. Route annotations truthfully describe preview/apply behavior and do not override client permission policy.

### Sources

- CA-A-1141 v1, thirteen-row mapping and K7/K14–K16; CA-P-1117 v3 shared Run obligation.
- CA-R-1720 v17; CA-R-1525 v6; CA-R-1728 v16; CA-D-523 v2.
