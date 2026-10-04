---
subjects:
  governs: "principles"
  depends_on: []
version: 24
updated_at: "2026-10-03 02:10:09 +0400"
relations:
  child_of:
    - CA-M-001
    - CA-M-261
atom_id: "CA-R-1696"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1696-CORE_META_MODEL-CORE-REQUIREMENT--keep-the-core-meta-model-implementation-neutral.md
---
# Summary

Keep the Core Meta-Model implementation neutral

## Scope

CORE_META_MODEL authority and its reusable model invariants and expansion boundaries.

## Claim

CORE_META_MODEL authority **must** define reusable model invariants **and** expansion boundaries **without** hidden dependence on a programming language, LLM provider **or** model, agent host, operating system, repository host, package manager, database, deployment platform, **or** other replaceable implementation mechanism.

mechanism-specific obligations belong **to** the Scope that owns the mechanism. Extensions **and** PROJECT_CONFIGURATION **may** expand the model for their bounded use **without** rewriting its governing Claims.

CORE_META_MODEL **may** name a mechanism **only** **when** the mechanism itself is the explicit Entity governed by the Claim, such as a Carrier format, portability boundary, **or** external constraint; this reference **must not** make that mechanism a hidden prerequisite of unrelated model Claims.

## Details
