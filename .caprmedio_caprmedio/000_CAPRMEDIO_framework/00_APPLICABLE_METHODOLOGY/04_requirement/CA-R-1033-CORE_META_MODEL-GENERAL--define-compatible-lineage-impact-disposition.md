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
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1033-CORE_META_MODEL-GENERAL--define-compatible-lineage-impact-disposition.md
---
# Summary

Define compatible Lineage Impact disposition

## Scope

`compatible` Lineage Impact dispositions.

## Claim

`compatible` **means** the child remains valid against the parent Revision required by the gate **and** traversal stops on that branch **without** a child update. **if** the gate requires the revised parent, **then** compatibility **must** be established against that new Revision; permission **to** consume a pinned earlier Revision **must not** establish compatibility for a gate that requires the new Revision.

## Details
