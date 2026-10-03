---
subjects:
  governs: "Workflow"
  depends_on:
    - "Step"
    - "Action"
    - "Atom/Content Role: Operations/Type: Workflow"
    - "Atom/Content Role: Operations/Type: Step"
    - "Workflow/Relation Kind: On Result"
version: 2
updated_at: "2026-09-21 00:57:42 +0000"
relations: {"relates_to": ["CA-R-1508", "CA-R-1509", "CA-R-1513", "CA-R-1563", "CA-R-1569"]}
---
# Keep Workflow graphs separate from Step bindings

a Workflow Atom **must** own **only** its graph scheme: Step references, typed directed Relations, entry points, transition conditions, **and** terminal outcomes.

- the referenced Step Atoms own Action references, parameters, **and** input bindings.
- reusable Action Atoms own Action behavior.
- the graph **must not** independently repeat those Step bindings **or** Action definitions; folder nesting **and** file order **must not** replace its declared control flow.
