---
atom_id: CA-P-1700
content_role: Plan
type: Plan
label: Task
work_sequence_number: 12
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
subjects:
  governs: "Bind native Release Tool boundary"
  depends_on: [Tool, Manifest, Action, Evaluation]
version: 1
updated_at: "2026-10-05 06:58:29 +0000"
relations:
  is_decomposition_of: [CA-P-1643]
  blocks: [CA-P-1644]
---
# Summary

Bind native Release Tool boundary

## Objective

Within <=15 minutes, implement the strict D560 native request/result boundary and locally observed effect-free preparation.

## Details

Own only RELEASE_VERSION/release_version.py and tests/test_release_version.py. Read accepted D560, D566/D567, R1876 and the existing contract/handoff helpers. Parse the exact closed request fields and conditional recording-recovery reference; refuse unknown overrides, malformed manifests and stale local N/source/structure/settings/frontier bindings. Prepare constructs the locally observed validated candidate and complete D560 result without effects. Reserve a private typed selected-Action execution interface for the separate provider phase integration; no caller-controlled phase or unguarded all-phase apply. Apply/recovery without admitted provider context must return truthful blocked/incomplete outcomes rather than claim execution. Golden-first actual disposable prepare/refusal cases must preserve whole-Project bytes and cover the result shape. No source/manifest/registry changes, real Project release, actual image operations, permission workaround or Journal fabrication. Preserve other Agents' changes.

## Definition of Done

The exact request/result and effect-free prepare/refusal cases pass with source/code/test hashes. The selected-Action provider and recording recovery remain explicit required integration, not a completed Release claim.
