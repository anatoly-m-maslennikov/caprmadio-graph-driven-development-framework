---
atom_id: CA-O-181
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Run host-capable Candidate E2E"
  depends_on: [Action, Test, Docker Image, Framework Package, Journal, Operator]
version: 1
updated_at: 2026-10-06 00:00:00 +0400
relations:
  relates_to: [CA-O-164, CA-O-177, CA-O-182, CA-R-1525, CA-R-1720]
---
# Summary

Run host-capable Candidate E2E

## Action

Run host-capable Candidate E2E **means** one explicitly authorized host-capable controller execution against CA-O-177's exact candidate image, package, source frontier and N/N+1 bindings.

## Details

The frozen Docker worker has no Docker socket and cannot claim this phase. A registered explicit host-capable controller and its exact declared capability are required; missing, denied, unsafe, unavailable, stale, non-passing or unjournalable capability yields its actual non-pass outcome. This Action never selects N+1, promotes, retires, mutates sources, expands mounts, exposes credentials or substitutes a cached/focused result. It records one recoverable Journal result bound to the exact candidate and image identity.
