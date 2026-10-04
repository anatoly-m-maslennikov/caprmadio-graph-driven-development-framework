---
atom_id: CA-D-547
content_role: Delivery
current_scope_unit: MCP
claim_target_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 18:30:00 +0000"
subjects:
  governs: "MCP/selected Workflow adapter Carrier"
  depends_on: [MCP, Tool, Workflow, Action, Operator, Run, Journal]
relations:
  delivery_for: [CA-R-1847, CA-R-1848]
---
# Summary

Bind selected Workflow MCP adapters

## Scope

The declared delivery location and public request contract for selected MCP adapters.

## Claim

The selected adapter surface **must** be implemented in one Project-local MCP binding that delegates to shared Run support.

## Details

```toml
[selected_workflow_mcp]
entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/implementation_server.py"
adapter_module = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/selected_workflow_routes.py"
shared_service = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/WORKFLOW_OPERATIONS/RUN_SUPPORT"
routes = ["create_atom", "update_atom", "replace_atom", "change_atom_status", "create_scope_unit", "rename_scope_unit", "move_scope_unit", "remove_scope_unit", "run_implementation_workflow", "revert_changes", "build_entities_graph", "build_terms_graph", "build_applicable_methodology"]
observation_routes = ["get_selected_workflow_run", "get_selected_action_run", "recover_selected_run_recording"]
```

Each route adapts to, rather than redefines, `run_selected_operation(request)`. Its shared request contains route/operation identity, exact expected current definition revision, input/parameters, explicit current sealed Initiative authorization for a mutation, an idempotency/retry key, and real parent lineage only. Its shared `RunResult` contains real Run/definition IDs, outcome, result/effect/report/output refs, Journal recording state/event refs, currentness, and diagnostics. MCP uses `mode` defaulting to `preview` only to select permitted dispatch and passes the complete normalized request unchanged to shared support. Unknown fields, raw filesystem/shell instructions, mixed route capability, alternate root, or apply without exact authorization are errors or blocked outcomes.

`recover_selected_run_recording` accepts an exact pending event ref and optional request id only. This is a delivery declaration, not implementation acceptance.

### Sources

- CA-R-1847; CA-R-1848; CA-D-523 v2; CA-A-1141 v1 K7/K14–K16.
