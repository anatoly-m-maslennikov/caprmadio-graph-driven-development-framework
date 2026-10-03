---
atom_id: CA-C-108
priority: low
subjects:
  governs: "Entity"
  depends_on:
    - "Atom"
    - "Atom/Claim"
    - "Atom/Subjects"
    - "Atom/Content Role: Requirement"
    - "Atom/Content Role: Delivery"
    - "Scope Unit"
    - "Atom/Tier/Local Tier"
version: 2
updated_at: "2026-09-14 19:40:02 +0400"
relations: {}
---
# How many R and D Atoms may govern one Entity?

what limits, **if** **any**, should apply **to** the number of Requirement **and** Delivery Atoms that govern the same Entity while expressing distinct Claims?

## Context

the Operator can envisage cases requiring **`>1`** Requirement Atom for the same Entity because the Claims differ. the earlier proposed limit of **`<=1`** Requirement Atom **and** **`<=1`** Delivery Atom per Entity remains unresolved. distinct Claims **and** duplicated authority for the same Claim are different cases; correctly assigned Subjects, applicable Scope Units, **and** Local Tiers require consideration **before** choosing a rule.

## Disposition

deferred for later consideration at the Operator's request. this Concern records an open design question; it does **not** establish a cardinality rule **or** block the current migration.
