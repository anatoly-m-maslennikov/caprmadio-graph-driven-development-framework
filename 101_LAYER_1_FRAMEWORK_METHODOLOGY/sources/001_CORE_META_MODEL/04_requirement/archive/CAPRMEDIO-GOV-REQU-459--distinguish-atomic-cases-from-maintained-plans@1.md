---
subject_scopes:
  - evaluation
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-225--distinct-test-and-evaluation-chains
      - CAPRMEDIO-GOV-REQU-456--separate-route-catalog-and-project-whitelist
---

# Requirement — Distinguish atomic cases from maintained plans

A **Test Case** is one atomic deterministic check definition with exact
conditions and a pass/fail disposition.

An **Evaluation Case** is one atomic qualitative, probabilistic, statistical,
or model-judged assessment definition with explicit criteria and a disposition
rule.

The names **Test Plan** and **Evaluation Plan** are reserved for maintained
artifacts that organize applicable Test Cases and Evaluation Cases. A Case,
its executable implementation, and its resulting Observation remain distinct
artifacts.

## Primary claim

Atomic QA definitions are Test Cases and Evaluation Cases; maintained
collections are Test Plans and Evaluation Plans.

## Rationale

“Plan” implies an updateable collection or coordinated course of work. “Case”
names one independently governed check definition and keeps the Test and
Evaluation chains symmetrical.
