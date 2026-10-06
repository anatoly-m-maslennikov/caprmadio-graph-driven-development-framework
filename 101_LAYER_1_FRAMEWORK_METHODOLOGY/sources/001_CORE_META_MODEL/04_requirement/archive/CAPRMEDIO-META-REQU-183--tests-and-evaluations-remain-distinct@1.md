---
subject_scope: evaluation
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-182--governed-feedback-cycle
---

# Requirement — Tests and Evaluations remain distinct

Behavior with one exact expected result belongs to deterministic Test casening.
Behavior with multiple acceptable results judged by criteria belongs to
Evaluation casening. Their execution results remain distinct Observations.

## Primary claim

CAPRMEDIO keeps deterministic Tests and qualitative, probabilistic, statistical, or model-judged Evaluations in separate plans, implementations, and observation streams.

## Rationale

Automation does not erase the semantic difference between an exact assertion and a judgment against criteria or a rubric.
