---
atom_id: CA-C-389
content_role: Concern
type: Problem
current_scope_unit: caprmedio
claim_target_scope_unit: METHODOLOGY_SOURCES
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Validation Workflow and Step Carrier conformance"
  depends_on: [Operations, "Markdown Atom Carrier/Structure"]
version: 1
updated_at: "2026-10-04 13:46:41 +0000"
relations:
  concern_about: [CA-O-080, CA-O-088]
  relates_to: [CA-P-1420, CA-A-1140, CA-D-479, CA-C-376]
---
# Summary

Normalize validation Workflow and Step carriers

## Concern

Current CORE source O080 v4 and O088 v3 use Claim rather than registered Operation and lack Details. D479 v6 requires exactly Summary/Operation/Details for every Operations Carrier; a Workflow/Step Type does not waive those markers. Readable behavior remains semantically covered, not Carrier-compliant.

## Evidences

Both current source bodies were read completely for the bound R0160 mechanical-validation intent. The one saved check at2026-10-04T13:45:51.801361+00:00 confirmed their exact unchanged bytes and observed layout discrepancy, and this Concern's strict registered carrier. Exact source paths/revisions/fingerprints:

- CA-O-080 v4: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/ATOM_CARRIER_VALIDATION/CA-O-080-CORE_META_MODEL-WORKFLOW--validate-atom-carriers.md`; SHA256 `f89fc7a5982663c7dbcc372ecc8d62f49c7e591dd59881b287e1460ade89d555`.
- CA-O-088 v3: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/ATOM_CARRIER_VALIDATION/CA-O-088-CORE_META_MODEL-STEP--check-selected-atoms.md`; SHA256 `daddb9064368a8f35c5c0c3693341a8d94977091ccd085ac10faacfdf7a432fc`.

Each contains exactly one literal Summary and Claim, zero Operation/Details. A1140 retains the one-Step graph and unchanged O087 input/result binding; no source bytes changed. O087's same issue is already retained by C376 and is not duplicated. This is current direct Carrier evidence, not a historical report or runtime defect.

## Blast radius

Only these two sources. Root may bind separately authorized registered-heading normalization and independent preservation/Layout proof while retaining exact Step/Action references, selection inputs, result/report payload, valid/invalid/incomplete/error terminals, no automatic retry/repair/back edge and all existing authority. Pure Carrier refinement preserves identity/Summary/Version and refreshes updated_at; any semantic change requires separate authority. No source/parent/runtime/Git/Journal mutation occurs here. C389 stays Active; bounded comparison may close without claiming source conformance or whole-family readiness.
