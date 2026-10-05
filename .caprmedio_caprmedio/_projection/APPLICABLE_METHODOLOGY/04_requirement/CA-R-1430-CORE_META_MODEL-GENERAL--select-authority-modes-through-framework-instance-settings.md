---
subjects:
  governs: "Framework Instance Settings/Authority Modes"
  depends_on:
    - "Framework Instance Settings"
    - "Project Structure"
    - "Authority Mode"
    - "Project"
    - "Scope Unit"
    - "Atom"
version: 8
updated_at: "2026-10-02 22:59:46 +0400"
relations:
  child_of:
    - "CA-R-1402"
  relates_to:
    - "CA-M-279"
atom_id: "CA-R-1430"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1430-CORE_META_MODEL-GENERAL--select-authority-modes-through-framework-instance-settings.md
  source_atom_id: CA-R-1430
  source_atom_revision: 8
  source_sha256: ec9d8b3f6d6aa35d43101e4d7d6d405413778d4bc05d15cce92975ae6356d263
  original_relations_sha256: be5cc3030b7779b3445d3df040c85d6952a487441c36cfe1927e563974c04f18
---
# Summary

Select Authority Modes through Framework Instance Settings

## Scope

the selection **and** overrides of Authority Modes through Framework Instance Settings.

## Claim

Framework Instance Settings **must** select the Project Authority Mode **and** default Scope Unit Authority Mode. a Scope Unit's explicit Authority Mode override **must** be owned **only** by its Project Structure declaration; an omitted override uses the effective Framework Instance setting **without** becoming an authored per-unit value. permitted values are `strict` **and** `casual`; neither changes the authority of active Atoms.

## Details
