---
atom_id: CA-P-983
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
autonomous_confidence_threshold: 99
subjects:
  governs:
    continuant:
      - "Journal"
  depends_on:
    continuant:
      - "Atom"
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
version: 3
updated_at: "2026-09-14 01:17:47 +0400"
relations:
  depends_on:
    - CA-P-982
---
# Define the two Journal responsibilities

the Assignee **must** define artifact-change **and** Process-execution log views as non-authoritative Projections of the shared Project Journal.

## Scope

(selected RMEDO Journal-model authority **in** CORE_META_MODEL at `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL`); the source **and** lifecycle admission boundary established by CA-P-976 applies; historical versions, generated copies, runtime, Implementation code, **and** other CAP Atoms are excluded.

## Definition of Done

the Task is **not** Done **if** ((state-change facts **and** execution facts have no distinct responsibility) **or** (an execution record **must** duplicate authoritative state-change details) **or** (a read-**only** execution requires a fictitious state change) **or** (either derived log is classified as a separate Journal Type **or** independently authored historical source)).

## Details

consume the general Journal model **and** Carrier authority from the completed CA-Epic-016, especially CA-P-1088 **and** CA-P-1090. this Task owns **only** the Operation-specific artifact-change **and** Process-execution log Projection responsibilities **and** its necessary record relations, D refinements, **and** E checks; do **not** redefine generic Journal authority **or** graph ownership.

the shared Project Journal records the historical events once. the artifact-change log selects recorded Artifact changes; the Process-execution log organizes recorded events by their execution **and** recorded outcomes. both are rebuildable, non-authoritative Projections, **not** Journal Types. link an execution **to** its recorded Artifact changes using the source event references **without** duplicating historical authority; the same event **may** appear **in** both views. distinguish executions from their records **and** permit read-only executions **without** inventing changes. view selection **and** grouping do **not** require separate Journals, new Projection Types, **or** an unapproved number of physical files. define necessary model **and** Carrier authority **only**; do **not** rewrite historical Journals, create a new logging implementation, **or** migrate existing log files.

execute **only** **after** the explicit prerequisite is Done. **if** confidence **in** a decision is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains; do **not** silently select a new design. no migration is executed merely by creating this Task.

consume the Operator-directed [shared event Journal authority update](../execution_evidence/CA-P-1088-shared-event-journal-authority-update.md) **and** [ordered source-change map](../execution_evidence/CA-P-1088-shared-event-journal-changed-source-map.projection.json). this administrative alignment does **not** execute this Task **or** settle the deferred event-field schema **and** concrete execution associations.
