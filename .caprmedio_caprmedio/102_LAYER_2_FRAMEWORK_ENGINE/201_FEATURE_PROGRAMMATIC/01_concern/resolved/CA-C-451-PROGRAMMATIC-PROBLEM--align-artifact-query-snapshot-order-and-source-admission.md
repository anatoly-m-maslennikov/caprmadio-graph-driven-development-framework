---
atom_id: CA-C-451
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: resolved
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-05 02:06:04 +0000"
subjects:
  governs: "Artifact query snapshot order and source admission"
  depends_on: [Tool, Workflow, Action, Journal, Evaluation]
relations:
  concern_about: [CA-O-158, CA-P-1611, CA-P-1527, CA-P-1528]
---
# Summary

Align Artifact query snapshot order and source admission

## Concern

The Artifact query snapshot-order and source-admission defect is resolved in the accepted current source and its route binding. This resolution does not assert actual fresh-image, queue or MCP execution.

## Evidences

P1611 independently rejected O158@3, hash abe5ae697b49f9bd67c10261456fff398a97e0a6900d814aa4a06777b3f21e0f. Its actual admitted Run wording says the Artifact source snapshot is sealed first. selected_execution starts Workflow/Step/Action Runs before query_actions.artifact_query_action invokes the pure Tool and captures the Artifact snapshot. R1849@3/M330@3/D551@4 retain coherent pure Tool/shared recording boundaries. Current selected route validation intentionally still pins P1532 and O158@2; it rejects O158@3 until fresh source acceptance and subsequent rebind.

## Blast radius

P1527 now has current revised Artifact source and binding acceptance. Actual query consumer execution remains separately gated by P1604 and fresh-image proof by P1528 under C449; C447 remains its denied-migration blocker. Preserve P1532 as historical acceptance. No denied-operation retry, environment workaround or runtime pass is asserted here.

## Resolution

CA-P-1617 corrected O158 to version 4: admitted Workflow/Step/Action Run starts precede the pure Artifact query snapshot capture; continuation and results retain that sealed snapshot, while shared recording stays outside the Tool result. CA-P-1618@1 independently accepted the eight-source current packet, including O158@4. CA-P-1619@1 records the W14 validator, manifest and regression-test rebind to that acceptance. Independent review accepted the minimal rebind; eight focused development-worker tests passed. Commits 88405e40e and 4d1b6d254 preserve the source correction and binding. These are source/binding and development-test receipts, not actual current-image or queue/MCP proof.
