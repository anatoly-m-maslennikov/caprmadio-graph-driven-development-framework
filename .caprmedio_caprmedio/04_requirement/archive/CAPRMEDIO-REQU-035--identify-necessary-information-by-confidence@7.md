---
subject_scopes:
  - authority
tier: core
version: 7
updated_at: 2026-08-22 03:01:35
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-M-003-PRINCIPLE-METHOD--use-lossless-selective-exposure
---
# Identify necessary information by confidence

To determine whether project information is necessary, an LLM must inspect every active Project Principle, every active Atom in the information's full ancestor and descendant lineage, and every other active Atom in the same structural scope. The information is necessary when its omission would leave the LLM below the effective framework-owned confidence threshold configured for the active `FRAMEWORK_ENGINE`. The confidence and threshold are operational heuristics, not comparable probabilities across configurations.
