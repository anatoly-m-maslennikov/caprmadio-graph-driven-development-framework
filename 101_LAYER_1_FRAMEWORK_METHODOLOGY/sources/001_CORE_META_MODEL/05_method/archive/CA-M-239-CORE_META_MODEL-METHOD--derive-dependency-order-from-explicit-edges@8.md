---
cce_version: cce_1
cce_form: method
subjects:
  governs: "Dependency Order Derivation"
  depends_on:
    - "DEPENDS_ON"
    - "DERIVED_FROM"
    - "Atom/Direct Relation Serialization"
    - "Artifact/Revision"
    - "Artifact"
    - "Atom/Content Role: Plan/Type: Plan"
version: 8
updated_at: "2026-09-22 14:41:44 +0000"
relations:
  child_of:
    - CA-M-120
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Derive Dependency Order from Explicit Edges

**to** derive one non-Plan Artifact dependency order, the resolver **must** construct one directed graph from direct `relations.depends_on` edges from **every** dependent Artifact **to** **every** prerequisite Artifact, derive its `required_by` inverse view **without** authoring inverse edges, calculate one deterministic prerequisite-first topological order with canonical identity **only** as a tie-breaker, **and** reject a cycle; it **must not** use target-list position, Local Order, **or** `relations.derived_from` as a dependency edge. Plan readiness follows `BLOCKS` under CA-R-1580: **all** blockers **must** be Done, **and** independent ready Plans **may** execute concurrently subject **to** their permissions; navigation order **must not** add blocking.
