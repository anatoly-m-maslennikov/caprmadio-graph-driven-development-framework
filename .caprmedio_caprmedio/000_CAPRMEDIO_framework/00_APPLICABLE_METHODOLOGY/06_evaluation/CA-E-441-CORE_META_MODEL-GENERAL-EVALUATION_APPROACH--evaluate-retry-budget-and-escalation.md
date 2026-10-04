---
version: 13
updated_at: "2026-10-01 21:31:46 +0400"
relations: {"child_of":["CA-E-001"],"evaluation_for":["CA-O-024","CA-O-016","CA-R-1559","CA-M-295"]}
subjects:
  governs: "Implementation Retry Control"
  depends_on:
    - "Operator"
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Implementation"
    - "Atom/Content Role: Plan/Type: Plan/Autonomous Confidence Threshold"
    - "Project"
    - "Implementation Retry Limit"
atom_id: "CA-E-441"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation Approach"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-441-CORE_META_MODEL-GENERAL-EVALUATION_APPROACH--evaluate-retry-budget-and-escalation.md
---
# Summary

Evaluate retry budget **and** escalation

## Scope

the retry-policy Evaluation.

## Claim

the retry-policy Evaluation **must** return `fail` **if** **any** of the following occurs:

- the initial failed Evaluation consumes a retry.
- an automatic retry exceeds the effective Implementation Retry Limit resolved under CA-M-295-CORE_META_MODEL--resolve-implementation-retry-limits-by-source-precedence **and** enforced by CA-O-024-CORE_META_MODEL-ACTION--control-implementation-retries.
- starting a permitted fix-and-evaluate round is **not** counted once, **or** checking its permission again consumes another retry.
- a changed failure set **or** automatic next loop silently resets the budget.
- the last permitted retry fails **without** pausing **and** reporting remaining failures **to** the Operator.
- retrying bypasses a confidence gate, governing-Atom approval rule, **or** additional Operator constraint.
- successful completion under CA-O-016-CORE_META_MODEL-WORKFLOW--implement-evaluations-before-required-behavior still triggers another automatic repair retry.

earlier escalation required by governing authority **must not** be rejected merely because retries remain.

## Details
