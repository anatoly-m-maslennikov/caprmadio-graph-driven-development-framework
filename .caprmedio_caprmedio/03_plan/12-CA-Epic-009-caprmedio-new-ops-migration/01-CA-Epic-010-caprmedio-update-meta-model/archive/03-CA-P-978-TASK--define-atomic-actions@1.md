---
atom_id: CA-P-978
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
autonomous_confidence_threshold: 99
subjects:
  governs:
    continuant:
      - "Atom/Content Role: Ops"
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
    - CA-P-977
---
# Define atomic Actions

the Assignee **must** define the useful atomic boundary of an Action.

## Scope

(selected Action-definition authority **in** CORE_META_MODEL at `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL`); the source **and** lifecycle admission boundary established by CA-P-976 applies; historical versions, generated copies, runtime, Implementation code, **and** other CAP Atoms are excluded.

## Definition of Done

the Task is **not** Done **if** ((Action has no explicit operational contribution) **or** (atomicity **means** one machine instruction **or** one Tool call rather than no useful independently governed subdivision) **or** (an arbitrary large procedure is admitted as atomic **without** a justified boundary)).

## Details

an Action is an operational building block for which further division has no useful meaning at the modeled responsibility **and** granularity. do **not** equate Action with Actor, Tool, Task, execution record, **or** Carrier. retain one canonical definition; resolve **any** unapproved naming **or** identity choice with the Operator rather than creating synonyms.

execute **only** **after** the explicit prerequisite is Done. **if** confidence **in** a decision is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains; do **not** silently select a new design. no migration is executed merely by creating this Task.
