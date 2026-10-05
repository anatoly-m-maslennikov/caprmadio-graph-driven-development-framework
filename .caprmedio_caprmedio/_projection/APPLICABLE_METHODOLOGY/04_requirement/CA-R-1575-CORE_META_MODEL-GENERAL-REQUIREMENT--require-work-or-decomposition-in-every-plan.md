---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Content Role: Plan/Type: Plan/Decomposition"
    - "Atom/Summary"
    - "Atom/Claim"
version: 4
updated_at: "2026-10-03 00:22:56 +0400"
relations: {"relates_to": ["CA-R-1574", "CA-R-1579"]}
atom_id: "CA-R-1575"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1575-CORE_META_MODEL-GENERAL-REQUIREMENT--require-work-or-decomposition-in-every-plan.md
  source_atom_id: CA-R-1575
  source_atom_revision: 4
  source_sha256: 8c4d635ae8957bc19b7d55f483d09dc04669ca3b6b9685f17624c1673069de57
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Require work or decomposition in every Plan

## Scope

Plan Atoms and their work or decomposition.

## Claim

**every** Plan Atom **must** have **`>=1`** of:

- its own work content;
- **`>0`** outgoing `DECOMPOSES_INTO` Relations **to** other Plan Atoms.

both contributions **may** be present within the same Claim; a Summary alone **without** either contribution is insufficient.

## Details
