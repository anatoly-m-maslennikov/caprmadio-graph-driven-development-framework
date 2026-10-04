---
atom_id: CA-C-429
content_role: Concern
type: Problem
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: resolved
version: 2
updated_at: "2026-10-04 18:16:52 +0000"
subjects:
  governs: "Atom Replacement/Admission Evaluation"
  depends_on: [Atom, Artifact/Revision, Plan, Journal]
relations:
  concern_about: [CA-E-247, CA-O-031]
---
# Summary

Distinguish pre-Run denial from recorded Run failure

## Concern

E247's unchanged-Journal denial assertion does not explicitly distinguish a never-started Action Run from an actual started rejected or failed Run.

## Evidences

P1472 found the direct unauthorized-apply case. Shared accepted Run authority requires actual started rejected/failed Runs to retain truthful records. Denial before any Run starts can leave the Journal unchanged; no new Journal owner or extra Workflow is required.

## Blast radius

### Resolution

P1481 saved E247v12 with the pre-Run denial qualification and complete archived v11. P1483 independently accepted the precise delta: unchanged Journal applies only before any Run starts; actual started rejected/failed/parent Runs retain truthful evidence. Source test-contract defect resolved, not implemented runtime proof.

### Original impact

The exact bound repair and independent review precede affected source acceptance. Preserve meaningful source/history and truthful proof; no runtime completion is claimed.
