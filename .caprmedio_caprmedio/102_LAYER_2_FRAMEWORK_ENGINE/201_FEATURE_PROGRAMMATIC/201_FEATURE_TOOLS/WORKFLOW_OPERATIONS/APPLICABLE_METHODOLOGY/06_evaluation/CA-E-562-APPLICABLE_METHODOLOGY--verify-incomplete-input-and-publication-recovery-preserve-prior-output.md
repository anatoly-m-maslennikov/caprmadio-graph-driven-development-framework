---
atom_id: CA-E-562
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
  depends_on: [Tool, Methodology Source, Carrier, Projection, Journal, Workflow Run]
relations:
  evaluation_for: [CA-R-1839, CA-R-1842, CA-M-226]
---
# Summary

Plan functional proof that incomplete inputs and publication recovery preserve prior output without replaying authority edits.

## Scope

Functional incomplete-frontier, injected publication-failure, and recovery cases.

## Claim

An implementation **must** prove that incomplete input and failed or uncertain publication preserve the prior projection and never replay a source correction or claim a completed Journal publication.

## Details

Given a known prior output, exercise missing source, malformed carrier, inaccessible activated Extension, changed source during staging, newly added source during currentness validation, and incomplete conflict assessment. Every case must block before output mutation and return the exact finding. Inject a failure during multi-role publication and assert byte-for-byte restoration of the prior complete projection, no partial role tree, and no success receipt.

For recovery, provide the failed publication evidence and unchanged current inputs: the Tool may retry staging/publication only, retaining the same source and decision provenance and shared Run references. If any input or provenance changes, recovery must return to selection and assessment; it must not replay an external source correction. Record no completed publication until the atomic output and canonical Journal receipt both exist. This carrier records planned functional proof, not a runtime pass.

### Sources

- CA-R-1839; CA-R-1842; CA-M-226 v7; CA-O-157 v2; CA-O-009 v5.
