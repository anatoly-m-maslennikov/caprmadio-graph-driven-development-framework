---
subject_scope: evaluation
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-META-REQU-183--tests-and-evaluations-remain-distinct
      - CAPRMEDIO-META-REQU-185--separate-test-and-evaluation-proof
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-205--authority-and-evaluation-separation
      - CAPRMEDIO-META-REQU-223--streamlined-content-role-cycle
      - CAPRMEDIO-META-REQU-224--analysis-and-observation-boundary
---

# Requirement — Keep QA Cases mechanism-neutral and evaluation chains distinct

A QA Case is one mechanism-neutral Evaluation atom defining what claim is
checked, the applicable conditions, the acceptance criteria, and the
disposition rule. It does not prescribe whether the check is realized by an
automated test, model-judged evaluation, statistical assessment, rubric,
manual review, or another implementation mechanism.

One QA Case may be realized by multiple distinct evaluation implementations.
One implementation may realize multiple QA Cases only when its result remains
attributable to every covered Case. Coverage is therefore many-to-many but
never implicit.

Deterministic Test implementations and qualitative, probabilistic,
statistical, rubric-based, or model-judged Evaluation implementations retain
distinct chains. Each chain keeps its executable implementation, configuration
or rubric, factual Observation, evidence, and Verification judgment
distinguishable. A shared runner, prompt, judge, report, or gate does not merge
their meanings, observations, or coverage.

Test and Evaluation describe implementation mechanisms, not Evaluation
subtypes. The QA Case remains the Evaluation authority; executable mechanisms
are Implementation, and their results are Observation.

## Rationale

Mechanism-neutral Cases prevent the same evaluation obligation from being
duplicated merely because it has several realizations. Preserving distinct
implementation and observation chains still prevents deterministic correctness
from being collapsed into qualitative judgment.
