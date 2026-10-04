---
atom_id: CA-C-403
content_role: Concern
type: Problem
current_scope_unit: caprmedio
claim_target_scope_unit: METHODOLOGY_SOURCES
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: resolved
subjects:
  governs: "Concurrent committed-state recovery frontier"
  depends_on: [Journal, "Artifact/Revision", Evaluation]
version: 1
updated_at: "2026-10-04 14:18:42 +0000"
relations:
  concern_about: [CA-P-1376]
---
# Summary

Separate committed state recovery from concurrent edits

## Concern

The initial recovered-state Journal preparation for commit4c16aee45 stopped before appending because P1376 had already changed in the working tree. Its correct byte-equality guard prevented falsely claiming that the later working state belonged to that commit.

## Evidences

Root reopened the exact eleven saved Carrier states from that actual commit, excluding concurrent edits, and sealed eleven recovered-state Events. Actual append receipts matched prediction; reopened NDJSON matched all eleven validated Events. The record concerns those committed historical states, not current working bytes or save-Tool completion. The failed attempt appended nothing.

## Blast radius

Only this committed-state Journal recovery. Concurrent review work was preserved. Later changed Carrier states require their own truthful save disposition; no review, source or runtime gate is waived.
