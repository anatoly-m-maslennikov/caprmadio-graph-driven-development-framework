---
atom_id: CA-P-1697
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
subjects:
  governs: "Complete exact prior-image retirement"
  depends_on: [Tool, Image, Manifest, Runtime, Evaluation]
version: 1
updated_at: "2026-10-05 06:07:49 +0000"
relations:
  is_decomposition_of: [CA-P-1691]
  blocks: [CA-P-1644]
---
# Summary

Complete exact prior-image retirement

## Objective

After P1693, complete exact prior-image retirement within <=15 minutes.

## Details

Own only release_image.py and tests/test_release_image.py. Consume actual observed promotion evidence, current matching N+1 selector and actual immutable prior-image identity. Independently observe all retaining containers and required rollback references before exact removal; unknown or retained identity yields truthful retained/pending result. Do not accept caller flags, mutable tags, broad prune or force. Golden-first fake execution only; no actual image/container operation or C449 workaround. Preserve the already accepted build/verification API and other Agents' work.

## Definition of Done

Save exact code/test hashes and actual focused case outcomes, distinguishing mock evidence from actual image execution. Parent and actual release gates remain separate.
