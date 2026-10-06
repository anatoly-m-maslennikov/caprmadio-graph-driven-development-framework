---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: check_of
    targets:
      - CAPRMEDIO-GOV-METH-029--version-artifact-classification
      - CAPRMEDIO-FIELD-METH-069--version-lifecycle-type
  - type: replacement_of
    targets:
      - CAPRMEDIO-GOV-EVAL-023--delivery-artifact-classification
      - CAPRMEDIO-FIELD-EVAL-059--delivery-release-role-boundaries
---

# Test Case — Enforce the Version artifact classification

Parse the current registry, schemas, templates, active Version artifacts,
settings examples, and release-tool fixtures. Require the primary Type
`version`, the direct subtypes `roadmap`, `version_scope`, `change`,
`release_plan`, `readiness_record`, and `release_record`, and one shared
type-bearing `VERSION` identity sequence. Reject `delivery` as a current
artifact Type, mismatched or nested subtypes, stale active `DELIVERY` IDs, and
partial migrations. Preserved historical records may retain the former term
only when their currentness is explicitly historical.

Run artifact-type, project-health, release-artifact, release-integration,
bootstrap, recursive validation, and generated-view freshness checks.

This emitted Test atom is immutable. Later correction requires a successor
Test and append-only lifecycle event.

## Primary claim

Deterministic validation requires Version and its six exact direct subtypes across current authority, registries, templates, active carriers, generated views, settings examples, and release behavior, while rejecting Delivery as a current artifact Type.


## Historical frontmatter metadata

```yaml
promotion:
  affected_children:
    - "gov"
    - "tool"
    - "ops"
  applies_unchanged: false
  local_context_required: true
  parent_scope:
    kind: "project"
    id: "dset-specs-loops-framework"
```
