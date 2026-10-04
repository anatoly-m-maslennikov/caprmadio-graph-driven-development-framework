---
atom_id: CA-C-313
content_role: Concern
type: Problem
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: resolved
subjects:
  governs: "Scoped harvest diagnostic exclusions"
  depends_on:
    - "Artifact"
version: 1
updated_at: "2026-10-04 12:27:44 +0400"
relations:
  concerns:
    - CA-P-1288
---
# Summary

Match numbered harvest Carriers in diagnostic exclusions

## Concern

The ephemeral saved-Carrier diagnostic matched exclusion IDs only at basename start, so it did not exclude numbered Plan Carriers during another Agent's incomplete persistence.

## Evidences

Actual exclusion invocation still checked P1293. Root changed only this ephemeral diagnostic selector to match the ID after an optional navigational prefix. It then exposed A1008's real missing version, which was returned to the owning Agent with P1293's missing fields. Root P1288's four actual saved Carriers, native messages/parts/fingerprints and frontier passed a separate scoped check; no incomplete excluded Carrier is counted as a global pass.

## Blast radius

Ephemeral harvest diagnostic only; no delivered Tool or methodology authority change. Full shared check remains required after owning Agents finish.
