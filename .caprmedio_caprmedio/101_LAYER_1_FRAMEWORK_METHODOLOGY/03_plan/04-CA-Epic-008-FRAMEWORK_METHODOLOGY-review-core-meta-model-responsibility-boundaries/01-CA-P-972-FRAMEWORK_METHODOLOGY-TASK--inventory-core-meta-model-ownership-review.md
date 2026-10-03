---
atom_id: CA-P-972
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    occurrent:
      - "methodology ownership review"
  depends_on:
    continuant:
      - "Core Meta-Model"
      - "Atom/Claim"
      - "Atom/Claim/Scope"
      - "Atom/Revision"
      - "Atom/Content Role"
      - "Atom/Local Tier"
      - "Project Settings"
      - "Framework Instance Settings"
      - "Local Configuration"
version: 1
updated_at: "2026-09-11 03:04:50 +0400"
relations: {}
---
# Inventory Core Meta-Model ownership review

the Assignee **must** produce a source-bound inventory for reviewing the responsibility boundaries of CORE_META_MODEL.

## Scope

(**all** active Atoms **in** CORE_META_MODEL **and** the review inventory derived from those Atoms)

## Definition of Done

the Task is **not** Done **if** ((an active in-scope Atom is absent from the inventory) **or** (an entry lacks its exact identity, Revision, Carrier path, content digest, Claim, Content Role, **or** Local Tier) **or** (review criteria lack their governing authority **or** an explicit unresolved question) **or** (CORE_META_MODEL ownership is conflated with Local Tier Core) **or** (a derived copy, Draft, **or** archived Revision is treated as an active source) **or** (this Task changes reviewed authority **or** current Settings)).

## Details

read the current Project Principles **before** deriving review criteria. inventory **all** active Content Roles **and** **all** Local Tiers within CORE_META_MODEL, **not** **only** RMED **or** Core-tier Atoms. use current Local Configuration, Settings, other methodology sources, **and** relevant Project Atoms as comparison evidence; they are **not** mutation targets.

distinguish reusable model authority, permitted optional expansion, Project-specific methodology, current Operator-selected values, concrete Project requirements, **and** derived **or** ephemeral data. preserve separate dimensions for source ownership, Local Tier, **and** Content Role.

start boundary discovery from CA-R-1207, CA-R-1402, CA-R-1429, CA-R-1375, CA-R-1434, CAPRMEDIO-META-REQU-619, CAPRMEDIO-META-REQU-675, **and** CAPRMEDIO-META-REQU-688. these references are seeds, **not** a fixed complete list. resolve their exact current source Carriers; duplicate IDs require path-bound evidence rather than an arbitrary match. use existing reviews as leads, **not** as accepted dispositions.

record a reproducible source frontier **and** exclusions. changes **after** that frontier require a delta review **before** closure. this Epic produces review evidence **and** recommendations **only**; it does **not** move, rewrite, retire, **or** create methodology authority, modify Settings, implement Tools, **or** rebuild Projections.
