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
version: 19
updated_at: "2026-10-05 23:35:01 +0000"
relations: {}
---
# Summary

Harvest and implement session-derived operations

## Objective

Deliver the Operator-selected minimal Workflow set below: authoritative methodology Operations, reviewed PROGRAMMATIC/PROMPTS RMED, working implementations, and functional Docker/MCP execution. Reuse existing Actions, Tools, prompts and runtime infrastructure where they meet the selected behavior.

### Current Operator-selected scope

The Operator selected these sixteen Workflows:

1. Create Atom.
2. Update Atom.
3. Replace Atom.
4. Change Atom Status for any Atom and Content Role, including Archive as a shortcut rather than a duplicate Workflow.
5. Create Scope Unit.
6. Rename Scope Unit.
7. Move Scope Unit.
8. Remove Scope Unit.
9. Implementation Workflow.
10. Revert Changes.
11. Build Entities Graph.
12. Build Terms Graph.
13. Build Applicable Methodology.
14. Find and Fetch Artifacts (Markdown carriers).
15. Find and Fetch Journal Events.
16. Release Version, including project-local ca Skill installation without hooks.

The three Projection Workflows support rebuilding from current authoritative sources. A generic Rebuild Projections entrypoint may route to them; it is not an additional independent deliverable.

Validation, Relation checks, approval gates, and journaling are required supporting behavior inside these Workflows and their Actions, not additional standalone Workflows. Preserve the current identity rule: an Update that requires a Summary change hands off to Replace; it does not silently update the existing Atom's Summary. Change Status resolves the applicable current status model instead of hardcoding one Content Role's statuses. Scope Unit changes use the authoritative Project Structure and preserve or explicitly report affected references. Revert preserves required history and performs only the approved reversal.

The two query Workflows are read-only:

- Artifact queries filter any Markdown frontmatter property and any heading/section property, including `#`, `##`, and deeper headings. Return Artifact IDs by default; fetch only caller-selected properties/sections, such as Claims, when requested.
- Journal queries filter canonical Event fields. Return Event IDs by default; fetch only caller-selected fields or full Events when requested.
- Both use basic SQL-WHERE-style equality, inequality/NOT, and `IN`, with unambiguous boolean combinations. Return bounded, truthful coverage/pagination and invalid-filter diagnostics; do not evaluate arbitrary SQL/code or infer identities from filenames.
- Preserve the caller's requested property/status selection and do not fetch credentials/secrets or create mutation authority. The canonical Events Journal remains the one source, not independently maintained derived logs.
- Actual admitted Workflow/Action execution uses the single shared Run Journal support. Bind a stable query-source snapshot; the query's own execution records must not mutate or enlarge that captured result set. Preview is non-dispatching, and Run records must describe only actual execution.

### Change Atom Status coverage

The existing selected Change Atom Status Workflow applies to any Atom and every declared Content Role, using the current applicable status whitelist and defined folder mapping. It is not an Archive-only capability and adds no separate Workflow.

- Input: an Atom reference and the requested Status. Include Draft carriers according to the current identity rules.
- Resolve the applicable Status model for the Atom's actual Content Role and specialized Type, when present, from existing authoritative methodology. Use its admitted statuses and defined Carrier folders; caller-supplied values do not create new Status authority.
- Validate the requested Status. For the same Status, return a successful no-op without changing Atom bytes or placement. For a permitted change, update the complete Carrier and required metadata, and move it to the defined destination; create the destination folder when the Delivery rules permit it.
- Preserve identity, required Revision history and source information. Report invalid or missing models, undefined statuses or folder mappings, destination collisions and affected active references truthfully. Keep Archive as a shortcut through this same Workflow.
- Use the existing Workflow/Action shared Run Journal path for actual execution, including success, no-op and failure. Verify all declared Content Roles and their admitted statuses, not only the current Requirement fixture.

CA-P-1612 owns the bounded gap-closing decomposition below. Reuse CA-O-127/129/128 and the current generic status Action; extend source resolution and proof where needed rather than authoring another Workflow, Tool or independent status registry.

### Release Version

The Operator selected this additional release path:

