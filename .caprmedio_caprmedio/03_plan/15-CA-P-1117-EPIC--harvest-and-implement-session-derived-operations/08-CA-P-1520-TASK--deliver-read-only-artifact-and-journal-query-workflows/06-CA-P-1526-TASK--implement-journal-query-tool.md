---
atom_id: CA-P-1526
content_role: Plan
type: Plan
label: Task
work_sequence_number: 6
current_scope_unit: caprmedio
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: "Events Journal query Tool implementation"
  depends_on: [Implementation, Workflow, Action, Tool, Evaluation, Journal]
version: 3
updated_at: "2026-10-05 01:30:00 +0400"
relations:
  is_decomposition_of: [CA-P-1520]
  blocks: [CA-P-1527]
---
# Summary

implement journal query tool

## Objective

Within <=15 minutes, test-first implement the independently accepted Events Journal query Tool only. No source O/RMED changes, competing Journal/log, second executor, MCP route registration, or other Workflow implementation.

### Exact inputs, output, ownership, and gate

Inputs: current accepted P1533 source/RMED exact IDs/Versions/paths after P1531 repairs, and P1523 target paths. Ownership: `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/FIND_AND_FETCH_JOURNAL_EVENTS/` and `tests/test_find_and_fetch_journal_events.py` only. Output: a read-only Tool querying the canonical Events Journal, returning Event IDs by default and selected fields/full Events only when requested.

P1533 rejected the absent-field conflict. P1534 repair and current P1535 acceptance are true dispatch blockers. Test-first golden verification must cover permitted filters, requested statuses/properties, pagination/coverage, selected/full fetch, malformed/missing/duplicate/incomplete diagnostics, rejected arbitrary evaluation, no secret return, no mutation authority, no fictitious Run, and stable snapshot. Save actual command/result; P1527 owns integration. Import the sole R1850 parser/evaluator from FIND_AND_FETCH_ARTIFACTS/query_filter.py; do not maintain another grammar. Root saves this Plan's Result.

### Definition of Done

The owned Tool and golden tests pass against accepted source pins with truthful remainder; host proof is not MCP or image proof.
