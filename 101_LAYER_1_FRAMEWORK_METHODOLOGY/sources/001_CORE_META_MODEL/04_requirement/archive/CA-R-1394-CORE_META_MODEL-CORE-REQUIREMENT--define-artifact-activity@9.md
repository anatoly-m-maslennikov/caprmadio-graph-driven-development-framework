---
subjects:
  governs: "Artifact/Activity"
  depends_on:
    - "Artifact"
    - "Artifact/Revision/Status"
    - "Property"
version: 9
updated_at: "2026-09-11 02:13:22 +0400"
relations: {}
atom_id: "CA-R-1394"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Define Artifact Activity

the Artifact Property Activity **means** the derived Property that classifies an Artifact as Active **or** Inactive from its current Revision Status within the applicability defined by CA-R-1307. absence of an applicable Status model **means** absence of Activity, **not** Activity Inactive.
