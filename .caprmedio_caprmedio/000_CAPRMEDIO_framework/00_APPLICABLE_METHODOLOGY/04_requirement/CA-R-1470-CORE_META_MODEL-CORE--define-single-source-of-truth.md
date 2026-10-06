---
subjects:
  governs: "Single Source of Truth"
  depends_on:
    - "Atom"
    - "Atom/Claim"
    - "Project Structure"
    - "Structural Entity"
    - "Journal"
    - "Projection"
version: 7
updated_at: "2026-10-04 22:02:40 +0000"
relations: {}
atom_id: "CA-R-1470"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1470-CORE_META_MODEL-CORE--define-single-source-of-truth.md
  source_atom_id: CA-R-1470
  source_atom_revision: 7
  source_sha256: fdd8765be6618a53fd491a48907f6cf297398066efa9da9055bc54fdea47a017
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Single Source of Truth

## Scope

the authority of independently maintained facts.

## Claim

Single Source of Truth **means** **`=1`** canonical authoritative source for **every** independently maintained fact **in** the same applicable context. another representation of that fact references **or** derives from its source **without** becoming an independently maintained authority.

source authority is assigned per fact under the governing model: Atoms carry governing Claims **and** their declared source Relations; Project Structure owns declared Scope Unit facts; Structural Entity Carriers supply materialization observations; Journals preserve recorded historical facts. native Implementation Carriers **may** be authoritative for their actual realized content, structure, dependencies, **and** behavior. other admitted sources retain their declared authority. this does **not** require **all** facts **to** reside **in** **`=1`** Atom, file, **or** Artifact. a derived result **may** use multiple authoritative input facts **without** creating another authoritative source for those input facts.

## Details

Implementation actual-state authority does not establish governing intent, acceptance, or compliance. RMED remains authority for the required result, method, evaluation, and delivery. A dependency graph or another view generated from native I remains a non-authoritative Projection of those actual-state sources.
