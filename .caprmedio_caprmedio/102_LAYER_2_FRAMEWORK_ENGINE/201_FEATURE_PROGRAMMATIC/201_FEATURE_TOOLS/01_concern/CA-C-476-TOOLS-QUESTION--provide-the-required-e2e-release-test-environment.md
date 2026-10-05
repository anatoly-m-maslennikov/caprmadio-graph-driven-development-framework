---
atom_id: CA-C-476
content_role: Concern
type: Question
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-05 20:40:22 +0000"
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

The Operator explicitly approved a separate bounded host-side executor for the three source-pinned Docker E2E harnesses. Keep the isolated Unit executor unchanged and block Release promotion until both phases pass with complete candidate-bound coverage. This approval covers the bounded host executor; it does not authorize Docker socket mounts, a privileged daemon, a generic remote Docker interface, permission bypass, arbitrary candidate commands, or hidden test exclusions.

The selected sequence is compilation, closed Unit Gate, candidate-image build and canary, Candidate E2E Gate, Full Gate aggregation, then promotion. The frozen Docker worker is not the host E2E controller and gains no socket access. Missing host Python or Docker capability yields a non-passing unavailable result.

Source review accepted the candidate/image/phase bindings and byte-backed receipt/aggregation direction, but found absent literal command/environment carriers and absent configured limit keys. Repair CA-R-1890, CA-M-346, CA-E-589 and CA-D-582 before dependent implementation. Resolve `release_e2e` limits from explicit Framework Instance settings, otherwise the canonical defaults: inspect timeout 60 seconds, per-harness timeout 900 seconds, cleanup timeout 60 seconds, and 8 MiB each for retained stdout, stderr and JUnit. These are configurable safety defaults selected under the Epic's autonomous policy, not measured performance claims.

Actual Docker E2E execution, full-suite aggregation, source-frontier admission, Release installation and promotion remain unfinished. Retaining disposable fixture directories is not a gate failure by itself; uncertain Docker cleanup or a failed required command remains non-passing.
