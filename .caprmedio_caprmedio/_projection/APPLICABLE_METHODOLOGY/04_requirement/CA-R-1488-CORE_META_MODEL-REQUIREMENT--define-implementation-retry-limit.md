---
version: 6
updated_at: "2026-10-02 23:35:16 +0400"
relations: {}
subjects:
  governs: "Implementation Retry Limit"
  depends_on:
    - "Workflow Run"
    - "Implementation Workflow"
    - "Implementation Retry Control"
    - "Atom/Content Role: Evaluation"
atom_id: "CA-R-1488"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1488-CORE_META_MODEL-REQUIREMENT--define-implementation-retry-limit.md
  source_atom_id: CA-R-1488
  source_atom_revision: 6
  source_sha256: bb0cf786c7048e414a4f9bed02714f906c6828d7969544bb68c3be042a16ca81
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Implementation Retry Limit

## Scope

Implementation Retry Limit values in an Implementation Workflow Run.

## Claim

Implementation Retry Limit **means** the maximum number of additional fix-and-evaluate rounds permitted **after** the initial failed Evaluation **in** one Implementation Workflow Run.

- its value **must** be an integer **`>=0`**.
- a value **`=0`** permits no retry **after** the initial failure.
- the limit does **not** grant permission **to** repair, change authority, **or** bypass an applicable confidence threshold.

## Details
