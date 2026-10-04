---
atom_id: CA-R-1842
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
  depends_on: [Tool, Workflow, Step, Action, Methodology Source, Atom Revision, Carrier, Projection, Journal]
relations:
  relates_to: [CA-R-1839, CA-R-1840, CA-R-1841, CA-O-011, CA-O-157, CA-O-009, CA-M-226]
---
# Summary

Publish only a current resolved frontier atomically while preserving the prior output on failure.

## Scope

The CA-O-157 projection-publication boundary after a current conflict-free reassessment.

## Claim

`COMPILE_APPLICABLE_METHODOLOGY` **must** atomically publish only the complete current resolved frontier and **must** preserve the entire prior Applicable Methodology output when preparation, currentness validation, publication, or recording fails.

## Details

Immediately before commit, the Tool revalidates every selected source path, Atom ID, Revision, byte digest, source relation, decision provenance when applicable, and final source-frontier digest. It stages the full replacement output, including all governed RMED role directories, before one recoverable publication transaction. Any changed, newly discovered, missing, malformed, incomplete, stale, unresolved, or unsupported input blocks publication before output mutation. A transaction, filesystem, output-fidelity, or Journal-recording failure leaves the prior output byte-for-byte intact and reports whether publication was not started, rolled back, or has an explicitly uncertain recovery state.

Each published Carrier retains its original authored frontmatter, body, and Relations unchanged and adds only the non-authoritative projection binding required to identify its original source Carrier, Atom ID, Revision, and digest. The output is a derived Projection, not source authority. Successful publication returns the exact published output digest and canonical Journal/Run receipt references; it neither edits source authority nor substitutes a generated file for a source correction.

### Sources

- CA-O-011 v12 and CA-O-157 v2; CA-O-009 v5.
- CA-M-226 v6; CA-P-1442 v1; CA-A-1142 v2, W13 fidelity boundary.
