---
subjects:
  governs: "Lineage Impact Analysis"
  depends_on:
    - "Atom"
    - "Artifact/Revision"
    - "Atom Change Classification"
    - "Carrier-Only Recoding"
    - "Verification"
version: 17
updated_at: "2026-09-17 12:02:45 +0000"
relations:
  relates_to:
    - CAPRMEDIO-META-REQU-097
    - CAPRMEDIO-GOV-REQU-310
atom_id: "CAPRMEDIO-GOV-REQU-312"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Record one Lineage Impact Analysis per changed atom revision

**every** `refinement`, `semantic_revision`, **or** `replacement` of an admitted Atom **must** produce **`=1`** Lineage Impact Analysis Atom whose primary conclusion is the impact state of that exact changed parent Revision, while a `carrier_only` change **must** require lossless-recoding Verification instead.
