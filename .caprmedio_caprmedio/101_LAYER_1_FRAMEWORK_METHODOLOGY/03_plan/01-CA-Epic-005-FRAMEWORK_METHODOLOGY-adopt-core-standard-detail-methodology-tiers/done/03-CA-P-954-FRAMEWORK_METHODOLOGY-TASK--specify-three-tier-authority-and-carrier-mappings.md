---
atom_id: CA-P-954
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    occurrent:
      - "Atom/Global Tier"
  depends_on:
    continuant:
      - Atom/Claim
      - Atom/Claim/Scope
      - Scope Unit
      - Atom/Local Tier
      - Autonomous Confidence Threshold
version: 2
updated_at: "2026-09-10 01:48:30 +0400"
autonomous_confidence_threshold: 99
relations:
  depends_on:
    - CA-P-953
---
# Specify three-tier authority and Carrier mappings

the Assignee **must** specify the complete authority **and** Carrier mappings required by Core / General / Standard.

## Scope

(the active methodology rules for Local Tier eligibility, Global Tier derivation, Goal placement, Content Role **and** Type tier restrictions, tier parentage, **and** tier serialization)

## Definition of Done

the Task is **not** Done **if** (an admitted structural case lacks an explicit old-to-new authority mapping **or** Goal placement **or** a Content Role **or** Type restriction is unmapped **or** default omission, tier labels, **or** filename tokens are ambiguous **or** changed precedence is hidden as a naming change **or** lower-tier source authority becomes freely replaceable by an Extension **or** Local Configuration).

## Details

FX-04: consume the Scope specification from CA-P-953. use the accepted hierarchy: Core foundations **and** invariants; General shared specifications independent of concrete representation **or** implementation; Standard concrete fields, syntax, procedures, **and** test cases. Standard (STD) remains the lowest Local Tier **and** the omitted default. use CORE **and** GENERAL for explicit tier tokens. derive Global Tier mappings from the accepted structural hierarchy **and** ordered Local Tiers; this derivation requires **no** separate approval of tier arithmetic. reconcile the current Project Principle/Core/Standard ladder, external Goal exception, recursive child mapping, Core-only Implementation Method, **and** existing Standard-only Implementation Decision restrictions against the new hierarchy. preserve Project-only Principle eligibility; do **not** introduce another Principle tier. consult Project Principles **before** escalating a genuinely unresolved policy choice below the effective Autonomous Confidence Threshold. earlier execution evidence retains historical tier names; map its middle Standard to General **and** its lowest Detail to Standard, **not** its inventory of existing pre-change Standard Atoms.
