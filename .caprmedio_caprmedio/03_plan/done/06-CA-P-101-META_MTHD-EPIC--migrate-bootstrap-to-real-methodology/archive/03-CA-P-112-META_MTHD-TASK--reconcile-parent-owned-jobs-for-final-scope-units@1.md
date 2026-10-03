---
atom_id: CA-P-112
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - CAPRMEDIO Scope Unit/Job
    occurrent:
      - Job Reconciliation
  depends_on:
    occurrent:
      - CA-P-103
version: 1
updated_at: 2026-08-26 17:42:48 +0400
autonomous_confidence_threshold: 98
relations: {}
---
# Reconcile Parent-Owned Jobs for Final Scope Units

**when** CA-P-103 is Done, **then** the Assignee **must** reconcile at least one accepted parent-owned Job for every final Scope Unit without inventing a Job Claim from local Scope Requirements or topology authority.

## Scope

`((CAPRMEDIO and every final descendant Scope Unit established by CA-P-103) union (all active and draft Job Atoms and direct-parent-owned scope or purpose Atoms in the frozen CA-P-102 source frontier whose Claim Scope is one of those Scope Units) union (the three Job Atom drafts whose Claim Scopes are CORE_META_MODEL, INSTALLED_EXTENSIONS, and LOCAL_CONFIGURATION))`

## Definition of Done

the Task is **not done if** (CAPRMEDIO lacks at least one Operator-owned Job **or** any other final Scope Unit lacks at least one direct-parent-owned Job **or** any Job owner differs from the Operator for CAPRMEDIO or the direct Structural parent for another Scope Unit **or** a Job Claim is inferred only from the target Scope Unit's local Requirements **or** a topology-only Claim is converted into a Job **or** any accepted predecessor Job Claim changes during reconciliation **or** any materialized source-Layer Job differs from its accepted draft Claim **or** any predecessor Job lacks exactly one successor, retention, archive, or retirement disposition **or** any missing or ambiguous Job is resolved below the Autonomous Confidence Threshold).

## Details

preserve accepted Job Claims and ownership. materialize the accepted CORE_META_MODEL, INSTALLED_EXTENSIONS, and LOCAL_CONFIGURATION Job drafts under APPLICABLE_MTHD_SOURCES without broadening their Claims. treat direct-parent-owned purpose authority as a Job predecessor only when its Claim already states the intended work of the target Scope Unit. do not derive a Job from topology, child membership, or the target Scope Unit's highest local-tier Requirements. request Operator authority for every final Scope Unit whose Job is missing or ambiguous.
