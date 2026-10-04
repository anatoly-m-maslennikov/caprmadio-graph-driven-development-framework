---
atom_id: CA-D-547
content_role: Delivery
current_scope_unit: MCP
claim_target_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 5
updated_at: "2026-10-05 02:00:00 +0400"
subjects:
  governs: "MCP/selected Workflow adapter Carrier"
  depends_on: [MCP, Tool, Workflow, Action, Operator, Run, Journal, Projection, Project]
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
adapter_module = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/selected_routes.py"
shared_service = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/workflow_run_support.py"
execute_dispatch = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/orchestrator.py:enqueue_selected"
binding_manifest = ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json"
canonical_manifest_binding = "request.definition_manifest.{manifest_ref,manifest_digest}"
routes = ["create_atom", "update_atom", "replace_atom", "change_atom_status", "create_scope_unit", "rename_scope_unit", "move_scope_unit", "remove_scope_unit", "run_implementation_workflow", "revert_changes", "build_entities_graph", "build_terms_graph", "build_applicable_methodology", "find_and_fetch_artifacts", "find_and_fetch_journal_events"]
observation_routes = ["get_selected_workflow_run", "get_selected_action_run", "recover_selected_run_recording"]
```

`selected_workflow_bindings.json` is the one derived immutable per-route
Projection manifest. It resides in the selected Project's registered
`_projection/` root; the MCP implementation code retains its Engine delivery
location. Its existing thirteen entries materialize CA-A-1142 v2's
already-reviewed current source registry unchanged. Its two additional entries
are `find_and_fetch_artifacts` and `find_and_fetch_journal_events`, admitted
only by the exact CA-P-1532@2 and CA-P-1535@2 source-frontier pins specified in
CA-R-1847@4. The manifest keeps those two acceptance pins in one
`query_source_admissions` field and includes their accepted CA-O-158/159/160
and CA-O-161/162/163 source pins in the corresponding route definitions. It is
not a second graph authority and cannot select, replace, repair, or independently
admit a source.

For every route the manifest includes one exact source Workflow, its full
ordered Step list, its full ordered Action list, and only source-closed actual
native Action calls. Every definition entry carries its repository-relative
source path, Atom ID, Version, and SHA-256 digest. Its
`canonical_manifest_sha256` is the SHA-256 of RFC 8785 canonical JSON for the
whole object with that self field omitted; a server checks that canonical digest,
all original source pins, and both query admission frontiers before registration
and again before dispatch. Absent, incomplete, duplicate, malformed, altered,
or stale manifests reject without shared-support invocation, Run, Action Run,
worker, effect, Event, or Journal write.

Each route adapts to, rather than redefines, `run_selected_operation(request)`.
Its shared request contains route/operation identity, typed input/parameters, an
idempotency/retry key, real parent lineage only, and exactly the outer canonical
`definition_manifest` (`manifest_ref`, `manifest_digest`). A mutation also
contains explicit current sealed Initiative authorization. `source_freshness`
retains only selected-source registry/binding evidence; a manifest ref/digest
there or anywhere else is a shadow unknown field and is rejected, whether
matching or different. Its shared `RunResult` contains real Run/definition IDs,
outcome, result/effect/report/output refs, Journal recording state/event refs,
currentness, and diagnostics. MCP uses `mode` defaulting to `preview`; preview
has no Run/Event, and only explicit `execute` may request dispatch. An admitted
read-only query execute has no mutation authority; it is source-bound to its
canonical manifest and acceptance frontier. For the Journal route, capture the
CA-O-163 source token before shared support can record its own Run/Event.
CA-D-521 v3's existing `enqueue_selected` remains the accepted general DBOS
dispatch variant: the adapter reuses the existing APP and does not introduce an
executor. Unknown fields, raw filesystem/shell instructions, mixed route
capability, alternate root, `apply`, or execute without its required exact
authorization/admission are errors or blocked outcomes.

`recover_selected_run_recording` accepts an exact pending event ref and optional
request id only. This is a delivery declaration, not implementation acceptance:
the present `selected_routes.py` and both currently checked-in manifests still
publish the original thirteen-route schema, so this RMED revision does not claim
that either query route is registered, executable, or functionally verified.

### Sources

- CA-R-1847 v4; CA-R-1848 v4; CA-E-567 v4; CA-E-568 v4.
- CA-A-1142 v2; CA-P-1532 v2; CA-P-1535 v2; CA-D-527 v3; CA-D-521 v3; CA-D-548 v2; CA-D-523 v2.
