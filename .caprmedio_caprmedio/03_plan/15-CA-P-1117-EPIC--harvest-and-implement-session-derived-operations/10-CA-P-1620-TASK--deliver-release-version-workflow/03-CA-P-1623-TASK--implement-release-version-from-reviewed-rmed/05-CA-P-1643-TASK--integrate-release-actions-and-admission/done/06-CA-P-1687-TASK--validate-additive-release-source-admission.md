---
atom_id: CA-P-1687
content_role: Plan
type: Plan
label: Task
work_sequence_number: 6
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
subjects:
  governs: "Validate additive Release source admission"
  depends_on: [Workflow, Action, Tool, Manifest, Evaluation]
version: 1
updated_at: "2026-10-05 05:56:13 +0000"
relations:
  is_decomposition_of: [CA-P-1643]
  blocks: [CA-P-1644]
---
# Summary

Validate additive Release source admission

## Objective

Within <=15 minutes, implement the strict Release source-admission validator.

## Details

Own only new MCP/release_source_admission.py and its focused tests. Read accepted CA-D-572@3 and derive its exact closed pin record without creating a second authority. Validate current source bytes and identity, the accepted frontier, ten ordered Step/Action occurrences and complete RMED frontier. Preserve the current fifteen-route manifest when Release is absent. Reject absent, duplicate, stale, incomplete, malformed, reordered or caller-forged Release admission before shared support; D527 request definition_manifest remains its existing two fields.

Golden tests first. No actual manifest changes, route registration, native release dispatch, runtime installation, image work, source/Plan/Git edits or denied-operation workaround. Use disposable fixtures in the existing development worker only. Preserve every other Agent's work. Choose the best authorized option and record uncertainty rather than wait for Operator input.

## Definition of Done

The focused compatibility and refusal cases pass, and exact code/test hashes are retained. This is parser/validator proof only, not registration or release execution.

## Result

release_source_admission.py `e2bc6ba7c63c139d8d7b3b8c9eca85e8d3120cce3d93ea20c8ea55637e4946a8` and tests `05106a2c9a6e8029d1aa4c8e91634694d5eaeadde54fb9ebe079d35383444ffa`: eight focused tests pass, including thirty-seven separate live-pin revocations. The read-only helper derives the exact six-field record from D572@3, preserving ordered occurrences and current fifteen-route compatibility without reading Release authority when absent. Raw duplicate-key rejection and whole-manifest integration remain P1692; no actual manifest registration, dispatch or image completion occurred.
