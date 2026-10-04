---
atom_id: CA-E-561
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-04 23:02:50 +0400"
subjects:
  governs: "Tool/WORKFLOW_OPERATIONS/APPLICABLE_METHODOLOGY"
  depends_on: [Tool, Operator, Journal, Journal Record, Methodology Source, Projection]
relations:
  evaluation_for: [CA-R-1841, CA-R-1842]
---
# Summary

Plan functional proof that stale or noncanonical decision provenance cannot authorize selection or correction.

## Scope

Functional approval-currentness and provenance cases for conflict selection and source correction.

## Claim

An implementation **must** reject every approval that is not the exact current Operator decision recorded in the canonical Journal for the assessed source frontier.

## Details

Start from an assessed conflict and test a missing, stale-digest, mismatched-conflict, mismatched-proposal, mismatched-selected-source, ambiguous, rejected, revoked, or Journal-missing decision. Each case must return `blocked`, name the failing provenance binding, create no source edit or output mutation, and preserve the prior output. A TOML approval index lacking its matching canonical Journal record must fail equivalently.

Then provide one exact Operator decision with its Journal record and source bindings, change one selected source, and assert that the old decision becomes stale and apply remains blocked until fresh selection and assessment. Assert that an external authorized source correction receipt likewise requires reselection/reassessment rather than enabling direct publication. This carrier records planned functional proof, not a runtime pass.

### Sources

- CA-R-1841; CA-R-1842; CA-O-155 v2; CA-O-156 v2; CA-P-1442 v1.
