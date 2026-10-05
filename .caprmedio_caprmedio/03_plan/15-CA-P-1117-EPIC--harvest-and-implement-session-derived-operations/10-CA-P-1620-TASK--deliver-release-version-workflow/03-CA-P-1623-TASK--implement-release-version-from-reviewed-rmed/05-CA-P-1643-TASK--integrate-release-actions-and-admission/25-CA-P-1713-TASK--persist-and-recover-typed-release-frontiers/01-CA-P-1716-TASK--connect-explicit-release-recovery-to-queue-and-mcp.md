---
atom_id: CA-P-1716
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
version: 1
updated_at: "2026-10-05 13:27:20 +0000"
subjects:
  governs: "Explicit Release recovery delivery"
  depends_on: [Workflow, Action, Implementation, Evaluation, Journal, Manifest, Permission]
relations:
  is_decomposition_of: [CA-P-1713]
  blocks: [CA-P-1624]
---
# Summary

Connect explicit Release recovery to queue and MCP

## Objective

Deliver the typed public and durable-queue path to the existing frozen Release recovery implementation.

## Details

1. review CA-R-1883, CA-M-340, CA-E-583 and CA-D-577 before implementation.
2. admit only the existing frozen Release Run through the closed recovery request. Ordinary enqueue and redispatch never become recovery.
3. preserve the canonical Run identity and exact sealed request, source, approval, permission, checkpoint and Journal bindings. Scheduler transport identity is not a second canonical Run.
4. recover exact pending recording through the shared writer; leave uncertain/in-progress effects blocked and never replay them.
5. test request rejection before queue admission, source/permission staleness, exact worker delegation and truthful observation without inventing starts or terminal evidence.
6. the bounded implementation/review estimate is <=15 minutes; decompose further if actual remaining work exceeds that bound.

## Definition of Done

Reviewed source, strict CLI/MCP/queue boundaries and focused tests connect an explicit admitted recovery request to the existing private recovery method. Normal selected execution remains unchanged. Live queue/MCP recovery and canonical Journal proof are required separately before full Release closure.
