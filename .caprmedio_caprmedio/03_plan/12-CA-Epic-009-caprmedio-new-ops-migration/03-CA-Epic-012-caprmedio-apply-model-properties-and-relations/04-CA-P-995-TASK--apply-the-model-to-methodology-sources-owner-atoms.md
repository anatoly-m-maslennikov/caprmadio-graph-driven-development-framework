---
atom_id: CA-P-995
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
autonomous_confidence_threshold: 99
subjects:
  governs:
    continuant:
      - "Atom"
  depends_on:
    continuant:
      - "Atom/Claim"
      - "Atom/Content Role"
      - "Atom/Subjects"
      - "Scope Unit"
      - "Atom/Local Tier"
      - "Atom/Global Tier"
      - "Relation"
      - "Actor"
      - "Operator"
      - "AI Agent"
      - "Atom/Content Role: Plan/Type: Task"
      - "Autonomous Confidence Threshold"
version: 1
updated_at: "2026-09-12 23:54:02 +0400"
relations:
  depends_on:
    - CA-P-994
---
# Apply the model to Methodology Sources owner Atoms

the Assignee **must** align the Methodology Sources owner Atoms with the reconciled model.

## Scope

(selected directly owned RMEDO Atoms **in** METHODOLOGY_SOURCES at `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources`, excluding child Scope Units); the source **and** lifecycle admission boundary established by CA-P-976 applies; historical versions, generated copies, runtime, Implementation code, **and** other CAP Atoms are excluded.

## Definition of Done

the Task is **not** Done **if** ((a directly owned admitted Atom is omitted) **or** (content **or** Carrier metadata retain a conflicting Operation **or** temporal-axis rule) **or** (a child-source Atom is duplicated **in** this batch)).

## Details

cover the actual parent-source Goal carriers **and** **any** other admitted directly owned authority. CORE_META_MODEL **and** PROJECT_CONFIGURATION were handled separately. preserve Goal hierarchy **and** do **not** grant Goals **to** the generated Applicable Methodology Projection.

execute **only** **after** the explicit prerequisite is Done. **if** confidence **in** a decision is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains; do **not** silently select a new design. no migration is executed merely by creating this Task.
