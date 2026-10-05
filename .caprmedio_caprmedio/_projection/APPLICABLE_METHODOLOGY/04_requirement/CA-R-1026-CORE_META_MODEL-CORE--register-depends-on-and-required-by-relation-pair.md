---
subjects:
  governs: "Dependency Relation Pair"
  depends_on:
    - "atom-boundary"
    - "relation-model"
    - "Artifact"
version: 16
updated_at: "2026-10-02 21:16:45 +0400"
relations: {}
atom_id: "CA-R-1026"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1026-CORE_META_MODEL-CORE--register-depends-on-and-required-by-relation-pair.md
  source_atom_id: CA-R-1026
  source_atom_revision: 16
  source_sha256: e2e76fb76c3e5d47d8e9df3e56e48c6ca3381d006c1b70233b3ee5f0bdfd1cd7
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Register depends_on and required_by relation pair

## Scope

the `depends_on` **and** `required_by` relation pair.

## Claim

`depends_on` **means** a direct dependency-ordering relation from a dependent Artifact **to** its prerequisite Artifact, with `required_by` as its inverse-derived view. Plan start dependencies use the Plan Graph's `BLOCKS` under CA-R-1580 instead; this Relation Kind **must not** duplicate that scheduling fact.

## Details
