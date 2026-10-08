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
version: 2
updated_at: "2026-10-05 06:07:49 +0000"
relations:
  is_decomposition_of: [CA-P-1643]
  blocks: [CA-P-1644]
---
# Summary

Implement bound Release image phases

## Objective

Complete bound candidate-image phases through bounded child Tasks. P1696 retains the completed build/verification frontier; P1697 completes retirement after P1693 supplies observed promotion evidence. This composite is not an executable fifteen-minute leaf.

## Details

Own only RELEASE_VERSION/release_image.py and focused tests/test_release_image.py. Consume current locally sealed candidate, compilation, complete package and passing suite evidence; build from the pinned Dockerfile and a private exact candidate context, not mutable candidate tags or caller success flags. Produce immutable image identity and actual complete package/executable canary evidence. Keep executing N unchanged; promotion is separate. Exact prior-image retirement requires actual verified promotion and no retaining container or required rollback reference; no broad prune or forced removal. Use the existing Docker surface, closed arguments and truthful failed/incomplete effects with repairable context.

Golden first with explicit fake command execution and actual output fixtures. This leaf must not run a real build, provision a runner, create/remove containers or images, or work around C449. Only the already permitted development worker may run the disposable focused tests. No actual repository release/runtime, source/Plan/Git writes or credential reads. Coordinate suite/package APIs and preserve other edits. Choose the best authorized option, record uncertainty and continue. If the whole helper does not fit fifteen minutes, retain the exact implemented frontier and bounded required remainder.

## Definition of Done

Actual code and focused failure/identity/currentness/retaining-reference cases have exact hashes and truthful mock-versus-live evidence. No mock receipt proves an actual image, installation, MCP or Release gate.

## Result

Build/verification implementation is complete: release_image.py `6ae95bd3055e759221f4ca0611fda4a444811e8a8f522c9750a8b94c66494024`, tests `f15a7092dcf3c6d78888d25a74846ed905f299587a69b9812614110585be21a1`, fifteen fake-Docker golden tests passed. The actual production-evidence reader refuses test-double receipts. Retirement deliberately fails closed until the separate promotion/prior-image/rollback authority producer exists. No actual Docker image/container, Release or promotion occurred. P1697 is required before this composite can close.
