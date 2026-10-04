---
atom_id: CA-P-1534
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
status: Active
subjects:
  governs: "Align missing Event field filter semantics"
  depends_on: [Implementation, Workflow, Action, Evaluation, Journal]
version: 1
updated_at: "2026-10-05 01:30:00 +0400"
relations:
  is_decomposition_of: [CA-P-1520]
  blocks: [CA-P-1535]
---
# Summary

Align missing Event field filter semantics

## Objective

Within <=15 minutes, repair the single confirmed source conflict rejected by P1533.

## Details

Own only current CA-R-1869 and CA-E-575, their @2 predecessor archives, and one new CA-C-438 Conflict in TOOLS. Read shared R1850@2 and P1533 rejection. A syntactically valid event:/ JSON Pointer absent from an individual Event follows shared missing=false comparison semantics; invalid namespace/escaping/syntax is rejected. Add an explicit missing-versus-null golden case. Do not modify R1850 or invent a local grammar, Tool or Journal. Source edits require Version bump and preserved predecessor; Summary unchanged. Publish exact current SHA-256 pins. Confidence 90%; check active Principles before a question.

### Definition of Done

The exact bounded result, changed files, source pins and actual verification are saved with truthful remainder. No broader implementation or immutable-image proof is implied.
