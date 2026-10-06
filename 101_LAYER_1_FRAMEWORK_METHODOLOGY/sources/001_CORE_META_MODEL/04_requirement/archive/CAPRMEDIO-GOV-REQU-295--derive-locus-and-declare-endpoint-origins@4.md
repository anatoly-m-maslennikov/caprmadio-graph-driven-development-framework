---
subject_scopes:
  - relation-model
version: 4
updated_at: 2026-08-22 01:37:40
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-084--relational-artifacts-declare-endpoints
---
# Derive Governance origin and encode graph relations

Each registered Atom Type derives exactly one `governance_origin`: `internal`
or `external`. Atom carriers do not repeat the Type-derived origin.

Every graph relation is encoded as a typed edge under the relation-owning Atom's
`relations` frontmatter. Relation direction follows from the registered
relation kind and the identity of the Atom that owns the direct edge.

Graph connectivity does not become another Governance origin. External
provenance, issuer, source, or ownership facts use their precise type-specific
properties rather than a generic duplicate origin field.

## Rationale

The rule keeps meaning ownership orthogonal to graph connectivity and prevents
relation edges from becoming duplicate Artifact identities.
