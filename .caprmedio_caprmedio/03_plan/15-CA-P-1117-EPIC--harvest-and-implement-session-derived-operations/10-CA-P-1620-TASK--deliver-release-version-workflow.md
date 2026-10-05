---
atom_id: CA-P-1620
content_role: Plan
type: Plan
label: Task
work_sequence_number: 10
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
subjects:
  governs: "Deliver Release Version Workflow"
  depends_on: [Workflow, Action, Tool, Methodology, Implementation, Projection, Skill, Journal]
version: 1
updated_at: "2026-10-05 02:09:37 +0000"
relations:
  is_decomposition_of: [CA-P-1117]
  blocks: [CA-P-1123, CA-P-1124]
---
# Summary

Deliver Release Version Workflow

## Objective

Deliver the Operator-requested Release Version capability, reusing the existing compiler, installer, shared executor and Docker infrastructure. This is a composite; its bounded children author and review source, implement, then verify the actual release path.

## Details

The Operator selected full Methodology source delivery to root 101_LAYER_1_FRAMEWORK_METHODOLOGY/sources, then Applicable Methodology compilation and delivery for runtime use under .caprmedio_caprmedio/000_CAPRMEDIO_framework. Install the full declared Framework package into .caprmedio_runtime, including its Methodology, not only Engine binaries. Install the project-local ca Skill without hooks. Run the full declared test suite, rebuild the Docker image, verify the installed package and actual new image, then remove only the exact retired image when unused. Authoritative sources remain the single source of truth; release/runtime copies are derived deliveries, not competing authoring sources.

Bind selected Version/source revision, release notes, package manifest/digests, source and compilation destinations, project-local Skill target, tests, rollback/currentness gates, image/container references and canonical Run Journal/report destinations. Preserve Project settings, framework-instance settings, authoring sources, Journals, unrelated project Skills and rollback state during installation. Keep secrets outside packages/images. Explicit Operator invocation authorizes only the selected release boundary; no autonomous release or force-prune.

Current project_structure.toml still delivers FRAMEWORK_METHODOLOGY to 101_FRAMEWORK_METHODOLOGY. Source authoring must reconcile that binding with the newly selected 101_LAYER_1_FRAMEWORK_METHODOLOGY/sources delivery before implementation; file presence is not authority. Exact compiler output layout is bound by reviewed D before effects, not silently inferred from this Plan.

The existing fifteen-route manifest remains the accepted closed fifteen-route contract until the reviewed additive Release Version source and route admission permit its extension. Do not rewrite historical fifteen-route evidence as proof for this sixteenth capability. C447/C449 remain their existing denied-relocation and host-test-environment blockers; this addition grants no bypass.

The first working vertical cut freezes Version N as the executing Framework/Methodology. That N builds and tests candidate N+1 using separately pinned candidate sources. Installation promotes N+1 only after its required gates pass; N remains the working runtime and rollback point until then. The running release graph and inputs do not silently switch to candidate definitions mid-Run. First-cut release verification must not recursively invoke another release to prove itself.

## Definition of Done

All four required children and their bounded remainders are Done; independently accepted source/RMED and functional current-release evidence cover delivery, compilation, full-suite gates, complete runtime installation, project Skill installation without hooks, actual new image and safe exact old-image retirement. Rollback and failure cases preserve actual effects and truthful shared Run records.

## Planning review

/root/review_combined_query_tools independently ACCEPTED the P1620–P1624 planning packet after the premature global-review assertion was corrected. This is Plan-only progression: no release source, Tool, installation, current image or retirement is accepted by that verdict. The source-authoring stage is decomposed into bounded O, RMED and existing-interface binding children; all three gate the complete-packet source review P1622. The executing N remains frozen while candidate N+1 is built and tested separately.
