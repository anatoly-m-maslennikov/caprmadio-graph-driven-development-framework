---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
priority: medium
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-GOV-EVAL-020--feature-and-layer-distinction
  - type: check_of
    targets:
      - CAPRMEDIO-META-REQU-202--layer-handoff-contracts
      - CAPRMEDIO-META-REQU-203--acyclic-layer-dependencies
      - CAPRMEDIO-META-REQU-227--scope-path-is-structural
---

# Evaluation Case — Assess feature and layer distinction

Give reviewers examples with horizontal peer contracts, forward-only ordered
authority, and unavoidable backward dependencies. Ask whether each structure
should use features, layers, nested scope paths, or conversion from layers to
features.

The evaluation passes when at least 90% classify horizontal ownership as
features, ordered downstream authority as layers, and irreducible backward
dependency as a reason to stop claiming a clean layer model.
