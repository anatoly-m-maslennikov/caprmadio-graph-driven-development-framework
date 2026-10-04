---
atom_id: CA-R-1827
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Workflow Operations/Atom Lifecycle/Sealed Target"
  depends_on: ["Atom", "Artifact/Carrier", "Atom/Relation", "Authorization"]
version: 1
updated_at: "2026-10-04 18:30:23 +0000"
relations:
  relates_to: [CA-O-127, CA-O-128, CA-O-129, CA-O-145, CA-O-067, CA-R-866, CA-R-868, CA-R-1041]
---
# Summary

Validate one sealed lifecycle target

## Scope

Single-target/predecessor validation and Relation diagnostics before a selected lifecycle operation is delegated.

## Claim

The dispatcher **must** accept exactly one resolved target and, for Replace, exactly one resolved active predecessor and the complete native successor Carrier set. It seals identity, path, filename, expected Version/digest, requested operation/result, and applicable status-model revision before delegation. It preserves the native Create/Update/Replace Carrier and successor-set guards. It checks active inbound and outgoing Relations whose targets would become invalid, unresolved, or semantically inconsistent after the proposed result; it returns every detected broken active inbound/outgoing reference as a diagnostic and does not silently retarget or repair it.

Preview is the default and writes no Carrier, history, or effect. Mutation requires an explicitly authorized Project-local MCP request with the sealed target and delegation envelope; a stale seal, missing authorization, invalid target/predecessor, or failed structural/currentness check prevents mutation. A model-admitted authorized Change Status, including Archive, remains dispatchable when its resulting active references are broken: it performs the admitted status transition and reports those broken references and active referrers for the separate authorized repair Workflow; diagnostics are not automatic retargeting or a blanket lifecycle veto.

## Details

Bulk targeting, generalized relation repair, and arbitrary destructive changes are outside this one-target slice.
