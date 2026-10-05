---
subjects:
  governs: "Implementation Binding"
  depends_on:
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Implementation"
    - "Atom/Claim"
version: 5
updated_at: "2026-10-02 23:35:16 +0400"
relations: {}
atom_id: "CA-R-1504"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1504-CORE_META_MODEL-CORE-REQUIREMENT--keep-evaluation-implementation-coverage-explicit.md
  source_atom_id: CA-R-1504
  source_atom_revision: 5
  source_sha256: 036ff4c6b8e0ef57df3b74a1f009dd5ed0850c613e1ab2919d3d66aee2b3337f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Keep Evaluation implementation coverage explicit

## Scope

coverage between Evaluation Atoms and their implementation realizations.

## Claim

coverage between Evaluation Atoms **and** their realizations **may** be many-to-many **only** with explicit attribution:

- **`=1`** Evaluation Atom **may** be realized by multiple distinct implementations.
- **`=1`** implementation **may** realize multiple Evaluation Atoms **only** **when** its result remains attributable **to** **every** covered Claim.

## Details

a shared implementation **must not** make its covered Claims **or** their result attribution implicit. this Claim governs coverage, **not** a new Carrier **or** a second implementation registry.
