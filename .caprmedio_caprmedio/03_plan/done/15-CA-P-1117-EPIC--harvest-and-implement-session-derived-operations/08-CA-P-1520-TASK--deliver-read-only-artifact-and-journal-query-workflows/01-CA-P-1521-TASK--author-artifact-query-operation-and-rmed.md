---
atom_id: CA-P-1521
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: "Artifact query source and RMED authoring"
  depends_on: [Operations, Workflow, Action, Tool, Evaluation, Journal]
version: 3
updated_at: "2026-10-05 01:20:00 +0400"
relations:
  is_decomposition_of: [CA-P-1520]
  blocks: [CA-P-1522]
---
# Summary

author artifact query operation and rmed

## Objective

Within <=15 minutes, author only the minimum source packet for Find and Fetch Artifacts: one read-only Workflow, one query Action, required Step(s), and their PROGRAMMATIC RMED/Evaluation/Delivery contract. No code, MCP registration, source harvesting, or source snapshot mutation.

### Exact inputs, outputs, and gate

Inputs are the live Goal/Principles, current active operation/RMED layout, CA-P-1520, the canonical Markdown carrier model, and the shared Run/Journal contract. Outputs are saved, active, uniquely identified O Workflow/Action/Step and RMED carriers in their native authority paths, with source-to-RMED bindings, target Tool path `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/FIND_AND_FETCH_ARTIFACTS/`, and golden-test path `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/FIND_AND_FETCH_ARTIFACTS/tests/test_find_and_fetch_artifacts.py`.

The contract must cover every frontmatter and heading property; literal equality, inequality/NOT, IN, and an unambiguous boolean grammar; default Artifact IDs; caller-selected property/section fetch; bounded pagination/coverage; no Active-only or arbitrary-status/property exclusion; malformed carrier, missing ID, duplicate property/heading, incomplete read, and invalid-filter diagnostics; no filename identity inference, credentials/secrets, arbitrary SQL/code, mutations, fictitious Runs, or snapshot changes. This is the source-authoring packet; its absent outputs block P1522/P1525/P1527 and cannot be assumed bound before it is Done.

### Verification

Statically verify one minimal Workflow/Action route, complete source/RMED references, exact target/test paths, all required negative diagnostics, and `git diff --check`. Archive meaningful predecessor source revisions if the active carrier rules require replacement. Record only actual saved authoring evidence; remain Active until complete.

### Definition of Done

The exact active source/RMED IDs, Versions, and paths are saved with the stated contract and verification; otherwise this authoring packet remains Active and blocks P1522.

## Result

CA-P-1530 supersedes the rejected packet with active source definitions:
CA-O-158@2 Workflow, CA-O-159@2 Action, and CA-O-160@2 Step in
`000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/`.
Saved active RMED: CA-R-1849@2, CA-R-1850@2 (the shared bounded query-filter contract),
CA-M-330@2, CA-E-569@2, and CA-D-551@2 in the respective
`102_LAYER_2_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/`,
`05_method/`, `06_evaluation/`, and `07_delivery/` source paths. The exact
delivery and golden-test paths are bound in CA-D-551@1 and CA-E-569@1.

## Evidence

Static source-authoring verification is limited to saved carrier metadata,
one Workflow/Step/Action route, referenced RMED IDs and paths, and repository
diff hygiene. No Tool, registration, migration, source snapshot, Run, Journal
receipt, or runtime test was created or claimed.
