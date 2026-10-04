---
atom_id: CA-P-1117
content_role: Plan
type: Plan
label: Epic
work_sequence_number: 15
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
subjects:
  governs: "Session-derived operational capability delivery"
  depends_on:
    - "Operations"
    - "Implementation"
version: 2
updated_at: "2026-10-04 16:19:11 +0400"
relations: {}
---
# Summary

Harvest and implement session-derived operations

## Objective

Reconcile the retained session-derived evidence, update authoritative methodology Operations and PROGRAMMATIC/PROMPTS RMED, obtain independent subagent review, and implement the adopted capabilities. Build Docker images from which all implemented workflows, MCP and all other implemented tools operate, including pre-existing implementations.

The historical evidence window is [2026-09-04 05:54:15 +0400, 2026-10-04 05:54:15 +0400). Later explicit Operator corrections in this session amend this Plan without shifting that historical cutoff. The latest explicit Operator input overrides earlier input within its authorized scope; Project Principles remain higher authority. Plan creation is not evidence that the harvest or implementations have been executed.

### Operator-closed harvest

The Operator directed: stop harvesting and continue this Epic. The admitted corpus contains 102 completed packets covering 5,463 of 13,011 session records: 4,504 PRIMARY records and 959 worker records. The remaining 7,548 records are outside further harvesting for this Epic. Interrupted CA-P-1325 / CA-A-1043 is preserved as partial evidence and contributes no completed coverage. Context records do not increase coverage.

CA-P-1118 and its unfinished harvest descendants are canceled, not Done. CA-P-1118 is removed from this Epic's required decomposition and its harvest gates are removed. Completed harvest results remain inputs to reconciliation. This amendment does not waive reconciliation, Operations review, RMED, implementation, complete Docker runtime coverage, or closure evidence.

### Governing inputs and destinations

- Current Operator Goal: create and evolve a working CAPRMEDIO Framework; re-read the live Goal carrier before autonomous decisions.
- Project-local active authority and all active Project Principles first; applicable methodology authority next; engine-local RMED thereafter. Current source revisions, not this summary, govern exact distinctions and tiers.
- Authoritative methodology sources: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources`. Reusable, project-independent Operations belong to `001_CORE_META_MODEL`; caprmedio-specific Operations belong to `003_PROJECT_CONFIGURATION`. Reconciliation must record each adopted Operation's destination before authoring. The applicable-methodology projection is derived and never the authoring authority.
- PROGRAMMATIC authority: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC`; delivery: `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC`.
- PROMPTS authority: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/202_FEATURE_PROMPTS`; delivery: `102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS`.
- R = required implementation outcomes/results; M = construction technique for implementation or tests; E = assurance policy/acceptance/test cases; D = delivery/carriers. Use current active source authority to resolve exact applicability and local tiers.
- Reuse the existing orchestrator, MCP, tools, prompts and Docker packaging baseline where appropriate; cross-map older active harvest/migration Plans instead of maintaining duplicate work.
- Keep valuable extracted decisions, manifest/frontiers, review results and execution evidence in governed Analysis/Plan/Journal carriers with source references. Disposable intermediate packets may live in `.caprmedio_tmp` but cannot be the only retained completion evidence.
- Docker coverage includes every implemented workflow, MCP service/interface and all other implemented tools. Runtime input/project-data mounts and explicitly provided external services/credentials are allowed by their governed contracts; baked secrets, undeclared host implementation mounts and host-only packages are not. Local build/run is in scope; publishing images, deploying services, or changing account authorization requires separate authority.

### Composite task sequence

Authoring disposition: the Plan files have been created and independently reviewed. The Operator explicitly authorizes mechanical Git commits for this Epic without the save Tool; if Git cannot commit, skip that commit, retain the unfinished save disposition, and continue independent ready work. CA-C-292 remains an active save-Tool defect, but repairing it is not a prerequisite for this authorized Git path. Record actual commit results without claiming Tool-generated Journal provenance. The stricter body-layout disposition for source conflict CA-C-290 is nonblocking for this Epic's preparation.

- CA-P-1118: Canceled harvest stage; retained completed evidence supplies the following stage.
- CA-P-1119: Reconcile and author methodology operations.
- CA-P-1120: Specify and review PROGRAMMATIC capabilities.
- CA-P-1121: Specify and review PROMPTS capabilities.
- CA-P-1122: Implement and verify adopted capabilities.
- CA-P-1123: Build and verify Docker images for the complete runtime.
- CA-P-1124: Verify project-wide traceability and close the epic.

The remaining required decomposition has six composite stages. Existing bounded execution preflights bind work from the admitted corpus; they must not create further harvest leaves. Each preflight binds a small packet and creates the actual one-file <=15-minute execution leaves plus any identified reconciliation, authoring, implementation, or verification remainder.

### Execution controls

- Each task/subtask has exactly one Plan Markdown file. A composite owns its same-stem directory of child files; the Epic's folder has its mandatory same-stem governing file beside it.
- Each executable leaf has one assigned AI Agent and a work estimate of <=15 minutes. Before execution bind exact input evidence, governing revisions, target files, required result, functional verification and any decision disposition. If the estimate exceeds fifteen minutes, decompose further before execution; never silently expand a leaf.
- After every completed task/subtask, review actual results and current authority, then update every affected next dependent Plan before it executes. Add BLOCKS edges for new remainder/repair/re-review leaves; navigation order is not a dependency. A composite cannot be Done until all required child/remainder work is Done.
- Below the inherited 90% confidence threshold, check the active Operator Goal and Project Principles. If still uncertain, select and record the best safe in-scope option and create a C/Question. The Operator explicitly permits proceeding with that safe authorized choice while the Question remains open; a permission, runtime, evidence, or authority blocker still postpones the affected task. Confidence never grants permissions or overrides higher authority.
- Every issue encountered becomes one appropriately typed Concern at its narrowest owning Scope Unit: Problem for blockers/failures, Question for unresolved choices, Conflict for incompatible governing claims. The Concern owns concern_about to the directly affected task/entity and records evidence, impact and disposition. Do not substitute ephemeral chat notes for C atoms.
- On permission/runtime/evidence blockers, create a C/Problem, retain truthful unfinished task state and frontier, postpone the task and execute another independent ready task. Do not bypass its BLOCKS prerequisites, permission denial, or missing authority.
- Prefer functional, integration, E2E and canary verification. Use unit tests only where they add necessary isolated proof; do not couple acceptance to implementation structure.
- Preserve unrelated changes. Use mechanical Git commits for this Epic's changes under the Operator's explicit exception; do not invoke COMMIT_CHANGE_SET or make its repair a prerequisite. If Git cannot commit, skip that commit and retain a truthful save frontier. Retain required execution Journal evidence and append-only history; do not fabricate save-Tool receipts.

## Details

### Definition of Done

This Epic is not Done if any remaining required composite task or child/remainder/repair/re-review task is unfinished; any admitted harvested decision lacks a source and supersession disposition; any adopted operation/capability lacks current reviewed governing sources, the correct CORE_META_MODEL or PROJECT_CONFIGURATION destination, and implementation; any implemented workflow, MCP interface or other tool lacks passing functional execution evidence from a built Docker image; any blocking issue lacks a resolved Concern; or required source/projection/execution-Journal/Git provenance is incomplete under the Operator-approved save policy. Operator-canceled harvesting is excluded from required completion, not reported as Done. A skipped Git commit requires an explicit disposition, not an invented receipt; save-Tool receipts are not required for this exception. Nonblocking Concerns require an explicit justified disposition and must not be silently discarded.
