---
atom_id: CA-P-1699
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
  governs: "Validate Draft Update head before writing"
  depends_on: [Atom, Carrier, History, Tool, Evaluation]
version: 1
updated_at: "2026-10-05 06:38:35 +0000"
relations:
  is_decomposition_of: [CA-P-1685]
  blocks: [CA-P-1638]
---
# Summary

Validate Draft Update head before writing

## Objective

Within <=10 minutes, validate the current Draft head before any Update effect.

## Details

Own only lifecycle_intents.py and tests/test_draft_promotion_golden.py. The current native review rejects the Update path because it loads an unrelated supplied parent without validating that parent against the actual current Draft. Call the supported unique current-head validator before reserving or writing; only its validated result may parent the update. Reject unrelated valid head substitution, stale same-path replay and mismatching current bytes with no Project changes. Preserve successful Create/Update/demotion/promotion/recovery and shared changed-carrier behavior. Golden first, then actual designated-worker focused tests; no source/Plans/Git/real-project/image changes or C447/C449 workaround.

## Definition of Done

Actual substitution/replay unchanged-tree regressions and existing native/status cases pass with exact hashes, permitting the required narrow independent re-review.
