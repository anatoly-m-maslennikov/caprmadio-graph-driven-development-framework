---
subjects:
  governs: "Methodology Source/expansion mapping"
  depends_on:
    - "Methodology Source"
    - "Extension"
    - "Project Configuration"
    - "Core Meta-Model"
version: 4
updated_at: "2026-09-17 05:07:33 +0000"
relations: {child_of: [CA-M-006], method_for: [CA-R-1375]}
atom_id: "CA-M-298"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Method"
---
# Describe methodology expansion mappings

**to** describe a Methodology Source expansion mapping, use **`=1`** explicit mapping description that identifies:

- the source element **and** its provenance;
- the exact canonical target;
- the mapping rule;
- the intended scope of application;
- the applicable Core Meta-Model distinctions at **any** Local Tier.

apply this same mapping convention **to** Extension **and** Project Configuration sources regardless of provenance. the convention supports CA-R-1375's expansion boundary; it does **not** admit activation **or** reliance. CA-O-054 owns that admission Action **and** re-evaluation following material changes.
