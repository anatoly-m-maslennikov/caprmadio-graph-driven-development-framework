---
subject_scopes:
  - subject-scope
project_settings:
  artifacts:
    identity:
      scope_path_in_ids: true
version: 4
updated_at: 2026-08-18 20:19:17
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-REQU-427--expandable-scope-path-identities
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
  relates_to:
    - CAPRMEDIO-GOV-REQU-303--optional-project-prefix
    - CAPRMEDIO-GOV-REQU-323--register-caprmedio-type-prefixes
---
# Use expandable scope paths in identities

The canonical artifact identity and filename shape is:

```text
<PROJECT>-<SCOPE_PATH>-<TYPE_PREFIX>-<NNN>[-<SUBTYPE>]--<SUMMARY>.<ext>
```

`PROJECT` is omitted when project-prefix configuration disables it.
`SCOPE_PATH` is omitted at project scope. When present, it contains one or more
registered operator-chosen scope-label segments ordered from broader parent to narrower child. The first segment occupies Level 1, and every following segment occupies the next numbered level; path position is the single source of truth for structural level.

Scope does not change numbering. Numeric sequences remain project-wide for
each registered Type prefix. Every scope segment and
parent-child relationship is registered in `.caprmedio/caprmedio_project_settings.toml`, and a
path must match that registry exactly.

The first implementation and every later vocabulary change perform one
complete lossless migration across active and archived identities, filenames,
relations, Projection and Journal references, settings, Implementation
references, Ops records, and commit provenance.

## Rationale

One structural coordinate supports a project root and arbitrary configured hierarchy depth without hardcoding a scope-label taxonomy.
