---
atom_id: CA-D-532
content_role: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Workflow Operations/Atom Lifecycle/Result Carrier"
  depends_on: ["Artifact/Carrier", "Journal/Record"]
version: 2
updated_at: "2026-10-04 23:01:23 +0400"
relations:
  delivery_for: [CA-R-1826, CA-R-1828]
---
# Summary

Deliver lifecycle result carriers

## Scope

The returned lifecycle dispatch record and its handoff to native Tools and shared Run support.

## Claim

The route-specific lifecycle payload in CA-D-527's one result preserves the typed request identity; complete sealed and observed target/predecessor Carrier sets and, for Replace, every successor Carrier set; expected and observed Version/digest; operation/model/currentness selection; authorization; diagnostics; exact native outcome; history/lineage; and known/unknown effects. It supplies those facts to the shared result without creating an outer result, a second Event schema, or an assertion of persistence that did not occur.

CA-D-527 alone carries the outer disposition, actual started Run IDs/definition bindings, canonical receipts or recording blocker, and retry disposition. When persistence or verification is incomplete, this payload marks the affected carrier/effect unknown or unverified and the shared result uses `recording_pending`; delivery retries the canonical recording path only and never replays an effect. Unstarted preview, decline, and block results invent no Run/Event identity.

## Details

Status-transition diagnostics distinguish observed broken references from an unperformed or failed transition. An authorized Archive that newly breaks Relations retains the actual transition, lists every newly broken Relation and active referrer, and identifies a separate repair handoff without automatic repair or retargeting.
