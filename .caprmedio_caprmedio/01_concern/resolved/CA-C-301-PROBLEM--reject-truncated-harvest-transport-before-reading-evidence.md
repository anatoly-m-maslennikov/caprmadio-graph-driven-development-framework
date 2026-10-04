---
atom_id: CA-C-301
content_role: Concern
type: Problem
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: resolved
subjects:
  governs: "Harvest output transport truncation"
  depends_on:
    - "Project"
version: 1
updated_at: "2026-10-04 11:00:21 +0400"
relations:
  concern_about:
    - CA-P-1260
  relates_to:
    - CA-A-978
---
# Summary

Reject truncated harvest transport before reading evidence

## Concern

Oversized combined native text/metadata output was truncated and could not be parsed. Such output cannot establish semantic coverage. This is a transport defect in the harvesting interaction, not source unavailability or Atom failure.

## Evidences

First full payload transport reported22825 original tokens above the22000 output cap; parsing failed atJSON position88012. An earlier attempt also rejected the truncation warning as invalid JSON. A combined metadata/status output likewise showed an explicit truncation marker and was not used as complete evidence. Recovery omitted duplicate full-text copies, used compact per-part fingerprints and separate bounded displays. All40 native messages/20625 characters, raw/text hashes, roles/timestamps and selected aggregate matched; two bounded20-message displays and exact context spans were then read completely. No truncated evidence was counted as harvested; source bytes unchanged.

## Blast radius

Only root1260 transport and binding displays. Resolved by compact extraction and bounded display with explicit completeness checks. A978 retains all40 full texts/dispositions and exact prior contexts. No methodology, implementation, settings, services or external state changed.
