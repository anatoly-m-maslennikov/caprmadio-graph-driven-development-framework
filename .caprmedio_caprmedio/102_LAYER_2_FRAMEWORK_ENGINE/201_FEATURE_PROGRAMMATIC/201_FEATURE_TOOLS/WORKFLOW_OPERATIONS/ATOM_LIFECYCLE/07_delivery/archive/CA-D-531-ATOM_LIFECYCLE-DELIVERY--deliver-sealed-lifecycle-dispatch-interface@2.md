---
atom_id: CA-D-531
content_role: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Workflow Operations/Atom Lifecycle/Dispatch Interface"
  depends_on: ["Tool", "Authorization", "Atom"]
version: 2
updated_at: "2026-10-04 23:01:23 +0400"
relations:
  delivery_for: [CA-R-1825, CA-R-1827]
---
# Summary

Deliver sealed lifecycle dispatch interface

## Scope

The future Project-local MCP entrypoint contract; no executable carrier is supplied by this specification.

## Claim

The entrypoint is one selected route under CA-D-527 and accepts no independent outer request/result. Its CA-D-527 `request.parameters` carries the typed lifecycle boundary: requested operation/result; exactly one complete new target Carrier set for Create, or exactly one complete current target/predecessor Carrier set for Update, Replace, or Change Status; and, for Replace, the complete accepted set of one or more distinct successor Carrier sets. It also carries the exact target/predecessor identity and locator, expected current Version/digest, proposed result or status mapping, and current qualified status model and model revision. `mode` remains preview unless the CA-D-527 outer request explicitly executes with its sealed operator authorization; an adapter envelope does not add authority.

The entrypoint returns CA-R-1828 only as the route-specific payload of CA-D-527's result. CA-D-527 remains the sole owner of outer disposition, started Run identities/definition bindings, canonical receipts or recording blocker, and retry disposition. A Summary-changing Update returns a terminal non-effect `replace_handoff`; Replace is a separately admitted new outer request with fresh exact definitions, currentness, and permission, never inherited Update permission.

## Details

For an authorized Archive, the model-admitted status transition proceeds even when it newly breaks Relations. Diagnostics enumerate every newly broken Relation and active referrer and expose only a separate repair handoff; the entrypoint never silently repairs, retargets, or suppresses the transition.
