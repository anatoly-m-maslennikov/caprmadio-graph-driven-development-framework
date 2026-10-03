---
subject_scopes:
  - feature-boundary
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 7
updated_at: 2026-08-23 15:33:04 +0400
---
# Register extensible Tool capability classes

Every Tool must register exactly one primary Tool kind: `finder` for strictly read-only retrieval or evaluation, or `doer` for governed mutation or materialization. `checker` is a registered Finder specialization that applies explicit Evaluation criteria and returns issues, evidence, or a verdict; additional specializations may extend a primary kind only through explicit registration of their semantics and interface obligations.
