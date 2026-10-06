---
subjects:
  governs: "Workflow"
  depends_on:
    - "Entity"
    - "Atom"
    - "Atom/Content Role"
    - "Type"
    - "Status"
    - "Scope Unit"
    - "Atom Collection"
    - "Carrier"
version: 2
updated_at: "2026-09-18 21:23:47 +0000"
relations: {"evaluation_for": ["CA-R-1521"]}
---
# Validate lifecycle Workflow adaptability

the Evaluation **must** check that a status-change Workflow follows the target Entity's applicable model under CA-R-1521.

- supply **`=2`** applicable status models with different admitted values, including a newly admitted value absent from the original model; the same Workflow definition **must** support their admitted transitions.
- specialize an Atom's model by Content Role **and** Type; checking **only** a universal Atom value list fails.
- supply an applicable Scope Unit **or** Atom Collection model; admit its valid change **without** imposing an Atom lifecycle.
- request an unknown value, a prohibited transition, **or** a change **without** a defined model: reject **without** inventing a value **or** bypassing required Carrier behavior.
- supply a model requiring an unsupported capability: require an explicit limitation rather than a false pass.

these cases validate the methodology definition; an executor requires separate Implementation checks.
