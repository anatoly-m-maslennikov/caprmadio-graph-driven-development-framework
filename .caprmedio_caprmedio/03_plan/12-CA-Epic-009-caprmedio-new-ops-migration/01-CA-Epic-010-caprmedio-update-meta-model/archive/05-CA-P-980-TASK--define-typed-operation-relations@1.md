---
atom_id: CA-P-980
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
autonomous_confidence_threshold: 99
subjects:
  governs:
    continuant:
      - "Relation"
  depends_on:
    continuant:
      - "Atom"
      - "Atom/Claim"
      - "Atom/Content Role"
      - "Atom/Subjects"
      - "Scope Unit"
      - "Atom/Local Tier"
      - "Atom/Global Tier"
      - "Actor"
      - "Operator"
      - "AI Agent"
      - "Atom/Content Role: Plan/Type: Task"
      - "Autonomous Confidence Threshold"
version: 1
updated_at: "2026-09-12 23:54:02 +0400"
relations:
  depends_on:
    - CA-P-979
---
# Define typed Operation relations

the Assignee **must** establish graph-owned typed relations for Actions **and** Processes.

## Scope

(selected graph **and** Subject relation authority needed for Operations **in** CORE_META_MODEL at `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL`); the source **and** lifecycle admission boundary established by CA-P-976 applies; historical versions, generated copies, runtime, Implementation code, **and** other CAP Atoms are excluded.

## Definition of Done

the Task is **not** Done **if** ((a required relation lacks an owner graph kind, endpoint domains, direction, cardinality, **or** precise contribution) **or** (the same relation fact has independently maintained authority **in** multiple graphs) **or** (GOVERNS **or** DEPENDS_ON is removed merely with the temporal nesting) **or** (dependency is silently interpreted as execution order) **or** (Entity, Process, Action, Term, **and** execution references cannot be resolved coherently)).

## Details

cover the required Action-**to**-Process composition **and** ordering **and** the required Atom-**to**-Operation governance/reference cases. admit **only** relation kinds actually needed; the Operator did **not** specify exactly two relation kinds. make the Entity/Process boundary **and** reference domain explicit **without** duplicating identity across graphs. Terms remain project-specific words **or** phrases, **not** executions. do **not** revive dependencies between Scope Units: structural containment remains its own tree. ask about **any** unresolved exact relation name **or** domain below 99% confidence; do **not** freeze a speculative schema.

execute **only** **after** the explicit prerequisite is Done. **if** confidence **in** a decision is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains; do **not** silently select a new design. no migration is executed merely by creating this Task.