1. Bind the selected next Version, exact source revision and release notes.
2. Deliver a full Methodology source copy to root `101_LAYER_1_FRAMEWORK_METHODOLOGY/sources`.
3. Compile Applicable Methodology from those sources. Bind the compiled package delivery and the Methodology consumed under `.caprmedio_caprmedio/000_CAPRMEDIO_framework` to the same accepted source and Version. Preserve the upstream authoring sources; installed copies do not independently redefine authority.
4. Run the full declared test suite and retain its result. Failed or incomplete required gates prevent release promotion.
5. Install the full declared Framework package into `.caprmedio_runtime`, including Methodology, Engine, Tools, applications, MCP, Skills and their required packaged resources; it is not only an Engine installation.
6. Install the project-local `ca` Skill without hooks, using the reviewed project-local client target. Preserve unrelated Skills, settings, authoring sources and Journals.
7. Rebuild the Docker image for the selected Version, then verify the actual installed package, MCP and new image. Source/mock tests and image build alone do not prove this gate.
8. Only after successful verification, retire the exact prior image when no container or required rollback reference needs it. No broad pruning or forced image removal.

The first working vertical cut establishes a frozen Version N that builds and tests N+1. A release Run binds the executing N implementation and Methodology separately from the candidate N+1 sources/package. Changes being built do not silently redefine the running Workflow. Promote the candidate only after its required gates pass; retain N as the working runtime and rollback point until then.

CA-P-1620 owns source-first authoring/review, test-first implementation and actual-release verification. The admitted sixteen-route successor is published and observed; earlier fifteen-route evidence remains historical proof of its bound predecessor only. Dispatch still requires fresh exact source admission and the actual runtime gates. This Plan does not itself execute a release or delete an image.

### Run journaling

Every Workflow Run and every Action Run must be journaled, including standalone Actions, nested invocation lineage, failed or canceled Runs, and successful no-op outcomes. Retain the Run identifiers, governing definition, parent Run/Step references where applicable, input references, start, terminal outcome, results, and actual change/evidence references. Do not put secrets in the Journal.

Use the authoritative Events Journal as the single event source; Artifact Change Log and Process Execution Log are derived views, not independently maintained competing Journals. Journal failures must be reported truthfully; an unpersisted event or Run is never claimed journaled or complete. Functional verification must prove both Workflow-level and Action-level records, failure paths, lineage, and reconstructable results.

Canonical Journal carriers use the single Project-local `.caprmedio_<project name>/_journal/` root. Canonical persisted Projection carriers use `.caprmedio_<project name>/_projection/` by default, including graphs and derived log views. Applicable Methodology is the Operator-selected exception: retain its canonical Atom Projection role folders at `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/`, beside the unchanged `000_APPLICABLE_MTHD_sources/` source folder. Its previously proposed move into `_projection/APPLICABLE_METHODOLOGY/` is withdrawn. The extra untracked copy is not another canonical authority and remains untouched pending scoped reconciliation. Release Version also delivers source/compiled package copies at the Operator-selected release/runtime destinations; these remain bound derived deliveries, not competing authoring or Journal authority. Runtime locks, receipts, pending recording and disposable stages remain ephemeral runtime state. Preserve historical event bytes and sealed recovery context during relocation; do not create duplicate canonical Journal or Projection authority.

### Projection behavior

- Build Entities Graph from current authoritative Entity declarations and properties, including the declared Project Structure where applicable; retain source traceability.
- Build Terms Graph from current authoritative Term declarations and their own Relation Types; retain source traceability.
- Build Applicable Methodology from the selected Core Meta-Model, installed Extensions, and Project Configuration. Preserve original Atom relations, detect conflicts, and require Operator approval before source corrections.
- All three outputs are derived Projections, not new sources of truth. Rebuilding them does not silently rewrite source authority. Report incomplete coverage, source conflicts, and stale or inaccessible inputs rather than claiming a complete Projection.

### Scope amendment and retained history

This explicit Operator scope replaces the former requirement to implement every adopted harvest capability and container-test every unrelated existing Tool. Required Docker coverage now includes all sixteen selected Workflows and the Actions, Tools, prompts, MCP paths and runtime infrastructure they actually use, including reused implementations. It is not satisfied by an image build alone.

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

Authoring disposition: the earlier Plan files retain their independent reviews. Newly added or amended branches require their own saved pre-execution review; creation alone does not prove review or execution. The Operator explicitly authorizes mechanical Git commits for this Epic without the save Tool; if Git cannot commit, skip that commit, retain the unfinished save disposition, and continue independent ready work. CA-C-292 remains an active save-Tool defect, but repairing it is not a prerequisite for this authorized Git path. Record actual commit results without claiming Tool-generated Journal provenance. The stricter body-layout disposition for source conflict CA-C-290 is nonblocking for this Epic's preparation.

