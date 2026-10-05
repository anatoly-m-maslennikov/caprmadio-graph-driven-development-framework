---
atom_id: CA-P-1677
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
  governs: "Implement target-bound Draft history"
  depends_on: [Atom, Carrier, History, Tool, Evaluation, Journal]
version: 1
updated_at: "2026-10-05 04:41:02 +0000"
relations:
  is_decomposition_of: [CA-P-1662]
  blocks: [CA-P-1638]
---
# Summary

Implement target-bound Draft history

## Objective

Within <=15 minutes, implement target-bound Draft history.

## Details

After accepted P1676, implement only the existing Create/Demotion/Draft Update/Promotion lineage handoff in atom_operations.py and lifecycle_intents.py, with focused golden corpus additions. Preserve all external changes. The retained history entry must bind the actual current target path/bytes and direct origin; mutable caller/carrier fields alone must not select another identity. Cover both actual P1638 forgeries, ordinary create/demote/update/promote, changed Summary, missing/stale history and no-effect refusals. Existing development worker only. No shared route, source, manifest, environment/image or C447/C449 bypass.

Choose the best authorized in-scope option when uncertain; record C/Question and continue. One Task, one Agent. You are not alone: preserve all other work. No broad harvesting, source campaign or denied-operation workaround.

## Definition of Done

Save exact source/code hashes, the actual bounded result, genuine evidence and remaining coverage. A rejected review or partial test does not close the parent or mandatory runtime gates.
