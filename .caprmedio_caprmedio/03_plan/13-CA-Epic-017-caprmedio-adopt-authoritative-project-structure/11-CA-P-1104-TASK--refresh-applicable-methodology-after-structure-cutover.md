---
atom_id: CA-P-1104
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
autonomous_confidence_threshold: 99
subjects:
  governs: "Applicable Methodology"
  depends_on:
    - "Project Structure"
    - "Projection"
    - "Operator"
    - "Autonomous Confidence Threshold"
version: 1
updated_at: "2026-09-15 00:07:17 +0000"
relations:
  depends_on:
    - CA-P-1101
---
# Refresh Applicable Methodology after structure cutover

the Assignee **must** refresh the existing Applicable Methodology from the updated methodology source authority after the Project Structure cutover.

## Scope

the caprmedio Framework Instance's existing Applicable Methodology under `.caprmedio_caprmedio/000_CAPRMEDIO_framework`, its accepted methodology sources, **and** its compatible canonical compilation Tool; the Project Structure manifest is an input **only** where structural source resolution needs it.

## Definition of Done

the Task is **not** Done **if** (Applicable Methodology still exposes superseded source authority **or** loses source traceability **or** a source Claim is rewritten by compilation **or** an unresolved conflict is silently selected **or** a separate Project Structure Projection is generated).

## Details

CA-P-1102 was cancelled because the Operator does **not** need a separate Project Structure Projection. this Task refreshes **only** the existing Applicable Methodology, which remains a derived methodology Artifact **and** is **not** the structural source of truth. use the compatible compiler **and** current selected Core Meta-Model, installed Extension, **and** Project Configuration sources. do **not** convert manifest records into Atoms **or** automatically rebuild unrelated graph views. validate current source bindings **and** deterministic selected content, allowing independently governed refresh timestamps.

execute **only** after CA-P-1101 is Done. **if** confidence is below the effective threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains. preserve unrelated sources **and** history.
