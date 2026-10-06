---
subjects:
  governs: "Project Scope Unit Graph Projection"
  depends_on:
    - "Project Settings"
    - "Project Name"
    - "Obsolete Project Name"
version: 7
updated_at: "2026-09-11 15:04:40 +0400"
relations:
  child_of:
    - "CA-R-1052"
atom_id: "CA-D-392"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Delivery"
---
# Register obsolete project names

the Project Scope Unit Graph Projections **must** expose Project identity from the Project Settings Artifact with `project.name` as the canonical name **and** `project.obsolete_names` as the registered prior names **without** becoming authority for (Project Name **or** Obsolete Project Name).
