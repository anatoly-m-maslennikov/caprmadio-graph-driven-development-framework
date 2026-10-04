---
atom_id: CA-P-1538
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: "Complete shared filter semantics and bounds"
  depends_on: [Implementation, Tool, Evaluation]
version: 1
updated_at: "2026-10-04 21:37:54 +0000"
relations:
  is_decomposition_of: [CA-P-1525]
  blocks: [CA-P-1525]
---
# Summary

Complete shared filter semantics and bounds

## Objective

Within <=15 minutes, test-first finish this bounded P1525 implementation remainder. The original source acceptance is still current; do not narrow its required behavior to existing passing tests.

## Details

Own only FIND_AND_FETCH_ARTIFACTS/query_filter.py and new tests/test_query_filter.py. Shared R1850@2 and P1532 accepted pins govern. Preserve exported parse_filter/evaluate_filter/typed_equal/QueryFilterError/MISSING API or coordinate an additive API early. Enforce recursion depth for NOT, parentheses and typed JSON literals, tokens including literals, bounded IN; validate bad JSON/duplicate object members/nonfinite numbers, malformed separators/operators and trailing syntax without eval. JSON number has one semantic type (integer/float compare numerically; booleans never numbers). Validate all selectors before short-circuit evaluation, via additive helper, so malformed unvisited branches cannot pass. Test missing/null, deep lists/maps, precedence, escaped quotes and all resource rejection cases with bounded diagnostics. No Artifact filesystem implementation, source/RMED/Plan, Journal/MCP or settings-file changes. Publish API to Artifact and Journal workers. Run focused golden test file; root persists result.

You are not alone; preserve concurrent edits and use apply_patch. Inherit 90% confidence and mechanical Git exception; root owns Plan writes/commits. No harvesting, FPF, external deployment, actual Project authority mutation or permission bypass. If unfinished, save the exact frontier instead of claiming Done.

### Definition of Done

Every owned requirement has passing golden evidence against current accepted source pins, exact commands/results and truthful integration/image remainder.
