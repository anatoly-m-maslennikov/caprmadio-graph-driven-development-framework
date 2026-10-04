---
atom_id: CA-E-542
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 22:39:38 +0400"
subjects:
  governs: "WORKFLOW_OPERATIONS/RUN_SUPPORT/Run provenance"
  depends_on: [Workflow, Step, Action, Initiative, Journal, Evaluation]
relations:
  evaluation_for: [CA-R-1822]
---
# Summary

Verify selected Run identities, revisions and lineage

## Scope

Canonical selected-Run evidence for actual nested and standalone invocation.

## Claim

Every actual selected Run remains reconstructable with its distinct identity,
exact definition revisions, and real lineage.

## Test case

Execute one selected Workflow containing two Actions with one nested/handoff
edge, then one standalone read-only Action. Capture start and terminal events,
definition bindings, Initiative/action identities, and reconstructed Process
Log view.

## Acceptance criteria

- The Workflow, every actual Step, and every Action have distinct Run
  identities and exact admitted definition ID/Version/path/digest bindings.
- Nested evidence names only actual parents and predecessors/successors.
  Ending one Run neither creates nor implies successor authorization.
- The standalone Action has no fictitious Workflow/Step parent, and recovery or
  duplicate report delivery adds no new Run.
- The reconstructed view references canonical event identities and retains the
  same Initiative without replacing it by session, queue, or adapter identity.

## Details

The fixture must use exact captured source revisions, not reconstructed current
definitions, so it can distinguish preserved bindings from later source drift.
The checked assertion is the Claim above.

## Failure disposition

Reject collapsed identities, missing revisions, invented parents, or a view
that cannot reconstruct the captured canonical evidence.
