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
      - CAPRMEDIO-GOV-REQU-432--separate-standalone-origin-from-relational-endpoints
---

# Requirement — Evergreen artifacts have internal origin

Every evergreen specification, plan, synthesis, architecture view, dashboard,
or other semantic projection is authored by the project through compilation.
It therefore declares:

```toml
artifact_type = "evergreen"
authority_origin = "internal"
```

Externally originated Constraints, evidence, references, and observations may
be compilation inputs. Their external origins remain attached to those source
artifacts and are preserved through provenance. They do not change the
compiled artifact's internal authorship.

## Primary claim

Every evergreen artifact has internal authority origin because the project semantically compiles and authors it, even when its source atoms or evidence have external origins.

## Rationale

Source provenance and artifact authorship are distinct: externally originated inputs remain traceable without making the project-authored compiled projection external.


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
