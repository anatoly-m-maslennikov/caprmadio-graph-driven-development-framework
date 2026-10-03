---
subjects:
  governs: "Lineage Impact Analysis"
  depends_on:
    - "Atom"
    - "Artifact/Revision"
    - "Atom Change Classification"
    - "Carrier-Only Recoding"
    - "Verification"
version: 19
updated_at: "2026-09-28 06:30:40 +0400"
relations:
  relates_to:
    - CA-R-1687
    - CA-R-1632
atom_id: "CA-R-1633"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Archived"
author: "Anatoly Maslennikov"
type: "Requirement"
global_tier: 10
---
# Record one Lineage Impact Analysis per changed atom revision

**every** `refinement`, `semantic_revision`, **or** `replacement` of an admitted Atom **must** produce **`=1`** Lineage Impact Analysis Atom whose primary conclusion is the impact state of that exact changed parent Revision, while a `carrier_only` change **must** require lossless-recoding Verification instead.
