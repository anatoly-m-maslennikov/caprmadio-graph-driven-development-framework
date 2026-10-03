---
atom_id: CA-P-985
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
    - CA-P-984
---
# Inventory mixed RMED and Ops Claims in Core Meta-Model

the Assignee **must** produce a Claim-level RMED-versus-O disposition for **every** selected Core Meta-Model Atom.

## Scope

(selected RMEDO Atoms **in** CORE_META_MODEL at `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL`); the source **and** lifecycle admission boundary established by CA-P-976 applies; historical versions, generated copies, runtime, Implementation code, **and** other CAP Atoms are excluded.

## Definition of Done

the Task is **not** Done **if** ((an input Atom lacks a fully-O, partially-O, retain-RMED, **or** retain-O disposition) **or** (an independently replaceable operational clause is hidden **in** retained RMED) **or** (a retained clause **or** source-**to**-successor mapping is lost)).

## Details

review actual Claims, **not** keywords, current role letters, **or** old temporal buckets. distinguish Implementation Method choices from operational workflows. partial cases need a lossless split plan; whole cases need a role-migration plan. do **not** execute the migration **in** this inventory Task.

execute **only** **after** the explicit prerequisite is Done. **if** confidence **in** a decision is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains; do **not** silently select a new design. no migration is executed merely by creating this Task.
