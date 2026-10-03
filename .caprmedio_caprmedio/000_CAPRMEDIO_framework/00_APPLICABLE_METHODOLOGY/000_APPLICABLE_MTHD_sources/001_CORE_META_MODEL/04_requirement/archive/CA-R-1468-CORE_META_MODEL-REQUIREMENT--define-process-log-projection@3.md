---
cce_version: cce_1
cce_form: definition
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
version: 3
updated_at: "2026-09-18 14:16:20 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Define Process Log Projection

a Process Log **means** a non-authoritative Projection of the Project Journal that presents recorded Workflow Runs, Step Runs, **and** Action executions using their recorded execution associations, progress, **and** outcomes. it includes recorded executions **without** Artifact changes **and** does **not** infer an unrecorded execution association **or** successful outcome.
