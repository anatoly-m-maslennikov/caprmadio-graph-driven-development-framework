---
subjects:
  governs: "Atom selection"
  depends_on:
    - "Owned Atoms"
    - "Targeting Atoms"
    - "Subtree-owned Atoms"
    - "Subtree-targeting Atoms"
    - "Atom/Claim/Target Scope"
    - "Scope Unit"
cce_version: cce_1
cce_form: evaluation
version: 1
updated_at: "2026-09-15 23:56:42 +0400"
relations:
  evaluation_for:
    - CA-R-1448
    - CA-R-1449
    - CA-M-273
---
# Validate Claim-target Atom-set Selection

## Claim checked

ownership **and** Claim targeting produce distinct direct **and** recursive Atom sets from the same complete source frontier.

## Test case

create Scope Unit `A`, its descendant `A_CHILD`, sibling `B`, Atoms owned by each unit with omitted current targets, one Atom owned by `B` and targeting `A`, one Atom owned by `A` and targeting `B`, **and** nested Atom Collections under `A`. derive all four sets for `A`; repeat after changing only collection nesting **and** Local Tiers. **then** remove the incoming Atom from the claimed-complete frontier, replace targeting with ownership, **or** replace Scope Unit ancestry with physical directory ancestry.

## Acceptance criteria

Owned Atoms contain only Atoms owned directly by `A`; Targeting Atoms additionally include the Atom owned by `B` and targeting `A` but exclude the Atom owned by `A` and targeting `B`; each recursive set adds the corresponding members for `A_CHILD`. collection nesting **and** Local Tier changes do not alter the sets. incomplete source coverage **or** ownership-target substitution fails explicitly.

## Failure disposition

record a Concern naming the selected Scope Unit, source frontier, expected set, **and** every missing, extra, **or** unresolved member.
