---
atom_id: CA-P-930
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
      - CA-P-929
version: 1
updated_at: 2026-08-30 19:25:06 +0400
autonomous_confidence_threshold: 99
relations: {}
---
# Recompile Applicable Methodology after Authority Repairs

**when** CA-P-929 is Done, **then** the Assignee **must** deterministically recompile and atomically apply the Applicable Methodology from the repaired exact source frontier.

## Scope

`((the current active RMEDO Atom revisions in CORE_META_MODEL and LOCAL_CONFIGURATION) union (the Applicable Methodology compiler, tests, and conflict approval authority) union (the generated APPLICABLE_METHODOLOGY RMEDO Carrier directories))`

## Definition of Done

the Task is **not done if** (a dry-run has an unresolved **or** stale-approved conflict **or** two identical dry-runs differ **or** compilation selects CAP, Implementation, Draft, Archived, Done, **or** Canceled Atoms **or** application does not replace **only** generated RMEDO output **or** a generated Carrier lacks exact source provenance **or** deletion prevents deterministic regeneration **or** compiler tests fail).

## Details

record the repaired source-frontier digest, generated-tree digest, selected Atom count, conflict count, and test result separately from source authority.
