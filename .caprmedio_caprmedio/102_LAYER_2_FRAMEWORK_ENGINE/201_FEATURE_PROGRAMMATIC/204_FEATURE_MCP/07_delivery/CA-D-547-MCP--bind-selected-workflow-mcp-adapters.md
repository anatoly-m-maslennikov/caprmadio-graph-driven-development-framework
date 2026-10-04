---
atom_id: CA-D-547
content_role: Delivery
current_scope_unit: MCP
claim_target_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-04 19:21:30 +0000"
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
binding_manifest = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/selected_workflow_bindings.json"
canonical_manifest_binding = "request.definition_manifest.{manifest_ref,manifest_digest}"
routes = ["create_atom", "update_atom", "replace_atom", "change_atom_status", "create_scope_unit", "rename_scope_unit", "move_scope_unit", "remove_scope_unit", "run_implementation_workflow", "revert_changes", "build_entities_graph", "build_terms_graph", "build_applicable_methodology"]
observation_routes = ["get_selected_workflow_run", "get_selected_action_run", "recover_selected_run_recording"]
```

`selected_workflow_bindings.json` is the one derived immutable per-route manifest. It materializes CA-A-1142 v2's already-reviewed current source registry; it is not a second graph authority and cannot select, replace, or repair sources. For every one of the thirteen routes it includes one exact source Workflow, its full ordered Step list, the full ordered Action list bound to those Steps, and only source-closed actual native Action calls. Every definition entry carries its repository-relative source path, Atom ID, Version, and SHA-256 digest. Its `canonical_manifest_sha256` is the SHA-256 of RFC 8785 canonical JSON for the whole object with that self field omitted; a server checks the same canonical digest and every source pin before registration and again before dispatch. Absent, incomplete, duplicate, malformed, altered, or stale manifests reject without shared-support invocation, Run, Action Run, worker, effect, Event, or Journal write.

Each route adapts to, rather than redefines, `run_selected_operation(request)`. Its shared request contains route/operation identity, typed input/parameters, explicit current sealed Initiative authorization for a mutation, an idempotency/retry key, real parent lineage only, and exactly the outer canonical `definition_manifest` (`manifest_ref`, `manifest_digest`). `source_freshness` retains only selected-source registry/binding evidence; a manifest ref/digest there or anywhere else is a shadow unknown field and is rejected, whether matching or different. Its shared `RunResult` contains real Run/definition IDs, outcome, result/effect/report/output refs, Journal recording state/event refs, currentness, and diagnostics. MCP uses `mode` defaulting to `preview`; only explicit `execute` may request dispatch, and the complete normalized request passes unchanged to shared support. CA-D-521 v3's existing `enqueue_selected` is the accepted general DBOS dispatch variant: the adapter reuses the existing APP and does not introduce an executor. Unknown fields, raw filesystem/shell instructions, mixed route capability, alternate root, `apply`, or execute without exact authorization are errors or blocked outcomes.

`recover_selected_run_recording` accepts an exact pending event ref and optional request id only. This is a delivery declaration, not implementation acceptance.

### Sources

- CA-R-1847 v3; CA-R-1848 v3; CA-E-567 v3; CA-E-568 v3.
- CA-A-1142 v2; CA-D-527 v3; CA-D-521 v3; CA-D-548 v1; CA-D-523 v2.
