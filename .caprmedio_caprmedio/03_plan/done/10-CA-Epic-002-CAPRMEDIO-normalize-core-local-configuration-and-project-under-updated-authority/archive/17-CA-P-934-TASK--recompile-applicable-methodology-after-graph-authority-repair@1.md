---
atom_id: CA-P-934
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    continuant:
      - Applicable Methodology
    occurrent:
      - Applicable Methodology Recompilation
  depends_on:
    occurrent:
      - CA-P-933
version: 1
updated_at: 2026-08-31 20:56:10 +0400
autonomous_confidence_threshold: 99
relations: {}
---
# Recompile Applicable Methodology after Graph Authority Repair

**when** CA-P-933 is Done, **then** the Assignee **must** recompile Applicable Methodology from the exact current Core Meta-Model and Local Configuration frontier.

## Scope

`((CORE_META_MODEL active RMEDO Atoms) union (LOCAL_CONFIGURATION active RMEDO Atoms) union (generated Applicable Methodology RMEDO Atoms))`

## Definition of Done

the Task is **not done if** (the compiled tree omits the repaired Project Scope Unit Graph source authority **or** includes CAP, Draft, Archived, inactive, **or** unselected sources **or** any unresolved conflict, stale approval, source mismatch, provenance error, nondeterministic output, **or** compiler-test failure remains).

## Details

run two byte-identical dry-runs before applying. apply generated RMEDO Atoms only.
