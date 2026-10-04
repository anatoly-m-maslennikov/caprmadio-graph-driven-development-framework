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
status: Done
subjects:
  governs: "Selected Workflow implementation delivery"
  depends_on: [Implementation, Workflow, Action, Evaluation, Journal]
version: 5
updated_at: "2026-10-04 19:43:47 +0000"
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

## Result

Completed the bounded Tool packet without changing source authority or Journal storage. `build_graph(repository, request)` is the strict CA-D-539 public API; `source_frontier_for` seals the Atom and optional Project Structure frontier; `construct_entities_graph_projection` and `construct_terms_graph_projection` are the CA-O-134/CA-O-137 Action adapters exposed in `ACTION_HANDLERS`; `run` is the queue-facing alias. The API accepts one graph kind, selected Atom identities, optional selected Scope Units, representation configuration, permission evidence, and receipt references. It returns exactly one of `entities_graph` or `terms_graph`, source/revision/path/digest lineage, quality dispositions, effects, non-authoritative status, and receipt references.

Entities output expands source Atoms into identities, frontmatter Properties, Claim digest, Atom-source `GOVERNS`/`DEPENDS_ON` evidence, admitted `IS_BORNE_BY`/`IS_ALLOWED_VALUE_OF` Relations, and optionally bound Project Structure records. Terms output retains Definition authority, admitted `SUBKIND_OF`/`DEPENDS_ON` Relations, parent/ancestor/dependency sets, unresolved references, conflicts, and cycles. Malformed or invalid quality, source mismatch, permission, recording, destination, or stale-existing-output conditions cannot report `built` or `no_op`. Publication is canonical JSON under the registered derived-output root, atomically replaces one file only, and rechecks the full source frontier immediately before output.

Test-first baseline in the development worker was the prescribed command with three errors because `source_frontier_for` and `build_graph` did not exist. The final same command passed four CA-E-555--558 selected-graph tests. The full generator suite passed 16 tests. The persistence case created one temporary derived JSON projection, proved exact-byte `no_op`, then left no source or Journal change.

Changed files:

- `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_ENTITY_GRAPH/generate_entity_graph.py`
- `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_ENTITY_GRAPH/tests/test_selected_graphs.py`

Unclaimed remainder: P1510 owns the shared Run/Journal implementation and P1517 owns the source graph executor integration that will consume the exported handlers; P1518 owns MCP routing; P1519/P1123 own fresh-image Docker/MCP proof. No source repair, authoritative Project Structure change, Journal write, MCP change, or immutable-image claim was made here.

## Reopened

The prior selected fixtures used retired `cce_form`, `cce_version`, and nested `continuant`/`occurrent` Subject schema. The saved parser therefore did not prove the current scalar-or-list `subjects.governs`/`subjects.depends_on` carrier format, and `cce_form == definition` was not a current Definition admission rule. This Plan is Active until a self-sufficient current-format golden fixture reproduces and verifies the compatibility repair, active-status filtering, explicit current Definition admission, and expanded Entity/Property/Relation source representation.

## Reopened Result

The current-format fixture first failed: the retired parser rejected scalar/list Subjects and `status: Done` remained in the frontier. The repaired parser admits current scalar, inline-list, and direct-list `subjects.governs`/`subjects.depends_on` values with `temporal_form: CURRENT`; it preserves the nested `continuant`/`occurrent` form and `cce_form` as legacy compatibility only. Current source selection excludes an explicitly non-Active Carrier with a visible `inactive-status-skipped` diagnostic. Term membership is now admitted from current `type: Definition` or `content_role: Definition`, with legacy `cce_form: definition` retained as a compatibility fallback.

The Entities Graph now records governed subject identities as Entity nodes, complete frontmatter Property nodes, direct Relation nodes, structural `IS_BORNE_BY`/`IS_ALLOWED_VALUE_OF` relations where declared, and a separate expanded `source_atoms` collection. It no longer presents Atom identifiers themselves as Entity identities. `queue_action_handlers(repository)` supplies CA-O-134/O-137 handlers in `SelectedExecution`'s frozen-context contract, returning declared graph outcomes and effect references without owning a transition, receipt, or retry.

Final current-format verification passed 7 selected tests and 19 generator tests in the Docker development worker. The current-source fixture covers scalar `governs`, inline-list `governs`, inline-list `depends_on`, Active filtering, current Definition Type term admission, expanded Entity/Property/Relation/Atom output, and the queue adapter contract. No source authority, Journal, MCP route, or queue module was changed. P1517 still owns registering `queue_action_handlers(repository)` with `SelectedExecution`; P1510/P1518/P1519/P1123 retain their prior boundaries.
