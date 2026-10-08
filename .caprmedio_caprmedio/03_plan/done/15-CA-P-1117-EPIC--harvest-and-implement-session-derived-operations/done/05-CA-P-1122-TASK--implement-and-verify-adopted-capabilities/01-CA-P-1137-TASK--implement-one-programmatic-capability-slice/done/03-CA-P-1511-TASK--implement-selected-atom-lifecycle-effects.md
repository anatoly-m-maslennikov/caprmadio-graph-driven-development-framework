---
atom_id: CA-P-1511
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
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
version: 4
updated_at: "2026-10-08 15:33:32 +0000"
relations:
  is_decomposition_of: [CA-P-1137]
  blocks: [CA-P-1123, CA-P-1164, CA-P-1165, CA-P-1166]
---
# Summary

implement selected atom lifecycle effects

## Objective

Implement one bounded native capability packet from independently accepted RMED. Estimate <=15 minutes; inherit 90% threshold and explicit mechanical Git save exception from P1117. No harvesting, FPF or broader delivery. Dispatch is gated until P1120/P1121 current reviews and initial implementation preflight are Done; creation of this Plan does not authorize bypassing that gate.

### Exact inputs

P1494/P1501 accepted native ATOM_LIFECYCLE current R1825–28,E545–48,D530–32; O127/128/129/145,O067/native lifecycle bindings and shared D527v3.

Root supplies the current active Method projection before implementation; relevant Goal and Project Principles remain governing. Reopen current saved R/M/E/D and directly bound O source definitions, not preparation summaries alone.

### Ownership

Existing TOOLS atom_operations.py, lifecycle_intents.py, REPLACE_ATOM/replace_atom.py and bounded native lifecycle fixtures/tests. Preserve compatible existing entrypoints and unrelated changes; do not edit shared support or orchestrator.

You are not alone in the codebase. Preserve concurrent/unrelated edits; use apply_patch. A shared implementation interface is owned by P1510; publish small callable API details early and reuse it, not duplicate request seals/Journals. Domain Actions do not own Workflow continuation: the source-bound graph executor owns that.

### Output and verification

Create/Update/Replace/Change Status effect adapters with full carried properties and complete Carrier sets, current qualified status models, exact currentness and safe paths. Same Summary Update preserves identity/history with meaningful Version rule; changed Summary emits terminal non-effect Replace handoff. Replace all admitted >=1 successors then archive one predecessor truthfully. Status already same no-op; authorized model change may produce reported broken active refs/referrers with no auto repair. Expose action-level callables to the graph coordinator, not hardcoded Workflow transition policy. Golden full requests first incl Create/duplicate/stale/multitarget/summary handoff/status/partial.

Test-first exact command in the usable Python/Docker environment:

`python -m unittest discover -s 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tests -p 'test_selected_atom_lifecycle.py' -v`

Retain actual initial failing golden baseline, real tested saved effects and final result. The development worker's /project mount is a code-test environment, not proof of immutable-image coverage; P1123 owns fresh-image functional evidence. No stale source/unsupported outcome or skipped scenario may count as pass. Update this Plan with actual changed files, commands/results, precise not-yet-covered remainder, then move Done only for the complete bound packet. If the <=15-minute packet runs out of capacity/time, stop at a safe saved frontier and notify root for a separately bound continuation; do not mark partial Done or silently expand.

## Details

### Definition of Done

The exact owned packet has saved implementation and source-driven golden functional proof, with truthful defects/remaining dependencies. Aggregate integration, all13route Docker/MCP proof and full Epic closure remain separate and unclaimed.

### Implementation result — 2026-10-04

Implemented the route-local adapter API in `lifecycle_intents.py`:
`create_atom_action`, `update_atom_action`, `replace_atom_action`, and
`change_status_atom_action`. Each takes one complete sealed Carrier boundary
and caller-provided `execute`/`authorized` admission flags; it returns only
route facts and does not create a Run, receipt, Event, Journal entry, retry, or
Workflow continuation. `carrier_descriptor` supplies the exact full current
Carrier seal for the shared CA-D-527 caller.

`atom_operations.py` now supplies atomic complete-Carrier primitives used by
those actions. New Create and successor carriers must explicitly carry the
same `atom_id` as their filename; it is never inferred or inserted. A semantic
Update retains a role-local `@Version` prior revision before writing the next
Version. Summary-changing Update accepts validated, not-yet-published complete
successor inputs and returns them unchanged in its terminal, non-effect
Replace handoff. Replace preflights every supplied successor, publishes all of
them before predecessor archive, and returns `partial` plus the exact unknown
remainder when a later successor or predecessor archive fails. A non-Archive
Change Status atomically relocates a carrier to the qualified status subfolder
and promotes `Active` back to the role root; its model need not invent a
`type` when the current Content Role model has none. Archive only reports
broken active references/referrers and does not repair them. The replacement
module re-exports `replace_atom_action` without changing its legacy
deferred-intent CLI.

Initial test-first baseline (Docker development worker) failed because the
action API did not yet exist: `ImportError: cannot import name LifecycleError`.
The updated current-contract golden cases then failed as expected before this
revision (`1` failure, `5` errors): missing frontmatter identity was accepted,
Summary handoff and Replace demanded already-existing successors, `type` was
mandatory in status models, and semantic Update did not emit preserved
history. Final verification passed:

`docker exec -i -w /project caprmedio-ea535e2c0d4e-worker-1 python -m unittest discover -s 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tests -p 'test_selected_atom_lifecycle.py' -v` — 7 tests passed. Coverage includes explicit matching/mismatched IDs, non-placeholder status models and status relocation/promotion, native Version history, supplied successor publication order, and both second-successor and archive-failure truthful partial results.

`docker exec -i -w /project caprmedio-ea535e2c0d4e-worker-1 python -m unittest discover -s 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_SEARCH/tests -p 'test_atom_operations.py' -v` — 19 tests passed. `python -m py_compile` passed for all three owned modules.

Changed paths: `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/atom_operations.py`,
`102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/lifecycle_intents.py`,
`102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/REPLACE_ATOM/replace_atom.py`,
and `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tests/test_selected_atom_lifecycle.py`.

At the 2026-10-04 checkpoint this Plan remained Active. The route-local
packet was saved and its bounded golden cases passed, but shared execution
and current-image proof were then pending.
P1510 must wire these action callables into the shared seal/receipt service;
its run identities, durable Journal evidence, recording-pending handling,
retry behavior, post-effect verification/recording fault injection, and the
cross-route MCP/fresh-image Docker proof remain outside this Plan's ownership.

### Accepted retained-scope closure

the current first-cut lifecycle implementation, rollback/partial and composition evidence is accepted in CA-P-1655@10. W01-W04 also passed actual selected Docker/stdio and authenticated Docker HTTP execution, with native effects and canonical Workflow/Action Journal records. This satisfies this native lifecycle packet's previously pending retained-scope integration. Broader original-route and formal Release obligations remain deferred, not claimed complete. The Operator-authorized administrative Git closure follows a failed read-only MCP queue-status attempt; it dispatches no closure Run or Event.
