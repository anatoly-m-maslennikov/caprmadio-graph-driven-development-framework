---
atom_id: CA-P-1540
content_role: Plan
type: Plan
label: Task
work_sequence_number: 13
current_scope_unit: caprmedio
claim_target_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: "Bind bounded repeated Step Run identities"
  depends_on: [Implementation, Workflow, Action, Evaluation, Journal]
version: 3
updated_at: "2026-10-04 22:18:37 +0000"
relations:
  is_decomposition_of: [CA-P-1137]
  blocks: [CA-P-1517]
---
# Summary

Bind bounded repeated Step Run identities

## Objective

Within <=15 minutes, test-first finish this bounded original-thirteen execution remainder under current accepted source/RMED.

## Details

Own selected_execution.py requested-Run validation, actual Step identity selection and tests/test_selected_execution.py only. Do not edit P1536's Step packet semantics except required safe interface integration. Current requested_runs pins one row per manifest Step, but executor uses actual traversal ordinal: skipping a Step can journal the wrong definition, and revisiting reaches unregistered IDs. Fix by manifest Step identity with per-definition visit counters and caller-declared bounded visit limits; first-visit ID shape may remain compatible, additional predeclared visit rows have distinct identities/current exact definitions and parent lineage. Default visit limit=1; explicit positive bounded parameters support authorized retry visits without unbounded dynamic admissions. Predeclare permitted rows before effects; shared lazy Run support starts only actually traversed Runs, never records unused planned rows. Respect existing source transitions and retry permission/budget; no hardcoded successor policy or invented automatic retries. Test real shared RunExecutionSession and canonical Journal in disposable Projects, branched skipping and bounded revisit, wrong/stale rows rejected, exhausted/unregistered visit before effect, terminal recovery no replay. Publish requested-runs helper for fixtures/MCP. No shared support/source/RMED/backend/MCP/real Project changes. Root saves result; image/Codex transport remains separate.

Read current Epic/P1517/P1519, directly bound source/RMED and current active Method projection before edits. Inherit 90% confidence and mechanical save exception. You are not alone; preserve concurrent work and use apply_patch. No harvesting, FPF, paid Agent call, production authority mutation, external deployment or permission bypass. Root owns Plan writes/commits. Unfinished work retains an exact truthful frontier.

### Definition of Done

The bounded owned behavior has actual functional golden evidence, commands/results and exact changed files. No aggregate Docker/MCP/Agent proof is implied.

## Result

The executor now derives requested and actual Step Run IDs from manifest Step identity, not traversal position. First visits retain :step:<manifest ordinal>; explicit bounded run_visit_limits admit distinct :visit:<n> Step and Action rows with current exact definitions and parent lineage. build_requested_runs(...) exposes the planned-row construction for fixtures. Default one visit and exact-row validation remain fail-closed before effects.

Worker evidence: 18 tests passed and 1 failed in the real selected_execution suite. Branch skipping recorded the correct manifest Step; exhaustion, bad/stale rows and terminal recovery/no replay passed. The authorized shared-session loop failed before its handler because the shared recorder repeated identical definition_bindings for the distinct planned visits. CA-C-439 records that defect; CA-P-1541 owns its narrow repair and blocks completion here.

Changed files: WORKFLOW_ORCHESTRATOR/selected_execution.py and tests/test_selected_execution.py.

Final integration: CA-P-1541 repaired the independently owned shared-recorder definition deduplication. Root reran the current twenty-test selected-execution suite, seven selected-Run support tests, four Journal schema-v5 tests and two dedicated repeated-binding regressions in the development Docker worker; all passed. The real shared-session loop now retains distinct predeclared visit Run IDs and unique definition bindings; skipped Steps retain their actual manifest identities. This bounded packet is Done. Live Agent startup, all-route MCP/queue and immutable-image proof remain separately required.
