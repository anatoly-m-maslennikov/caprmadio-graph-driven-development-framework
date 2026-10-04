---
atom_id: CA-P-1518
content_role: Plan
type: Plan
label: Task
work_sequence_number: 9
current_scope_unit: caprmedio
claim_target_scope_unit: MCP
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

implement selected mcp routes and source manifest

## Objective

Implement one bounded native capability packet from independently accepted RMED. Estimate <=15 minutes; inherit 90% threshold and explicit mechanical Git save exception from P1117. No harvesting, FPF or broader delivery. Dispatch is gated until P1120/P1121 current reviews and initial implementation preflight are Done; creation of this Plan does not authorize bypassing that gate.

### Exact inputs

P1499/P1504 accepted current native R1847/48,E567/68,D547/48; D521v3 and D527v2; A1142 current thirteen source graph bindings.

Root supplies the current active Method projection before implementation; relevant Goal and Project Principles remain governing. Reopen current saved R/M/E/D and directly bound O source definitions, not preparation summaries alone.

### Ownership

MCP/implementation_server.py and new selected_routes.py/selected_route_bindings.json + focused tests/test_selected_routes_mcp.py; only necessary existing service/gateway compatibility changes. No DBOS backend, shared support or domain modules.

You are not alone in the codebase. Preserve concurrent/unrelated edits; use apply_patch. A shared implementation interface is owned by P1510; publish small callable API details early and reuse it, not duplicate request seals/Journals. Domain Actions do not own Workflow continuation: the source-bound graph executor owns that.

### Output and verification

Golden MCP contract tests first, expose13 explicit capability route names using shared preview/execute service and source-bound executor; no adapter-local executor. One immutable full13 route manifest derived from current source graphs/Step Actions/entry/on_result/sourcepathsVersionsdigests, canonicaldigest and no second authority; incomplete/stale rejected. Alias Archive is same route. Preserve8existinghelpers/hotreload. Existing workflow_orchestrator tagged enqueue_selected/status allows independently queued selected routes via sameAPP. Update discovery/result/status references only withinselectedscope. Publish manifest schema/internalAPI immediately for orchestrator consumer.

Test-first exact command in the usable Python/Docker environment:

`python -m unittest discover -s 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/tests -p 'test_selected_routes_mcp.py' -v`

Retain actual initial failing golden baseline, real tested saved effects and final result. The development worker's /project mount is a code-test environment, not proof of immutable-image coverage; P1123 owns fresh-image functional evidence. No stale source/unsupported outcome or skipped scenario may count as pass. Update this Plan with actual changed files, commands/results, precise not-yet-covered remainder, then move Done only for the complete bound packet. If the <=15-minute packet runs out of capacity/time, stop at a safe saved frontier and notify root for a separately bound continuation; do not mark partial Done or silently expand.

## Details

### Definition of Done

The exact owned packet has saved implementation and source-driven golden functional proof, with truthful defects/remaining dependencies. Aggregate integration, all13route Docker/MCP proof and full Epic closure remain separate and unclaimed.

## Actual implementation result

Saved the bounded MCP projection in `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/`: `selected_routes.py`, canonical `selected_workflow_bindings.json`, additive server registration, and `tests/test_selected_routes_mcp.py`.  The manifest contains exactly the thirteen adopted route names with ordered Workflow/Step/Action pins, native Action pins, entry Steps, On Result edges, source freshness, and a SHA-256 digest of its RFC 8785 canonical form with the self field omitted.  `selected_manifest_contract()` publishes this consumer boundary; `load_selected_manifest()` rejects incomplete, stale, or tampered pins before every routed call.

The adapter preserves the stable gateway and existing helpers. Preview injects the shared lazy `RunTracker` with a live manifest observer and no local executor. Execute re-derives a current preview receipt, then passes only the exact authorized request to the existing `enqueue_selected` APP path; route code never creates a Workflow or Action Run itself. Observation is non-dispatching and recovery forwards one pending event reference only.

Initial golden baseline (before these files existed) failed as expected with `ModuleNotFoundError: No module named 'selected_routes'`. After implementation, the required Docker command passed:

