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
version: 2
updated_at: "2026-09-13 01:09:00 +0400"
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

Completion evidence: [Action atomicity report](../../execution_evidence/CA-P-978-action-atomicity-report.md) **and** [exact source/Task change map](../../execution_evidence/CA-P-978-changed-source-map.projection.json). new CA-R-1452 Version 1 is the single canonical Action definition: explicit operational contribution **and** no useful independently governed subdivision at the modeled responsibility **and** granularity. semantic acceptance fixtures reject arbitrary large procedures **without** justification, reject instruction/Tool-call counts as the atomicity criterion, **and** preserve the distinction from Actor, Tool, Task, particular execution, Journal Record, **and** Carrier. all 1,557 predecessor sources **and** all 53 excluded Drafts are unchanged; YAML, source identity, one governed Subject, preserved Task metadata **and** exact archive bytes pass. the Definition of Done falsifying condition is false. existing Subject serialization is temporary compatibility **only**; relation, taxonomy, temporal **and** carrier decisions remain with later Tasks. Git materialization under CA-D-335 remains explicitly pending because of the unrelated staged index.
