---
subjects:
  governs: "Projection/Type: Process Log"
  depends_on:
    - "Step Run"
    - "Workflow Run"
    - "Projection"
    - "Journal"
    - "Journal/Record"
    - "Action"
    - "Workflow"
version: 5
updated_at: "2026-09-18 14:16:20 +0000"
relations: {}
atom_id: "CA-R-1468"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Define Process Log Projection

a Process Log **means** a non-authoritative Projection of the Project Journal that presents recorded Workflow Runs, Step Runs, **and** Action executions using their recorded execution associations, progress, **and** outcomes. it includes recorded executions **without** Artifact changes **and** does **not** infer an unrecorded execution association **or** successful outcome.
