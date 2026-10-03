---
atom_id: CA-P-986
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
    - CA-P-985
---
# Migrate Core Meta-Model operational Claims

the Assignee **must** move operational Claims **to** their admitted O authority.

## Scope

(selected **and** dispositioned RMEDO Claims **in** CORE_META_MODEL at `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL`); the source **and** lifecycle admission boundary established by CA-P-976 applies; historical versions, generated copies, runtime, Implementation code, **and** other CAP Atoms are excluded.

## Definition of Done

the Task is **not** Done **if** ((a dispositioned operational Claim remains authoritative **in** RMED **and** O simultaneously) **or** (a partial split loses a non-operational Claim) **or** (identity, revision, incoming references, **or** approved authority ownership is broken) **or** (a pending classification decision is silently guessed)).

## Details

execute the preceding disposition map. preserve unchanged Spec Claims **in** the correct RMED role; migrate whole operational Claims **or** split mixed carriers with complete predecessor/successor traceability **and** exact prior-version preservation. make **only** role-migration Carrier changes required for validity here; bulk Subject/property normalization remains sub-Epic 3. do **not** implement Tools **or** alter Settings values.

execute **only** **after** the explicit prerequisite is Done. **if** confidence **in** a decision is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains; do **not** silently select a new design. no migration is executed merely by creating this Task.
