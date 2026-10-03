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
version: 1
updated_at: "2026-09-12 23:54:02 +0400"
relations:
  depends_on:
    - CA-P-982
---
# Define the two Journal responsibilities

the Assignee **must** distinguish State Change Log **and** Process Execution Log responsibilities.

## Scope

(selected RMEDO Journal-model authority **in** CORE_META_MODEL at `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL`); the source **and** lifecycle admission boundary established by CA-P-976 applies; historical versions, generated copies, runtime, Implementation code, **and** other CAP Atoms are excluded.

## Definition of Done

the Task is **not** Done **if** ((state-change facts **and** execution facts have no distinct responsibility) **or** (an execution record **must** duplicate authoritative state-change details) **or** (a read-**only** execution requires a fictitious state change) **or** (two logical Journal Types force two physical files **without** D authority)).

## Details

State Change Log records what changed; Process Execution Log records what ran **and** its outcomes. link an execution **to** its produced state-change records **without** duplicating authority. distinguish executions from their persistent records. permit these two logical Types **without** requiring  per Scope Unit. define necessary model **and** Carrier authority **only**; do **not** rewrite historical Journals, create a new logging implementation, **or** migrate existing log files.

execute **only** **after** the explicit prerequisite is Done. **if** confidence **in** a decision is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains; do **not** silently select a new design. no migration is executed merely by creating this Task.