`docker exec -i -w /project caprmedio-ea535e2c0d4e-worker-1 python -m unittest discover -s 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/tests -p 'test_selected_routes_mcp.py' -v`

Result: 6 tests passed, including all thirteen explicit preview routes, fresh immutable pins, stale and shadow-manifest refusal, exact execute forwarding, and constrained recovery. A direct server inventory also confirmed all thirteen selected routes and all pre-existing implementation-server tools are registered.

Status remains **Active**, not Done. At this saved frontier the queue consumer still observed an earlier binding representation (`workflow.kind/path/sha256` and per-step `steps`) whereas D547v3 supplies `source_path/digest`, `ordered_steps`, `ordered_actions`, and route-level `on_result`. P1517 must consume this published canonical schema and complete the real enqueue/dispatch handoff; P1123 separately owns fresh immutable-image functional proof. No all-route Docker execution, terminal Action effects, or queue completion is claimed here.

### Reopened manifest graph-sufficiency repair

The current P1517 consumer now reads the D547v3 representation, which exposed a source-projection defect rather than a queue defect: `create_atom`, `replace_atom`, and `change_atom_status` each bound only CA-O-129 but incorrectly carried the Update-only CA-O-145/CA-O-129 edges. The initial physical cross-consumer baseline correctly refused those three routes with `D547 On Result source is not a bound Step`.

The repaired manifest retains those two lifecycle edges only for `update_atom`, whose entry and ordered Steps actually bind CA-O-145 and CA-O-129. The three non-Update routes now contain no invented successor edge. `selected_routes.load_selected_manifest()` also validates every edge source and target against the route's bound Steps (with `complete` as the sole declared terminal target), before a request reaches shared support.

`build_applicable_methodology` now reproduces CA-O-011's current governed transition conditions verbatim, including the explicit CA-O-157 `completed publication from the still-valid final frontier` to `complete` terminal. The negative/escalation outcomes remain non-edges as the source defines them; no compiler-result alias or new terminal policy was invented. Generic compiler labels therefore remain fail-closed unless a future source-authorized mapping is supplied.

Added a disposable physical-manifest test that copies the exact manifest and every pin into a fresh Project, derives the expected Workflow/Step/Action Run identities from the queue's validated graph, and calls `SelectedExecution.freeze` for each of the thirteen routes. It creates no worker, DBOS job, or Action effect. The required Docker test command now passes seven tests, including that all-thirteen cross-consumer freeze proof:

`docker exec -i -w /project caprmedio-ea535e2c0d4e-worker-1 python -m unittest discover -s 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/tests -p 'test_selected_routes_mcp.py' -v`

This supersedes the earlier queue-schema compatibility remainder. Status remains **Active** because no selected Action dispatch, terminal effect, or fresh immutable-image functional proof is claimed; P1123 owns that separate proof. P1520 query work is out of this packet.

### Projection placement follow-up

`selected_routes.py` now resolves the derived manifest only from the Project's configured `paths.control_root` under `_projection/selected_workflow_bindings.json` (default `.caprmedio_caprmedio`). The resolved repository-relative path is carried in both `selected_manifest_contract(root)` and the exact accepted `request.definition_manifest`; an old Engine delivery path is rejected even with a matching digest. The loader's in-memory result carries that actual path without changing the immutable four-field manifest schema or treating `source_freshness` as a second outer-manifest reference.

Added a focused resolver test, including a custom configured control root, and corrected this test fixture's Journal root to `_journal`. Its Docker invocation passed:

`docker exec -i -w /project caprmedio-ea535e2c0d4e-worker-1 python -m unittest 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/tests/test_selected_routes_mcp.py -k manifest_ref_uses_the_configured_control_root_projection`

At this point the complete MCP test module correctly fails its real-manifest setup because the physical projection has not yet been moved by the separately owned placement packet; the old Engine location is deliberately not used as a fallback. The manifest relocation and D547 authority update remain outside this change. No all-route result is claimed by this follow-up until that projection is present.
