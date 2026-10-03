---
atom_id: CA-E-425
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Relational Atom Classification Validation
  depends_on:
    continuant:
      - Relational Atom/Qualified Type
      - "Atom/Content Role: Requirement/Type: Goal"
      - "Atom/Content Role: Requirement/Type: Demand"
      - "Atom/Content Role: Plan/Type: Objective"
version: 2
updated_at: 2026-09-06 01:45:12 +0400
relations:
  replacement_of:
    - CA-R-877
  evaluation_for:
    - CA-R-923
    - CA-R-924
    - CA-R-747
    - CA-R-1365
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-425-CORE_META_MODEL-CORE-EVALUATION--validate-relational-atom-classifications.md
---
# Validate Relational Atom Classifications

## Claim checked

**every** Relational Atom **must** have **`=1`** qualified Type allowed by the Applicable Methodology, **and** the Core contribution **must** admit **only** Requirement/Goal, Requirement/Demand, **and** Plan/Objective.

## Test case

create one relational Requirement/Goal Atom, one relational Requirement/Demand Atom, **and** one relational Plan/Objective Atom. **then** create relational Atoms with Requirement/Task, Plan/Task, Method, Evaluation, Delivery, Implementation, **and** Ops qualified Types **without** an additional Applicable Methodology contribution.

## Acceptance criteria

**only** the Requirement/Goal, Requirement/Demand, **and** Plan/Objective fixtures pass.

## Failure disposition

record a Concern naming the invalid Relational Atom qualified Type.
