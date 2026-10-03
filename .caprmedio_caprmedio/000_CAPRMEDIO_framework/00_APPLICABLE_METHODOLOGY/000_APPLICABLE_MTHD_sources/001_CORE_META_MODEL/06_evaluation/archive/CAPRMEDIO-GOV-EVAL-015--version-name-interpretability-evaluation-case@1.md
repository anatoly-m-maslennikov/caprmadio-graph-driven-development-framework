---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
priority: medium
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
      - CAPRMEDIO-GOV-EVAL-011--mece-artifact-classification
      - CAPRMEDIO-FIELD-EVAL-058--delivery-artifact-boundaries
---

# Evaluation Case — Interpret the Version artifact Type

Give independent reviewers the current artifact catalog, filenames, and short
artifact examples without explaining the former name. Pass only when every
reviewer identifies Version as the release-lifecycle Type; assigns Roadmap,
Version Scope, Change, Release Plan, Readiness Record, and Release Record as
flat direct subtypes; preserves their distinct roles; and does not confuse the
Type with product-version strings, source-control versions, deployment state,
or semantic Decision Types.

Record ambiguity and rival interpretations. A majority vote does not conceal
one materially different classification; reconcile it or keep the Evaluation
inconclusive.

This emitted Evaluation atom is immutable. Later correction requires a
successor Evaluation and append-only lifecycle event.

## Primary claim

Independent reviewers can correctly interpret Version and assign all six release-lifecycle artifacts without needing an additional explanation of the primary Type name.


## Historical frontmatter metadata

```yaml
promotion:
  affected_children:
    - "gov"
    - "ops"
  applies_unchanged: false
  local_context_required: true
  parent_scope:
    kind: "project"
    id: "dset-specs-loops-framework"
```
