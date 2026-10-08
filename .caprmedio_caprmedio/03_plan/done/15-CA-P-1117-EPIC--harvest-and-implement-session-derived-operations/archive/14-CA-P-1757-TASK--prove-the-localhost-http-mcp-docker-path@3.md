---
atom_id: CA-P-1757
content_role: Plan
type: Plan
label: Task
work_sequence_number: 14
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Archived
version: 3
updated_at: "2026-10-08 14:57:41 +0000"
subjects:
  governs: "Prove the localhost HTTP MCP Docker path"
  depends_on: [Implementation, Workflow, Action, Evaluation, Journal]
relations:
  is_decomposition_of: [CA-P-1117]
  blocks: [CA-P-1655, CA-P-1124]
---
# Summary

Prove the localhost HTTP MCP Docker path

## Objective

Verify the opt-in HTTP MCP service in an actual isolated candidate container with an explicit loopback port and ephemeral test token. This is required FIRST CUT evidence alongside the six scoped Workflows, existing stdio MCP/orchestrator compatibility, and shared journaling.

## Details

Root owns actual Docker effects; current accepted HTTP packet and P1756 gate execution. Use a disposable project and explicit runtime environment only; no Codex Agent start, host socket mount, baked secret, or undeclared host implementation mount. Preserve permissions, secret isolation, currentness, identity, status-model and Journal-evidence checks.

Estimated bounded slice: <=15 minutes. Workers share the checkout, preserve other edits and do not stage or commit. Root owns integration and Git. Preparation does not prove runtime execution.

## Definition of Done

Actual authenticated initialize/list/call, health and lifecycle tests pass on localhost; invalid credentials, Host and Origin fail before tools; stdio stays usable; and startup/shutdown lifecycle evidence is retained. This must prove HTTP in Docker, not only host or build behavior. It does not claim all-sixteen/full-release coverage, N+1 promotion, automatic Release Version/prior-image retirement, or completion of deferred Scope Unit mutations, Revert, graph builders, or standalone advanced Artifact/Journal queries.

## Accepted actual proof

the Operator's retained report `.caprmedio_tmp/epic-first-cut-20261008/http-5fab36806-terminal-omm68ywL/full.log` passed 14 tests in 118.565 seconds, with no skips; SHA-256 `4f157a1e8985d837aa91d10f759735d8600e29753ecdc1d95bdc2b9141da2e1b`. The exact immutable candidate image was `sha256:75759a40209b4f2ab9adae212d1f3d8f771bb252a986bcdd5d24dead90bb9cb9`, runtime source commit `5fab36806`; the separately corrected host harness was commit `9dea0a672`, SHA-256 `0c17f2bb27c9692b5bcde6302799de25d3790bfed9bccd1bacafddcaa0d23a15`.

all six retained Workflows completed over authenticated HTTP with native-effect and canonical Journal checks. The proof also passed non-mutating previews; health; loopback startup and shutdown; invalid credential, Host, Origin, denied reload-call and prior-session continuation refusal with unchanged recording state; W01 token rotation and replacement-session access; and same-candidate W01 stdio context compatibility. Separate accepted receipts cover the broader six-route stdio and all-role Status boundaries.

the deterministic `.caprmedio_tmp/epic-first-cut-20261008/http-workflow-receipts.json`, SHA-256 `adb7d7f0b08be0f58ec97afaebb1a4ae8c0d6d9f4350c8d4c49e282df71b7818`, verifies six actual completed Workflow terminals and 18 completed Action terminals, their frozen definitions, event digests, parent lineage and retained result/effect references. W09 uses the explicit golden mock Agent, not a live LLM. The independent read-only acceptance confirms the required first-cut HTTP boundary, not formal Release or installed-runtime promotion. The original failed reports are retained.

functional work is accepted. Active metadata remains until the separate authorized administrative or governed closure occurs; no production closure Run or Journal receipt is invented.

## Pre-execution review

Root accepts this bounded repair/restoration against Operator authority, DRY, preservation of valuable information and the latest continuation. Keep installed N intact and distinguish local tests from required actual runtime gates.
