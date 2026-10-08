---
atom_id: CA-D-587
content_role: Delivery
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-06 10:47:48 +0000"
subjects:
  governs: "MCP/Release binding state reconciliation carriers"
  depends_on: [MCP, Manifest, Git, Operator, Journal, Carrier, Source Carrier]
relations:
  delivery_for: [CA-R-1893, CA-M-349]
---
# Summary

Encode the Release binding state observation

## Scope

private observer input/context, canonical Journal evidence and existing pending recording carriers.

## Claim

the observer **must** encode its exact plan and recovered state using the existing canonical Manifest and schema-3 Work Journal carriers, with an exact local predecessor witness and no generic Journal-schema extension.

## Details

1. `release_manifest_reconciliation.py` is private non-dispatching support. its plan, trusted authorization and execute/recovery interfaces do not add a public route or another Workflow.
2. the read-only target is `.caprmedio_caprmedio/_projection/selected_workflow_bindings.json`. the plan seals its reference/raw SHA-256, exact Git HEAD commit/blob, latest target event/revision/SHA-256, next revision and source frontier. the trusted context also binds registered Operator, Journal author and actual session.
3. output is `event: recovered`, `kind: governed_project_state`, `schema_version: 3`, with positive result/carrier revision `predecessor_version + 1`. `recovery_evidence` contains only `git` and `carrier`.
4. Git evidence contains exact committed input proof. carrier evidence has exactly `identity`, `kind`, `filename`, `version`, `sha256`, `predecessor_event_id`, `predecessor_version`, and `predecessor_sha256`. the predecessor fields are observation witnesses, not a fabricated historical change edge. no top-level `previous_result_event`, `action_type` or `sources` is added to this state event.
5. use the configured single `_journal/` root and existing runtime pending/receipt support. observation pending IDs have their own unambiguous prefix, exact sealed plan/event/context and no Manifest effect references. hold the existing `release-manifest-carrier:<reference>` lock; do not create another lock or ledger.
6. execute results distinguish observed/already-recorded, blocked and recording-required states and retain exact event/receipt or pending references. exact retry returns the original event and timestamp. a successor refresh's normal completed change carries `previous_result_event` pointing to this recovered state.
7. source carriers, historical Journal lines, the Manifest, selectors, packages, Skills, images and queues are not mutable observer targets.
