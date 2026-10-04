---
subjects:
  governs: "Atom/Content Role: Requirement/Type: Demand"
  depends_on:
    - "Local Order"
version: 22
updated_at: "2026-10-02 19:57:02 +0400"
relations:
  evaluation_for:
    - CA-R-932
    - CA-R-933
    - CA-R-916
    - CA-R-944
    - CA-R-1293
    - CA-R-934
    - CA-R-954
atom_id: "CA-E-243"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-243-CORE_META_MODEL-QA_CASE--validate-a-demand-atom.md
---
# Summary

Validate a Demand Atom

## Scope

Demand Atoms and their Consumer-owned Producer-result constraints.

## Claim

a Demand is owned by its Consumer **and** constrains **only** one Producer result authorized by the Consumer's accepted Goal.

### Test case

create valid Demand Atoms with Consumer **and** Producer Scope Unit references **in** permitted branches **and** with a later ordered sibling as Consumer **and** an earlier ordered sibling as Producer. **then** remove the Goal-authorized need for the Producer result, change ownership, target an ancestor, direct child, deeper descendant, **or** later ordered sibling, use equal Producer **and** Consumer Local Order, target two results, constrain Producer authority outside the selected result, fully define Producer Scope, **and** add a separate Demand-direction relation Kind.

### Acceptance criteria

**only** fixtures with Consumer ownership, a permitted direction, one exact Goal-authorized need for the Producer result, one exact Implementation result, **and** no additional direction relation pass.

### Failure disposition

record a Concern naming the invalid Demand fact.

## Details
