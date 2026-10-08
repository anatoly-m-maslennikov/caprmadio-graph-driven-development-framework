---
atom_id: CA-P-1525
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: caprmedio
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: "Artifact query Tool implementation"
  depends_on: [Implementation, Workflow, Action, Tool, Evaluation, Journal]
version: 4
updated_at: "2026-10-04 22:46:18 +0000"
relations:
  is_decomposition_of: [CA-P-1520]
  blocks: [CA-P-1527]
---
# Summary

implement artifact query tool

## Objective

Within <=15 minutes, test-first implement the independently accepted Artifact query Tool only. No source O/RMED changes, second executor, MCP route registration, or implementation of other Workflows.

### Exact inputs, output, ownership, and gate

Inputs: current accepted P1532 source/RMED exact IDs/Versions/paths after P1530 repairs, and P1521 target paths. Ownership: `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/FIND_AND_FETCH_ARTIFACTS/` and `tests/test_find_and_fetch_artifacts.py` only. Output: a read-only Tool that meets the accepted source contract, returns Artifact IDs by default and selected properties/sections only when requested, and preserves canonical carrier identity without filename inference.

P1532 acceptance is a true dispatch blocker. Test-first golden verification must cover permitted filters, requested statuses/properties, pagination/coverage, selected fetch, malformed/missing/duplicate/incomplete diagnostics, rejected arbitrary evaluation, no secret return, no mutation authority, and stable snapshot. Save actual command/result; P1527 owns integration.

P1532 now accepts the current eight-carrier v2 packet with exact SHA-256 pins. Within the owned directory, deliver one reusable `query_filter.py` parser/evaluator implementing R1850, and publish its callable API before the Journal Tool depends on it. P1526 must import this same implementation rather than maintain a second grammar. Own the Tool, parser and golden tests only; root saves this Plan's Result from actual evidence. Reuse safe YAML support. The Docker development worker is a test environment, not immutable-image proof.

### Definition of Done

The owned Tool and golden tests pass against accepted source pins with truthful remainder; host proof is not MCP or image proof.

## Result

Final bounded Tool disposition: Done. P1537/P1538 implemented the admitted Tool and sole parser; P1546 completed the namespace collision golden case; P1548 added observed parser statistics. Independent P1547@3 accepts Artifact pure core and shared parser against current P1532 sources, with 11 Artifact and 7 parser tests. The initial result below is historical and superseded. MCP/queue/Run/image gates remain P1527/P1528.

Initial implementation is saved in FIND_AND_FETCH_ARTIFACTS: shared `query_filter.py`, `find_and_fetch_artifacts.py`, package entry and three golden tests. Development-worker tests passed 3/3; that narrow check does not satisfy the complete bound golden corpus. Root inspection found continuation re-enumeration instead of retained members, incorrect canonical section selector/boundaries, incomplete resource/secret diagnostics and YAML fallback, plus incomplete shared parser depth/token and number semantics. This Plan remains Active; separately bound P1537/P1538 must complete these obligations before P1525 is Done. No MCP, immutable-image, live Journal or actual selected Run proof exists yet.
