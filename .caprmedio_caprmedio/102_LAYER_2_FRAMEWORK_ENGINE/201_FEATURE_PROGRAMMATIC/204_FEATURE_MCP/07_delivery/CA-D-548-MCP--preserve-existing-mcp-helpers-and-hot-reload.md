---
atom_id: CA-D-548
content_role: Delivery
current_scope_unit: MCP
claim_target_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 18:30:00 +0000"
subjects:
  governs: "MCP/selected Workflow compatibility"
  depends_on: [MCP, Tool, Workflow, Run, Project]
relations:
  delivery_for: [CA-R-1847, CA-R-1848]
---
# Summary

Preserve existing MCP helpers and hot reload

## Scope

Compatibility of selected MCP adapters with the stable gateway and existing helper surface.

## Claim

Selected adapters **must** be additive and reload-compatible; they **must not** replace the stable gateway, its root binding, or its eight existing helpers.

## Details

Implementation registers the declared routes through `create_server(root)` after root resolution and uses the current stdio transport and stable hot-reload boundary. It preserves `discover_tools`, `discover_operations`, `get_execution_context`, `get_execution_status`, `resume_execution_context`, `watch_execution`, `rmed_atoms_base_revise`, and `workflow_orchestrator` with their current names and contracts. It does not make `workflow_orchestrator` an executor for selected O016 or other unsupported selected Workflows.

Reload validates a complete new route registry before publication, keeps in-flight calls on their captured implementation generation, and rolls back invalid registration without removing prior helpers. The selected route registry exposes only current/admitted source bindings supplied by the adapter/service; stale or unsupported routes remain rejected or explicitly deferred. MCP code contains adapter/validation/projection logic only; the common `RUN_SUPPORT` interface owns lifecycle execution, durable event retries, and canonical Journal persistence.

### Sources

- CA-D-523 v2; CA-E-533 v1; CA-E-534 v1; CA-A-1141 v1 K7/K16.
