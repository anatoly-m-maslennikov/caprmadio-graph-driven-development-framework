---
atom_id: CA-E-582
content_role: Evaluation
type: QA Case
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 17:18:46 +0400"
subjects:
  governs: "MCP/additive Release manifest publication"
  depends_on: [MCP, Projection, Manifest, Workflow, Step, Action, Operator, Run, Journal]
relations:
  evaluation_for: [CA-R-1882, CA-M-339, CA-D-576]
---
# Summary

Verify additive Release manifest publication

## Scope

Functional proof of the publisher's plan, exact successor, readback, and non-dispatch boundaries.

## Claim

Every publisher realization **must** prove that plan mode has no effect and authorized execution publishes only the exact verified fifteen-to-sixteen route successor.

## Details

Using a functional fixture with a current canonical fifteen-route manifest and D572's exact current admission, verify plan mode performs no write, creates no Run or Journal event, and returns the proposed addition and digest evidence. Verify execute preserves all fifteen route rows and `query_source_admissions`; preserves the selected-source freshness fields and binding reference while recomputing only its selected-binding digest; adds exactly one `release_version` row and one Release admission; recomputes the canonical manifest digest; and passes exact published-byte readback through the existing loader.

Reject a missing, malformed, stale, noncanonical, non-fifteen-route, or already-sixteen-route input; an altered existing row, source-freshness value, query admission, D572 pin, P1622 pin, O164 graph pin, ordered Step/Action sequence, Release RMED pin, digest, or authorization; and any source or output reference to the obsolete Applicable Methodology projection. Each rejection leaves the canonical manifest unchanged and does not dispatch O164, create a Release Version Run, queue work, build or retire an image, install a runtime, or claim full-release acceptance.

Inject failures before replacement, after replacement before readback, and after verified readback before shared recording. Confirm the first leaves the canonical file unchanged; the later cases report only the observed partial state and recording requirement. Confirm the publisher never writes a Journal directly and never creates a second executor or lifecycle ledger. This is planned functional proof, not runtime or full-release acceptance.
