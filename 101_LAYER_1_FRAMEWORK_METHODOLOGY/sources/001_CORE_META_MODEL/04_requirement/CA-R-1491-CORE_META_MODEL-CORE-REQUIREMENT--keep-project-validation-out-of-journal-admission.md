---
subjects:
  governs: "Journal"
  depends_on:
    - "Journal/Record"
    - "Artifact/Carrier"
    - "Atom"
    - "Project"
    - "Applicable Methodology"
    - "Atom/Content Role: Evaluation"
version: 6
updated_at: "2026-10-02 23:35:16 +0400"
relations:
  child_of:
    - CA-R-1490
  relates_to:
    - CA-R-1745
atom_id: "CA-R-1491"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Keep Project validation out of Journal admission

## Scope

Journal admission of observable Project events.

## Claim

the Journal **must** preserve observable Project events independently of whether the recorded Project state conforms **to** Applicable Methodology.

- append admission **must** check **only** event **and** storage integrity: readable event structure, required event identity **and** fields, selected digest bindings, safe append access, **and** append-only history.
- Atom-ID grammar, filenames, placement, Properties, Relations, **and** lifecycle conformance belong **to** separate Evaluations **and** their Tools. a failed **or** unresolved conformance check **must not** block recording an **otherwise** intact event.
- preserve observed values **without** silently repairing them. accepted storage **must not** be presented as proof of a conforming Project **or** a correctly performed action.
- later Project changes **must not** prevent recording intact historical observations **or** cause those observations **to** be rebound **to** current state.
- repeated submission of the same Event identity **and** payload **must** be idempotent; conflicting payloads under the same identity **must not** overwrite history.
- unsafe **or** malformed append input **must** fail storage admission **without** losing the pending evidence. this boundary grants no permission **to** mutate the Project **or** bypass Journal access controls.

## Details
