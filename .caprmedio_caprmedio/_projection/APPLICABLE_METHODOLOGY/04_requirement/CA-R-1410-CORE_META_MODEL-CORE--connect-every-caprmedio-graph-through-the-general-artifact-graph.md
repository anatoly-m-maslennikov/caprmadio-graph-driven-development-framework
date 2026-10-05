---
subjects:
  governs: "CAPRMEDIO Graph/Connectivity"
  depends_on:
    - "General Artifact Graph"
    - "Artifact"
    - "Structural Entity"
version: 7
updated_at: "2026-10-02 22:41:14 +0400"
relations: {}
atom_id: "CA-R-1410"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1410-CORE_META_MODEL-CORE--connect-every-caprmedio-graph-through-the-general-artifact-graph.md
  source_atom_id: CA-R-1410
  source_atom_revision: 7
  source_sha256: 4cba155ea2ec0fdc6d5425e85e6590c2d63cc6c8653c325975a4ff74123ec1b9
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Connect Every CAPRMEDIO Graph through the General Artifact Graph

## Scope

CAPRMEDIO Graphs and their connections to the General Artifact Graph.

## Claim

**every** CAPRMEDIO Graph **must** connect **to** the General Artifact Graph through **`>=1`** shared **or** referenced source Artifact **or** Structural Entity. the connection preserves the existing source identity **without** creating a duplicate source **or** requiring an artificial Artifact for a structural-only source.

## Details
