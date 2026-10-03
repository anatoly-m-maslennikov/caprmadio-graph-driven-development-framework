---
atom_id: CA-E-425
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Relational Atom Classification Validation"
  depends_on:
    - "Relational Atom/Qualified Type"
    - "Atom/Content Role: Requirement/Type: Goal"
    - "Atom/Content Role: Requirement/Type: Demand"
    - "Atom/Content Role: Plan/Type: Objective"
version: 7
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  evaluation_for:
    - CA-R-923
    - CA-R-924
    - CA-R-1365
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Validate Relational Atom Classifications

## Claim checked

**every** Relational Atom **must** have **`=1`** qualified Type allowed by the Applicable Methodology, **and** the Core contribution **must** admit **only** Requirement/Goal, Requirement/Demand, **and** Plan/Objective.

## Test case

create one relational Requirement/Goal Atom, one relational Requirement/Demand Atom, **and** one relational Plan/Objective Atom. **then** create relational Atoms with Requirement/Task, Plan/Task, Method, Evaluation, Delivery, Implementation, **and** Operations qualified Types **without** an additional Applicable Methodology contribution.

## Acceptance criteria

**only** the Requirement/Goal, Requirement/Demand, **and** Plan/Objective fixtures pass.

## Failure disposition

record a Concern naming the invalid Relational Atom qualified Type.
