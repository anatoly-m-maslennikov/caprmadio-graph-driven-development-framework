---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Claim"
    - "Atom/Author"
    - "Atom/Content Role: Plan/Type: Plan/Assignee"
    - "Atom/Content Role: Plan/Type: Plan/Definition of Done"
    - "Atom/Content Role: Plan/Type: Plan/Details"
    - "Atom/Content Role: Plan/Type: Plan/Label"
    - "Atom/Content Role: Plan/Type: Plan/Subtype"
    - "Atom/Content Role: Plan/Type: Plan/Status"
    - "Atom/Content Role: Plan/Type: Plan/Decomposition"
    - "Hub Atom"
    - "Scope Unit"
    - "Autonomous Confidence Threshold"
version: 4
updated_at: "2026-09-22 23:02:20 +0000"
relations: {"evaluation_for": ["CA-R-1574", "CA-R-1575", "CA-R-1576", "CA-R-1577", "CA-R-1581", "CA-R-1599", "CA-R-1583", "CA-R-1584", "CA-R-1587", "CA-R-1588", "CA-R-1589", "CA-M-306", "CA-D-470"]}
---
# Summary

Validate common Plan authoring

## Claim

the Plan authoring Evaluation **must** reject **any** Plan that violates the common model.

### cases

- accept a standalone file-backed Plan, a file-backed Hub with decomposed work **and** an optional directory, **and** a Plan with both own work **and** decomposition. reject a folder-only Plan.
- reject a Summary-only Plan with no own work **and** no decomposition; do **not** complete it by an empty all-of test.
- require **=1** Claim **and** effective Author; require **=1** effective Assignee for own work, but **not** for a pure Hub.
- require **`=1`** observable, decidable Definition of Done **in** **every** Plan Markdown file, including a pure Hub. reject its absence.
- accept an atomic **or** explicitly grouped composite falsification expression; reject ambiguity **or** Details that introduce independent work **or** another completion claim.
- mark Done **only** **when** own work is complete, **all** directly decomposed Plans are Done, **and** its falsification expression is false. reject Canceled **or** Archived decomposition as completed work.
- change **only** the Label among Version, Objective, Epic, Task, **and** Subtask: authoring admission **and** completion **must** remain unchanged. reject treating those Labels as authoring Subtypes.
- select the owning Scope Unit as the default Claim Target Scope Unit during authoring regardless of Hub nesting, **and** require the resolved value inside the Atom; preserve a permitted different target **and** narrower Claim restrictions. reject an ancestor target **or** **any** Hub substituted as a Scope Unit target.
- accept inherited confidence values **without** copied overrides; reject an unresolved effective value **before** autonomous execution.

report the exact Plan identity **and** failed rule; a Label **must not** waive the failure.
