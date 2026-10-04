---
atom_id: CA-M-285
content_role: Method
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Core
global_tier: 6
status: Active
author: Anatoly Maslennikov
version: 11
updated_at: "2026-10-04 02:45:43 +0400"
subjects:
  governs: "software-evaluation-selection"
  depends_on:
    - "programmatic software"
    - "Actor"
    - "Spec"
    - "Evaluation"
    - "Implementation"
relations:
  derived_from:
    - CA-A-053
  child_of:
    - CA-M-110
---
# Summary

Select software Evaluation techniques by failure mode

## Scope

selection of behavioral software Evaluation techniques for PROGRAMMATIC components.

## Claim

**to** select behavioral software Evaluation techniques for a PROGRAMMATIC component, the Actor selecting the portfolio **must** take the applicable Spec **and** declared failure predicates as inputs; choose for **each** predicate the least costly stable observable boundary that exposes the failure **without** coupling acceptance **to** replaceable Implementation structure; repeat the selection **until** every predicate has an admitted check **and** every retained duplicate has an explicit emergent-risk **or** defense-in-depth purpose; produce a traceable evaluation portfolio; **and** reject **or** escalate any predicate for which no safe observable boundary can be established.

## Details

1. classify a selected technique on separate axes for test scope, test purpose, boundary realism, execution environment, **and** release stage. functional testing is a purpose that may occur at multiple scopes; canary evaluation is a release stage, **not** another test scope.
2. use small semantic tests for pure transformations, invariants, dense edge cases, **and** precise diagnosis. minimize tests that mirror private helpers, internal call order, object arrangement, **or** mock choreography; retain an interaction assertion **only if** that interaction is itself governed behavior.
3. use focused integration **and** public-interface functional tests for behavior that depends on files, Git, subprocesses, packaging, protocols, adapters, **or** other real boundaries. use controlled real boundaries **when** the boundary is the behavior being checked; mock admitted external dependencies **or** input data, **not** the Implementation under evaluation.
4. reserve installed end-to-end tests for a small set of critical operator journeys **or** emergent failures that a narrower boundary cannot expose. do **not** make an end-to-end test the universal first acceptance boundary.
5. admit canary evaluation **only if** the component has a safe cohort **or** shadow surface, representative workload, control comparison, health observations, bounded exposure, immediate stop, **and** tested rollback. otherwise use dry-run, differential, **or** recoverable-fixture evaluation. canary evidence supplements rather than replaces pre-deployment evidence.
6. use reviewed golden baselines for large deterministic outputs. derive expected outputs **and** observable effects from governing authority; do **not** accept current Implementation output as its own oracle **or** refresh a baseline automatically after failure.
7. remove duplicate higher-boundary checks **when** a cheaper stable boundary fully exposes the same failure, **unless** an explicit emergent risk **or** defense-in-depth purpose requires both.
8. judge sufficiency by covered failure predicates **and** portfolio cost rather than fixed test counts, fixed layer ratios, **or** raw coverage percentages. use changed-code coverage, mutation results, runtime, flakiness, maintenance churn, localization cost, **and** escaped defects as selection evidence, **not** as independent proof of correctness.
9. keep fast syntax, format, lint, type, **and** focused behavioral checks **in** the changed-code gate. keep expensive campaigns outside synchronous Hooks **unless** an admitted measured bound permits them.

## Sources

- [ISO/IEC/IEEE 29119-1:2022 — Software testing — General concepts](https://www.iso.org/obp/ui/#iso:std:iso-iec-ieee:29119:-1:ed-2:v1:en)
- [Trautsch et al. — Are Unit and Integration Test Definitions Still Valid for Modern Java Projects?](https://www.swe.informatik.uni-goettingen.de/publications/are-unit-and-integration-test-definitions-still-valid-modern-java-projects-empirical)
- [Spadini et al. — Mock objects for testing Java systems](https://link.springer.com/article/10.1007/s10664-018-9663-0)
- [Google Testing Blog — How Much Testing is Enough?](https://testing.googleblog.com/2021/06/how-much-testing-is-enough.html)
- [AWS Prescriptive Guidance — Quality by design](https://docs.aws.amazon.com/prescriptive-guidance/latest/hexagonal-architectures/improve-software-quality.html)
- [Google SRE Workbook — Canarying Releases](https://sre.google/workbook/canarying-releases/)
- [Microsoft Azure Well-Architected Framework — Safe deployment practices](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/safe-deployments)
- [Productive Coverage: Improving the Actionability of Code Coverage](https://research.google/pubs/productive-coverage-improving-the-actionability-of-code-coverage/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
