---
subjects:
  governs: "Demand Validation"
  depends_on:
    - "Atom/Content Role: Requirement/Type: Demand"
    - "Local Order"
cce_version: cce_1
cce_form: evaluation
version: 17
updated_at: "2026-09-10 05:21:58 +0400"
relations:
  evaluation_for:
    - CA-R-932
    - CA-R-933
    - CA-R-916
    - CA-R-944
    - CA-R-1293
    - CA-R-934
    - CA-R-954
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Validate a Demand Atom

## Claim checked

a Demand is owned by its Consumer **and** constrains **only** one Producer result authorized by the Consumer's accepted Goal.

## Test case

create valid Demand Atoms with Consumer **and** Producer Scope Unit references in permitted branches **and** with a later ordered sibling as Consumer **and** an earlier ordered sibling as Producer. **then** remove the Goal-authorized need for the Producer result, change ownership, target an ancestor, direct child, deeper descendant, **or** later ordered sibling, use equal Producer **and** Consumer Local Order, target two results, constrain Producer authority outside the selected result, fully define Producer Scope, **and** add a separate Demand-direction relation Kind.

## Acceptance criteria

**only** fixtures with Consumer ownership, a permitted direction, one exact Goal-authorized need for the Producer result, one exact Implementation result, **and** no additional direction relation pass.

## Failure disposition

record a Concern naming the invalid Demand fact.
