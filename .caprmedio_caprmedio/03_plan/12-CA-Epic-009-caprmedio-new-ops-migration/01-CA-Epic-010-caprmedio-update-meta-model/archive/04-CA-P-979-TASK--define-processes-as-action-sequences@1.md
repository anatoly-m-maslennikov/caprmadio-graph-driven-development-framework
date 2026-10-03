---
atom_id: CA-P-979
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
    - CA-P-978
---
# Define Processes as Action sequences

the Assignee **must** define a Process as a sequence of Actions.

## Scope

(selected Process-definition authority **in** CORE_META_MODEL at `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL`); the source **and** lifecycle admission boundary established by CA-P-976 applies; historical versions, generated copies, runtime, Implementation code, **and** other CAP Atoms are excluded.

## Definition of Done

the Task is **not** Done **if** ((Process composition lacks explicit ordering) **or** (a Process definition is conflated with a particular execution) **or** (the same reusable Action **must** be redefined for **every** Process) **or** (unapproved branching, looping, concurrency, **or** recursive composition semantics are silently introduced)).

## Details

use the Operator's sequence-of-Actions definition, **not** mathematical subsequence by accident. preserve distinct reusable definition **and** execution references. **if** existing accepted Operations need branches, retries, **or** other control flow, present the precise compatibility decision instead of inventing a rule **or** deleting behavior.

execute **only** **after** the explicit prerequisite is Done. **if** confidence **in** a decision is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains; do **not** silently select a new design. no migration is executed merely by creating this Task.
