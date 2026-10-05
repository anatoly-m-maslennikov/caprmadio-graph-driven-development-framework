---
atom_id: CA-P-1640
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
subjects:
  governs: "Build Release Version contract golden tests"
  depends_on: [Workflow, Action, Tool, Manifest, Methodology, Implementation, Skill, Evaluation, Journal]
version: 1
updated_at: "2026-10-05 02:43:50 +0000"
relations:
  is_decomposition_of: [CA-P-1623]
  blocks: [CA-P-1643]
---
# Summary

Build Release Version contract golden tests

## Objective

Within <=15 minutes, build Release Version contract golden tests.

## Details

Own new RELEASE_VERSION/tests/test_release_contract.py and explicit mocks only: e2e-style request-to-result pure preparation checks, missing/forged/unsealed/currentness/digest/path errors and good complete Framework manifest. Follow R1876–1880/M331–333/E571–574/D560–564 exactly; coordinate API with P1639. No effects or mocked promotion presented as actual proof.

Inputs are P1622 accepted source/RMED pins: O164–179@1, R1876–1880@1, M331–333@1, E571–574@1, D560–564@1. D561/E572 are the repaired accepted pins, not their rejected predecessors. Preserve external dirt and designated C447/C449 boundaries; existing development worker tests are not fresh-image proof.

## Definition of Done

Save exact bounded output and test/remaining-coverage evidence. Pure preparation, staging or source review never establishes release promotion, complete P1623, P1624 or Epic closure.

