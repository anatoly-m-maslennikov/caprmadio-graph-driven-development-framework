---
subjects:
  governs: "Relation Kind/Metadata"
  depends_on:
    - "Relation Kind"
    - "CAPRMEDIO Graph"
    - "Projection"
    - "Atom"
version: 20
updated_at: "2026-09-15 01:47:49 +0400"
relations: {}
atom_id: "CA-R-806"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Register Complete Relation Kind Metadata

**every** admitted Relation Kind **must** have **`=1`** canonical metadata record derived from its governing authority that resolves its owning kind of CAPRMEDIO Graph, canonical name, meaning, declared direction, inverse direction, source class, target class, the allowed graph context of **every** endpoint including cross-graph **and** authoritative-source references **when** admitted, cardinality, authority effect, transitivity, applicability, Status, **and** exclusive purpose.
