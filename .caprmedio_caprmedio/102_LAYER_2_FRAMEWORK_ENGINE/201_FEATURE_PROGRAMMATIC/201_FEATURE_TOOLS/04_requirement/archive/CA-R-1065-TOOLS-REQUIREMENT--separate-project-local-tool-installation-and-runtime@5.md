---
subject_scopes:
  - feature-boundary
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 5
updated_at: "2026-08-23 11:37:28"
relations:
  child_of:
    - CAPRMEDIO-REQU-702--define-framework-engine-layer-scope
---
# Separate project-local Tool installation and runtime

All Tools in one CAPRMEDIO project must use one project-local installation rooted at `.caprmedio_install` and one project-local runtime rooted at `.caprmedio_runtime`. The installation contains content-addressed executable releases, shared non-executable libraries, machine-readable registries, declared dependencies, stable launchers, and Hook carriers. The runtime contains only mutable execution state, caches, logs, service state, and other reconstructible outputs.

An installed Tool must import executable and non-executable implementation only from its selected installation release; it must not import framework implementation from the canonical source tree, `.caprmedio`, `.caprmedio_runtime`, or another project path. Host interpreters and Git remain declared substrate dependencies rather than copied framework implementation. A host-required discovery carrier may point into `.caprmedio_install`, but it must contain no independent framework behavior and must not become dependency authority.
