---
subject_scopes:
  - relation-model
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
  relates_to:
    - CAPRMEDIO-GOV-REQU-309--revision-bound-parent-child-commit-messages
---
# Classify lineage impact with four dispositions

When an Atomic Artifact receives a new committed revision, each directly
dependent child reached by the impact review must receive exactly one
disposition:

- `compatible` — the child remains valid and bound to the earlier parent
  revision; no child update is created and traversal stops on that branch;
- `update_required` — create a new committed revision of the same child based
  on the new parent revision, then assess the revised child's descendants;
- `replacement_required` — create a successor, archive the replaced child,
  and assess every descendant that depended on the replaced child; or
- `uncertain` — create a Question when knowledge is unresolved or a Problem
  when a verified discrepancy or blockage exists, then stop that branch until
  it is resolved.

The review must preserve the parent revision examined, the child examined, the
chosen disposition, and any resulting child revision or blocking artifact.
Tooling may automate traversal and classification proposals, but it must not
silently select a non-compatible outcome or continue through an uncertain
branch.

## Rationale

A closed disposition set makes impact propagation deterministic while avoiding
unnecessary rewrites of compatible children and preventing uncertain effects
from silently reaching deeper descendants.
