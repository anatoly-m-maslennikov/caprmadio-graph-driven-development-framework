---
subjects:
  governs: "lifecycle-traceability"
  depends_on: []
version: 21
updated_at: "2026-10-03 02:13:51 +0400"
relations:
  child_of:
    - CAPRMEDIO-REQU-007-CORE-REQUIREMENT--full-minimal-traceability
    - CA-E-002
atom_id: "CA-R-1697"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1697-CORE_META_MODEL-CORE-REQUIREMENT--bind-traceability-to-exact-claims-and-revisions.md
  source_atom_id: CA-R-1697
  source_atom_revision: 21
  source_sha256: ec50dcadfd39438b319cf3d5bcafd0cbbf257f6f2885230cf2bb0688c6e952e9
  original_relations_sha256: 1a0524f477df91d6f61ba6ed9eb1ee88a4409751914a1e0856255d36167b4dd8
---
# Summary

Bind traceability to exact claims and revisions

## Scope

CAPRMEDIO traceability assertions.

## Claim

**every** CAPRMEDIO traceability assertion **must** identify the exact governed claim revision on which a receiving artifact, implementation target, evaluation use, delivery action, operational observation, **or** other governed result relies.

## Details

the trace **must** preserve the source identity **and** accepted Revision, the receiving identity **or** stable target locator, the typed relation between them, the bounded scope **and** use, **and** the provenance needed **to** replay that relation. a relation **to** an artifact ID **without** its relied-upon revision is insufficient **after** the Atom has more than one accepted Revision.

Traceability records relationships; it does **not** transfer authority **or** prove correctness, execution, delivery, **or** currentness. secondary storage history **may** preserve Carrier evidence, while governed Journals preserve semantic relationships independently of that secondary history.