- CA-P-1118: Canceled harvest stage; retained completed evidence supplies the following stage.
- CA-P-1119: Bind, author or reuse, and independently review the original thirteen selected source Workflows and their required Actions.
- CA-P-1120: Specify and independently review their PROGRAMMATIC capabilities, including all-Run journaling and Projection construction.
- CA-P-1121: Specify and independently review only the PROMPTS capabilities required by these Workflows.
- CA-P-1122: Implement and functionally verify the selected capabilities from reviewed RMED.
- CA-P-1123: Verify all selected execution paths in Docker, including MCP and reused dependencies.
- CA-P-1124: Verify the sixteen-Workflow coverage matrix, Run Journal evidence and traceability, then close the Epic.
- CA-P-1520: Deliver the two additional read-only query Workflows: source O/RMED authoring and independent reviews, test-first Tool implementation, discovery/MCP/orchestrator/shared-Journal integration, fresh-image E2E, and independent closure review.
- CA-P-1612: Complete the existing Change Atom Status capability for every Content Role using current status/folder authority, then prove the resolved model and execution behavior independently.
- CA-P-1620: Deliver Release Version from independently reviewed source/RMED, including complete Methodology/runtime-package/project-Skill installation and actual new-image verification before exact old-image retirement.
- CA-P-1655: Final code review against the current applicable RMED and Operations, covering all sixteen selected Workflows and their used implementation paths; this review blocks CA-P-1124 and Epic closure.

The original six composite stages retain the original thirteen-Workflow execution branch; CA-P-1520 is a separately governed required composite for the two additions. Existing bounded preflights bind work to their selected Workflows, not to an open-ended harvest inventory. Create only necessary <=15-minute authoring, review, implementation or verification leaves; preparation does not count as implementing a Workflow. The two new source packets are saved but their initial reviews rejected them. Repairs and current independent acceptance, rather than file presence or completed rejected reviews, gate dependent implementation.

### Execution controls

- Each task/subtask has exactly one Plan Markdown file. A composite owns its same-stem directory of child files; the Epic's folder has its mandatory same-stem governing file beside it.
- Each executable leaf has one assigned AI Agent and a work estimate of <=15 minutes. Before execution bind exact input evidence, governing revisions, target files, required result, functional verification and any decision disposition. If the estimate exceeds fifteen minutes, decompose further before execution; never silently expand a leaf.
- After every completed task/subtask, review actual results and current authority, then update every affected next dependent Plan before it executes. Add BLOCKS edges for new remainder/repair/re-review leaves; navigation order is not a dependency. A composite cannot be Done until all required child/remainder work is Done.
- Complete this Epic autonomously through its required implementation, verification and final review. When uncertain, check the active Operator Goal, Project Principles and current authority, choose the best authorized in-scope option, and create a C/Question recording the uncertainty, considered options, selected choice and reason. Continue without waiting for an Operator answer; uncertainty alone is not a reason to stop or leave required work unfinished. Inherit the 90% confidence threshold for recording uncertainty, not as a request-to-pause gate. Actual permission, runtime, evidence or authority blockers still postpone only the affected work and never justify a bypass or false completion.
- Every issue encountered becomes one appropriately typed Concern at its narrowest owning Scope Unit: Problem for blockers/failures, Question for unresolved choices, Conflict for incompatible governing claims. The Concern owns concern_about to the directly affected task/entity and records evidence, impact and disposition. Do not substitute ephemeral chat notes for C atoms.
- On permission/runtime/evidence blockers, create a C/Problem, retain truthful unfinished task state and frontier, postpone the task and execute another independent ready task. Do not bypass its BLOCKS prerequisites, permission denial, or missing authority.
- Prefer functional, integration, E2E and canary verification. Use unit tests only where they add necessary isolated proof; do not couple acceptance to implementation structure.
- Preserve unrelated changes. Use mechanical Git commits for this Epic's changes under the Operator's explicit exception; do not invoke COMMIT_CHANGE_SET or make its repair a prerequisite. If Git cannot commit, skip that commit and retain a truthful save frontier. Retain required execution Journal evidence and append-only history; do not fabricate save-Tool receipts.

## Details

### Current execution frontier

### First working release cut

