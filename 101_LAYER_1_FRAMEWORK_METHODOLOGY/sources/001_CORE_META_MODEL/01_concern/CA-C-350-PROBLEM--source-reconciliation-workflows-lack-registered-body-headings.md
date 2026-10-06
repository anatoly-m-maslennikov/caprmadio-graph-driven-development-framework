---
atom_id: CA-C-350
content_role: Concern
type: Problem
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Source Reconciliation Workflow Carrier layout"
version: 1
updated_at: "2026-10-04 16:48:00 +0400"
relations:
  concern_about: [CA-O-010, CA-O-011]
  relates_to: [CA-D-479, CA-P-1340, CA-A-1058]
---
# Summary

Current source Workflows CA-O-010 v7 and CA-O-011 v10 lack the registered Operation body headings required by CA-D-479 v6.

## Concern

Neither Carrier has literal `# Summary`, `## Operation` or `## Details`. Their executable clauses are present, but prose position/descriptive headings cannot substitute for the registered Property markers. This is a confirmed source Carrier layout gap, not a semantic flow defect or an implementation failure.

## Evidences

CA-A-1058 compares both full live source files with CA-D-479 v6. Exact later-authoring targets:

- `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-010-CORE_META_MODEL-WORKFLOW--reconcile-sources.md` — v7, SHA-256 `fe23f033b0c68300ba3e63cdab27e574a81b4e4781c79a0ea06d1f659da55e94`; descriptive H1, `## Steps`, `## Transitions`.
- `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-011-CORE_META_MODEL-WORKFLOW--bind-source-reconciliation-to-applicable-methodology.md` — v10, SHA-256 `7afcae57fc1496c5f01e74ec39735b76b7df9c0189f72cd4db509a4ba787cf83`; descriptive H1 and unsectioned binding table.

## Blast radius

Limit future repair to these two CORE_META_MODEL source Carriers. Add the required Summary/Operation/Details markers; keep executable text inside Operation, with Steps/Transitions as subordinate headings and Details allowed empty. Preserve clause order and all inputs, references, cardinalities, transitions, stops, confidence/authorization gates, accepted retry budget, approval/frontier-digest binding, exact source identity/Revision/owner/Claim/bytes/form preservation, scope and status. A demonstrably meaning-preserving format change retains O010 v7/O011 v10 and refreshes updated_at; any substantive change requires separately authorized versioning.

No repair is performed by P1340. Root must bind later authoring and independent preservation/layout checks before claiming Carrier compliance. This typed, explicit follow-up permits bounded reconciliation acceptance only; it does not establish whole-stage authoring or implementation readiness.
