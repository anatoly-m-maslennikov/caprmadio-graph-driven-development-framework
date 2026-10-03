---
cce_version: "cce_1"
cce_form: "method"
subjects:
  governs: "software-evaluation-selection"
  depends_on:
    - "programmatic software"
version: 10
updated_at: "2026-09-24 17:18:07 +0000"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-110"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Select software Evaluation techniques by failure mode

## Claim

select PROGRAMMATIC behavioral Evaluations with end-to-end tests as the first acceptance boundary, a reviewed golden corpus as their repeatable evidence base, **and** targeted complementary tests for discovered issues.

- prepare end-to-end tests **before** implementing the behavior they check. exercise the real public command, interface, **or** installed component boundary; a small explicit prerequisite needed **to** run the test does **not** justify implementing the feature first.
- use a golden corpus of mock inputs, fixtures, controlled external responses, **and** reviewed expected outputs. include valid, invalid, boundary, **and** representative combined cases. mock admitted external dependencies **or** input data, **not** the implementation being checked.
- derive expected outputs **and** observable effects from governing RED authority. do **not** accept current implementation output as its own oracle **or** automatically refresh a golden baseline after a failure.
- use unit, integration, property-based, stateful, mutation, **or** other focused tests **when** they reproduce, isolate, **or** prevent recurrence of an observed issue. preserve the failing case **and** verify the fix with the focused regression **and** relevant end-to-end corpus. additional tests complement, **not** replace, the end-to-end boundary; retain already-required checks.
- select the smallest complementary test set that covers the declared failure modes. keep fast syntax, format, lint, type, **and** focused behavioral checks **in** the changed-code gate; expensive campaigns stay outside synchronous Hooks **unless** an admitted measured bound permits them.
- keep expected results, actual results, failed assertions, diagnosis, fix, relevant inputs, source frontier, test configuration, **and** replay command traceable. these observations are evidence for a separately invoked Method-learning Workflow, **not** new M authority created by the implementation Workflow.
- reject acceptance **when** required coverage is missing, a result is stale **or** unreplayable, **or** a focused passing test masks a failed required end-to-end check.

## Sources

- [Hypothesis documentation](https://hypothesis.readthedocs.io/en/latest/)
- [Mutmut documentation](https://mutmut.readthedocs.io/en/latest/)
- [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12)
- [Syrupy snapshot testing](https://github.com/syrupy-project/syrupy)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
