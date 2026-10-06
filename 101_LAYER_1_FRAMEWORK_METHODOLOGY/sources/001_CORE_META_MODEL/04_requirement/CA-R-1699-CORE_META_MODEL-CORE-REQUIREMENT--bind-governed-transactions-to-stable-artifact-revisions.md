---
subjects:
  governs: "lifecycle-traceability"
  depends_on: []
version: 22
updated_at: "2026-10-03 02:14:48 +0400"
relations:
  child_of:
    - CA-E-002
atom_id: "CA-R-1699"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Bind governed transactions to stable artifact revisions

## Scope

governed changes.

## Claim

**every** governed change forms one directed provenance transaction from exact parent Artifact revisions **to** the governed Artifacts **or** native targets created **or** revised by that change.

## Details
