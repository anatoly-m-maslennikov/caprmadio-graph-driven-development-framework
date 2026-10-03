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
version: 2
updated_at: 2026-08-31 21:41:58 +0400
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

## Completion Evidence

two byte-identical dry-runs selected 632 active RMEDO Atoms from the exact CORE_META_MODEL and LOCAL_CONFIGURATION frontier with source-frontier digest `1807df50a636b5be387f25452fb9dc4154a315c7413ec138732796b09edc1d39`, zero conflicts, zero unresolved conflicts, zero stale approval requirements, and zero diagnostics.

the compiler atomically applied 632 generated RMEDO Carrier files with generated-tree digest `e3f669ef8ba3d2492eb6aecbb29f563462780cf84457135f576eebaac98968bd`. The generated CAPRMEDIO-META-REQU-627 Carrier projects exact Core Meta-Model source revision 11 and source digest `7f4407826c7bcec1d0ab973efd39fd6a0613e986c7702825c789e3e5ab865fed`; its source path resolves exactly. all nine compiler tests pass. the non-authoritative execution evidence is stored in `execution_evidence/CA-P-934-applicable-methodology-recompilation-after-graph-authority-repair.projection.json`.
