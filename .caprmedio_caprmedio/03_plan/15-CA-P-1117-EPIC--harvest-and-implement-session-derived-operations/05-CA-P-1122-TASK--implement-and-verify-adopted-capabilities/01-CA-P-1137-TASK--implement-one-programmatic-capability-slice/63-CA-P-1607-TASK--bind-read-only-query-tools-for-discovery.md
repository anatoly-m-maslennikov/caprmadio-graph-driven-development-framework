---
atom_id: CA-P-1607
content_role: Plan
type: Plan
label: Task
work_sequence_number: 63
current_scope_unit: caprmedio
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: "Bind read-only query Tools for discovery"
  depends_on: [Tool, Workflow, Action, MCP, Evaluation, Projection]
version: 1
updated_at: "2026-10-05 00:54:40 +0000"
relations:
  is_decomposition_of: [CA-P-1137]
  blocks: [CA-P-1527, CA-P-1528]
---
# Summary

Bind read-only query Tools for discovery

## Objective

Within <=15 minutes, add explicit discovery bindings for the two existing read-only query Tools in their Delivery authority and update affected selected-route source pins. Own CA-D-551, CA-D-557, exact prior Revision archives and necessary current manifest pins only.

## Details

One independently owned Task. Preserve concurrent edits. Root saves the truthful result and validated mechanical commit. C447 and C449 remain distinct protected blockers. No FPF, harvesting, denied-operation retry or broad audit.

## Definition of Done

Existing entrypoints and Workflow/Action IDs are bound without claiming unregistered MCP names. Current source discovery finds the two Tools, and any dependent source-pin change is verified separately. No immutable-image pass is inferred.

## Result

Done: CA-D-551@3 and CA-D-557@2 carry explicit bindings for existing FIND_AND_FETCH_ARTIFACTS and FIND_AND_FETCH_JOURNAL_EVENTS entrypoints, Action IDs CA-O-159/CA-O-162, Workflow IDs CA-O-158/CA-O-161 and actual registered MCP names. Exact predecessor archives retain D551@2 and D557@1 bytes; Summaries and IDs are unchanged. No selected manifest edit was required because its execution pins bind Workflow/Step/Action/frontier sources, not these discovery-only additions.

Independent source review ACCEPTED the bounded discovery additions, not atom-wide re-acceptance of inherited placement text. Current CA-O-158's D551@2 execution pin remains unchanged. Focused development/source catalog tests pass 9/9 and selected manifest tests pass 12/12. The initial injected-exposure catalog assertion is not actual live MCP availability; P1609 separately repairs actual registered exposure and tests the real stdio server. No image or client-cache acceptance follows.

The reviewer noted inherited D551 direct-import wording does not match the pure query entrypoint; that separate wording must be adjudicated without invalidating or broadening this discovery acceptance.
