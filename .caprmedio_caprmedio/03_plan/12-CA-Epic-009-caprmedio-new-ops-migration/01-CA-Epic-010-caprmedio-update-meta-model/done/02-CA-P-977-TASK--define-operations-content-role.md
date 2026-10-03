---
atom_id: CA-P-977
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
updated_at: "2026-09-13 00:56:11 +0400"
relations:
  depends_on:
    - CA-P-976
---
# Define Operations Content Role

the Assignee **must** establish the accepted Operations Content Role boundary.

## Scope

(selected RMEDO authority defining Content Roles **in** CORE_META_MODEL at `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL`); the source **and** lifecycle admission boundary established by CA-P-976 applies; historical versions, generated copies, runtime, Implementation code, **and** other CAP Atoms are excluded.

## Definition of Done

the Task is **not** Done **if** ((O still **means** **only** an occurred-event record) **or** (Processes **or** their executions are treated as RMED Spec contents) **or** (Plan is renamed **to** Process) **or** (a Content Role is assigned **only** because an Atom mentions an Operation)).

## Details

RMED specifies Implementation. O defines operational Action **and** Process behavior **and** Actor participation/authorization policies. P remains Plan for intended Tasks **and** Objectives; Epics group Tasks. Journal records carry execution evidence **and** state changes. this Task updates definitions **and** directly conflicting role-classification authority, **not** existing Task carriers **or** runtime Tools. a meta-model definition describing the O role is distinct from an operational procedure using that role.

execute **only** **after** the explicit prerequisite is Done. **if** confidence **in** a decision is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains; do **not** silently select a new design. no migration is executed merely by creating this Task.

Completion evidence: [Operations role boundary report](../../execution_evidence/CA-P-977-operations-role-boundary-report.md) **and** [exact predecessor/successor change map](../../execution_evidence/CA-P-977-changed-source-map.projection.json). 15 Active CORE_META_MODEL role-definition **and** directly conflicting classification Atoms were revised under their existing identities; **every** prior revision is preserved byte-for-byte. the other 1,542 frozen sources **and** all 53 excluded Drafts are unchanged. O defines reusable operational behavior **and** participation/authorization policies, P remains intended Tasks **and** Objectives, **and** actual executions **and** their Journal Records are distinct from RMED Spec. classification follows primary contribution, including meta-model definitions that remain R. source integrity, YAML syntax, unchanged metadata/relations, **and** the semantic boundary cases pass; the Definition of Done falsifying condition is false. Git materialization under CA-D-335 remains explicitly pending because of the unrelated staged index.
