---
subjects:
  governs: "Atom/Local Tier"
  depends_on:
    - "Change Content Roles"
    - "Atom/Content Role: Implementation"
    - "Atom"
    - "Atom/Local Tier: Standard"
version: 5
updated_at: "2026-10-01 21:44:50 +0400"
relations: {"relates_to": ["CA-R-1549", "CA-R-1343", "CA-R-660"]}
atom_id: "CA-R-1566"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1566-CORE_META_MODEL-GENERAL-REQUIREMENT--keep-change-and-implementation-content-at-standard.md
  source_atom_id: CA-R-1566
  source_atom_revision: 5
  source_sha256: cc61247d4acc05e59d324f07457582d6f98e11280b75f91799b57d7aea365039
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Keep Change **and** Implementation content at Standard

## Scope

Atoms whose Content Role is Concern, Analysis, Plan, Operations, **or** Implementation.

## Claim

an Atom whose Content Role is **in** (Concern, Analysis, Plan, Operations, Implementation) **must** resolve **to** Local Tier Standard.

- an omitted filename tier token denotes Standard, **not** the absence of the internally carried Local Tier; persistence, reuse, importance, **or** nesting does **not** promote that content **to** Core **or** General.
- the RMED Atoms specifying that content retain their own Local Tiers; the content does **not** inherit its specification's tier.

## Details
