---
subjects:
  governs: "relation-model"
  depends_on:
    - "atom-boundary"
version: 20
updated_at: "2026-10-03 01:23:33 +0400"
relations:
  {}
atom_id: "CA-R-1632"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Classify lineage impact with four dispositions

## Scope

directly dependent children reached by the Impact Review after an Atom receives a new accepted Revision.

## Claim

**when** an Atom receives a new accepted Revision, **every** directly dependent child reached by the Impact Review **must** receive **`=1`** disposition from (`compatible`, `update_required`, `replacement_required`, `uncertain`).

## Details
