---
cce_version: cce_1
cce_form: method
subjects:
  governs: "Confidence Threshold/resolution"
  depends_on:
    - "Atom/Content Role: Plan/Type: Objective"
    - "Confidence Threshold"
    - "Operator"
    - "Atom/Content Role: Plan/Type: Task"
    - "Epic"
    - "Framework Instance Settings"
    - "Property"
    - "AI Agent"
version: 3
updated_at: "2026-09-16 14:01:24 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
    - "CA-R-1428"
---
# Resolve confidence thresholds by source precedence

**to** resolve an effective Confidence Threshold for a decision **or** action, an AI Agent **must** perform **all** of:

1. identify the confidence decision **and** context **to** which the threshold applies.
2. inspect applicable sources **in** this precedence: direct Operator input, an explicit value on the Task, the nearest enclosing Epic with an explicit value, **and** the Framework Instance Settings default. resolve an Epic value from the active Objective Atom that targets that Epic under CA-D-273, **not** from the Objective Carrier's containing folder. **when** the Epic has no active Objective **or** the requested override field is absent, inspect its enclosing Epics from nearest **to** farthest; another explicit field does **not** block inheritance of the omitted field. during that Epic lookup, multiple active Objectives **or** invalid override metadata require Operator disposition **without** silently falling through.
3. use the first applicable explicit value; **if** no source supplies a value **or** the selected source is invalid **or** ambiguous, **then** request Operator disposition **before** the affected autonomous action **without** inventing a value **or** silently selecting a lower-precedence source.
4. apply direct Operator input **only** within its stated context; do **not** change unrelated decisions, Tasks, Epics, **or** Settings.
5. do **not** copy an inherited value into a Task **or** Epic override. preserve an explicitly selected override as explicit **when** its value **`=`** the currently inherited value, because later changes **to** the inherited source **must not** silently change that explicit selection.
