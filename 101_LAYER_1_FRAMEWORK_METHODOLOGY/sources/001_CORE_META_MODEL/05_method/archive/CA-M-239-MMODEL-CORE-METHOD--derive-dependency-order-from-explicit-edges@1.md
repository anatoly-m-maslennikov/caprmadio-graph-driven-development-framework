---
atom_id: CA-M-239
cce_version: cce_1
cce_form: method
subjects:
  governs:
    occurrent:
      - Dependency Order Derivation
  depends_on:
    continuant:
      - DEPENDS_ON
      - DERIVED_FROM
      - Atom/Direct Relation Serialization
      - Artifact/Revision
      - "Atom/Content Role: Plan/Type: Task"
version: 1
updated_at: 2026-09-01 23:18:00 +0400
relations:
  child_of:
    - CA-M-120
---
# Derive Dependency Order from Explicit Edges

**to** derive one dependency order, the resolver **must** construct one directed graph from direct `relations.depends_on` edges from **every** Consumer **to** **every** prerequisite Provider, derive its `required_by` inverse view **without** authoring inverse edges, calculate one deterministic prerequisite-first topological order with canonical identity **only** as a tie-breaker, **and** reject a cycle; it **must not** use target-list position, Local Order, **or** `relations.derived_from` as a dependency edge.
