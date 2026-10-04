---
atom_id: CA-E-549
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 19:29:30 +0000"
subjects:
  governs: "Tool/PROJECT_STRUCTURE golden successful cases"
  depends_on: [Tool, Scope Unit, Project Structure, Workflow, Action, Journal]
relations:
  relates_to: [CA-R-1662, CA-R-1829, CA-R-1830, CA-R-1831, CA-R-1832]
---
# Summary

Complete authorized Scope Unit Create, Rename, and Move

## Scope

Golden functional cases against a disposable project with declared TOML authority and independently observed implementation paths.

## Claim

The Evaluation **must** prove an authorized Create, Rename, and Move produce the expected tree and repaired reference sets through the real workflow boundary.

## Details

- Create an Ordered unit with a valid unique sibling `local_order`; Rename it and Move it under a valid parent.
- Assert authoritative TOML changes, distinct authority/delivery paths, cycle-free declarations, repaired incoming references/parent-owned attachments, reported Carrier observations, and exact result revisions.
- Assert no unrelated Carrier is deleted, all required Workflow/Action result references are returned where execution occurred, and shared Journal evidence is inspected through its existing contract.