The Operator directed cutting or postponing work to reach a first working release. Keep the required Unit, candidate-image/canary, Docker/MCP, Full Gate and Journal proofs. Postpone automatic prior-image retirement, expanded crash/restart recovery testing, the broad all-sixteen audit and additional edge-case expansion. Retain N as rollback and preserve the existing later cleanup/recovery capabilities. A first-release caller may stop after verified promotion; an unexecuted retirement Step is deferred, not retired or completed. The deferred work and full Epic closure remain unfinished.

Newest local evidence: 7874fc864 saves the private Candidate E2E gate and byte-backed golden tests. Its complete module passed 11/11 after retained failed/malformed/empty JUnit was fixed; narrow D582#10 review accepted that final repair. Unit partition/driver/admission tests subsequently passed 20/20, and the Full Gate's seven focused tests passed. Consumer/source-admission integration remains under verification. Docker now connects from this session to Engine 29.8.2; the earlier denied/unavailable socket observations below are historical. Read-only first-N preparation finds a conflict-free current source assessment but a stale canonical compiled tree: 77 missing, five extra and 958 changed output carriers. No current N, project-local Skill, real candidate image, installation, promotion or image removal is claimed by this local evidence.

The latest continuation saves the bootstrap proof implementation in b790a3fd0 after independent compiler/bootstrap source acceptance and a combined 50-case run (32.933 seconds). P1732-P1738 are Done for this local slice; P1739 and parent P1714 remain Active for actual compilation/image/install/Skill/Journal proof. The fresh direct Docker CLI probe still returns socket permission denied; no image or runtime publication is claimed.

The Operator approved the separate bounded host E2E executor. Its RMED, private-driver grammar and configurable defaults are accepted in c450b1b45; C476@2 records approval and unfinished implementation. P1740 with children P1741-P1749 owns the bounded executor, sealed Harness bindings, phase map, consumer/admission integration and independent local acceptance; P1744/P1745 are now decomposed further into P1750-P1754. Existing Suite RMED phase amendments are accepted in 7d14bebd9. P1743 is Done and C477 resolved; the independently accepted Operations graph and original full predecessor archives are saved in 1c159f18d. Root saved the bounded proof/task frontier in ebacdd1ee and the context/Driver/Harness/phase-map code in 5e0dfee93 after independent source acceptance. Root's actual verification passed 24 combined context/Driver/phase-map cases, five Runtime image-binding cases and two actual MCP transport cases. C479/C480 are resolved for strict context admission and duplicate testcase refusal. The private gate's capability/settings/predecessor repairs have bounded static acceptance but still need expanded golden behavior and explicit D582#10 Harness metadata; C478 remains Active. Canonical Methodology is still stale and Docker access remains denied even after the Operator recreated its socket. Actual full-suite execution, source-frontier rebind, first-runtime installation and promotion remain mandatory. These newest facts supersede older development snapshots below, not their actual historical events.

The Operator temporarily deferred queue item #5: the final all-sixteen-Workflow code-versus-RMED/O review, coverage audit and Epic closure. CA-P-1655 and CA-P-1124 remain unfinished and are not being executed now. Continue the source-admission, manifest-publication, recovery integration, first-runtime installation and actual runtime-test work; their necessary local checks remain in scope. This deferral is neither a waiver of final acceptance nor permission to mark the Epic Done.

The latest 2026-10-05 continuation supersedes the older snapshots below. P1715 is Done: c1a4749e2 actually published and independently observed the source-admitted sixteen-route successor, with completed canonical Event journal:release-manifest:81cf4fac9b9087e14d451502fa1be473c664eea1f7f4b74e1032ba1b084449a7. Physical Carrier SHA-256 is 1eabfd2f1a0df45ae0df2ff4b2221ebe557ef1f520a990ef6d10f542259d6723; the canonical digest is 48a03709ba64113b007893bf92886be447a57be1ce5b324056c8f18eab7854e7. Durable recovery, source admission and immutable-suite executor development are saved in 88e6546d8. Earlier focused recovery/provider and source-admission results are not actual Docker Release acceptance.

The Operator stopped PID 61257. Root then started a host worker that emitted structured v5 readiness and subsequently stopped only that owned foreground worker cleanly after code changed. The old v3 Base Revise Run remains ENQUEUED and was not replayed or migrated. Actual Docker compiler Run release-methodology-reconcile-20261005-1805 reached its first Action but ended interrupted_pending without effects: frozen host compiler parameters did not match /project. Its six canonical Workflow/Step/Action Journal records are saved in 877a669bf. Local trusted-root repair 684b87f0e passes four focused tests, but the Docker worker has not loaded it. A new freshly admitted Run is required after an authorized runtime rebuild/restart and source reassessment; scheduler SUCCESS is not Workflow success.

