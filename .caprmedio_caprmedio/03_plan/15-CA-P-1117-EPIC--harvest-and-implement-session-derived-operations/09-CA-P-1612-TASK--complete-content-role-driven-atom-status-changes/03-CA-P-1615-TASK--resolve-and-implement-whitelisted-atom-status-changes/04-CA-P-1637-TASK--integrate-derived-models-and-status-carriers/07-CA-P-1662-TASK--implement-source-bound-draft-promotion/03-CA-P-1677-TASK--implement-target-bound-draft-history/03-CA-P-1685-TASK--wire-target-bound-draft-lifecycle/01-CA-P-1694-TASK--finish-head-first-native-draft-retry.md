---
atom_id: CA-P-1694
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
subjects:
  governs: "Finish head-first native Draft retry"
  depends_on: [Atom, Tool, Manifest, Evaluation, Workflow]
version: 1
updated_at: "2026-10-05 06:06:00 +0000"
relations:
  is_decomposition_of: [CA-P-1685]
  blocks: [CA-P-1638]
---
# Summary

Finish head-first native Draft retry

## Objective

Within <=15 minutes, finish head-first native Draft retry.

## Details

Own only atom_operations.py, lifecycle_intents.py and tests/test_draft_promotion_golden.py. Current Create/Update/demotion history wiring exists, but promotion selects an ID before pending lookup. Resolve the trusted retained head first; exact pending request/head/output bindings decide recovery before fresh allocation or output preparation. Same-transition retries after partial output/finalization or old-Draft removal must reuse the one identity/output; changed requests and origin substitutions refuse. Add actual native regression cases rather than repeating the existing five happy/refusal tests. Use accepted P1690 lookup/recovery APIs without reading private files. Preserve external baseline and all other edits. Disposable dev-worker tests only, no real-repository effects, Git/source/Plan/image or C447/C449 workarounds.

## Definition of Done

The exact targeted saved effects/refusals and focused cases pass with code/test hashes. Required parent integration and image proof remain separate.
