---
subject_scopes:
  - lifecycle
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-REQU-425--explicit-artifact-commit-lifecycle
---
# Omit update settings from Atomic Artifacts

The canonical artifact catalog starts with a concise commented legend before
the first group or Type definition. The legend defines every shared field,
including where the field applies.

## Truth ownership

```toml
source_of_truth = true # or false
```

- `true`: an artifact of this catalog entry is the canonical source of truth
  for the concern it explicitly owns.
- `false`: the artifact is derived, supporting, executable, observational, or
  navigational for that concern and does not replace its declared source of
  truth.

## Commit lifecycle

Every persisted artifact entry uses:

```toml
commit_on_create = true
```

This means creating the artifact requires a Git commit that adds its carrier.

Only entries whose governed content may be updated in place declare:

```toml
commit_on_update = true
```

This means every persisted in-place update requires a Git commit.

Atomic Artifact entries do not contain `commit_on_update`. The field is not an
operator-selectable behavior for atoms: every admitted same-ID revision is
unconditionally committed through the governed revision transaction. The
absence of the field does not prohibit Atomic Artifact revisions.

A governed identity, filename, path, or carrier-format migration does not
change the atomic claim and is handled as a separately authorized, fully
committed `carrier_only` change. A refinement or semantic revision keeps the
artifact ID only under the governed change-class boundary. A replacement
creates a successor ID.

Any permitted removal is also a Git change. Atomic Artifacts are archived or
replaced through explicit relations and are not deleted as ordinary mutable
files.

## Rationale

Revision-bound Git history governs Atomic Artifact change directly. Encoding
that invariant as an optional catalog switch would permit projects to disable
the history needed for exact dependency and impact replay.

## Historical frontmatter metadata

```yaml
promotion:
  affected_children:
    - "governance"
    - "tool"
    - "skill"
    - "implementation"
    - "ops"
  applies_unchanged: false
  local_context_required: true
```
