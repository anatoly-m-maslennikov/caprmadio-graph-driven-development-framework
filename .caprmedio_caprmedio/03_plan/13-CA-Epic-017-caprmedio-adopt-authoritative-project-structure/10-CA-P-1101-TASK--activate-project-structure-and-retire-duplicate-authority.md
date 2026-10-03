---
atom_id: CA-P-1101
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
    - CA-P-1100
---
# Activate Project Structure and retire duplicate authority

the Assignee **must** cut over caprmedio to the validated Project Structure source **without** leaving competing structural authority.

## Scope

the caprmedio Project's structural authority boundary: `.caprmedio_caprmedio/project_structure.toml`, affected active structural/path Atoms, per-unit mode override settings, Goal/reference carriers, declared authority/Implementation folders, **and** selected consumers **only** as listed in the accepted migration map.

## Definition of Done

the Task is **not** Done **if** (two active sources govern the same structural value **or** a consumer uses the old source **or** a Goal/reference breaks **or** valid non-structural Claims are lost **or** history is rewritten **or** any cutover check fails **without** recovery to one coherent authority state).

## Details

recheck source revisions **and** the candidate/test evidence immediately before switching. changed inputs invalidate stale dispositions. activate the validated file at `.caprmedio_caprmedio/project_structure.toml` **and** switch admitted consumers under the defined recovery procedure. preserve Project identity/prefix **and** Framework Instance defaults; remove duplicated per-unit explicit overrides from their former live Settings source.

apply the exact approved Atom dispositions: concrete Name/order/path bindings move **to** TOML, Goal Claims remain R, mixed D/R Atoms retain valid general rules, **and** superseded sources retain recoverable history. do **not** retire unrelated Principles **or** product Requirements. repair references **and** perform **only** mapped necessary carrier moves; no gratuitous renumbering, blanket empty-folder cleanup, deletion of unexpected folders, **or** edits **to** .DS_Store files. avoid a partially switched set of live consumers. preserve recovery evidence **and** validate before declaring the new source active.

execute **only** after the direct prerequisite is Done **when** one is declared. **if** confidence is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains. preserve unrelated working-tree changes **and** historical records. creating this Task authorizes no execution by itself.

current scope correction: **after** every admitted consumer reads `project_structure.toml` directly, retire the legacy `project_scope_unit_graph.projection.toml` output **and** its selected rebuild entry points with recoverable history. do **not** create a replacement Project Structure Projection. preserve Applicable Methodology **and** unrelated Projection Artifacts.
