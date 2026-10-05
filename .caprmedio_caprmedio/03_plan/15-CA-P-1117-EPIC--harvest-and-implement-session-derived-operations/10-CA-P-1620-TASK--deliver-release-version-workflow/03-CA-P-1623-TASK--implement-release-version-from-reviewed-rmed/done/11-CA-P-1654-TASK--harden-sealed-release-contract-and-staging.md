---
atom_id: CA-P-1654
content_role: Plan
type: Plan
label: Task
work_sequence_number: 11
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
subjects:
  governs: "Harden sealed release contract and staging"
  depends_on: [Atom, Status, Carrier, Tool, Methodology, Evaluation]
version: 1
updated_at: "2026-10-05 04:08:40 +0000"
relations:
  is_decomposition_of: [CA-P-1623]
  blocks: [CA-P-1650, CA-P-1643]
---
# Summary

Harden sealed release contract and staging

## Objective

Complete this composite through its bounded child Tasks; it is not a fifteen-minute executable leaf.

## Details

CA-P-1656 implements the typed contract, CA-P-1657 verifies it independently, and CA-P-1658 repairs package staging. P1651 rejected the raw-mapping prototype; accepted D566/D567/E572@2 govern these children.

Adapt the prototype pure Release contract and staging helper to accepted D566/D567 only after P1649 accepts the source. Separate locally constructed trusted authority and post-compiler typed handoff from caller mappings. Canonical v2 checksum, complete source inventory, source-observed modes, safe non-symlink staging root and unchanged N are required. Coordinate independently owned golden tests; no selector, public Skill, image or Journal effects.

Read accepted source and the current worktree. Preserve unrelated edits and existing history. No denied-operation retry, new host environment or immutable-image acceptance claim.

## Definition of Done

Save the bounded output, exact current evidence and any unresolved coverage. Partial source, mock or helper acceptance does not complete the parent or Epic.

## Result

All three bounded children are Done: P1656 locally sealed typed D566/D567 handoffs; P1657 independently verified 27 focused golden cases; P1658 staged the complete framework from typed SealedCandidateCompilation with five focused package tests and thirteen handoff tests. The source/currentness and packaging boundary is repaired; actual compilation, full-suite, Skill/runtime installation, immutable-image verification, promotion, retirement and Journal gates remain assigned to subsequent Tasks. This composite does not claim those later gates.
