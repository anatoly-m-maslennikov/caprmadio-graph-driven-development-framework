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
      - CAPRMEDIO-GOV-REQU-295--derive-locus-and-declare-endpoint-origins
---

# Requirement — Release Plan is a maintained Definition

A Release Plan declares:

```toml
artifact_type = "maintained"
content_role = "definition"
authority_origin = "internal"
```

It defines the intended release scope, entry conditions, ordered release work,
completion conditions, and release target.

Related artifacts remain distinct:

- release scripts and procedures are maintained Methods;
- packaged or published release assets are maintained Implementations;
- readiness evidence and the Release Record are Observations.

## Primary claim

A Release Plan is a maintained, internal Definition artifact because it directly states the intended release scope, conditions, sequence, and completion state rather than implementing or observing the release.

## Rationale

A Release Plan governs what the release is intended to contain and satisfy; release tooling is Method, delivered release assets are Implementation, and readiness or publication records are Observation.


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
