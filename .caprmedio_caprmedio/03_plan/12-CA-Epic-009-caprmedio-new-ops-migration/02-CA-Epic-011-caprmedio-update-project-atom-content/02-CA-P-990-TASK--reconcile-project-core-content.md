---
atom_id: CA-P-990
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
    - CA-P-989
---
# Reconcile project core content

the Assignee **must** align the selected project Core Claims with the new Operations model.

## Scope

(selected project-root RMEDO Atoms at Local Tier Core **and** Global Tier 1 **in** `.caprmedio_caprmedio`, plus CA-P-034); the source **and** lifecycle admission boundary established by CA-P-976 applies; historical versions, generated copies, runtime, Implementation code, **and** other CAP Atoms are excluded.

## Definition of Done

the Task is **not** Done **if** ((an admitted Atom lacks a content disposition) **or** (a retained Claim conflicts with the new role, Actor, Process, Tool, **or** temporal-axis boundary) **or** (independent Claims are lost **or** duplicated) **or** (this content-**only** Task performs a bulk property, relation, ID, filename, folder, **or** tier migration)).

## Details

preserve the established Principle/Core distinction; this is **not** a tier redesign. the approved P exceptions here are CA-P-034; prepare their O successor **and** reference dispositions **without** changing **any** other P Atom. reconcile content **and** Summaries **only**; record whole/partial O migrations **and** legacy field changes for sub-Epic 3 instead of prematurely applying them. preserve permissions, Operator authority, **and** runtime guarantees. higher-priority direct Operator decisions govern; **otherwise** resolve conflicts from Project Principles first.

execute **only** **after** the explicit prerequisite is Done. **if** confidence **in** a decision is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains; do **not** silently select a new design. no migration is executed merely by creating this Task.
