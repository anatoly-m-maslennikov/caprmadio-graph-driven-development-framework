---
atom_id: CA-P-1123
content_role: Plan
type: Plan
label: Task
work_sequence_number: 6
current_scope_unit: caprmedio
claim_target_scope_unit: FRAMEWORK_ENGINE
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: "Session-derived operational capability delivery"
  depends_on:
    - "Operations"
    - "Implementation"
version: 5
updated_at: "2026-10-05 03:11:41 +0000"
relations:
  is_decomposition_of:
    - CA-P-1117
  blocks:
    - CA-P-1655
    - CA-P-1173
    - CA-P-1124
    - CA-P-1147
---
# Summary

Build and verify Docker images for the complete runtime

## Objective

Build and functionally verify Docker images for all sixteen selected Workflows in current CA-P-1117 v13, including Release Version governed by CA-P-1620 and every Action, Tool, prompt, MCP interface and runtime dependency they actually use, including reused implementations. The Operator's scope amendment excludes container-testing unrelated existing Tools and harvested capabilities.

Exercise image-based mutation and no-op paths on controlled mock Projects, the Implementation Workflow, Revert, all three Projection builders, the two read-only query Workflows, and Workflow/Action Journal persistence and recovery. Query proof must cover source-snapshot stability, default Artifact/Event IDs, selected property/section or field/full-Event fetch, pagination/coverage, malformed-carrier/missing-ID/duplicate-heading-or-property/incomplete-read and invalid-filter diagnostics, and no credential/secret return; a query must not create mutation authority. Keep image identity, Run/Action IDs and result evidence. A successful image build or host-only test is insufficient. Runtime Project-data mounts are allowed; undeclared host implementation mounts and baked secrets are not.

### Work decomposition

This is a composite task, not a fifteen-minute executable leaf. Its initial child files partition the work; add more <=15-minute one-file subtasks for remaining evidence, capability slices, reviews or failures. Roll-up effort depends on the frozen inventory. Inherit CA-P-1117 execution controls and its autonomous-confidence threshold; do not copy or override inherited values.

Before marking this task Done, verify full-stage coverage and update the next dependent task(s) from actual results. A blocked child remains unfinished, has a C/Problem, and does not authorize bypassing this parent's gate.

## Details

### Prospective Release Version coverage

This amendment binds CA-P-1117v13 and CA-P-1620v1 under CA-P-1631. Release Version is a sixteenth selected Workflow, not a claim that its source, implementation, installation or image is already accepted. The existing closed fifteen-route manifest remains admitted only for its reviewed scope until separately accepted additive source and route admission permit extension. Do not change that manifest or reinterpret earlier fifteen-route evidence through this Plan.

| Release boundary | Required functional evidence before coverage acceptance |
| --- | --- |
| Selected source and full Methodology delivery | Pin selected Version, source revision/digests, release notes and complete package manifest. Prove the full Methodology source copy at root `101_LAYER_1_FRAMEWORK_METHODOLOGY/sources`, preserving authoring sources. Reconcile the existing Structure delivery binding through reviewed source authority before effects; folder presence does not admit a new binding. |
| Compilation and delivered Methodology | Compile from the pinned copied sources and verify the reviewed compiled-package destination and runtime-consumed Methodology under `.caprmedio_caprmedio/000_CAPRMEDIO_framework` share the same accepted source/Version. Copies remain derived deliveries, not competing authoring or canonical Projection/Journal authority; exact output layout is source-reviewed before effects. |
| Full-suite and complete runtime package | Run the full declared test suite with retained command/environment/result evidence; required failures, incomplete execution or opt-out skips are not passes. Install and verify the complete declared Framework package in `.caprmedio_runtime`, including Methodology, Engine, Tools, applications, MCP, Skills and required packaged resources, not only Engine binaries. Preserve Project/framework-instance settings, authoring sources, Journals and rollback state; keep secrets outside packages/images. |
| Project-local ca Skill | Verify installation at the reviewed project-local client target without hooks. Preserve unrelated project Skills and settings; no user-wide installation, hook, credential or ambient grant is inferred. |
| Current image and installed execution | Rebuild the selected Version's image, retain exact image/context/package/source identities and verify the actual installed package, MCP and new image. Bind all sixteen current selected paths and their Workflow/Action Journal evidence. Source/mock/development-worker tests and image build alone are insufficient; undeclared host implementation mounts/dependencies and stale images cannot supply current proof. |
| Rollback and exact retirement | Prove failure/partial-install/promotion rollback preserves the working runtime, settings, sources, Skills and append-only Journal evidence. After successful package/new-image verification, retire only the pinned prior image when no container or required rollback reference needs it. In-use, unknown or stale retirement targets remain protected with truthful retained/pending results, not a claimed retirement. No force removal or broad pruning. |

The first vertical cut freezes executing Version N's implementation, Methodology, Workflow/Action definitions and admitted inputs separately from candidate N+1's pinned sources/package. N builds and tests N+1; candidate changes do not redefine the running Run or silently substitute definitions. Promote N+1 only after every required gate passes; N remains working runtime and rollback point until then. First-cut verification does not recursively invoke another release to prove itself.

Cover compiler/test/install/Skill/image/retirement failures, invalid permission or changed source/currentness, incomplete effects and rollback, and Journal append failure. Retain actual completed/unattempted effects, safe result references and truthful shared Workflow/Action records; recording recovery does not replay release effects or invent completion.

### Preserved proof and blocked frontier

Earlier fifteen-route source/native evidence, P1596's image build and other retained results remain historical evidence for their exact bound bytes and scope. They are not sixteen-route release proof or proof for later changed sources/Engine context. This amendment runs no tests, installation, release, image build or deletion.

CA-C-447/CA-P-1549's denied Applicable Methodology relocation remains unfinished; preserve completed byte-verified moves and original links without retry, equivalent move, rebasing or permission bypass. CA-C-449 retains the unavailable declared host Docker/MCP test environment and unexecuted actual-image cases. Do not use stale development workers or a built image to bypass either gate. Independently ready work may continue only within its admitted dependencies; full-stage/image acceptance stays blocked until required findings and evidence are resolved.

Exact committed P1123v3 predecessor from `0ca6fcf2b9a4d44a96e3661d0a389dc9a700eff7` is preserved byte-for-byte at `archive/06-CA-P-1123-TASK--build-and-verify-docker-images-for-the-complete-runtime@3.md`; its historical properties are not rewritten. Current Summary, identity, decomposition and BLOCKS remain unchanged and Status remains Active.

### Definition of Done

This Plan is not Done if any of the sixteen selected Workflows or required support/MCP paths is absent from the scoped inventory, lacks passing current-image functional and Workflow/Action Journal evidence, or requires undeclared host implementation code/dependencies. All three Projection builders, Revert, Implementation and both query Workflows retain their actual-runtime gates. Release Version additionally needs independently reviewed source/additive admission, complete source copy and compilation, full declared tests, complete runtime package and project-local ca Skill without hooks, actual installed-package/MCP/new-image proof, failure/rollback and safe exact retirement evidence, and frozen N-to-N+1 promotion. Required verification/review/repair leaves must be Done and C447/C449's required blockers must have truthful resolved dispositions; build-only, skipped, stale-source or fifteen-route historical evidence cannot close this prospective coverage. Unrelated runtime inventory remains excluded.
