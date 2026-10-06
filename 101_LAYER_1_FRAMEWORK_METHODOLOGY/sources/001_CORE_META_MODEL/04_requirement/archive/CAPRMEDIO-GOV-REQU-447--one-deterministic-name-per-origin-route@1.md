---
subject_scopes:
  - artifact-catalog
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMEDIO-GOV-REQU-446--axis-routed-artifacts-without-type-taxonomy
---

# Requirement — One deterministic name per origin route

Every admitted route has exactly one internal name and one external name.

The name is derived from the complete route:

```text
<Governance Origin> <Revision Mode> <Content Role> <Artifact | Relation>
```

Examples:

```text
Internal Atomic Definition Artifact
External Atomic Definition Artifact
Internal Maintained Method Relation
External Evergreen Observation Artifact
```

The origin word is selected only from `Internal` or `External`. The final word
is selected only from `Artifact` or `Relation`.

Route names are deterministic display outputs. They are not stored Types,
subtypes, aliases, routing inputs, identity authorities, or lifecycle owners.

## Primary claim

Every admitted artifact route has exactly one deterministic internal name and one deterministic external name; route names are derived display outputs rather than artifact Types.

## Rationale

One name per governance origin keeps interfaces readable without recreating a competing Type taxonomy or allowing aliases to affect routing.


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
