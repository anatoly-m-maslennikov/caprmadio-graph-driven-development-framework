---
atom_id: CA-C-324
content_role: Concern
type: Problem
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: resolved
subjects:
  governs: "Harvest proof schema assumptions"
  depends_on:
    - "Artifact"
version: 1
updated_at: "2026-10-04 14:13:49 +0400"
relations:
  concern_about:
    - CA-P-1306
    - CA-A-1024
    - CA-P-1308
---
# Summary

Correct harvest proof schema assumptions

## Concern

The root's bounded native/saved proof initially expected original_parts in every future selected binding record. P1308 correctly binds those records by exact native metadata while retaining full required antecedents and first/following originals. A conditional repair of the proof then produced an invalid Python semicolon before if.

## Evidences

The first proof returned nonzero after the independently successful P1301 proof, raising KeyError for a future metadata-only selected record. The syntax-invalid attempt returned nonzero without any executed proof. Neither failed attempt was counted as a worker proof or source-reading pass.

The corrected proof requires complete original_parts/full_text for every saved A1024 source record and all full saved contexts; it permits exact metadata-only future selected records and opens each directly from its frozen native source. It verifies raw/text/role/time fingerprints, prefix hashes, per-source/global aggregates, all98 substantive dispositions, current/next disjointness and full following frontier. Both the current98/context2 and next60/context2 native/saved proofs then passed. No missing source originals or Tool implementation defect was inferred.

## Blast radius

Root integration provenance checking for P1306/A1024 and its next P1308 only. The saved source evidence and coverage did not change. This repairs the ephemeral proof's schema assumption; it does not implement a framework Tool, add a semantic recheck stage, reset a leaf clock or hide its overrun.
