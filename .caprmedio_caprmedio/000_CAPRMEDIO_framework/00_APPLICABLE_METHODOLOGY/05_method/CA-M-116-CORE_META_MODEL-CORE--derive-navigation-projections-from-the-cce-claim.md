---
subjects:
  governs: "Atom Claim Projection"
  depends_on:
    - "Atom/Claim"
    - "Atom/Summary"
    - "Translation"
version: 14
updated_at: "2026-10-02 20:25:13 +0400"
relations:
  relates_to:
    - CA-M-294
atom_id: "CA-M-116"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-116-CORE_META_MODEL-CORE--derive-navigation-projections-from-the-cce-claim.md
  source_atom_id: CA-M-116
  source_atom_revision: 14
  source_sha256: e0eff5e7fcfbe3a2384f00b3a195829e49136e5ecbda2a929e5cc6ff83d4a22d
  original_relations_sha256: 9bf67064015f173c315f553cfdea41bbcb9767069ed6dd9a11f2fb394a1a9d88
---
# Summary

Derive navigation Projections from the CCE Claim

## Scope

navigation values derived from an Atom Claim.

## Claim

**to** derive navigation values from an Atom Claim, the Generator **must** derive the concise human-readable Summary **when** creating the Atom **and** derive requested Translations directly from the Claim, **without** adding authoritative meaning. choose wording under CA-M-294-CORE_META_MODEL-METHOD--use-simpler-words-without-losing-meaning. for an existing Atom identity, retain **and** check the Summary under CA-R-1273-CORE_META_MODEL-CORE-REQUIREMENT--keep-summary-source-faithful **and** CA-R-1464-CORE_META_MODEL-REQUIREMENT--keep-summary-fixed-for-atom-identity rather than regenerating it as an independent Projection.

## Details
