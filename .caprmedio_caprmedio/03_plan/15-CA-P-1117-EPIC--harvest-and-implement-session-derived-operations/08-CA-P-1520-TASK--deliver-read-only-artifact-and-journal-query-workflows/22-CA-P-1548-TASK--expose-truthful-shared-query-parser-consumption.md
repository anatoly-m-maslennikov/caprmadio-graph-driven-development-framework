---
atom_id: CA-P-1548
content_role: Plan
type: Plan
label: Task
work_sequence_number: 22
current_scope_unit: caprmedio
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: "Expose truthful shared query parser consumption"
  depends_on: [Implementation, Workflow, Action, Evaluation, Journal]
version: 2
updated_at: "2026-10-04 22:18:37 +0000"
relations:
  is_decomposition_of: [CA-P-1520]
  blocks: [CA-P-1545, CA-P-1547]
---
# Summary

Expose truthful shared query parser consumption

## Objective

Within <=15 minutes, complete this bounded repair or acceptance packet with saved source-bound evidence.

## Details

Inputs: accepted CA-R-1850 shared closed filter grammar, CA-R-1865/CA-D-556 consumption evidence and CA-P-1544's token diagnostic defect. Ownership: only FIND_AND_FETCH_ARTIFACTS/query_filter.py and tests/test_query_filter.py. Add a compatible public parse_filter_with_stats API returning (tree, statistics), without changing existing parse_filter tree behavior, duplicating the grammar/parser, or weakening limits. Statistics must use actual parser counters, not expression byte length or AST depth standing in for syntactic depth; preserve actual maximum IN members and relevant depth consumption if exported. Count valid expression tokens exactly; failures must preserve observed exhaustion rather than reporting guessed success. Coordinate final API details immediately with CA-P-1545 owner. Test a 3-token expression, NOT/parentheses, IN literal and separator counts, long strings/objects, exact maxima and maximum-plus-one bounds. Run the parser and full existing Artifact suite; no Journal Tool/source/Plan/MCP edits.

Inherit CA-P-1117's 90% confidence threshold and explicit mechanical Git save exception. You are not alone; preserve other workers' edits and use apply_patch. No harvesting, FPF, broad audit, permission bypass, deployment or unrelated changes. Root owns Plan updates and commits. If unfinished, return exact remainder; do not mark the aggregate Epic Done.

### Definition of Done

The owned packet has actual scoped evidence and a truthful saved result. The final fifteen-Workflow Docker/MCP proof remains separate.

### Actual result

query_filter.py exports compatible parse_filter_with_stats returning the unchanged tree plus actual parser statistics: tokens, grammar_depth, syntactic_depth, literal_depth and in_members. parse_filter preserves its tree-only API. QueryFilterError.statistics retains actual counters for failures and maximum-plus-one exhaustion; no duplicate parser or byte-count estimate is introduced.

The worker changed only query_filter.py and tests/test_query_filter.py. Actual Docker runtime:local results were seven parser and eleven Artifact tests passing, including three-token comparison, seven-token IN separators, syntactic/literal nesting, long literals and exact maximum-plus-one counts. This is scoped source-code test evidence, not fresh immutable-image proof. CA-P-1545 consumes the API and CA-P-1547 independently reviews the final combined packet.
