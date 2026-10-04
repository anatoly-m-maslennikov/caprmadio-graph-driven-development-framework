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
version: 4
updated_at: "2026-10-04 19:15:16 +0000"
relations: {}
---
# Summary

Harvest and implement session-derived operations

## Objective

Deliver the Operator-selected minimal Workflow set below: authoritative methodology Operations, reviewed PROGRAMMATIC/PROMPTS RMED, working implementations, and functional Docker/MCP execution. Reuse existing Actions, Tools, prompts and runtime infrastructure where they meet the selected behavior.

### Current Operator-selected scope

The Operator narrowed the remaining delivery to these thirteen Workflows:

1. Create Atom.
2. Update Atom.
3. Replace Atom.
4. Change Atom Status, including Archive as a shortcut rather than a duplicate Workflow.
5. Create Scope Unit.
6. Rename Scope Unit.
7. Move Scope Unit.
8. Remove Scope Unit.
9. Implementation Workflow.
10. Revert Changes.
11. Build Entities Graph.
12. Build Terms Graph.
13. Build Applicable Methodology.

The three Projection Workflows support rebuilding from current authoritative sources. A generic Rebuild Projections entrypoint may route to them; it is not a fourteenth independent deliverable.

Validation, Relation checks, approval gates, and journaling are required supporting behavior inside these Workflows and their Actions, not additional standalone Workflows. Preserve the current identity rule: an Update that requires a Summary change hands off to Replace; it does not silently update the existing Atom's Summary. Change Status resolves the applicable current status model instead of hardcoding one Content Role's statuses. Scope Unit changes use the authoritative Project Structure and preserve or explicitly report affected references. Revert preserves required history and performs only the approved reversal.

### Run journaling

Every Workflow Run and every Action Run must be journaled, including standalone Actions, nested invocation lineage, failed or canceled Runs, and successful no-op outcomes. Retain the Run identifiers, governing definition, parent Run/Step references where applicable, input references, start, terminal outcome, results, and actual change/evidence references. Do not put secrets in the Journal.

Use the authoritative Events Journal as the single event source; Artifact Change Log and Process Execution Log are derived views, not independently maintained competing Journals. Journal failures must be reported truthfully; an unpersisted event or Run is never claimed journaled or complete. Functional verification must prove both Workflow-level and Action-level records, failure paths, lineage, and reconstructable results.

### Projection behavior

- Build Entities Graph from current authoritative Entity declarations and properties, including the declared Project Structure where applicable; retain source traceability.
- Build Terms Graph from current authoritative Term declarations and their own Relation Types; retain source traceability.
- Build Applicable Methodology from the selected Core Meta-Model, installed Extensions, and Project Configuration. Preserve original Atom relations, detect conflicts, and require Operator approval before source corrections.
- All three outputs are derived Projections, not new sources of truth. Rebuilding them does not silently rewrite source authority. Report incomplete coverage, source conflicts, and stale or inaccessible inputs rather than claiming a complete Projection.

### Scope amendment and retained history

This explicit Operator scope replaces the former requirement to implement every adopted harvest capability and container-test every unrelated existing Tool. Required Docker coverage now includes all thirteen selected Workflows and the Actions, Tools, prompts, MCP paths and runtime infrastructure they actually use, including reused implementations. It is not satisfied by an image build alone.

Keep the completed harvest, reconciliation, five additional authored Actions, layout repairs and their evidence. They remain available history and reusable sources; they do not create extra delivery obligations. No further harvest or broad reconciliation campaign is required. Existing child Plans must be rebound to this scope before execution; historical or unrelated leaves remain truthfully classified and are excluded from the required decomposition, not reported Done.

CA-P-1131's legacy authoring-bundle closure and CA-C-410's directory-rename failure are outside the required decomposition after this amendment. Their unresolved physical placement is preserved, not bypassed or claimed fixed. Remove their obsolete gates on the newly scoped source review; review of every source actually used by the selected Workflows remains required.

The historical evidence window is [2026-09-04 05:54:15 +0400, 2026-10-04 05:54:15 +0400). Later explicit Operator corrections in this session amend this Plan without shifting that historical cutoff. The latest explicit Operator input overrides earlier input within its authorized scope; Project Principles remain higher authority. Plan creation is not evidence that the harvest or implementations have been executed.

### Operator-closed harvest

The Operator directed: stop harvesting and continue this Epic. The admitted corpus contains 102 completed packets covering 5,463 of 13,011 session records: 4,504 PRIMARY records and 959 worker records. The remaining 7,548 records are outside further harvesting for this Epic. Interrupted CA-P-1325 / CA-A-1043 is preserved as partial evidence and contributes no completed coverage. Context records do not increase coverage.

CA-P-1118 and its unfinished harvest descendants are canceled, not Done. CA-P-1118 is removed from this Epic's required decomposition and its harvest gates are removed. Completed harvest results remain optional evidence for the selected Workflows. The current scope still requires source review, RMED, implementation, scoped functional Docker coverage, Run journaling, and closure evidence.

### Governing inputs and destinations

