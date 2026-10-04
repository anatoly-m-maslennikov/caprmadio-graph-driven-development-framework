---
subjects:
  governs: "Extension"
  depends_on:
    - "Core Meta-Model"
    - "Journal"
    - "Projection"
    - "Project Configuration"
version: 5
updated_at: "2026-10-02 23:17:53 +0400"
relations: {}
atom_id: "CA-R-1466"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1466-CORE_META_MODEL-CORE--keep-git-integration-in-an-extension.md
---
# Summary

Keep Git integration in an Extension

## Scope

Git integration in the Core Meta-Model.

## Claim

Git integration **must** be optional Extension authority, **not** a prerequisite of the Core Meta-Model. Git commit policies, commit-message encodings, hooks, **and** event-to-commit references belong **to** that Extension; selecting it **must not** replace the authoritative Journal **or** make Git history an independent source for the same recorded facts. the Core Meta-Model **must** remain applicable **without** Git integration.

## Details
