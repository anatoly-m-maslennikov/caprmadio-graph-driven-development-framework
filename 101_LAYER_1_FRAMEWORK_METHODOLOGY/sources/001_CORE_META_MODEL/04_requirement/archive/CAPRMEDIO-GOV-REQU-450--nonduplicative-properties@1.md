---
subject_scopes:
  - artifact-catalog
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-190--explicit-three-axis-route
      - CAPRMEDIO-META-REQU-191--sparse-routing-matrix
      - CAPRMEDIO-GOV-REQU-449--markdown-yaml-frontmatter
---

# Requirement — Give every property one meaning

An artifact property section contains no two properties that express the same
meaning and no property whose value is deterministically derived from another
canonical property, the artifact catalog, the current project, or repository
placement.

The artifact type and optional subtype determine their registered route.
Therefore Markdown frontmatter does not repeat `revision_mode`,
`content_role`, or `governance_locus`. Atomic artifacts do not carry an
acceptance status: creation follows explicit acceptance, while archive
placement represents removal from active authority.

Project identity is ambient. Internal acceptance does not require a repeated
operator-authority property. External origin uses a precise source reference,
issuer, or relation endpoint instead of a generic authority string.

Repeated relations of the same kind use one non-empty `targets` array.
Relations with different roles, qualifiers, or meanings remain separate.

## Rationale

Redundant properties can disagree and create competing sources of truth.
Derived values belong in deterministic resolution and validation, not in every
artifact carrier.
