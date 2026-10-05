---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Blocking"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Content Role: Plan/Type: Plan/Status: Done"
    - "Atom/Content Role: Plan/Type: Plan/Decomposition"
    - "Atom/Content Role: Plan/Type: Plan/Work Sequence Number"
    - "Hub Atom"
version: 5
updated_at: "2026-10-02 20:16:06 +0400"
relations: {"evaluation_for": ["CA-R-1580", "CA-R-1583", "CA-R-1592", "CA-D-471", "CA-D-481"]}
atom_id: "CA-E-504"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-504-CORE_META_MODEL-QA_CASE--validate-plan-blocking-and-parallel-readiness.md
  source_atom_id: CA-E-504
  source_atom_revision: 5
  source_sha256: c2f9b7d5ffcaea593698480c7c8ad7d4d4d2b90fb0395e9a09680f468f115894
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Validate Plan blocking and parallel readiness

## Scope

Plan blocking **and** parallel readiness.

## Claim

the blocking Evaluation **must** reject a start **unless** **all** explicit blockers are Done **and** the applicable execution permissions hold.

## Details

- `A BLOCKS B`, `B BLOCKS C`: permit `A`, **then** `B`, **then** `C` **only** **after** the preceding Plan is Done.
- `A BLOCKS C`, `B BLOCKS C`: allow `A` **and** `B` **to** be ready concurrently; `C` waits for both.
- reorder leading navigation numbers **or** give two Plans the same Hub: do **not** invent another blocking edge.
- reject a self-edge, cycle, unresolved **or** non-Plan target, duplicate direct declaration, inverse declaration, **or** Plan scheduling encoded as `depends_on`.
- accept a Done blocker; Backlog, Active, Canceled, **and** Archived **must not** satisfy its completion gate.
- combine decomposition completion dependencies with blocking for deadlock detection: **if** Hub `H` decomposes **into** `A` **and** `H BLOCKS A`, reject the unsatisfiable cycle even though the blocking graph alone is acyclic.
- distinguish readiness from forced execution: a deterministic display order does **not** prohibit concurrent independent work **or** grant execution authority.

report the failing endpoints **and**, for a cycle, its complete prerequisite chain.
