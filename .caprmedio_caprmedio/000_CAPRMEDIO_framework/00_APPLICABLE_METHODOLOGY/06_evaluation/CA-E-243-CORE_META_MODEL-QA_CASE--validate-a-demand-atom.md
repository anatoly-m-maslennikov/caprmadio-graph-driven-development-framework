---
subjects:
  governs:
    occurrent:
      - Demand Validation
  depends_on:
    continuant:
      - "Atom/Content Role: Requirement/Type: Demand"
atom_id: CA-E-243
cce_version: cce_1
cce_form: evaluation
version: 12
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-243-CORE_META_MODEL-QA_CASE--validate-a-demand-atom.md
---
# Validate a Demand Atom

## Claim checked

a Demand is owned by its Consumer **and** constrains **only** one Producer result authorized by the Consumer's accepted Goal.

## Test case

create valid Demands across permitted branches **and** from a later ordered sibling to an earlier ordered sibling. **then** remove the Goal-authorized dependency, change ownership, target an ancestor, direct child, deeper descendant, **or** later ordered sibling, target two results, constrain Producer authority outside the selected result, fully define Producer Scope, **and** add a separate Demand-direction relation Kind.

## Acceptance criteria

**only** fixtures with Consumer ownership, a permitted direction, one exact Goal-authorized dependency, one exact Implementation result, **and** no additional direction relation pass.

## Failure disposition

record a Concern naming the invalid Demand fact.