P1722-P1726 and P1727-P1731 are Done for the bounded complete-suite driver, private current-control context, focused tests and independent integration review. Their accepted source packet is saved in b7d44ccfa and implementation in 689dd212f. The fixed CLI, exact schema-2 envelope and actual per-case reports preserve the candidate-inventory and sixteen-route contracts. Twelve golden driver tests and 34 context/timing/checkpoint/handoff/executor/retained-image tests pass. Seventeen intentional fixture payloads no longer match real-test discovery; no production exclusion was added. C475 is resolved for that bounded design/implementation, not for actual full-suite execution.

P1714 and P1717/P1721 remain Active. A complete Framework N selector/package and project-local ca Skill are still absent, and canonical Applicable Methodology remains stale. First-N source authoring is being repaired to require compiler-current canonical output and actual complete-package bootstrap-image build/inspect/canary proof; matching labels alone are insufficient. C476 records another source-confirmed prerequisite: the three mandatory Docker E2E modules cannot execute inside the existing closed, read-only, network-disabled suite environment. Their skips are non-passing. A separately governed E2E-capable gate needs accepted RMED before implementation; no host Docker socket mount, hidden exclusion or permission relaxation is authorized by this Plan.

The Operator directed retaining test fixture directories, so cleanup alone is not a blocker. Direct Docker socket access and isolated Release atomic directory publication remain denied. No actual complete-runtime installation, Skill activation, new image, image removal or Release promotion is claimed. These external gates and the deferred final audit remain open; current development evidence does not close them.

The following paragraphs are historical snapshots, not newer completion assertions.

Latest bounded result: f2ba6c494 resolves the image override review finding with a shared strict immutable-ID resolver; independent review accepts it and root reruns five pure cases. Root also reruns four guarded-registration and two hook-payload cases, plus three existing pure provider serialization cases. Suite candidate-binding/N-carrier and private provider/retirement repairs remain working-tree code with fixture verification pending, not accepted complete implementation. Recovery review established that saved native results omit preflight/type identity; no unsafe rehydrator was created. A typed closed checkpoint in the existing shared progress path is required before restart continuation. Directory-cleanup C449 remains the real test blocker; no canonical manifest, installed runtime, Skill or Docker image was changed by this continuation.

Parallel continuation saved 194dee472 (truthful task/environment frontier), 85a80d698 (explicit Methodology delivery destination), 3eec8cffb (guarded Release registration, four pure tests) and 28f5e572c (hook-free ca payload admission, two pure tests). d7e1c53de preserved explicit image selection with four pure tests, but independent review found arbitrary tag overrides too broad; a strict immutable-ID repair is in progress. The live canonical manifest is still fifteen routes, and no image was built, promoted or retired. Provider effect-reference and retirement-outcome repairs remain saved but fixture-unverified. Suite candidate/N-preservation and typed recovery prerequisites are still being implemented. Public effect-free Release refusal is intentional under D560/D572 until successor admission, not itself an authority conflict.

The latest am-default probes permit Docker inventory and temporary-file removal, but deny temporary-directory removal. The Operator directed leaving the empty probe untouched. C449 remains Active for fixture cleanup; no tests are weakened or relabelled passing. Ten independent subagents now continue bounded Release implementation and source/code reviews in parallel. P1712's three fixture-root changes pass independent static review without weakening production checks or cleanup; runtime verification remains pending.

The latest Operator input retains Applicable Methodology at its original framework location. D550@3, D326@15 and the five Project Structure delivery bindings now express that exception; compiler path support and all40 focused compiler/selected/expansion tests pass, saved in 2cebdbabd. Project Settings join the freshness snapshot; explicit Release child output is preserved. C447's denied move is withdrawn rather than executed or bypassed. Historical migration evidence remains unchanged, and legacy-manifest accounting remains separate.

