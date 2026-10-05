---
atom_id: CA-P-1641
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
status: Active
subjects:
  governs: "Stage complete Framework package"
  depends_on: [Workflow, Action, Tool, Manifest, Methodology, Implementation, Skill, Evaluation, Journal]
version: 1
updated_at: "2026-10-05 02:43:50 +0000"
relations:
  is_decomposition_of: [CA-P-1623]
  blocks: [CA-P-1643]
---
# Summary

Stage complete Framework package

## Objective

Within <=15 minutes, stage complete Framework package.

## Details

Own new RELEASE_VERSION/release_packaging.py and its dedicated tests only: candidate non-active full Framework package under D562 content-addressed release root, complete Engine/Methodology/ca resources, manifest verification, collision/idempotency and source/selector preservation. Explicit staging only; no current.toml promotion, public Skill change, image/test gate manufacture or actual release invocation.

Inputs are P1622 accepted source/RMED pins: O164–179@1, R1876–1880@1, M331–333@1, E571–574@1, D560–564@1. D561/E572 are the repaired accepted pins, not their rejected predecessors. Preserve external dirt and designated C447/C449 boundaries; existing development worker tests are not fresh-image proof.

## Definition of Done

Save exact bounded output and test/remaining-coverage evidence. Pure preparation, staging or source review never establishes release promotion, complete P1623, P1624 or Epic closure.

