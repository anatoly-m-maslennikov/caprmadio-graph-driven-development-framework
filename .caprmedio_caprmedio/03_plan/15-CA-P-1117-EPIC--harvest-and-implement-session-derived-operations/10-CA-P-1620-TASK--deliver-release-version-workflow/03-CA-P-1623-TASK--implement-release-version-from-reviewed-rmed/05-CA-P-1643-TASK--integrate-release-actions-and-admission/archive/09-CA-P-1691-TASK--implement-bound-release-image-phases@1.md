---
atom_id: CA-P-1691
content_role: Plan
type: Plan
label: Task
work_sequence_number: 9
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
subjects:
  governs: "Implement bound Release image phases"
  depends_on: [Tool, Manifest, Evaluation, Image, Runtime]
version: 1
updated_at: "2026-10-05 05:54:08 +0000"
relations:
  is_decomposition_of: [CA-P-1643]
  blocks: [CA-P-1693, CA-P-1644]
---
# Summary

Implement bound Release image phases

## Objective

Within <=15 minutes, implement bound candidate-image build, verification and exact retirement phase helpers.

## Details

Own only RELEASE_VERSION/release_image.py and focused tests/test_release_image.py. Consume current locally sealed candidate, compilation, complete package and passing suite evidence; build from the pinned Dockerfile and a private exact candidate context, not mutable candidate tags or caller success flags. Produce immutable image identity and actual complete package/executable canary evidence. Keep executing N unchanged; promotion is separate. Exact prior-image retirement requires actual verified promotion and no retaining container or required rollback reference; no broad prune or forced removal. Use the existing Docker surface, closed arguments and truthful failed/incomplete effects with repairable context.

Golden first with explicit fake command execution and actual output fixtures. This leaf must not run a real build, provision a runner, create/remove containers or images, or work around C449. Only the already permitted development worker may run the disposable focused tests. No actual repository release/runtime, source/Plan/Git writes or credential reads. Coordinate suite/package APIs and preserve other edits. Choose the best authorized option, record uncertainty and continue. If the whole helper does not fit fifteen minutes, retain the exact implemented frontier and bounded required remainder.

## Definition of Done

Actual code and focused failure/identity/currentness/retaining-reference cases have exact hashes and truthful mock-versus-live evidence. No mock receipt proves an actual image, installation, MCP or Release gate.