Docker API access and the declared host dependency environment now work. C449@3 records the current remaining filesystem blocker: Release fixture directory cleanup raises EPERM. P1710 saves sixteen focused provider tests, with three pure boundary cases passing; the fixture-based run is not a pass. P1712 corrects macOS /tmp versus /private/tmp normalization and adds a root-equality regression; static checks pass, but fixture verification is still blocked. Capacity interruption C468 is cleared by a normal subagent return, not by a model override. All source/mock, private-provider and static review results remain distinct from fresh-image, shared Journal, durable restart and actual sixteenth-route acceptance.

P1711 independently accepts the pinned exact-image-retirement delta at96% with no blocking code finding. Its review does not rerun or relabel previous mock tests. Durable same-intent recording reconciliation, current host regressions, real image proof and complete Release dispatch remain unfinished. The deleted057792 image is not usable evidence; P1600-P1604 require a newly bound immutable image before execution.

Current checkpoint supersedes every earlier snapshot: the autonomous rule is in force, with chosen uncertainties recorded as C466/C467 rather than Operator questions. P1699 independently accepts the Draft Update repair98%; P1685/P1677/P1662/P1637 and current P1638 development review are Done, and C460 is resolved. Exact owned staged native code passes23 cases without including external legacy-migration changes. P1698, P1693 and P1700 complete retained image verification, actual disposable selector/Skill promotion recovery and the strict effect-free Tool boundary; they do not prove a real Release.

P1701 composes all ten Release phases with14 focused tests. P1702 removes the suite's hidden installation prerequisite with21 suite cases and37 image/14 promotion regressions; fresh suite execution precedes O175 staging without hidden package/Skill creation, resolving C467. C466's approved retention source is now D573@2, independently accepted99% after the successful-evidence ambiguity repair. P1706/P1709 bind and independently accept D572@4/P1622's exact amended frontier at98%, with21 RMED/38 unique source pins and15 admission tests; the production fifteen-route manifest remains untouched. P1707 implements conditional exact retirement and P1708 shared native provider integration in parallel. Public sixteenth registration, durable restart/recording recovery, final code-versus-RMED/O review and actual full-suite/new-image/queue/MCP Release gates remain required. C447/C449 are unchanged permission/evidence boundaries, not bypassed. The Epic remains Active.

Current autonomous continuation supersedes the snapshots below: P1690 repaired atomic history consumption and missing-Draft recovery; P1683/P1684/P1690 are Done after independent acceptance at97%. P1694 finishes head-first native promotion retry with eight promotion and fourteen status cases passing; independent P1638 still rejects Draft Update accepting an unrelated retained head, and P1699 now owns that pre-write repair. P1685 and its native integration parents remain Active until that current finding is fixed and reviewed.

Release preparatory implementation now includes full source delivery, bound full-suite execution, shared persistent source inventory, exact image-input sealing, image build/canary evidence, additive source admission and loader validation. P1698 adds selector-independent retained image-artifact verification with twenty-five mock-image cases passing. P1693 is integrating that reader into observed Framework/Skill promotion and recovery; P1697 exact prior-image retirement follows it. Native Release entrypoint/providers, sixteenth public registration and real full-suite/new-image/MCP/queue Release proof remain required. Local tests and mock image evidence are not full Release acceptance. C447/C449 boundaries remain unchanged.

Latest verified frontier supersedes the older snapshots below. The Operator requires autonomous completion: choose the best authorized in-scope option, record uncertainty in C/Question, and continue without waiting; genuine permission/evidence boundaries still cannot be bypassed. Source-derived qualified status resolution and the eight shared source-driven cases are accepted. D446@7 binds same-Atom demotion by removing its own identifier. P1638 rejected two Draft-origin substitutions not covered by earlier passing cases. P1675/P1676/P1681 complete independently accepted D568@5/D570@4/D569@5 target-bound history and non-consuming pending finalization. P1683/P1684's thirteen focused passes were followed by independent REJECT at98%: concurrent finalizers duplicated consumption and terminal recovery failed after Draft removal. Those two Tasks are reopened; C462/P1690 own the bounded repair. P1685's Create/Update/demotion wiring is partial until supported pending lookup and exact native retry are complete. P1637/P1662/P1677 remain Active. C459 records the chosen design, C460 the original native gap. P1647 remains Done for independent shared-status scope; current W01-W04 pins are rebound, other routes unchanged.

