---
atom_id: CA-P-1717
content_role: Plan
type: Plan
label: Task
work_sequence_number: 27
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
version: 1
updated_at: "2026-10-05 16:49:29 +0000"
subjects:
  governs: "Release suite preservation"
  depends_on: [Implementation, Evaluation, Skill, Methodology, Image, Manifest]
relations:
  is_decomposition_of: [CA-P-1643]
  blocks: [CA-P-1624]
---
# Summary

Isolate the Release suite from the executing runtime

## Objective

Preserve the executing runtime N, active ca Skill and canonical authority while running the complete declared candidate Release suite.

## Details

1. apply CA-R-1879 and CA-E-574 to the concrete CA-C-472 finding; the independent review already rejects real-root execution with only a post-run stale check.
2. bind a genuine isolated execution boundary with protected canonical inputs and a separate writable fixture/output area. Preserve the complete selected suite, sealed candidate inputs, exact executing N and evidence format.
3. implement adversarial attempted-write tests before the repair. Check truthful failed, unavailable and incomplete outcomes; no unavailable Docker or directory-publication result is reported passing.
4. independently review the repaired local boundary. This necessary Release gate is not the deferred all-Workflow final audit.
5. estimate the bounded next implementation/review leaf at <=15 minutes; decompose before expanding beyond that limit.

## Current frontier

The local adapter passed **9** focused command, mount, path and timeout boundary tests. Immutable-image bootstrap checks passed **2** cases, and generic suite-boundary checks passed **2** cases. This is focused local evidence, not actual Release-gate evidence.

The complete declared suite has not reached its executor. The retained-suite run stops in `release_compilation.py:313` when `os.replace` receives `EPERM`; an earlier Action O174 `deliver_sources` attempt also stopped at a rename `EPERM`. The installed-N Docker execution, complete-suite evidence and required delivery/compilation publication gates therefore remain open.

## Definition of Done

The repaired boundary is independently accepted against current CA-R-1879 and CA-E-574, protected-carrier tests pass, and the complete declared suite executes with retained actual evidence without changing N, public ca or authority. Source/mock tests alone do not close the actual Release gate.

## Pre-execution review

Root accepts this bounded repair Plan from /root/checkpoint_integration_review's source/code rejection. It retains the existing preservation requirement and full-suite scope, changes no runtime permission, and permits no alternate endpoint or denied-operation bypass. Actual runtime evidence remains mandatory.
