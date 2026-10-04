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
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1410-CORE_META_MODEL-CORE--connect-every-caprmedio-graph-through-the-general-artifact-graph.md
---
# Summary

Connect Every CAPRMEDIO Graph through the General Artifact Graph

## Scope

CAPRMEDIO Graphs and their connections to the General Artifact Graph.

## Claim

**every** CAPRMEDIO Graph **must** connect **to** the General Artifact Graph through **`>=1`** shared **or** referenced source Artifact **or** Structural Entity. the connection preserves the existing source identity **without** creating a duplicate source **or** requiring an artificial Artifact for a structural-only source.

## Details
