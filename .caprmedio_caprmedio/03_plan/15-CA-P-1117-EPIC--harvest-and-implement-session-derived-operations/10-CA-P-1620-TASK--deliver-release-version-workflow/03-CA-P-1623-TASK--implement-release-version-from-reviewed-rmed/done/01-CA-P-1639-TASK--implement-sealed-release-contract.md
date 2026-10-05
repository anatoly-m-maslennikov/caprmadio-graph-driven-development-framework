---
atom_id: CA-P-1639
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
  governs: "Implement sealed Release Version contract"
  depends_on: [Workflow, Action, Tool, Manifest, Methodology, Implementation, Skill, Evaluation, Journal]
version: 1
updated_at: "2026-10-05 04:15:01 +0000"
relations:
  is_decomposition_of: [CA-P-1623]
  blocks: [CA-P-1643]
---
# Summary

Implement sealed Release Version contract

## Objective

Within <=15 minutes, implement sealed Release Version contract.

## Details

Own new RELEASE_VERSION/release_contract.py only: strict request/result boundary per D560; pure canonical candidate construction, validated required complete package/source/currentness bindings, digest and traversal/destination collisions. No effects, source edits or callable apply placeholder that reports success. Coordinate API with P1640 test author.

Inputs are P1622 accepted source/RMED pins: O164–179@1, R1876–1880@1, M331–333@1, E571–574@1, D560–564@1. D561/E572 are the repaired accepted pins, not their rejected predecessors. Preserve external dirt and designated C447/C449 boundaries; existing development worker tests are not fresh-image proof.

## Definition of Done

Save exact bounded output and test/remaining-coverage evidence. Pure preparation, staging or source review never establishes release promotion, complete P1623, P1624 or Epic closure.

## Result

The initial raw-mapping prototype was rejected and repaired through P1648/P1649/P1656/P1657. Current committed release_contract.py SHA-256 6dc7f9502f264368fd8e83c167bceaf4a59ec36fe69b101b6d08e4e19f2cc423 and release_handoff.py 17c66c4ead4989d5908cd6642cf667b0e3347c39572b8d3716b03447f57f4647 implement canonical D566 candidate.v2 plus locally observed typed D567 authority/copy/compiler/package boundaries. P1657 independently verified the repaired boundary in 27 focused cases. This closes the pure contract output, not actual compilation, Release execution or runtime promotion.
