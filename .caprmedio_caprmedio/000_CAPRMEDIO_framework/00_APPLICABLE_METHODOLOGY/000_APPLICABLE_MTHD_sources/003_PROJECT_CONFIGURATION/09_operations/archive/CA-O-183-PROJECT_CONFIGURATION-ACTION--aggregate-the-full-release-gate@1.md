---
atom_id: CA-O-183
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Aggregate the full Release Gate"
  depends_on: [Action, Test, Docker Image, Framework Package, Journal]
version: 1
updated_at: 2026-10-06 00:00:00 +0400
relations:
  relates_to: [CA-O-164, CA-O-174, CA-O-177, CA-O-182, CA-O-184, CA-R-1525, CA-R-1720]
---
# Summary

Aggregate the full Release Gate

## Action

Aggregate the full Release Gate **means** the read-only decision over the exact closed-unit, image-canary and host Candidate E2E receipts for one frozen N/N+1 candidate.

## Details

Every receipt must name the same candidate manifest, source frontier, compiled output, package, immutable image and parent lineage. Missing, stale, non-pass, mixed-candidate, partial or unjournalable evidence is non-pass. This Action creates no runtime/Skill selection, image removal, retry, Docker effect or new authority.
