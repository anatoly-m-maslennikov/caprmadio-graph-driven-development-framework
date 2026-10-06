---
subjects:
  governs: "Projection"
  depends_on:
    - "Artifact/Revision"
version: 3
updated_at: "2026-09-17 04:06:18 +0000"
relations: {"child_of":["CAPRMEDIO-META-REQU-657"]}
atom_id: "CA-R-1494"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Record Projection dependency provenance only when required

a Projection **must** record dependency provenance **only** **when** its registered job requires that information; no Projection is required **to** persist a blanket source frontier.

this conditional recording obligation does **not** remove source traceability required by CAPRMEDIO-META-REQU-657 **or** a more specific admitted Projection specification.
