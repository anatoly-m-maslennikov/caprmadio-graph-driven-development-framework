---
subject_scopes:
  - external-boundary
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMEDIO-GOV-REQU-432--separate-standalone-origin-from-relational-endpoints
  - type: replacement_of
    targets:
      - CAPRMEDIO-GOV-REQU-433--evergreen-artifacts-have-internal-origin
  - type: override_of
    targets:
      - CAPRMEDIO-GOV-REQU-437--unique-internal-and-external-type-names
  - type: relates_to
    targets:
      - CAPRMEDIO-GOV-REQU-438--generated-outputs-are-evergreen-implementations
---

# Requirement — Evergreen projections may have external authority

An Evergreen artifact is a mutable current projection. Its authority origin
identifies who governs the projected truth:

- `internal` — the project compiles and governs the current projection;
- `external` — an external authority publishes and governs the current
  projection, while the project tracks, synchronizes, or references it.

A local mirror or cache of an external Evergreen artifact does not make it
internal.

The Evergreen row of the standalone matrix is:

| Content role | Internal Type | External Type |
|---|---|---|
| Definition | Specification | Constraint Set |
| Rationale | Rationale Synthesis | External Rationale Synthesis |
| Method | Guidance | External Methodology |
| Implementation | Generated Implementation | Reference Implementation |
| Observation | View | External Overview |

Examples include:

- a current externally governed constraint set;
- a current synthesis explaining an external constraint set;
- an external methodology, profile, or pattern collection;
- an evolving reference implementation or implementation target;
- an externally governed current overview.

The following boundaries keep the classification MECE:

- an immutable upstream version or digest is Atomic;
- an external library, SDK, or directly used tool is a Maintained Dependency;
- a copied external asset used directly by the implementation is a Maintained
  Imported Asset;
- an external current projection governed upstream is Evergreen;
- a project-generated dashboard or other executable projection is an internal
  Generated Implementation.

## Primary claim

Evergreen artifacts are mutable current projections and may have internal or external authority origin; the external Evergreen Types are Constraint Set, External Rationale Synthesis, External Methodology, Reference Implementation, and External Overview.

## Rationale

A current projection may be governed by the project or by an upstream authority. Treating every Evergreen artifact as internal loses the authority of evolving external constraint sets, methodologies, implementation references, and overviews.


## Historical frontmatter metadata

```yaml
promotion:
  affected_children:
    - "governance"
    - "tool"
    - "skill"
    - "implementation"
    - "ops"
  applies_unchanged: true
  local_context_required: false
```
