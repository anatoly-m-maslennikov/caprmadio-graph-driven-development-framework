---
atom_id: CA-C-496
content_role: Concern
type: Question
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: resolved
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-06 10:46:48 +0000"
subjects:
  governs: "Release Binding Refresh"
  depends_on: [Operator, Manifest, Source Carrier, Release Version, Journal, MCP]
relations:
  concern_about: [CA-R-1882, CA-M-339, CA-D-576, CA-P-1117]
---
# Summary

How should an existing Release binding be refreshed

## Concern

Should the existing private, journaled publisher gain a plan-first refresh operation for the already published sixteen-route Release binding after an accepted source revision?

## Evidences

- the N8 repair updates admitted Release authority. The saved binding retains the predecessor pins, and current MCP source admission correctly refuses it.
- CA-R-1882, CA-M-339 and CA-D-576 admit only initial fifteen-to-sixteen-route publication. The current publisher cannot refresh an existing sixteen-route binding; resetting it to fifteen routes or hand-editing it would bypass that boundary.
- the proposed bounded extension preserves all fifteen non-Release routes, query admissions and source-registry authority, derives the Release record only from current accepted sources, previews exact input/output bytes, and uses the existing Operator authorization, atomic publication and canonical Journal lifecycle. Actual Release dispatch remains through MCP and all release gates remain required.

## Blast radius

Fresh source-bound Release dispatch and later changes to Release authority. Historical N5–N8 requests, installed N and their evidence must remain unchanged.

## Details

the Operator approved the guarded capability. R1882/M339/E582/D576 v3 were independently accepted and saved at 6b9ae7a5c; the implementation and regression proofs were independently accepted and saved at d24eb8d89. this question is answered, not proof of actual publication. the first actual attempt was blocked before any write by the separate pre-existing Journal-history gap recorded in CA-C-497. CA-P-1780 remains Active until its actual publication and Journal proof succeed.
