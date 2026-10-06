---
subject_scope: artifact-model
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMEDIO-META-REQU-111--nine-content-roles-with-plan
      - CAPRMEDIO-META-REQU-114--preserve-content-role-boundaries-through-caprmedio-loop
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-093--analysis-and-ops-fact-boundary
      - CAPRMEDIO-REQU-003--apply-dry-across-caprmedio
---

# Requirement — Place rationale in Analysis

Rationale is interpretive justification and belongs to the Analysis Content role. Requirement, Method, Evaluation, and Delivery artifacts own normative specification and must not embed a `Rationale` section or duplicate rationale metadata.

When material rationale is worth preserving, one Analysis Atom owns one primary explanatory conclusion and relates it to one or more applicable specification Atoms. Rationale is optional: an obvious claim does not require an Analysis Atom merely to satisfy a template.

If explanatory text changes an obligation, boundary, selected method, evaluation condition, delivery rule, or acceptance meaning, that text is normative rather than rationale and remains in the applicable specification Atom.

## Primary claim

Material rationale is optional Analysis linked to specification artifacts; it is never embedded normative specification content.
