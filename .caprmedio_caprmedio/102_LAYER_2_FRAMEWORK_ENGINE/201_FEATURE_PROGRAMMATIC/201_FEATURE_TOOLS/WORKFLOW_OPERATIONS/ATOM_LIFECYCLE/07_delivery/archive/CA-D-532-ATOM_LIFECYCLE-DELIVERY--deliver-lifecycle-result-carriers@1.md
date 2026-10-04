---
atom_id: CA-D-532
content_role: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: "Workflow Operations/Atom Lifecycle/Result Carrier"
  depends_on: ["Artifact/Carrier", "Journal/Record"]
version: 1
updated_at: "2026-10-04 19:29:30 +0000"
relations:
  delivery_for: [CA-R-1826, CA-R-1828]
---
# Summary

Deliver lifecycle result carriers

## Scope

The returned lifecycle dispatch record and its handoff to native Tools and shared Run support.

## Claim

The result carrier preserves request, sealed/observed Carrier data, operation/model selection, authorization, diagnostics, exact native outcome, history/lineage, and known/unknown effects. It hands these facts to shared Run support without creating a second event schema or asserting persistence that did not occur.

## Details

Status-transition diagnostics distinguish observed broken references from an unperformed or failed transition, and identify the separate repair handoff where it is needed.
