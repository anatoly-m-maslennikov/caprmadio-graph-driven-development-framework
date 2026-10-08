---
atom_id: CA-P-1815
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
version: 1
updated_at: "2026-10-06 21:37:39 +0000"
subjects:
  governs: "Seal the selected refresh reference frontier"
  depends_on: [Implementation, Evaluation, Source Carrier, Workflow, Action, Journal]
relations:
  is_decomposition_of: [CA-P-1809]
  relates_to: [CA-C-514]
---
# Summary

Seal the selected refresh reference frontier

## Objective

include and validate the exact registered selected-source refresh authority in the private Unit reference closure.

## Details

source-first CA-D-580 v7 declares five exact Active authority/dependency pins; implement its closed parser and materialization, preserve the context member set and reject arbitrary discovery. root owns CA-D-572 and current binding publication.

## Definition of Done

the confirmed defect is explained and repaired against current authority; source-equivalent focused regressions have a captured terminal result and independent review accepts the bounded change. actual full Release acceptance remains with the parent Plan.

## Acceptance evidence

independent review accepts the strict five-source closed parser, captured bytes/modes and unchanged context schema. the full reference-context module passed 18 tests in 14.818 seconds. a fresh sealed/gitless reconstruction with 256 captured reference rows, R1041 and D588 passed all six selected-refresh cases in 8.926 seconds, exit 0. the historical fixture carries the exact reader bytes from Git 92fe70738, SHA-256 554c2fd2a0fd3578433861c4f25089be1d0b743de986cca2993da5bdc11feafc, without replacing historical control pins or bypassing D572 checks. the final D572 v16 source-admission module also passed all 14 tests in 6.085 seconds.

this is bounded source/fixture acceptance only; actual complete Release acceptance remains with CA-P-1809 and CA-P-1117.

## Reopened fixture integration

parallel final review found that full_suite_golden/control_fixture.py copies Prompt bindings but omits the D580 v7 selected-refresh authority leaves. retained E2E fixture materialization therefore fails before execution. the production context and its focused tests remain accepted; this Task is reopened until the shared retained-fixture closure preserves the same exact five declared sources and its dependent setup regressions pass. N14 was deliberately interrupted early rather than treating this known incompatible setup as a new complete test gate.

the shared fixture repair is accepted and saved at dfc76e4f0. it derives only D580's five fixed paths, copies their exact bytes and modes, and revalidates their identities, Active status and digests through the production parser. independent review accepts it without weakening authority or expanding discovery. reference-context tests passed 19/19, selected-refresh tests passed 6/6, and image/suite/promotion setup checks passed. independent retained E2E fixture tests passed 2/2 in 19.050 seconds; E2E-context tests passed 13/13 in 0.100 seconds; full-gate fixture tests passed 7/7 in 240.244 seconds. root retained the actual terminal result for the complete E2E-gate fixture module: 11/11 in 101.806 seconds, exit 0. these are bounded fixture regressions, not fresh Candidate Docker/MCP acceptance; CA-P-1809 still requires the unchanged full Release gate.
