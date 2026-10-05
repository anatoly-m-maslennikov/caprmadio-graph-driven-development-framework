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
status: Done
subjects:
  governs: "Events Journal query Tool implementation"
  depends_on: [Implementation, Workflow, Action, Tool, Evaluation, Journal]
version: 5
updated_at: "2026-10-04 22:46:18 +0000"
relations:
  is_decomposition_of: [CA-P-1520]
  blocks: [CA-P-1527]
---
# Summary

implement journal query tool

## Objective

Within <=15 minutes, test-first implement the independently accepted Events Journal query Tool only. No source O/RMED changes, competing Journal/log, second executor, MCP route registration, or other Workflow implementation.

### Exact inputs, output, ownership, and gate

Inputs: current accepted P1535 source/RMED exact ID/Version/path/SHA-256 pins after P1534 repair, and P1523 target paths. Ownership: `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/FIND_AND_FETCH_JOURNAL_EVENTS/` and `tests/test_find_and_fetch_journal_events.py` only. Output: a read-only Tool querying the canonical Events Journal, returning Event IDs by default and selected fields/full Events only when requested. Source gate is now accepted. P1538 owns completing the single shared parser; import that same API rather than duplicating it.

P1533 rejected the absent-field conflict. P1534 repair and current P1535 acceptance are true dispatch blockers. Test-first golden verification must cover permitted filters, requested statuses/properties, pagination/coverage, selected/full fetch, malformed/missing/duplicate/incomplete diagnostics, rejected arbitrary evaluation, no secret return, no mutation authority, no fictitious Run, and stable snapshot. Save actual command/result; P1527 owns integration. Import the sole R1850 parser/evaluator from FIND_AND_FETCH_ARTIFACTS/query_filter.py; do not maintain another grammar. Root saves this Plan's Result.

### Definition of Done

The owned Tool and golden tests pass against accepted source pins with truthful remainder; host proof is not MCP or image proof.

## Result

Done for the bounded native Tool contract. P1545@3 repairs opaque server-retained snapshot trust and selector diagnostics; P1548 supplies actual sole-parser consumption. Independent P1547@3 accepts Journal pure core against P1535, including all 14 passing Docker tests. Configured canonical root and retained member prefixes are revalidated; later appends and own execution events cannot enlarge a captured result. Handles are process-local and unknown after restart, not silently recaptured. Actual shared Run, standalone Action, queue/MCP and fresh-image gates remain P1527/P1528.
