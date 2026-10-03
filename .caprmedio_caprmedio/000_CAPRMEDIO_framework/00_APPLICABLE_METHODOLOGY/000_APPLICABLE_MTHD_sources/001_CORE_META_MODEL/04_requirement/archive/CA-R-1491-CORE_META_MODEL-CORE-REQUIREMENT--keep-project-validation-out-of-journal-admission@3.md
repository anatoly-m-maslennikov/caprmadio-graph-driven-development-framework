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
version: 3
updated_at: "2026-09-16 21:24:29 +0000"
relations:
  child_of:
    - CA-R-1490
  relates_to:
    - CAPRMEDIO-META-REQU-656
---
# Keep Project validation out of Journal admission

the Journal **must** preserve observable Project events independently of whether the recorded Project state conforms **to** Applicable Methodology.

- append admission **must** check **only** event **and** storage integrity: readable event structure, required event identity **and** fields, selected digest bindings, safe append access, **and** append-only history.
- Atom-ID grammar, filenames, placement, Properties, Relations, **and** lifecycle conformance belong **to** separate Evaluations **and** their Tools. a failed **or** unresolved conformance check **must not** block recording an **otherwise** intact event.
- preserve observed values **without** silently repairing them. accepted storage **must not** be presented as proof of a conforming Project **or** a correctly performed action.
- later Project changes **must not** prevent recording intact historical observations **or** cause those observations **to** be rebound **to** current state.
- repeated submission of the same Event identity **and** payload **must** be idempotent; conflicting payloads under the same identity **must not** overwrite history.
- unsafe **or** malformed append input **must** fail storage admission **without** losing the pending evidence. this boundary grants no permission **to** mutate the Project **or** bypass Journal access controls.
