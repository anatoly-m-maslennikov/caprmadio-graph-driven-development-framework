---
atom_id: CA-P-1781
content_role: Plan
type: Plan
label: Task
work_sequence_number: 30
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
version: 1
updated_at: "2026-10-06 10:52:36 +0000"
subjects:
  governs: "Git-backed Release binding baseline reconciliation"
  depends_on: [Manifest, Git, Journal, Operator, MCP, Evaluation]
relations:
  is_decomposition_of: [CA-P-1117]
  relates_to: [CA-C-497, CA-R-1893, CA-M-349, CA-E-592, CA-D-587]
  blocks: [CA-P-1780]
---
# Summary

Reconcile the exact Git-backed binding state

## Objective

record the Operator-approved, exact current Git-backed binding observation through independently reviewed source-first support, preserving all historical event and Manifest bytes, so guarded refresh can proceed truthfully.

## Details

- root owns source, integration, exact authorization and actual observation; independent bounded worker slices own the private observer, regression fixtures and read-only review. estimated implementation/verification slice <=15 minutes.
- R1893/M349/E592/D587 define this distinct support operation. use an existing-schema recovered state at the next positive carrier-history revision with an exact predecessor witness, not a fabricated completed historical change.
- the first refresh was blocked before a write; its latest canonical carrier record v2 hashes to `1eabfd2f1a0df45ae0df2ff4b2221ebe557ef1f520a990ef6d10f542259d6723`, while the exact current Git HEAD blob hashes to `e58209ebdfa598e7ed30b87abeac43606ab3fec35238c99870ea1a01a5a62946`.
- revalidate exact Git/current bytes, target history and absence of pending publication under the same carrier lock. refuse dirty, changed or conflicting evidence; never rewrite the Manifest or old Journal rows.
- preserve a sealed observation for recording-only retry. actual observation and later actual refresh are distinct recorded effects; neither proves full release acceptance.

## Definition of Done

source and implementation have independent acceptance and focused fixture proof; the actual observed state is appended exactly once with verified Git/current/predecessor evidence and no unresolved pending recording; old Journal bytes, the Manifest and installed N are unchanged. CA-P-1780 then owns the fresh authorized admission refresh.

## Pre-execution review

the Operator explicitly approved source-first reconciliation of the current Git-backed state and continuation. independent source review accepts the existing recovered-state schema with D587's exact local witness, avoiding a generic Journal schema extension or attribution of historical writes.
