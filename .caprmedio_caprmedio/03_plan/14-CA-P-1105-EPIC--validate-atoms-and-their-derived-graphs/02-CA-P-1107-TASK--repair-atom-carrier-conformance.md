---
atom_id: CA-P-1107
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 99
status: Active
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Atom/Property/Carrier"
  depends_on:
    - "Atom"
    - "Atom/Revision"
    - "Atom/Frontmatter"
    - "Relation"
    - "Tool"
    - "Evaluation"
    - "Project"
version: 1
updated_at: "2026-09-23 22:29:51 +0000"
relations:
  is_decomposition_of:
    - CA-P-1105
  blocks:
    - CA-P-1108
---
# Summary

Repair Atom carrier conformance

## Claim

the AI Agent **must** bring **all** current Project **and** methodology source Atom Carriers within this Epic's corpus boundary into conformance with the validated carrier rules.

## Definition of Done

the Plan is **not** Done **if** a current source Atom lacks a recorded validator result, **or** a carrier finding remains unresolved, **or** a repair loses authoritative information, **or** internal values are guessed from a filename **or** location, **or** the final scan **and** repair record do **not** identify the checked revisions.

## Details

- inventory the corpus **and** capture source revisions before repairs; account for current Atoms, Drafts, historical revisions, projected copies, **and** malformed candidates explicitly.
- run the validator from CA-P-1106; review findings by rule **and** Scope Unit, using governing authority **and** accepted source evidence for corrections.
- restore missing Properties, remove obsolete **or** inadmissible fields, repair structured sections, **and** remove duplicated inverse Relations **only** after preserving their authoritative information. missing source evidence requires Operator resolution, **not** a fabricated value.
- retain Summary identity boundaries, Status-specific rules, legitimate role differences, **and** exact historical revisions. report historical-only findings separately.
- rerun the validator after repairs; record coverage counts, dispositions, remaining findings, **and** exact command/configuration. an unresolved finding blocks completion.
- apply current source authority, including CA-R-1598 **and** CA-D-478–483; do **not** treat an outdated compiled copy as newer authority.
- check Project Principles **before** escalating uncertainty; ask the Operator **if** confidence remains **<99%**. do **not** silently weaken an Evaluation **or** discard a finding **to** pass.
- preserve unrelated work **and** history; follow the current revision, replacement, Summary identity, **and** approval rules.
