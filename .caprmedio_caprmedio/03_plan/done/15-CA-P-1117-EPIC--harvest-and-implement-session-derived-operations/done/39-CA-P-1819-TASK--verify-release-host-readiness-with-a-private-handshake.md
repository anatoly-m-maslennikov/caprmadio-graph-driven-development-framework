---
atom_id: CA-P-1819
content_role: Plan
type: Plan
label: Task
work_sequence_number: 39
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
version: 3
updated_at: "2026-10-07 12:27:46 +0000"
subjects:
  governs: "verify Release host readiness with a private handshake"
  depends_on: [Workflow Run, Implementation, Evaluation, Operator]
relations:
  is_decomposition_of: [CA-P-1117]
  relates_to: [CA-R-1891, CA-M-347, CA-E-590, CA-D-583]
---
# Summary

verify Release host readiness with a private handshake

## Objective

implement and verify the accepted private nonce handshake so ordinary Release host readiness can be established without a process-signal permission.

## Details

- preserve the closed N15 unknown disposition and installed runtime.
- implement the bounded handshake, worker lifecycle integration and ordinary bridge admission against accepted M347/E590/D583.
- test exact identity and freshness, bounded carrier handling, refusal cases and lifecycle ordering.
- reopen final source pins before starting the replacement host.
- the Operator stopped the old idle host; its readiness carrier is absent. a fresh Release remains subject to all mandatory gates.

## Progress

- accepted implementation: `70de481d0`; private source admission now reopens 21 implementation Carriers through D572@20.
- 21 focused health/bridge/lifecycle tests and 18 source-admission tests pass. independent review accepted the final nonblocking read and shutdown ordering.
- MCP hot reload succeeded; the current Release Version context is complete and the public binding manifest remains unchanged.
- installed runtime selector SHA remains `23c17beeab33e1a281c68bfbd492d6ea27b6e5e36c275744c7cb56bdc98c9fdc`.
- the Operator launched the replacement host from Terminal. actual availability passed with PID 37158 and current runtime fingerprint `8628650133b8ea344c914f241e03e6f903f197c4d92122f2b50ffe013a53a213`, after a fresh nonce response and metadata revalidation. no process-signal readiness bypass was used.
- seven broader legacy host-test errors came from denied temporary-directory cleanup. retain those fixtures as directed; do not report those tests as passed or alter production cleanup.

## Definition of Done

focused tests and independent code review pass; source admission validates final bytes; the explicitly started replacement host answers a fresh exact-identity challenge. no readiness bypass, uncertain replay or passing Release result is invented.
