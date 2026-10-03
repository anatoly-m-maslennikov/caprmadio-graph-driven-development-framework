---
subjects:
  governs:
    occurrent:
      - Demand Validation
  depends_on:
    continuant:
      - "Atom/Content Role: Requirement/Requirement Type: Demand"
atom_id: CA-E-243
cce_version: cce_1
cce_form: evaluation
version: 9
updated_at: 2026-08-29 02:40:41 +0400
relations: {}
---
# Validate a Demand Atom

## Claim checked

a Demand is owned by its Consumer **and** constrains **only** one Producer result authorized by the Consumer's accepted Job.

## Test case

create valid Demands across permitted branches **and** from a later ordered sibling to an earlier ordered sibling. **then** remove the Job-authorized dependency, change ownership, target an ancestor, direct child, deeper descendant, **or** later ordered sibling, target two results, constrain Producer authority outside the selected result, fully define Producer Scope, **and** add a separate Demand-direction relation Kind.

## Acceptance criteria

**only** fixtures with Consumer ownership, a permitted direction, one exact Job-authorized dependency, one exact Implementation result, **and** no additional direction relation pass.

## Failure disposition

record a Concern naming the invalid Demand fact.
