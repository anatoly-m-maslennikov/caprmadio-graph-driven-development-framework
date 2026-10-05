---
subjects:
  governs: "Atom/Claim"
  depends_on:
    - "Atom"
    - "Atom/Content Role: Evaluation"
    - "Scope Unit"
    - "Atom/Claim/Target Scope Unit"
version: 9
updated_at: "2026-10-01 21:31:46 +0400"
relations: {}
atom_id: "CA-E-461"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation Approach"
global_tier: 10
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-461-CORE_META_MODEL-GENERAL-EVALUATION_APPROACH--warn-about-selected-sibling-claim-boundaries.md
  source_atom_id: CA-E-461
  source_atom_revision: 9
  source_sha256: cd79da801ab754642cd976ad09a973a6f08112927b042130ccd6795870ee2788
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Warn About Selected-sibling Claim Boundaries

## Scope

an Atom Claim concerning **only** selected sibling Scope Units.

## Claim

**when** **`=1`** Atom Claim concerns **only** **`>=2`** selected sibling Scope Units **and** does **not** apply **to** their containing Scope Unit as a whole, the Evaluation **must** report a non-blocking boundary warning for review; that restriction alone **must not** make the Atom invalid **or** trigger automatic rejection, splitting, **or** retargeting **to** their parent.

## Details
