---
atom_id: CA-P-1797
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
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
  governs: "Require preparation Evaluation authority"
  depends_on: [Implementation, Evaluation, Action, Journal]
relations:
  is_decomposition_of: [CA-P-1794]
  relates_to: [CA-C-503]
---
# Summary

Require preparation Evaluation authority

## Objective

require the bound Evaluation at preparation and test missing, stale and wrong-role bindings before any agent call.

## Details

- keep this repair bounded to its confirmed source contract. shared installed runtime, frozen candidates and historical Journals remain unchanged by fixture tests.
- preserve independent workers' edits; root owns Git, source pins and Release integration.

## Definition of Done

the preparation rejection matrix and focused prompt/binding suites pass; rejected cases call no agent.

## Result

the preparation test rejects missing, stale and wrong-role Evaluation bindings before dispatch. the focused prompt-contract suite passes 20 tests and selected-project-binding suite passes seven; independent review accepts the repair. actual full Release completion remains a separate unfinished gate.
