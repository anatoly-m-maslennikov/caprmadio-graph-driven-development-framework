---
atom_id: CA-P-1514
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
  governs: "Selected Workflow implementation delivery"
  depends_on: [Implementation, Workflow, Action, Evaluation, Journal]
version: 1
updated_at: "2026-10-04 19:12:21 +0000"
relations:
  is_decomposition_of: [CA-P-1137]
  blocks: [CA-P-1123, CA-P-1164, CA-P-1165, CA-P-1166]
---
# Summary

implement source traceable entity and term graphs

## Objective

Implement one bounded native capability packet from independently accepted RMED. Estimate <=15 minutes; inherit 90% threshold and explicit mechanical Git save exception from P1117. No harvesting, FPF or broader delivery. Dispatch is gated until P1120/P1121 current reviews and initial implementation preflight are Done; creation of this Plan does not authorize bypassing that gate.

### Exact inputs

P1497 PASS; native R1835–38/E555–58/D538–40; O133–138; existing generator and shared D527.

Root supplies the current active Method projection before implementation; relevant Goal and Project Principles remain governing. Reopen current saved R/M/E/D and directly bound O source definitions, not preparation summaries alone.

### Ownership

TOOLS/GENERATE_ENTITY_GRAPH/generate_entity_graph.py and sibling tests/test_selected_graphs.py/fixture corpus. Preserve compatible existing consumers; no source repair or Journal rewrite.

You are not alone in the codebase. Preserve concurrent/unrelated edits; use apply_patch. A shared implementation interface is owned by P1510; publish small callable API details early and reuse it, not duplicate request seals/Journals. Domain Actions do not own Workflow continuation: the source-bound graph executor owns that.

### Output and verification

Test-first strict graph request supports entities_graph and terms_graph separately. Complete Entity/Property/Relation/Atom-source/authoritative Structure graph; governed Terms tree/parent ancestor/dependency/unresolved/conflict/cycle sets, graph-specific relations and exact source revision/location/digest lineage. Canonical deterministic publication + immediate final source frontier recheck; any unmet quality blocks built/no_op, no source mutations. Export individual O134/O137 Action adapters; shared outer Run result and current source binding consumed, full golden/negative/effect tests.

Test-first exact command in the usable Python/Docker environment:

`python -m unittest discover -s 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_ENTITY_GRAPH/tests -p 'test_selected_graphs.py' -v`

Retain actual initial failing golden baseline, real tested saved effects and final result. The development worker's /project mount is a code-test environment, not proof of immutable-image coverage; P1123 owns fresh-image functional evidence. No stale source/unsupported outcome or skipped scenario may count as pass. Update this Plan with actual changed files, commands/results, precise not-yet-covered remainder, then move Done only for the complete bound packet. If the <=15-minute packet runs out of capacity/time, stop at a safe saved frontier and notify root for a separately bound continuation; do not mark partial Done or silently expand.

## Details

### Definition of Done

The exact owned packet has saved implementation and source-driven golden functional proof, with truthful defects/remaining dependencies. Aggregate integration, all13route Docker/MCP proof and full Epic closure remain separate and unclaimed.
