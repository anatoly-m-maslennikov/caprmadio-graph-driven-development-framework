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
status: Active
version: 1
updated_at: "2026-10-07 10:54:16 +0000"
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

## Definition of Done

focused tests and independent code review pass; source admission validates final bytes; the explicitly started replacement host answers a fresh exact-identity challenge. no readiness bypass, uncertain replay or passing Release result is invented.
