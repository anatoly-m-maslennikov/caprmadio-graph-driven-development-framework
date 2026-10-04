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
status: Active
subjects:
  governs: "Artifact query Tool implementation"
  depends_on: [Implementation, Workflow, Action, Tool, Evaluation, Journal]
version: 1
updated_at: "2026-10-05 00:02:29 +0400"
relations:
  is_decomposition_of: [CA-P-1520]
  blocks: [CA-P-1527]
---
# Summary

implement artifact query tool

## Objective

Within <=15 minutes, test-first implement the independently accepted Artifact query Tool only. No source O/RMED changes, second executor, MCP route registration, or implementation of other Workflows.

### Exact inputs, output, ownership, and gate

Inputs: accepted P1522 source/RMED exact IDs/Versions/paths and P1521 target paths. Ownership: `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/FIND_AND_FETCH_ARTIFACTS/` and `tests/test_find_and_fetch_artifacts.py` only. Output: a read-only Tool that meets the accepted source contract, returns Artifact IDs by default and selected properties/sections only when requested, and preserves canonical carrier identity without filename inference.

P1522 acceptance is a true dispatch blocker. Test-first golden verification must cover permitted filters, requested statuses/properties, pagination/coverage, selected fetch, malformed/missing/duplicate/incomplete diagnostics, rejected arbitrary evaluation, no secret return, no mutation authority, and stable snapshot. Save actual command/result; P1527 owns integration.

### Definition of Done

The owned Tool and golden tests pass against accepted source pins with truthful remainder; host proof is not MCP or image proof.
