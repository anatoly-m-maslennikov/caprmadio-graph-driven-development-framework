---
atom_id: CA-E-582
content_role: Evaluation
type: QA Case
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-05 18:02:02 +0400"
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

Every publisher realization **must** prove that plan mode has no effect and trusted execution publishes only the exact verified fifteen-to-sixteen route successor with truthful, resumable canonical Journal evidence.

## Details

1. Using a functional fixture with a current canonical fifteen-route manifest and the source-owned current D572 admission, verify plan mode performs no write, creates no Run or Journal event, and returns the proposed addition and digest evidence. Verify execute preserves all fifteen route rows and `query_source_admissions`; preserves the selected-source freshness fields and binding reference while recomputing only its selected-binding digest; adds exactly one `release_version` row and one Release admission; recomputes the canonical manifest digest; and passes exact published-byte readback through the existing loader.
2. Reject a missing, malformed, stale, noncanonical, non-fifteen-route, or already-sixteen-route input; an altered existing row, source-freshness value, query admission, current admission frontier, digest, or authorization; and any source or output reference to the obsolete Applicable Methodology projection. Reject an unregistered Operator, a grant bound to another root/input bytes/frontier/candidate digest, and every caller-supplied authorization boolean, callback, or lifecycle record. Each rejection leaves the canonical manifest unchanged and does not dispatch O164, create a Release Version Run, queue work, build or retire an image, install a runtime, or claim full-release acceptance.
3. Verify the adapter seals the complete pending publication intent before replacement. Verify its normal Journal record is existing `completed` `governed_project_change` evidence with the exact target path, digest, and prior-event link; where no prior terminal evidence exists, verify the required recovered `governed_project_state` observation. Verify `result.version` advances the Journal carrier history only, while the Projection remains versionless and records only its completed-rebuild `updated_at`.
4. Inject failures before replacement, after replacement before readback, and after verified readback before Journal finalization. Confirm the first leaves the canonical file unchanged. For every later restart, confirm exact candidate bytes finalize only the sealed original Journal event without another replacement; nonmatching bytes remain ambiguous and never replay the mutation. Confirm the publisher never writes a Journal directly and never creates a second executor, Workflow Run, or lifecycle ledger. This is planned functional proof, not runtime or full-release acceptance.
