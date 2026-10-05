---
subjects:
  governs: "Compatible Lineage Impact Disposition"
  depends_on:
    - "atom-boundary"
    - "relation-model"
version: 15
updated_at: "2026-10-02 21:16:45 +0400"
relations: {}
atom_id: "CA-R-1033"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1033-CORE_META_MODEL-GENERAL--define-compatible-lineage-impact-disposition.md
  source_atom_id: CA-R-1033
  source_atom_revision: 15
  source_sha256: 434d199f97e943b1841e95d441397aa3352433b7ceb6b7ae88c4b1b4fec3a738
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define compatible Lineage Impact disposition

## Scope

`compatible` Lineage Impact dispositions.

## Claim

`compatible` **means** the child remains valid against the parent Revision required by the gate **and** traversal stops on that branch **without** a child update. **if** the gate requires the revised parent, **then** compatibility **must** be established against that new Revision; permission **to** consume a pinned earlier Revision **must not** establish compatibility for a gate that requires the new Revision.

## Details