Release source authoring P1621/P1627-P1629 and corrected P1622 acceptance are complete. P1650/P1672 independently accept the actual compiler frontier separately from the canonical-tree digest; P1680 proves real compiler-to-stager propagation. P1673/P1674/P1679/P1682 complete the repaired additive source packet: D572@3 owns the closed complete pin record; R1847@7 delegates it; O164/O165/O166/O173@2 preserve child-only materialization. Final source review accepts at99%. P1686's twelve full-copy/refusal/recovery cases and compiler/pipeline regressions pass. P1687 implements additive admission validation and P1688 the bound suite phase in parallel with lifecycle wiring. Native Release providers/registration, full-suite, installation, fresh-image and actual Release execution remain unfinished. C447 denied Projection relocation and C449 immutable-image/MCP runtime proof remain genuine gates. No release promotion, project Skill replacement, image retirement or denied-operation bypass has occurred.

P1605 diagnosed a stale live discovery generation and absent query discovery bindings; P1607/P1609 repaired explicit bindings and registry-derived availability. Live reload changed generation from 1be08a172092c071a5412fb0958dba3a2cacf353276618cb644a2a4ed350c04f to 677e2f34b80b3f6aa3637dcedea7cd0b8af05b633666fdfe2ec632c5d0d727b6. Actual MCP discovery now returns both query Tools as MCP-available, 49 diagnostics and no projected CA-O-159/162 ambiguity. Client schema refresh remains unconfirmed; this is not fresh-image execution. P1608's independent source acceptance repairs the query test's Projection-write blind spot. Subsequent Engine changes are not included in P1596's earlier immutable image.

P1610 corrected native Artifact query/shared Run authority; P1611 rejected its inherited snapshot-before-Run statement. P1617 repaired O158@4 and independent P1618 accepted the current exact eight-source frontier in 88405e40e. Independently accepted P1619 rebound W14 to P1618@1/O158@4 in 4d1b6d254, preserving the other fourteen routes, W15 admission and registry. Eight focused development-worker tests passed in 14.8 seconds, including rejection of rehashed old P1532 with current O158. This is source/development admission, not immutable-image, queue or client-schema acceptance; C449/P1604 retain those separate gates. The earlier native fifteen-route acceptance remains historical evidence for its bound bytes, not a current revised-source dispatch claim. Live discovery is resolved separately as C450.

 P1589 now accepts all fifteen selected native contracts in the development worker: the strict W01-W08/W11-W15 suite passed, W09 passed 3/3 and W10 passed 2/2. The proofs include actual native effects, frozen inputs, graph/progress consistency and per-Run shared Journal lineage. W09 is explicitly mock-not-live-llm. Native success is not immutable-image, MCP or queue-process acceptance.

P1566's rejected Revert candidate is retained separately from the accepted P1574/P1581 repair and P1584 actual native route proof; C446 is resolved. P1567 caches stable approved carriers, supplies a valid pre-Run Journal directory and uses explicit container-visible paths before preview. P1576/P1586 bind structural cutover to actual sealed predecessor receipts. P1592 finalizes W13 derived progress only after actual recording; the raw native pending_recording result remains truthful. P1588 accepts P1591's trusted-root workspace overlap guard. P1597 accepts explicit bounded Docker mock injection without widening mounts or changing the live default. No old harvest resumes.

P1547 accepts both native query Tools and the sole parser after repaired adversarial snapshots and truthful consumption diagnostics; P1525/P1526 are Done for native Tool scope. P1543 accepts the fifteen-route MCP source, and P1552 accepts D521@5's exact two-frontier admission. Neither source registration nor core tests count as runtime/image proof.

P1596 built fresh immutable image sha256:057792974dc2d81f84f99dee5535a44d5ee30513b03f6154381d99aa0bd558cd from unchanged Engine context 811cfd014de92cc407cb1ae825d4054a30eb7407274d26b8098ae149bceed063. P1593's harness retains the verified MCP 2.3 API, fresh connections, exact structured output and strict W01-W15/J01-J08 gates. The image build is not functional proof. P1600-W01-W05, P1601-W06-W10, P1602-W11-W15 and P1603 safety cases remain unexecuted: the host test environment is unusable and declared dependency provisioning hit filesystem rename EPERM. C449 preserves this new blocker; no permission bypass or stale-worker substitution occurred. P1604's query-specific actual-MCP remainder remains Active. P1594/P1595/P1598/P1599 record focused native, filter and consumer coverage without closing P1527/P1528/P1529.