- Current Operator Goal: create and evolve a working CAPRMEDIO Framework; re-read the live Goal carrier before autonomous decisions.
- Project-local active authority and all active Project Principles first; applicable methodology authority next; engine-local RMED thereafter. Current source revisions, not this summary, govern exact distinctions and tiers.
- Authoritative methodology sources: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources`. Reusable, project-independent Operations belong to `001_CORE_META_MODEL`; caprmedio-specific Operations belong to `003_PROJECT_CONFIGURATION`. Reconciliation must record each adopted Operation's destination before authoring. The applicable-methodology projection is derived and never the authoring authority.
- PROGRAMMATIC authority: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC`; delivery: `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC`.
- PROMPTS authority: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/202_FEATURE_PROMPTS`; delivery: `102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS`.
- R = required implementation outcomes/results; M = construction technique for implementation or tests; E = assurance policy/acceptance/test cases; D = delivery/carriers. Use current active source authority to resolve exact applicability and local tiers.
- Reuse the existing orchestrator, MCP, tools, prompts and Docker packaging baseline where appropriate. Bind each selected Workflow to its current source definition, Actions, implementation and functional evidence; do not invent duplicate Workflows for shared infrastructure.
- Keep valuable extracted decisions, manifest/frontiers, review results and execution evidence in governed Analysis/Plan/Journal carriers with source references. Disposable intermediate packets may live in `.caprmedio_tmp` but cannot be the only retained completion evidence.
- Docker coverage includes every selected Workflow and its actual Action, Tool, prompt, MCP and runtime execution path. Runtime input/project-data mounts and explicitly provided external services/credentials are allowed by their governed contracts; baked secrets, undeclared host implementation mounts and host-only packages are not. Local build/run is in scope; publishing images, deploying services, or changing account authorization requires separate authority.

### Composite task sequence

Authoring disposition: the Plan files have been created and independently reviewed. The Operator explicitly authorizes mechanical Git commits for this Epic without the save Tool; if Git cannot commit, skip that commit, retain the unfinished save disposition, and continue independent ready work. CA-C-292 remains an active save-Tool defect, but repairing it is not a prerequisite for this authorized Git path. Record actual commit results without claiming Tool-generated Journal provenance. The stricter body-layout disposition for source conflict CA-C-290 is nonblocking for this Epic's preparation.

- CA-P-1118: Canceled harvest stage; retained completed evidence supplies the following stage.
- CA-P-1119: Bind, author or reuse, and independently review the thirteen selected source Workflows and their required Actions.
- CA-P-1120: Specify and independently review their PROGRAMMATIC capabilities, including all-Run journaling and Projection construction.
- CA-P-1121: Specify and independently review only the PROMPTS capabilities required by these Workflows.
- CA-P-1122: Implement and functionally verify the selected capabilities from reviewed RMED.
- CA-P-1123: Verify all selected execution paths in Docker, including MCP and reused dependencies.
- CA-P-1124: Verify the thirteen-Workflow coverage matrix, Run Journal evidence and traceability, then close the Epic.

The remaining required decomposition has six composite stages. Existing bounded preflights bind work to the thirteen selected Workflows, not to an open-ended harvest inventory. Reuse or replace their old packet bindings before execution. Create only necessary <=15-minute authoring, review, implementation or verification leaves; preparation does not count as implementing a Workflow.

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

### Current execution frontier

The selected thirteen-capability scope is unchanged. Required source definitions and independent source reviews are complete; P1119/P1132 are physically Done. No harvesting or broad source audit remains. P1484–1492 supplied eighty-two native PROGRAMMATIC/PROMPTS specification carriers and the exact Docker acceptance portfolio. Eight independent RMED review leaves P1493–P1500 found bounded corrections; graph/PROMPTS contracts passed first, and shared Run support, lifecycle, structure and Revert passed focused correction re-acceptance. Compiler compatibility and MCP mode/full-frontier bindings are the last narrow current specification corrections under P1504/P1506.

P1510–P1519 now bind the actual test-first implementation packets: shared sealed Run/Journal support, lifecycle, authoritative structure, Revert, Entity/Term graphs, compilation, Implementation prompts/Actions, existing DBOS graph execution, MCP/manifest and the selected Docker golden harness. Dispatch remains gated on the required current RMED acceptance/preflight. Existing baseline code is not proof of these selected deliverables. After the exact last gate closes, execute these independent owned packets in parallel, retain actual golden tests/effects and complete functional Docker/MCP/journaling evidence. No additional source campaign is required.

### Definition of Done

This Epic is not Done until all thirteen selected Workflows have reviewed source definitions, correctly located RMED, implementations and passing functional Docker/MCP evidence for their required execution paths; every Workflow Run and Action Run in the acceptance scenarios has truthful Journal evidence; all three main Projections have passing source-traceability and rebuild evidence; and every required composite/leaf, repair or review is Done with blocking findings resolved. The coverage matrix must identify actual source, implementation, image, Run, Action and result evidence for every selected Workflow, not infer coverage from file presence or a successful image build. Preserve required history and source/Projection/Journal/Git provenance under the approved save exception. Operator-excluded harvest work, additional capability delivery and legacy administrative closure are not required completion and are never falsely reported Done. A skipped commit requires an explicit disposition; nonblocking Concerns retain justified dispositions.
