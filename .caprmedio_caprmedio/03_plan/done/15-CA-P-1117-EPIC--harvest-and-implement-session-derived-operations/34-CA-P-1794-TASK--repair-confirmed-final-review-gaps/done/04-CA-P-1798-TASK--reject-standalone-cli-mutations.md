---
atom_id: CA-P-1798
content_role: Plan
type: Plan
label: Task
work_sequence_number: 4
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
version: 1
updated_at: "2026-10-06 17:23:10 +0000"
subjects:
  governs: "Reject standalone CLI mutations"
  depends_on: [Implementation, Evaluation, Action, Journal]
relations:
  is_decomposition_of: [CA-P-1794]
  relates_to: [CA-C-504]
---
# Summary

Reject standalone CLI mutations

## Objective

reject standalone CLI apply before writes, preserving preview and the existing admitted selected/MCP native mutation functions.

## Details

- keep this repair bounded to its confirmed source contract. shared installed runtime, frozen candidates and historical Journals remain unchanged by fixture tests.
- preserve independent workers' edits; root owns Git, source pins and Release integration.

## Definition of Done

both executable wrappers reject direct apply without filesystem effects; preview and admitted native behavior retain coverage.

## Result

the canonical executable wrappers refuse standalone apply before repository resolution and writes. the 26-test focused suite passes, including actual subprocess refusal and preview zero-write checks; independent source/code review accepts the bounded repair. actual full Release completion remains a separate unfinished gate.
