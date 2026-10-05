---
atom_id: CA-C-476
content_role: Concern
type: Question
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 19:49:20 +0000"
subjects:
  governs: "Release suite/E2E execution environment"
  depends_on: [Evaluation, Test Suite, Implementation, Docker Image, Workflow, Action]
relations:
  concern_about: [CA-P-1717, CA-P-1721]
---
# Summary

Provide the required E2E Release test environment

## Concern

How should the required Docker/MCP E2E tests execute under the complete Release gate while preserving the immutable suite's closed, read-only, network-disabled execution boundary?

## Evidences

The complete driver discovers all real sealed Framework test modules and treats skipped tests as non-passing. Three packaged modules require Docker opt-in variables: test_docker_e2e.py, test_selected_workflows_docker_e2e.py and test_selected_query_mcp_e2e.py. The selected-query module also requires an exact image input. The current suite executor admits neither opt-in variable; its child runner further closes the environment. The E2E fixtures need Docker execution and writable fixture trees, but the isolated suite has no Docker socket, no network, and a read-only workspace. This incompatibility is source-confirmed; no actual complete suite was run.

## Blast radius

Actual full-suite acceptance and Release promotion. Focused golden tests and truthful driver behavior do not establish the missing E2E environment. The sixteen-route manifest and deferred final all-sixteen audit are unchanged.

## Disposition

Preserve the isolated executor and truthful non-pass state. Do not hide the E2E modules, accept their skips, mount the host Docker socket into the test container, or relax permissions by implementation alone. The preferred next design is a separately governed E2E-capable gate whose observed case evidence is bound to the same candidate and included in complete coverage. Its exact executor, fixture boundary and image lifecycle require RMED first and independent review before implementation. This records the chosen direction under the Epic's autonomous policy; it is not a new execution permission or passing gate.
