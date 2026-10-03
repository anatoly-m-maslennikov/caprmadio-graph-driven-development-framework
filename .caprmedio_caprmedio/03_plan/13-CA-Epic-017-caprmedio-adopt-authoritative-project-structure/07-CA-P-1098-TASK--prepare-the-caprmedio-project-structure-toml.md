---
atom_id: CA-P-1098
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
version: 1
updated_at: "2026-09-14 23:56:42 +0000"
relations:
  depends_on:
    - CA-P-1097
---
# Prepare the caprmedio project_structure.toml

the Assignee **must** prepare a validated Project Structure TOML candidate for caprmedio using the accepted migration inventory.

## Scope

the caprmedio Project Structure candidate for final location `.caprmedio_caprmedio/project_structure.toml`, using the exact selected sources **and** dispositions from CA-P-1097.

## Definition of Done

the Task is **not** Done **if** (the candidate violates CA-P-1095's schema **or** omits/duplicates an admitted unit **or** contains guessed values **or** has unresolved reference/path/mode conflicts **or** is activated before the cutover gate).

## Details

materialize the accepted `[[scope_units]]` records, including readability fields, using CA-P-1097's resolved values rather than copying the example row blindly. use the candidate Carrier/state admitted by CA-P-1095; reserve the final filename **without** exposing a second active authoritative source. apply the defined parent/root references **and** path bases. carry **only** explicit per-unit mode overrides; omit inherited values.

validate schema, structural consistency, source coverage, Goal reference resolution, path bindings, **and** isolation from other Projects. preserve original source evidence **and** record a stable candidate identity/digest for consumer tests. no duplicate Atom retirement, folder rename, existing Projection overwrite, **or** live consumer switch occurs here.

execute **only** after the direct prerequisite is Done **when** one is declared. **if** confidence is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains. preserve unrelated working-tree changes **and** historical records. creating this Task authorizes no execution by itself.
