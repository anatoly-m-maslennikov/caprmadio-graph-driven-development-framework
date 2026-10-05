---
atom_id: CA-P-1695
content_role: Plan
type: Plan
label: Task
work_sequence_number: 12
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
subjects:
  governs: "Align MCP status-request golden inputs"
  depends_on: [Atom, Tool, Manifest, Evaluation, Workflow]
version: 1
updated_at: "2026-10-05 06:19:48 +0000"
relations:
  is_decomposition_of: [CA-P-1643]
  blocks: [CA-P-1644]
---
# Summary

Align MCP status-request golden inputs

## Objective

Within <=15 minutes, align MCP status-request golden inputs.

## Details

Own only the two MCP golden test files containing test_every_selected_route_forwards_one_mutation_free_preview and test_current_physical_manifest_freezes_original_thirteen_through_queue, plus their existing fixture helper if necessary. Current failures use obsolete route_input for change_atom_status; current accepted admission requires actual target and status. Construct real disposable Atom/model/structure bindings without weakening status, source, preview, queue or no-mutation guards. Golden first, run the focused MCP suites. No production code or actual manifest/source changes, runtime/image/queue-process effects, Git/Plan writes or permission workaround. Preserve other Agents' edits; report pre-existing versus corrected findings truthfully.

## Definition of Done

The exact targeted saved effects/refusals and focused cases pass with code/test hashes. Required parent integration and image proof remain separate.

## Result

The only changed file is tests/test_selected_routes_mcp.py, SHA-256 `a9b68ee839cd4164563abd7ded89feaad9fa3fc1a6b04efd73988207935a5f2d`. Actual target/status descriptors and copied source-bound models/Project Structure replace obsolete status placeholders; the queue fixture uses a real preview receipt. Root ran all twelve tests in the designated development worker: twelve pass in1.476s. The worker's host verification was incomplete, not called a pass. This proves fixture/development regression behavior only, not actual queue-process or immutable-image acceptance.
