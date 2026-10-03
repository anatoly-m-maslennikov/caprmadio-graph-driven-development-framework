---
atom_id: CA-O-089
content_role: Operations
type: Action
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Implementation Failure Diagnosis"
  depends_on:
    - "Action"
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Implementation"
    - "Atom/Content Role: Method"
    - "Atom/Content Role: Plan/Type: Plan"
    - "AI Agent"
    - "Operator"
    - "Spec"
version: 1
updated_at: "2026-09-24 01:39:33 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  relates_to:
    - CA-O-020
    - CA-O-021
    - CA-O-024
    - CA-R-1559
    - CA-R-1591
---
# Summary

Diagnose implementation test failures

## Claim

Implementation Failure Diagnosis **means** the Agentic Action that explains failed implementation checks **before** choosing a recovery route.

- inputs: the selected P/Plan item, actual failure output, failing candidate, prepared tests, execution phase, current R/E/D **and** Method bindings, complete relevant inputs, **and** applicable confidence/permission gates.
- inspect the failing assertion, expected behavior, code path, test setup, **and** reproducibility. a failing test alone does **not** prove an implementation defect **or** a missing Method.
- return `expected_initial_failure` **only** **when** a correct prepared test exposes selected behavior **not** implemented yet; retain that test's initial failure evidence. this is normal test-first progress, **not** a failed repair retry **or** a reason **to** invent a corrective Method.
- return `implementation_defect` for incorrect production code **or** `test_implementation_defect` for incorrect executable test code, with evidence, affected work, **and** proposed correction. **every** admitted repair still passes through retry control.
- return `authority_change_required` for incorrect, missing, **or** conflicting governing expected behavior; return `environment_blocker` for unavailable execution prerequisites outside the admitted correction; return `unresolved` **when** evidence **or** confidence is insufficient.
- do **not** modify code, governing Atoms, Status, **or** test expectations. report failures honestly; do **not** relabel an unexplained failure as expected merely **to** proceed.
