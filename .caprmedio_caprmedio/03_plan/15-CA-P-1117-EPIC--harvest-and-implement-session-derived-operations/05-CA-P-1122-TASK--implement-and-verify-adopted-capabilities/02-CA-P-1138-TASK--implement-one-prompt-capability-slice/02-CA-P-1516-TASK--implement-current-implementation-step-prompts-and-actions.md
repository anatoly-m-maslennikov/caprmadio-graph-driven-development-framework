---
atom_id: CA-P-1516
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: PROMPTS
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: "Selected Workflow implementation delivery"
  depends_on: [Implementation, Workflow, Action, Evaluation, Journal]
version: 1
updated_at: "2026-10-04 19:39:00 +0000"
relations:
  is_decomposition_of: [CA-P-1138]
  blocks: [CA-P-1123, CA-P-1164, CA-P-1165, CA-P-1166]
---
# Summary

implement current implementation step prompts and actions

## Objective

Implement one bounded native capability packet from independently accepted RMED. Estimate <=15 minutes; inherit 90% threshold and explicit mechanical Git save exception from P1117. No harvesting, FPF or broader delivery. Dispatch is gated until P1120/P1121 current reviews and initial implementation preflight are Done; creation of this Plan does not authorize bypassing that gate.

### Exact inputs

P1500 PASS; current native R1843–46/M326–29/E563–66/D544–46; O016/seven current Steps/Actions; active Method projection distinct RED; existing delivered IMPLEMENTATION_WORKFLOW prompts/tests.

Root supplies the current active Method projection before implementation; relevant Goal and Project Principles remain governing. Reopen current saved R/M/E/D and directly bound O source definitions, not preparation summaries alone.

### Ownership

102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/IMPLEMENTATION_WORKFLOW/* including source_bindings.json, seven short prompts, packet/Method projection helper and implementation_actions.py; its focused tests. No generic DBOS backend/shared support edits.

You are not alone in the codebase. Preserve concurrent/unrelated edits; use apply_patch. A shared implementation interface is owned by P1510; publish small callable API details early and reuse it, not duplicate request seals/Journals. Domain Actions do not own Workflow continuation: the source-bound graph executor owns that.

### Output and verification

Refresh 17 stale bindings and correct old PROGRAMMATIC-only E2E wording. Golden mock first and runnable command tests before behavior; compiled active Ms separate selected RED; <=15min P subtasks; exactly supplied Integrated/Isolated context per Agentic Step and replaceable callable Agent adapter (Codex CLI/current worker available). Actual seven Action handlers gather/prepare/implement/check/diagnose/admitrepair/repair return current labels, evidence and permissions/retry state. Separate corrective Method learning. Add short self-contained step prompts and truthful complete output envelopes without requiring MCP. Export action handlers for existing orchestrator; no fake live LLM proof.

Test-first exact command in the usable Python/Docker environment:

`python -m unittest discover -s 102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/IMPLEMENTATION_WORKFLOW/tests -v`

Retain actual initial failing golden baseline, real tested saved effects and final result. The development worker's /project mount is a code-test environment, not proof of immutable-image coverage; P1123 owns fresh-image functional evidence. No stale source/unsupported outcome or skipped scenario may count as pass. Update this Plan with actual changed files, commands/results, precise not-yet-covered remainder, then move Done only for the complete bound packet. If the <=15-minute packet runs out of capacity/time, stop at a safe saved frontier and notify root for a separately bound continuation; do not mark partial Done or silently expand.

## Details

### Definition of Done

The exact owned packet has saved implementation and source-driven golden functional proof, with truthful defects/remaining dependencies. Aggregate integration, all13route Docker/MCP proof and full Epic closure remain separate and unclaimed.

## Result

Completed the bounded IMPLEMENTATION_WORKFLOW packet.

- Refreshed `source_bindings.json` from the reviewed R1843–46/M326–29/E563–66/D544–46 sources and current O016v11, seven Steps, and seven Actions; all identities, versions, paths, and digests are now checked.
- Added `implementation_actions.py`: current Action exports, `implement_selected_queue`, separate active-M projection validation from selected R/D/E, exact context/permission/under-fifteen-minute Isolated-handoff checks, test-first/retry gates, replaceable Agent dispatch, and truthful result envelopes. It does not require MCP, own Workflow transitions, or duplicate Journal/shared-run effects.
- Expanded focused tests for the refreshed frontier, mock-Agent envelope, blocked context/test-first/retry cases, and explicit non-live-LLM boundary. Updated README callable API and current packet references.

Initial golden baseline (Docker worker): `python -m unittest discover -s 102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/IMPLEMENTATION_WORKFLOW/tests -v` failed only on all 17 stale pins. Final same command: 10 tests passed. The mock-Agent checks are contract proof only; no live LLM run, immutable image coverage, MCP route coverage, shared `implement_run_support` implementation, aggregate integration, or Epic closure is claimed.

### Functional sufficiency follow-up

Reopened and completed the label-only success gap. `current_source_bindings()` now recomputes each reviewed authority digest and version from live bytes; queue admission requires the complete current source frontier. `prepare_method_projection(method_paths)` produces sorted full-content active-M input with source identity/version/path/digest, and `compile_active_methods` rejects any changed projection while retaining R/D and E as separate inputs. Successful `prepared`, `implemented`, `passed`, and `repaired` results now require their respective performed-work outputs and nonempty evidence.

The Docker test suite now has 12 passing tests. Its golden Agent fixture creates a disposable implementation and assertion, retains the initial actual failing command result (`returncode: 1`), writes the required implementation, and retains final actual passing command output (`returncode: 0`) through CA-O-092, CA-O-093, and CA-O-094 queue calls. Remaining dependencies are only P1510 shared-run integration, P1517 graph/queue integration, fresh immutable-image coverage, MCP routes, and a deliberately separate live-Agent proof; none are claimed here.