Carrier cutover is partial, not complete: 102 registered historical view Projections moved in 615b49250 with 55,288,394 byte-identical predecessor bytes, and P1556 saves the durable map. The first Applicable Methodology role-directory move was denied EPERM. Project C447/P1549 retain that blocked remainder; C443 is now the separate PROGRAMMATIC legacy-consumer issue. No retry, alternative move, rebasing or rollback occurred. All 963 original source links remain valid and the distinct legacy Engine manifest remains untouched. The earlier 337-file Journal byte-preserving cutover remains verified. Independent ready implementation continues while denied work remains unfinished.

The following paragraphs are retained historical frontier snapshots, not current completion assertions.

Centralized carrier cutover: CA-D-549/CA-D-550 establish `_journal/` and `_projection/`. The earlier directory rename was denied and was not bypassed. Current readback now finds `_journal/` and no old `work_journal/`; root compared all 337 tracked historical Journal files against their Git predecessor bytes and verified all 337 identical, with no missing or changed files. The canonical MCP manifest exists in `_projection/` and its original-thirteen current source pins loaded successfully. Remaining cutover: persisted graph/signature outputs and Applicable Methodology carriers still use old physical locations; relocate only the registered derived outputs and rebase their source references before whole-cutover/image acceptance. Source authority stays in the framework folder and runtime locks/receipts/pending records stay ephemeral. This readback is not a claim that all persisted Projections are migrated.

The original thirteen-capability implementation branch is unchanged. Required source definitions and independent source reviews are complete for those thirteen; P1119/P1132 are physically Done for that scope. No harvesting or broad source audit remains. P1484–1492 supplied eighty-two native PROGRAMMATIC/PROMPTS specification carriers and the original Docker acceptance portfolio. P1493–P1500 reviews and their bounded corrections have been accepted; P1120/P1121 and the initial implementation preflights are Done.

The two query source packets are accepted: P1532 accepts the repaired Artifact packet; P1533 rejected a remaining Journal absence-semantics conflict; P1534 repaired it and P1535 accepted the final Journal source pins. Workers returned both query Tools and the shared filter. Root's combined development-worker suites passed 15 Artifact/filter and 8 Journal tests; P1544 now independently checks their actual contract coverage. Tool code/test counts alone do not close P1525/P1526 or prove shared Run/MCP/image behavior. P1542/P1543 author and independently accept the necessary additive fifteen-route MCP source contract before P1527 integration.

P1510–P1519 bind the test-first implementation packets. P1536 completed Implementation Step-specific input handoff, and P1539 completed native W01–W08 golden inputs with actual disposable-Project adapter effects. P1540's manifest-based repeat visit identities retain one failing real shared-recorder test; P1541 repairs duplicate Workflow definition bindings without weakening the Journal. Implementation Agent startup, governed Revert service startup, compilation approval/correction paths, remaining golden inputs, actual all-route queue/MCP dispatch, and fresh immutable-image execution remain unproven. Original-thirteen implementation continues independently of query source admission. Final coverage and Epic closure require all fifteen Workflows, actual effects and truthful every-Run Journal evidence.

### Definition of Done

CA-P-1655 must finish the final code-versus-RMED/O review with explicit coverage, saved evidence and resolved blocking findings before CA-P-1124 closes this Epic. Passing tests alone do not replace that comparison.

This Epic is not Done until all sixteen selected Workflows have reviewed source definitions, correctly located RMED, implementations and passing functional Docker/MCP evidence for their required execution paths; every Workflow Run and Action Run in the acceptance scenarios has truthful Journal evidence; all three main Projections have passing source-traceability and rebuild evidence; and every required composite/leaf, repair or review is Done with blocking findings resolved. The coverage matrix must identify actual source, implementation, image, Run, Action and result evidence for every selected Workflow, not infer coverage from file presence or a successful image build. The two query Workflows additionally require source-snapshot-stable, read-only query proof, default-ID and selected-fetch proof, invalid-filter/coverage/pagination proof, and a no-credentials/secrets proof. Release Version additionally requires full source copy, accepted compilation, complete runtime package, project-local ca Skill without hooks, full-suite and actual new-image/installation verification, safe exact old-image retirement, and the frozen N-to-N+1 promotion boundary. Preserve required history and source/Projection/Journal/Git provenance under the approved save exception. Operator-excluded harvest work, unrelated additional capability delivery and legacy administrative closure are not required completion and are never falsely reported Done. A skipped commit requires an explicit disposition; nonblocking Concerns retain justified dispositions.
