---
atom_id: CA-P-1102
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
autonomous_confidence_threshold: 99
subjects:
  governs: "Projection"
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
    - CA-P-1101
---
# Rebuild structure-dependent Projections

the Assignee **must** rebuild affected derived outputs from the cut-over authority **without** reintroducing structural source ownership.

## Scope

the caprmedio Project's structure-dependent Projections, including the Project Scope Unit Graph, affected derived graph/navigation views, **and** Applicable Methodology under `.caprmedio_caprmedio/000_CAPRMEDIO_framework`, restricted to the cutover impact map.

## Definition of Done

the Task is **not** Done **if** (a selected Projection is stale **or** lacks traceability to current sources **or** a generated view claims editable source authority **or** rebuilding overwrites project_structure.toml **or** rebuilding rewrites source Claims **or** an old duplicate output remains selected as current).

## Details

use compatible validated Tools **and** accepted source-selection/Evaluation rules. Applicable Methodology remains a Projection of its selected methodology Atom sources; do **not** turn Project Structure rows into methodology Atoms merely to include the manifest. structure graphs derive from the manifest with observations clearly distinguished. do **not** restore a second authored `parent`/`structural_parent` pair **or** authored inverse edges.

check completeness, current source paths, digests/revisions, explicit-versus-effective mode provenance, **and** same-source deterministic results. output refresh timestamps may differ under their own rules. report undeclared materialized folders **and** declared missing folders **without** silently changing source authority. retire obsolete selected generated outputs through the admitted recovery-safe procedure, preserving historical evidence.

execute **only** after the direct prerequisite is Done **when** one is declared. **if** confidence is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains. preserve unrelated working-tree changes **and** historical records. creating this Task authorizes no execution by itself.
