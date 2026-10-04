---
atom_id: CA-O-018
content_role: Operations
type: Action
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Evaluation Implementation"
  depends_on:
    - "Action"
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Method"
    - "Atom/Content Role: Delivery"
    - "Atom/Content Role: Requirement"
    - "Atom/Content Role: Implementation"
version: 6
updated_at: "2026-10-04 03:57:26 +0400"
relations:
  relates_to:
    - CA-O-017
    - CA-O-020
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-018-CORE_META_MODEL-ACTION--implement-evaluations.md
---
# Summary

Implement Evaluations

## Claim

Evaluation Implementation **means** the Agentic Action that prepares **or** reuses the tests for selected implementation work **before** its required behavior is implemented.

- inputs: the selected P/Plan item, active Method Projection, applicable R/E/D authority, current candidate, existing tests, complete test inputs, **and** owned work boundary.
- derive expected behavior from the governing R/E/D, **not** from the current code. apply **all** governing Methods within Delivery boundaries; reuse sufficient existing tests **when** the selected mode permits.
- write positive, negative, boundary, **and** relevant regression cases. preserve the selected test requirements, including real-command end-to-end execution with mock input Atoms **when** required; do **not** mock the implementation being checked.
- make tests runnable **when** prerequisites permit **and** return the exact tests, commands, expected outcomes, authority bindings, **and** any execution blocker. actual execution belongs **to** Implementation Evaluation.
- return `prepared` **or** `blocked`. preparing tests is **not** a passing test result; missing behavior **may** cause an expected initial failure, which still requires diagnosis before feature implementation.

- honor the selection procedure established by applicable Methods **and** the acceptance, priority, **and** disposition rules established by applicable Evaluation authority. prepare the complete admitted portfolio at its selected observable boundaries; no test scope has default priority. preserve issue-driven targeted checks as complementary evidence **without** creating Method Atoms.
