---
atom_id: CA-P-1099
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
autonomous_confidence_threshold: 99
subjects:
  governs: "Scope Unit"
  depends_on:
    - "Artifact"
    - "Atom"
    - "Operator"
    - "AI Agent"
    - "Autonomous Confidence Threshold"
version: 2
updated_at: "2026-09-15 00:07:17 +0000"
relations:
  depends_on:
    - CA-P-1098
---
# Specify Engine consumers of Project Structure

the Assignee **must** establish the Engine authority needed for Tools **and** other consumers to use authoritative Project Structure.

## Scope

FRAMEWORK_ENGINE **and** its descendant Scope Units; active RMEDO sources concerning structure read/write, Settings resolution, Atom scope/reference resolution, graph generation, search/navigation, installation entry points, **and** migration validation.

## Definition of Done

the Task is **not** Done **if** (an affected consumer lacks a disposition **or** Tool R/M/E/D still requires folder/Projection-derived authority **or** an implementation-specific process duplicates O authority **or** mutation permissions **and** compatibility boundaries remain unspecified).

## Details

use the consumer inventory **and** accepted Core/configuration authority. update selected Tool specifications before Implementation changes. specify a shared source-resolution boundary where appropriate **without** creating a second independently maintained schema. cover readers, editors, graph generators, Atom operations, downstream displays, validators, **and** actual selected execution entry points. distinguish an editable structural source from read-only derived views.

require explicit errors for missing/invalid/conflicting source rather than silent fallback **to** old Settings, obsolete root paths, folder parsing, **or** Projection values. any transitional reader mode is explicit, bounded, **and** removed **or** disabled at cutover. keep Project identity/prefix in Project Settings **and** effective mode resolution traceable. no Tool code, installation, hooks, manifest activation, **or** historical rewriting occurs in this authority-only Task.

execute **only** after the direct prerequisite is Done **when** one is declared. **if** confidence is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains. preserve unrelated working-tree changes **and** historical records. creating this Task authorizes no execution by itself.

current scope correction: Project Structure consumers read `project_structure.toml` directly. migrate consumers away from the existing structural graph Projection; do **not** implement **or** retain an automatic structural-Projection rebuild as the new source-resolution path. optional graph visualization capabilities are **not** required by this Epic.
