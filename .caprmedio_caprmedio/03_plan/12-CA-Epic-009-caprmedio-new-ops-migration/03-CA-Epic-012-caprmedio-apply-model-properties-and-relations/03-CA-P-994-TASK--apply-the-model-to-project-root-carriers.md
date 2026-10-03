---
atom_id: CA-P-994
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
    - CA-P-993
---
# Apply the model to project-root carriers

the Assignee **must** materialize the approved project-root content dispositions **in** their Carriers.

## Scope

(selected project-root RMEDO carriers **in** `.caprmedio_caprmedio`, plus **only** CA-P-032, CA-P-033, **and** CA-P-034); the source **and** lifecycle admission boundary established by CA-P-976 applies; historical versions, generated copies, runtime, Implementation code, **and** other CAP Atoms are excluded.

## Definition of Done

the Task is **not** Done **if** ((a selected Atom's fields, role, path, **or** references disagree with its reconciled Claim) **or** (an approved P Actor policy lacks a unique O successor with preserved tier) **or** (**any** other CAP **or** I Atom is changed) **or** (a distinct governed target is discarded during temporal flattening)).

## Details

complete role/ID/path migrations, lossless partial splits, Subjects, Properties, **and** direct Relations **in** Principle **then** Core **then** Standard order. the three P exceptions are limited **to** Actor policies. preserve their old revisions **and** trace **every** incoming reference; **if** a necessary reference repair is outside the authorized set, ask the Operator rather than broadening the edit scope. do **not** rewrite unrelated Plans, even **to** remove their legacy temporal keys.

execute **only** **after** the explicit prerequisite is Done. **if** confidence **in** a decision is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains; do **not** silently select a new design. no migration is executed merely by creating this Task.
