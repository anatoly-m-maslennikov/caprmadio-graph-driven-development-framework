---
atom_id: CA-P-1537
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: "Complete Artifact query contract and golden corpus"
  depends_on: [Implementation, Tool, Evaluation]
version: 1
updated_at: "2026-10-04 21:37:54 +0000"
relations:
  is_decomposition_of: [CA-P-1525]
  blocks: [CA-P-1525]
---
# Summary

Complete Artifact query contract and golden corpus

## Objective

Within <=15 minutes, test-first finish this bounded P1525 implementation remainder. The original source acceptance is still current; do not narrow its required behavior to existing passing tests.

## Details

Own only FIND_AND_FETCH_ARTIFACTS/find_and_fetch_artifacts.py, __init__.py and tests/test_find_and_fetch_artifacts.py. Read accepted P1532 eight source pins and current active Methods. Use current existing query_filter API, coordinated with P1538 (no parser edits). Complete retained snapshot cursor continuation without re-enumeration, canonical section:/ escaped path and correct section boundaries excluding sibling sections and fenced-code pseudoheadings, configuration loaded from real Default/Instance Settings rather than copied defaults, full safe PyYAML (no narrow homemade fallback), temporal normalization, snapshot-wide diagnostics/duplicates, secret/credentials exclusion including nested selected containers and forbidden carriers, root/path/symlink bounds, pre-read resource limits and truthful measured coverage/exhaustion. Add golden cases for every E569 obligation and each configured budget. No query-source or shared Run/MCP/Journal/Projection writes. Use the declared locked PyYAML dependency in a verified usable Python environment; the current development image may need its dependencies refreshed. Golden tests must prove real retained selection and no leakage/mutation, not just successful return.

You are not alone; preserve concurrent edits and use apply_patch. Inherit 90% confidence and mechanical Git exception; root owns Plan writes/commits. No harvesting, FPF, external deployment, actual Project authority mutation or permission bypass. If unfinished, save the exact frontier instead of claiming Done.

### Definition of Done

Every owned requirement has passing golden evidence against current accepted source pins, exact commands/results and truthful integration/image remainder.
