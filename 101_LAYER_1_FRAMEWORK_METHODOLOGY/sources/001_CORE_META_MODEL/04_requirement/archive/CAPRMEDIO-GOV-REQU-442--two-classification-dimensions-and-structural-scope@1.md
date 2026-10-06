---
subject_scopes:
  - artifact-catalog
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-GOV-REQU-441--three-primary-artifact-axes
  - type: relates_to
    targets:
      - CAPRMEDIO-GOV-REQU-435--git-commits-are-atomic-implementations
      - CAPRMEDIO-GOV-REQU-436--pull-requests-are-relational-methods
      - CAPRMEDIO-FIELD-METH-075--operate-without-backward-implementation-authority
---

# Requirement — Two classification dimensions and structural scope

DSET's primary classification matrix has exactly two intrinsic dimensions:

1. `revision_mode`;
2. `content_role`.

Every persisted governed artifact also has one canonical `scope_path`. The path
is a required structural ownership address and selects a slice of the shared
two-dimensional matrix. It is not a third semantic dimension.

`scope_path` uses the narrowest common owner that can govern the whole
artifact. It may contain the project, feature group, feature, layer, enabled
nested combinations, and future structural segments.

The path does not:

- identify the artifact's Entity of Concern;
- state where a claim applies;
- establish a bounded semantic context;
- determine Revision Mode, Content Role, Type, subtype, or qualifiers.

If meaning or invariants differ across structural scopes, DSET names the
semantic context or an explicit bridge. It never infers semantic equivalence or
difference from a filesystem or ownership path.

The complete classification shape is:

```text
MatrixCell(revision_mode, content_role)
@ StructuralScope(scope_path)
+ Qualifiers(relation_shape, governance_origin)
-> Type(+ optional direct subtype)
```

Each Scope Path renders a filtered matrix slice, not a separate ontology.

## Primary claim

DSET classifies persisted artifacts through exactly two intrinsic dimensions, revision_mode and content_role; scope_path is a required structural ownership address and matrix-slice key, not a semantic classification dimension.

## Rationale

FPF strict distinction separates intrinsic artifact characteristics from structural location, applicability, and views. A hierarchical scope path indexes the shared matrix but neither identifies the Entity of Concern nor establishes a bounded semantic context.


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
