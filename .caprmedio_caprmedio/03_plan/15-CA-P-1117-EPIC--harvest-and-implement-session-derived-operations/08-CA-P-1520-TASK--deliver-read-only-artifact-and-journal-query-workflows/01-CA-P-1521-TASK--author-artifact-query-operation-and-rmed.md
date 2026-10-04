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
status: Active
subjects:
  governs: "Artifact query source and RMED authoring"
  depends_on: [Operations, Workflow, Action, Tool, Evaluation, Journal]
version: 1
updated_at: "2026-10-05 00:02:29 +0400"
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
