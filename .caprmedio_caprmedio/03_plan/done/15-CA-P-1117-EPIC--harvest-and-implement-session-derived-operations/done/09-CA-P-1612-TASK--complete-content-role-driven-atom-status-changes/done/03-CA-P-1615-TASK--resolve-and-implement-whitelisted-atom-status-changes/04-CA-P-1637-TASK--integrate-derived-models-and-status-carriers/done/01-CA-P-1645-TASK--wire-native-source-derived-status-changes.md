---
atom_id: CA-P-1645
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
subjects:
  governs: "Wire native source-derived status changes"
  depends_on: [Atom, Status, Carrier, Tool, Manifest, Methodology, Evaluation, Journal]
version: 1
updated_at: "2026-10-05 03:19:26 +0000"
relations:
  is_decomposition_of: [CA-P-1637]
  blocks: [CA-P-1647]
---
# Summary

Wire native source-derived status changes

## Objective

Within <=15 minutes, wire native source-derived status changes.

## Details

Own lifecycle_intents.py and narrow necessary atom_operations.py changes only. Reuse accepted authoritative_status_models.py and D466/D461/D565 instead of caller-authored whitelist/transition matrix. Supply pure preflight_atom_lifecycle(root, operation, parameters) for shared preview/freeze/dispatch; resolve actual non-Active current carriers, destination/source currentness, no-op before effects, collisions, version/body/history and precise refusal diagnostics. Coordinate P1646 golden tests. Preserve external dirt. The Operator's same-Atom Draft removal decision is bound by accepted D446@7/D288@12; future identity assignment leaving Draft remains separately gated. No shared orchestrator/MCP/manifest edits.

Read the accepted parent source pins and current worktree before changes. Respect external file ownership, C447 denied relocation and C449 host/image gate; the existing development worker is not new immutable-image proof.

## Definition of Done

Save bounded output/current exact evidence and truthful remaining coverage. Partial source/helper/mock acceptance does not complete the parent or Epic.

## Result

Native owner /root/prepare_lifecycle_golden_inputs saved source-derived change_status preflight/effects in lifecycle_intents.py (15d15e7afabf2abc0d46fdb4e68fa5ecf8e78f6ccc765fcd8c60cb5c13c79c99) and atom_operations.py (2a5532d89e6a5a8957b10a80814e07117ce6debf8bbc0af2ba8b2bd52b046519), preserving external dirt. Non-Active current carriers, D461/D466/D565 paths, exact no-op, model-currentness revocation, identified-to-Draft ID removal and immutable history are implemented. All14 current native golden tests pass. Replace still uses its old model interface and leaving Draft still needs admitted identity assignment; these remain separate unfinished coverage, not a universal-status or shared/MCP/image acceptance claim.
