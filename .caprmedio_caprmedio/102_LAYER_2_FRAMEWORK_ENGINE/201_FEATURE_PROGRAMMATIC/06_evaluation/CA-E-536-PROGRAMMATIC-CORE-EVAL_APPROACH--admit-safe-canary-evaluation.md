---
atom_id: CA-E-536
content_role: Evaluation
type: Evaluation Approach
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Core
global_tier: 6
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 03:52:53 +0400"
subjects:
  governs: "canary-evaluation-admission"
  depends_on:
    - "programmatic software"
    - "Evaluation"
    - "Implementation"
relations:
  evaluation_for:
    - CA-M-285
  derived_from:
    - CA-A-053
---
# Summary

Admit safe canary evaluation

## Scope

canary Evaluation of a changed PROGRAMMATIC component against a production-like **or** live workload.

## Claim

given a proposed change, canary cohort **or** shadow surface, workload, control, health observations, exposure bound, stop mechanism, **and** rollback evidence, admit canary Evaluation **only when** the cohort **or** shadow surface isolates exposure; the workload is representative of the governed behavior; the control comparison **and** health observations can distinguish regression; exposure is bounded; immediate stop is available; **and** rollback has been tested against the applicable state boundary. reject canary execution **when** any condition fails **and** require dry-run, differential, **or** recoverable-fixture evidence instead. canary evidence supplements rather than replaces required pre-deployment evidence.

## Details

- record the exact change, cohort **or** shadow selector, workload frontier, control, health predicates, maximum exposure, observation window, stop owner, rollback procedure, **and** replayable rollback evidence.
- pass with the admitted bounds **and** remaining risks **only when** all conditions are established before exposure.
- fail with the violated condition **when** isolation, comparison, stopping, **or** rollback is inadequate. return unresolved **when** workload representativeness **or** state recovery cannot be established.

## Sources

- [Google SRE Workbook — Canarying Releases](https://sre.google/workbook/canarying-releases/)
- [Microsoft Azure Well-Architected Framework — Safe deployment practices](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/safe-deployments)
- [CA-M-285-PROGRAMMATIC-CORE-METHOD--select-software-evaluation-techniques-by-failure-mode](../05_method/CA-M-285-PROGRAMMATIC-CORE-METHOD--select-software-evaluation-techniques-by-failure-mode.md)
