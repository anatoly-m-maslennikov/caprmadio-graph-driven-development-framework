---
atom_id: CA-P-1541
content_role: Plan
type: Plan
label: Task
work_sequence_number: 14
current_scope_unit: caprmedio
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: "Deduplicate Workflow definition bindings for repeat Runs"
  depends_on: [Implementation, Workflow, Action, Evaluation, Journal]
version: 2
updated_at: "2026-10-04 22:18:37 +0000"
relations:
  is_decomposition_of: [CA-P-1137]
  blocks: [CA-P-1540, CA-P-1517]
---
# Summary

Deduplicate Workflow definition bindings for repeat Runs

## Objective

Within <=15 minutes, complete this one bounded required Epic remainder with saved source-bound evidence.

## Details

Inputs: current CA-P-1540 worker result and real test_shared_session_authorized_loop_uses_distinct_predeclared_visit_ids failure; accepted CA-P-1510 / CA-R-1821 through CA-R-1824, CA-E-541 through CA-E-544, CA-D-527 through CA-D-529; current active Methods at tmp/selected_workflows/current_active_methods.md. Ownership: 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/workflow_run_support.py and a dedicated bounded regression test under its tests/ only. Do not edit selected_execution.py, its tests, Journal schema, source authority, MCP, backend or Plans. Exact repeated Step/Action definition Revisions may occur in several predeclared requested Runs; a Workflow Event needs one canonical entry per identical definition Revision, not one entry per visit. Preserve all distinct requested/actual Run identities, lineage, lazy invoked-only recording, exact digests and currentness. Conflicting bindings are not silently collapsed. Reproduce the real P1540 failure before the change, deduplicate compatible Workflow-level bindings deterministically in the shared recorder, and prove the 19-test selected_execution suite plus selected-run and Journal compatibility suites. Add a real canonical-Journal regression showing distinct revisit Run IDs with unique definition_bindings. No effect replay, new permission, Journal relaxation or unbounded retry.

Inherit CA-P-1117's 90% confidence threshold and explicit mechanical Git save exception. You are not alone; preserve other workers' edits and use apply_patch. No harvesting, FPF, broader audit, permission bypass, deployment or unrelated changes. Root owns Plan updates and commits. If this bounded packet is incomplete, return exact remainder without claiming Done.

### Definition of Done

The owned packet has actual scoped verification and a truthful saved result with exact changed or reviewed files; aggregate all-fifteen Docker/MCP proof remains separate.

### Actual result

Canonical Workflow definition bindings now deduplicate identical pinned revisions while distinct requested/actual repeated Run identities and parent lineage remain intact. Conflicting exact bindings for one definition identity fail before dispatch. Journal schema-v5 uniqueness was preserved.

Changed files: workflow_run_support.py and tests/test_workflow_run_support_repeat_bindings.py. Root inspected the saved diff and independently reran the selected-execution suite (20 tests), selected-Run support suite (7), Journal schema-v5 suite (4), and dedicated real canonical-Journal repeat-binding regressions (2); all passed in the existing development Docker worker. The pre-change shared loop failed before any handler; the repaired case records distinct visit Run IDs with three unique reusable definition bindings. The current suite has twenty tests, superseding the planned count of nineteen.

CA-C-439 is resolved by this evidence. Full immutable-image and aggregate MCP/queue acceptance remain separate; no broader proof is claimed.
