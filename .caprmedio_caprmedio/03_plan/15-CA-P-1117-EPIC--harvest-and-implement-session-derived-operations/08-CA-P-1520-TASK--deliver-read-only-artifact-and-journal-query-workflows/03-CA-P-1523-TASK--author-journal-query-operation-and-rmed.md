---
atom_id: CA-P-1523
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: caprmedio
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: "Events Journal query source and RMED authoring"
  depends_on: [Operations, Workflow, Action, Tool, Evaluation, Journal]
version: 1
updated_at: "2026-10-04 20:15:56 +0000"
relations:
  is_decomposition_of: [CA-P-1520]
  blocks: [CA-P-1524]
---
# Summary

author journal query operation and rmed

## Objective

Within <=15 minutes, author only the minimum source packet for Find and Fetch Journal Events: one read-only Workflow, one query Action, required Step(s), and their PROGRAMMATIC RMED/Evaluation/Delivery contract. No code, alternate log, MCP registration, or source snapshot mutation.

### Exact inputs, outputs, and gate

Inputs are the live Goal/Principles, current active operation/RMED layout, CA-P-1520, the canonical Events Journal and shared Run/Journal contract. Outputs are saved, active, uniquely identified O Workflow/Action/Step and RMED carriers in native authority paths, source-to-RMED bindings, target Tool path `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/FIND_AND_FETCH_JOURNAL_EVENTS/`, and golden-test path `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/FIND_AND_FETCH_JOURNAL_EVENTS/tests/test_find_and_fetch_journal_events.py`.

The canonical Events Journal is the sole query source. The contract must cover Event IDs by default, selected fields or full Events, Event-field filtering with equality/inequality/NOT/IN and unambiguous boolean grammar, truthful bounded coverage/pagination, and the caller's requested field/value selection. Report malformed Event records, missing Event IDs, duplicate Event fields, incomplete reads and invalid filters. Bind a stable source snapshot so this query's execution records are not included in or allowed to enlarge its own result set. Do not create a competing log, infer identity from filenames, fetch credentials/secrets, evaluate arbitrary SQL/code, create mutation authority or invent Runs. These absent outputs block P1524/P1526/P1527 and cannot be assumed bound.

### Verification

Statically verify one minimal Workflow/Action route, canonical-Journal-only source binding, complete source/RMED references, exact target/test paths, required negative diagnostics, and `git diff --check`. Archive meaningful predecessor source revisions only when active carrier rules require replacement. Record only actual saved authoring evidence; remain Active until complete.

### Definition of Done

The exact active source/RMED IDs, Versions, and paths are saved with the canonical-Journal contract and verification; otherwise this authoring packet remains Active and blocks P1524.
