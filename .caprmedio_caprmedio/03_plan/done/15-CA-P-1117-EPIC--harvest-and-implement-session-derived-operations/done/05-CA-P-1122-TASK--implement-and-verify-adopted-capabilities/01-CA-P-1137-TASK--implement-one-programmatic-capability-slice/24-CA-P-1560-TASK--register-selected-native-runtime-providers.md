---
atom_id: CA-P-1560
content_role: Plan
type: Plan
label: Task
work_sequence_number: 24
current_scope_unit: caprmedio
claim_target_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: "Register selected native runtime providers"
  depends_on: [Workflow, Action, Implementation, Evaluation, Journal]
version: 2
updated_at: "2026-10-04 22:52:48 +0000"
relations:
  is_decomposition_of: [CA-P-1137]
  blocks: [CA-P-1519]
---
# Summary

Register selected native runtime providers

## Objective

Within <=15 minutes, wire the existing selected dispatcher to its explicit native providers.

## Details

Saved result: explicit worker startup now instantiates SelectedNativeProviders lazily. It supplies a distinct ImplementationAgent callback and per-frozen-request Revert factory through the existing Action session. Six registered-provider tests, twenty selected-execution tests and four Agent tests passed. Base Revise passed 29/30 under the inherited Docker namespace; the remaining hardcoded native-path idle-worker test passed separately under its expected native namespace. These are separate observations, not an unqualified clean full-suite result. Focused provider tests mock the shared session and do not establish canonical Journal, MCP or full image acceptance. No authenticated Agent call or real Project effect was performed.

Inputs: current accepted original-thirteen source/RMED, P1553 native Revert factory and P1554 ImplementationAgent callback. Own backend.py and a narrowly required startup-provider module plus test_selected_native_providers.py. Preserve Base Revise and explicit worker lifecycle; no selected_execution.py, Tools, source, manifest, MCP or fixture edits. Bind ImplementationAgent only as the independent Implementation callback, never reuse Base Revise outputs or grant ambient write permission. Bind Revert per exact frozen selected context through make_native_revert_service and make_revert_action_handler with the already provided session. No caller-added arbitrary effects, inferred inverses, duplicated Runs or broadened capability. Prove actual disposable lifecycle/structural effects and executable mock implementation effects through registered selected dispatch; denied or unsupported provider inputs remain truthful. Do not start authenticated CLI or real Project effects. If current source does not admit a transport or registration, return the exact source gap instead of widening it.

Inherit CA-P-1117's 90% threshold and mechanical Git exception. You are not alone; preserve others and use apply_patch. Root saves Plans/commits. No FPF, harvesting, credential/config edits or permission bypass.

## Definition of Done

Explicit selected startup exposes the native providers with functional disposable proof and preserves the old worker contract.
