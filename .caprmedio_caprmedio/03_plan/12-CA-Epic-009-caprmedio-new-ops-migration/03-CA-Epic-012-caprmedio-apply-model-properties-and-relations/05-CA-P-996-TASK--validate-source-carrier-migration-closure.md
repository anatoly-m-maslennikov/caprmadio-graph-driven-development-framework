---
atom_id: CA-P-996
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
    - CA-P-995
---
# Validate source Carrier migration closure

the Assignee **must** verify lossless source-level model application.

## Scope

(the selected source carriers covered by sub-Epics 1 through 3); the source **and** lifecycle admission boundary established by CA-P-976 applies; historical versions, generated copies, runtime, Implementation code, **and** other CAP Atoms are excluded.

## Definition of Done

the Task is **not** Done **if** ((an input lacks a retained, replaced, split, moved, **or** archived-successor disposition) **or** (an active duplicate authority **or** dangling **in**-scope reference remains) **or** (source content **and** metadata disagree) **or** (a deliberately deferred generated output is presented as current **or** validated)).

## Details

check source identities, versions, Carrier paths, Subjects, Relations, Type registrations, **and** scoped schema validation. **if** a validator **or** compiler cannot handle the new model, record the exact unsupported capability **and** request separate implementation authority; do **not** change I under this RMEDO Epic. historical **and** generated carriers are **not** rewritten. no installed Tool **or** runtime conformance claim follows from source validation.

execute **only** **after** the explicit prerequisite is Done. **if** confidence **in** a decision is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains; do **not** silently select a new design. no migration is executed merely by creating this Task.
