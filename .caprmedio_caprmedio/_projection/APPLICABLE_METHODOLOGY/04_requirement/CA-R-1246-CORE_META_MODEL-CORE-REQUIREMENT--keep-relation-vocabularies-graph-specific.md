---
subjects:
  governs: "Relation Kind"
  depends_on:
    - "CAPRMEDIO Graph"
    - "Applicable Methodology"
    - "Projection"
    - "Relation Kind/Metadata"
version: 11
updated_at: "2026-10-02 21:35:09 +0400"
relations: {}
atom_id: "CA-R-1246"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1246-CORE_META_MODEL-CORE-REQUIREMENT--keep-relation-vocabularies-graph-specific.md
  source_atom_id: CA-R-1246
  source_atom_revision: 11
  source_sha256: 79e1932957ce002ac47ff529f5fb56a1311ebc5bbc07ac85482021ce5b19d4c3
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Keep relation vocabularies graph-specific

## Scope

Relation Kinds and their graph-qualified identities in CAPRMEDIO Graphs.

## Claim

**every** Relation Kind **must** belong **to** **`=1`** kind of CAPRMEDIO Graph **and** be admitted as native **only** **in** instances of that graph kind. instances of the same graph kind governed by the same Applicable Methodology **must** reuse the same Relation Kind authority.

the owning graph kind **and** canonical name **must** determine the Relation Kind's graph-qualified identity. matching names **or** compatible endpoints **must not** make Relation Kinds from different graph kinds interchangeable.

the owning graph kind determines a Relation Kind's authority, **not** a requirement that **all** endpoints occupy the same graph. admitted cross-graph endpoints **and** source references under CA-R-1472 retain that graph-qualified ownership. another graph **may** represent a source-traceable reference **or** view of the Relation **without** registering it as native.

## Details
