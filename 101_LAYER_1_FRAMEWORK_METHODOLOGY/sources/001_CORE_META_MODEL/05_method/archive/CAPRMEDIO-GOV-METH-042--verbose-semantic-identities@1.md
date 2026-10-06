---
artifact_subtype: implementation_decision
subject_scopes:
  - artifact-catalog
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-GOV-METH-041--four-direct-decision-subtypes
      - CAPRMEDIO-GOV-REQU-396--artifact-naming-setting
      - CAPRMEDIO-GOV-REQU-411--subtype-bearing-atomic-filenames
      - CAPRMEDIO-GOV-REQU-412--naming-axis-owns-numbering
---

# Decision — Verbose semantic identities

The four semantic Types remain Decision, Question, Problem, and QA.

Decision uses the direct subtypes `requirement`, `constraint`, `contract`, and
`implementation_decision`. Their ID kinds are `REQUIREMENT`, `CONSTRAINT`,
`CONTRACT`, and `IMPL`. An empty-subtype Decision continues to use `DECISION`.

QA uses the required direct subtypes `test_plan` and `evaluation_plan`. Their
ID kinds are `TEST-CASE` and `EVALUATION-CASE`. A QA atom defines intended proof; Test
code and Evaluation prompts, datasets, fixtures, harnesses, and runners are
Implementation artifacts, while observed results are Evidence Records.

A naming-policy change is one complete governed migration. It updates current
and historical semantic IDs, carrier names, relations, lifecycle targets,
compiled documents, settings, implementation references, proof references,
and generated views together. The previous short tokens do not remain accepted
aliases after cutover. Numeric suffixes are preserved when the migrated
project-wide sequences do not collide.

## Primary claim

DSET uses the canonical semantic ID kinds REQUIREMENT, CONSTRAINT, CONTRACT, IMPL, TEST-CASE, and EVALUATION-CASE; QA atoms are plans rather than executable checks, and adopting this vocabulary requires a complete historical identity migration without retained short aliases.

## Rationale

Verbose identity kinds are understandable from a file list, while Test Case and Evaluation Case preserve the boundary between a QA definition and its executable implementation or evidence. IMPL remains short to keep the implementation kind readable and distinct from the longer authority kinds.
