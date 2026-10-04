---
atom_id: CA-P-1512
content_role: Plan
type: Plan
label: Task
work_sequence_number: 4
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
version: 1
updated_at: "2026-10-04 19:57:03 +0000"
relations:
  is_decomposition_of: [CA-P-1137]
  blocks: [CA-P-1123, CA-P-1164, CA-P-1165, CA-P-1166]
---
# Summary

implement authoritative project structure effects

## Objective

Implement one bounded native capability packet from independently accepted RMED. Estimate <=15 minutes; inherit 90% threshold and explicit mechanical Git save exception from P1117. No harvesting, FPF or broader delivery. Dispatch is gated until P1120/P1121 current reviews and initial implementation preflight are Done; creation of this Plan does not authorize bypassing that gate.

### Exact inputs

P1495/P1503 accepted native PROJECT_STRUCTURE current R1829–32/E549–52/D533–35; O015/O139–144 and callable O004/O012/O005/O013/O014; current authoritative TOML schema and shared D527.

Root supplies the current active Method projection before implementation; relevant Goal and Project Principles remain governing. Reopen current saved R/M/E/D and directly bound O source definitions, not preparation summaries alone.

### Ownership

TOOLS/WORKFLOW_OPERATIONS/PROJECT_STRUCTURE/project_structure.py and sibling tests/test_project_structure.py. Normal implementation placement remains below declared TOOLS delivery root; no new Scope Unit. No shared library/orchestrator edits.

You are not alone in the codebase. Preserve concurrent/unrelated edits; use apply_patch. A shared implementation interface is owned by P1510; publish small callable API details early and reuse it, not duplicate request seals/Journals. Domain Actions do not own Workflow continuation: the source-bound graph executor owns that.

### Output and verification

Strict typed structural parameters under shared outer envelope, Create/Rename/Move/Remove authoritative TOML mutations, complete type/order/Label/navigation/depth/Authority Mode/path validation, explicit direct-parent Goal gap disposition, exact approved reference/carrier repairs, no inferred delivery folder creation/broad recursive deletion. Preserve required history and exact partial/recovery evidence. Export individual Action adapters consumed by the source-bound six-Step graph; golden real TOML/temp-project effects and non-happy cases first.

Test-first exact command in the usable Python/Docker environment:

`python -m unittest discover -s 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/WORKFLOW_OPERATIONS/PROJECT_STRUCTURE/tests -p 'test_project_structure.py' -v`

Retain actual initial failing golden baseline, real tested saved effects and final result. The development worker's /project mount is a code-test environment, not proof of immutable-image coverage; P1123 owns fresh-image functional evidence. No stale source/unsupported outcome or skipped scenario may count as pass. Update this Plan with actual changed files, commands/results, precise not-yet-covered remainder, then move Done only for the complete bound packet. If the <=15-minute packet runs out of capacity/time, stop at a safe saved frontier and notify root for a separately bound continuation; do not mark partial Done or silently expand.

## Details

### Definition of Done

The exact owned packet has saved implementation and source-driven golden functional proof, with truthful defects/remaining dependencies. Aggregate integration, all13route Docker/MCP proof and full Epic closure remain separate and unclaimed.

## Result

Implemented the bounded PROJECT_STRUCTURE domain Action adapters below the declared TOOLS delivery root:

- `create_scope_unit`, `rename_scope_unit`, `move_scope_unit`, and `remove_scope_unit` delegate to the strict route-domain `apply_scope_unit_action`; `rollback_scope_unit_change` restores only the exact still-current partial cutover boundary.
- The domain API accepts only route-owned `parameters` and returns `structural_result` states. It does not create a Run, Journal event, proposal receipt, outer mode, or Workflow continuation; those remain CA-D-527/RUN_SUPPORT responsibilities.
- Authoritative TOML input is validated for complete declaration fields, canonical Name/Label, direct parent and acyclicity, Ordered-only local order, independent navigation number, derived structural depth, safe distinct path fields, and explicit/inherited Authority Mode. Create and Move require a direct-parent Goal coverage disposition; an authorized named missing-Goal gap is reported, not inferred, invented, or blanket-rejected.
- Exact reference frontier entries are digest-pinned and replace only an explicitly named text occurrence. Remove deletes only its selected declaration, rejects descendant removal, preserves named Carrier/history dispositions, and never creates a delivery folder or recursively deletes filesystem content. A post-declaration failure returns exact applied/unapplied effects and a constrained rollback boundary.

Changed files:

- `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/WORKFLOW_OPERATIONS/PROJECT_STRUCTURE/project_structure.py`
- `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/WORKFLOW_OPERATIONS/PROJECT_STRUCTURE/tests/test_project_structure.py`

Actual verification in the usable development container:

1. Initial empty test-directory baseline: `Ran 0 tests` / `NO TESTS RAN`.
2. Test-first golden baseline after adding the test: expected import error because `project_structure.py` did not exist.
3. `docker exec -i -w /project caprmedio-ea535e2c0d4e-worker-1 python -m unittest discover -s 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/WORKFLOW_OPERATIONS/PROJECT_STRUCTURE/tests -p 'test_project_structure.py' -v` passed `10` tests: authorized Create with inherited mode and a named Goal gap; Rename/Move exact repair; invalid/stale no-effect; non-recursive Remove/no-op; injected partial then exact rollback; invalid order/path rejection; exact no-op; O015-scoped queue guards; and two shared-service cases.
4. `git diff --check -- 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/WORKFLOW_OPERATIONS/PROJECT_STRUCTURE` passed.

### Shared-service proof

The two shared-service fixtures instantiate P1510's `RunTracker` with a currentness observer, the real route executor, and a UTC Journal context. They prove default preview has no TOML or Journal effect; sealed execute creates only the declared TOML effect; the adapter starts and finishes one actual CA-O-014 Action Run; and canonical schema-v5 Journal started/completed records retain that actual Run ID. The first case retains a named, authorized missing direct-parent Goal gap without inventing a Goal or delivery directory. The second proves a service-level no-op has no effects and a Remove that would delete a parent with declared child returns a failed Action Run/domain conflict while retaining TOML and observed Carrier content.

`queue_action_handlers(repository)` exposes O004/O012/O005/O013/O014 only for the O015 workflow context. Its shared O004/O005 handlers reject other Workflow IDs so a compiler context cannot be interpreted as a structural request. O014 requires `sealed_outer_admission is True`; it returns the domain result and exact effect paths but owns no transition, receipt, or Journal event.

This completes P1512's owned domain and shared-service proof. Selected graph registration, MCP exposure, Docker image proof, and broader workflow integration remain separately owned and unclaimed.
