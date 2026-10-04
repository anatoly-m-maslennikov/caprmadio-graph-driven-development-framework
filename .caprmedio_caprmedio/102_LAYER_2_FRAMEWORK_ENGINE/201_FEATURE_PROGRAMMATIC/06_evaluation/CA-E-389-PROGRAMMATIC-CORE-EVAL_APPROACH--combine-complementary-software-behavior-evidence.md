---
atom_id: CA-E-389
content_role: Evaluation
type: Evaluation Approach
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Core
global_tier: 6
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "software-evaluation-portfolio-admission"
  depends_on:
    - "programmatic software"
    - "Spec"
    - "Evaluation"
    - "Implementation"
version: 10
updated_at: "2026-10-04 03:52:53 +0400"
relations:
  evaluation_for:
    - CA-M-285
  derived_from:
    - CA-A-053
---
# Summary

Combine complementary software behavior evidence

## Scope

admission of a behavioral software Evaluation portfolio for a PROGRAMMATIC component.

## Claim

given the applicable Spec, declared failure predicates, proposed Evaluation portfolio, **and** replay evidence, accept the portfolio **only when** **every** predicate is covered by **`>=1`** reproducible check at the least costly stable observable boundary established by the evidence; no check makes acceptance depend solely on replaceable private Implementation structure **when** a semantic **or** public behavior boundary can expose the predicate; **every** retained higher-boundary duplicate has an explicit emergent-risk **or** defense-in-depth purpose; **and** an installed end-to-end check is retained **only when** a narrower boundary cannot expose its critical journey **or** emergent failure. reject a portfolio that violates any condition, **and** return unresolved **when** boundary stability, coverage, **or** relative cost cannot be established from the supplied evidence.

## Details

### Inputs and evidence

- identify each failure predicate, the authority that establishes it, the check that exposes it, the observed boundary, replay inputs, expected **and** actual results, runtime, flakiness, maintenance burden, **and** failure-localization evidence.
- classify each check separately by test scope, test purpose, boundary realism, execution environment, **and** release stage. functional testing is a purpose that may occur at multiple scopes; canary evaluation is a release stage rather than another test scope.

### Boundary checks

- admit small semantic checks for pure transformations, invariants, dense edge cases, **and** precise diagnosis. reject assertions that merely mirror private helpers, internal call order, object arrangement, **or** mock choreography **unless** that interaction is itself governed behavior.
- admit focused integration **and** public-interface functional checks for files, Git, subprocesses, packaging, protocols, adapters, **and** other real boundaries. controlled external inputs **or** dependencies may be substituted; the Implementation under evaluation is not substituted for itself.
- admit installed end-to-end checks for critical operator journeys **or** emergent failures that narrower checks cannot expose. end-to-end is not the universal first **or** dominant acceptance boundary.
- remove a duplicate higher-boundary check **when** a cheaper stable check fully exposes the same predicate **unless** retained duplication has recorded emergent-risk **or** defense-in-depth purpose.

### Sufficiency and disposition

- judge sufficiency by failure-predicate coverage **and** portfolio cost rather than fixed test counts, fixed scope ratios, **or** raw coverage percentages. coverage, mutation results, runtime, flakiness, churn, localization cost, **and** escaped defects guide selection but do not independently prove correctness.
- pass with the admitted portfolio identities **and** rationale. fail with the uncovered **or** policy-violating predicates. return unresolved with the exact missing boundary, cost, **or** replay evidence.

## Sources

- [ISO/IEC/IEEE 29119-1:2022 — Software testing — General concepts](https://www.iso.org/obp/ui/#iso:std:iso-iec-ieee:29119:-1:ed-2:v1:en)
- [Trautsch et al. — Are Unit and Integration Test Definitions Still Valid for Modern Java Projects?](https://www.swe.informatik.uni-goettingen.de/publications/are-unit-and-integration-test-definitions-still-valid-modern-java-projects-empirical)
- [Spadini et al. — Mock objects for testing Java systems](https://link.springer.com/article/10.1007/s10664-018-9663-0)
- [Google Testing Blog — How Much Testing is Enough?](https://testing.googleblog.com/2021/06/how-much-testing-is-enough.html)
- [Productive Coverage: Improving the Actionability of Code Coverage](https://research.google/pubs/productive-coverage-improving-the-actionability-of-code-coverage/)
- [CA-M-285-PROGRAMMATIC-CORE-METHOD--select-software-evaluation-techniques-by-failure-mode](../05_method/CA-M-285-PROGRAMMATIC-CORE-METHOD--select-software-evaluation-techniques-by-failure-mode.md)
