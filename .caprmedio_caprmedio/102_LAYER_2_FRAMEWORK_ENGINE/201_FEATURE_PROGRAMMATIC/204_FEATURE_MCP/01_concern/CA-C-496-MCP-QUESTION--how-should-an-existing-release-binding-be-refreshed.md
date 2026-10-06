---
atom_id: CA-C-496
content_role: Concern
type: Question
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-06 06:38:52 +0000"
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

The Operator has been asked about private publisher use. Clarification is required because the currently implemented publisher supports initial publication only. Code repairs and diagnostics can finish independently; no refresh or Release dispatch is authorized by this Concern itself.
