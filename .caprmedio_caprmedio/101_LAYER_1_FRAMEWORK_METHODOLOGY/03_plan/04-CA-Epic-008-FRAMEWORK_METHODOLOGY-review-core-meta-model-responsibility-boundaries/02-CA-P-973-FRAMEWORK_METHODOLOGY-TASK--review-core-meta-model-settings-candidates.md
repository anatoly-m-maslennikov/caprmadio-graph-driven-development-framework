---
atom_id: CA-P-973
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    occurrent:
      - "methodology ownership review"
  depends_on:
    continuant:
      - "Core Meta-Model"
      - "Project Settings"
      - "Framework Instance Settings"
      - "Local Configuration"
      - "Atom/Claim"
      - "Atom/Content Role"
      - "Atom/Local Tier"
      - "Confidence Threshold"
version: 1
updated_at: "2026-09-11 03:04:50 +0400"
relations:
  depends_on:
    - CA-P-972
---
# Review Core Meta-Model Settings candidates

the Assignee **must** review the Settings ownership of Claims **in** CORE_META_MODEL against the accepted boundary inventory.

## Scope

(active Claims **in** CORE_META_MODEL screened for Settings ownership **and** their review evidence)

## Definition of Done

the Task is **not** Done **if** ((an inventoried Atom lacks a Settings-candidate screening result) **or** (a candidate lacks a Claim-level rationale **and** proposed authoritative owner) **or** (a current selected value is confused with the rule defining its permitted values, defaults, precedence, **or** representation) **or** (a Project initialization input is assigned **to** Framework Instance Settings **without** authority) **or** (a CAPRMEDIO behavior choice is assigned **to** Project Settings **without** authority) **or** (a proposal duplicates current selected values across Atoms **and** Settings) **or** (review conclusions below the effective Confidence Threshold bypass the Operator) **or** (reviewed authority **or** Settings is changed)).

## Details

screen the complete CA-P-972 inventory, **then** review candidates individually. Project Settings own inputs needed **before** the first Project Atom **or** Implementation; Framework Instance Settings own current Operator-selected framework behavior **and** configuration. declarations of what a setting is, its legal sources, precedence, application conditions, validation, **and** Carrier belong **to** the appropriate methodology RMED authority.

a configurable default is **not** automatically a misplaced current value. determine whether the Claim defines a reusable default mechanism, an explicitly permitted default, a Project-specific expansion, **or** this instance's selected value. distinguish current Extension activation **and** selected revisions from Extension definitions **and** Local Configuration expansion rules.

consider confidence thresholds, reporting **and** authority modes, retry policies, source selections, names, prefixes, **and** path bindings as discovery candidates, **not** predetermined findings. preserve generic Carrier specifications **in** D **where** they belong. assess source ownership separately from Core, General, **and** Standard tier placement.

for a mixed Claim, recommend which generic obligation remains authoritative **and** which selected value should be owned elsewhere; do **not** perform the split. **before** escalating, try **to** resolve the issue from Project Principles **and** current authority. resolve the effective Confidence Threshold through current precedence **without** inventing a fixed value.
