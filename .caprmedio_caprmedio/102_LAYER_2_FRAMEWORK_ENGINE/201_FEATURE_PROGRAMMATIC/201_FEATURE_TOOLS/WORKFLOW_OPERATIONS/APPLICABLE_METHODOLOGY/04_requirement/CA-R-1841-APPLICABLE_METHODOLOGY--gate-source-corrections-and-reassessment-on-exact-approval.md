---
atom_id: CA-R-1841
content_role: Requirement
type: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 18:37:19 +0000"
subjects:
  governs: "Tool/WORKFLOW_OPERATIONS/APPLICABLE_METHODOLOGY"
  depends_on: [Tool, Workflow, Step, Action, Methodology Source, Operator, Journal, Journal Record, Atom Revision, Projection]
relations:
  relates_to: [CA-R-1839, CA-R-1840, CA-O-011, CA-O-154, CA-O-155, CA-O-156, CA-O-006, CA-O-007, CA-O-008]
---
# Summary

Gate source correction and conflict-selection dispositions on exact canonical-Journal approval, then reassess.

## Scope

The CA-O-154 through CA-O-156 decision and correction boundary; source mutation remains outside the compiler.

## Claim

`COMPILE_APPLICABLE_METHODOLOGY` **must not** edit methodology authority and **must** accept a conflict selection or correction result only with exact current Operator, source, and Journal provenance, followed by reselection and reassessment.

## Details

For a decision, the Tool requires the exact conflict ID, proposal or candidate selection, source-frontier digest, Operator identity, canonical Journal decision reference, and receipt evidence that the decision is current and unambiguous. A stale, partial, missing, mismatched, rejected, ambiguous, or revoked decision is `blocked`. A Project Configuration approval file may be a non-authoritative lookup index only when it resolves to that exact canonical Journal decision; it cannot independently authorize selection or correction.

When the accepted disposition requires source correction, the Tool returns the source-owner correction request and awaits an independently produced owned-source change receipt. It has no `edit_source` or projected-Claim-fix mode. No compiler-side effect, output change, approval cache, or inferred delegation may alter source authority. A successful external source change, a non-mutating selection decision, a failed correction, or a recovery attempt requires a fresh CA-R-1839 selection and CA-R-1840 assessment before publication. Failed or partial correction preserves the prior projection and reports actual known effects; it never resumes from the former assessment.

The Tool returns `{ outcome: "reassess_required" | "blocked", decision_provenance, correction_request_or_receipt, evidence_refs }`. It does not create a duplicate approval Atom or duplicate shared Run-support behavior.

### Sources

- CA-O-011 v12, CA-O-154 v2, CA-O-155 v2, and CA-O-156 v2.
- CA-O-006 v6, CA-O-007 v6, and CA-O-008 v11.
- CA-P-1442 v1 and CA-A-1142 v2, W13 decision/Journal boundary.
