---
atom_id: CA-C-320
content_role: Concern
type: Problem
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: resolved
subjects:
  governs: "Native evidence transport completeness"
  depends_on:
    - "Artifact"
version: 1
updated_at: "2026-10-04 13:41:16 +0400"
relations:
  concern_about:
    - CA-P-1300
---
# Summary

Reject incomplete packet reading transports

## Concern

Three P1300 read attempts were rejected before admitting source reading: an oversized combined output and two invalid script-input attempts. The initial generic guard did not distinguish their failure reasons.

## Evidences

The root rejected nonzero or truncated outputs before parsing or counting their text. It then decoded serialized JSON explicitly and split native reads into three whole-record groups of nine. All27 whole texts and original parts, plus all nine bound full antecedents, were successfully loaded. No failed read became an evidence disposition or pass. Native/saved proof still governs final admission.

## Blast radius

P1300 reading only. Corrected transports restored complete access; no source was unavailable, no snapshot changed, and no framework Tool or runtime code was modified. The original execution clock was not reset.
