---
atom_id: CA-D-542
content_role: Delivery
type: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 18:37:19 +0000"
subjects:
  governs: "Tool/WORKFLOW_OPERATIONS/APPLICABLE_METHODOLOGY/Carrier"
  depends_on: [Tool, Methodology Source, Atom Revision, Projection, Operator, Journal, Journal Record]
relations:
  delivery_for: [CA-R-1840, CA-R-1841, CA-R-1842]
---
# Summary

Encode inspectable source, decision, Journal, publication, and prior-output provenance.

## Scope

The result/receipt Carrier contract for dry run, blocked result, atomic publication, and recovery.

## Claim

The compiler result **must** make exact source, decision, Journal, output, and prior-output state independently inspectable without treating a Projection or configuration index as source authority.

## Details

Every result contains `outcome`, `operation`, `source_frontier_digest`, `source_frontier`, `conflicts`, `decision_provenance`, `publication`, `evidence_refs`, and shared `run_receipt_refs`. Every frontier row contains `source_layer`, optional `extension_id` and `extension_revision`, `source_carrier_path`, `source_atom_id`, `source_atom_revision`, `source_sha256`, and `original_relations_digest`. Every decision row contains conflict ID, proposal/selection, Operator identity, canonical Journal record reference and digest, and the bound frontier digest; an optional configuration-index reference is marked `non_authoritative`.

For each published Carrier, `publication.output` records output path, output digest, and the exact original-source binding. The rendered Carrier preserves the original source frontmatter/body/Relations and records only its generated projection binding. A blocked/failed result includes `prior_output_state: "preserved" | "not_started" | "uncertain"`, exact findings, and no success receipt. A successful result contains atomic transaction ID, complete output digest, and canonical Journal publication reference. It never reports a source mutation as a compiler effect.

### Sources

- CA-R-1840 through CA-R-1842; CA-O-155 v2 and CA-O-157 v2.
- CA-P-1442 v1, fidelity and canonical-Journal boundary.
