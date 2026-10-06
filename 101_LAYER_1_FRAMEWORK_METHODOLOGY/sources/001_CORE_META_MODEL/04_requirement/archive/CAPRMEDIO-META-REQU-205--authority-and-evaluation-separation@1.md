---
subject_scope: authority
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-196--three-axis-artifact-routing
---

# Requirement — Separate authority from evaluation

CAPRMEDIO distinguishes:

- authoritative Definitions and Methods;
- maintained and generated Implementations;
- Test and Evaluation Methods;
- execution Observations and Evidence;
- Verification judgments about sufficiency and currentness.

Tests, Evaluations, Evidence, dashboards, and Verification may support,
challenge, or invalidate reliance on a claim. They cannot establish, edit,
replace, or override semantic authority. An evaluation failure creates feedback
for the appropriate owner rather than silently changing the governing claim.

## Primary claim

CAPRMEDIO keeps authoritative claims, checking methods, implementations, observations, evidence, and verification judgments semantically distinct, and evaluation cannot establish or override authority.

## Rationale

Evidence can be canonical for an observation without becoming the authority for desired behavior, implementation policy, or project scope.


## Historical frontmatter metadata

```yaml
promotion:
  affected_children:
    - "governance"
    - "tool"
    - "skill"
    - "implementation"
    - "operations"
  applies_unchanged: true
  local_context_required: false
```
