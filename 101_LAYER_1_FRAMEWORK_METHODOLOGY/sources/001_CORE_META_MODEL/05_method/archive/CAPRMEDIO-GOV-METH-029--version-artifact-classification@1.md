---
artifact_subtype: implementation_decision
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
      - CAPRMEDIO-GOV-METH-022--delivery-artifact-type
  - type: relates_to
    targets:
      - CAPRMEDIO-FIELD-METH-069--version-lifecycle-type
---

# Decision — Classify release lifecycle artifacts as Version

The canonical artifact registry uses the primary Type `version` for Roadmap,
Version Scope, Change, Release Plan, Readiness Record, and Release Record.
Those six direct subtypes remain flat. Default type-bearing artifact IDs and
filenames use `VERSION`.

Current schemas, templates, examples, validation, settings documentation,
generated views, and active carriers must not accept or emit `delivery` as an
artifact Type. Ordinary prose may still use the English word “delivery” for a
development flow, deployment, message transport, or historical evidence when
it is not naming the governed Type.

This Decision completely replaces `CAPRMEDIO-GOV-METH-022--delivery-artifact-type` and is the
classification sibling of `CAPRMEDIO-FIELD-METH-069--version-lifecycle-type`, which owns the unchanged
release-lifecycle behavior.

This emitted Decision atom is immutable. Later correction requires a successor
Decision and append-only lifecycle event.

## Primary claim

The artifact registry classifies the six release-lifecycle roles under the primary Version artifact Type, never Delivery.

## Rationale

Version identifies the governed artifact subject without requiring readers to distinguish DSET's prior use of Delivery from deployment or workflow delivery.


## Historical frontmatter metadata

```yaml
promotion:
  affected_children:
    - "meta"
    - "gov"
    - "tool"
    - "skill"
    - "ops"
  applies_unchanged: false
  local_context_required: true
  parent_scope:
    kind: "project"
    id: "dset-specs-loops-framework"
```
