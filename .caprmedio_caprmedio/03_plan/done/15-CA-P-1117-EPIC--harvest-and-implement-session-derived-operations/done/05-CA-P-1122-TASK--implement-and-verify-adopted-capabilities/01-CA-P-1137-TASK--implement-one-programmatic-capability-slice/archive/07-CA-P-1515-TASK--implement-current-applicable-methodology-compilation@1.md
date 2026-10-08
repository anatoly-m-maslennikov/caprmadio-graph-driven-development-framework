---
atom_id: CA-P-1515
content_role: Plan
type: Plan
label: Task
work_sequence_number: 7
current_scope_unit: caprmedio
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
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

implement current applicable methodology compilation

## Objective

Implement one bounded native capability packet from independently accepted RMED. Estimate <=15 minutes; inherit 90% threshold and explicit mechanical Git save exception from P1117. No harvesting, FPF or broader delivery. Dispatch is gated until P1120/P1121 current reviews and initial implementation preflight are Done; creation of this Plan does not authorize bypassing that gate.

### Exact inputs

P1498/P1506 accepted R1839–42/E559–62/D541–43 plus current M226; O011/O152–157/O004–009/O010 supporting; current settings/authoritative Structure and shared D527.

Root supplies the current active Method projection before implementation; relevant Goal and Project Principles remain governing. Reopen current saved R/M/E/D and directly bound O source definitions, not preparation summaries alone.

### Ownership

TOOLS/COMPILE_APPLICABLE_METHODOLOGY/compile_applicable_methodology.py and its tests/test_compile_applicable_methodology.py/bounded selected companion. No corrections to source authority during code unless separately bound and approved.

You are not alone in the codebase. Preserve concurrent/unrelated edits; use apply_patch. A shared implementation interface is owned by P1510; publish small callable API details early and reuse it, not duplicate request seals/Journals. Domain Actions do not own Workflow continuation: the source-bound graph executor owns that.

### Output and verification

Golden CLI/temp-fixture tests first: Core + every settings-activated Extension revision + Project Configuration; active RMEDO only and original Atom relations/source fidelity. Strict caller boundary full rejection matrix. Canonical Journal-backed exact current Operator dispositions only, source corrections trigger fresh selection/assessment and no approval inference. Atomic output preservation/fail/uncertain/pending publication and repeat rebuild determinism. Export actual Action adapters for six-Step graph; no TOML-only approval or installed-extension rejection. Preserve native approved construction behavior.

Test-first exact command in the usable Python/Docker environment:

`python -m unittest discover -s 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/COMPILE_APPLICABLE_METHODOLOGY/tests -p 'test_selected_compilation.py' -v`

Retain actual initial failing golden baseline, real tested saved effects and final result. The development worker's /project mount is a code-test environment, not proof of immutable-image coverage; P1123 owns fresh-image functional evidence. No stale source/unsupported outcome or skipped scenario may count as pass. Update this Plan with actual changed files, commands/results, precise not-yet-covered remainder, then move Done only for the complete bound packet. If the <=15-minute packet runs out of capacity/time, stop at a safe saved frontier and notify root for a separately bound continuation; do not mark partial Done or silently expand.

## Details

### Definition of Done

The exact owned packet has saved implementation and source-driven golden functional proof, with truthful defects/remaining dependencies. Aggregate integration, all13route Docker/MCP proof and full Epic closure remain separate and unclaimed.

## Implementation result — 2026-10-04

Status remains `Active`: the bounded compiler and focused functional proof are saved, but shared Run-support recording and source-graph queue dispatch remain owned integration dependencies. This Plan does not claim their completion or immutable-image coverage.

### Saved implementation

- `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/COMPILE_APPLICABLE_METHODOLOGY/compile_applicable_methodology.py`
  - accepts only the strict governed request contract through `run_request`; the legacy CLI builds that request without exposing mutable source or output locations;
  - selects Active Core, settings-selected installed Extension revisions, and Active Project Configuration from Project Structure and Framework Settings; inactive and unselected candidates are reported but never emitted;
  - requires exact canonical-Journal decision references for conflict selections. A Project Configuration TOML file is not authority; source change makes decision provenance stale and blocks publication;
  - stages the full derived role set under `.caprmedio_runtime`, rechecks the whole source state, atomically replaces generated files with rollback, and reports pending recording rather than inventing a Journal receipt;
  - exports `ACTION_ADAPTERS` for CA-O-004 through CA-O-009. These are individual Action adapters only; they do not execute or continue CA-O-011.
- `tests/test_selected_compilation.py` adds current golden/strict-boundary evidence. Existing compatibility tests now retain no TOML-only authorization premise.

### Verification

Initial test-first run of the newly added selected suite failed before compiler execution because its temporary fixture attempted to recreate an already-created `.caprmedio_caprmedio` directory. The fixture was corrected with `exist_ok=True`; that setup failure is retained as test-authoring evidence and is not represented as a product failure.

Passed locally:

`python -m unittest discover -s 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/COMPILE_APPLICABLE_METHODOLOGY/tests -p 'test_*.py' -v`

Result: 28 tests passed. This includes deterministic regeneration, output-preserving rollback, strict request rejections, every settings-activated Extension revision, active Extension source fidelity, canonical-Journal selection, stale-decision rejection, and recovery-reference gating.

Passed in the development container after the final publication implementation:

`docker exec -i -w /project caprmedio-ea535e2c0d4e-worker-1 python -m unittest 102_FRAMEWORK_ENGINE.201_PROGRAMMATIC.201_TOOLS.COMPILE_APPLICABLE_METHODOLOGY.tests.test_selected_compilation.SelectedCompilationTest.test_golden_active_core_extension_and_project_configuration_preserve_source_fidelity -v`

Result: 1 test passed.

### Remaining integration

- P1510 must pass canonical shared Run/Journal recorder handles into these adapters so a successful publication can transition from `pending_recording` to a receipt-backed published result without duplicate Journal semantics.
- The source-graph interpreter / selected queue must register and dispatch the six exported adapters in CA-O-011 order; this compiler intentionally does not own Workflow continuation.
- P1123 owns fresh Docker-image functional proof. The development-container test above does not establish immutable-image coverage.
