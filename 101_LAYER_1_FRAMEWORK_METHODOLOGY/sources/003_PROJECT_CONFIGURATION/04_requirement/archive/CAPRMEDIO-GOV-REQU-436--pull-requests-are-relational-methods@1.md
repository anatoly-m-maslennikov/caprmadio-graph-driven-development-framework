---
subject_scopes:
  - relation-model
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMEDIO-GOV-REQU-432--separate-standalone-origin-from-relational-endpoints
  - type: relates_to
    targets:
      - CAPRMEDIO-GOV-REQU-435--git-commits-are-atomic-implementations
---

# Requirement — Pull requests are relational Methods

A pull request declares:

```toml
artifact_type = "maintained"
content_role = "method"
relation_shape = "relational"
```

It has at least two endpoints:

```toml
[[endpoints]]
role = "source"
target = "<source repository and branch>"
origin = "internal" # or external

[[endpoints]]
role = "target"
target = "<target repository and branch>"
origin = "internal" # or external
```

Canonical cases are:

| PR case | Source origin | Target origin |
|---|---|---|
| Project branch into its own integration or protected branch | internal | internal |
| External contributor or fork into the project | external | internal |
| Project contribution into an upstream repository | internal | external |
| External repository contribution into another external repository | external | external |

The native repository-qualified PR number is the canonical identity. DSET does
not allocate a duplicate semantic sequence for the PR itself.

A merged or closed PR remains a maintained platform record because its body,
labels, discussion, and other metadata may remain editable. The merge commit
or squash commit is the resulting Atomic Implementation. When immutable proof
of the final PR state is required, DSET captures a separate Atomic Observation
that references both the PR and resulting commit.

## Primary claim

A pull request is classified as maintained + method + relational, retains its native repository and PR-number identity, and represents internal or external participation through its source and target endpoint origins rather than one authority-origin value.

## Rationale

A pull request is a mutable review and integration mechanism connecting two branches or repositories; merging it produces an immutable commit but does not transform the mutable PR record into an Atomic Implementation.


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
