---
subjects:
  governs:
    continuant:
      - artifact-query
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 6
updated_at: 2026-08-30 16:44:07 +0400
---
# Query artifacts by filters

The framework must provide one deterministic generic Artifact Tool that returns stably ordered canonical artifact IDs and carrier paths matching composable filters for structural scope, layer, tier, Feature, Content role, subject scope, lifecycle state, and typed relations without loading artifact bodies.

This Tool owns generic artifact-query mechanics only. `ATOM_SEARCH` owns CAPRMEDIO Markdown Atom eligibility, selector, lifecycle, subtree, content-query, and output-view semantics; it may use this Tool as a helper but the generic Tool must not become the public Atom-search operation.
