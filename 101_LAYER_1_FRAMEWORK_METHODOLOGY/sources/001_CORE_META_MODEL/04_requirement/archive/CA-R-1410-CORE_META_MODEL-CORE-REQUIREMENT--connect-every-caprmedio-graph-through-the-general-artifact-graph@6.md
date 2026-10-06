---
subjects:
  governs: "CAPRMEDIO Graph/Connectivity"
  depends_on:
    - "General Artifact Graph"
    - "Artifact"
    - "Structural Entity"
version: 6
updated_at: "2026-09-14 21:49:27 +0400"
relations: {}
atom_id: "CA-R-1410"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Connect Every CAPRMEDIO Graph through the General Artifact Graph

**every** CAPRMEDIO Graph **must** connect **to** the General Artifact Graph through **`>=1`** shared **or** referenced source Artifact **or** Structural Entity. the connection preserves the existing source identity **without** creating a duplicate source **or** requiring an artificial Artifact for a structural-only source.
