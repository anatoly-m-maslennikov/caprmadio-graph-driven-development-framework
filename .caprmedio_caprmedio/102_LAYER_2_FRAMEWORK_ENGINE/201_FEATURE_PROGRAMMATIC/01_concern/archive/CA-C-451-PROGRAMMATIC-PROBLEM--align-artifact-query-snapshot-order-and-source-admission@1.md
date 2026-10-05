---
atom_id: CA-C-451
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 01:10:50 +0000"
subjects:
  governs: "Artifact query snapshot order and source admission"
  depends_on: [Tool, Workflow, Action, Journal, Evaluation]
relations:
  concern_about: [CA-O-158, CA-P-1611, CA-P-1527, CA-P-1528]
---
# Summary

Align Artifact query snapshot order and source admission

## Concern

The revised Artifact query source packet remains unadmitted. Its Workflow still states an Artifact snapshot/Run order that does not match current execution; the old accepted route pins cannot attest revised source bytes.

## Evidences

P1611 independently rejected O158@3, hash abe5ae697b49f9bd67c10261456fff398a97e0a6900d814aa4a06777b3f21e0f. Its actual admitted Run wording says the Artifact source snapshot is sealed first. selected_execution starts Workflow/Step/Action Runs before query_actions.artifact_query_action invokes the pure Tool and captures the Artifact snapshot. R1849@3/M330@3/D551@4 retain coherent pure Tool/shared recording boundaries. Current selected route validation intentionally still pins P1532 and O158@2; it rejects O158@3 until fresh source acceptance and subsequent rebind.

## Blast radius

P1527 cannot claim current revised Artifact source dispatch acceptance, and P1528 remains unfinished. Resolve the source-order statement or implementation ordering without weakening snapshot isolation, obtain fresh independent acceptance, then rebind current selected sources. Preserve P1532 as old acceptance. Do not retry C447's denied migration, work around C449's host environment or treat successful discovery as Workflow execution. This issue is separate from the resolved live discovery failure.
