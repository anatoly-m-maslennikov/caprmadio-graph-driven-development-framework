---
atom_id: CA-P-992
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
    - CA-P-991
---
# Apply the model to Core Meta-Model carriers

the Assignee **must** apply the reconciled model **to** Core Meta-Model Properties **and** Relations.

## Scope

(selected RMEDO carriers **in** CORE_META_MODEL at `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL`); the source **and** lifecycle admission boundary established by CA-P-976 applies; historical versions, generated copies, runtime, Implementation code, **and** other CAP Atoms are excluded.

## Definition of Done

the Task is **not** Done **if** ((a selected Carrier still requires the removed temporal nesting) **or** (a Subject **or** Relation loses its target **or** meaning) **or** (new **and** old role/property representations disagree) **or** (canonical identity, revision, **or** reference resolution is invalid)).

## Details

apply admitted D rules **to** subjects, graph-owned relations, Properties, role/type metadata, identifiers **and** filenames as required. remove CONTINUANT/OCCURRENT keys **without** deleting semantic distinctions; reconcile collisions **before** flattening. use exact source identity **and** Version rather than a global ambiguous ID match. do **not** write generated APPLICABLE_METHODOLOGY **or** change Tool implementation.

execute **only** **after** the explicit prerequisite is Done. **if** confidence **in** a decision is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains; do **not** silently select a new design. no migration is executed merely by creating this Task.
