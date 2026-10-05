---
atom_id: CA-P-1752
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
version: 2
updated_at: "2026-10-05 22:45:36 +0000"
subjects:
  governs: "Candidate E2E Release gate/Bind host E2E capability and reopen execution evidence"
  depends_on: [Implementation, Evaluation, Workflow, Action, Docker Image, Test Suite, Journal]
relations:
  is_decomposition_of: [CA-P-1745]
  blocks: [CA-P-1753]
---
# Summary

Bind host E2E capability and reopen execution evidence

## Objective

Bind the actual executed frozen-N Driver/controller and trusted executables into the canonical E2E receipt. Implement a byte-proof reader for capability, JUnit and output carriers, candidate/image/map/grammar identities and prerequisite receipts. Preserve the confirmed positional-image API with required keyword-only image_build.

## Details

Ownership: RELEASE_VERSION/release_e2e_gate.py; context/Driver only when required by this boundary. Expected execution slice <=15 minutes. Workers share the checkout and preserve edits outside their exclusive scope. Root owns integration and Git. Source/currentness, permission and missing evidence guards remain intact.

## Definition of Done

Independent source review accepts the boundary and the golden tamper/removal/cross-candidate cases prove refusal. Static acceptance alone does not finish behavior verification.

## Pre-execution review

Root selects this bounded decomposition to finish the accepted R1890/M346/E589/D582 contract, not a narrower smoke-test substitute. Existing retained N, public routes, pending Runs and canonical Journal history remain protected.

## Recorded verification

Local implementation acceptance is saved in 7874fc864 and 5e0dfee93. The complete private gate module passed 11/11 tests after bounded failed/malformed/empty JUnit retention was fixed; the affected method also passed independently. Narrow D582#10 review accepted the final branch. Earlier context/Driver/phase-map, Runtime image-binding and actual stdio transport results remain retained. Synthetic image/command observations are mock data, not Docker or Release proof. No full-suite, installation, promotion or retirement result is claimed.
