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
version: 2
updated_at: 2026-08-30 20:03:41 +0400
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

## Completion Evidence

two byte-identical dry-runs selected 632 active RMEDO Atoms from the exact CORE_META_MODEL and LOCAL_CONFIGURATION frontier with source-frontier digest `b7c21b03fcbcb6e2e29d39c19d1c423aae0c3c408da466eecfbf9fd0e39d0c81`, zero conflicts, zero unresolved conflicts, zero stale approval requirements, and zero diagnostics.

the compiler atomically applied 632 generated RMEDO Carrier files with generated-tree digest `b691b68b5f507407216cefe8c52cb8d707b4a4a273c35f733d2f1f3fa5b7ba41`; each generated Carrier has a source path that resolves to its selected source. all nine compiler tests pass. the non-authoritative execution evidence is stored in `execution_evidence/CA-P-930-applicable-methodology-recompilation.projection.json`.
